from password_checker import check_password_strength
from password_generator import generate_password
from utils import password_tips

print("Smart Password Strength Checker")

password = input("Enter a password: ")

strength = check_password_strength(password)

print("Password Strength:", strength)

print("\nSecurity Tips:")
for tip in password_tips():
    print("-", tip)

print("\nSuggested Strong Password:", generate_password())
