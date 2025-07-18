while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer greater than zero.")
            continue
        break
    except ValueError:
        print("Please enter a valid positive integer.")

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()
    row += 1
