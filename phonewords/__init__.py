__words_cache = None

KEYPAD = {
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ"
}

KEYPAD_INVERSE = {letter: number for number, letters in KEYPAD.items() for letter in letters}

def spell(number):
    """
    Generates and returns a simple mapping, containing single-digit strings as keys and lists of characters as values.
    Every mapping key corresponds to a digit in the provided telephone number and every corresponding
    mapping value represents the set of letters on the telephone keypad button corresponding to that digit.

    Digits that have no corresponding letters, as well as non-digits, are mapped to themselves in the returned dict.
    """
    return {digit: list(KEYPAD.get(digit, digit)) for digit in number}

def spell_all(number):
    """
    Generates and returns a list, containing the exhaustive set of all strings that can be created using the 
    corresponding letters on the telephone keypad.

    Digits that have no corresponding letters, as well as non-digits, are treated verbatim when constructing these strings.
    """

    candidates = [list(KEYPAD.get(digit, digit)) for digit in number]

    result = [""]

    for s in candidates:
        new_result = []
        for r in result:
            for c in s:
                new_result.append(r + c)
        result = new_result

    return result

def spell_dict(number):
    """
    Identical to spell_all, except the returned list is filtered to only contain valid words,
    as included in /usr/share/dict/words.

    The first call to this function reads in /usr/share/dict/words and caches it in the module.
    Subsequent calls read from this cached list instead.
    """
    global __words_cache

    if not __words_cache: # load words from /usr/share/dict/words if we need to
        with open('/usr/share/dict/words', 'r') as fp:
            __words_cache = set(word.strip().upper() for word in fp)

    return [word for word in spell_all(number) if word in __words_cache]


def digitize(word):
    """
    Generates and returns a string containing the telephone keypad digits corresponding to
    each letter in the input string.

    Characters in the input string that are not letters are inserted verbatim in the output string.
    """
    return "".join(KEYPAD_INVERSE.get(letter, letter) for letter in word)
