""" Day 1 """

# print("Hello\nHello\nHello")
# print("Jerome" + " " + "Haynes")

# first = "Jerome"
# last = "Haynes"
# print(f"{first} {last}")
# print("Hello how are you?")

# 1. Create a greeting for your program.
greeting = "Welcome to the band name generator!"
print(greeting)
# 2. Ask the user for the city that they grew up in.
city = input("What city did you grow up in?\n")
# 3. Ask the user for the name of a pet.
pet = input("What is a name of your favorite pet?\n")
# 4. Combine the name of their city and pet and show them their band name.
band_name = f"{city} {pet}"
# 5. Make sure the input cursor shows on a new line:
print(f"Your band name is {band_name}")