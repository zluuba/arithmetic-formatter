from arithmetic_formatter.arithmetic_arranger import arranger, AppError
import pytest


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


def test_arranger_correct_data():
    assert arranger(CORRECT_INPUT) == CORRECT_OUTPUT
    assert arranger(CORRECT_INPUT, display_result=True) == CORRECT_OUTPUT_WITH_RESULT


def test_arranger_incorrect_data():
    with pytest.raises(AppError) as incorrect_input_length:
        arranger(INCORRECT_INPUT_LENGTH)
        assert "Too many problems." in str(incorrect_input_length.value)

    with pytest.raises(AppError) as incorrect_operators:
        arranger(INCORRECT_OPERATORS)
        assert "Operator must be '+' or '-'." in str(incorrect_operators.value)

    with pytest.raises(AppError) as incorrect_operands:
        arranger(INCORRECT_OPERANDS)
        assert "Numbers must only contain digits." in str(incorrect_operands.value)

    with pytest.raises(AppError) as incorrect_number_length:
        arranger(INCORRECT_NUM_LENGTHS)
        assert "Numbers cannot be more than four digits." in str(incorrect_number_length.value)
