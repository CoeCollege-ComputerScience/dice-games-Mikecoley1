import random


def Predictions():
    players = ["Player 1", "Player 2", "Player 3"]
    active_players = players[:]
    num_dice = 10

    print("Welcome to the Predictions Game!")
    print("Each player predicts a number between 1 and 6, rolls 10 dice, and looks for a pair.")
    print("If no pair matches the prediction, the player is out. The last player standing wins!\n")

    while len(active_players) > 1:
        for player in active_players[:]:
            input(f"\n{player}'s turn! Press Enter to roll the dice...")

            prediction = random.randint(1, 6)
            dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]

            print(f"{player} predicts: {prediction}")
            print(f"{player} rolls: {dice_rolls}")

            if dice_rolls.count(prediction) >= 2:
                print(f"{player} stays in the game!")
            else:
                print(f"{player} is out!")
                active_players.remove(player)

            if len(active_players) == 1:
                break

    print(f"\nGame over! The winner is {active_players[0]}!")

# Main function
def main():
    Predictions()

main()