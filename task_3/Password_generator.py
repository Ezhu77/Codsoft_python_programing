import random
import string

def generate_password(length=12):
    # Define the character sets to choose from
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_characters, k=length-4)
    random.shuffle(password)

    return ''.join(password)

password = generate_password(12)
print("Generated Password:", password)
