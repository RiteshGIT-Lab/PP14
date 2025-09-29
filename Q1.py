import re

def check_password_strength(password: str) -> bool:
    # Minimum length
    if len(password) < 8:
        return False
    # Uppercase and lowercase
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    # Digit
    if not re.search(r'\d', password):
        return False
    # Special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    if check_password_strength(pwd):
        print("Strong password! ✅")
    else:
        print("Weak password.  Please ensure it has:\n"
              "- At least 8 characters\n"
              "- Both uppercase and lowercase letters\n"
              "- At least one digit\n"
              "- At least one special character (!@#$%^&* etc.)")