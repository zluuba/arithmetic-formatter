CORRECT_OPERATORS = {'+', '-'}
MAX_NUMBER_LENGTH = 4
SPACE = ' '
SPACES_SEPARATOR = SPACE * 4


class AppError(Exception):
    pass


def is_correct_operator(operator):
    if operator in CORRECT_OPERATORS:
        return True
    return False


def is_correct_operands(num1, num2):
    if not num1.isdigit() or not num2.isdigit():
        return False
    return True


def is_correct_number_length(num1, num2):
    if len(num1) > MAX_NUMBER_LENGTH or \
            len(num2) > MAX_NUMBER_LENGTH:
        return False
    return True


def get_formatted_problem(num1, num2, operator, display_result):
    max_num_length = max(len(num1), len(num2))
    max_line_length = max_num_length + 2

    first_row = num1.rjust(max_line_length)
    second_row = operator + (SPACE * (max_line_length - len(num2) - 1)) + num2
    dashes = '-' * max_line_length

    if display_result:
        if operator == '+':
            result = str(int(num1) + int(num2))
        else:
            result = str(int(num1) - int(num2))
        result_line = SPACE * (max_line_length - len(result)) + result
        return [first_row, second_row, dashes, result_line]

    return [first_row, second_row, dashes]


def arranger(arithmetic_problems, display_result=False):
    if len(arithmetic_problems) > 5:
        raise AppError("Too many problems.")

    checked_problems = []
    for problem in arithmetic_problems:
        num1, operator, num2 = problem.split()

        if not is_correct_operator(operator):
            raise AppError("Operator must be '+' or '-'.")

        if not is_correct_operands(num1, num2):
            raise AppError("Numbers must only contain digits.")

        if not is_correct_number_length(num1, num2):
            raise AppError("Numbers cannot be more than four digits.")

        checked_problems.append([num1, num2, operator, display_result])

    lines = []
    for problem in checked_problems:
        line = get_formatted_problem(*problem)
        lines.append(line)

    result = ''
    for i in range(len(lines[0])):
        result_line = ''
        for line in lines:
            result_line += line[i] + SPACES_SEPARATOR
        result += result_line.rstrip() + '\n'

    return result.strip('\n')
