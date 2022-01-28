from cipher.caesar_cipher import caesar_cipher
from cipher.morse import text_from_morse, text_to_morse
from cipher.pig_latin import piglatinize, depiglatinize

# Cipher tests
# Logically, a decrypted text must be the same as it was before encryption.


def test_caesar_cipher() -> bool:
    t = "This is a test!"

    t_cc = caesar_cipher(t, 10)

    return caesar_cipher(t_cc, -10) == t


def test_morse() -> bool:
    t = "This is a test!"

    t_morse = text_to_morse(t)

    return text_from_morse(t_morse) == t.upper()


def test_pig_latin() -> bool:
    t = "This is a test!"

    t_pl = piglatinize(t)

    return depiglatinize(t_pl) == t


if __name__ == '__main__':
    test_pig_latin()

    print(
        f"Caesar Cipher: {'OK' if test_caesar_cipher() else 'FAILED'}\n"
        f"Morse Code: {'OK' if test_morse() else 'FAILED'}\n"
        f"Pig Latin: {'OK' if test_pig_latin() else 'FAILED'}"
    )
