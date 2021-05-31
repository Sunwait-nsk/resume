import random


class Warrior:

    def __init__(self, name):
        self.name = name
        self.health = 100

    def info(self):
        print('Воин {} имеет {} очков здоровья'.format(self.name, self.health))


class War:

    def __init__(self):
        self.warrior_1 = Warrior(1)
        self.warrior_2 = Warrior(2)

    def to_go(self):
        first_place = random.randint(1, 2)
        if first_place == 1:
            print('Воин с именем {} наносит удар'.format(self.warrior_1.name))
            self.warrior_2.health -= 20
        else:
            print('Воин с именем {} наносит удар'.format(self.warrior_2.name))
            self.warrior_1.health -= 20

    def info(self):
        self.warrior_1.info()
        self.warrior_2.info()

    def victoria(self):
        if self.warrior_1.health <= 0:
            print('Победу одержал воин с именем {}'.format(self.warrior_2.name))
            return True
        elif self.warrior_2.health <= 0:
            print('Победу одержал воин с именем {}'.format(self.warrior_1.name))
            return True
        return False


battle = War()
print('Битва начинается')
battle.info()
count = 0
while not battle.victoria():
    count += 1
    print('\nРаунд {} \n*****************'.format(count))
    battle.to_go()
    battle.info()



