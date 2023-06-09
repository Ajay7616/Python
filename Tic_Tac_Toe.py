from tkinter import *
import numpy as np

board_width_height = 400
symbol_size = (board_width_height / 3 - board_width_height / 8) /2
X_symbol = '#EE4035'
O_symbol = '#0492CF'
green_color = '#03AC31'

class Tic_Tac_Toe():
    def __init__(self):
        self.window= Tk()
        self.window.title('Tic-Tac-Toe')
        self.box = Canvas(self.window, width=board_width_height, height=board_width_height)
        self.box.pack()

        self.window.bind('<Button-1>', self.click)

        self.board_initialize()
        self.X_turns = True
        self.game_status = np.zeros(shape=(3,3))

        self.X_starts = True
        self.game_reset = False
        self.game_over = False
        self.game_tie = False
        self.X_wins = False
        self.O_wins= False

        self.X_score=0
        self.O_score=0
        self.tie_score=0

    def mainloop(self):
        self.window.mainloop()

    def board_initialize(self):
        for i in range(2):
            self.box.create_line((i + 1) * board_width_height / 3, 0, (i+1) * board_width_height /  3,  board_width_height)

        for i in range(2):
            self.box.create_line(0, (i + 1) * board_width_height / 3, board_width_height, (i + 1) * board_width_height / 3)

    def play_again(self):
        self.board_initialize()
        self.X_starts = not self.X_starts
        self.X_turns = self.X_starts
        self.game_status = np.zeros(shape=(3,3))

    def draw_O(self, logical_position):
        logical_position = np.array(logical_position)
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.box.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                         grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=10,
                                         outline=O_symbol)

    def draw_X(self, logical_position):
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.box.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                         grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=5,
                                         fill=X_symbol)
        self.box.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                         grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=5,
                                         fill=X_symbol)

    def  display_gameover(self):
        if self.X_wins:
            self.X_score += 1
            text = 'Winner: Player 1'
            color = X_symbol
        elif self.O_wins:
            self.O_score += 1
            text = 'Winner: Player 2'
            color = O_symbol
        else:
            self.tie_score += 1
            text = 'Game has  tie'
            color = 'gray'

        self.box.delete("all")
        self.box.create_text(board_width_height / 2, board_width_height / 4, font="times 30 bold", fill=color, text=text)

        score_text = 'Score \n'
        self.box.create_text(board_width_height / 2, 4 * board_width_height / 8, font="arial 20 bold", fill=green_color, text=score_text)

        score_text = 'Player 1: ' + str(self.X_score) + '\n'
        score_text += 'Player 2: ' + str(self.O_score) + '\n'
        score_text += 'Tie: ' + str(self.tie_score)
        self.box.create_text(board_width_height / 2, 2.5* board_width_height / 4, font="arial 20 bold", fill=green_color, text=score_text)
        self.game_reset = True

        score_text = 'Click to play again \n'
        self.box.create_text(board_width_height / 2, 15 * board_width_height / 16, font="calibari 20", fill='gray', text = score_text)

    def convert_logical_to_grid_position(self, logical_position):
        logical_position = np.array(logical_position, dtype=int)
        return (board_width_height / 3) * logical_position + board_width_height / 6

    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (board_width_height / 3), dtype=int)

    def is_grid_occupied(self, logical_position):
        if self.game_status[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True

    def winner(self, player):
        player = -1 if player == 'X' else 1
        for i in range(3):
            if self.game_status[i][0] == self.game_status[i][1] == self.game_status[i][2] == player:
                return True
            if self.game_status[0][i] == self.game_status[1][i] == self.game_status[2][i] == player:
                return True
        if self.game_status[0][0] == self.game_status[1][1] == self.game_status[2][2] == player:
                return True
        if self.game_status[0][2] == self.game_status[1][1] == self.game_status[2][0] == player:
                return True
        return False

    def is_tie(self):
        r,c = np.where(self.game_status == 0)
        tie = False
        if len(r) == 0:
            tie = True
        return tie

    def gameover(self):
        self.X_wins = self.winner('X')
        if not self.X_wins:
            self.O_wins = self.winner('O')
        if not self.O_wins:
            self.tie = self.is_tie()
        game_over = self.X_wins or self.O_wins or self.tie
        if self.X_wins:
            print('X wins')
        if self.O_wins:
            print('O wins')
        if self.tie:
            print('Its a tie')
        return game_over

    def click(self, event):
        grid_position = [event.x, event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)

        if not self.game_reset:
            if self.X_turns:
                if not self.is_grid_occupied(logical_position):
                    self.draw_X(logical_position)
                    self.game_status[logical_position[0]][logical_position[1]] = -1
                    self.X_turns = not self.X_turns
            else:
                if not self.is_grid_occupied(logical_position):
                    self.draw_O(logical_position)
                    self.game_status[logical_position[0]][logical_position[1]] = 1
                    self.X_turns = not self.X_turns

            if self.gameover():
                self.display_gameover()
        else:
            self.box.delete("all")
            self.play_again()
            self.game_reset = False

game_instance = Tic_Tac_Toe()
game_instance.mainloop()
