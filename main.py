class Cell:
    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки

    def __init__(self, number, busy = False):
        self.number = number
        self.busy = busy




class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки

    def __init__(self):
        self.board = [Cell(i) for i in range(1, 10)]

    def print_board(self):
        print("-" * 13)
        for i in range(3):
            print("|", self.board[0 + i * 3].number, "|", self.board[1 + i * 3].number, "|", self.board[2 + i * 3].number, "|")
            print("-" * 13)

    def check_win(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.board[each[0]].number == self.board[each[1]].number == self.board[each[2]].number:
                if player_1.symb == self.board[each[0]].number:
                    print(f'Победил {player_1.name}')
                else:
                    print(f'Победил {player_2.name}')
                return True
        return False

    def check_busy(self, number):
        if self.board[number-1].busy:
            return True
        return False


class Player:
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит

    def __init__(self, name, symb, win=False):
        self.name = name
        self.symb = symb
        self.win = win

    def go_cell(self, number, Board):
        Board.board[number-1].busy = True
        Board.board[number-1].number = self.symb

player_1 = Player('Петя', 'X')
player_2 = Player('Володя', 'O')
board = Board()
count = 0
win = False
def play(player, board):
    number = int(input(f'Куда идем, {player.name}?'))
    if board.check_busy(number):
        print('Клетка занята! Попробуйте еще раз!')
        play(player, board)
    else:
        player.go_cell(number, board)

while True:
    if board.check_win():
        break
    else:
        board.print_board()
        play(player_1, board)
        board.print_board()
        play(player_2, board)
