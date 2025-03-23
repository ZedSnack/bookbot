"""Bookbot program for boot.dev"""


import sys
from stats import get_word_count, get_char_counts, print_count_report


def main():
    if len(sys.argv) > 1:
        file_contents = get_book_text(sys.argv[1])
        print("============ BOOKBOT ============\n"
            "Analyzing book found at {sys.argv[1]}...\n"
            "----------- Word Count ----------\n"
            f"Found {get_word_count(file_contents)} total words\n"
            "--------- Character Count -------")
        char_count = get_char_counts(file_contents)
        chars_list = print_count_report(char_count)
        for d in chars_list:
            if d["char"].isalpha() == True:
                print(f"{d["char"]}: {d["count"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents


main()
