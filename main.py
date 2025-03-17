from stats import get_num_characters, get_num_words

def main():
    print("============ BOOKBOT ============")
    filepath = 'books/frankenstein.txt'
    print(f"Analyzing book found at {filepath}...")
    get_num_words(filepath)
    get_num_characters(filepath)
    print("============= END ===============")

main()
