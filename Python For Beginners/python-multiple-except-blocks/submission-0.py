def divide_numbers(a: str, b: str) -> None:
    try:
        convertedA = int(a)
        convertedB = int(b)

        print(convertedA / convertedB)
    except ValueError as valueError:
        print("Error: Invalid value!")
    except ZeroDivisionError as zeroDivisionError:
        print("Error: Division by zero!")
    except Error as error:
        print(f"An error occurred: {error}")




# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
