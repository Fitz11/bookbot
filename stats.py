def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(filepath):
    # print(get_book_text('books/frankenstein.txt'))
    book_text = get_book_text(filepath)
    words = book_text.strip().split()
    print(f"{len(words)} words found in the document")
    return len(words)

def get_num_characters(filepath):
    text = get_book_text(filepath)
    text = text.lower()
    charlist = {}
    for char in text:
        val = charlist.get(char)
        if val == None:
            charlist.update({char: 1})
        else:
            charlist.update({char: val+1})
    print(charlist)
