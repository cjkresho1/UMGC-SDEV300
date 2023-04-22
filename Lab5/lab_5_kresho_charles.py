"""This application allows the user to interact with data about housing and population change.
Charles Kresho, 04/17/23
"""

import statistics as stats
from matplotlib import pyplot as plt

# Global variables for the popchange and housing csv's
popchange_list = []
housing_list = []


def load_popchange_csv():
    """
    Load in the data from PopChange.csv, stored in the global popchange_list.
    Storage popchange_list is a 2D list, a list of lists!
    :return: Nothing
    """
    with open("PopChange.csv", 'r', encoding="UTF-8") as input_file:
        # Lines are formatted as such:
        # Id,Geography,Target Geo Id,Target Geo Id2,Pop Apr 1,Pop Jul 1,Change Pop
        # [4] = Pop Apr 1
        # [5] = Pop Jul 1
        # [6] = Change Pop
        input_file.readline()
        while True:
            # For each line, trip and split on commas, store in list
            line = input_file.readline()
            line = line.strip()
            if len(line) == 0:  # Break at end line
                break
            split_line = line.split(',')
            popchange_list.append(split_line)


def load_housing_csv():
    """
    Load in the data from Housing.csv, stored in the global housing_list.
    Storage housing_list is a 2D list, a list of lists!
    :return: Nothing
    """
    with open("Housing.csv", 'r', encoding="UTF-8") as input_file:
        # Lines are formatted as such:
        # AGE,BEDRMS,BUILT,NUNITS,ROOMS,WEIGHT,UTILITY
        # [0] = AGE
        # [1] = BEDRMS
        # [2] = BUILT
        # [4] = ROOMS
        # [6] = UTILITY
        input_file.readline()
        while True:
            # For each line, trip and split on commas, store in list
            line = input_file.readline()
            line = line.strip()
            if len(line) == 0:  # Break at end line
                break
            split_line = line.split(',')
            housing_list.append(split_line)


def print_menu_popchange():
    """
    Print out the menu for interacting with the popchange data.
    :return: Nothing
    """
    print("Select the Column you want to analyze:")
    print("a. Pop Apr 1")
    print("b. Pop Jul 1")
    print("c. Change Pop")
    print("d. Exit Column")


def analyze_popchange():
    """
    The machine state for interacting with the popchange data.
    :return: Nothing
    """
    while True:
        print_menu_popchange()
        user_char = get_char("Enter the letter choice you want: ")
        print()
        if user_char == 'a':  # Pop Apr 1 data
            attribute_index = 4
            plt.title("Pop Apr 1")
            print("You selected Pop Apr 1")
        elif user_char == 'b':  # Pop Jul 1 data
            attribute_index = 5
            plt.title("Pop Jul 1")
            print("You selected Pop Jul 1")
        elif user_char == 'c':  # Change Pop data
            attribute_index = 6
            plt.title("Change Pop")
            print("You selected Change Pop")
        elif user_char == 'd':  # Exit this and return to the main menu
            return
        else:  # Invalid menu selection
            attribute_index = -1
            print("Invalid menu choice, please try again.")

        if not attribute_index == -1:
            cur_list = []
            count = len(popchange_list)

            # Calculate min/max, and create a list of only the data to be analyzed
            minimum = float(popchange_list[0][attribute_index])
            maximum = float(popchange_list[0][attribute_index])
            for i in range(count):
                cur_list.append(float(popchange_list[i][attribute_index]))
                if cur_list[i] > maximum:
                    maximum = cur_list[i]
                if cur_list[i] < minimum:
                    minimum = cur_list[i]

            mean = stats.mean(cur_list)
            std_div = stats.stdev(cur_list)

            # Output data and a histogram
            print(f'Count = {count:.0f}')
            print(f'Mean = {mean:.1f}')
            print(f'Standard = {std_div:.1f}')
            print(f'Min = {minimum:.1f}')
            print(f'Max = {maximum:.1f}')
            print()
            plt.hist(cur_list)
            plt.axis("on")
            plt.grid(True)
            plt.show()


def print_menu_housing():
    """
    Print out the menu for interacting with the housing data.
    :return: Nothing
    """
    print("Select the Column you want to analyze:")
    print("a. House Age")
    print("b. Bedrooms Count")
    print("c. Year Built")
    print("d. Room Count")
    print("e. Utility")
    print("f. Exit Column")


def analyze_housing():
    """
    The machine state for interacting with the housing data.
    :return: Nothing
    """
    while True:
        print_menu_housing()
        user_char = get_char("Enter the letter choice you want: ")
        print()
        if user_char == 'a':  # House Age data
            attribute_index = 0
            plt.title("House Age")
            print("You selected House Age")
        elif user_char == 'b':  # Bedroom num data
            attribute_index = 1
            plt.title("Bedrooms Count")
            print("You selected Bedrooms Count")
        elif user_char == 'c':  # Year data
            attribute_index = 2
            plt.title("Year Built")
            print("You selected Year Built")
        elif user_char == 'd':  # Room data
            attribute_index = 4
            plt.title("Room Count")
            print("You selected Room Count")
        elif user_char == 'e':  # Utility data
            attribute_index = 6
            plt.title("Utility")
            print("You selected Utility")
        elif user_char == 'f':
            return
        else:  # Invalid menu selection
            attribute_index = -1
            print("Invalid menu choice, please try again.")

        if not attribute_index == -1:
            cur_list = []
            count = len(housing_list)

            # Calculate min/max, and create a list of only the data to be analyzed
            minimum = float(housing_list[0][attribute_index])
            maximum = float(housing_list[0][attribute_index])
            for i in range(count):
                cur_list.append(float(housing_list[i][attribute_index]))
                if cur_list[i] > maximum:
                    maximum = cur_list[i]
                if cur_list[i] < minimum:
                    minimum = cur_list[i]

            mean = stats.mean(cur_list)
            std_div = stats.stdev(cur_list)

            # Output data and a histogram
            print(f'Count = {count:.0f}')
            print(f'Mean = {mean:.1f}')
            print(f'Standard = {std_div:.1f}')
            print(f'Min = {minimum:.1f}')
            print(f'Max = {maximum:.1f}')
            print()
            plt.hist(cur_list)
            plt.axis("on")
            plt.grid(True)
            plt.show()


def get_integer(int_prompt="Enter a whole number:"):
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


def get_char(char_prompt="Enter a letter: "):
    """
    Get an integer from the user.
    :param char_prompt: Prompt to be printed to the user
    :return: A char from the user
    """
    while True:
        try:
            user_char = input(char_prompt)
            if not len(user_char) == 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid input, please enter a single letter.")

    return user_char[0]


def print_menu_top():
    """
    Print out the main menu.
    :return: Nothing
    """
    print("Select the file you want to analyze:")
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program")


if __name__ == '__main__':
    load_popchange_csv()
    load_housing_csv()
    print("********** Welcome to the Python Data Analysis App **********")

    while True:
        print_menu_top()
        user_choice = get_integer("Enter your choice: ")
        print()
        if user_choice == 1:
            analyze_popchange()
            print("You selected to exit the column menu")
        elif user_choice == 2:
            analyze_housing()
            print("You selected to exit the column menu")
        elif user_choice == 3:
            break
        else:
            print("Invalid menu input.")
    print("********** Thanks for using the Data Analysis App **********")
