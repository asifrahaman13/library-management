import random
import string


def generate_random_password(length):
    password = ""
    while True:
        password = "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(length)
        )
        if any(char.isdigit() for char in password):
            break
    return password


# Generate a random password of at least 8 characters
random_password = generate_random_password(8)


def generate_random_string(length):
    chars = string.digits + string.ascii_lowercase
    return "".join(random.choice(chars) for _ in range(length))


# Generate a random string in the specified format
random_string = "-".join(
    [
        generate_random_string(3),
        generate_random_string(1) + "f6",
        generate_random_string(8),
        generate_random_string(2),
    ]
)
