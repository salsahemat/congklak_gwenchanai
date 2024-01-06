import tkinter as tk
from tkinter import *
from congklak_logic import Congklak
from PIL import Image, ImageTk

class CongklakGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Congklak Game")

        seed = Image.open('asset/biji.png')
        seed = seed.resize((60, 60), Image.ANTIALIAS)
        self.hole_image = ImageTk.PhotoImage(seed)

        # self.hole_image = tk.PhotoImage(file="asset/biji.png")
        # self.hole_image = self.hole_image.subsample(4,4)

        self.game = Congklak()

        self.buttons = []
        self.button_labels = []

        start_x, start_y = 210, 200  # You need to adjust these values based on your background
        circle_distance_x = 83  # The horizontal distance between centers of circles
        circle_distance_y = 100  # The vertical distance between top and bottom row centers

        for i in range(14):

            if i < 7:  # Top row
                x_position = start_x + (i * circle_distance_x)
                y_position = start_y
            else:  # Bottom row
                x_position = start_x + ((13 - i) * circle_distance_x)
                y_position = start_y + circle_distance_y


            row = 0 if i < 7 else 2
            col = i if i < 7 else 13 - i
            button_frame = tk.Frame(self.master)
            button_frame.grid(row=row+1, column=col, padx=10)

            button = tk.Button(self.master, width=30, height=55, image=self.hole_image, command=lambda i=i: self.make_player_move(i))
            # button = tk.Button(button_frame, image=self.hole_image, command=lambda i=i: self.make_player_move(i))
            # button.grid(row=0, column=0, padx=3, pady=3)
            button.place(x=x_position, y=y_position)
            self.buttons.append(button)
            
            label = tk.Label(self.master, text=str(self.game.board[i]))
            # label = tk.Label(button_frame, text=str(self.game.board[i]))
            # label.grid(row=1, column=0)
            label.place(x=x_position, y=y_position + 70)
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
        # Player's move
        self.game.make_move(move, 1)
        self.update_gui()

        if self.game.is_game_over():
            self.show_winner()
        else:
            # Introduce a delay of 850 milliseconds (adjust as needed)
            self.master.after(850, self.make_ai_move)

    def make_ai_move(self):
        # AI's move
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
        # Atur nilai store AI dan store pemain menjadi 0
        self.game.board[0] = 0
        self.game.board[7] = 0

        self.update_gui()

# root = tk.Tk()
# app = CongklakGUI(root)
# root.mainloop()
