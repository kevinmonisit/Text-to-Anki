"""
Main module. Run to convert text files to anki-importable cards.
"""

import sys
from converter import AnkiConverter

if __name__ == "__main__":
    if len(sys.argv) > 0:
        obj = AnkiConverter(sys.argv[0])
