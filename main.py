"""One Word for the Boss -- make.fun bounty entry (program/v1).

Bounty: entrants send exactly one word describing their boss. A judge
model compares entries two at a time on how funny the word is, how true
it rings, and how fresh it feels. The program writes that single word
to /output/entry.txt.

Chosen word: "Disappearer"

Why this word won over the other two candidates:
  * Hoverer -- strong and true (the boss hovering over your shoulder),
    but the word itself reads a little awkward and its joke is only
    "he watches you work".
  * Ghoster -- modern and funny, but a ghoster can be anyone (a date,
    a friend); it is less specifically a word about a boss, so it is
    weaker on the judge's first criterion.
  * Disappearer -- the boss who vanishes the moment real work or a
    problem shows up. It is a real noun (one who disappears), it is
    funny on its own, it catches a habit every worker has actually
    met, it is not the first word anyone reaches for, and it travels:
    a disappearing boss is the same joke in a kitchen, a warehouse,
    or an office. The irony lands without any caption: the person
    who is supposed to be in charge is the one you can never find.
    It also beats "Hoverer" on freshness -- "hoverer" is the word a
    thesaurus hands you, while "disappearer" is the word a colleague
    actually repeats at lunch -- and it beats "Ghoster" because it
    can only describe a person who is supposed to be present, which
    is exactly what a boss is.

The program is fully deterministic: the word is a constant in this
file. No network, no randomness, no environment variables, no input
files. It self-checks the gate (UTF-8 text, 1-30 characters, not
only whitespace, a single word with no spaces) before writing.
"""

import os

# The entry: one word, no spaces, well inside the 30-character gate.
WORD = "Disappearer"

OUTPUT_PATH = "/output/entry.txt"

# Gate limits from the bounty rules: 1 to 30 characters, not only
# whitespace, a single word.
MIN_LENGTH = 1
MAX_LENGTH = 30


def check_word(word):
    """Self-check the entry against the bounty gate. Raises on failure."""
    if not isinstance(word, str):
        raise ValueError("entry must be a string")
    if not (MIN_LENGTH <= len(word) <= MAX_LENGTH):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(word))
        )
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if word != word.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no spaces")
    if not word.isalpha():
        raise ValueError("entry must be letters only, no digits or punctuation")
    word.encode("utf-8")  # must be valid UTF-8 text
    return True


def main():
    check_word(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
