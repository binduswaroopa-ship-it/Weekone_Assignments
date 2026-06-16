def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def main():
    while True:
        user_input = input("Enter your mark (0-100): ")
        try:
            mark = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if mark < 0 or mark > 100:
            print("Please enter a number between 0 and 100.")
            continue

        grade = get_grade(mark)
        print(f"Mark: {mark} -> Grade: {grade}")
        break


if __name__ == "__main__":
    main()