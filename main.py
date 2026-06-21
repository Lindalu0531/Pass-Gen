import string
import random
def pass_gen(length):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*(?><::{}|)"
    pool = letters + numbers + symbols
    password = ""

    for i in range(length):
        password += random.choice(pool)
    return password

print("Welcome to password Generator")
try:
    length = int(input("Enter the amount of charectors u want(max 128): "))
    if length > 128 or  length < 0:
        print("Error: Please enter between 0 and 128")
        pass_gen(length)
    else:
        print(f"Your generatod password is: {pass_gen(length)}")
except ValueError:
    print("Please Type a valid number!")