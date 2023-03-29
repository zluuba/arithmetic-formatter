from arithmetic_formatter.core import arranger, AppError
import unittest


CORRECT_INPUT = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
CORRECT_OUTPUT = '''   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----'''

CORRECT_OUTPUT_WITH_RESULT = '''   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172'''

INCORRECT_INPUT_LENGTH = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "3 + 439", "73 + 906"]
INCORRECT_OPERATORS = ["32 * 698", "3801 / 2", "45 - 43", "123 + 49"]
INCORRECT_OPERANDS = ["3^2 + 698", "3801 - 2", "4)5 + 43", "12=3 + 49"]
INCORRECT_NUM_LENGTHS = ["32 + 69899", "3805551 - 2", "45 + 43", "123 + 49"]


class UnitTests(unittest.TestCase):
    def test_arranger_correct_data(self):
        result = arranger(CORRECT_INPUT)
        expected = CORRECT_OUTPUT
        self.assertEqual(result, expected)

        result = arranger(CORRECT_INPUT, display_result=True)
        expected = CORRECT_OUTPUT_WITH_RESULT
        self.assertEqual(result, expected)

    def test_arranger_incorrect_input_length(self):
        with self.assertRaises(AppError) as incorrect_input_length:
            arranger(INCORRECT_INPUT_LENGTH)

        result = str(incorrect_input_length.exception)
        self.assertEqual(result, "Too many problems.")

    def test_arranger_incorrect_operators(self):
        with self.assertRaises(AppError) as incorrect_operators:
            arranger(INCORRECT_OPERATORS)

        result = str(incorrect_operators.exception)
        self.assertEqual(result, "Operator must be '+' or '-'.")

    def test_arranger_incorrect_operands(self):
        with self.assertRaises(AppError) as incorrect_operands:
            arranger(INCORRECT_OPERANDS)

        result = str(incorrect_operands.exception)
        self.assertEqual(result, "Numbers must only contain digits.")

    def test_arranger_incorrect_number_length(self):
        with self.assertRaises(AppError) as incorrect_number_length:
            arranger(INCORRECT_NUM_LENGTHS)

        result = str(incorrect_number_length.exception)
        self.assertEqual(result, "Numbers cannot be more than four digits.")


if __name__ == "__main__":
    unittest.main()
