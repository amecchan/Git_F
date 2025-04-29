# A program that tells if a pH value (0-14) is acidic, basic, or neutral.

ph = int(input("Enter a pH value between 0 and 14: "))

if ph > 7:
  print("Basic")
elif ph < 7:
    print("Acidic")
else:
    print("Netural")
