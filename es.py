# Count the number of 'e's in an input text file
# Ref to check the mimetypes https://docs.python.org/3/library/mimetypes.html
# Author: Carmine Giardino

import mimetypes
import os

LETTER_TO_COUNT = 'e'


# Request valid filename
while True:
    filename = input(f"Insert the text filename path to count the total number of '{LETTER_TO_COUNT}': ")

    if not os.path.exists(filename):
        print(f"Filename '{filename}' does not exist. Please enter a valid filename.")
        continue

    if not os.access(filename, os.R_OK):
        print("The file is not readable.")
        continue

    mime_type, _ = mimetypes.guess_type(filename)

    # Accepts text files based on MIME type OR common extensions
    if (mime_type and mime_type.startswith("text")
            or filename.endswith(('.txt', '.log', '.md', '.csv', '.json'))):
        # The file is valid
        break
    else:
        print("The file needs to be a text file.")


def count_es_in_file(filename_to_analyze: str, letter_to_count: str) -> int:
    """Counts occurrences of a specific letter in a text file efficiently."""
    count = 0
    try:
        with open(filename_to_analyze, 'rt', encoding="utf-8") as f:
            for line in f:  # Read line by line
                count += line.count(letter_to_count)
    except Exception as e:
        raise RuntimeError(f"Error reading file '{filename_to_analyze}': {e}")
    return count


# Count 'e' occurrences
try:
    count_es = count_es_in_file(filename, LETTER_TO_COUNT)
    print(f"The total number of '{LETTER_TO_COUNT}' is {count_es}")
except RuntimeError as e:
    print(e)
