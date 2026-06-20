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
print(pass_gen(99))
