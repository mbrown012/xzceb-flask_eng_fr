import unittest

from translator import english_to_french, french_to_english

class testEnglishToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Hello'),'Hello')

class testFrenchToEnglish(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')

unittest.main()
