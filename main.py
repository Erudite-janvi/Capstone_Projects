def user_login():
    username = input("Enter user name :")
    return username


def user_Password():
    print("Note: Password should contain:")
    print("- Length between 12 and 20 characters")
    print("- At least three uppercase letters")
    print("- At least three lowercase letters")
    print("- At least one digit")
    print("- At least three special characters")
    print("- Only letters, numbers, and special characters are allowed")
    print("- Should not contain 5 same characters or numbers consecutively")
    print("- Should not contain the username")
    print("- Should not have 3 same special characters consecutively")

    password = input("Enter password: ").strip()
    print("Entered password:", password)
    

    return password


def password_length_validator(password):
    min_length = 12
    max_length = 20
    if len(password) < min_length or len(password) > max_length:
        return False
    return True


def uppercase_char_validator(password):
    uppercase_count = sum(char.isupper() for char in password)
    if uppercase_count < 3:
        return False
    return True


def lowercase_char_validator(password):
    lowercase_letters = [char for char in password if char.islower()]
    lowercase_count = len(lowercase_letters)
    if lowercase_count >= 3:
        return True
    return False


def any_digit_validator(password):
    if any(char.isdigit() for char in password):
        return True
    return False


def special_char_validator(password):
    count = 0
    for char in password:
        if char in "!@#$%^&*()_-~":
            count += 1
    if count >= 3:
        return True
    return False


def allowed_special_character(password):
    for char in password:
        if char in "!@#$%^&*()_-~":
            return True
    return False


def start_with_digit(password):
    if (password[0].isdigit() and password[1].isdigit) or (password[0] in "!@#$%^&*()_-~"):
        return True
    return False


def check_consecutive_char(password):
    consecutive_count = 1
    max_consecutive_allowed = 4
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            consecutive_count += 1
            if consecutive_count > max_consecutive_allowed:
                return False
        elif password[i] != password[i + 1]:
            consecutive_count = 1
    return True


def Password_Contain_Username(username, password):
    if username in password:
        return False
    return True


def Consecutive_Special(password):
    count = 1
    for i in range(len(password) - 1):
        if password[i] in "!@#$%^&*()_-~" and password[i + 1] in "!@#$%^&*()_-~":
            if password[i] == password[i + 1]:
                count = count + 1
                if count >= 3:
                    return False
        elif password[i] != password[i + 1]:
            count = 1
    return True


def passwordValidator(username, password):
    errors = []

    if not password_length_validator(password):
        errors.append("Password must contain between 12 and 20 characters")

    if not uppercase_char_validator(password):
        errors.append("Password must contain at least 3 uppercase letters")

    if not lowercase_char_validator(password):
        errors.append("Password must contain at least 3 lowercase letters")

    if not any_digit_validator(password):
        errors.append("Password must contain at least one digit")

    if not special_char_validator(password):
        errors.append("Password must contain at least 3 special characters")

    if not allowed_special_character(password):
        errors.append(
            "Password must contain only letters, numbers, and special characters from the allowed set")

    if not start_with_digit(password):
        errors.append(
            "Password must start with at least 2 digits or one special character")

    if not check_consecutive_char(password):
        errors.append(
            "Password cannot contain more than 5 consecutive identical characters or numbers")

    if not Password_Contain_Username(username, password):
        errors.append("Password cannot contain the username")

    if not Consecutive_Special(password):
        errors.append(
            "Password cannot contain three consecutive special characters")

    # to Check if any errors were found
    if errors:

        for error in errors:
            print(error)
        return False

    else:
        return True
        


def main():
    username = user_login()
    valid_password = False
    while not valid_password:
        password = user_Password()
        valid_password = passwordValidator(username, password)
       
    print("Valid Password")


if __name__ == "__main__":
    main()
