import re

def password_strength(password):
    length = len(password)
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    digit = bool(re.search(r'[0-9]', password))
    special_char = bool(re.search(r'[^A-Za-z0-9]', password))

    score = 0
    feedback = ""

    # Criteria
    if length >= 8:
        score += 1
    if uppercase:
        score += 1
    if lowercase:
        score += 1
    if digit:
        score += 1
    if special_char:
        score += 1

    # Feedback
    if score == 5:
        feedback = "Strong password"
    elif score >= 3:
        feedback = "Moderate password"
    else:
        feedback = "Weak password"

    return feedback

def main():
    password = input("Enter your password: ")
    strength = password_strength(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()
