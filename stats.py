# Calculates total word count in 'text' variable
def get_num_words(text):
    words = text.split()
    return len(words)


### Splits into unique words and increments whenever found. Returns a dict.
def get_char_count(text):
    #Create & populate a list with unique characters all lowercase
    unique_char = set()
    for word in text.split():
        for char in word:
            unique_char.add(char.lower())
    #print (f"Unique Char list is:{sorted(unique_char)}")

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list