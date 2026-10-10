def calculate_average(marks)a
    """Calculate the average of student marks."""
    if not marks:
        raise ValueError("Marks list cannot be empty")

    return sum(marks) / len(marks)


def calculate_result(average):
    """Return the result based on the average marks."""
    if average >= 40:
        return "PASS"

    return "FAIL"


def main():
    marks = [85, 72, 90, 65, 78]

    average = calculate_average(marks)
    result = calculate_result(average)

    print(f"Average marks: {average:.2f}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
