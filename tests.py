import unittest

import phonewords

class PhoneWordsTest(unittest.TestCase):
    def test_digitize(self):
        self.assertEqual(phonewords.digitize('HAT'), '428')
        self.assertEqual(phonewords.digitize('123'), '123')
        self.assertEqual(phonewords.digitize('1AB'), '122')
        self.assertEqual(phonewords.digitize('1-877-HATBOWL'), '1-877-4282695')

    def test_spell(self):
        self.assertEqual(
            phonewords.spell('123'),
            {'1': ['1'], '2': ['A', 'B', 'C'], '3': ['D', 'E', 'F']}
        )

    def test_spell_all(self):
        self.assertEqual(
            set(phonewords.spell_all('123')),
            {'1AD', '1AE', '1AF', '1BD', '1BE', '1BF', '1CD', '1CE', '1CF'}
        )

if __name__ == '__main__':
    unittest.main()
