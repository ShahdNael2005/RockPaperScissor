import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Set up the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("800x400")

# Load images for Rock, Paper, and Scissors
rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))

# Load different images for computer choices
computer_rock_img = ImageTk.PhotoImage(Image.open("rockC.png").resize((100, 100)))
computer_paper_img = ImageTk.PhotoImage(Image.open("paperC.png").resize((100, 100)))
computer_scissors_img = ImageTk.PhotoImage(Image.open("scissorsC.png").resize((100, 100)))

# Choices for the game
options = ("Rock", "Paper", "Scissors")

# Initialize scores and high score
player_score = 0
computer_score = 0
high_score = 0

# Function to handle the game logic
def play(player_choice):
    global player_score, computer_score, high_score

    computer_choice = random.choice(options)

    # Update player choice image
    player_choice_label.config(image=choice_images[player_choice])

    # Update computer choice image
    if computer_choice == "Rock":
        computer_choice_label.config(image=computer_rock_img)
    elif computer_choice == "Paper":
        computer_choice_label.config(image=computer_paper_img)
    else:
        computer_choice_label.config(image=computer_scissors_img)

    # Determine the outcome
    if player_choice == computer_choice:
        result.set("It's a tie!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result.set("You win!")
        player_score += 1
        # Update high score if necessary
        if player_score > high_score:
            high_score = player_score
    else:
        result.set("You lose!")
        computer_score += 1

    # Update scores
    player_score_label.config(text=f"Player Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    high_score_label.config(text=f"High Score: {high_score}")

    # Show the restart button
    retry_button.grid(row=0, column=0, padx=10, pady=10)

# Function to handle the start of the game
def start_game():
    main_menu_frame.grid_forget()  # Hide the main menu
    game_frame.grid(row=0, column=0, sticky="nsew")  # Show the game frame
    rock_button.grid(row=1, column=0, padx=10, pady=10)
    paper_button.grid(row=1, column=1, padx=10, pady=10)
    scissors_button.grid(row=1, column=2, padx=10, pady=10)
    player_choice_label.grid(row=0, column=1, padx=20, pady=10)
    computer_choice_label.grid(row=0, column=2, padx=20, pady=10)
    player_label.grid(row=0, column=0, padx=20, pady=10)
    computer_label.grid(row=0, column=3, padx=20, pady=10)
    player_score_label.grid(row=2, column=0, pady=5)
    computer_score_label.grid(row=2, column=2, pady=5)
    high_score_label.grid(row=2, column=1, pady=5)  # High score label
    result_label.grid(row=3, column=0, columnspan=4, pady=10)

    # Hide the restart button initially
    retry_button.grid_forget()

# Function to handle returning to the main menu
def main_menu():
    game_frame.grid_forget()  # Hide the game frame
    main_menu_frame.grid(row=0, column=0, sticky="nsew")  # Show the main menu frame

# Function to show the "How to Play" instructions
def show_instructions():
    instructions_window = tk.Toplevel(root)
    instructions_window.title("How to Play")
    instructions_window.geometry("400x200")

    instructions_text = (
        "Rock Paper Scissors Game Instructions:\n\n"
        "1. Choose Rock, Paper, or Scissors.\n"
        "2. The computer will make a choice.\n"
        "3. Rock beats Scissors.\n"
        "Scissors beats Paper.\n"
        "Paper beats Rock.\n"
        "4. The winner is displayed on the screen.\n"
        "5. Your score and the computer's score are updated."
    )

    instructions_label = tk.Label(instructions_window, text=instructions_text, padx=20, pady=20, font=("Arial", 12))
    instructions_label.pack()

# Function to show the high score in a message box
def show_high_score():
    messagebox.showinfo("High Score", f"Current High Score: {high_score}")

# Function to restart the game
def restart_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    player_score_label.config(text=f"Player Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    player_choice_label.config(image=None)
    computer_choice_label.config(image=None)
    result.set("Make your choice!")

# Function to exit the game
def exit_game():
    root.destroy()

# Store images in a dictionary for easy reference
choice_images = {
    "Rock": rock_img,
    "Paper": paper_img,
    "Scissors": scissors_img
}

# GUI layout
main_menu_frame = tk.Frame(root)
main_menu_frame.grid(row=0, column=0, sticky="nsew")

start_button = tk.Button(main_menu_frame, text="Start", command=start_game, font=("Arial", 16))
start_button.grid(row=0, column=0, padx=20, pady=10)

instructions_button = tk.Button(main_menu_frame, text="How to Play", command=show_instructions, font=("Arial", 16))
instructions_button.grid(row=1, column=0, padx=20, pady=10)

high_score_button = tk.Button(main_menu_frame, text="High Score", command=show_high_score, font=("Arial", 16))
high_score_button.grid(row=2, column=0, padx=20, pady=10)

exit_button = tk.Button(main_menu_frame, text="Exit", command=exit_game, font=("Arial", 16))
exit_button.grid(row=3, column=0, padx=20, pady=10)

# Game frame (initially hidden)
game_frame = tk.Frame(root)

# Buttons for player choices (initially hidden)
rock_button = tk.Button(game_frame, image=rock_img, command=lambda: play("Rock"))
paper_button = tk.Button(game_frame, image=paper_img, command=lambda: play("Paper"))
scissors_button = tk.Button(game_frame, image=scissors_img, command=lambda: play("Scissors"))

# Labels to display choices
player_choice_label = tk.Label(game_frame, text="Your Choice", font=("Arial", 14))
computer_choice_label = tk.Label(game_frame, text="Computer's Choice", image=None)

# Labels to display scores
player_score_label = tk.Label(game_frame, text=f"Player Score: {player_score}", font=("Arial", 14))
computer_score_label = tk.Label(game_frame, text=f"Computer Score: {computer_score}", font=("Arial", 14))

# Label to show the result
result = tk.StringVar()
result_label = tk.Label(game_frame, textvariable=result, font=("Arial", 16))

# Labels for identifying player and computer
player_label = tk.Label(game_frame, text="Your Choice", font=("Arial", 14))
computer_label = tk.Label(game_frame, text="Computer's Choice", font=("Arial", 14))

# Label to show the high score
high_score_label = tk.Label(game_frame, text=f"High Score: {high_score}", font=("Arial", 14))

# Bottom buttons frame
bottom_buttons_frame = tk.Frame(game_frame)

# Retry, Main Menu, and Exit buttons
retry_button = tk.Button(bottom_buttons_frame, text="Restart", command=restart_game, font=("Arial", 14))
retry_button.grid(row=0, column=0, padx=10, pady=10)

main_menu_button = tk.Button(bottom_buttons_frame, text="Main Menu", command=main_menu, font=("Arial", 14))
main_menu_button.grid(row=0, column=1, padx=10, pady=10)

exit_button = tk.Button(bottom_buttons_frame, text="Exit", command=exit_game, font=("Arial", 14))
exit_button.grid(row=0, column=2, padx=10, pady=10)

# Place the bottom_buttons_frame at the bottom of the game_frame
bottom_buttons_frame.grid(row=4, column=0, columnspan=4, pady=10)

# Start the application
root.mainloop()
