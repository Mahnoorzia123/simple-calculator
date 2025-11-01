# Taking number and operator from user

num1 = float(input("Enter 1st number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter 2nd number: "))

if op == "+": 
    print(f"Result: {num1 + num2}") #Sum

elif op == "-":
    print(f"Result: {num1-num2}") #Subtract

elif op == "*":
    print(f"Result: {num1 * num2}") #Multiply

elif op == "/":

    if num2 == 0:
        print("Error: Cannot divide by zero.") # Handle zero division22
    else:
        print(f"Result: {num1 / num2}") #Division

else:
    print("Invalid operater")
    
