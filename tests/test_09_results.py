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
    """
    # Verify output when cosine similarity is slightly above 50.1% (e.g., 50.62%)
    def test_similarity_slightly_above_50_percent(self):
        processor = TextProcessor("org-059.txt", "FID-005.txt")
        result = processor.results([[0, 0.5062]])
        expected_result = {
            "File being compared": "org-059.txt",
            "Comparing with": "FID-005.txt",
            "Percentage of similarity": 50.62
        }
        self.assertEqual(result, expected_result)

    # Verify output when cosine similarity is above 50.10%
    def test_similarity_above_50_percent(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        result = processor.results([[0, 0.6975]])
        expected_result = {
            "File being compared": "org-023.txt",
            "Comparing with": "FID-005.txt",
            "Percentage of similarity": 69.75
        }
        self.assertEqual(result, expected_result)
    # Verify output when cosine similarity is below 50.1%
    def test_cosine_similarity_below_50_percent(self):
        processor = TextProcessor("org-011.txt", "FID-014.txt")
        result = processor.results([[0, 0.4213]])
        expected_result = {
            "File being compared": "org-011.txt",
            "Comparing with": "FID-014.txt",
            "Percentage of similarity": 42.13
        }
        self.assertEqual(result, expected_result)
    
    # Verify output when cosine similarity is exactly 100%
    def test_similarity_exactly_100_percent(self):
        processor = TextProcessor("org-062.txt", "FID-017.txt")
        result = processor.results([[0, 1.0]])
        expected_result = {
            "File being compared": "org-062.txt",
            "Comparing with": "FID-017.txt",
            "Percentage of similarity": 100.0
        }
        self.assertEqual(result, expected_result)

    # Verify output when cosine similarity is exactly 1%
    def test_similarity_exactly_1_percent(self):
        processor = TextProcessor("org-011.txt", "FID-014.txt")
        result = processor.results([[0, 0.01]])
        expected_result = {
            "File being compared": "org-011.txt",
            "Comparing with": "FID-014.txt",
            "Percentage of similarity": 1.0
        }
        self.assertEqual(result, expected_result)
    # Verify output when cosine_evaluation array is empty or malformed
    def test_cosine_evaluation_empty_or_malformed(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        with self.assertLogs() as captured:
            processor.results([])  # Pasar una lista vacía para probar el caso de entrada vacía
        self.assertNotIn("The similarity of the two documents is: 0.00%", captured.output)
        self.assertIn("The cosine evaluation could not be performed. Please check your input.", captured.output[0])

        with self.assertLogs() as captured:
            processor.results(None)  # Pasar None para probar el caso de entrada None
        self.assertNotIn("The similarity of the two documents is: 0.00%", captured.output)
        self.assertIn("The cosine evaluation could not be performed. Please check your input.", captured.output[0])
    # Check for correct rounding of percentages to two decimal places
    def test_correct_rounding_of_percentages(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        result = processor.results([[0, 0.6975]])
        expected_result = {
            "File being compared": "org-023.txt",
            "Comparing with": "FID-005.txt",
            "Percentage of similarity": 69.75
        }
        self.assertEqual(result, expected_result)
    # Test the response time of the method for performance analysis
    def test_response_time_performance_analysis(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        start_time = time.time()
        processor.results([[0, 50.10]])
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertLessEqual(execution_time, 0.01) 

    # Verify that the method correctly handles None values
    def test_handles_none_values(self):
        processor = TextProcessor("org-023.txt", "FID-005.txt")
        with self.assertLogs() as captured:
            processor.results(None)
        self.assertIn("The cosine evaluation could not be performed. Please check your input.", captured.output[0])

if __name__ == '__main__':
    unittest.main()