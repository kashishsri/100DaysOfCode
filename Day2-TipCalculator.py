print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? "))
people = int(input("How many people to split the bill? "))
split_total = (bill + tip) / people
# print("Each person should pay: " + str(split_total))
print(f"Each person should pay : {round(split_total, 2)}")