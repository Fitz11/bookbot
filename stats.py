def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(filepath):
    print("----------- Word Count ----------")
    book_text = get_book_text(filepath)
    words = len(book_text.strip().split())
    print(f"Found {words} total words")

def sort_dict(dic):
    return dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

def get_num_characters(filepath):
    print("----------- Character Count ----------")
    text = get_book_text(filepath)
    text = text.lower()
    charlist = {}
    for char in text:
        val = charlist.get(char)
        if val == None:
            charlist.update({char: 1})
        else:
            charlist.update({char: val+1})
    sorted_chars = sort_dict(charlist)
    for key in sorted_chars:
        if key.isalpha():
            print(f"{key}: {sorted_chars.get(key)}")

