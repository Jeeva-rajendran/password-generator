import secrets
import string

# Define the character set: letters, digits, and punctuation
characters = string.ascii_letters + string.digits + string.punctuation

# Prompt the user for the desired password length
length = int(input("Enter the length of the password: "))

# Generate a secure password
password = ''.join(secrets.choice(characters) for _ in range(length))

print("Generated password:", password)
