def greet():
   print("-------------------")
   print(" Приветвствуем вас ")
   print("     В игре        ")
   print(" Крестики нолики   ")
   print("-------------------")
   print(" Формат ввода: x,y ")
   print(" x - номер строки  ")
   print(" y - номер столбца ")
greet()
field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
def show():
   print()
   print(f"      0 | 1 | 2 | ")
   print("  --------------- ")
   for i, row in enumerate(field):
       row_str = f"  {i} | {' | '.join(row)} | "
       print(row_str)
       print("  --------------- ")
   print()
show()
def ask():
    while True:
        cords = input("      Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Ввидите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапозона ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята ")
            continue

        return x, y

x, y = ask()

def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field [c[0]] [c[1]])
            if symbols == ["X", "X", "X"]:
                print(" Выйграл X! ")
                return True
            if symbols == ["0", "0", "0"]:
                print(" Выйграл 0! ")
                return True
    return False
check_win()

num = 0
while True:

    num += 1

    show()

    if num % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if num == 9:
        print("Ничья")
        break

print(" ---------- ")
input(" Конец игры! ")
















