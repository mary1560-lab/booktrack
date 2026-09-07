from src.api import search_books
from src.storage import load_library, save_library
from src.logic import (
    display_search_results,
    is_duplicate,
    calculate_progress,
    get_favorite_books,
    add_to_library
)

STATUS_MAP = {
    "1": "want_to_read",
    "2": "reading",
    "3": "completed"
}

STATUS_LABELS = {
    "want_to_read": "Want to Read",
    "reading": "Reading",
    "completed": "Completed"
}


def print_menu():
    print("\n========== BOOKTRACK ==========")
    print("1. Search for a Book")
    print("2. My Library")
    print("3. Update Reading Progress")
    print("4. Rate a Completed Book")
    print("5. Favorite Books")
    print("6. Reading Summary")
    print("7. Exit")
    print("================================")


def search_menu(library):
    query = input("Enter a book title or author: ")
    results = search_books(query)
    display_search_results(results)

    if not results:
        return

    choice = input("Choose a book number to add it (or press Enter to skip): ").strip()
    if choice == "":
        return

    if not choice.isdigit() or not (1 <= int(choice) <= len(results)):
        print("Invalid choice.")
        return

    selected_book = results[int(choice) - 1]

    print("\nChoose the book status:")
    print("1. Want to Read")
    print("2. Reading")
    print("3. Completed")
    status_choice = input("Your choice: ").strip()

    if status_choice not in STATUS_MAP:
        print("Invalid status choice.")
        return

    status = STATUS_MAP[status_choice]
    added = add_to_library(library, selected_book, status)
    if added:
        save_library(library)


def view_library(library):
    if not library:
        print("Your library is currently empty.")
        return

    print("\n===== My Library =====")
    for index, book in enumerate(library, start=1):
        status_label = STATUS_LABELS.get(book["status"], book["status"])
        rating = book["rating"] if book["rating"] else "-"
        print(f"{index}. {book['title']} - {book['author']} "
              f"| Status: {status_label} | Rating: {rating}")
    print("=======================\n")


def update_reading_progress(library):
    reading_books = [b for b in library if b["status"] == "reading"]

    if not reading_books:
        print("There are no books currently being read.")
        return

    print("\nBooks currently being read:")
    for index, book in enumerate(reading_books, start=1):
        print(f"{index}. {book['title']} (Current page: {book['current_page']}/{book['pages']})")

    choice = input("Choose a book number: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(reading_books)):
        print("Invalid choice.")
        return

    book = reading_books[int(choice) - 1]
    new_page = input(f"Enter current page (out of {book['pages']}): ").strip()

    percentage = calculate_progress(new_page, book["pages"])
    if percentage is None:
        return

    book["current_page"] = int(new_page)
    save_library(library)
    print(f"Progress updated: {percentage}% of the book completed.")


def rate_completed_book(library):
    completed_books = [b for b in library if b["status"] == "completed"]

    if not completed_books:
        print("There are no completed books to rate.")
        return

    print("\nCompleted books:")
    for index, book in enumerate(completed_books, start=1):
        current_rating = book["rating"] if book["rating"] else "-"
        print(f"{index}. {book['title']} (Current rating: {current_rating})")

    choice = input("Choose a book number: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(completed_books)):
        print("Invalid choice.")
        return

    book = completed_books[int(choice) - 1]
    rating_input = input("Enter a rating from 1 to 5: ").strip()

    if not rating_input.isdigit() or not (1 <= int(rating_input) <= 5):
        print("Rating must be a whole number from 1 to 5.")
        return

    book["rating"] = int(rating_input)
    save_library(library)
    print(f"'{book['title']}' rated {rating_input} stars.")


def show_favorite_books(library):
    favorites = get_favorite_books(library)

    if not favorites:
        print("No favorite books yet (must be completed and rated 4 or 5).")
        return

    print("\n===== Favorite Books =====")
    for index, book in enumerate(favorites, start=1):
        print(f"{index}. {book['title']} - {book['author']} | Rating: {book['rating']} stars")
    print("===========================\n")


def reading_summary(library):
    total = len(library)
    want_to_read = len([b for b in library if b["status"] == "want_to_read"])
    reading = len([b for b in library if b["status"] == "reading"])
    completed = len([b for b in library if b["status"] == "completed"])

    rated_books = [b for b in library if b["rating"] is not None]
    average_rating = (
        round(sum(b["rating"] for b in rated_books) / len(rated_books), 1)
        if rated_books else 0
    )

    print("\n===== Reading Summary =====")
    print(f"Total Books: {total}")
    print(f"Want to Read: {want_to_read}")
    print(f"Currently Reading: {reading}")
    print(f"Completed: {completed}")
    print(f"Average Rating: {average_rating}")
    print("============================\n")


def main():
    library = load_library()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            search_menu(library)
        elif choice == "2":
            view_library(library)
        elif choice == "3":
            update_reading_progress(library)
        elif choice == "4":
            rate_completed_book(library)
        elif choice == "5":
            show_favorite_books(library)
        elif choice == "6":
            reading_summary(library)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()