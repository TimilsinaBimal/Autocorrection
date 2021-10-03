import re
from string_manipulation import Manipulation


def process_data(filepath):
    words = []
    with open(filepath, 'br') as f:
        lines = f.readlines()
    lines = [line.decode() for line in lines]
    sentence = " ".join(lines)
    sentence = sentence.lower()
    words = re.findall(r"\w+", sentence)
    return words


def get_count(word_l):
    word_count_dict = {}
    for word in word_l:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict


def get_probs(vocab):
    word_count_dict = get_count(vocab)
    probs = {}
    total_words = sum(word_count_dict.values())
    for key, value in word_count_dict.items():
        probs[key] = value / total_words
    return probs


# def edit_n_letters(word, n):
#     probable_words = [word]
#     for idx in range(n):
#         for words in probable_words:
#             string = Manipulation(words)
#             probable_words += string.delete_letter()
#             probable_words += string.insert_letter()
#             probable_words += string.replace_letter()
#             probable_words += string.switch_letter()
#             if idx == 0:
#                 probable_words = probable_words[1:]

#     return set(probable_words)


def edit_one_letter(word):
    edit_one_set = set()
    string = Manipulation(word)

    probable_words = string.delete_letter() + string.insert_letter() \
        + string.replace_letter() + string.switch_letter()
    edit_one_set = edit_one_set.union(set(probable_words))
    return edit_one_set


def edit_two_letters(word):
    edit_two_set = set()
    string = Manipulation(word)
    probable_words = string.delete_letter() + string.insert_letter() \
        + string.replace_letter() + string.switch_letter()
    final_words = []
    for words in probable_words:
        string = Manipulation(words)
        final_words = final_words + \
            string.delete_letter() + string.insert_letter() \
            + string.replace_letter() + string.switch_letter()

    edit_two_set = set(final_words)
    return edit_two_set


def get_corrections(word, probs, vocab, n=2, verbose=False):
    suggestions = []
    n_best = []

    if word in vocab:
        org_word = [word]
    else:
        org_word = []
    one_edit_words = [w for w in edit_one_letter(word) if w in vocab]
    two_edit_words = [w for w in edit_two_letters(word) if w in vocab]
    temp_suggestions = org_word or one_edit_words or two_edit_words
    best_words = {w: probs[w] for w in temp_suggestions if w in vocab}
    best_words = dict(sorted(best_words.items(), key=lambda item: item))
    n_best = list(best_words.items())[:n]
    suggestions = [w[0] for w in n_best]

    if verbose:
        print("entered word = ", word, "\nsuggestions = ", suggestions)

    return n_best
