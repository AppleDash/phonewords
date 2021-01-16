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
    return {digit: list(KEYPAD.get(digit, digit)) for digit in number}

def spell_all(number):
    candidates = [list(KEYPAD.get(digit, digit)) for digit in number]

    result = [""]
    
    for s in candidates:
        new_result = []
        for c in s:
            for r in result:
                new_result.append(r + c)
        result = new_result

    return result

def digitize(word):
    return "".join(KEYPAD_INVERSE.get(letter, letter) for letter in word)
