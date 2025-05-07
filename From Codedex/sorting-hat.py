#Here's a recap of everything we learned so far:

# Control flow is the order in which the program's code executes.
# if statement tests a condition for truth and executes the code if it's True.
# elif clause can be added between if and else.
# else executes the code if none of the above is True.
# Relational operators are used to compare two values: ==, !=, >, >=, <, <=.
# Logical operators are used to combine two or more conditions: and, or, not.

print("\t\t-------------------")   
print("\t\t SORTING HAT QUIZ")
print("\t\t-------------------")    

gryffindor = 0
raven = 0
huffle = 0
slyth = 0

print("Q1) Do you like Dawn or Dusk? \n1)  Dawn \n2)  Dusk")
ans1 = int(input("Answer: "))

if ans1 == 1:
  gryffindor +=1
  raven += 1
elif ans1 == 2:
  huffle += 1
  slyth += 1
else :
  print("Wrong input")

print("\nQ2) When I’m dead, I want people to remember me as: \n1)  The Good \n2)  The Great \n3)  The Wise \n4)  The Bold")
ans2 = int(input("Answer: "))

if ans2 == 1:
    huffle += 1
elif ans2 == 2: 
    slyth += 1
elif ans2 == 3:
    raven += 1
elif ans2 == 4:
    gryffindor += 1
else:
    print("Wrong input")

print("\nQ3) Which kind of instrument most pleases your ear? \n1)  The violin \n2)  The trumpet \n3)  The piano \n4)  The drum")
ans3 = int(input("Answer: "))

if ans3 == 1:
    slyth += 1
elif ans3 == 2:
    gryffindor += 1
elif ans3 == 3:
    raven += 1
elif ans3 == 4:
    huffle += 1
else:
    print("Wrong input")


print("\n\nCalculating your house...")
print("\n\nYour scores are:")
print("Gryffindor = ", gryffindor)
print("Ravenclaw = ", raven)
print("Hufflepuff = ", huffle)
print("Slytherin = ", slyth)
print("\n")

print("\n\nCongratulations! You have completed the quiz. \nNow let's see which house you belong to!")

if gryffindor > raven and gryffindor > huffle and gryffindor > slyth:
    print("You are in Gryffindor")
elif raven > gryffindor and raven > huffle and raven > slyth:
    print("You are in Ravenclaw")
elif huffle > gryffindor and huffle > raven and huffle > slyth:
    print("You are in Hufflepuff")
elif slyth > gryffindor and slyth > raven and slyth > huffle:
    print("You are in Slytherin")
else:
    print("You are in a house that is not listed")

