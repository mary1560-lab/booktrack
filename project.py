"""
BookTrack — CS50P Final Project entry point.
Reuses the storage and API modules built for the full application,
and defines the three required custom functions directly here.
"""

from src.storage import load_library, save_library
from src.api import search_books


def calculate_progress(current, total):
    """
    Calculates reading progress percentage and validates the values.
    Returns a percentage (float) or None if the values are invalid.
    """
    try:
        current = int(current)
        total = int(total)
    except (ValueError, TypeError):
        return None

    if current < 0:
        return None
    if total <= 0:
        return None
    if current > total:
        return None

    return round((current / total) * 100, 1)


def is_duplicate(library, title):
    """
    Checks whether a book already exists in the library (case-insensitive).
    Returns True if it's a duplicate, False otherwise.
    """
    for book in library:
        if book["title"].strip().lower() == title.strip().lower():
            return True
    return False


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


def main():
    library = load_library()

    while True:
        print("\n========== BOOKTRACK ==========")
        print("1. Search for a Book")
        print("2. My Library")
        print("3. Check Reading Progress")
        print("4. Favorite Books")
        print("5. Exit")
        print("================================")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            query = input("Enter a book title or author: ")
            results = search_books(query)
            for index, book in enumerate(results, start=1):
                print(f"{index}. {book['title']} - {book['author']} ({book['first_publish_year']})")

        elif choice == "2":
            if not library:
                print("Your library is empty.")
            for book in library:
                print(f"{book['title']} - {book['author']} | Status: {book['status']}")

        elif choice == "3":
            for book in library:
                if book["status"] == "reading":
                    progress = calculate_progress(book["current_page"], book["pages"])
                    print(f"{book['title']}: {progress}% complete" if progress is not None else f"{book['title']}: not enough data")

        elif choice == "4":
            favorites = get_favorite_books(library)
            if not favorites:
                print("No favorite books yet.")
            for book in favorites:
                print(f"{book['title']} - Rating: {book['rating']}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()