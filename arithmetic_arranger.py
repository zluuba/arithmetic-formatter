class AppError(Exception):
    pass


def is_correct_operator(operator):
    if operator in {'+', '-'}:
        return True
    return False


def is_correct_operands(num1, num2):
    if not num1.isdigit() or not num2.isdigit():
        return False
    return True


def is_correct_number_length(num1, num2):
    if len(num1) > 4 or len(num2) > 4:
        return False
    return True


def get_formatted_problem(num1, num2, operator, display_result):
    length_num1 = len(num1)
    length_num2 = len(num2)
    max_num_length = max(length_num1, length_num2)
    max_line_length = max_num_length + 2

    first_row = num1.rjust(max_line_length)
    second_row = operator + (' ' * (max_line_length - length_num2 - 1)) + num2
    dashes = '-' * max_line_length

    if display_result:
        if operator == '+':
            result = str(int(num1) + int(num2))
        else:
            result = str(int(num1) - int(num2))
        result_line = ' ' * (max_line_length - len(result)) + result
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

    # result = ''
    for i in range(len(lines[0])):
        for line in lines:
            # result += line[i] + '    '
            print(line[i], end='    ')
        # result += '\n'
        print()
