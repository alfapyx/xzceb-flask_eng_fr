"""
Test for the final project
"""
import unittest
from machinetranslation import translator as tr


class TestFrenchToEnglish(unittest.TestCase):
    """
    Test for the f2e function
    """
    def test_for_null_input(self):
        """
        Test if an empty string is returned
        """
        self.assertEqual("", tr.french_to_english(""))

    def test_for_translation(self):
        """
        Test if a proper translation is returned
        """
        self.assertEqual("Hello", tr.french_to_english("Bonjour"))


class TestEnglishToFrench(unittest.TestCase):
    """
    Test for the e2f function
    """
    def test_for_null_input(self):
        """
        Test if an empty string is returned
        """
        self.assertEqual("", tr.english_to_french(""))

    def test_for_translation(self):
        """
        Test if a proper translation is returned
        """
        self.assertEqual("Bonjour", tr.english_to_french("Hello"))


if __name__ == "__main__":
    unittest.main()
