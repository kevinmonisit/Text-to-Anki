"""Tests basic reading and writing Anki card functionality
"""

import unittest
from src import converter
import os

# @TODO:
# Make tests more comprehensive. Lean away from creating a new file
# and using the hard-coded questions.


class TestBasic(unittest.TestCase):

    def setUp(self):
        self.test_content = "What is my name?\n\nKevin\n\n2+2=?\n\n4"
        self.test_file_name = "./tests/__tester__.txt"
        self.questions = ["1? @T",
                          "2? ",
                          "3? @NT",
                          "4?@T ",
                          "5 @T"]

        self.test_QAs = []
        self.test_answer = "test answer"

        for i in self.questions:
            self.test_QAs.append((i, self.test_answer))

    def _write_test_file(self):
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)
        else:
            print("Removed file {}".format(self.test_file_name))

        f = open(self.test_file_name, "w")
        f.write(self.test_content)
        f.close()

    def test_get_lines(self):
        self._write_test_file()

        content = converter.get_lines(self.test_file_name)

        expected_content = ["What is my name?", '', "Kevin", '',
                            "2+2=?", '', "4"]

        self.assertEqual(content, expected_content)

    def test_convert_list_to_tuples(self):
        self._write_test_file()

        content = converter.get_lines(self.test_file_name)
        content = converter._convert_to_tuples(content)

        expected_content = [("What is my name?", "Kevin"),
                            ("2+2=?", "4")]

        self.assertEqual(content, expected_content)

    # tests that are yet to be implemented.
    def test_typed_answers_error(self):
        content = [("What is my name @G", "Kevin")]

        with self.assertWarns(UserWarning):
            converter._divide_tuples_by_type(content)

    def test_typed_answers(self):
        content = [("What is my name? ", "Kevin"),
                   ("2 + 2 = ? @NT", "4")]

        data = converter._divide_tuples_by_type(content)

        # expected return value is a tuple containing lists
        # within each list are tuples in the (question, answer) format
        # first lists are typed, second list are not typed
        expected_data = ([("What is my name?", "Kevin")],
                         [("2 + 2 = ?", "4")])

        self.assertEqual(data, expected_data)

    def test_typed_answers_output(self):
        # TODO: Make the question list an instance of this class
        # so that it can be used in other test functions

        typed, non_typed = converter._divide_tuples_by_type(self.test_QAs)

        # expected content will be two lists: one of typed and non-typed
        # answers
        expected_typed = [("1?", self.test_answer),
                          ("2?", self.test_answer),
                          ("4?", self.test_answer),
                          ("5", self.test_answer)]

        expected_non_typed = [("3?", self.test_answer)]

        self.assertEqual(typed, expected_typed)
        self.assertEqual(expected_non_typed, non_typed)

    def test_removal_of_possible_tokens(self):
        # could most likely share questions list with
        # test_typed_answers_output test
        questions = ["First, ", "Second",
                     "Third@T", "Fourth@T ",
                     "Fifth @TT", "Sixth @@T",
                     "Seventh @NT ", "Eight @NT @NT"]

        TYPED = converter.TYPED
        NOT_TYPED = converter.NOT_TYPED
        expect = [("First, ", None),
                  ("Second", None),
                  ("Third", TYPED),
                  ("Fourth", TYPED),
                  ("Fifth ", None),
                  ("Sixth ", TYPED),
                  ("Seventh ", NOT_TYPED),
                  ("Eight ", NOT_TYPED)]

        output_questions = []
        for i in questions:
            output_questions.append(converter._remove_token(i))

        self.assertEqual(output_questions, expect)

    def test_question_suffix(self):
        self._write_test_file()
        content = converter.get_lines(self.test_file_name)

        typed, not_typed = converter.convert_to_anki(content, "NOTE")
        # self.test_content = "What is my name?\n\nKevin\n\n2+2=?\n\n4"
        expected = ("What is my name? <strong>NOTE</strong>;Kevin\n2+2=? "
                    "<strong>NOTE</strong>;4\n")

        self.assertEqual(typed, expected)

    def test_ignore_up_key(self):
        """
        Successfully ignore lines above ignore up key.
        """
        pass

    def test_ignore_key_errors(self):
        """
        In cases of multiple ignore-up keys, incorrect placement, etc.,
        raise an error.
        """
        pass


class TestParsing(unittest.TestCase):

    def _create_cards_from_test_files(self):
        test_file_1 = converter.get_lines('./tests/samples/dynamic1.txt',
                                          STARTHERE_key_exists=True)

        test_file_2 = converter.get_lines('./tests/samples/dynamic2.txt',
                                          STARTHERE_key_exists=True)

        cards_1 = converter._convert_to_tuples(test_file_1)
        cards_2 = converter._convert_to_tuples(test_file_2)

        return cards_1, cards_2

    def test_dynamic_QA_parsing(self):
        """
        Tests that the number of question and answer pairs are correct
        """
        cards_1, cards_2 = self._create_cards_from_test_files()

        self.assertEqual(6, len(cards_1))
        self.assertEqual(6, len(cards_2))

    def test_QA_content(self):
        """
        Tests whether the content in dynamic1.txt and dynamic2.txt is
        parsed correctly and the content is what is expected.
        """

        content = self._create_cards_from_test_files()

        # card lists containts tuples of (question, answer)
        for card_list in content:
            for QA_entry in card_list:
                test = (QA_entry[0].strip() == "Question" and
                        QA_entry[1].strip() == "Answer")

                self.assertTrue(test)


if __name__ == "__main__":
    unittest.main()
