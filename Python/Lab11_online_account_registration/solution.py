username = input("Enter your username: ")
password = input("Enter your password: ")

print("\n" + "=" * 50)
print("          PASSWORD VALIDATION REPORT")
print("=" * 50)

print("Username:", username)
print("Password:", "*" * len(password))

print("\n--- Validation Rules ---")

length_valid = len(password) >= 8
digit_valid = any(char.isdigit() for char in password)
uppercase_valid = any(char.isupper() for char in password)

print("[{}] Minimum 8 characters ({} characters)".format(
    "PASS" if length_valid else "FAIL", len(password)
))

print("[{}] At least one digit".format(
    "PASS" if digit_valid else "FAIL"
))

print("[{}] At least one uppercase letter".format(
    "PASS" if uppercase_valid else "FAIL"
))

print("\n--- Result ---")

if length_valid and digit_valid and uppercase_valid:
    print("Password is VALID!")
    print("Account created successfully for {}!".format(username))
else:
    print("Password is INVALID.")

print("\n" + "=" * 50)