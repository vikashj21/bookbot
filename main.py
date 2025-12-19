from stats import count_words, num_occurences
import sys

def get_book_text(filepath):
    print("Analyzing book found at " + filepath)
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    text = get_book_text(book_path)
    # text = get_book_text('books/frankenstein.txt')
    num_words = count_words(text)
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    occurences = num_occurences(text)

    print("--------- Character Count -------")
    for char, count in sorted(occurences.items(), key=lambda kv: kv[1], reverse=True):
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()    