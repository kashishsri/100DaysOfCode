from Day10_art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
     "+" : add,
     "-" : sub,
     "*" : mul,
     "/" : div,
}


def calculator():
    first_num = float(input("What's the first number? : "))
    for key in operations:
        print(key)
    calc_on = True

    while calc_on:
        operation_symbol = input("Pick an operation : ")
        next_num = float(input("What's the next number? : "))
        calc_func = operations[operation_symbol] # this returns value of the key which is same as name of functions defined add, sub etc
        result = calc_func(first_num, next_num) # this value or func name e.g. add, mul used here as func name.
        print(f"{first_num} {operation_symbol} {next_num} = {result}")
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation : ") == 'y':
            first_num = result
        else:
            calc_on = False

calculator()




