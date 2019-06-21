# © pythonicway.com/python-games/python-textgames/15-python-black-jack
from random import shuffle


class Card:
    """
    Каждая карта будет обладать рангом и мастью,
    а так же методами получения числа очков,
    получения ранга карты и перегруженного метода __str__
    для простоты отображения карты в консоли.
    """

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        """ Возращает количество очков которое дает карта
            return 10 for 10, Jack, Queen, King
        """
        if self.rank in 'TJQK':
            return 10
        else:
            # Возвращает нужное число очков за любую другую карту
            # Туз изначально дает одно очко.
            return " A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Hand:
    """ Изначально рука у нас пустая, но при необходимости
        мы добавим в нее нужное количество карт.
        Тут будут метод добавления карты,
        метод подсчета очков на руке и перегруженный метод __str__.
    """

    def __init__(self, name):
        self.name = name
        # Изначально рука пустая
        self.cards = list()

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        """Получаем число очков на руке"""
        result = 0
        aces = 0
        for card in self.cards:
            result += card.card_value()
            # Если на руке есть туз - увеличиваем количество тузов
            if card.get_rank() == 'A':
                aces += 1
        # Решаем считать тузы за 1 очко или за 11
        if result + aces * 10 <= 21:
            result += aces * 10
        return result

    def __str__(self):
        text = f"{self.name}'s contains:\n"
        for card in self.cards:
            text += f"{str(card)} "
        text += f"\nHand value: {str(self.get_value())}"
        return text


class Deck:
    def __init__(self):
        # ранги
        ranks = "23456789TJQKA"
        # масти
        suits = "DCHS"
        # генератор списков создающий колоду из 52 карт
        self.cards = [Card(r, s) for r in ranks for s in suits]
        # перетасовываем колоду.
        shuffle(self.cards)

    def deal_card(self):
        """ Функция сдачи карты """
        return self.cards.pop()


def main():
    # создаем колоду
    d = Deck()
    # задаем "руки" для игрока и дилера
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    # сдаем две карты игроку
    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())
    # сдаем одну карту дилеру
    dealer_hand.add_card(d.deal_card())
    print(dealer_hand)
    print("="*20)
    print(player_hand)
    # Флаг проверки необходимости продолжать игру
    in_game = True
    # набирать карты игроку имеет смысл только если у него на руке меньше 21 очка
    while player_hand.get_value() < 21:
        ans = input("Hit or stand? (h/s) ")
        if ans == "h":
            player_hand.add_card(d.deal_card())
            print(player_hand)
            # Если у игрока перебор - дилеру нет смысла набирать карты
            if player_hand.get_value() > 21:
                print("You lose")
                in_game = False
        else:
            print("You stand!")
            break
    print("=" * 20)
    if in_game:
        # По правилам дилер обязан набирать карты пока его счет меньше 17
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(d.deal_card())
            print(dealer_hand)
            # Если у дилера перебор играть дальше нет смысла - игрок выиграл
            if dealer_hand.get_value() > 21:
                print("Dealer bust")
                in_game = False
    if in_game:
        # Ни у кого не было перебора - сравниваем количество очков у игрока и дилера.
        # В нашей версии если у дилера и игрока равное количество очков - выигрывает казино
        if player_hand.get_value() > dealer_hand.get_value():
            print("You win")
        else:
            print("Dealer win")


if __name__ == "__main__":
    main()
