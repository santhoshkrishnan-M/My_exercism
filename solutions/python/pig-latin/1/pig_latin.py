def translate(text):
    vowels = "aeiou"

    def convert(word):
      
        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            return word + "ay"

        i = 0
        while True:
           
            if word[i:i+2] == "qu":
                i += 2
                break

            if word[i] == "y" and i != 0:
                break

            if word[i] in vowels:
                break

            i += 1

        return word[i:] + word[:i] + "ay"

    return " ".join(convert(word) for word in text.split())