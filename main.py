with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def count_words(file_contents):
    word_count = len(file_contents.split())
    print(f"{word_count} words found in the document")


def char_count(file_contents):
    char_dict = {}
    for char in file_contents.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    char_list = list(char_dict.items())
    char_list.sort()
    for char, count in char_list:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")


print("--- Begin report of books/frankenstein.txt ---")
count_words(file_contents)
print()
char_count(file_contents)
print("--- End report ---")
