#example 1
import random 
for i in range(10): 
    print("Dice roll:", random.randint(1, 6)) 


#example 2
import random 
heads = 0 
tails = 0 
for _ in range(100): 
    if random.choice(["Heads", "Tails"]) == "Heads": 
        heads += 1 
else: 
    tails += 1 
    print("Heads:", heads) 
    print("Tails:", tails)

#example 3
lottery = random.sample(range(1, 50), 6) 
print("Lottery numbers:", lottery)

#example 4 
import random 
import string
characters = string.ascii_uppercase + string.ascii_lowercase + string.digits +"!#$%^&*" 
password = "".join(random.choice(characters) for _ in range(10)) 
print("Generated password:", password) 


#example 5
import random 
number = random.randint(1, 50) 
while True: 
    guess = int(input("Enter your guess: ")) 
if guess > number: 
    print("Too High") 
elif guess < number: 
    print("Too Low") 
else: 
    print("Correct! You guessed it.") 
    br

    