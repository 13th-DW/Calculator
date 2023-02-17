from bases import Bases
bases = Bases()


def base_type(string: str):

    while True:
        try:
            input_base = int(input(f"{string} base type(2-36): "))
            if input_base not in range(2, 17):
                print("Basenumber is incorrect.")
                continue
            return input_base
        except ValueError:
            print("Basenumber is incorrect.")


def convertor(base: int, number: int):
    return bases.toBase(number, base)
