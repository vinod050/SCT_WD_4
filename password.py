import re


def assess_password_strength(password: str) -> dict:
    score = 0
    feedback = []

    # Length checks
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Password should be at least 8 characters long.")

    if len(password) >= 12:
        score += 2

    # Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 2
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase letters
    if re.search(r"[a-z]", password):
        score += 2
    else:
        feedback.append("Add at least one lowercase letter.")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Special characters
    if re.search(r"[!@#$%^&*()_\-+=\[\]{}|;:'\",.<>?/]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Strength label
    if score <= 3:
        strength = "Weak"
    elif score <= 6:
        strength = "Moderate"
    elif score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }


# -------------------------------
# INTERACTIVE USAGE
# -------------------------------
if __name__ == "__main__":
    password = input("Enter password to evaluate: ")
    result = assess_password_strength(password)

    print("\nPassword Strength Report")
    print("------------------------")
    print(f"Score     : {result['score']} / 10")
    print(f"Strength  : {result['strength']}")

    if result["feedback"]:
        print("\nSuggestions:")
        for item in result["feedback"]:
            print(f"- {item}")
    else:
        print("\nExcellent password. No improvements needed.")
