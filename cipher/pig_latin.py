def piglatinize(text: str):
    """
    A language game, Pig Latin alters the words of a text by moving the first
    consonant of each word into the end and adding the suffix -ay to the word.

    For example:
    pig -> igpay
    latin -> atinlay

    When words begin with consonant clusters, the whole all the consonants are
    moved:
    smile -> ilesmay

    When the word starts with a vowel, it's just added the suffix -yay:
    example -> exampleyay
    """

    text = text.split(' ')

    for i in range(len(text)):
        word = list(text[i])
        first = word[0]
        word.pop(0)
        word.append(first)
        text[i] = ''.join(word) + 'ay'

    return ' '.join(text)

def depiglatinize(text: str):
    """
    The reverse process to return a piglatinized text back to normal.
    """

    text = text.split(' ')

    for i in range(len(text)):
        word = list(text[i])
        first = word[-3]
        word = word[:-3]
        word.insert(0, first)
        text[i] = ''.join(word)
    
    return ' '.join(text)


if __name__ == '__main__':
    example = piglatinize("This is a Pig Latin phrase")

    print(example)

    example = depiglatinize(example)

    print(example)