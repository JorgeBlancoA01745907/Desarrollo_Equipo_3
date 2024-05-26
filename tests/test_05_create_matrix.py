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

class TestCreateMatrix(unittest.TestCase):

    # Verify that the method returns a list containing two sublists
    def test_returns_two_sublists(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        stems1 = ['word1', 'word2']
        stems2 = ['word3', 'word4']
        result = processor.create_matrix(stems1, stems2)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[1], list)

    # Test with empty lists for both stems1 and stems2
    def test_empty_lists(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        stems1 = []
        stems2 = []
        result = processor.create_matrix(stems1, stems2)
        self.assertEqual(result, [[], []])

    # Check that the order of the input lists is preserved in the output
    def test_order_preserved_in_output(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        stems1 = ['word1', 'word2']
        stems2 = ['word3', 'word4']
        result = processor.create_matrix(stems1, stems2)
        self.assertEqual(result, [stems1, stems2])

    # Check the behavior when lists contain non-string elements
    def test_non_string_elements_in_lists(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        stems1 = ['word1', 123, 'word2']
        stems2 = [456, 'word3', 'word4']
        result = processor.create_matrix(stems1, stems2)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[1], list)

    # Confirm that the method does not alter the content of the input lists
    def test_method_does_not_alter_content(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        stems1 = ['word1', 'word2']
        stems2 = ['word3', 'word4']
        original_stems1 = stems1.copy()
        original_stems2 = stems2.copy()
        result = processor.create_matrix(stems1, stems2)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[1], list)
        self.assertEqual(stems1, original_stems1)
        self.assertEqual(stems2, original_stems2)

    # Test with one empty list and one non-empty list
    def test_one_empty_list_and_one_non_empty_list(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        stems1 = []
        stems2 = ['word1', 'word2']
        result = processor.create_matrix(stems1, stems2)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[1], list)

    # Ensure that the method handles lists of stemmed words correctly
    def test_handles_lists_of_stemmed_words_correctly(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        stems1 = ['word1', 'word2']
        stems2 = ['word3', 'word4']
        result = processor.create_matrix(stems1, stems2)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[1], list)

    # Test with very large lists to check for performance issues
    def test_large_lists_performance(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        stems1 = ['word1'] * 1000000
        stems2 = ['word2'] * 1000000
        result = processor.create_matrix(stems1, stems2)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[1], list)

    # Verify that the method can handle lists with duplicate elements
    def test_handles_lists_with_duplicates(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        stems1 = ['word1', 'word1', 'word2']
        stems2 = ['word2', 'word3', 'word3']
        result = processor.create_matrix(stems1, stems2)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[1], list)

    # Check if the method returns a new list object rather than modifying the input lists
    def test_returns_new_list_object(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        stems1 = ['word1', 'word2']
        stems2 = ['word3', 'word4']
        result = processor.create_matrix(stems1, stems2)
        self.assertIsInstance(result, list)
        self.assertNotEqual(id(result), id(stems1))
        self.assertNotEqual(id(result), id(stems2))

    # Ensure that the method handles lists with special characters and numbers
    def test_handles_lists_with_special_characters_and_numbers(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        stems1 = ['word1', 'word2', 'special@', '123']
        stems2 = ['word3', 'word4', 'characters!', '456']
        result = processor.create_matrix(stems1, stems2)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[1], list)

    # Test the method with unicode and special characters in the list elements
    def test_special_characters_in_list_elements(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        stems1 = ['word1', 'word2', 'unicódé', 'speci@l']
        stems2 = ['word3', 'word4', 'uni©ode', 'spéci@l']
        result = processor.create_matrix(stems1, stems2)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[1], list)

if __name__ == '__main__':
    unittest.main()