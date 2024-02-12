import random
import string

def random_password(length):
    # Generate random password characters
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Define paswordlength
password_length = 12  

# Generate random password
generated_password = random_password(password_length)

# Print Generated Password
print("Generated Password:", generated_password)
