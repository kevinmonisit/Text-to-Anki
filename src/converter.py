"""
Converts text to anki
"""

from os import error
import warnings

STARTHERE_KEY = "STARTHERE"


def get_lines(file_dir, STARTHERE_key_exists=False) -> list:
    """ Creates a list of lines from a text file.
        If the line "IGNOREUP" exists, then exclude all lines
        beforehand and only return the lines after.

    Args:
        file_dir ([str]): the path to the source file
        STARTHERE_key_exists (bool, optional): If true, the method will
        look for the key. If not found, an error will be raised.
        Defaults to False.

    Returns:
        list: [description]
    """

    file = open(file_dir)
    lines = []

    line = file.readline()

    while line:
        if not line:
            break

        lines.append(line.strip())
        line = file.readline()

    # starting from the bottom of the text file
    # search for the ignore key.
    # the line where the ignore key is will be the starting point

    if(STARTHERE_key_exists):
        index = len(lines) - 1
        while index > 0:
            if(lines[index].strip() == STARTHERE_KEY):
                print("THE STARTHERE KEY WAS FOUND")
                # index + 1 in order to ignore the ignore key
                # and return the rest of the file
                return lines[(index+1):len(lines)]

            index -= 1

        raise Exception("STARTHERE_key_exists = True but STARTHERE_KEY was not"
                        "found in the source.")

    # index + 1 in order to ignore the ignore key
    return lines


def convert_to_anki(content) -> tuple:
    """
    Converts data from a read text file into anki-importable text.

    Returns a tuple of two lists. First list contains
    all questions that have answers that are supposed to be typed
    and the second contains QAs that are not typed.

    Args:
        content ([list]): contains the lines of a source file that contains
        the questions and answers

    Returns:
        tuple of two lists: QAS with typed answers
        and QAs without typed answers
    """

    cards = _convert_to_tuples(content)
    typed, non_typed = _divide_tuples_by_type(cards)

    return _convert_tuples_to_anki(typed), _convert_tuples_to_anki(non_typed)


def _convert_to_tuples(lines) -> list:
    """Converts the lines that are in a text file into question and answer
       tuples (question, answer)

    Args:
        lines ([type]): [description]

    Returns:
        [list]: list of QAs in tuples --> (question, answer)
    """
    QUESTION = 1
    ANSWER = 0

    look_for = QUESTION

    cards = []
    question = ""
    answer = ""

    for i in lines:

        if len(i) < 1:
            continue

        if look_for == QUESTION:
            question = i
            look_for = ANSWER

        elif look_for == ANSWER:
            answer = i

            _QA = (question, answer)
            # _check_QA_is_valid(_QA)
            cards.append(_QA)

            look_for = QUESTION

    return cards


def _convert_tuples_to_anki(data) -> str:
    """
    Converts tuples that are in a (Question, Answer) format
    into a string that is Anki-readable and can be
    imported into Anki.

    (Question, Answer) converts to Question;Answer.

    Args:
        data ([list]): A list of tuples in a (Question, Answer) format.

    Returns:
        [str]: A string is returned that is in a format that
        can be read by Anki. E.g. what is 2 + 2?;4
    """

    content = ""
    index = 0

    while index < len(data):
        entry = "{};{}\n".format(data[index][0], data[index][1])
        content += entry

        index += 1

    return content


def _divide_tuples_by_type(tuples_list) -> tuple:
    """

        Tests the functionality of adding a sign that the card's
        answer is meant to be typed or not.

        If there is a 'T' or 't', the answer will be typed.

        Function returns a tuple containing (list of typed cards, list
        of non-typed cards) in the format (Question, Answer)

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
