"""
Main module. Run to convert text files to anki-importable cards.
"""

import sys
import src.converter as converter
import argparse
import os.path
from os import path

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
                                Default is True.",
                        choices=[False, True],
                        default=True)

    args = parser.parse_args()

    path = args.path
    source = args.source
    starting_point_exists = args.s

    print([path, source, starting_point_exists].join(' '))

    lines = converter.get_lines(source,
                                STARTHERE_key_exists=starting_point_exists)

    # if len(sys.argv) == 2:
    #     source = sys.argv[1]
    #     lines = converter.get_lines(source, look_for_ignore_up=True)

    #     content = converter.convert_to_anki(lines)
    #     for i in content:
    #         print(i)

    # else:
    #     raise Exception("Invalid number of arguments."
    #                     "Check README.md on how to use.")
