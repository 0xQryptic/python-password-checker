# Accepts password
password = input("Please input your password: ")

# f-string allows you include the value of the variable right inside the string.
print(f"Your password is: {password}") 

# Checking the length of the password.
password_length = len(password)
print(f"Your password is {password_length} characters long.")

if password_length < 8:
    print("Failed length check.")
    is_length_good = False
else:
    print("Passed length check.")
    is_length_good = True

#Checking to see if there is an uppercase letter.
has_uppercase = False
for char in password:
    if char.isupper():
        has_uppercase = True
        break

if has_uppercase:
    print("Passed uppercase check.")
else:
    print("Failed uppercase check.")

#Checking for a lowercase letter.
has_lowercase = False
for char in password:
    if char.islower():
        has_lowercase = True
        break

if has_lowercase:
    print("Passed lowercase check.")
else:
    print("Failed lowercase check.")

#Checking for a digit.
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break

if has_digit:
    print("Passed digit check.")
else:
    print("Failed digit check.")

#Checking for a special character.
special_char = "!@#$%^&*()_-+=<>?"
has_special = False

for char in password:
    if char in special_char:
        has_special = True
        break

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
    print("Your password is strong!")

elif strength_score >= 3:
    print("Your password is medium.")

else:
    print("Your password is weak.")



