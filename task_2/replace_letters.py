LETTERS_MAPPING = {
    "a": "z", "b": "e", "c": "e", "d": "e", "e": "d", "f": "i", "g": "i",
    "h": "i", "i": "h", "j": "o", "k": "o", "l": "o", "m": "o", "n": "o",
    "o": "n", "p": "u", "q": "u", "r": "u", "s": "u", "t": "u", "u": "t",
    "v": "a", "w": "a", "x": "a", "y": "a", "z": "a"
}


def replace_letters(word: str) -> str:
    result = ""

    for letter in word:
        if letter not in LETTERS_MAPPING:
            raise ValueError(f"{letter} is not the lowercase letter")

        result += LETTERS_MAPPING[letter]

    return result


if __name__ == "__main__":
    word_1 = "cat"
    word_2 = "abcdtuvwxyz"

    replaced_word_1 = "ezu"
    replaced_word_2 = "zeeeutaaaaa"

    assert replace_letters(word_1) == replaced_word_1
    assert replace_letters(word_2) == replaced_word_2
