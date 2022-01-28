from string import ascii_lowercase, ascii_uppercase


def caesar_cipher(text: str, key: int) -> str:
    """
    One of the simplest encryption techniques, the Caesar cipher was created by
    Julius Caesar to encrypt messages of high military importance.

    The function receives the text to be encrypted and a shift key. Then, every
    character in the text is shifted by the amount of positions specified by the
    key. For example: the letter A, with a shift key of 3, becomes the letter D,
    which is 3 positions after it.

    The same function can be used to encrypt and decrypt the text.
    """
    new_text = []

    for c in text:
        if c in ascii_lowercase:
            index = (ascii_lowercase.index(c) + key) % 26
            new_text.append(ascii_lowercase[index])

        elif c in ascii_uppercase:
            index = (ascii_uppercase.index(c) + key) % 26
            new_text.append(ascii_uppercase[index])

        else:
            new_text.append(c)

    return "".join(new_text)