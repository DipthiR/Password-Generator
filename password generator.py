import random
import string

def generate_password():
    # Ask the user for their preferences
    length = int(input("Enter the length of the password: "))
    
    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'

    # Build the pool of characters based on user preferences
    characters = ""
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Ensure the pool is not empty
    if not characters:
        print("You must select at least one type of character!")
        return

    # Randomly choose characters from the pool
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage
password = generate_password()
print("Generated Password:", password)
