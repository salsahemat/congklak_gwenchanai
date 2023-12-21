import tkinter as tk
from tkinter import messagebox
from congklak_logic import Congklak

class CongklakGUI:
     # Inisialisasi GUI untuk permainan Congklak
    def __init__(self, master):
        # Inisialisasi kelas CongklakGUI
        self.master = master
        self.master.title("Congklak Game")

        # Load foto untuk biji dan tempat 
        self.hole_image = tk.PhotoImage(file="asset/biji.png")
        self.hole_image = self.hole_image.subsample(7)  # Ubah faktor subsample menjadi 7 agar lebih bisa dilihat

        self.store_image = tk.PhotoImage(file="asset/tempat1.png")
        self.store_image = self.store_image.subsample(7)  # Ubah faktor subsample menjadi 7 agar lebih bisa dilihat

        self.game = Congklak()

        # Membuat tombol-tombol untuk lubang-lubang pemain
        self.buttons = []
        for i in range(6):
            button = tk.Button(self.master, image=self.hole_image, command=lambda i=i: self.make_player_move(i))
            button.grid(row=0, column=i)
            self.buttons.append(button)

        # Label untuk menampilkan status lubang dan toko pemain AI
        self.ai_label = tk.Label(self.master, text=f"Player 2 (AI): {self.game.board[7:13][::-1]} | {self.game.board[13]}")
        self.ai_label.grid(row=1, columnspan=6)

        # Label untuk menampilkan status lubang dan toko pemain manusia
        self.player_label = tk.Label(self.master, text=f"Player 1: {self.game.board[:6]} | {self.game.board[6]}")
        self.player_label.grid(row=2, columnspan=6)

        # Tombol untuk mereset permainan
        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=3, columnspan=6)


    def make_player_move(self, move):
        # Melakukan langkah pemain manusia
        self.game.make_move(move, 1)
        self.update_gui()

        # Memeriksa apakah permainan sudah berakhir
        if self.game.is_game_over():
            self.show_winner()

        # Melakukan langkah pemain AI setelah langkah pemain manusia
        self.make_ai_move()


    def make_ai_move(self):
        # Memanggil fungsi untuk mencari dan melakukan langkah terbaik pemain AI
        ai_move = self.game.find_best_move()
        # Melakukan langkah AI dengan langkah terbaik yang ditemukan
        self.game.make_move(ai_move, 2)
        # Memperbarui tampilan GUI setelah langkah AI
        self.update_gui()

        # Memeriksa apakah permainan sudah berakhir setelah langkah pemain AI
        if self.game.is_game_over():
            # Menampilkan pemenang jika permainan sudah berakhir
            self.show_winner()


    def update_gui(self):
        # Memperbarui tampilan tombol untuk lubang-lubang pemain manusia
        for i in range(6):
            self.buttons[i]["text"] = str(self.game.board[i])

        # Memperbarui teks label untuk status lubang dan toko pemain AI
        self.ai_label["text"] = f"Player 2 (AI): {self.game.board[7:13][::-1]} | {self.game.board[13]}"

        # Memperbarui teks label untuk status lubang dan toko pemain manusia
        self.player_label["text"] = f"Player 1: {self.game.board[:6]} | {self.game.board[6]}"

    def show_winner(self):
        # Menentukan pemenang berdasarkan jumlah biji di toko pemain
        winner = "Player 1" if self.game.board[6] > self.game.board[13] else "Player 2 (AI)"
        # Menampilkan popup informasi dengan pemenang permainan
        messagebox.showinfo("Game Over", f"The game is over! {winner} wins!")

    def reset_game(self):
        # Mereset permainan dengan membuat objek Congklak baru
        self.game = Congklak()
        # Memperbarui tampilan GUI setelah mereset permainan
        self.update_gui()