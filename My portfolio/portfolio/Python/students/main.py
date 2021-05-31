import random


class Student:

    def __init__(self, name, group):
        self.name = name
        self.number_group = group
        self.ratings = [random.randint(1, 5) for _ in range(5)]
        self.average_score = self.score()

    def score(self):
        sum_score = 0
        for count in self.ratings:
            sum_score += count
        return sum_score/5

    def info(self):
        print('Студент: {} Группа {} Оценки {} Средний бал {}'.format(
            self.name, self.number_group, self.ratings, self.average_score))


class Group:

    def __init__(self, name, count):
        self.name = name
        self.group = [Student(name_new(), self.name) for _ in range(count)]

    def info(self):
        # TODO стараемся избавлять по всему модулю от приставки i_
        for student in self.group:
            student.info()

    def output_sorted(self):
        plenty_score = {}
        plenty_score_1 = []
        for student in self.group:
            plenty_score[student.average_score] = student.name
            plenty_score_1.append(student.average_score)
        plenty_score_1.sort()
        for score in plenty_score_1:
            print('Студент {} имеет средний балл = {}'.format(plenty_score[score], score))


def name_new():
    name = ['А', 'И', 'Е', 'П', 'В', 'Г', 'Д', 'Б', 'У', 'К']
    surname = [
        'Иванов', 'Петров', 'Васечкин', 'Тасечкин', 'Ушкин', 'Брюшкин', 'Светлова', 'Позднева', 'Тойкичева', 'Сойкина']
    new_name = random.choice(surname) + ' ' + random.choice(name)
    return new_name


people = Group('a12', 10)
people.info()
people.output_sorted()


