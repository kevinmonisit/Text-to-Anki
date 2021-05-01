"""
Main module. Run to convert text files to anki-importable cards.
"""

import sys
import src.converter as converter


if __name__ == "__main__":
    """
        Make a choice of whether to make a file or not.

        python3 main.py source.txt > cards.txt
            - if there are multiple typed or non-typed, or tags,
            divide them up in the text file

        python3 main.py source.txt
            if second parameter not present, make a cards.txt file
            unlike the first option, the program will make
            multiple text files separating the categories.
    """

    if len(sys.argv) > 3:
        pass
    elif len(sys.argv) == 2:
        source = sys.argv[1]
        lines = converter.get_lines(source)

        content = converter.convert_to_anki(lines)
        for i in content:
            print(i)

    else:
        raise Exception("Invalid number of arguments."
                        "Check README.md on how to use.")
