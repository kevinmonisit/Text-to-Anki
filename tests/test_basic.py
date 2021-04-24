"""Tests basic reading and writing Anki card functionality
"""

import unittest
from src import converter
import os

class test_basic(unittest.TestCase):
    
    def setUp(self):
        self.test_content = "What is my name?\n\nKevin\n\n2+2=\n\n4"
        self.test_file_name = "./tests/__tester__.txt"

    def _write_test_file(self):
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)
        else:
            print("Removed file {}".format(self.test_file_name))
        
        f = open(self.test_file_name, "w")
        f.write(self.test_content)
        f.close()
     
    def test_get_lines(self):
        self._write_test_file()

        content = converter.get_lines(self.test_file_name)
    
        expected_content = ["What is my name?", '', "Kevin", '',
                            "2+2=", '', "4"]
        
        self.assertEqual(content, expected_content);
    
    def test_convert_list_to_tuples(self):
        self._write_test_file()

        content = converter.get_lines(self.test_file_name)
        content = converter._convert_to_tuples(content)

        expected_content = [("What is my name?", "Kevin"), 
                            ("2+2=", "4")]

        self.assertEqual(content, expected_content)
        
    # tests that are yet to be implemented.
    def test_typed_answers_error(self):
        content = [("What is my name", "Kevin")]
        
        self.assertRaises(ValueError, lambda: converter.add_typed_answers(content))
        
    
    def __test_typed_answers(self):
        content = [("What is my name? T", "Kevin"), 
                            ("2+2= ?", "4")]
        
        data = converter.add_typed_answers(content)

        # expected return value is a tuple containing lists
        # within each list are tuples in the (question, answer) format
        # first lists are typed, second list are not typed
        expected_data = ([("What is my name?", "Kevin")], 
                         [("2 + 2 = ?", "4")])
        
        self.assertEqual(data, expected_data)        
        
if __name__ == "__main__":
    unittest.main()