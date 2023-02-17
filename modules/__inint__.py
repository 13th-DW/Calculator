def evaluate(first, second, command):
    try:
        if command == "+":
            return first + second

        elif command == "-":
            return first - second

        elif command == "-":
            return first - second

        elif command == "*":
            return first * second

        elif command == "**":
            return first ** second

        elif command == "/":
            return first / second

        elif command == "//":
            return first // second

        elif command == "%":
            return first % second

    except ZeroDivisionError:
        return "You can't / on 0"
