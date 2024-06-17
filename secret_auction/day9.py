""" Dictionary """
# example = {
#     "bug": "An error in a program that prevents the program from running as expected.",
#     "function": "A piece of code that you can easily call over. Helps with (DRY)",
# }

# example["css"] = "Used to style web pages"

# print(example["bug"])
# print(example.get("bug"))
# print(example)

# for (key, value) in example.items():
#     print(key, value)

from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    pass 
  else:
    print("Please type 'yes' or 'no'.")