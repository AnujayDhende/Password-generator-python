# Password Generator Project
import random
import sys

letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get values from command line or use defaults
try:
    nr_letters = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    nr_symbols = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    nr_numbers = int(sys.argv[3]) if len(sys.argv) > 3 else 3
except ValueError:
    print("Invalid input. Please provide integers for letters, symbols, and numbers.")
    sys.exit(1)

# Easy Level Password (letters + symbols + numbers in order)
password = ""

for _ in range(nr_letters):
    password += random.choice(letters)

for _ in range(nr_symbols):
    password += random.choice(symbols)

for _ in range(nr_numbers):
    password += random.choice(numbers)

print("Generated Password:", password)


