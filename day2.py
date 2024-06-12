""" Day 2 """

# num = 12;
# value = str(num)
# num1 = int(value[0])
# num2 = int(value[1])
# answer = num1 + num2
# print(answer)

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
bill_amount = int(input("What was the total bill? $\n"))
tip_percentage = int(
    input("How much tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))

tip_amount = (bill_amount * tip_percentage) / 100
total_amount = bill_amount + tip_amount
amount_per_person = total_amount / people
rounded_amount_per_person = round(amount_per_person, 2)

print(
    f"Your bill total is {bill_amount}, split between {people} people, with a {tip_amount}% tip, each person should pay ${rounded_amount_per_person}")
