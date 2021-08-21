# T20.25 Описати клас Decks, який призначений для моделювання великої кількості
# випробувань з роздавання гральних карт. Одна колода карт складається максимум з 52
# карт (по 13 карт 4 мастей). Гідність карт від 2 до 10, а також валет, дама, король, туз.
# Масті – піки, трефа, бубни, черви. У тій чи іншій грі може встановлюватись обмеження
# щодо мінімальної гідності карт (наприклад, починаючи з 7). При одному роздаванні
# карт колода тасується випадковим чином та m гравцям роздають по n карт. Інші карти
# залишаються в колоді. Гравець, якому роздають карти, називається «рукою».
# Зовнішнє представлення карти – це кортеж з двох полів, що є рядками (<гідність>,
# <масть>). Для використання масивів numpy кожну карту у внутрішньому представленні
# можна закодувати цілим числом: гідність – від 2 (2) до 14 (туз), масть – 1, 2, 3, 4
# помножити на 100. Так, наприклад, 9 трефа буде мати код 209. Для отримання масті
# карти k достатньо виконати k // 100, а для отримання гідності достатньо виконати
# k % 100.
# Клас Decks повинен містити методи для перетворення карти з зовнішнього
# представлення у внутрішнє та навпаки, метод роздавання карт, метод «фіксованого»
# роздавання та, можливо, інші методи. Метод роздавання карт повинен повертати
# тривимірний масив з N випадковим чином розданих колод (m гравцям по n карт всього
# m*n*N) а також двовимірний масив – залишків N колод. Метод фіксованого роздавання
# повинен фіксувати карти на першій руці та випадковим чином роздавати їх на всі інші
# руки.
# Застосувати клас Decks для розв’язання задачі: 4 гравцям роздають по 5 карт.
# Обчислити ймовірність того, що на будь-якій руці опиняться:
# (Варіант 6) а) 4 карти однакової гідності.

import numpy as np

CODES_POWER = dict((str(i),i) for i in range(2, 10+1))
CODES_POWER.update({"Валет": 11, "Королева": 12, "Король": 13, "Туз": 14})

CODES_SUIT = {
    "Піка": 1,
    "Трефа": 2,
    "Бубна": 3,
    "Черва": 4
}


def encode_one_unit(card_external):
    """
    :param card_external: external card - (SUIT : str, POWER : str)
    :return: encoded card ...
    """
    return 100 * CODES_SUIT[card_external[0]] + CODES_POWER[card_external[1]]


encode_cards = np.vectorize(encode_one_unit)


class Decks:

    def __init__(self):
        ...

    @staticmethod
    def encode(deck_external):
        return encode_cards(deck_external)

    def decode(self, deck_internal):
        return ()