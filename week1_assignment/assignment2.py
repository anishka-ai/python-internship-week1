
# Assignment 2: Student Grade Calculator
# Calculate average marks and assign a grade.

def calculate_average(marks):
    """Calculate the average of all subject marks."""
    return sum(marks) / len(marks)


def calculate_grade(average):
    """Assign a grade based on average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def main():
    print("===== Student Grade Calculator =====")

    try:
        name = input("Enter student name: ").strip()

        if not name:
            print("Student name cannot be empty.")
            return

        num_subjects = int(input("Enter number of subjects: "))

        if num_subjects <= 0:
            print("Number of subjects must be greater than zero.")
            return

        marks = []

        for i in range(num_subjects):
            mark = float(input(f"Enter marks for subject {i + 1}: "))

            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(mark)

        average = calculate_average(marks)
        grade = calculate_grade(average)

        print("\n===== Student Result =====")
        print(f"Student Name: {name}")
        print(f"Total Marks: {sum(marks):.2f}/{num_subjects * 100}")
        print(f"Average Marks: {average:.2f}%")
        print(f"Grade: {grade}")

        if grade == "F":
            print("Result: Fail")
        else:
            print("Result: Pass")

    except ValueError:
        print("Invalid input! Please enter numeric values for marks.")


if __name__ == "__main__":
    main()
