def hellopython():
    print("Hello, Python!")

def goodbyepython():
    print("Goodbye, Python!")

def main():
    answer = int(input("Enter 0 or 1: "))
    if answer == 0:
        hellopython()
    else:
        goodbyepython()

main()
