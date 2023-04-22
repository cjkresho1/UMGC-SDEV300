"""This program collects the information for a voter registration.
Author: Charles Kresho
Version: 03/21/2023
"""
import sys

# A list of all the valid state abbreviations
VALID_STATES = ['AL', 'AK', 'AZ', 'AR', 'AS', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU', 'HI',
                'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO',
                'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PA',
                'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'TT', 'UT', 'VT', 'VA', 'VI', 'WA', 'WV', 'WI',
                'WY']


def prompt_continue():
    """Determine if the user wants to continue registering.

    Exits the program directly if the user says no. Repeats until valid yes/no input.
    """
    user_input = input("Do you want to continue with the voter Registration? (yes/no)\n")

    # Exits the program on a no, just returns on a yes (recursively calls until a yes/no)
    if user_input.lower() == "yes":
        return
    if user_input.lower() == "no":
        print("Thank you for trying the Voter Registration Application.")
        sys.exit()
    else:
        print("Invalid input, try again.")
        prompt_continue()


# Runs if this is the "main" class
if __name__ == '__main__':
    print("Welcome to the Python Voter Registration Application.")
    prompt_continue()

    # Get the first name from the user...loops if there is no input?
    firstName = input("What is your first name?\n")
    while len(firstName) == 0:
        print("Invalid name, try again.")
        prompt_continue()
        firstName = input("What is your first name?\n")
    prompt_continue()

    # Get the last name from the user...loops if there is no input?
    lastName = input("What is your last name?\n")
    while len(lastName) == 0:
        print("Invalid name, try again.")
        lastName = input("What is your last name?\n")
        prompt_continue()
    prompt_continue()

    # Get the age of the user. Loop until an age between 0 and 120 (noninclusive) is input.
    # Exits if the user is under the age of 18.
    while True:
        # Report if the user enters a non-digit age
        try:
            age = int(input("What is your age?\n"))
            if 0 < age < 120:
                break
            print("Your age must be valid (greater than 0 and less than 120).")
            prompt_continue()
        except ValueError:
            print("Please input a number for your age.")
            prompt_continue()
    if age < 18:
        print("You must be 18 years or older to vote.")
        print("Thank you for trying the Voter Registration Application.")
        sys.exit()
    prompt_continue()

    # Get the citizenship status of the user. Exit if the user is not a citizen.
    while True:
        citizenInput = input("Are you a U.S. Citizen? (yes/no)\n")
        if citizenInput.lower() == "yes":
            break
        if citizenInput.lower() == "no":
            print("You must be a U.S. citizen to vote.")
            print("Thank you for trying the Voter Registration Application.")
            sys.exit()
        else:
            print("Invalid input, try again.")
        prompt_continue()
    prompt_continue()

    # Get the state the user lives in. Must be a 2-character abbreviation of one of the 50 states.
    while True:
        state = input("What state do you live in (enter 2-character abbreviation)?\n")
        state = state.upper()
        try:
            VALID_STATES.index(state)
            break
        except ValueError:
            print("This is not a valid state abbreviation, try again.")
        prompt_continue()
    prompt_continue()

    # Get the zipcode from the user.
    while True:
        try:
            zipCode = int(input("What is your zipcode?\n"))
            if 10000 <= zipCode < 100000:
                break
            print("A zip code must be 5 digits in length.")
            prompt_continue()
        except ValueError:
            print("Please input a number for your zipcode.")
            prompt_continue()

    # Report back to the user their information, and exit.
    print("Thanks for registering to vote. Here is the information we received:")
    print(f"Name (first last): {firstName} {lastName}")
    print(f"Age: {age}")
    print("U.S. Citizen: Yes")
    print(f"State: {state}")
    print(f"Zipcode: {zipCode}")
    print("Thanks for trying the Voter Registration Application. Your voter registration card " +
          "should be shipped within 3 weeks.")
