# BookTrack — Project Brief

## 1. Project Idea & Feature List

**Project Idea:** BookTrack is a Python terminal program. The user searches for
a real book via the Open Library API, picks a book from the results, adds it
to their personal library, tracks their reading progress, rates completed
books, and reviews their reading history. All data is stored locally in a
JSON file.

**Feature List:**
- Search for a book by title or author via Open Library API.
- Add a book to the library with a status: Want to Read, Reading, or Completed.
- Track reading progress by current page (with percentage calculation).
- Rate completed books from 1 to 5.
- View favorite books (completed + rated 4 or 5), sorted by rating.
- View a reading summary (totals per status + average rating).
- Persist all personal library data in `data/library.json`.

## 2. Flowchart (Program Path)
Start -> Main Menu -> Search Book -> Show Results -> Choose Book -> Choose Status
-> Save to JSON -> View / Update / Rate -> Exit
(after every action, return to Main Menu)

## 3. Functions Plan

| Function | Responsibility |
|---|---|
| `main()` | Runs the main menu loop and connects all parts of the program. |
| `search_books(query)` | Searches Open Library and returns the results. |
| `load_library()` | Reads the library from `library.json`. |
| `save_library(library)` | Saves changes to `library.json`. |
| `calculate_progress(current, total)` | Calculates the reading progress percentage and validates the page. |
| `get_favorite_books(library)` | Filters books rated 4 or 5 and sorts them from highest to lowest. |
| `add_to_library(library, book, status)` | Adds a new book to the library and prevents duplicates. |
| `is_duplicate(library, title)` | Checks if a book already exists in the library. |
| `display_search_results(results)` | Displays search results in a numbered list. |

## 4. Team Split

| Member | Responsibility |
|---|---|
| Hiba Thanaa | Project structure setup, Open Library API integration (`search_books`), core logic (`calculate_progress`, `is_duplicate`, `get_favorite_books`, `add_to_library`), main CLI menu (`main.py`), pytest unit tests, README, and final testing/debugging of the whole program. |
| Ayham Abd Aljabbar | Implemented the library storage module (`load_library`, `save_library` in `storage.py`), helped write and refine the `display_search_results` function, reviewed the flowchart and requirements, and helped prepare the presentation slides and demo video script. |