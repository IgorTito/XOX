x = "x"
o = "0"
num = 9
empty = " "
draw = "ничья"


# приветсвие
def field():
    print(
        """
        Добро пожаловать в игру 'Крестики-нолики'
        игровое поле выглядит следующиим образом
        
        0 | 1 | 2
        3 | 4 | 5
        6 | 7 | 8
        
        цифра соответствует полложению крестика или нолика
        
        """
    )


# функция вопроса
def start(question):
    answer = ""

    while answer not in ("да", "нет"):
        answer = input(question).lower()
    return answer


# кто начинает первым
def first_move():
    move = start("Если хотите начать первым, введите 'Да' или 'Нет', чтобы начал компьютер: ")

    if move == "да":
        print("Вы начинаете!")
        chel = x
        comp = o
    elif move == "нет":
        print("Начинает комьютер")
        chel = o
        comp = x
    return chel, comp


# ввод цифры
def add_number(question, low, high):
    answer = None
    while answer not in range(low, high):
        answer = int(input(question))
    return answer


# вывод игрового поля
def game(board):
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])


def empty_board():
    board = []
    for cell in range(num):
        board.append(empty)
    return board


def moves(board):
    move = []
    for cell in range(num):
        if board[cell] == empty:
            move.append(cell)
    return move


# выигрышные секторы
def win(board):
    win_moves = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for step in win_moves:
        if board[step[0]] == board[step[1]] == board[step[2]] != empty:
            winner = board[step[0]]
            return winner
    if empty not in board:
        return draw


# ход игрока
def chel_move(board, chel):
    field = moves(board)
    move = None
    while move not in field:
        move = add_number("Ваш ход, выберите одно из полей - ", 0, num)
        if move not in field:
            print("Это кклетка уже занята! Выбериет другую")
    return move


# стратегия компьютера / сделать копию списка/ перебор из лучших вариантов/
def comp_move(board, comp, chel):
    board = board[:]
    best = (4, 0, 6, 8, 2, 1, 7, 3, 5)
    print("Компьютер выбрал позицию -", end=" ")
    for move in moves(board):
        board[move] = comp
        if win(board) == comp:
            print(move)
            return move
        board[move] = empty
    for move in moves(board):
        board[move] = chel
        if win(board) == chel:
            print(move)
            return move
        board[move] = empty
    for move in best:
        if move in moves(board):
            print(move)
            return move


def next_step(step):
    if step == x:
        return o
    else:
        return x


# определение победителя

def result(winner, comp, chel):
    if winner == comp:
        print("Выиграл компьютер")
    elif winner == chel:
        print("Вы выиграли!")
    else:
        print("Ничья")


def main():
    field()
    chel, comp = first_move()

    board = empty_board()
    game(board)
    step = x
    while not win(board):
        if step == chel:
            move = chel_move(board, chel)
            board[move] = chel
        else:
            move = comp_move(board, comp, chel)
            board[move] = comp
        game(board)
        step = next_step(step)
    winner = win(board)
    result(winner, comp, chel)


main()
