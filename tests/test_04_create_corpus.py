"""
Authors: Erika García,
Christian Parrish,
Jorge Blanco
"""

import sys
import os
import unittest

# This is to add the parent directory to the system path in order to access Model.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model import TextProcessor

class TestCreateCorpus(unittest.TestCase):

    # Returns a list of unique words when input list has duplicates
    def test_returns_unique_words_with_duplicates(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        input_words = ["apple", "banana", "apple", "orange", "banana"]
        expected_output = ["apple", "banana", "orange"]
        result = processor.create_corpus(input_words)
        self.assertEqual(result, expected_output)

    # Returns an empty list when input is an empty list
    def test_returns_empty_list_with_empty_input(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        input_words = []
        expected_output = []
        result = processor.create_corpus(input_words)
        self.assertEqual(result, expected_output)

    # Handles a list with a single word by returning the same list
    def test_handles_single_word_list(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        input_words = ["apple"]
        expected_output = ["apple"]
        result = processor.create_corpus(input_words)
        self.assertEqual(result, expected_output)

    # Preserves the order of first occurrences when removing duplicates
    def test_preserves_order_of_first_occurrences(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        input_words = ["apple", "banana", "apple", "orange", "banana"]
        expected_output = ["apple", "banana", "orange"]
        result = processor.create_corpus(input_words)
        self.assertEqual(result, expected_output)

    # Processes an already unique list without any changes
    def test_unique_list_no_changes(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        input_words = ["apple", "banana", "orange"]
        expected_output = ["apple", "banana", "orange"]
        result = processor.create_corpus(input_words)
        self.assertEqual(result, expected_output)

    # Works correctly with lists containing non-string elements like numbers or booleans
    def test_works_with_non_string_elements(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        input_words = [3, 2, True, 3, False]
        expected_output = [3, 2, True, False]
        result = processor.create_corpus(input_words)
        assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Handles lists with varying cases (e.g., 'Word' vs 'word') without altering case sensitivity
    def test_handles_lists_with_varying_cases(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        input_words = ["Word", "word", "Word", "word"]
        expected_output = ["Word", "word"]
        result = processor.create_corpus(input_words)
        self.assertEqual(result, expected_output)

    # Efficiently handles large lists without performance degradation
    def test_handles_large_lists(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        input_words = ["apple"] * 1000000
        expected_output = ["apple"]
        result = processor.create_corpus(input_words)
        self.assertEqual(result, expected_output)

    # Maintains Unicode and special characters in words without corruption
    def test_maintains_unicode_and_special_characters(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        input_words = ["apple", "bánánà", "apple", "órange", "bánánà"]
        expected_output = ["apple", "bánánà", "órange"]
        result = processor.create_corpus(input_words)
        self.assertEqual(result, expected_output)

    # Does not modify the original input list but returns a new list
    def test_does_not_modify_original_input(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        input_words = ["apple", "banana", "apple", "orange", "banana"]
        expected_output = ["apple", "banana", "orange"]
        result = processor.create_corpus(input_words)
        self.assertEqual(result, expected_output)

    # Can process lists containing multiple languages
    def test_process_lists_multiple_languages(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        input_words = ["apple", "banana", "manzana", "orange", "naranja"]
        expected_output = ["apple", "banana", "manzana", "orange", "naranja"]
        result = processor.create_corpus(input_words)
        self.assertEqual(result, expected_output)

    # Handles lists with words that are substrings of each other correctly
    def test_handles_substring_words_correctly(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        input_words = ["apple", "app", "orange", "orang"]
        expected_output = ["apple", "app", "orange", "orang"]
        result = processor.create_corpus(input_words)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()