 
bids = {}
biding_finished= False

def find_highest_bidder(bidding_reccord):
    highest_bidd=0
    winner=""
    for bidder in bidding_reccord:
        bid_amount=bidding_reccord[bidder]
        if bid_amount > highest_bidd:
            highest_bidd =bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")



while not biding_finished:
    name=input("What is your name?")
    price=input("What is your bid? $")
    bids[name] = price
    should_continue=input("Are there  any other bidders? Type 'yes' or 'No'.\n" )
    if should_continue == "no":
        biding_finished=True
        find_highest_bidder(bids)
    elif should_continue=="yes":
        clear

