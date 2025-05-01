from stats import get_num_words, count_chars, sort_words
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)
    char_count = count_chars(book_text)
    nice_report = sort_words(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in nice_report:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():  # Check if it's an alphabetical character
            print(f"{char}: {count}")

    print("============= END ===============")


main()