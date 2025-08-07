import sys
from stats import word_count, char_count, char_count_sorted

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    path = sys.argv[1]
    frank = get_book_text(path)
    num_words = word_count(frank)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    cc_rep = char_count_sorted(char_count(frank))
    for item in cc_rep:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
if __name__ == "__main__" and len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
