
# Assignment 3: Even/Odd & Prime Number Checker
# Check whether a number is even, odd, and prime.

def check_even_odd(number):
    """Check whether a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def check_prime(number):
    """Check whether a number is prime."""
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def main():
    print("===== Even/Odd & Prime Number Checker =====")

    try:
        number = int(input("Enter an integer: "))

        print(f"Number: {number}")
        print(f"Type: {check_even_odd(number)}")

        if check_prime(number):
            print("Prime Status: Prime number")
        else:
            print("Prime Status: Not a prime number")

    except ValueError:
        print("Invalid input! Please enter a whole number.")


if __name__ == "__main__":
    main()
