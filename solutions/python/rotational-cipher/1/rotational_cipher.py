def rotate(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = key % 26  # handle keys like 26, 52, etc.

            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            result += new_char
        else:
            # keep spaces, punctuation unchanged
            result += char

    return result