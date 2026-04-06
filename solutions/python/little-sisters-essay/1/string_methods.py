# 1. Capitalize title
def capitalize_title(title):
    return title.title()


# 2. Check sentence ending
def check_sentence_ending(sentence):
    return sentence.endswith('.')


# 3. Clean up spacing
def clean_up_spacing(sentence):
    return sentence.strip()


# 4. Replace word choice
def replace_word_choice(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)