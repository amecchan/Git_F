# A program that checks if a user can ride a roller coaster based on their height and credits.
# The maximum height is 137 cm and the minimum credits required is 10.

height = int(input('What is your height(cm)? '))
credits = int(input('How many credits do you have? '))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif not height >= 137 and credits >= 10:
  print("You are not tall enough to ride.")
elif height >= 137 and not credits >= 10:
  print("You don't have enough credits.")
else:
  print("Neither requirements are met.")