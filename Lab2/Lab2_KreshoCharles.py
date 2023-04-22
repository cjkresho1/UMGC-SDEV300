"""

"""
import math
import string
import secrets
from datetime import date


def generate_secure_password(num_chars=8, uses_upper_case=True, uses_lower_case=True,
                             uses_nums=True, uses_special_chars=True):
    if not uses_upper_case and not uses_lower_case and not uses_nums and not uses_special_chars:
        print("Must answer yes to at least one option for password value.")
        return

    alphabet = ""

    if uses_upper_case:
        alphabet += string.ascii_uppercase
    if uses_lower_case:
        alphabet += string.ascii_lowercase
    if uses_nums:
        alphabet += string.digits
    if uses_special_chars:
        alphabet += string.punctuation

    while True:
        password = "".join(secrets.choice(alphabet) for i in range(num_chars))
        if ((any(c.islower() for c in password) or not uses_lower_case) and
                (any(c.isupper() for c in password) or not uses_upper_case) and
                (any(c.isdigit() for c in password) or not uses_nums) and
                (any(c in string.punctuation for c in password))):
            break
    return password


def print_formatted_percent(numerator=1.0, denominator=10.0, num_decimals=3):
    val = numerator / denominator

    return round(val, num_decimals)


def days_till_2025_july_4():
    today = date.today()
    july_4_2025 = date(2025, 7, 4)

    time_till_2025_july_4 = abs(july_4_2025 - today)
    return time_till_2025_july_4.days


def calc_triangle_leg(leg1_len=1.0, leg2_len=2.0, angle=90.0):
    c_squared = (leg1_len ** 2) + (leg2_len ** 2) - (2 * leg1_len * leg2_len
                                                     * math.cos(angle / 180 * math.pi))
    c = math.sqrt(c_squared)

    return round(c, 3)


def volume_right_cylinder(radius=1.0, height=1.0):
    volume = math.pi * (radius ** 2) * height

    return round(volume, 3)


def print_menu():
    print("Menu: ")
    print("1. Generate a secure password")
    print("2. Calculate a percentage")
    print("3. How many days until July 4th, 2025")
    print("4. Calculate the third leg of a triangle, using the law of Cosines")
    print("5. Calculate the volume of a Right Circular Cylinder")
    print("6. Exit")


def get_yes_no(prompt):

    while True:
        val = input(prompt)
        val = val.lower()

        if val == "yes":
            is_yes = True
            break
        elif val == "no":
            is_yes = False
            break
        else:
            print("Invalid input, enter either yes/no.")

    return is_yes


def get_integer(int_prompt):
    while True:
        try:
            user_int = int(input(int_prompt))
            break
        except ValueError:
            print("Invalid input, please enter a whole number.")

    return user_int


def get_float(float_prompt):
    while True:
        try:
            user_float = float(input(float_prompt))
            break
        except ValueError:
            print("Invalid input, please enter a whole number.")

    return user_float


if __name__ == '__main__':
    print("Welcome to the Lab 2 application!")

    while True:
        print_menu()
        while True:
            try:
                user_val = int(input("Enter a selection (enter the number): "))
                break
            except ValueError:
                print("Invalid input, please enter a number.")

        print("")
        if user_val == 1:
            pass_length = get_integer("What length should the password be: ")
            needs_lowercase = get_yes_no("Do you want lowercase characters in your password: ")
            needs_uppercase = get_yes_no("Do you want uppercase characters in your password: ")
            needs_numbers = get_yes_no("Do you want numbers in your password: ")
            needs_special = get_yes_no("Do you want special characters in your password: ")
            generated_pass = generate_secure_password(pass_length, needs_uppercase, needs_lowercase,
                                                      needs_numbers, needs_special)
            print(f"Generated password: {generated_pass}")
        elif user_val == 2:
            numer = get_float("Enter a numerator: ")
            denom = get_float("Enter a denominator: ")
            precision = get_integer("Enter number of decimal points on output: ")
            generated_percent = print_formatted_percent(numer, denom, precision)
            print(f"The percent is {generated_percent}")
        elif user_val == 3:
            days = days_till_2025_july_4()
            print(f"Days till July 4th, 2025: {days}")
        elif user_val == 4:
            leg1 = get_float("Enter the length of the first leg of the triangle: ")
            leg2 = get_float("Enter the length of the second leg of the triangle: ")
            angel = get_float("Enter the angel of the angel between the two legs: ")
            third_leg = calc_triangle_leg(leg1, leg2, angel)
            print(f"The third leg of the triangle is {third_leg}")
        elif user_val == 5:
            cyl_radius = get_float("Enter the radius of the cylinder: ")
            cyl_height = get_float("Enter the height of the cylinder: ")
            cyl_volume = volume_right_cylinder(cyl_radius, cyl_height)
            print(f"The volume of the cylinder is {cyl_volume}")
        elif user_val == 6:
            break
        else:
            print("Invalid menu selection, try again.")

    print("Thank you for using the Lab 2 application.")
