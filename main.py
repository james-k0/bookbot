def get_book_text(filepath):
    with open(filepath) as f:
        print(f.read())
    f.close()


def main():
    get_book_text("books/frankenstein.txt")

main()

