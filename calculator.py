import maths_helper


class Calculator:
    def __init__(self):
        self.operand_x = None
        self.operand_y = None
        self.operator = None

    @property
    def operand_x(self):
        return self.__operand_x

    @operand_x.setter
    def operand_x(self, value):
        try:
            if value is None or float(value):
                self.__operand_x = float(value) if value else value
            else:
                print('Please enter a valid number')
        except ValueError:
            print('Please enter a valid number')

    @property
    def operand_y(self):
        return self.__operand_y

    @operand_y.setter
    def operand_y(self, value):
        try:
            if value is None or float(value):
                self.__operand_y = float(value) if value else value
            else:
                print('Please enter a valid number')
        except ValueError:
            print('Please enter a valid number')

    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, value):
        allowed_operations = ['+', '-', '/', 'x']
        if value is None or value.strip() in allowed_operations:
            self.__operator = value.strip() if value else value
        else:
            print('Please enter a valid operator')

    def solve(self):
        self.operand_x = maths_helper.operationsDict[self.operator](self.operand_x, self.operand_y)
        print(f"The result is {self.operand_x}")
        self.operator = None
        self.operand_y = None

    def clear(self):
        self.operand_x = None
        self.operand_y = None
        self.operator = None
        print("Cleared")
