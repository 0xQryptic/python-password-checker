# Accepts password
password = input("Please input your password: ")

# f-string allows you include the value of the variable right inside the string.
print(f"Your password is: {password}") 

# Checking the length of the password.
password_length = len(password)
print(f"Your password is {password_length} characters long.")


if password_length < 8:
    print("Your password is too short.")
else:
    print("Your password is long enough.")

