while True:
    user_input = input("Enter a number to see its multiplication table: ")
    try:
        number = int(user_input)
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")