import random


def KeepLowest():
    player1_score = 0
    player2_score = 0
    round_number = 1
    num_dice = 5

    print("Welcome to the Keep the Lowest Dice Game!")
    print("First player to reach 20 points wins!\n")

    while player1_score < 20 and player2_score < 20:
        print(f"--- Round {round_number} ---")
        input("Press Enter to roll the dice for both players...")

        p1_roll = [random.randint(1, 6) for _ in range(num_dice)]
        p2_roll = [random.randint(1, 6) for _ in range(num_dice)]

        p1_min = min(p1_roll)
        p2_min = min(p2_roll)

        print(f"Player 1 rolls: {p1_roll} -> Keeps: {p1_min}")
        print(f"Player 2 rolls: {p2_roll} -> Keeps: {p2_min}")

        if p1_min < p2_min:
            player1_score += p1_min
            print(f"Player 1 wins this round! Total score: {player1_score}")
        else:
            player2_score += p2_min
            print(f"Player 2 wins this round! Total score: {player2_score}")

        if player1_score >= 20:
            print("\nPlayer 1 wins the game!")
            break
        elif player2_score >= 20:
            print("\nPlayer 2 wins the game!")
            break

        round_number += 1
        print()  # Blank line for better readability

# Main function
def main():
    KeepLowest()

main()