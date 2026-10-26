
import math


def calculate_bmi(weight, height):
    """Calculate BMI using weight in kg and height in metres."""
    return weight / (height ** 2)


def get_positive_number(message, maximum=None):
    """Ask until the user enters a valid positive number."""
    while True:
        try:
            value = float(input(message))

            if not math.isfinite(value) or value <= 0:
                print("Error: Please enter a finite number greater than zero.")
            elif maximum is not None and value > maximum:
                print(f"Error: Please enter a value no greater than {maximum}.")
            else:
                return value

        except ValueError:
            print("Error: Please enter a valid numeric value.")


def main():
    print("=" * 35)
    print("       BMI CALCULATOR")
    print("=" * 35)

    weight = get_positive_number("Enter your weight in kg: ")
    height = get_positive_number(
        "Enter your height in metres (for example, 1.70): ",
        maximum=3.0,
    )

    bmi = calculate_bmi(weight, height)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print("\n---------- BMI RESULT ----------")
    print(f"Your BMI: {bmi:.2f}")
    print(f"Category: {category}")
    print("--------------------------------")


if __name__ == "__main__":
    main()
