import random
import tkinter as tk
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"
def on_button_click(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)
    update_scores(result)
def update_scores(result):
    global player_score, computer_score
    if result == "You win!":
        player_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    player_score_label.config(text=f"Player: {player_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")
player_score = 0
computer_score = 0
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")  
heading_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 17))
heading_label.pack(pady=5)
result_label = tk.Label(root, text="", font=("Helvetica", 10))
result_label.pack(pady=10)
choices_frame = tk.Frame(root)
choices_frame.pack(pady=10)
rock_button = tk.Button(choices_frame, text="Rock", width=10, command=lambda: on_button_click("Rock"))
rock_button.grid(row=0, column=0, padx=5)
paper_button = tk.Button(choices_frame, text="Paper", width=10, command=lambda: on_button_click("Paper"))
paper_button.grid(row=0, column=1, padx=5)
scissors_button = tk.Button(choices_frame, text="Scissors", width=10, command=lambda: on_button_click("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)
scores_heading_label = tk.Label(root, text="Scores", font=("Helvetica", 14),pady=20)
scores_heading_label.pack(pady=(0,5))
scores_frame = tk.Frame(root)
scores_frame.pack(pady=(0,10))
player_score_label = tk.Label(scores_frame, text=f"Player: {player_score}")
player_score_label.grid(row=2, column=0, padx=5)
computer_score_label = tk.Label(scores_frame, text=f"Computer: {computer_score}")
computer_score_label.grid(row=2, column=1, padx=5)
root.mainloop()

