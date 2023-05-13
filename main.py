# Создание пустого игрового поля
board = [' '] * 9

# Функция для отображения игрового поля
def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

# Функция для проверки выигрышных комбинаций
def check_win(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные комбинации
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные комбинации
        [0, 4, 8], [2, 4, 6]  # Диагональные комбинации
    ]
    for combination in win_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

# Функция для проверки ничьей
def check_tie():
    return ' ' not in board

# Основной игровой цикл
def play_game():
    current_player = 'X'

    while True:
        display_board()

        # Ход игрока
        move = input("Ход игрока " + current_player + ". Введите номер ячейки (0-8): ")
        move = int(move)

        if board[move] == ' ':
            board[move] = current_player
        else:
            print("Некорректный ход. Попробуйте снова.")
            continue

        # Проверка условий победы и ничьей
        if check_win(current_player):
            display_board()
            print("Игрок", current_player, "победил!")
            break
        elif check_tie():
            display_board()
            print("Ничья!")
            break

        # Смена игрока
        current_player = 'O' if current_player == 'X' else 'X'

# Запуск игры
play_game()