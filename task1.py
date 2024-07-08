def calculator(a, b):
    x = input("Choose the arithmetic operation:\n add, sub, mult, div, pow, reminder\n")
    if x == "add":
        return a + b
    elif x == "sub":
        return a - b
    elif x == "mult":
        return a * b
    elif x == "div":
        if b == 0:
            try:
                return a / 0
            except ZeroDivisionError:  #Here we dealed with xerodivision error, as output will be undefined if quotient is zero
                print("ZeroDivision error occurs!")
                return None
        else:
            return a / b
    elif x == "pow":
        try:
            return a**b
        except OverflowError :   #Here we dealed with overflowerror , where python sometimes can't implement a large exponent value
            print("OverflowError occurred:")
        else:
            return a**b  
    elif x == "reminder":
        return a % b
    else:
        return "Invalid operation"


operand1=float(input("Enter operand1:"))
operand2=float(input("Enter operand2:"))
result = calculator(operand1, operand2)
print("Output =", result)
