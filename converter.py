"""
Converts text to anki
"""

import warnings

class AnkiConverter():
    """Converts customzied text files to Anki cards
    """

    def __init__(self, file_dir):
        pass

    def __get_lines(self, file_dir):
        """Creates a list of each line in a text file
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
            warnings.warn("Text file has uneven question-to-field format. (n={})"
                            .format(number_of_lines), RuntimeWarning)

        file.close()

        return lines

    def __convert_to_tuples(self, lines):
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

        if index_to_start == 0 and lines[index] == 'IGNOREUP':
            warnings.warn("IGNOREUP was not found in the text file. \
                Converting entire text file to anki cards.", RuntimeWarning)

        return cards, index_to_start

    def __convert_tuples_to_anki(self, data, index_to_start):
        """Converts tuples that are in (question, answer) format into anki-readable text format
        """

        content = ""

        index = index_to_start
        while index < len(data):
            content += "{};{}\n".format(data[index][0], data[index][1])
            index += 1

        return content

    def convert_to_anki(self, file_dir):
        """Convert plain text file into Anki-readable cards

        Args:
            file_dir ([str]): directory to text file

        Returns:
            [str]: contents of anki-importable text file
        """
        cards, index_to_start = self.__convert_to_tuples(self.__get_lines(file_dir))

        return self.__convert_tuples_to_anki(cards, index_to_start)