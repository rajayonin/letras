"""
Generates the Radix trees for each letter, using an input file of words
"""

import sys

from tqdm import tqdm

from trie import Trie
from utils import is_letter, MAX_LETTERS, TRANSLATE_TABLE


HELP_TEXT = """
Usage:
    python3 generate_trees.py [DICTIONARY_FILE]
"""


words: dict[str, Trie] = {}

if __name__ == "__main__":

    # parse input

    if not 1 < len(sys.argv) < 3:
        sys.exit(HELP_TEXT)

    if sys.argv[1] == "--help":
        print(HELP_TEXT)
        sys.exit()

    input_file = sys.argv[1]

    # count number of words
    with open(input_file, "rb") as f:
        num_lines = sum(1 for _ in f)

    # read file
    with open(input_file, "r") as fd:
        for word in tqdm(fd, total=num_lines):
            # clean word
            word = word.lower().translate(TRANSLATE_TABLE).strip()

            # skip useless words
            if not all((is_letter(c) for c in word)) or len(word) > MAX_LETTERS:
                continue

            # update trie with word data

            radix, *rest = word  # separate radix from rest of word
            root = words.get(radix, Trie(radix))  # get root of tree for radix

            curr = root
            for i, letter in enumerate(rest):
                if letter not in curr:
                    curr.append(letter, end=i == len(rest) - 1)

                curr = curr[letter]  # navigate to child node

            # save trie
            words[radix] = root


    # write tree files
    for letter, trie in words.items():
        with open(f"trees/{letter}", "w") as fd:
            fd.write(str(trie))
            # trie.pretty_print()

