def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words_with_prefix = [prefix + word for word in vocab_words[1:]]
    return " :: ".join([prefix] + words_with_prefix)


def remove_suffix_ness(word):
    root = word[:-4]  # remove 'ness'
    if root.endswith("i"):
        root = root[:-1] + "y"
    return root


def adjective_to_verb(sentence, index):
    words = sentence.replace(".", "").split()
    return words[index] + "en"
