import unittest
import sys
import os
sys.path.append(os.path.abspath('../machinetranslation'))
import translator
class TestStringMethods(unittest.TestCase):

    def test_en_fr(self):
        self.assertEqual(translator.english_to_french('Yes'), 'Oui')
    def test_en_fr2(self):
        self.assertNotEqual(translator.english_to_french('No'), 'Oui')

    def test_fr_en(self):
        self.assertEqual(translator.french_to_english('Oui'), 'Yes')
    def test_fr_en2(self):
        self.assertNotEqual(translator.french_to_english('What?'), 'Yes')

if __name__ == '__main__':
    unittest.main()