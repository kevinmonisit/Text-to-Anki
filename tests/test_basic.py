"""Tests basic reading and writing Anki card functionality
"""

import unittest
import converter
import os

class test_basic(unittest.TestCase):

    def __delete_test_files(self, tester_name, output_name):
        names = [tester_name, output_name]
        
        for name in names:        
            if os.path.exists(name):
                os.remove(name)
            else:
                print("OKAY. File {} does not exist, no need to delete.".format(name))

    def test_convert_to_anki(self):
        
        tester_input_name = "tester.txt"
        output_name = "cards.txt"

        self.__delete_test_files(tester_input_name, output_name)

        content = converter.convert_to_anki(tester_input_name, output_name)
        print(content)


        self.assertEqual(1,1)



if __name__ == "__main__":
    unittest.main()