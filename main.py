from modules import evaluate
from modules import inputs, convertor


def main_program():

    input_base = convertor.base_type("Input")
    output_base = convertor.base_type("Output")

    if input_base == 10:
        first_num = inputs.input_float_number(input_base, 'First')
        second_num = inputs.input_float_number(input_base, 'Second')
        operation_type = inputs.operations()

        return evaluate(first_num, second_num, operation_type)

    else:
        first_num = inputs.input_int_number(input_base, 'First')
        second_num = inputs.input_int_number(input_base, 'Second')
        operation_type = inputs.operations()
        result = evaluate(first_num, second_num, operation_type)

        if (output_base == 10 and type(result) == float):
            return result

        return convertor.convertor(output_base, result)
