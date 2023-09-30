from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry('520x445')
root.title('Tic Tac Toe')
root.resizable(False,False)
#root.config(bg='grey')

label = tk.Label(root,bd=20,relief=FLAT, text='TIC TAC TOE', height=2, width=24, font=("Helvetica", 24,"bold"),bg='grey',fg='white')
label.grid(columnspan=5)
label.place(x=9,y=5)

buttonframe=Frame(root,bd=10,relief=RAISED)
buttonframe.grid(columnspan=5)
buttonframe.place(x=11,y=125)

current_player = "X"  # Initialize the current player

# Create a 2D list to represent the game board
game_board = [["" for _ in range(3)] for _ in range(3)]


def check_winner(player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(game_board[i][j] == player for j in range(3)) or \
                all(game_board[j][i] == player for j in range(3)):
            return True
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == player or \
            game_board[0][2] == game_board[1][1] == game_board[2][0] == player:
        return True
    return False


def on_button_click(row, col):
    global current_player

    if game_board[row][col] == "" and not check_winner("X") and not check_winner("O"):
        game_board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner(current_player):
            label.config(text=f"Player {current_player} wins!!!")
        elif all(game_board[i][j] != "" for i in range(3) for j in range(3)):
            label.config(text="It's a tie!")
        else:
            current_player = "O" if current_player == "X" else "X"


# Create buttons and add click event handlers

buttons = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(buttonframe, bg='lightgrey', text='', width=10, height=2, font=("Helvetica", 14),
                               padx=20, pady=20, command=lambda row=i, col=j: on_button_click(row, col))
        buttons[i][j].grid(row=i + 2, column=j + 1)



root.mainloop()

