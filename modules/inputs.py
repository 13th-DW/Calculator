def input_int_number(input_base: int, string: str):
    while True:
        try:
            num = int(input(f"{string} number: "), base=input_base)
            return num
        except:
            print("Value is incorrect.")


def input_float_number(string: str):
    while True:
        try:
            num = float(input(f"{string} number: "))
            return num
        except:
            print("Value is incorrect.")


def operations():

    operations_list = '+', '-', '*', '**', '/', '//', '%'
    while True:
        operation_type = input("Operation (+,-,*,**,/,//,%): ")

        if operation_type in operations_list:
            return operation_type
        else:
            print("Sorry, I don't understand you.")
