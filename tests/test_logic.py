import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.logic import (
    calculate_progress,
    is_duplicate,
    get_favorite_books,
    add_to_library,
    display_search_results
)


def test_calculate_progress_normal_case():
    """Progress should be calculated correctly for valid input."""
    result = calculate_progress(50, 100)
    assert result == 50.0


def test_calculate_progress_current_greater_than_total():
    """Should return None when current page exceeds total pages."""
    result = calculate_progress(150, 100)
    assert result is None


def test_calculate_progress_invalid_numbers():
    """Should return None when input is not a valid number."""
    result = calculate_progress("abc", 100)
    assert result is None


def test_calculate_progress_negative_current():
    """Should return None when current page is negative."""
    result = calculate_progress(-5, 100)
    assert result is None


def test_is_duplicate_found():
    """Should detect a duplicate book regardless of letter case."""
    library = [{"title": "Atomic Habits", "author": "James Clear"}]
    assert is_duplicate(library, "atomic habits") is True


def test_is_duplicate_not_found():
    """Should return False when the book is not in the library."""
    library = [{"title": "Atomic Habits", "author": "James Clear"}]
    assert is_duplicate(library, "1984") is False


def test_get_favorite_books_filters_correctly():
    """Should only return completed books rated 4 or 5, sorted descending."""
    library = [
        {"title": "Book A", "status": "completed", "rating": 3},
        {"title": "Book B", "status": "completed", "rating": 5},
        {"title": "Book C", "status": "reading", "rating": 5},
        {"title": "Book D", "status": "completed", "rating": 4},
    ]
    favorites = get_favorite_books(library)
    assert len(favorites) == 2
    assert favorites[0]["title"] == "Book B"
    assert favorites[1]["title"] == "Book D"


def test_add_to_library_success():
    """Should successfully add a new book to an empty library."""
    library = []
    book = {"title": "Dune", "author": "Frank Herbert", "pages": 412}
    result = add_to_library(library, book, "want_to_read")
    assert result is True
    assert len(library) == 1
    assert library[0]["status"] == "want_to_read"


def test_add_to_library_duplicate_rejected():
    """Should reject adding a book that already exists in the library."""
    library = [{"title": "Dune", "author": "Frank Herbert", "pages": 412,
                "status": "reading", "current_page": 0, "rating": None}]
    book = {"title": "Dune", "author": "Frank Herbert", "pages": 412}
    result = add_to_library(library, book, "want_to_read")
    assert result is False
    assert len(library) == 1