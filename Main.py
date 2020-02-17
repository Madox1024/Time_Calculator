from TimeCalc import MillisecondStamp, gen_time_stamp


def find_operator(og_input):
    if "+" or "-" or "*" or "/" in og_input:
        if "+" in og_input:
            operator = "+"
        elif "-" in og_input:
            operator = "-"
        elif "*" in og_input:
            operator = "*"
        elif "/" in og_input:
            operator = "/"
        else:
            operator = False
        return operator


def parser(og_input, operator):
    if not operator:
        raise ValueError
    else:
        split_input = og_input.split(operator, 1)
        if (":" in split_input[0]) or (":" in split_input[1]):
            return split_input


def error(code, operator, input1, input2):
    operator_dict = {"+": "add",
                     "-": "subtract",
                     "*": "multiply",
                     "/": "divide"}
    if code == 1:
        return "Please include a time stamp, use ':' to delineate. Ex: HH:MM:SS.MS"
    if code == 2:
        return "Invalid Operation; cannot {operation} a {type1} and a {type2}.".format(
            operation=operator_dict[operator], type1=input1, type2=input2
        )
    if code == 3:
        return "Invalid operator; please use '+', '-', '*', or '/'."


# math() will convert the inputs to MillisecondStamp if given a timestamp, this is used for error handling later
def math(operator, split_input):
    if ":" in split_input[0]:
        input1 = MillisecondStamp(split_input[0])
    else:
        input1 = int(split_input[0])
    if ":" in split_input[1]:
        input2 = MillisecondStamp(split_input[1])
    else:
        input2 = int(split_input[1])
    return operation(operator, input1, input2)


# operation() decides what the appropriate operation is given the operator
def operation(operator, input1, input2):
    if operator == "+":
        return add(input1, input2)
    elif operator == "-":
        return subtract(input1, input2)
    elif operator == "*":
        return multiply(input1, input2)
    elif operator == "/":
        return divide(input1, input2)


# checks that both inputs are MillisecondStamp then adds, if not, ValueError is thrown for error code 2 (see main)
def add(input1, input2):
    if type(input1) is MillisecondStamp and type(input2) is MillisecondStamp:
        result = gen_time_stamp(input1.total_ms + input2.total_ms)
        return result
    else:
        raise ValueError


# checks that both inputs are MillisecondStamp then subtracts, if not, ValueError is thrown for error code 2
def subtract(input1, input2):
    if type(input1) is MillisecondStamp and type(input2) is MillisecondStamp:
        result = gen_time_stamp(input1.total_ms - input2.total_ms)
        return result
    else:
        raise ValueError


# checks that at least one input is MillisecondStamp then multiplies, if not, ValueError is thrown for error code 2
def multiply(input1, input2):
    if (type(input1) is MillisecondStamp or type(input2) is MillisecondStamp) and\
            (type(input1) is int or type(input2) is int):
        if type(input1) is MillisecondStamp:
            result = gen_time_stamp(input1.total_ms * input2)
        else:
            result = gen_time_stamp(input1 * input2.total_ms)
        return result
    else:
        raise ValueError


# checks that input1 is a MillisecondStamp then divides, if not, ValueError is thrown for error code 2
def divide(input1, input2):
    if type(input1) is MillisecondStamp:
        if type(input2) is int:
            result = gen_time_stamp(input1.total_ms / input2)
        else:
            result = int(input1.total_ms / input2.total_ms)
        return result
    else:
        raise ValueError


def main():
    og_input = input("->")
    operator = find_operator(og_input)
    try:
        split_input = parser(og_input, operator)
    except ValueError:
        print(error(3, None, None, None))
        return
    try:
        print(math(operator, split_input))
    except(TypeError, AttributeError):
        print(error(1, operator, None, None))
    except ValueError:
        print(error(2, operator, split_input[0], split_input[1]))


while True:
    main()
