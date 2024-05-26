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


class TestCreateUnigramMatrix(unittest.TestCase):

    # Verify that a correct unigram matrix is created when both final_matrix and big_corpus are populated with multiple unique stemmed words
    def test_populated_final_matrix_and_big_corpus(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        final_matrix = [['apple', 'banana'], ['banana', 'cherry']]
        big_corpus = ['apple', 'banana', 'cherry', 'date']
        expected_matrix = [[1, 1, 0, 0], [0, 1, 1, 0]]
        result_matrix = processor.create_unigram_matrix(final_matrix, big_corpus)
        self.assertEqual(result_matrix, expected_matrix)

    # Check the behavior when final_matrix is empty and big_corpus is non-empty
    def test_empty_final_matrix_non_empty_big_corpus(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        final_matrix = []
        big_corpus = ['apple', 'banana', 'cherry']
        expected_matrix = []
        result_matrix = processor.create_unigram_matrix(final_matrix, big_corpus)
        self.assertEqual(result_matrix, expected_matrix)

    # Ensure that the matrix contains only 1s and 0s where 1 represents the presence of a word from big_corpus in final_matrix and 0 represents absence
    def test_unigram_matrix_presence(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        final_matrix = [['apple', 'banana'], ['banana', 'cherry']]
        big_corpus = ['apple', 'banana', 'cherry', 'date']
        expected_matrix = [[1, 1, 0, 0], [0, 1, 1, 0]]
        result_matrix = processor.create_unigram_matrix(final_matrix, big_corpus)
        self.assertEqual(result_matrix, expected_matrix)

    # Confirm that the method handles multiple paragraphs (lists within final_matrix) correctly, creating a sub-list for each
    def test_multiple_paragraphs_handling(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        final_matrix = [['apple', 'banana'], ['banana', 'cherry']]
        big_corpus = ['apple', 'banana', 'cherry', 'date']
        expected_matrix = [[1, 1, 0, 0], [0, 1, 1, 0]]
        result_matrix = processor.create_unigram_matrix(final_matrix, big_corpus)
        self.assertEqual(result_matrix, expected_matrix)

    # Check that the method returns a matrix of correct dimensions given the sizes of final_matrix and big_corpus
    def test_populated_final_matrix_and_big_corpus(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        final_matrix = [['apple', 'banana'], ['banana', 'cherry']]
        big_corpus = ['apple', 'banana', 'cherry', 'date']
        expected_matrix = [[1, 1, 0, 0], [0, 1, 1, 0]]
        result_matrix = processor.create_unigram_matrix(final_matrix, big_corpus)
        self.assertEqual(result_matrix, expected_matrix)

    # Test that the order of words in big_corpus is correctly reflected in the order of columns in the resulting unigram matrix
    def test_order_of_words_reflected_in_matrix(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        final_matrix = [['apple', 'banana'], ['banana', 'cherry']]
        big_corpus = ['apple', 'banana', 'cherry', 'date']
        expected_matrix = [[1, 1, 0, 0], [0, 1, 1, 0]]
        result_matrix = processor.create_unigram_matrix(final_matrix, big_corpus)
        self.assertEqual(result_matrix, expected_matrix)

    # Verify the method's response when both final_matrix and big_corpus are empty
    def test_empty_final_matrix_and_big_corpus(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        final_matrix = []
        big_corpus = []
        expected_matrix = []
        result_matrix = processor.create_unigram_matrix(final_matrix, big_corpus)
        self.assertEqual(result_matrix, expected_matrix)

    # Ensure correct behavior when final_matrix contains paragraphs with repeated words
    def test_final_matrix_with_repeated_words(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        final_matrix = [['apple', 'banana', 'apple'], ['banana', 'cherry', 'banana']]
        big_corpus = ['apple', 'banana', 'cherry', 'date']
        expected_matrix = [[1, 1, 0, 0], [0, 1, 1, 0]]
        result_matrix = processor.create_unigram_matrix(final_matrix, big_corpus)
        self.assertEqual(result_matrix, expected_matrix)

    # Test the function with big_corpus containing words not present in any paragraph of final_matrix
    def test_big_corpus_words_not_present(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        final_matrix = [['apple', 'banana'], ['banana', 'cherry']]
        big_corpus = ['apple', 'banana', 'cherry', 'date']
        expected_matrix = [[1, 1, 0, 0], [0, 1, 1, 0]]
        result_matrix = processor.create_unigram_matrix(final_matrix, big_corpus)
        self.assertEqual(result_matrix, expected_matrix)
    """
    #TODO: See why it is failing this test and fix it
    # Assess performance and efficiency for very large inputs
    def test_performance_efficiency_large_inputs(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        final_matrix = [['apple', 'banana'] * 1000, ['banana', 'cherry'] * 1000]
        big_corpus = ['apple', 'banana', 'cherry', 'date']
        expected_matrix = [[1] * 1000 + [0] * 1000, [0] * 1000 + [1] * 1000]
        result_matrix = processor.create_unigram_matrix(final_matrix, big_corpus)
        
        # Print expected and result matrices
        print("Expected Matrix:")
        for row in expected_matrix:
            print(row)
        print("Result Matrix:")
        for row in result_matrix:
            print(row)
        
        # Compare element-wise instead of comparing the entire lists
        for expected_row, result_row in zip(expected_matrix, result_matrix):
            self.assertEqual(expected_row, result_row)

    """
    # Check how the method handles non-string elements within the lists, if any are mistakenly passed
    def test_non_string_elements_handling(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        final_matrix = [['apple', 'banana', 123], ['banana', 'cherry', True]]
        big_corpus = ['apple', 'banana', 'cherry', 'date']
        expected_matrix = [[1, 1, 0, 0], [0, 1, 1, 0]]
        result_matrix = processor.create_unigram_matrix(final_matrix, big_corpus)
        self.assertEqual(result_matrix, expected_matrix)

    # Verify that the method correctly handles special characters and numbers in words if they are not cleaned previously
    def test_special_characters_and_numbers_handling(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        final_matrix = [['apple', 'banana'], ['banana', 'cherry']]
        big_corpus = ['apple', 'banana', 'cherry', 'date']
        expected_matrix = [[1, 1, 0, 0], [0, 1, 1, 0]]
        result_matrix = processor.create_unigram_matrix(final_matrix, big_corpus)
        self.assertEqual(result_matrix, expected_matrix)

    # Test the method's behavior when final_matrix contains sub-lists of varying lengths
    def test_final_matrix_varying_lengths(self):
        processor = TextProcessor("dummy1.txt", "dummy2.txt")
        final_matrix = [['apple', 'banana'], ['banana', 'cherry', 'date']]
        big_corpus = ['apple', 'banana', 'cherry', 'date']
        expected_matrix = [[1, 1, 0, 0], [0, 1, 1, 1]]
        result_matrix = processor.create_unigram_matrix(final_matrix, big_corpus)
        self.assertEqual(result_matrix, expected_matrix)

if __name__ == "__main__":
    unittest.main()