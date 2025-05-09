guess = 0
tries = 0

print('===================== Guess the Number =====================\n')
while guess != 6 and tries < 5:
  guess = int(input('Guess the Number: '))
  tries += 1    # always remember increment syntax
                # to count the number of tries

if tries != 5:
  print("You got it!")
else:
  print('You failed! You have used all your tries.')
