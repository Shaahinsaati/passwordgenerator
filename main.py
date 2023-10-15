import random
import string


def password_generator(length=10, has_digit=True, has_specials=True):
    characters = string.ascii_letters  # using upper and lowe case both in same time
    if has_digit:
        characters += string.digits  # Include digits

    if has_specials:
        characters += string.punctuation  # Special characters like / \ *

    if not characters:
        print('Password must include at least one type of characters')
        return None

    final_password = ''.join(random.choice(characters) for _ in range(length))
    return final_password


if __name__ == "__main__":
    password_length = int(input("Enter your desired password length: "))
    has_digit = input("Include digits (y/n) ? : ").lower() == 'y'
    has_specials = input("Include special characters (y/n) ? : ").lower() == 'y'
    password = password_generator(length=password_length, has_digit=has_digit, has_specials=has_specials)

