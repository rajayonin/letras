import sys

from trie import Trie
from utils import is_letter, MAX_LETTERS


HELP_TEXT = """
Usage:
    python3 letras.py [LETRAS]
"""


def resolve(letters: list[str], tree: Trie):
    return _resolve(letters, tree, tree.letter, tree.letter)

def _resolve(letters: list[str], tree: Trie, current_prediction: str, best_prediction: str) -> str:
    if tree.is_end():  # end of word
        return current_prediction

    # search through all children nodes
    for node in [ n for n in tree.children if n.letter in letters ]:
        working_set = letters.copy()
        working_set.remove(node.letter)

        if len(new_prediction := _resolve(working_set, node, current_prediction + node.letter, best_prediction)) > len(best_prediction):
            best_prediction = new_prediction

    return best_prediction





if __name__ == "__main__":

    # parse input

    if not 1 < len(sys.argv) < 3:
        sys.exit(HELP_TEXT)

    if sys.argv[1] == "--help":
        print(HELP_TEXT)
        sys.exit()

    letters: list[str] = list(sys.argv[1])

    if not 0 < len(letters) <= MAX_LETTERS:
        sys.exit("Invalid size of input!")

    if not all(is_letter(c) for c in letters):
        sys.exit("Invalid characters found in input!")

    # work

    prediction = letters[0]  # longest predicted word

    # try with different letters
    for radix in set(letters):  # we use set to remove duplicates

        working_set = letters.copy()  # copy that we can manipulate
        working_set.remove(radix)

        # load tree
        try:
            with open(f"trees/{radix}", "r") as fd:
                tree = Trie.from_str(fd.read())
        except FileNotFoundError:
            # tree does not exist
            continue

        # resolve the tree
        new_prediction = resolve(working_set, tree)


        # travel the tree
        # curr = tree
        # for letter in working_set:
        #     if curr.is_leaf():
        #         break

        #     if letter in curr:
        #         new_prediction += letter
        #         working_set.remove(letter)
        #         curr = curr[letter]

        if len(new_prediction) > len(prediction):
            prediction = new_prediction


    print(prediction)




