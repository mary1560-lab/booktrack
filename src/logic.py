# Core business logic: progress calculation, duplicates, and favorites
def display_search_results(results):
    """
    Displays the search results in a numbered, clear format for the user to choose from.
    """
    if not results:
        print("No results to display.")
        return

    print("\n===== Search Results =====")
    for index, book in enumerate(results, start=1):
        pages_display = book["pages"] if book["pages"] else "N/A"
        print(f"{index}. {book['title']} - {book['author']} "
              f"({book['first_publish_year']}) | Pages: {pages_display}")
    print("===========================\n")


def is_duplicate(library, title):
    """
    Checks whether a book already exists in the personal library (based on title).
    Returns True if duplicated, False otherwise.
    """
    for book in library:
        if book["title"].strip().lower() == title.strip().lower():
            return True
    return False


def calculate_progress(current, total):
    """
    Calculates reading progress percentage and validates the values.
    Returns a percentage (float) or None if values are invalid.
    """
    try:
        current = int(current)
        total = int(total)
    except (ValueError, TypeError):
        print("Please enter valid whole numbers for pages.")
        return None

    if current < 0:
        print("Current page cannot be negative.")
        return None

    if total <= 0:
        print("Total pages value is invalid.")
        return None

    if current > total:
        print("Current page cannot be greater than total pages.")
        return None

    percentage = (current / total) * 100
    return round(percentage, 1)


def get_favorite_books(library):
    """
    Filters completed books rated 4 or 5, sorted from highest to lowest rating.
    """
    favorites = [
        book for book in library
        if book.get("status") == "completed" and book.get("rating") in (4, 5)
    ]
    favorites.sort(key=lambda b: b["rating"], reverse=True)
    return favorites


def add_to_library(library, book, status):
    """
    Adds a new book to the personal library after setting its status.
    Prevents duplicates and sets current_page and rating defaults.
    """
    if is_duplicate(library, book["title"]):
        print(f"'{book['title']}' already exists in your library.")
        return False

    new_book = {
        "title": book["title"],
        "author": book["author"],
        "pages": book["pages"] if book["pages"] else 0,
        "status": status,
        "current_page": 0,
        "rating": None
    }

    library.append(new_book)
    print(f"'{book['title']}' was added to your library with status: {status}")
    return True