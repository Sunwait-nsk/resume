import random


class Number21:

    def __init__(self, name_1, name_2):
        self.player1 = Player(name_1)
        self.player2 = Player(name_2)
        self.deck = Pictures()

    def info(self, count):
        print('Ход {}:\n игрок {} имеет {} очков и игрок {} имеет {} очков'.format(
            count, self.player1.name, self.player1.score, self.player2.name, self.player2.score
        ))

    def move(self):
        if len(self.deck.element) > 0:
            card_1, card_1_score = conversions_card(random.randint(1, 13))
            self.deck.delete_card(card_1)
            card_1_score -= self.card_ace_player_1(card_1)
            card_2, card_2_score = conversions_card(random.randint(1, 13))
            self.deck.delete_card(card_2)
            card_2_score -= self.card_ace_player_1(card_2)
            print("игрок {} получает карты: {} , {}". format(self.player1.name, card_1, card_2))
            card_3, card_3_score = conversions_card(random.randint(1, 13))
            self.deck.delete_card(card_3)
            card_3_score -= self.card_ace_player_2(card_3)
            card_4, card_4_score = conversions_card(random.randint(1, 13))
            self.deck.delete_card(card_4)
            card_4_score -= self.card_ace_player_2(card_4)
            print("игрок {} получает карты: {} , {}".format(self.player2.name, card_3, card_4))
            self.player1.score += card_1_score + card_2_score
            self.player2.score += card_3_score + card_4_score

    def victoria(self):
        victoria_result = ""
        if self.player1.score > 21 and self.player2.score > 21:
            victoria_result = ""
        elif self.player1.score > 21:
            victoria_result = self.player2.name
        elif self.player2.score > 21:
            victoria_result = self.player1.name
        elif self.player1.score == 21 or self.player1.score > self.player2.score:
            victoria_result = self.player1.name
        elif self.player2.score == 21 or self.player2.score > self.player1.score:
            victoria_result = self.player2.name
        print('игру выиграл игрок: ', victoria_result)

    def card_ace_player_1(self, pin):
        result = 0
        if pin == 'T':
            if self.player1.score > 21:
                result = 10
        return result

    def card_ace_player_2(self, pin):
        result = 0
        if pin == 'T':
            if self.player1.score > 21:
                result = 10
        return result


class Pictures:

    def __init__(self):
        self.element = {'2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4, '8': 4, '9': 4, '10': 4, 'V': 4, 'D': 4,
                        'K': 4, 'T': 4}

    def delete_card(self, name):
        if self.element[name] > 0:
            self.element[name] -= 1
        else:
            del self.element[name]


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0


def conversions_card(card):
    if card == 11:
        result = 'V'
        result_score = 10
    elif card == 12:
        result = 'D'
        result_score = 10
    elif card == 13:
        result = 'K'
        result_score = 10
    elif card == 14:
        result = 'T'
        result_score = 11
    else:
        result = str(card)
        result_score = card
    return result, result_score


black_jack = Number21('Юзер', 'Компьютер')
answer = 'да'
while answer == 'да':
    count_move = 1
    black_jack.move()
    black_jack.info(count_move)
    answer = input('Еще один ход? (да/нет) ')
black_jack.victoria()


