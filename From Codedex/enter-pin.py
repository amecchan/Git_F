# Write code below 💖
# This code is a simple ATM PIN verification program.
# It prompts the user to enter a PIN and checks if it matches the given PIN (1234).
# If the entered PIN is incorrect, it keeps asking for the PIN until the correct one is entered.

print('BANK OF CODEDEX')
pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. \nEnter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')