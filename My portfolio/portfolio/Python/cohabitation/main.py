import random


class Men:

    def __init__(self, name):
        self.name = name
        self. satiety = 50
        self.money = 0

    def info(self):
        if self.satiety >= 40:
            satiety = 'не голоден'
        elif self.satiety > 0:
            satiety = 'голоден'
        else:
            satiety = 'умер'
        print(
            'Человек по имени {} - {} ({}) и имеет денег {}'.format(
                self.name, satiety, self.satiety, self.money))

    def work(self):
        self.money += 50
        self.satiety -= 40
        print('Ход: работать.')
        print(
            'Человек {} заработал 50 единиц и общее количество денег теперь равно {} '.format(
                self.name, self.money))

    def to_eat(self, house):
        print('Ход: поесть.')
        if house.eat > 0:
            self.satiety += 50
            house.eat -= 50
            print('Человек {} съел 50 единиц '.format(self.name))

    def play_men(self):
        self.satiety -= 20
        print('Ход: поиграть.')
        print('Человек {} потерял 20 единиц сытости'.format(self.name))

    def check_satiety(self, house):
        print('Ход: поесть если голоден.')
        if self.satiety < 20:
            self.satiety = 50
            house.eat -= 50
            print('Человек {} съел 50 единиц '.format(self.name))

    def check_house_eat(self, house):
        print('Ход: сходить в магазин если мало еды.')
        if house.eat < 10:
            if self.money > 0:
                self.money -= 50
                house.eat += 50
                print('Человек {} пополнил запасы еды на 50 единиц '.format(self.name))

    def check_house_money(self, house):
        print('Ход: работать если мало денег.')
        if house.money < 50:
            print('Человек {} пошел на работу'.format(self.name))
            self.work()


class House:

    def __init__(self, count):
      
        self.mens = [Men(i_count) for i_count in range(count)]
        self.eat = 50
        self.money = 0

    def house_money(self):
        self.money = 0
        for men in self.mens:
            self.money += men.money

    def info(self):
        print('В доме проживает {} человек/а. В доме есть :  '.format(len(self.mens)))
        print('Деньги: {}\nЕда: {}'.format(self.money, self.eat))
        for men in self.mens:
            men.info()

    def hunger(self):
        for men in self.mens:
            if men.satiety <= 0:
                print('Человек {} умер'.format(men.name))
                self.mens.remove(men)

   
    def step(self):
        # 1- работать, 2 поесть, 3 поесть если есть голод
        # 4 если мало еды - сходить в магазин
        # 5 работать если мало денег 6 играть
        for men in self.mens:
            motion = random.randint(1, 6)
            if motion == 1:
                men.work()
            elif motion == 2:
                men.to_eat(house_1)
            elif motion == 6:
                men.play_men()
            elif motion == 3:
                men.check_satiety(house_1)
            elif motion == 4:
                men.check_house_eat(house_1)
            elif motion == 5:
                men.check_house_money(house_1)
            self.house_money()


house_1 = House(2)
house_1.info()
print('Начинаем проживать год')
day = 0
while len(house_1.mens) > 0:
    day += 1
    print('***************\nДень {}\n'.format(day))
    # розыгрываем действия
    house_1.step()
    house_1.hunger()
    house_1.info()
