def get_text(path):
  with open(path, encoding="utf-8") as f:
    book = f.read()
  return book


def num_words(text):
  words = text.split()
  return len(words)


def char_count(text):
  chars = {}
  for c in text.lower():
    _c = c
    if c in chars:
      chars[c] += 1
    else:
      chars[c] = 1

  return chars


def generate_report(path):
  text = get_text(path)
  print(f"--- Begin report of {path} ---")
  print(f"{num_words(text)} words found in the document\n\n")
  char_count_sorted = sorted(char_count(text).items(),
                             key=lambda p: p[1],
                             reverse=True)
  for c, count in char_count_sorted:
    if c.isalpha():
      print(f"The '{c}' character was found {count} times")
  print("--- End report ---")


def main():
  generate_report("books/frankenstein.txt")


main()
