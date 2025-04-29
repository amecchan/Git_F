#Here is currency conversion code that converts currency from pesos, soles, and reais to USD.
#This is a simple exercise from codedex.io 

co_usd = 0.00024
pe_usd = 0.27
br_usd = 0.18
money1 = int(input("What do you have left in pesos? "))
money2 = int(input("What do you have left in soles? "))
money3 = int(input("What do you have left in reais? "))
total = (money1*co_usd)+(money2*pe_usd)+(money3*br_usd)
print(total)