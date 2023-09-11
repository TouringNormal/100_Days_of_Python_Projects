#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bids = {}
finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = " "
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid ${bid_amount}")

while not finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    is_finished = input("Are there any other bidders? Type 'yes' or 'no'.")
    if is_finished == "no":
        finished = True
        highest_bidder(bids)
    elif is_finished == "yes":
        finished = False






