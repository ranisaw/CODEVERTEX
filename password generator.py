import random
import string

def generate_password(length=12):
    """
    Generates a random password with the given length.
    The password includes uppercase, lowercase, digits, and special characters.
    """
    if length < 6:
        print("Password length should be at least 6 characters for better security.")
        return None

    # Character pools
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()-_+="

    # Ensure the password contains at least one character from each category
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to ensure randomness
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Main function
if __name__ == "__main__":
    try:
        password_length = int(input("Enter desired password length (minimum 6): "))
        password = generate_password(password_length)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")
