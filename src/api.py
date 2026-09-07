import requests

API_URL = "https://openlibrary.org/search.json"


def search_books(query, limit=5):
    """
    Searches for books in the Open Library API based on a title or author name.
    Returns a list of dicts, each containing: title, author, first_publish_year, pages.
    On connection failure or no results, returns an empty list instead of crashing.
    """
    if not query or not query.strip():
        print("Please enter a valid book title or author name.")
        return []

    params = {"q": query.strip(), "limit": limit}

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"Error: Could not connect to the internet or the API: {error}")
        return []

    data = response.json()
    docs = data.get("docs", [])

    if not docs:
        print("No matching books found.")
        return []

    results = []
    for doc in docs:
        results.append({
            "title": doc.get("title", "Unknown Title"),
            "author": ", ".join(doc.get("author_name", ["Unknown Author"])),
            "first_publish_year": doc.get("first_publish_year", "N/A"),
            "pages": doc.get("number_of_pages_median", None)
        })

    return results
