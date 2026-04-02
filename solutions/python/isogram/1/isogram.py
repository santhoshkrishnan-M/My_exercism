def is_isogram(word):
    word = word.lower()
    seen = set()

    for char in word:
        if char == " " or char == "-":
            continue
        if char in seen:
            return False
        seen.add(char)

    return True
