class Congklak:
    def __init__(self):
        # Inisialisasi papan congklak
        self.board = [7] * 16  # Setiap lubang awalnya berisi 7 biji
        self.board[7] = 0  # Lubang untuk pemain 1
        self.board[14] = 0  # Lubang untuk pemain 2

    def is_game_over(self):
        # Permainan berakhir jika semua lubang pemain 1 atau pemain 2 kosong
        return all(count == 0 for count in self.board[:6]) or all(count == 0 for count in self.board[7:13])

    def make_move(self, move, player):
        # Mengambil jumlah biji di lubang yang dipilih
        stones = self.board[move]
        # Menetapkan lubang yang dipilih menjadi kosong
        self.board[move] = 0

        # Inisialisasi indeks untuk pergerakan biji
        index = move
        while stones > 0:
            # Menggerakkan indeks ke lubang berikutnya (dengan siklus pada indeks 14)
            index = (index + 1) % 14
            # Menyebarkan biji ke lubang selain lubang pemain lawan
            if not (player == 1 and index == 13) and not (player == 2 and index == 6):
                self.board[index] += 1
                stones -= 1

        # Mengambil langkah khusus jika biji terakhir jatuh di lubang terakhir pemain
        if player == 1 and 0 <= index <= 5 and self.board[index] == 1:
            opposite_index = 12 - index
            # Mengambil biji di lubang terakhir dan lubang lawan
            self.board[6] += self.board[index] + self.board[opposite_index]
            # Menetapkan lubang terakhir dan lubang lawan menjadi kosong
            self.board[index] = 0
            self.board[opposite_index] = 0
        elif player == 2 and 7 <= index <= 12 and self.board[index] == 1:
            opposite_index = 12 - index
            # Mengambil biji di lubang terakhir dan lubang lawan
            self.board[13] += self.board[index] + self.board[opposite_index]
            # Menetapkan lubang terakhir dan lubang lawan menjadi kosong
            self.board[index] = 0
            self.board[opposite_index] = 0


    def evaluate(self):
        # Skor akhir permainan adalah selisih biji antara pemain 1 dan pemain 2
        return self.board[6] - self.board[13]

    def chance_moves(self, player):
        # Menentukan kumpulan lubang yang masih berisi biji untuk pemain tertentu
        if player == 1:
            # Mengembalikan indeks lubang untuk pemain 1 yang berisi biji
            return [i for i in range(6) if self.board[i] != 0]
        elif player == 2:
            # Mengembalikan indeks lubang untuk pemain 2 yang berisi biji
            return [i for i in range(7, 13) if self.board[i] != 0]


    def find_best_move(self):
        # Algoritma Minimax sederhana dengan pencarian kedalaman tetap
        best_val = float('-inf')  # Inisialisasi nilai terbaik dengan nilai minus tak hingga
        best_move = -1  # Inisialisasi langkah terbaik dengan nilai -1

        for move in self.chance_moves(2):
            # Membuat papan baru untuk setiap langkah dan menyalin nilai papan saat ini
            new_board = Congklak()
            new_board.board = self.board.copy()
            # Melakukan langkah pada papan baru
            new_board.make_move(move, 1)
            # Mencari nilai Minimax pada kedalaman 3 untuk langkah saat ini
            move_val = new_board.minimax(3, False)

            # Memperbarui langkah terbaik jika nilai langkah saat ini lebih tinggi dari nilai terbaik sejauh ini
            if move_val > best_val:
                best_val = move_val
                best_move = move

        # Mengembalikan langkah terbaik yang ditemukan
        return best_move

    def minimax(self, depth, maximizing_player):
        # Fungsi rekursif Minimax untuk mengevaluasi langkah terbaik pada kedalaman tertentu
        if depth == 0 or self.is_game_over():
            # Mengembalikan nilai evaluasi jika mencapai kedalaman 0 atau permainan berakhir
            return self.evaluate()

        if maximizing_player:
            # Jika giliran pemain 1 (maksimalkan), cari nilai maksimum
            max_eval = float('-inf')  # Inisialisasi nilai maksimum dengan nilai minus tak hingga
            for move in self.chance_moves(1):
                # Membuat papan baru untuk setiap langkah dan menyalin nilai papan saat ini
                new_board = Congklak()
                new_board.board = self.board.copy()
                # Melakukan langkah pada papan baru
                new_board.make_move(move, 1)
                # Rekursif untuk mencari nilai Minimax pada kedalaman yang lebih rendah
                eval = new_board.minimax(depth - 1, False)
                # Memperbarui nilai maksimum jika nilai langkah saat ini lebih tinggi dari nilai maksimum sejauh ini
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            # Jika giliran pemain 2 (minimalkan), cari nilai minimum
            min_eval = float('inf')  # Inisialisasi nilai minimum dengan nilai tak hingga
            for move in self.chance_moves(2):
                # Membuat papan baru untuk setiap langkah dan menyalin nilai papan saat ini
                new_board = Congklak()
                new_board.board = self.board.copy()
                # Melakukan langkah pada papan baru
                new_board.make_move(move, 2)
                # Rekursif untuk mencari nilai Minimax pada kedalaman yang lebih rendah
                eval = new_board.minimax(depth - 1, True)
                # Memperbarui nilai minimum jika nilai langkah saat ini lebih rendah dari nilai minimum sejauh ini
                min_eval = min(min_eval, eval)
            return min_eval
