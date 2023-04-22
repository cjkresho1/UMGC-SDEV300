"""Provides the user with information regarding states, their capital, population, and flowers.
Charles Kresho, 04/03/2023, UMGC SDEV 300/7380
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Stores the following information for each US state in a list of Tuples:
# (STATE_NAME, STATE_CAPITAL, STATE_POPULATION_2023, STATE_FLOWER)
# List is sorted alphabetically.
# Source for state population: https://worldpopulationreview.com/states/state-capitals
# Source for state flower names and pictures: https://statesymbolsusa.org/categories/flower

STATE_INFO = {
    "Alabama": ("Montgomery", 199055, "Camellia"),
    "Alaska": ("Juneau", 32549, "Forget Me Not"),
    "Arizona": ("Phoenix", 1656892, "Saguaro Cactus Blossom"),
    "Arkansas": ("Little Rock", 205312, "Apple Blossom"),
    "California": ("Sacramento", 542481, "California Poppy"),
    "Colorado": ("Denver", 750130, "Colorado Lavender Columbine"),
    "Connecticut": ("Hartford", 119938, "Mountain Laurel"),
    "Delaware": ("Dover", 40411, "Peach Blossom"),
    "Florida": ("Tallahassee", 200606, "Orange Blossom"),
    "Georgia": ("Atlanta", 522328, "Cherokee Rose"),
    "Hawaii": ("Honolulu", 355077, "Hawaiian Hibiscus"),
    "Idaho": ("Boise", 244687, "Syringa"),
    "Illinois": ("Springfield", 113836, "Violet"),
    "Indiana": ("Indianapolis", 907802, "Peony"),
    "Iowa": ("Des Moines", 217343, "Wild Prairie Rose"),
    "Kansas": ("Topeka", 126320, "Sunflower"),
    "Kentucky": ("Frankfort", 29526, "Goldenrod"),
    "Louisiana": ("Baton Rouge", 226864, "Magnolia"),
    "Maine": ("Augusta", 18827, "White Pine Cone and Tassel"),
    "Maryland": ("Annapolis", 41538, "Black-Eyed Susan"),
    "Massachusetts": ("Boston", 693062, "Mayflower"),
    "Michigan": ("Lansing", 112149, "Apple Blossom"),
    "Minnesota": ("St. Paul", 319465, "Pink and White Lady Slipper"),
    "Mississippi": ("Jackson", 147758, "Magnolia"),
    "Missouri": ("Jefferson City", 43273, "Hawthorn"),
    "Montana": ("Helena", 33261, "Bitterroot"),
    "Nebraska": ("Lincoln", 300892, "Goldenrod"),
    "Nevada": ("Carson City", 59647, "Sagebrush"),
    "New Hampshire": ("Concord", 44360, "Purple Lilac"),
    "New Jersey": ("Trenton", 92659, "Violet"),
    "New Mexico": ("Santa Fe", 93373, "Yucca Flower"),
    "New York": ("Albany", 99635, "Rose"),
    "North Carolina": ("Raleigh", 486796, "Dogwood"),
    "North Dakota": ("Bismarck", 77327, "Wild Prairie Rose"),
    "Ohio": ("Columbus", 941364, "Scarlet Carnation"),
    "Oklahoma": ("Oklahoma City", 711372, "Oklahoma Rose"),
    "Oregon": ("Salem", 181805, "Oregon Grape"),
    "Pennsylvania": ("Harrisburg", 50270, "Mountain Laurel"),
    "Rhode Island": ("Providence", 194801, "Violet"),
    "South Carolina": ("Columbia", 138840, "Yellow Jessamine"),
    "South Dakota": ("Pierre", 14223, "Pasque Flower"),
    "Tennessee": ("Nashville", 715913, "Iris"),
    "Texas": ("Austin", 1013293, "Bluebonnet"),
    "Utah": ("Salt Lake City", 203707, "Sego Lily"),
    "Vermont": ("Montpelier", 8140, "Red Clover"),
    "Virginia": ("Richmond", 233330, "Dogwood"),
    "Washington": ("Olympia", 58344, "Coast Rhododendron"),
    "West Virginia": ("Charleston", 48102, "Rhododendron"),
    "Wisconsin": ("Madison", 280829, "Wood Violet"),
    "Wyoming": ("Cheyenne", 66833, "Indian Paintbrush")
}


def display_all_states_info():
    """Prints a formatted list of all the states and their information.
    Output is formatted in alphabetical order...if the dictionary is in alphabetical order.
    """

    # Display titles for the information
    print(f'{"State":<20}{"Capital":<20}{"Population":<20}{"State Flower"}')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # For each element in the dictionary, print the state, followed by the capital, pop, and flower
    for state, info in STATE_INFO.items():
        print(f'{state:<20}{info[0]:<20}{info[1]:<20,d}{info[2]}')


def display_one_state_info(state_name=""):
    """If the state is in the Dictionary, print its information and the state flower's picture.
    State Flowers picture must be located at: './stateFlowerImages/[state flower name]'
    """
    # Print error message if the passed state is not a state.
    if state_name not in STATE_INFO:
        print(f"{state_name} is not one of the 50 U.S. states.")
    else:
        # Print the state information.
        state_info = STATE_INFO.get(state_name)
        print(f"Info for {state_name}")
        print(f"State Capital: {state_info[0]}")
        print(f"State Population: {state_info[1]:,d}")
        print("Please close the image of the state flower to continue.")

        # Display a "graph" of the state flower image.
        # Image files are named the same as the flower stored in STATE_INFO + ".png".
        img = mpimg.imread('./stateFlowerImages./Apple Blossom.png')
        plt.imshow(img)

        # Ensure there is no graphing when the image is shown.
        plt.axis("off")
        plt.grid(False)

        # Set the title = the flower name.
        plt.title(f"{state_info[2]}")
        plt.show()
        plt.close()


def display_graph_top_5_populations():
    """Display a bar graph which shows the populations of the 5 most populated states.
    Uses the matplotlib library.
    """
    print("Close the graph to continue.")
    top_5_states = [
        ("", -1),
        ("", -1),
        ("", -1),
        ("", -1),
        ("", -1)
    ]

    # For each state in the state list...
    for state, state_info in STATE_INFO.items():
        # Compare the population to the top 5 states' population
        for cur_index in range(5):
            # If the current state's population is greater than the current list's position's pop...
            if state_info[1] > top_5_states[cur_index][1]:
                # Move all later items down the list by one
                for temp_index in range(4, cur_index, -1):
                    top_5_states[temp_index] = tuple(top_5_states[temp_index - 1])
                # Then replace the matched on in the list, and exit the inner loop
                top_5_states[cur_index] = (state, state_info[1])
                break

    # Set the x and y axes data (names/population)
    state_names = []
    state_pops = []
    for item in top_5_states:
        state_names.append(item[0])
        state_pops.append(item[1])

    # Get the graph
    bar_graph, axes = plt.subplots()
    # Set the graph = bar graph, graphed using x and y data from above
    bars = axes.bar(state_names, state_pops)
    # This line puts the value of each bar above the bar, formatted like a format string
    axes.bar_label(bars, fmt="{:,.0f}")
    # Set title of the Window
    bar_graph.canvas.manager.set_window_title('Top 5 State Populations')
    # Ensure the graph is on
    plt.axis("on")
    # Set the graph's labels
    plt.xlabel("States")
    plt.ylabel("Population (Million People)")
    plt.title("Top 5 State Populations")
    plt.show()
    plt.close()


def update_state_population(new_population=0, state_name=""):
    """Updates the population of one of the states in the dictionary.
    Prints error message if state is not in the dictionary.
    """
    if state_name not in STATE_INFO:
        print(f"{state_name} is not one of the 50 U.S. states.")
    else:
        state_tuple = tuple(STATE_INFO[state_name])
        STATE_INFO[state_name] = (state_tuple[0], new_population, state_tuple[2])
        print(f"{state_name}'s population updated from {state_tuple[1]:,d} to {new_population:,d}.")


def print_menu():
    """Display the menu of options to the user.

    """
    print("Menu:")
    print("1) Display all U.S. States and Capital, Population, and Flower in Alphabetical order.")
    print("2) Display the Capital, Population, and image of the State Flower for a specific State.")
    print("3) Display a graph of the top 5 populated states.")
    print("4) Update the population of a state.")
    print("5) Exit the program.")


def get_integer(int_prompt="Input a whole number: "):
    """Get an integer from the user.
    Loops until the user enters a whole number.
    """
    while True:
        try:
            user_int = int(input(int_prompt))
            break
        except ValueError:
            print("Invalid input, please enter a whole number.")

    return user_int


def get_integer_positive(int_prompt):
    """Get a positive integer from the user.
    Loops until the user enters a whole number.
    """
    is_positive_integer = False
    while not is_positive_integer:
        try:
            user_int = int(input(int_prompt))
            if user_int >= 0:
                is_positive_integer = True
            else:
                print("Please enter a non-negative whole number.")
        except ValueError:
            print("Invalid input, please enter a whole number.")

    return user_int


if __name__ == '__main__':
    print("   Welcome to the State Information Application!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while True:
        print("")
        print_menu()
        user_val = get_integer("Enter a selection (enter the number): ")

        print("")
        if user_val == 1:
            display_all_states_info()
        elif user_val == 2:
            display_state_name = input("Enter the state name: ")
            display_one_state_info(display_state_name)
        elif user_val == 3:
            display_graph_top_5_populations()
        elif user_val == 4:
            update_state_name = input("Enter the state name: ")
            update_state_pop = \
                get_integer_positive("Enter the state's new population as a number: ")
            update_state_population(update_state_pop, update_state_name)
        elif user_val == 5:
            break
        else:
            print("Invalid menu selection, try again.")

    print("Thank you for using the state information application.")
