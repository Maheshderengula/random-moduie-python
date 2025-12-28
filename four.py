#example 1
import random 
subjects = ["A monkey", "A cat", "The boy"] 
verbs = ["eats", "drives", "plays with"] 
objects = ["a banana", "a car", "a ball"] 
sentence = random.choice(subjects) + " " + random.choice(verbs) + " " + random.choice(objects) 
print(sentence)


#example 2 
import random 
choices = ["rock", "paper", "scissors"] 
user = input("Enter rock/paper/scissors: ") 
computer = random.choice(choices) 
print("Computer choice:", computer) 
if user == computer: 
    print("It's a tie!") 
elif (user == "rock" and computer == "scissors") or \
(user == "paper" and computer == "rock") or  \
(user == "scissors" and computer == "paper"):
    print("You win!") 
else: 
    print("Computer wins!")


#example 3 
import random 
p1_score = 0 
p2_score = 0 
for i in range(5): 
    p1 = random.randint(1, 6) 
    p2 = random.randint(1, 6) 
    p1_score += p1 
    p2_score += p2 
    print(f"Round {i+1}: Player1={p1}, Player2={p2}") 
    print("Total Player 1:", p1_score) 
    print("Total Player 2:", p2_score) 
if p1_score > p2_score: 
    print("Player 1 wins") 
elif p2_score > p1_score: 
    print("Player 2 wins") 
else: 
    print("It's a tie") 