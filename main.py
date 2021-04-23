"""
Main module. Run to convert text files to anki-importable cards.
"""

import sys
import converter

if __name__ == "__main__": 
    i = ""
    f = ""

    path_to_file = ""
    data = converter.get_lines(path_to_file)

    content = converter.convert_to_anki(data)

    f = open("cards.txt", "w")
    f.write(content)
    f.close()



   