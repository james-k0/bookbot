import sys
from stats import get_num_words, char_breakdown, list_of_dictionaries
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    filepath=sys.argv[1]
    text = text_of(filepath)
    count = get_num_words(text)
    chars_dict = char_breakdown(text)
    chars_list = list_of_dictionaries(chars_dict)
    report(filepath, count, chars_list)


def text_of(filepath):
    with open(filepath) as f:
        return f.read()


def report(filepath,count,chars_list):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------\nFound {count} total words\n--------- Character Count -------")
    for entry in chars_list:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")
main()
