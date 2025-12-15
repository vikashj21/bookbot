from stats import count_words, num_occurences

def get_book_text(filepath):
    print(filepath)
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    # get_book_text('books/frankenstein.txt')
    text = get_book_text('books/frankenstein.txt')
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    occurences = num_occurences(text)
    print(occurences)

if __name__ == "__main__":
    main()    