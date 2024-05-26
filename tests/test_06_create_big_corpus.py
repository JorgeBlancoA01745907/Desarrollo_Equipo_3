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

class TestCreateBigCorpus(unittest.TestCase):

    # Combines two non-empty corpora into one larger corpus without duplicates
    def test_combines_non_empty_corpora(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = ["word1", "word2", "word3"]
        corpus2 = ["word3", "word4", "word5"]
        expected_result = ["word1", "word2", "word3", "word4", "word5"]
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

    # Handles empty input for both corpora correctly, returning an empty list
    def test_handles_empty_input(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = []
        corpus2 = []
        expected_result = []
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

    # Maintains the order of elements as they first appear in the input lists
    def test_maintains_order_of_elements(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = ["word1", "word2", "word3"]
        corpus2 = ["word3", "word4", "word5"]
        expected_result = ["word1", "word2", "word3", "word4", "word5"]
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

    # Returns a list containing all unique elements from both input lists
    def test_create_big_corpus_unique_elements(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = ["word1", "word2", "word3"]
        corpus2 = ["word3", "word4", "word5"]
        expected_result = ["word1", "word2", "word3", "word4", "word5"]
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

    # Handles corpora with overlapping elements correctly by removing duplicates
    def test_handles_overlapping_elements(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = ["word1", "word2", "word3"]
        corpus2 = ["word3", "word4", "word5"]
        expected_result = ["word1", "word2", "word3", "word4", "word5"]
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

    # Works correctly when both input corpora contain the same elements
    def test_both_corpora_same_elements(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = ["word1", "word2", "word3"]
        corpus2 = ["word1", "word2", "word3"]
        expected_result = ["word1", "word2", "word3"]
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

    # Handles one corpus being empty and the other non-empty correctly
    def test_handles_one_empty_corpus(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = []
        corpus2 = ["word1", "word2", "word3"]
        expected_result = ["word1", "word2", "word3"]
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

    # Returns an empty list when both input lists are empty
    def test_returns_empty_list_when_both_input_lists_are_empty(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = []
        corpus2 = []
        expected_result = []
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

    # Processes correctly when both corpora are identical
    def test_processes_correctly_when_both_corpora_are_identical(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = ["word1", "word2", "word3"]
        corpus2 = ["word1", "word2", "word3"]
        expected_result = ["word1", "word2", "word3"]
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

    # Processes large corpora efficiently without performance degradation
    def test_processes_large_corpora_efficiently(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = ["word1", "word2", "word3"]
        corpus2 = ["word3", "word4", "word5"]
        expected_result = ["word1", "word2", "word3", "word4", "word5"]
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

    # Verifies that the output list does not contain any duplicates even if input lists have multiple duplicates
    def test_no_duplicates_in_output(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = ["word1", "word1", "word2", "word3", "word3"]
        corpus2 = ["word3", "word3", "word4", "word5", "word5"]
        expected_result = ["word1", "word2", "word3", "word4", "word5"]
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

    # Checks the type of input to ensure only lists are processed, raising an error for other data types
    def test_input_type_validation(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = ["word1", "word2", "word3"]
        corpus2 = "word3, word4, word5"
        with self.assertRaises(TypeError):
            processor.create_big_corpus(corpus1, corpus2)

    # Ensures that the method can handle a large number of elements in both corpora without running out of memory
    def test_handles_large_number_of_elements(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = ["word1"] * 1000000
        corpus2 = ["word2"] * 1000000
        expected_result = ["word1", "word2"]
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

    # Confirms that non-string elements are handled correctly if present in the corpora
    def test_non_string_elements_handling(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = ["word1", "word2", "word3", 123, True]
        corpus2 = ["word3", "word4", "word5"]
        expected_result = ["word1", "word2", "word3", 123, True, "word4", "word5"]
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

    # Tests the function's response time to ensure it meets performance requirements
    def test_create_big_corpus_performance(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        corpus1 = ["word1", "word2", "word3"]
        corpus2 = ["word3", "word4", "word5"]
        expected_result = ["word1", "word2", "word3", "word4", "word5"]
        result = processor.create_big_corpus(corpus1, corpus2)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()