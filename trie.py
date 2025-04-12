
class Trie:
    """
    A radix tree implementation.
    """
    letter: str
    children: list['Trie']
    end: bool  # if its end of word or not

    def __init__(self, letter: str, end: bool = False):
        self.letter = letter
        self.children = []
        self.end = end

    def append(self, letter: str, end: bool = False):
        """
        Adds a letter as a child to the current tree.
        """
        self.children.append(Trie(letter, end=end))

    def _add_child(self, node: 'Trie'):
        self.children.append(node)

    def __contains__(self, letter: str) -> bool:
        """
        Checks if the specified `letter` is a children, ignoring accents
        """
        return letter in { child.letter for child in self.children }

    def __str__(self) -> str:
        return str(self.to_list())

    def __repr__(self) -> str:
        return self.__str__()

    def __getitem__(self, letter: str):
        for child in self.children:
            if child.letter == letter:
                return child

        raise IndexError(f"'{letter}' not found in children")

    def pretty_print(self, indent=0):
        head, children = self.to_list()

        # TODO
        # ├── c
        # │   ├── a
        # │   │   ├── c
        # │   │   └── í

        print(" " * indent, end="")
        print(head)

        for c in children:
            c.pretty_print(indent + 2)


    def to_list(self) -> list:
        return [self.letter + ("*" if self.end else ""), [*self.children]]

    def is_end(self) -> bool:
        """
        Checks if this tree is an end of word
        """
        return self.end or len(self.children) == 0

    @staticmethod
    def from_str(repr: str) -> 'Trie':
        return Trie.from_list(eval(repr))  # esto es pelín feo, pero 🤫

    @staticmethod
    def from_list(repr: list) -> 'Trie':
        letter, children = repr

        end = False
        if letter.endswith("*"):
            end = True
            letter = letter.removesuffix("*")


        trie = Trie(letter, end)

        for node in children:
            trie._add_child(Trie.from_list(node))

        return trie



if __name__ == "__main__":
    a = Trie("a", end=True)
    a.append("d")
    a.append("a", end=True)

    print(a)


    print(Trie.from_str(str(a)))



