"""
Authors: Erika García,
Christian Parrish,
Jorge Blanco
"""

import sys
import os
import time
import unittest

# This is to add the parent directory to the system path in order to access Model.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model import TextProcessor

class TestResults(unittest.TestCase):
    """
    Make the appropriate changes to the test cases below, change the .txt files to correct ones
    # Verify output when cosine similarity is slightly above 55% (e.g., 55.01%)
    def test_similarity_slightly_above_55_percent(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        with self.assertLogs() as captured:
            processor.results([[0, 0.5501]])
        self.assertIn("The similarity of the two documents is: 55.01%", captured.output[0])
        self.assertIn("The two documents provided are similar and therefor plagiarism is present.", captured.output[0])


    # Verify output when cosine similarity is above 55%
    def test_similarity_above_55_percent(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        with self.assertLogs() as captured:
            processor.results([[0, 0.56]])
        self.assertIn("The similarity of the two documents is: 56.00%", captured.output[0])
        self.assertIn("The two documents provided are similar and therefor plagiarism is present.", captured.output[0])


    # Verify output when cosine similarity is below 55%
    def test_cosine_similarity_below_55_percent(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        with self.assertLogs() as captured:
            processor.results([[0, 0.54]])
        self.assertIn("The similarity of the two documents is: 54.00%", captured.output[0])
        self.assertIn("The two documents are not similar, there's no plagiarism present.", captured.output[0])

    # Verify output when cosine similarity is exactly 100%
    def test_similarity_exactly_100_percent(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        with self.assertLogs() as captured:
            processor.results([[0, 1.0]])
        self.assertIn("The similarity of the two documents is: 100.00%", captured.output[0])
        self.assertIn("The two documents provided are similar and therefor plagiarism is present.", captured.output[0])

    # Verify output when cosine similarity is exactly 0%
    def test_similarity_exactly_0_percent(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        with self.assertLogs() as captured:
            processor.results([[0, 0]])
        self.assertIn("The similarity of the two documents is: 0.00%", captured.output[0])
        self.assertIn("The two documents are not similar, there's no plagiarism present.", captured.output[0])

    # Verify output when cosine similarity is slightly below 55% (e.g., 54.99%)
    def test_cosine_similarity_slightly_below_55_percent(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        with self.assertLogs() as captured:
            processor.results([[0, 0.5499]])
        self.assertIn("The similarity of the two documents is: 54.99%", captured.output[0])
        self.assertIn("The two documents are not similar, there's no plagiarism present.", captured.output[0])

    # Verify output when cosine similarity is a negative value
    def test_cosine_similarity_negative_value(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        with self.assertLogs() as captured:
            processor.results([[0, -0.1]])
        self.assertIn("The similarity of the two documents is: -10.00%", captured.output[0])
        self.assertIn("The two documents are not similar, there's no plagiarism present.", captured.output[0])
    # Verify output when cosine_evaluation array is empty or malformed
    def test_cosine_evaluation_empty_or_malformed(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        with self.assertLogs() as captured:
            processor.results([])
        self.assertIn("The similarity of the two documents is: 0.00%", captured.output[0])
        self.assertIn("The two documents are not similar, there's no plagiarism present.", captured.output[0])

    # Check for correct rounding of percentages to two decimal places
    def test_correct_rounding_of_percentages(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        with self.assertLogs() as captured:
            processor.results([[0, 0.556]])
        self.assertIn("The similarity of the two documents is: 55.60%", captured.output[0])
        self.assertIn("The two documents provided are similar and therefor plagiarism is present.", captured.output[0])
    """

    # Test the response time of the method for performance analysis
    def test_response_time_performance_analysis(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        start_time = time.time()
        processor.results([[0, 0.55]])
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertLessEqual(execution_time, 0.01)  # Assuming the method should execute in less than 0.01 seconds
    """
    # Verify that the method correctly handles None values
    def test_handles_none_values(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        with self.assertLogs() as captured:
            processor.results(None)
        self.assertIn("The similarity of the two documents is: 0.00%", captured.output[0])
        self.assertIn("The two documents are not similar, there's no plagiarism present.", captured.output[0])
    """

if __name__ == '__main__':
    unittest.main()