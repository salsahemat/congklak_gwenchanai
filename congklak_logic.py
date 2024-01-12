class Congklak:
    def __init__(self):
        # Inisialisasi papan congklak
        self.board = [7] * 16  # Setiap lubang awalnya berisi 7 biji
        self.board[8] = 0  # Lubang untuk pemain 1
        self.board[0] = 0  # Lubang untuk pemain 2

    def is_game_over(self):
        # Permainan berakhir jika semua lubang pemain 1 atau pemain 2 kosong
        return all(count == 0 for count in self.board[:8]) or all(count == 0 for count in self.board[8:15])

    def make_move(self, move, player):
        # Mengambil jumlah biji di lubang yang dipilih
        stones = self.board[move]
        # Menetapkan lubang yang dipilih menjadi kosong
        self.board[move] = 0

        # Inisialisasi indeks untuk pergerakan biji
        index = move
        while stones > 0:
            # Menggerakkan indeks ke lubang berikutnya (dengan siklus pada indeks 16)
            index = (index + 1) % 16
            # Menyebarkan biji ke lubang selain lubang pemain lawan
            if not (player == 1 and index == 0) and not (player == 2 and index == 8):
                self.board[index] += 1
                stones -= 1

        # Mengambil langkah khusus jika biji terakhir jatuh di lubang terakhir pemain
        if player == 1 and 8 <= index <= 15 and self.board[index] == 1:
            opposite_index = 16 - index
            # Mengambil biji di lubang terakhir dan lubang lawan
            self.board[15] += self.board[index] + self.board[opposite_index]
            # Menetapkan lubang terakhir dan lubang lawan menjadi kosong
            self.board[index] = 0
            self.board[opposite_index] = 0
        elif player == 2 and 0 <= index <= 7 and self.board[index] == 1:
            opposite_index = 8 - index
            # Mengambil biji di lubang terakhir dan lubang lawan
            self.board[7] += self.board[index] + self.board[opposite_index]
            # Menetapkan lubang terakhir dan lubang lawan menjadi kosong
            self.board[index] = 0
            self.board[opposite_index] = 0


    def evaluate(self):
        # Skor akhir permainan adalah selisih biji antara pemain 1 dan pemain 2
        score = self.board[8] - self.board[15]
        if score > 0:
            return 1
        elif score < 0:
            return -1
        else:
            return 0

    def chance_moves(self, player):
        # Menentukan kumpulan lubang yang masih berisi biji untuk pemain tertentu
        if player == 1:
            # Mengembalikan indeks lubang untuk pemain 1 yang berisi biji
            return [i for i in range(8) if self.board[i] != 0]
        elif player == 2:
            # Mengembalikan indeks lubang untuk pemain 2 yang berisi biji
            return [i for i in range(8, 15) if self.board[i] != 0]


    def minimax(self, depth, maximizing_player, alpha, beta):
        # Fungsi rekursif Minimax dengan Alpha-Beta Pruning
        if depth == 0 or self.is_game_over():
            # Jika kedalaman mencapai 0 atau permainan berakhir, evaluasi posisi saat ini
            return self.evaluate()

        if maximizing_player:
            max_eval = float('-inf')
            # Inisialisasi evaluasi maksimum dengan nilai negatif tak terhingga
            for move in self.chance_moves(1):
                # Iterasi melalui semua kemungkinan gerakan pemain 1
                new_board = Congklak()
                new_board.board = self.board.copy()
                new_board.make_move(move, 1)
                # Buat papan baru dan lakukan move pemain 1
                eval = new_board.minimax(depth - 1, False, alpha, beta)
                # Rekursi dengan pemanggilan fungsi minimax untuk pemain 2 (minimizing player)
                max_eval = max(max_eval, eval)
                # Update evaluasi maksimum
                alpha = max(alpha, eval)
                # Update alpha
                if beta <= alpha:
                    # Algoritma Alpha-Beta Pruning
                    break
            return max_eval
        else:
            min_eval = float('inf')
            # Inisialisasi evaluasi minimum dengan nilai positif tak terhingga
            for move in self.chance_moves(2):
                # Iterasi melalui semua kemungkinan gerakan pemain 2 (AI)
                new_board = Congklak()
                new_board.board = self.board.copy()
                new_board.make_move(move, 2)
                # Buat papan baru dan lakukan move pemain 2
                eval = new_board.minimax(depth - 1, True, alpha, beta)
                # Rekursi dengan pemanggilan fungsi minimax untuk pemain 1 (maximizing player)
                min_eval = min(min_eval, eval)
                # Update evaluasi minimum
                beta = min(beta, eval)
                # Update beta
                if beta <= alpha:
                    # Algoritma Alpha-Beta Pruning
                    break
            return min_eval

    def find_best_move(self):
        best_val = float('-inf')
        # Inisialisasi evaluasi terbaik dengan nilai negatif tak terhingga
        best_move = -1

        for move in self.chance_moves(2):
            # Iterasi melalui semua kemungkinan gerakan pemain 2 (AI)
            new_board = Congklak()
            new_board.board = self.board.copy()
            new_board.make_move(move, 1)
            # Buat papan baru dan lakukan move pemain 1
            move_val = new_board.minimax(3, False, float('-inf'), float('inf'))
            # Panggil fungsi minimax untuk pemain 2 dengan kedalaman 3 (sesuaikan sesuai kebutuhan)
            if move_val > best_val:
                # Jika evaluasi hasil move lebih baik daripada yang sudah ada
                best_val = move_val
                # Update evaluasi terbaik
                best_move = move
                # Update langkah terbaik
        return best_move

