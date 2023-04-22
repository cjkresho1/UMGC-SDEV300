"""A program that gives use of matrix operations.
Charles Kresho, 04/11/23
"""

import re
import statistics as stats
import numpy


def get_user_phone_number():
    """
    Gets the user's phone number; must be formatted exactly
    Loops until success.
    :return: None
    """
    phone_string = input("Enter your phone number (XXX-XXX-XXXX): ")
    while True:
        # Remove any non-numeric characters
        phone_number = re.match(r'\d{3}-\d{3}-\d{4}', phone_string)
        # A phone number is only valid if it contains 10 characters
        if phone_number is not None:
            break
        phone_string = input("Your phone number is not formatted properly. Please renter: ")


def get_zip_plus_four():
    """
    Gets the user's zip code+4; must be formatted exactly
    Loops until success.
    :return: None
    """
    zip_string = input("Enter your zip code+4 (XXXXX-XXXX): ")
    while True:
        # Remove any non-numeric characters
        zip_code = re.match(r'\d{5}-\d{4}', zip_string)
        # A zip code+4 is only valid if it contains 9 characters
        if zip_code is not None:
            break
        zip_string = input("Your zip code+4 is not formatted properly. Please renter: ")


def get_3x3_matrix():
    """
    Returns a 3x3 list of digits (matrix) from the user. Throws ValueError on improper input.
    Uses Reg-ex to accept any non-alphanumeric character as a seperator in each line.
    :return: a 3x3 matrix from the user.
    """
    first_line = []
    second_line = []
    third_line = []

    valid_matrix = False
    # Loop until successful
    while not valid_matrix:
        valid_matrix = True

        # For each line, break into a list, where delimiters are any non-alphanumeric character
        first_line = re.split(r'[^a-zA-Z0-9]+', input())
        second_line = re.split(r'[^a-zA-Z0-9]+', input())
        third_line = re.split(r'[^a-zA-Z0-9]+', input())

        # Ensure proper length
        if not len(first_line) == 3:
            valid_matrix = False
            print("Your first line did not have exactly three elements.")
        if not len(second_line) == 3:
            valid_matrix = False
            print("Your second line did not have exactly three elements.")
        if not len(third_line) == 3:
            valid_matrix = False
            print("Your third line did not have exactly three elements.")

    # Can throw ValueError on improper input.
    for i in range(3):
        first_line[i] = float(first_line[i])
        second_line[i] = float(second_line[i])
        third_line[i] = float(third_line[i])

    return [first_line, second_line, third_line]


def matrix_addition(x_1=None, x_2=None):
    """
    Performs matrix addition on two matrices.
    Throws an error if the matricies are not the same size.
    :param x_1: A 3x3 matrix
    :param x_2: A 3x3 matrix
    :return: The two matricies added together
    """
    if x_2 is None:
        x_2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    if x_1 is None:
        x_1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    return numpy.add(x_1, x_2)


def matrix_subtraction(x_1=None, x_2=None):
    """
    Performs matrix subtraction on two matrices.
    Throws an error if the matricies are not the same size.
    :param x_1: A 3x3 matrix
    :param x_2: A 3x3 matrix
    :return: The second matrix subtracted from the first
    """
    if x_2 is None:
        x_2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    if x_1 is None:
        x_1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    return numpy.subtract(x_1, x_2)


def matrix_multiplication(x_1=None,
                          x_2=None):
    """
    Performs matrix multiplication on two matrices.
    Throws an error if the matricies don't have matching inside dimensions
    :param x_1: A 3x3 matrix
    :param x_2: A 3x3 matrix
    :return: The product of the two matrices
    """
    if x_1 is None:
        x_1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    if x_2 is None:
        x_2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    return numpy.matmul(x_1, x_2)


def matrix_element_multiplication(x_1=None,
                                  x_2=None):
    """
    Performs element by element multiplication on two matrices.
    Throws an error if the matricies don't have the same dimensions
    :param x_1: A 3x3 matrix
    :param x_2: A 3x3 matrix
    :return: The element by element product of the two matrices
    """
    if x_2 is None:
        x_2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    if x_1 is None:
        x_1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    return numpy.multiply(x_1, x_2)


def matrix_transpose(x_1=None):
    """
    Transposes the input matrix
    :param x_1: A 3x3 matrix
    :return: The transposed matrix
    """
    if x_1 is None:
        x_1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    return numpy.transpose(x_1)


def matrix_row_mean(x_1=None):
    """
    Prints a list with the mean of each row of a matrix.
    :param x_1: A 3x3 matrix
    :return: None
    """
    if x_1 is None:
        x_1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    first_row = stats.mean(x_1[0])
    second_row = stats.mean(x_1[1])
    third_row = stats.mean(x_1[2])

    print(f"Row: {first_row:.2f} {second_row:.2f} {third_row:.2f}")


def matrix_column_mean(x_1=None):
    """
    Prints a list with the means of each column
    :param x_1: A 3x3 matrix
    :return: None
    """
    if x_1 is None:
        x_1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    x_1 = numpy.transpose(x_1)
    first_row = stats.mean(x_1[0])
    second_row = stats.mean(x_1[1])
    third_row = stats.mean(x_1[2])

    print(f"Column: {first_row:.2f} {second_row:.2f} {third_row:.2f}")


def print_matrix(x_1=None):
    """
    Prints a formatted display of a matrix
    :param x_1: A 3x3 matrix
    :return: None
    """
    if x_1 is None:
        x_1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for i in range(3):
        print(f'{x_1[i][0]:.2f} {x_1[i][1]:.2f} {x_1[i][2]:.2f}')


def print_operations_menu():
    """
    Prints a list of menu options.
    :return: None
    """
    print("Select a Matrix Operation from the list below: ")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Matrix Multiplication")
    print("4: Element by element multiplication")


def get_yes_no(prompt):
    """
    Converts a yes/no input from the user into True/False
    Accepts yes/y/no/n of any case.
    :param prompt: Prompt to be printed to the user
    :return: True/False
    """
    while True:
        val = input(prompt)
        val = val.lower()

        if val in ('yes', 'y'):
            is_yes = True
            break
        if val in ('no', 'n'):
            is_yes = False
            break
        print("Invalid input, enter either yes/no.")

    return is_yes


def get_integer(int_prompt):
    """
    Get an integer from the user.
    :param int_prompt: Prompt to be printed to the user
    :return: An integer from the user
    """
    while True:
        try:
            user_int = int(input(int_prompt))
            break
        except ValueError:
            print("Invalid input, please enter a whole number.")

    return user_int


if __name__ == '__main__':
    print("***************** Welcome to the Python Matrix Application *****************")
    while True:
        print("Do you want to play the Matrix Game?")

        # Exit the program when the user enters no
        if not get_yes_no("Enter Y for Yes or N for No: "):
            break
        get_user_phone_number()
        get_zip_plus_four()

        # Loop until the user enters a valid 3x3 matrix
        while True:
            print("Enter your first 3x3 matrix: ")
            try:
                matrix_1 = get_3x3_matrix()
                break
            except ValueError:
                print("Please enter numbers only for the matrix entries.")
        print("Your first 3x3 matrix is:")
        print_matrix(matrix_1)

        # Loop until the user enters a valid 3x3 matrix
        while True:
            print("Enter your second 3x3 matrix: ")
            try:
                matrix_2 = get_3x3_matrix()
                break
            except ValueError:
                print("Please enter numbers only for the matrix entries.")
        print("Your second 3x3 second is:")
        print_matrix(matrix_2)

        # Allow the user to select one operation to be done of the input matrices
        print_operations_menu()
        matrix_result = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        operations_menu_selection = get_integer("Enter your selection: ")
        while True:
            if operations_menu_selection == 1:
                print("You selected Addition. The results are: ")
                result_matrix = matrix_addition(matrix_1, matrix_2)
                break
            if operations_menu_selection == 2:
                print("You selected Subtraction. The results are: ")
                result_matrix = matrix_subtraction(matrix_1, matrix_2)
                break
            if operations_menu_selection == 3:
                print("You selected Matrix Multiplication. The results are: ")
                result_matrix = matrix_multiplication(matrix_1, matrix_2)
                break
            if operations_menu_selection == 4:
                print("You selected Element Multiplication. The results are: ")
                result_matrix = matrix_element_multiplication(matrix_1, matrix_2)
                break
            print("")

        # Print the result of the above operation, the transpose, and the row and column means
        print_matrix(result_matrix)
        print("The Transpose is: ")
        print_matrix(matrix_transpose(result_matrix))
        print("The row and column mean values of the results are: ")
        matrix_row_mean(result_matrix)
        matrix_column_mean(result_matrix)

    print("***************** Thanks for playing Python Numpy *****************")
