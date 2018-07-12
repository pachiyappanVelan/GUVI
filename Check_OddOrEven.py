def Check_OddOrEven(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
try:
    Check_OddOrEven(int(input().strip()))
except:
    print("Invalid")
