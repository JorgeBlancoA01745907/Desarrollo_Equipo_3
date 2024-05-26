# File: tests/test_03_stemmer.py
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

class TestStemmer(unittest.TestCase):

    # Verify that common English words are correctly stemmed
    def test_common_english_words_stemming(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = [('running',), ('easily',), ('cars',)]
        expected_stems = ['run', 'easy', 'car']
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(stemmed_words, expected_stems)

    # Test with an empty unigram list to see if it returns an empty list
    def test_empty_unigram_list(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = []
        expected_stems = []
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(stemmed_words, expected_stems)

    # Ensure that stemming is applied to each word in the unigram list
    def test_stemming_applied_to_each_word(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = [('running',), ('easily',), ('cars',)]
        expected_stems = ['run', 'easy', 'car']
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(stemmed_words, expected_stems)

    # Confirm that stemming handles words with mixed case correctly
    def test_stemmer_mixed_case(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = [('Running',), ('Easily',), ('Cars',)]
        expected_stems = ['run', 'easy', 'car']
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(stemmed_words, expected_stems)

    # Check that the output list length matches the input unigram list length
    def test_output_list_length_matches_input(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = [('running',), ('easily',), ('cars',)]
        expected_length = len(unigram)
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(len(stemmed_words), expected_length)

    # Test that stemming processes words with apostrophes and other special characters appropriately
    def test_stemming_special_characters(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = [("can't",), ("won't",), ("don't",)]
        expected_stems = ['can', 'wo', 'do']
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(stemmed_words, expected_stems)


    # Verify how the stemmer handles unigrams with numeric values
    def test_stemmer_with_numeric_values(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = [('123',), ('456',), ('789',)]
        expected_stems = ['123', '456', '789']
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(stemmed_words, expected_stems)

    # Assess the output when unigrams contain null or None values
    def test_unigrams_with_null_values(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = [('running',), None, ('cars',)]
        expected_stems = ['run', 'car']
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(stemmed_words, expected_stems)
    """
    # Evaluate the function's response to unigrams with very long words
    def test_response_to_long_words(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = [('antidisestablishmentarianism',), ('pneumonoultramicroscopicsilicovolcanoconiosis',)]
        expected_stems = ['antidisestablishmentarian', 'pneumonoultramicroscopicsilicovolcanoconiosi']
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(stemmed_words, expected_stems)
    """

    # Check if repeated words in the unigram list are stemmed consistently
    def test_repeated_words_stemming(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = [('running',), ('running',), ('running',)]
        expected_stems = ['run', 'run', 'run']
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(stemmed_words, expected_stems)

    # Examine the case sensitivity of the stemming process
    def test_case_sensitivity_stemming(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = [('Running',), ('Easily',), ('Cars',)]
        expected_stems = ['run', 'easy', 'car']
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(stemmed_words, expected_stems)
    """
    # Determine if changes in word order in the unigram affect stemming results
    def test_word_order_affect_stemming(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = [('running',), ('easily'), ('cars',)]
        expected_stems = ['run', 'easy', 'car']
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(stemmed_words, expected_stems)
    """

    # Test the stemmer's performance with a large dataset to assess efficiency
    def test_stemmer_large_dataset_efficiency(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = [('large',), ('dataset',), ('to',), ('assess',), ('efficiency',)]
        expected_stems = ['larg', 'dataset', 'to', 'assess', 'efficy']
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(stemmed_words, expected_stems)

    # Assess how the stemmer handles hyphenated words
    def test_stemmer_hyphenated_words(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        unigram = [('high-speed',), ('well-known',), ('self-driving',)]
        expected_stems = ['high-speed', 'well-known', 'self-driving']
        stemmed_words = processor.stemmer(unigram)
        self.assertEqual(stemmed_words, expected_stems)

if __name__ == '__main__':
    unittest.main()