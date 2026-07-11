print("----- Number Analyzer -----")
try:
    a = int(input("Enter a number: "))
    print("The number you've entered:", a)
    if a % 2 == 0 and a > 0:
        print("It is an even positive number.")
    elif a % 2 == 0 and a < 0:
        print("It is an even negative number.")
    elif a % 2 != 0 and a > 0:
        print("It is an odd positive number.")
    elif a % 2 != 0 and a < 0:
        print("It is an odd negative number.")
    else:
        print("It is zero.")

except ValueError:
    print("Invalid input! Please enter an integer.")

finally:
    print("Program Ended.")
