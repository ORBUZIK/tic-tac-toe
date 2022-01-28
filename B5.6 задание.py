field = [[' ']*4 for i in range(4)]

player = 'x'
cross_count = 0
ending = 1

#стилизация матрицы
for i in range(4):
    for j in range(4):
        if i == 0:
            field[i][j] = j-1
        elif j == 0:
            field[i][j] = i-1
        field[0][0] = ' '






#функция хода
def step():
    global player
    global cross_count

    y, x = map(int, input('Введите строку и столбец: ').split())
    print('\n')
    if player == 'x':
        field[y+1][x+1] = 'x'
        player = 'o'
        cross_count += 1
    else:
        field[y+1][x+1] = 'o'
        player = 'x'


# проверка выигрыша
def win_check(player):
    for i in range(3):
        check_line(field[i+1][1], field[i+1][2], field[i+1][3], player)
        check_line(field[1][i+1], field[2][i+1], field[3][i+1], player)
    check_line(field[1][1], field[2][2], field[3][3], player)
    check_line(field[3][1], field[2][2], field[1][3], player)

def check_line(a, b, c, sym):
    global ending

    if all([a == sym, b == sym, c == sym]):
        #печать матрицы
        for i in field:
            print(*i)
        print('\n')
        print(f'{sym} выйграли!')
        ending = 0


# проверка ничьи
def draw_check(col):
    global ending

    if col == 5:
        print('Ничья :(')
        ending = 0



# все вместе
def main():
    global player
    global cross_count
    global ending

    while ending == 1:
        #печать матрицы
        for i in field:
            print(*i)
        print('\n')

        step()

        win_check(player)

        draw_check(cross_count)


main()