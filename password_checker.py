import re

def password_strength(password):
    strength = 0
    feedback = []

    if len(password) < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    elif len(password) >= 12:
        strength += 2
    else:
        strength += 1

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Use a mix of uppercase and lowercase letters.")

    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    common_patterns = ['123', 'password', 'qwerty', 'letmein']
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Avoid using common patterns or words like 'password' or '123'.")
        strength -= 1

    if strength <= 2:
        feedback.append("Overall strength: Weak.")
    elif strength == 3:
        feedback.append("Overall strength: Moderate.")
    else:
        feedback.append("Overall strength: Strong.")

    return "\n".join(feedback)

if __name__ == "__main__":
    user_password = input("Enter a password to test its strength: ")
    print(password_strength(user_password))

