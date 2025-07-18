while True:
    user_input = input("Enter the size of the pattern: ").strip()
    if not user_input:
        print("Input cannot be empty.")
        continue
    if not user_input.isdigit():
        print("Please enter a valid positive integer.")
        continue
    size = int(user_input)
    if size <= 0:
        print("Please enter a positive integer greater than zero.")
        continue
    break

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()
    row += 1