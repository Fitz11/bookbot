from stats import get_num_characters, get_num_words
import sys

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    if checkarg(args[0]) != True:
        sys.exit(1)
    print("============ BOOKBOT ============")
    filepath = args[0]
    print(f"Analyzing book found at {filepath}...")
    get_num_words(filepath)
    get_num_characters(filepath)
    print("============= END ===============")

def checkarg(arg):
    try:
        open(arg)
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    return True

main()
