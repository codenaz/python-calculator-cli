import calculator


def get_input(answer):
    if answer == 'clear':
        my_calculator.clear()
    if my_calculator.operand_x is None:
        new_answer = input('Enter your first operand: ')
        my_calculator.operand_x = new_answer
        get_input(new_answer)
    if my_calculator.operator is None:
        new_answer = input('Enter your operator (should be +,-,x or /): ')
        my_calculator.operator = new_answer
        get_input(new_answer)
    if my_calculator.operand_y is None:
        new_answer = input('Enter your second operand: ')
        my_calculator.operand_y = new_answer
        get_input(new_answer)


my_calculator = calculator.Calculator()


while True:
    initial_answer = None
    get_input(initial_answer)

    my_calculator.solve()
