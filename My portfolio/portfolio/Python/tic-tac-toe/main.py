class Field:

    def __init__(self, name):
        self.name = name
        self.value = " "

    def go_value(self, symbol_value):
        self.value = symbol_value

    def player_turn(self, symbol):
        if self.value == " ":
            self.value = symbol
            return True
        else:
            return False


class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def player_tur(self, number_field):

        if self.name == 1:
            symbol = 'X'
        else:
            symbol = 'O'
        if not number_field.player_turn(symbol):
            return False
        else:
            return True


class XO:

    def __init__(self):
        self.fields = [Field(index) for index in range(1, 11)]

    def info_board(self):
        print('-------------')
        print('| {} | {} | {} |'.format(self.fields[1].value, self.fields[2].value, self.fields[3].value))
        print('-------------')
        print('| {} | {} | {} |'.format(self.fields[4].value, self.fields[5].value, self.fields[6].value))
        print('-------------')
        print('| {} | {} | {} |'.format(self.fields[7].value, self.fields[8].value, self.fields[9].value))
        print('-------------')

    def end_game(self):
        cells = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        # Есть 8 вариантов выигрышных позиций, они здесь и перебираются. Происходит сравнение значений, к примеру, если
        # поле 1,2,3 имеют одинаковое значение равное либо Х, либо 0, то наступает конец игры.
        # При этом проверяется четвертое условие - поле не  является пустым
        for cell in cells:
            if self.fields[cell[0]].value == self.fields[cell[1]].value == self.fields[cell[2]].value != " ":
                print('Game over')
                return False
        return True


stroke_number = 0
player_1 = Player(1, 'X')
player_2 = Player(2, 'O')
game = XO()
fields_XO = game.fields
print("Номера игровых клеток: ")
print('-------------')
print('| 1 | 2 | 3 |')
print('-------------')
print('| 4 | 5 | 6 |')
print('-------------')
print('| 7 | 8 | 9 |')
print('-------------')
while game.end_game():
    stroke_number += 1
    try:
        if stroke_number > 9:
            print('Ничья. Game over')
            break
        elif stroke_number % 2 != 0:
            print('Ход первого игрока. Введите номер поля для Х: ', end=" ")
            number = int(input())
            if not player_1.player_tur(fields_XO[number]):
                raise ValueError
        elif stroke_number % 2 == 0:
            print('Ход второго игрока. Введите номер поля для О: ', end=' ')
            number = int(input())
            if not player_2.player_tur(fields_XO[number]):
                raise ValueError
    except ValueError:
        print("Эта клетка уже занята")
        stroke_number -= 1
    game.info_board()