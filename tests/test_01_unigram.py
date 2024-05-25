# File: tests/test_01_NLP.py
"""
Authors: Erika García,
Christian Parrish,
Jorge Blanco
"""

import sys
import os
import unittest
from unittest import TestCase

# This is to add the parent directory to the system path in order to access Model.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model import TextProcessor

class TestUnigram(unittest.TestCase):
    
    # Test with a normal sentence containing multiple words
    def test_normal_sentence(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        result = processor.make_unigram("This is a test of the make_unigram method")
        expected = [('This',), ('is',), ('a',), ('test',), ('of',), ('the',), ('make_unigram',), ('method',)]
        assert result == expected, f"Expected {expected}, but got {result}"

    # Test with an empty string
    def test_empty_string(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        result = processor.make_unigram("")
        expected = []
        assert result == expected, f"Expected {expected}, but got {result}"

    # Test with a single word
    def test_single_word(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        result = processor.make_unigram("Word")
        expected = [('Word',)]
        assert result == expected, f"Expected {expected}, but got {result}"
        
    # Test with a sentence containing mixed case words
    def test_mixed_case_words(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        result = processor.make_unigram("ThIs Is A TeSt Of ThE MaKe_UnIgRaM MeThOd")
        expected = [('ThIs',), ('Is',), ('A',), ('TeSt',), ('Of',), ('ThE',), ('MaKe_UnIgRaM',), ('MeThOd',)]
        assert result == expected, f"Expected {expected}, but got {result}"

    # Test with a sentence containing numbers and letters
    def test_sentence_with_numbers_and_letters(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        result = processor.make_unigram("This is a test with numbers 123 and letters")
        expected = [('This',), ('is',), ('a',), ('test',), ('with',), ('numbers',), ('123',), ('and',), ('letters',)]
        assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test with a sentence containing special characters that are not punctuation
    def test_special_characters_not_punctuation(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        result = processor.make_unigram("This is a test with special characters $%& that are not punctuation")
        expected = [('This',), ('is',), ('a',), ('test',), ('with',), ('special',), ('characters',), ('$%&',), ('that',), ('are',), ('not',), ('punctuation',)]
        assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test with a string containing only spaces
    def test_string_containing_only_spaces(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        result = processor.make_unigram("          ")
        expected = []
        assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test with a string containing only punctuation marks
    def test_string_containing_only_punctuation_marks(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        result = processor.make_unigram(".,?!()")
        expected = [('.,?!()',)]
        assert result == expected, f"Expected {expected}, but got {result}"
    # Test with a string that includes newline characters
    def test_string_with_newline_characters(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        result = processor.make_unigram("This is a test\nwith newline characters")
        expected = [('This',), ('is',), ('a',), ('test',), ('with',), ('newline',), ('characters',)]
        assert result == expected, f"Expected {expected}, but got {result}"
    """
    # Test with a very long string to check performance and memory usage
    def test_long_string_performance(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        long_string = " ".join(["word" + str(i) for i in range(100000)])  # Creating a very long string
        result = processor.make_unigram(long_string)
        expected = [('word0',), ('word1',), ('word2',), ..., ('word99999',)]  # Expected unigrams
        assert result == expected, f"Expected {expected}, but got {result}"
    """
    
    # Test with a string that includes tab characters
    def test_string_with_tab_characters(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        result = processor.make_unigram("This is a test\twith\ttab\tcharacters")
        expected = [('This',), ('is',), ('a',), ('test',), ('with',), ('tab',), ('characters',)]
        assert result == expected, f"Expected {expected}, but got {result}"
    # Test with input that is not a string (e.g., passing a list or integer)
    def test_input_not_string(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        with self.assertRaises(AttributeError):
            processor.make_unigram([1, 2, 3])

    # Test with a string containing HTML or XML tags
    def test_string_with_html_tags(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        result = processor.make_unigram("<p>This is a test</p>")
        expected = [('<p>This',), ('is',), ('a',), ('test</p>',)]
        assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == '__main__':
    unittest.main()