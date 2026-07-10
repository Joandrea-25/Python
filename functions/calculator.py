print("========== Python Calculator ==========")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
# Creating functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
  
def divide(a, b):
    return a / b
# Using try-except block to avoid Python crash when incoorect input is given by the user
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    choice = int(input("Choose an operation (1-4): "))

    if choice == 1:
        print("Answer =", add(a, b))

    elif choice == 2:
        print("Answer =", subtract(a, b))

    elif choice == 3:
        print("Answer =", multiply(a, b))

    elif choice == 4:
        if b == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Answer =", divide(a, b))

    else:
        print("Invalid choice!")

except ValueError:
    print("Please enter only numbers.")

print("Thank you for using the calculator!")
