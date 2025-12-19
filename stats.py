def count_words(book):
    return len(book.split())

def num_occurences(text):
    char = text.lower()
    occurences= {}
    for i in char:
        occurences[i] = occurences.get(i, 0) + 1
    return occurences

def sort_on(items):
    return ite