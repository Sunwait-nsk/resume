class Potato:
    stage_potato = ['семя', 'росток', 'зреет', 'созрела']

    def __init__(self, name):
        self.name = name
        self.stage = 'семя'

    def info(self):
        print('Картофель {} находится на стадии {}'.format(self.name, self.stage))

    def grow(self):
        self.stage = self.stage_potato[self.stage_potato.index(self.stage) + 1]


class Garden:

    def __init__(self, count):
        self.name = 'Potato'
        self.potatoes = [Potato(i_count) for i_count in range(1, count + 1)]

    def info(self):

        for potato in self.potatoes:
            potato.info()

    def grow_all(self):
        for potato in self.potatoes:
            potato.grow()

    def harvest_all(self):
        count = len(self.potatoes)
        for potato in self.potatoes:
            if potato.stage == 'созрела':
                potato.stage = 'семя'
        return count


class Gardener:

    def __init__(self):
        self.name = "Садовник"
        self.bed = Garden(5)
        self.harvest = 0

    def info(self):
        print('*****************\nСадовник {} ухаживает за грядкой {}. Количество урожая {}'.format(
            self.name, self.bed.name, self.harvest))
        self.bed.info()

    def care_garden(self):
        for _ in range(3):
            self.bed.grow_all()
            self.info()

    def clean_potato(self):
        self.harvest = self.bed.harvest_all()


potato_garden = Gardener()
potato_garden.info()
potato_garden.care_garden()
potato_garden.clean_potato()
potato_garden.info()
