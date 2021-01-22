import argparse
import phonewords

def _main():
    parser = argparse.ArgumentParser(description='Convert between phone keypad numbers and letters.')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--spell', '-s', help='Generate a mapping of each digit in the input string to corresponding phone letters.', action='store_const', dest='operation', const='spell')
    group.add_argument('--spell-all', '-S', help='Generate an exhaustive list of all strings that can be spelled with the input string of digits.', action='store_const', dest='operation', const='spell_all')
    group.add_argument('--spell-dict', '-D', help='Like --spell-all, but filtered on /usr/share/dict/words.', action='store_const', dest='operation', const='spell_dict')
    group.add_argument('--digitize', '-d', help='Generate an output string with each letter in the input replaced with the corresponding phone digit.', action='store_const', dest='operation', const='digitize')

    parser.add_argument('input', help='The input string to perform the requested operation on.')

    args = parser.parse_args()

    result = getattr(phonewords, args.operation)(args.input)

    if type(result) is list:
        for item in result:
            print(item)
    elif type(result) is dict:
        for k, v in result.items():
            print('{} {}'.format(k, " ".join(v)))
    else:
        print(result)

if __name__ == '__main__':
    _main()
