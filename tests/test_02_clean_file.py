# File: tests/test_01_clean_file.py
"""
Authors: Erika García,
Christian Parrish,
Jorge Blanco
"""

import sys
import os
import io
import unittest
from unittest import TestCase
from unittest.mock import mock_open, patch

# This is to add the parent directory to the system path in order to access Model.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model import TextProcessor

class TestCleanFile(unittest.TestCase):
    
    # Verify that punctuation marks ',.?!()' are removed from the document
    def test_punctuation_removal(self):
        with patch('builtins.open', mock_open(read_data="Hello, world! How are you? (I hope well).")):
            processor = TextProcessor("dummy_path1.txt", "dummy_path2.txt")
            result = processor.clean_file("dummy_path1.txt")
            expected = "hello world how are you i hope well"
            assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test with an empty file to see if it returns an empty string
    def test_empty_file(self):
        # Mocking the open function to return an empty file-like object
        with patch('builtins.open', mock_open(read_data="")):
            processor = TextProcessor("dummy_path1.txt", "dummy_path2.txt")
            result = processor.clean_file("dummy_path1.txt")
            self.assertEqual(result, "")

    # Confirm that the method returns the cleaned text as a string
    def test_clean_file_returns_cleaned_text(self):
        with patch('builtins.open', mock_open(read_data="Hello, world! How are you? (I hope well).")):
            processor = TextProcessor("dummy_path1.txt", "dummy_path2.txt")
            result = processor.clean_file("dummy_path1.txt")
            expected = "hello world how are you i hope well"
            assert result == expected, f"Expected '{expected.lower()}', but got '{result}'"
            
    # Check that the method reads the entire content of a file correctly
    def test_read_entire_content(self):
        with patch('builtins.open', mock_open(read_data="This is a test file with multiple lines. Line 2. Line 3.")):
            processor = TextProcessor("dummy_path1.txt", "dummy_path2.txt")
            result = processor.clean_file("dummy_path1.txt")
            expected = "this is a test file with multiple lines line 2 line 3"
            assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Verify behavior when the file contains only punctuation marks
    def test_file_contains_only_punctuation_marks(self):
        with patch('builtins.open', mock_open(read_data=",.?!()")):
            processor = TextProcessor("dummy_path1.txt", "dummy_path2.txt")
            result = processor.clean_file("dummy_path1.txt")
            self.assertEqual(result, "", "Punctuation marks were not removed correctly")

    # Test the method with a file containing only spaces and newlines
    def test_clean_file_with_spaces_and_newlines(self):
        with patch('builtins.open', mock_open(read_data="   \n\n\n   \n\n")):
            processor = TextProcessor("dummy_path1.txt", "dummy_path2.txt")
            result = processor.clean_file("dummy_path1.txt")
            self.assertEqual(result, "")

    
    # Check how the method handles files with non-English characters or symbols
    def test_non_english_characters_handling(self):
        with patch('builtins.open', mock_open(read_data="Hóla, qué tal? ¿Cómo estás? (Espero que bien).")):
            processor = TextProcessor("dummy_path1.txt", "dummy_path2.txt")
            result = processor.clean_file("dummy_path1.txt")
            self.assertEqual(result, "hóla qué tal cómo estás espero que bien")
    
    # Evaluate the function's response to a file path that does not exist
    def test_file_not_found(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            processor = TextProcessor("dummy_path1.txt", "dummy_path2.txt")
            with self.assertRaises(FileNotFoundError):
                processor.clean_file("non_existent_file.txt")

    # Check if the method can handle file paths with special characters
    def test_handle_special_characters_in_file_path(self):
        with patch('builtins.open', mock_open(read_data="Hello, world! How are you? (I hope well).")):
            processor = TextProcessor("dummy_path1.txt", "dummy_path2.txt")
            result = processor.clean_file("dummy_path1.txt")
            expected = "hello world how are you i hope well"
            assert result == expected, f"Expected '{expected.lower()}', but got '{result}'"

    # Determine the method's behavior with read-only files
    def test_clean_file_read_only_files(self):
        with patch('builtins.open', mock_open(read_data="Hello, world! How are you? (I hope well).")):
            processor = TextProcessor("dummy_path1.txt", "dummy_path2.txt")
            result = processor.clean_file("dummy_path1.txt")
            expected = "hello world how are you i hope well"
            assert result == expected, f"Expected '{expected.lower()}', but got '{result}'"

    # Test the method's response to concurrent access to the same file
    def test_concurrent_access(self):
        with patch('builtins.open', mock_open(read_data="Hello, world! How are you? (I hope well).")):
            processor = TextProcessor("dummy_path1.txt", "dummy_path2.txt")
            result1 = processor.clean_file("dummy_path1.txt")
            result2 = processor.clean_file("dummy_path1.txt")
            self.assertEqual(result1, result2, "concurrent access did not produce the same result")
   
   # Verify the method's handling of files with mixed content (text, numbers, symbols)
    def test_handling_mixed_content(self):
        # Mocking the open function to return a file-like object with mixed content
        with patch('builtins.open',mock_open(read_data="Hello 123 world! @#$ How are you? (I hope well).")):
            processor = TextProcessor("dummy_path1.txt", "dummy_path2.txt")
            result = processor.clean_file("dummy_path1.txt")
            self.assertEqual(result, "hello 123 world how are you i hope well")

    # Assess performance with very large text files
    def test_performance_large_text_files(self):
        large_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." * 10000
        with patch('builtins.open', mock_open(read_data=large_text)):
            processor = TextProcessor("dummy_path1.txt", "dummy_path2.txt")
            result = processor.clean_file("dummy_path1.txt")
            self.assertNotIn(",", result)
            self.assertNotIn(".", result)
            self.assertNotIn("!", result)
            self.assertNotIn("?", result)
            self.assertNotIn("(", result)
            self.assertNotIn(")", result)


if __name__ == '__main__':
    unittest.main()