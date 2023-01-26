def result(operand):
    match operand:
        case "+":
            return int(num1) + int(num2)

        case "-":
            return int(num1) - int(num2)

        case "*":
            return int(num1) * int(num2)

        case "/":
            return int(num1) / int(num2)


num1 = input("First number: ")
operation = input("+ - / * ")
num2 = input("Second number: ")
print(num1 + operation + num2 + "= " + str(result(operation)))


