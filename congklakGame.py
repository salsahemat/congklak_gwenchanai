import tkinter as tk
from tkinter import *
from tkinter import messagebox
from congklak_logic import Congklak
from PIL import Image, ImageTk

class CongklakGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Congklak Game")

        seed = Image.open('asset/biji.png')
        seed = seed.resize((60, 60), Image.LANCZOS)
        self.hole_image = ImageTk.PhotoImage(seed)

        self.game = Congklak()

        self.buttons = []
        self.button_labels = []
        
        # Koordinat x & y
        start_x, start_y = 125, 200  

        # jarak sumbu x
        distance_x = 83  

        # jarak sumbu y
        distance_y = 100  

        for i in range(16):
            
            # posisi koordinat atas baris
            if i < 8:  
                x_position = start_x + (i * distance_x)
                y_position = start_y
            # posisi koordinat bawah baris
            else:  
                x_position = start_x + 90 + ((15 - i) * distance_x)
                y_position = start_y + distance_y

            # jika index i lebih dari 8, maka nilai rownya adalah 2
            row = 0 if i < 9 else 2

            
            # jika index i lebih dari 8, maka nilai rownya adalah 15 - nilai index i
            col = i if i < 9 else 16 - i

            # frame untuk biji & label angka yang menunjukkan jumlah biji
            button_frame = tk.Frame(self.master)
            button_frame.grid(row=row+1, column=col, padx=10)

            # inisialisasi tombol biji
            button = tk.Button(self.master, width=30, height=55, image=self.hole_image, command=lambda i=i: self.make_player_move(i))
            # button = tk.Button(button_frame, image=self.hole_image, command=lambda i=i: self.make_player_move(i))
            # button.grid(row=0, column=0, padx=3, pady=3)
            button.place(x=x_position, y=y_position)
            self.buttons.append(button)
            
            # inisialisasi label angka
            label = tk.Label(self.master, text=str(self.game.board[i]))
            # label = tk.Label(button_frame, text=str(self.game.board[i]))
            # label.grid(row=1, column=0)
            label.place(x=x_position, y=y_position + 70)
            self.button_labels.append(label)

        # frame untuk menampilkan AI House
        self.ai_frame = tk.Frame(self.master, borderwidth=2, relief="solid")
        # self.ai_frame.grid(row=0, column=0, columnspan=7, padx=5, pady=5)
        self.ai_frame.place(x=100, y=150)

        # label untuk menampilkan tulisan AI House
        self.ai_house_label = tk.Label(self.ai_frame, text=f"AI House\n{self.game.board[8:16][::-1]}", justify='center')
        self.ai_house_label.pack()

        # frame untuk menampilkan Player House
        self.player_frame = tk.Frame(self.master, borderwidth=2, relief="solid")
        # self.player_frame.grid(row=2, column=7, columnspan=7, padx=5, pady=5)
        self.player_frame.place(x=800, y=150)

        # label untuk menampilkan tulisan Player Hause
        self.player_house_label = tk.Label(self.player_frame, text=f"Player House\n{self.game.board[:8]}")
        self.player_house_label.pack()

        # label untuk menampilkan tulisan Ai Store
        self.ai_store_label = tk.Label(self.master, text=f"AI Store: {self.game.board[0]}")
        # self.ai_store_label.grid(row=1, column=6)
        self.ai_store_label.place(x=100, y=120)

        # label untuk menampilkan tulisan Player Store
        self.player_store_label = tk.Label(self.master, text=f"Player Store: {self.game.board[8]}")
        # self.player_store_label.grid(row=1, column=7, columnspan=2)
        self.player_store_label.place(x=800, y=120)

        # menampilkan tombol reset
        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game)
        # self.reset_button.grid(row=4, column=0, columnspan=14)
        self.reset_button.place(x=400, y=450)

    def make_player_move(self, move):
        # Player's move
        self.game.make_move(move, 1)
        self.update_gui()

        if self.game.is_game_over():
            self.show_winner()
        else:
            # Introduce a delay of 990 milliseconds (adjust as needed)
            self.master.after(990, self.make_ai_move)

    def make_ai_move(self):
        # AI's move
        ai_move = self.game.find_best_move()
        self.game.make_move(ai_move, 2)
        self.update_gui()

        if self.game.is_game_over():
            self.show_winner()

    def update_gui(self):
        for i in range(16):
            self.buttons[i].config(text=str(self.game.board[i]))
            self.button_labels[i].config(text=str(self.game.board[i]))

        self.ai_house_label["text"] = f"AI House\n{self.game.board[8:15][::-1]}"
        self.player_house_label["text"] = f"Player House\n{self.game.board[:8]}"
        self.ai_store_label["text"] = f"AI Store: {self.game.board[0]}"
        self.player_store_label["text"] = f"Player Store: {self.game.board[8]}"

    def show_winner(self):
        if self.game.board[8] > self.game.board[0]:
            winner = "Player 1"
        elif self.game.board[8] < self.game.board[0]:
            winner = "AI"
        else:
            winner = "It's a draw!"

        messagebox.showinfo("Game Over", f"The game is over! {winner} wins!")

    def reset_game(self):
        self.game = Congklak()
        # Atur nilai store AI dan store pemain menjadi 0
        self.game.board[0] = 0
        self.game.board[8] = 0

        self.update_gui()