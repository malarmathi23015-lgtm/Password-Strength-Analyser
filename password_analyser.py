import re
import random
import string

COMMON_PASSWORDS = ["123456", "password", "admin", "qwerty", "abc123"]

def check_password_strength(password):
    score = 0
    suggestions = []

    if password.lower() in COMMON_PASSWORDS:
        return "Very Weak", ["This is a commonly used password!"]

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8–12 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    if re.search(r"(.)\1\1", password):
        suggestions.append("Avoid repeated characters (e.g., aaa)")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    elif score <= 6:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, suggestions


def generate_strong_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

password = input("Enter password: ")

strength, suggestions = check_password_strength(password)

print("\n🔐 Password Strength:", strength)

if suggestions:
    print("\n⚠ Suggestions to improve:")
    for s in suggestions:
        print("•", s)

if strength in ["Weak", "Very Weak"]:
    print("\n💡 Suggested Strong Password:", generate_strong_password())