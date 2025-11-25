import sys
from stats import count_words
from stats import count_chars
from stats import sort_chars

def get_book_text(filename):
    with open(filename) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filename = sys.argv[1]
    text = get_book_text(filename)
    num_words = count_words(text)
    sorted_chars = sort_chars(count_chars(text))
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char["char"]}: {char["num"]}")
    print(f"============= END ===============")



main()
