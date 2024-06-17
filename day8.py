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

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    new_str = ""
    for letter in text:
        current_index =  alphabet.index(letter)
        new_index = (current_index + shift) % len(alphabet)
        shift_letters = alphabet[new_index] 
        new_str += shift_letters
        print(new_str) 
        
# encrypt("hello", 5)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.