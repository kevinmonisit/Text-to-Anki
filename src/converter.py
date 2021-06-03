"""
Converts text to anki
"""

from os import error
import warnings

STARTHERE_KEY = "STARTHERE"

# card-type ID
TYPED = 0
NOT_TYPED = 1

DEFAULT_ANSWER_TYPE = TYPED
TYPED_ANSWER_TOKEN = "T"
NON_TYPED_ANSWER_TOKEN = "NT"


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


def _divide_tuples_by_type(tuples_list_of_cards) -> tuple:
    """

        Tests the functionality of adding a sign that the card's
        answer is meant to be typed or not. There are two meanings of 'type'
        being used: the classification of a card and whether or not
        the card is supposed to have a 'typed' answer.

        If there is a 'T' or 't', the answer will be typed.

        Function returns a tuple containing (list of typed cards, list
        of non-typed cards) in the format (Question, Answer)

    Args:
        lines ([list]): Receives list of tuples in (question, answer) format

    Returns:
        [tuple]: (list of typed QAs, list of non-typed QAs)
    """

    typed_questions = []
    non_typed_questions = []

    # tuples_list_of_cards = [(question, answer) ... ]
    for i in tuples_list_of_cards:

        question, possible_token = _remove_token(i[0])

        QA_ = (question.strip(), i[1])

        if(possible_token is None):
            if DEFAULT_ANSWER_TYPE == TYPED:
                typed_questions.append(QA_)
            else:
                non_typed_questions.append(QA_)

            continue

        if (possible_token == TYPED):
            typed_questions.append(QA_)
        elif(possible_token == NOT_TYPED):
            non_typed_questions.append(QA_)
        else:
            raise ValueError(
                "Token is {}, which should not be possible".format(
                    possible_token))

    return typed_questions, non_typed_questions


def _remove_token(question) -> str:
    """
    This is a helper function to _divide_tuples_by_type.
    Removes and returns the token at the end of a question that determines
    whether the answer is meant to be typed or not, if any.

    Args:
        question ([str]): question literal that derives from a
        (question, answer) tuple pair.

    Returns:
        str: returns both the new question literal and the token removed. If
             token does not exist, it will return None.
    """
    if(question.find('@') == -1):
        return question, None

    _question = question.split('@')

    question_without_token = _question[0]

    # token may or may note exist
    possible_token = _question[len(_question) - 1].strip().lower()
    # put warning if there is an @ char but an incorrect type ID

    if possible_token == TYPED_ANSWER_TOKEN.lower():
        return question_without_token, TYPED
    elif possible_token == NON_TYPED_ANSWER_TOKEN.lower():
        return question_without_token, NOT_TYPED
    else:
        warnings.warn("A \'@\' is found in a question without a valid token. \
                      The question is {}. If intended, ignore this warning.".
                      format(
                          question[0]
                      ))
        return question_without_token, None
