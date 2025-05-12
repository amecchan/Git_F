# Nine-Nine Bottles of Beer on the Wall
# This program prints the lyrics to the song "99 Bottles of Beer on the Wall" until it reaches 0 bottles.


for b in range(99, 0, -1): # Loop from 99 down to 1
  print(f'{b} bottles of beer on the wall')
  print(f'{b} bottles of beer')
  print(f'Take one down, pass it around\n{b-1} bottle of beer on the wall\n')
  
print('No more bottles of beer on the wall')
print('No more bottles of beer')
print('Go to the store and buy some more')
print('99 bottles of beer on the wall...')