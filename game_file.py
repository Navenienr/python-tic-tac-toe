'''игра крестики-нолики'''

import os
clear = lambda: os.system('clear')

def print_info():
    print ('''
            добро пожаловать в игру крестики нолики 
    ниже представлены поля для вашего хода в самой игре
                        | 1 | 2 | 3 |
                        -------------
                        | 4 | 5 | 6 |
                        -------------
                        | 7 | 8 | 9 |
    ''')

#генерация игрового поля
def print_field(field):
    for i in range (3):
        print (f"| {field[i *3]} | {field[i *3+1]} | {field[i *3+2]} |")
        if i <2:
            print ("-------------")

def chek_winner(field):
    #првоерка горизонтальных линий
    for i in range(0, 9, 3):
        if field[i] == field[i+1] == field[i+2] != " ":
            return field[i]


    #проверка вертикальных линий
    for i in range(3):
        if field[i] == field[i+3] == field[i+6] != " ":
            return field[i]

    #проверка диагонали
    if field[0] == field[4] == field[8] != " ":
        return field[0]
    if field[2] == field[4] == field[6] != " ":
        return field[2]

    #если нет победителя
    return None

def field_full(field):
    return " " not in field

def main ():

    print_info()

    field = [" "]*9
    current_player = "x"

    while True:

        for i in range (9):
            if field[i] == " ":
                continue
            else:
                clear()
                print_field(field)
                break

        try:
            move = int(input("Введите номер поля для хода (1-9): "))-1
            if 0 <= move <= 9 and field[move] == " ":
                # присвоение хода игрока
                field[move] = current_player

                # проверка условий окончания игры
                winner = chek_winner(field)

                # проверка состояния победителя
                if winner:
                    clear()
                    print_field(field)
                    print(f"игрок {winner} победил")
                    break

                # проверка заполненности поля
                if field_full(field):
                    clear()
                    print_field(field)
                    print("ничья")
                    break

                current_player = "0" if current_player == "x" else "x"

            else:
                print ("введите новое значение ")
        except ValueError:
            print ("пожалуйста введите число от 1 до 9 включительно")


main ()