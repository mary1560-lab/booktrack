from project import calculate_progress, is_duplicate, get_favorite_books


def test_calculate_progress():
    assert calculate_progress(50, 100) == 50.0
    assert calculate_progress(150, 100) is None
    assert calculate_progress("abc", 100) is None
    assert calculate_progress(-5, 100) is None


def test_is_duplicate():
    library = [{"title": "Atomic Habits", "author": "James Clear"}]
    assert is_duplicate(library, "atomic habits") is True
    assert is_duplicate(library, "1984") is False


def test_get_favorite_books():
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