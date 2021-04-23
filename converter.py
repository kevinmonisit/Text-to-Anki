"""
Converts text to anki
"""

import warnings

def get_lines(file_dir):
    """Creates an array of lines from a text file

    Args:
        file_dir ([str]): file directory to read

    Returns:
        [list]: a list of all lines from text file
    """
    file = open(file_dir)
    lines = []

    while True:
        line = file.readline()

        if not line:
            break

        if len(line) > 0:
            lines.append(line.strip())

    number_of_lines = len(lines)

    if number_of_lines % 4 != 0:
        warnings.warn("Text file has uneven question-to-field format. (n = {})"
                        .format(number_of_lines), RuntimeWarning)

    file.close()

    return lines

def _convert_to_tuples(lines):
    """Converts lines to a list of tuples which are in a (question, answer) format.
    """

    cards = []
    number_of_lines = len(lines)

    index = 0
    index_to_start = 0
    
    while index < number_of_lines:

        # @TODO
        # index_to_start will not be the correct index in the cards list
        if lines[index] == 'IGNOREUP':
            index_to_start = index

        if index + 2 < number_of_lines:
            cards.append((lines[index], lines[index+2]))

        index += 4

    if index_to_start == 0 and lines[0] != 'IGNOREUP':
        warnings.warn("IGNOREUP was not found in the text file. \
            Converting entire text file to anki cards.", RuntimeWarning)

    return cards

def __convert_tuples_to_anki(data):
    """Converts tuples that are in (question, answer) format into anki-readable text format
    """

    content = ""
    index = 0
    
    while index < len(data):
        entry = "{};{}\n".format(data[index][0], data[index][1])
        content += entry

        index += 1

    return content

def convert_to_anki(content):
    """Converts data from a read text file into anki-importable text

    Args:
        content ([list]): list of all lines of a correctly-formatted text file (use get_lines)
    """

    cards = __convert_to_tuples(content)

    return __convert_tuples_to_anki(cards)
