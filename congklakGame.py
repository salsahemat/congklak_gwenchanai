import tkinter as tk
from tkinter import messagebox
from congklak_logic import Congklak

class CongklakGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Congklak Game")

        self.hole_image = tk.PhotoImage(file="asset/biji.png")
        self.hole_image = self.hole_image.subsample(7)

        self.store_image = tk.PhotoImage(file="asset/tempat1.png")
        self.store_image = self.store_image.subsample(7)

        self.game = Congklak()

        self.buttons = []
        self.button_labels = []
        for i in range(14):
            row = 0 if i < 7 else 2
            col = i if i < 7 else 13 - i
            button_frame = tk.Frame(self.master)
            button_frame.grid(row=row+1, column=col)

            button = tk.Button(button_frame, image=self.hole_image, command=lambda i=i: self.make_player_move(i))
            button.grid(row=0, column=0)
            self.buttons.append(button)

            label = tk.Label(button_frame, text=str(self.game.board[i]))
            label.grid(row=1, column=0)
            self.button_labels.append(label)

        self.ai_frame = tk.Frame(self.master, borderwidth=2, relief="solid")
        self.ai_frame.grid(row=0, column=0, columnspan=7, padx=5, pady=5)

        self.ai_house_label = tk.Label(self.ai_frame, text=f"AI House\n{self.game.board[7:14][::-1]}", justify='left')
        self.ai_house_label.pack()

        self.player_frame = tk.Frame(self.master, borderwidth=2, relief="solid")
        self.player_frame.grid(row=2, column=7, columnspan=7, padx=5, pady=5)

        self.player_house_label = tk.Label(self.player_frame, text=f"Player House\n{self.game.board[:7]}")
        self.player_house_label.pack()

        self.ai_store_label = tk.Label(self.master, text=f"AI Store: {self.game.board[0]}")
        self.ai_store_label.grid(row=1, column=6)

        self.player_store_label = tk.Label(self.master, text=f"Player Store: {self.game.board[7]}")
        self.player_store_label.grid(row=1, column=7, columnspan=2)

        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=14)

    def make_player_move(self, move):
        self.game.make_move(move, 1)
        self.update_gui()

        if self.game.is_game_over():
            self.show_winner()
        else:
            ai_move = self.game.find_best_move()
            self.game.make_move(ai_move, 2)
            self.update_gui()

            if self.game.is_game_over():
                self.show_winner()

    def update_gui(self):
        for i in range(14):
            self.buttons[i].config(text=str(self.game.board[i]))
            self.button_labels[i].config(text=str(self.game.board[i]))

        self.ai_house_label["text"] = f"AI House\n{self.game.board[7:14][::-1]}"
        self.player_house_label["text"] = f"Player House\n{self.game.board[:7]}"
        self.ai_store_label["text"] = f"AI Store: {self.game.board[0]}"
        self.player_store_label["text"] = f"Player Store: {self.game.board[7]}"

    def show_winner(self):
        winner = "Player 1" if self.game.board[7] > self.game.board[0] else "AI"
        messagebox.showinfo("Game Over", f"The game is over! {winner} wins!")

    def reset_game(self):
        self.game = Congklak()
        self.update_gui()

root = tk.Tk()
app = CongklakGUI(root)
root.mainloop()
