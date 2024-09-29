chars_dict = {'a': 0,
'b': 0,
'c': 0,
'd': 0,
'e': 0,
'f': 0,
'g': 0,
'h': 0,
'i': 0,
'j': 0,
'k': 0,
'l': 0,
'm': 0,
'n': 0,
'o': 0,
'p': 0,
'q': 0,
'r': 0,
's': 0,
't': 0,
'u': 0,
'v': 0,
'w': 0,
'x': 0,
'y': 0,
'z': 0,
}
def count_words():
    with open('books/frankenstein.txt', 'r') as f:
        data = f.read()
    lines = data.split()
    counter = 0
    for line in lines:
        counter += 1
    return counter

def count_characters():
    total = 0
    with open('books/frankenstein.txt', 'r') as f:
        data = f.read()
    chars = data.lower()
    for char in chars:
        total = total + 1
        if char in chars_dict:
            chars_dict[char] = chars_dict[char] + 1
    print(f"{total} words total")
    for data in chars_dict:
        print(f"The '{data}' character was found {chars_dict[data]} times.")

count_characters()