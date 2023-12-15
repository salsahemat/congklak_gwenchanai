import copy

class CongklakGame:
    def __init__(self, board=None):
        if board is None:
            self.board = [7] * 14  # Congklak board with 7 stones in each hole
            self.board[6] = 0  # Store for player 1
            self.board[13] = 0  # Store for player 2
        else:
            self.board = board

    def is_game_over(self):
        return all(count == 0 for count in self.board[:6]) or all(count == 0 for count in self.board[7:13])

    def evaluate(self):
        return self.board[6] - self.board[13]

    def legal_moves(self, player):
        if player == 1:
            return [i for i in range(6) if self.board[i] != 0]
        elif player == 2:
            return [i for i in range(7, 13) if self.board[i] != 0]

    def make_move(self, move, player):
        stones = self.board[move]
        self.board[move] = 0

        index = move
        while stones > 0:
            index = (index + 1) % 14
            if not (player == 1 and index == 13) and not (player == 2 and index == 6):
                self.board[index] += 1
                stones -= 1

        if player == 1 and 0 <= index <= 5 and self.board[index] == 1:
            opposite_index = 12 - index
            self.board[6] += self.board[index] + self.board[opposite_index]
            self.board[index] = 0
            self.board[opposite_index] = 0
        elif player == 2 and 7 <= index <= 12 and self.board[index] == 1:
            opposite_index = 12 - index
            self.board[13] += self.board[index] + self.board[opposite_index]
            self.board[index] = 0
            self.board[opposite_index] = 0

    def minimax(self, depth, maximizing_player):
        if depth == 0 or self.is_game_over():
            return self.evaluate()

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.legal_moves(1):
                new_board = copy.deepcopy(self)
                new_board.make_move(move, 1)
                eval = new_board.minimax(depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.legal_moves(2):
                new_board = copy.deepcopy(self)
                new_board.make_move(move, 2)
                eval = new_board.minimax(depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self):
        best_val = float('-inf')
        best_move = -1

        for move in self.legal_moves(1):
            new_board = copy.deepcopy(self)
            new_board.make_move(move, 1)
            move_val = new_board.minimax(3, False)

            if move_val > best_val:
                best_val = move_val
                best_move = move

        return best_move


def print_board(game):
    print(f"Player 2 (AI): {game.board[7:13][::-1]} | {game.board[13]}")
    print(f"Player 1: {game.board[:6]} | {game.board[6]}")
    print("--------------")


def main():
    game = CongklakGame()

    while not game.is_game_over():
        print_board(game)

        player_move = int(input("Player 1's move (choose hole 1-6): ")) - 1
        game.make_move(player_move, 1)

        if game.is_game_over():
            break

        print_board(game)

        print("Player 2 (AI) is thinking...")
        ai_move = game.find_best_move()
        game.make_move(ai_move, 2)

    print_board(game)
    winner = "Player 1" if game.board[6] > game.board[13] else "Player 2 (AI)"
    print(f"The game is over! {winner} wins!")


if __name__ == "__main__":
    main()
