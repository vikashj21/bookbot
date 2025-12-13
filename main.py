def get_book_text(filepath):
    print(filepath)
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    return book.split()


def main():
    # get_book_text('books/frankenstein.txt')
    words = count_words(get_book_text('books/frankenstein.txt'))
    print(f"Found {len(words)} total words")

if __name__ == "__main__":
    main()    