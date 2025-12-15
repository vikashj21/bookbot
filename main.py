from stats import count_words

def get_book_text(filepath):
    print(filepath)
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    # get_book_text('books/frankenstein.txt')
    num_words = count_words(get_book_text('books/frankenstein.txt'))
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()    