""" Function Parameters """

# def greet(name):
#     print(f"Hello {name}!")
    
# greet("Timmy")

# def greet_with(name, location):
#     print(f"Hello {name}, what is it like in {location}?")

# greet_with(name="James", location="New York")

# # Check for prime number
# def prime_checker(num):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#     if is_prime:
#         print(f"{num} is a prime number.0.
#               0")
#     else:
#         print(f"{num} is not a prime number.")
            
            
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 