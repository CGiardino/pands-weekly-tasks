# Count the number of 'e's in an input text file
# Ref to check the mimetypes https://docs.python.org/3/library/mimetypes.html
# Author: Carmine Giardino
import mimetypes
import os.path

LETTER_TO_COUNT = 'e'
while True:
    filename = input(f"Insert the text filename path to count the total number of '{LETTER_TO_COUNT}': ")
    if os.path.exists(filename):
        if not os.access(filename, os.R_OK):
            print("The file is not readable")
        else:
            mime_type, _ = mimetypes.guess_type(filename)
            if mime_type and mime_type.startswith("text"):
                break
            else:
                print("The file needs to be a text file")
    else:
        print(f"Filename '{filename}' does not exist. Please enter a valid filename")

def count_es_in_file(filename_to_analyze: str, letter_to_count: str) -> int:
    count = 0
    try:
        with open(filename_to_analyze, 'rt') as f:
            for line in f.read():
                count += line.count(letter_to_count)
            return count
    except Exception as e:
        #just in case other exceptions arise or the permissions changed whilst running the program
        print(f"Error reading file: {e}")
        exit(126)

count_es = count_es_in_file(filename, LETTER_TO_COUNT)
print(f"The total number of '{LETTER_TO_COUNT}' is {count_es}")



