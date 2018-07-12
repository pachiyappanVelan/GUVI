def Check_Greatest(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)
try:
    input_ = input().split(" ")
    Check_Greatest(int(input_[0]),int(input_[1]),int(input_[2]))
except:
    print("Invalid Input")
