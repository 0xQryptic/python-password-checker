
def check_uppercase(password):
    """Checking for uppercase letters."""
    for char in password:
        if char.isupper():
            return True
    return False

def check_lowercase(password):
    """Checking for lowercase letters."""
    for char in password:
        if char.islower():
            return True
    return False

def check_digit(password):
    """Checking for digits."""
    for char in password:
        if char.isdigit():
            return True
    return False

def check_length(password, min_length=8):
    """Checking the length of the password."""
    actual_length = len(password)
    if actual_length >= min_length:
        return True
    else:
        return False

def check_special_char(password):
    """Checking for special characters."""
    special_char = "!@#$%^&*()_-+=<>?"
    for char in password:
        if char in special_char:
            return True
    return False

#Accepts password and creates a loop to test multiple passwords without restarting.
while True:
    password = input("Please input your password or type 'quit' to exit: ")
    if password.lower() == 'quit':
        print("Exiting password checker. Goodbye!")
        break

#f-string allows you include the value of the variable right inside the string.
    print(f"Your password is: {password}") 

#Checking the length of the password.
    actual_len = len(password)
    print(f"Your password is {actual_len} characters long.")
    is_length_good = check_length(password)
    if is_length_good:
        print("Passed length check.")
    else:
        print("Failed length check.")

#Checking to see if there is an uppercase letter.
    has_uppercase = check_uppercase(password)
    if has_uppercase:
        print("Passed uppercase check.")
    else:
        print("Failed uppercase check.")

#Checking for a lowercase letter.
    has_lowercase = check_lowercase(password)
    if has_lowercase:
        print("Passed lowercase check.")
    else:
        print("Failed lowercase check.")

#Checking for a digit.
    has_digit = check_digit(password)
    if has_digit:
        print("Passed digit check.")
    else:
        print("Failed digit check.")

#Checking for a special character.
    has_special = check_special_char(password)
    if has_special:
        print("Passed special character check.")
    else:
        print("Failed special character check.")

#Giving a strength score
    strength_score = 0

    if is_length_good:
        strength_score += 1

    if has_uppercase:
        strength_score += 1

    if has_lowercase:
        strength_score += 1

    if has_digit:
        strength_score += 1

    if has_special:
        strength_score += 1

    print("\n---Overall Strength Score---")
    print(f"Your password strength score is: {strength_score}/5.")

    if strength_score == 5:
        print("Password Strength: Strong")

    elif strength_score >= 3:
        print("Password Strength: Medium")

    else:
        print("Password Strength: Weak")

#Line Break
    print("-" * 40)





