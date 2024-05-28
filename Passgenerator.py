import string
import random

length = int(input("Enter the password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for i in range(length))

print("Your password is: " + password)
print("Thanks for using Password-generator")