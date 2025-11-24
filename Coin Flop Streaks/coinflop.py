import random
# Coin Flip Streaks
"""
 Your program breaks up the experiment into two parts: the first part
 generates a list of randomly selected 'heads'  and 'tails' values, and the second part checks if there is a streak
 in it. 
 Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what
 percentage of the coin flips contains a streak of six heads or tails in a row. 
 As a hint, the function call
 random.randint(0, 1)  will return a 0 value 50% of the time and a 1 value the other 50% of the time.
  
"""
#Import random module
# Create a function- prints either H or T for X- number of times, using a while loop.
    # create a list containing two variable: Heads and Tails

def coin_flip():
    tosses = ['H', 'T']
    outcome = []

    while True:
        try:
            no_tosses = int(input("Enter number of coin tosses: "))
            if no_tosses < 1:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Enter a valid integer.")

    for _ in range(no_tosses): #For input smaller than no_losses.
        outcome.append(random.choice(tosses)) 

    num_h = outcome.count('H')
    num_t = outcome.count('T')

    total = num_h + num_t #used to find percentage of tosses.

    per_h = (num_h / total) * 100
    per_t = (num_t / total) * 100

    return f"'H' appears {num_h}: {per_h:.2f}%, 'T' appears {num_t}: {per_t:.2f}%"

print(coin_flip())