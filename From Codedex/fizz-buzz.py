# fizz-buzz.py
# FizzBuzz is a classic programming problem that is often used in coding interviews.
# The task is to print from 1 to 100
# if it's divisible by 3, print "Fizz", if it's divisible by 5, print "Buzz",
# if it's divisible by both 3 and 5, print "FizzBuzz", otherwise print the number itself.
ans = 0

print("-------FizzBuzz-------")
for ans in range(1, 100, +1): # or (1, 101), they're the same
    if ans % 3 == 0 and ans % 5 == 0:
        print("FizzBuzz ⚡🐝")
    elif ans % 3 == 0:
        print("Fizz 🥤")
    elif ans % 5 == 0:
        print("Buzz 🐝")
    else:
        print(ans)
print("-----------------------")  