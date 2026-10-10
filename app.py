def calculate_average(marks):
    total = 0
    for mark in marks:
        total = total + mark

    average = total / len(marks)
    print("Average calculated")
    print("Average calculated")
    return average


def main():
    marks = [85, 72, 90, 65, 78]
    average = calculate_average(marks)
    print(f"Average: {average}")


if __name__ == "__main__":
    main()
