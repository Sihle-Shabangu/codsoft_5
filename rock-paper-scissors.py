import random


def main():
    valid_moves = ["rock", "paper", "scissors"]

    player = input("Please enter your name: ")
    print("Welcome!", player)

    ties, wins, loss = 0, 0, 0

    while True:
        random.shuffle(valid_moves)
        player_move = input("Enter your move (rock/paper/scissors) or type 'exit' to quit: ").lower()

        if player_move in ("exit", "quit"):
            if any([ties, wins, loss]):
                print(f"Ties: {ties}, Wins: {wins}, Losses: {loss}")
                print(win_lose(wins, loss), "\nGoodbye!")
            else:
                print("Goodbye!")
            break

        elif player_move in valid_moves:
            computer = random.choice(valid_moves)
            print(f"{player.capitalize()} ({player_move.capitalize()}) vs. Computer ({computer.capitalize()})")

            if player_move == computer:
                ties += 1
                print("You tied!")
            elif (
                (player_move == "rock" and computer == "scissors")
                or (player_move == "paper" and computer == "rock")
                or (player_move == "scissors" and computer == "paper")
            ):
                wins += 1
                print("You win!")
            else:
                loss += 1
                print("You lose!")
        else:
            print("Invalid move!")


def win_lose(w, l):
    if w == l:
        return "You tied!"
    elif w > l:
        return "You won!"
    else:
        return "You lost!"


if __name__ == "__main__":
    main()
