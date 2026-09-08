# Handles reading and writing the personal library to/from library.json
import json
import os

DATA_FILE = os.path.join("data", "library.json")


def load_library():
    """
    Reads the personal library from library.json and returns it as a list of dicts.
    If the file doesn't exist or is corrupted, returns an empty list instead of crashing.
    """
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        print("Warning: Could not read the library file. Starting with an empty library.")
        return []


def save_library(library):
    """
    Saves the list of books (library) into library.json in a readable format.
    """
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(library, file, indent=4, ensure_ascii=False)
    except OSError as error:
        print(f"Error: Could not save the library: {error}")