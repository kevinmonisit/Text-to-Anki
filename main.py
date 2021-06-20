"""
Main module. Run to convert text files to anki-importable cards.
"""

import sys
import src.converter as converter
import argparse
import os.path
from os import path, write

if __name__ == "__main__":
    """

        python3 main.py source.txt
        python 3 main.py -p ./path/to/add/files
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("source",
                        help="the path to a correctly formatted text file")
    parser.add_argument("-p", "--path",
                        help="Specify the path where output will go",
                        default="./")
    parser.add_argument("--s",
                        metavar="starting-point-specified",
                        nargs="?",
                        help="Whether to look for a STARTHERE token or not. \
                                Default is True=1. (False=0)",
                        choices=[0, 1],
                        default=True,
                        type=int)
    parser.add_argument("--ending",
                        metavar="suffix",
                        nargs="?",
                        help=("If specified, the program will add"
                              "an ending note/suffix to the ending"
                              "of all questions."),
                        default=None,
                        type=str)

    args = parser.parse_args()

    path = args.path
    source = args.source
    starting_point_exists = args.s
    ending_suffix = args.ending

    lines = converter.get_lines(source,
                                STARTHERE_key_exists=starting_point_exists)

    typed, not_typed = converter.convert_to_anki(lines, ending_suffix)

    print(typed)
    print("===== NOT TYPED BELOW =====")
    print(not_typed)

    if(path):
        files = [("typed_questions.txt", typed),
                 ("not_typed_questions.txt", not_typed)]

        for text_file in files:
            if(os.path.exists(text_file[0])):
                print("{} exists... overriding".format(text_file[0]))

            file = open(text_file[0], "w")
            file.write(text_file[1])
            file.close()
