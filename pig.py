import random

def TakeATurn():
    turn_total = 0
    rollagain = True
    while rollagain:
        roll = random.randint(1,6)
        print(f"Rolled: {roll}")
        if roll == 1:
            print("You rolled a 1. You lose!\n")
            return 0
        else:
            turn_total += roll
            print(f"Turn total: {turn_total}")
            rollagain = input("Roll again? (y/n): ").lower() == 'y'
    return turn_total
    
def Pig():
    player_1_score = 0
    player_2_score = 0
    while player_1_score < 100 and player_2_score < 100:
        print("Player 1's turn:")
        player_1_score += TakeATurn()
        print(f"Player 1 score: {player_1_score}\n")
        if player_1_score >= 100:
            print("Player 1 wins!")
            break
        
        print("Player 2's turn:")
        player_2_score += TakeATurn()
        print(f"Player 2 score: {player_2_score}\n")
        if player_2_score >= 100:
            print("Player 2 wins!")
            break
Pig()
