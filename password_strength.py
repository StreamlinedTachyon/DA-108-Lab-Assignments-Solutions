import string

def check_password_strength(password):
    # Initialize boolean variables
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # Calculate the password length
    password_length = len(password)

    # Categorize password strength
    if password_length >= 6 and has_upper and has_lower and has_digit and has_special:
        return "Strong", "Strong password! Great job!"
    elif password_length < 6:
        return "Weak", "Password is too short. Try using at least 6 characters."
    elif not (has_upper and has_lower):
        return "Weak", "Try including uppercase and lowercase letters, numbers, and special characters!"
    elif not has_digit:
        return "Weak", "Try using numbers for a stronger password!"
    elif not has_special:
        return "Medium", "Try adding special characters for a stronger password!"
    else:
        return "Weak", "Your password could be stronger!"

def password_strength_checker():
    # Maintain a history of entered passwords
    password_history = []

    print("Welcome to the Password Strength Checker!")
    while True:
        # Take user input
        password = input("Enter your password: ")
        password_history.append(password)

        # Check the password strength
        strength, feedback = check_password_strength(password)

        # Provide feedback
        print(feedback)
        if strength == "Strong":
            break

    print("\nPassword Strength Checker Complete!")
    print("History of passwords you entered:")
    print(password_history)

if __name__ == "__main__":
    password_strength_checker()
