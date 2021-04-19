"""
Main module. Run to convert text files to anki-importable cards.
"""

import sys
import converter

if __name__ == "__main__":
    
    content = converter.convert_to_anki("tests/tester.txt")



   