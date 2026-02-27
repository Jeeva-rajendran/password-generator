import secrets
import string

def password_generator():
    # Define the character set: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Prompt the user for the desired password length 
    length = int(input("Enter the length of the password: "))
    
    # Generate a secure password
    return ''.join(secrets.choice(characters) for _ in range(length))

password = password_generator()

print(password)
    
    