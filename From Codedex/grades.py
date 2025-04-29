# It prompts the user to enter a grade between 0 and 100 and prints the result if passed or failed.

grade = int(input("Enter a grade between 0-100: "))

if grade >= 55:
  print("You passed!")
else:
  print("You failed")