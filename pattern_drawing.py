while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  
    row += 1