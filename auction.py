# Importing operating system logic and art assets:
import os
import auction_art

# Creating variables:
# 1. A dictionary to store bids
# 2. Variables to store winner's name and bid
auction = {}
winner_name = ""
winner_bid = 0

# Bidding function that will gather user bids into the dictionary;
# Uses recursion to chain itself:
def bidding():
    # Gathering user input:
    # 1. Bidder's name
    # 2. Bidder's bid
    # 3. Will there be more bidders or not
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    again = input("Are there any other bidders? Type YES or NO: ").lower()

    # Writing new bid into the dictionary:
    auction[name] = bid

    # Clearing the screen;
    # This line was lifted from stackoverflow;
    # Works for most operating systems:
    os.system('cls' if os.name == 'nt' else 'clear')

    # Chaining itself unless user said otherwise:
    if again == "yes":
        bidding()

# Winner function that will go through the dictionary to find the highest bid:
def winner():
    # Increasing scope:
    global winner_name
    global winner_bid

    # Going through each key in the dictionary;
    # Saving highest key: value pair:
    for name in auction:
        if auction[name] > winner_bid:
            winner_name = name
            winner_bid = auction[name]


# Main logic:
# 1. Print intro art
# 2. Run bidding function to gather bids
# 3. Run winner function to determine the winner
print(auction_art.logo)
print("Welcome to the blind auction!")
bidding()
winner()

# Final statement:
print(f"The winner is {winner_name} with a bid of ${winner_bid}!")
