print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

# Рисуем игровое поле
board = list(range(1,10)) # Список чисел от 1 до 10
# Создаем функцию, чтобы нарисовать игровое поле
def draw_board(board):
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i *3], '|')
        print('-' * 13)

# Создаем функцию для игрока
def take_input(player_token):
# Создаем цикл для проверки корректного ввода пользователем
    valid = False
    while not valid:
        player_answer = input('Куда сходим '  + player_token +  '?')
        try:
            player_answer = int(player_answer)
        except ValueError:
            print('Неправильный ввод. Вы уверены, что ввели число?')
            continue
# В условие проверяем занята ли введенная клетка, если клетка занята будет ошибка.
# Если введено число не в диапозоне от 1 до 10, будет так же ошибка
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in 'XO':
                board[player_answer - 1] = player_token
                valid = True
            else:
                print('Эта клетка уже занята!')
        else:
            print('Неправильный ввод. Введите число от 1 до 9.')

# Проверка выйграл ли игрок
def check_win(board):
# Кортеж состоящий из побеных комбинаций
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
# Цикл производит проверку на победу игрока
    for e in win_coord:
        if board[e[0]] == board[e[1]] == board[e[2]]:
            return board[e[0]]
        return False

# Создаем функцию для проверки кто из игроков выйграл, либо сыгрли в ничью
def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1

        tmp = check_win(board)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)

input('Нажмите Enter для выхода!')


































