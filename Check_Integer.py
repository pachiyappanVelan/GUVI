def Check_Integer(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")
def main():
    try:
        number = int(input().strip())
        Check_Integer(number)
    except:
        print("Invalid Input")
if __name__ == '__main__':
    main()
