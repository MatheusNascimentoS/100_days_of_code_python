from art import logo 
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }

def calcutator():
    n1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)
    should_continue = True
    
    while should_continue:
    
        operation_symbol = input("Pick an operation from the above: ")
        
        n2 = float(input("What's the next number?: ")) 

        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")
    
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            n1 = answer
        else:
            should_continue = False
            calcutator()
            
        # new_operation_symbol = input("Pick another operation: ")
        # new_n = float(input("What's the next number?: "))
        # calculation_function = operations[new_operation_symbol]
        # new_answer = calculation_function(answer, new_n)
        # print(f"{answer} {new_operation_symbol} {new_n} = {new_answer}")
        # answer = new_answer
print(logo)
calcutator()