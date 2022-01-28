MORSE_ALPHABET = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-...',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '!': '-.-.--', '/': '--..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', 
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', 
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', '0': '-----', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ''
}


def to_morse(char: str, alphabet: dict = MORSE_ALPHABET) -> str:
    """
    Translates an individual character into it's morse code equivalent.
    """
    char = str(char)

    return alphabet[char]


def from_morse(char: str, alphabet: dict = None) -> str:
    """
    Translates an individual morse code character into it's Latin alphabet
    equivalent.
    """
    if alphabet == None:
        alphabet = dict(zip(MORSE_ALPHABET.values(), MORSE_ALPHABET.keys()))

    char = str(char)

    return alphabet[char]


def text_to_morse(text: str) -> str:
    """
    Converts text into morse code.
    """
    text = text.upper()
    text = list(text)

    for i in range(len(text)):
        text[i] = to_morse(text[i])

    return ' '.join(text)


def text_from_morse(text: str) -> str:
    """
    Translates text from morse code.
    """
    alphabet = dict(zip(MORSE_ALPHABET.values(), MORSE_ALPHABET.keys()))

    text = text.split(' ')

    for i in range(len(text)):
        text[i] = from_morse(text[i], alphabet)

    return ''.join(text)