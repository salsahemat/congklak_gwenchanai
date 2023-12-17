import tkinter as tk
from tkinter import messagebox

class CongklakGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Congklak Game")

        # Load images for holes and stores
        self.hole_image = tk.PhotoImage(file="asset/biji.png")
        self.store_image = tk.PhotoImage(file="asset/tempat2.png")

        self.game = Congklak()

        self.buttons = []
        for i in range(6):
            button = tk.Button(self.master, image=self.hole_image, command=lambda i=i: self.make_player_move(i))
            button.grid(row=0, column=i)
            self.buttons.append(button)

        self.ai_label = tk.Label(self.master, text=f"Player 2 (AI): {self.game.board[7:13][::-1]} | {self.game.board[13]}")
        self.ai_label.grid(row=1, columnspan=6)

        self.player_label = tk.Label(self.master, text=f"Player 1: {self.game.board[:6]} | {self.game.board[6]}")
        self.player_label.grid(row=2, columnspan=6)

        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=3, columnspan=6)

    def make_player_move(self, move):
        self.game.make_move(move, 1)
        self.update_gui()

        if self.game.is_game_over():
            self.show_winner()

        self.make_ai_move()

    def make_ai_move(self):
        ai_move = self.game.find_best_move()
        self.game.make_move(ai_move, 2)
        self.update_gui()

        if self.game.is_game_over():
            self.show_winner()

    def update_gui(self):
        for i in range(6):
            self.buttons[i]["text"] = str(self.game.board[i])

        self.ai_label["text"] = f"Player 2 (AI): {self.game.board[7:13][::-1]} | {self.game.board[13]}"
        self.player_label["text"] = f"Player 1: {self.game.board[:6]} | {self.game.board[6]}"

    def show_winner(self):
        winner = "Player 1" if self.game.board[6] > self.game.board[13] else "Player 2 (AI)"
        messagebox.showinfo("Game Over", f"The game is over! {winner} wins!")

    def reset_game(self):
        self.game = Congklak()
        self.update_gui()
