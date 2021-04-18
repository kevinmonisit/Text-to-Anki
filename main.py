"""
Converts text to anki
"""

import sys


def convert_text(file_dir, type_of_card):
    """
    Converts text to anki-ready cards.
    
    Format:
    [Question]
    [Space]
    [Field]
    [Space]

    """

    file = open(file_dir)
    lines = []

    cards = []

    while True:
        line = file.readline()

        if not line:
            break

        if len(line) > 0:
            lines.append(line.strip())

    for index, line in enumerate(lines):
        if index + 2 < len(lines):
            cards.append((lines[index], lines[index+2]))
        
        

    for i in cards:
        print(i)



if __name__ == "__main__":
    convert_text(sys.argv[1], sys.argv[2])