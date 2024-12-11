def main():
  with open("books/frankenstein.txt", encoding="utf-8") as f:
    book = f.read()
    print(book)


main()
