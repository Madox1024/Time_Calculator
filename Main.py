from TimeCalc import MillisecondStamp, gen_time_stamp


class Main:

    def __init__(self):
        self.og_input = input("->")
        self.operator = self.find_operator(self.og_input)
        try:
            self.split_input = self.parser(self.og_input, self.operator)
        except ValueError:
            self.error(3, None, None, None)
        try:
            try:
                self.math = Math(self.operator, self.split_input)
            except(TypeError, AttributeError):
                self.error(1, self.operator, None, None)
        except ValueError:
            self.error(2, self.operator, self.split_input[0], self.split_input[1])
        self.answer = self.math.answer
        print(self.answer)
        self.__init__()

    def find_operator(self, og_input):
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

    def parser(self, og_input, operator):
        if not operator:
            raise ValueError
        else:
            split_input = og_input.split(operator, 1)
            if (":" in split_input[0]) or (":" in split_input[1]):
                return split_input
            else:
                return

    def error(self, code, operator, input1, input2):
        operator_dict = {"+": "add",
                         "-": "subtract",
                         "*": "multiply",
                         "/": "divide"}
        if code == 1:
            print("Please include a time stamp, use ':' to delineate. Ex: HH:MM:SS.MS")
            quit()
        if code == 2:
            print("Invalid Operation; cannot {operation} a {type1} and a {type2}.").format(
                operation=operator_dict[operator], type1=type(input1), type2=type(input2)
            )
            quit()
        if code == 3:
            print("Invalid operator; please use '+', '-', '*', or '/'.")
            quit()


class Math:

    def __init__(self, operator, split_input):
        self.operator = operator
        self.split_input = split_input
        if ":" in split_input[0]:
            self.input1 = MillisecondStamp(split_input[0])
        else:
            self.input1 = int(split_input[0])
        if ":" in split_input[1]:
            self.input2 = MillisecondStamp(split_input[1])
        else:
            self.input2 = int(split_input[1])
        self.answer = self.operation(self.operator)

    def operation(self, operator):
        if operator == "+":
            return self.add(self.input1, self.input2)
        elif operator == "-":
            return self.subtract(self.input1, self.input2)
        elif operator == "*":
            return self.multiply(self.input1, self.input2)
        elif operator == "/":
            return self.divide(self.input1, self.input2)

    def add(self, input1, input2):
        if type(input1) == MillisecondStamp and type(input2) == MillisecondStamp:
            result = str(gen_time_stamp(input1.total_ms + input2.total_ms))
            return result
        else:
            raise ValueError

    def subtract(self, input1, input2):
        if type(input1) == MillisecondStamp and type(input2) == MillisecondStamp:
            result = str(gen_time_stamp(input1.total_ms - input2.total_ms))
            return result
        else:
            raise ValueError

    def multiply(self, input1, input2):
        if (type(input1) == MillisecondStamp or type(input2) == MillisecondStamp) and\
                (type(input1) == int or type(input2) == int):
            if type(input1) == MillisecondStamp:
                result = str(gen_time_stamp(input1.total_ms * input2))
            else:
                result = str(gen_time_stamp(input1 * input2.total_ms))
            return result
        else:
            raise ValueError

    def divide(self, input1, input2):
        if type(input1) == MillisecondStamp:
            if type(input2) == int:
                result = str(gen_time_stamp(input1.total_ms / input2))
            else:
                result = str(int(input1.total_ms / input2.total_ms))
            return result
        else:
            raise ValueError


Main = Main()
