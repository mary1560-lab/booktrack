# BookTrack 📚

A simple command-line Python application that lets you search for real books using the Open Library API, add them to your personal library, track your reading progress, rate completed books, and view your favorites.

## Problem & Idea

Readers often lose track of what they want to read, what they're currently reading, and what they've finished. BookTrack solves this by connecting to a real book database (Open Library) so users don't have to manually type book details, while keeping all personal data (status, progress, ratings) stored locally in a JSON file.

## Target User

Anyone who wants a lightweight, no-signup way to track their personal reading list from the terminal.

## Core Features

- Search for real books via the Open Library API (no API key required).
- Add books to your library with a status: Want to Read, Reading, or Completed.
- Track reading progress by page number, with automatic percentage calculation.
- Rate completed books from 1 to 5.
- View favorite books (completed + rated 4 or 5), sorted by rating.
- View a reading summary (totals per status + average rating).
- All data is saved locally in `data/library.json`.

## Requirements

- Python 3.10+
- Internet connection (for the search feature only)

## Installation & Setup

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd booktrack

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell
# source .venv/bin/activate       # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the program
python main.py
```

## Why `requests`?

We use the `requests` library instead of the built-in `urllib` because it offers a simpler, more readable syntax for making HTTP GET requests and handling errors, which keeps `src/api.py` clean and beginner-friendly.

## Usage Example
========== BOOKTRACK ==========

Search for a Book
My Library
Update Reading Progress
Rate a Completed Book
Favorite Books
Reading Summary
Exit
================================
Enter your choice: 1
Enter a book title or author: atomic habits

===== Search Results =====

Atomic Habits - James Clear (2018) | Pages: 320
...
Choose a book number to add it (or press Enter to skip): 1

Choose the book status:

1-Want to Read
2-Reading
3-Completed
Your choice: 2
'Atomic Habits' was added to your library with status: reading

## Data Structure (`data/library.json`)

```json
{
    "title": "Atomic Habits",
    "author": "James Clear",
    "pages": 320,
    "status": "reading",
    "current_page": 120,
    "rating": null
}
```

## Project Structure
booktrack/
├── main.py # Main menu, connects all parts
├── src/
│ ├── api.py # search_books() - Open Library API integration
│ ├── storage.py # load_library() / save_library() - JSON persistence
│ └── logic.py # progress calculation, favorites, add/validate logic
├── data/
│ └── library.json # Personal library data
├── tests/
│ └── test_logic.py # pytest unit tests
├── docs/ # Project planning documents
├── requirements.txt
└── README.md

## Error Handling Covered

- Book not found in search.
- No internet connection / API failure.
- Duplicate book detection.
- Invalid rating (must be 1-5).
- Current page outside valid range (negative or greater than total pages).
- Corrupted or missing `library.json` file (starts fresh instead of crashing).

## Testing

Run all unit tests with:
```bash
pytest -v
```
9 tests cover progress calculation, duplicate detection, favorites filtering, and adding books.

## Known Limitations

- Page count is not always available from the Open Library API for every book (defaults to 0 in that case).
- No graphical interface; command-line only, by design (per project scope).

## Future Improvements

- Add a simple search history.
- Allow removing/editing books from the library.
- Export reading summary to a text or PDF report.