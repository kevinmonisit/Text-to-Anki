"""
Converts text to anki
"""

from os import error
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


def convert_to_anki(content):
    """Converts data from a read text file into anki-importable text

    Args:
        content ([list]): list of all lines of a correctly-formatted text file
        (use get_lines)
    """

    cards = _convert_to_tuples(content)

    return _convert_tuples_to_anki(cards)


def _convert_to_tuples(lines):
    """
        Converts lines to a list of tuples which are in a (question, answer)
        format.
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
            _QA = (lines[index], lines[index + 2])
            _check_QA_is_valid(_QA)

            cards.append(_QA)

        index += 4

    if index_to_start == 0 and lines[0] != 'IGNOREUP':
        warnings.warn("IGNOREUP was not found in the text file. \
            Converting entire text file to anki cards.", RuntimeWarning)

    return cards


def _convert_tuples_to_anki(data):
    """
        Converts tuples that are in (question, answer) format into
        anki-readable text format
    """

    content = ""
    index = 0

    while index < len(data):
        entry = "{};{}\n".format(data[index][0], data[index][1])
        content += entry

        index += 1

    return content


def _split_QAs_answer(tuples_list) -> tuple:
    """

        Tests the functionality of adding a sign that the card's
        answer is meant to be typed or not.

        If there is a 'T' or 't', the answer will be typed.

        Function returns a tuple containing (list of typed cards, list
        of non-typed cards)

    Args:
        lines ([list]): Receives list of tuples in (question, answer) format
    """

    typed_questions = []
    non_typed_questions = []

    # tuples list is list of (questions, answer)
    for i in tuples_list:

        question = i[0]
        answer = i[1]

        if '?' not in question:
            print("Error for the question: {}".format(question))
            raise ValueError("Question incorrectly formatted."
                             "Line does not have a question mark at the end"
                             "of the"
                             "question.")

        # Format of i[0] would be "<question> <?> <typed answer or not>"
        # question = [<question>, <type>]
        # if there is no 'T', then the question is assumed to be not typed
        question_split = question.split('?')
        question_and_answer = (question_split[0] + '?', answer)

        if (len(question_split) > 1 and
                question_split[1].strip().lower() == "t"):
            # i[1] is the answer in (question, answer)
            typed_questions.append(question_and_answer)
        else:
            non_typed_questions.append(question_and_answer)

    return typed_questions, non_typed_questions


def _check_QA_is_valid(entry: tuple):
    """Checks whether a QA entry is valid.

    Args:
        entry ([tuple]): a tuple in the format of (question, answer)
    """

    if '?' not in entry[0]:
        print("Error at question {}".format(entry[0]))
        raise ValueError("An entry does not have a question mark in its"
                         "question")

    return True
