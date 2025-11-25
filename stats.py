def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
            continue
        chars[char] = 1
    return chars

def sort_on(items):
    return(items["num"])

def sort_chars(chars):
    sorted_chars = []
    for char in chars:
        new_char = {}
        new_char["char"] = char
        new_char["num"] = chars[char]
        if char.isalpha():
            sorted_chars.append(new_char)
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
