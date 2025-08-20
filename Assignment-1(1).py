#Simple Calculator


num1 = int(input("Enter a number"))
num2 =int(input("Enter second number"))
op = input("Enter the operator")
match op:
    case "+":
        print(num1+num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case "-":
        print(num1-num2)
    case "**":
        print(num1**num2)
    case "%":
        print(num1%num2)
    case "//":
        print(num1 // num2)
    case _:
        print("Invalid Operator")




