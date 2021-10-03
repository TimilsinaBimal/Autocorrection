from utils import process_data, get_probs, get_corrections
import os

BASE_DIR = 'data/'


def prepare_vocab():
    vocab = []
    folders = os.listdir(BASE_DIR)
    for folder in folders:
        folder_path = os.path.join(BASE_DIR, folder)
        files = os.listdir(folder_path)
        for file in files:
            file_name = os.path.join(folder_path, file)
            vocab += process_data(file_name)

    return vocab


def main():
    vocab = prepare_vocab()
    probs = get_probs(vocab)
    word = input("Enter the word you want suggestions for: ")
    suggestions = int(input("Enter the number of suggestions you want: "))
    tmp_corrections = get_corrections(
        word, probs, vocab, suggestions, verbose=True)
    for i, word_prob in enumerate(tmp_corrections):
        print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.6f}")


if __name__ == "__main__":
    main()
