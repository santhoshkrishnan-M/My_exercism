def is_pangram(sentence):
    letters = set()

    for char in sentence.lower():
        if char.isalpha():
            letters.add(char)

    if len(letters) == 26:
        return True
    else:
        return False