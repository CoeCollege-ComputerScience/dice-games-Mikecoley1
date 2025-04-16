import random # import the random

def rollDice(): # function to roll the dice
    return random.randint(1,6) + random.randint(1,6) #give the random number between 1 and 6 and returns the sum of the two numbers

def over_under(): # function to play/start the game
    player1_score = 0 # player 1 score
    player2_score = 0 # player 2 score
    target_wins = 3 # target wins
    round_number = 1 # round number
    while player1_score < target_wins and player2_score < target_wins: # while loop to check the score of the players and keeps playing until one hits 6 wins
        print(f"\n Round {round_number}") # print the round number
        round_number += 1 # add 1 to the round number
        p1_roll = rollDice() # player 1 rolls the dice
        print(f"Player 1 rolls: {p1_roll}") # print the player 1 roll

        guess = input("Player 2, guess Over or under: ").strip().lower() # player 2 guesses over or under(no spaces or uppercase)
        p2_roll = rollDice() # player 2 rolls the dice
        print(f"Player 2 rolls: {p2_roll}") # print the player 2 roll

        if (guess == "over" and p2_roll > p1_roll) or (guess == "under" and p2_roll < p1_roll): #checks if palyer 2 guessed right
            print("Player 2 wins that round!") # print player 2 wins
            player2_score += 1 # add 1 to player 2 score
        else: # if player 2 guessed wrong
            print("Player 1 wins that round!") # print player 1 wins
            player1_score += 1 # add 1 to player 1 score
        print(f"Player 1: {player1_score} Player 2: {player2_score}")
    if player1_score >= target_wins: # if player 1 score is greater than or equal to 6
        print("\nPlayer 1 wins the game!") # print player 1 wins
    elif player2_score >= target_wins: # if player 2 score is greater than or equal to 6
        print("\nPlayer 2 wins the game!")
   
      
      
    
    
def main(): # main function
    over_under() # calls function
main() # calls main function