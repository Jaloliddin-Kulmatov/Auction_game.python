from art import logo
print(logo)
bids = {}

def find_highest_bidder(highest_bidder):
    highest_bid = 0
    winner = ""
    for bidder in highest_bidder:
        price = highest_bidder[bidder]
        if price > highest_bid:
            highest_bid = price
            winner = bidder
    print(f"the highes bidder is {winner} with ${highest_bid}")



restart = True
while restart:
    name = str(input("What is your name? "))
    bid = int(input("What is the bid? $"))
    bids[name] = bid
    yes_or_not = input("Are there any other person? 'yes' or 'no'? ").lower()
    if yes_or_not == "yes":
        print("\n" * 100)
    else:
        restart = False
        find_highest_bidder(highest_bidder=bids)





