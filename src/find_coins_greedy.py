"""
Модуль для реалізації жадібного алгоритму знаходження оптимального способу видачі решти.
"""

from typing import List, Dict, Tuple

def find_coins_greedy(amount: int, denominations: List[int]) -> Tuple[Dict[int, int], int]:
    """
    Знаходить оптимальний спосіб видачі решти, використовуючи жадібний алгоритм.
    
    :param amount: Сума, яку потрібно видати (int).
    :param denominations: Список номіналів монет (list of int).
    :return: Кортеж (словник з номіналами монет та їх кількістю (dict), зібрана сума (int)).
    """
    denominations.sort(reverse=True)  # Сортуємо номінали монет у спадному порядку

    result: Dict[int, int] = {}  # Словник для зберігання кількостей монет
    total_collected: int = 0  # Змінна для накопичення зібраної суми

    for coin in denominations:
        if amount >= coin:
            count = amount // coin  # Кількість монет даного номіналу
            amount -= count * coin  # Вираховуємо решту
            result[coin] = count  # Додаємо до результату
            total_collected += count * coin  # Додаємо до зібраної суми

    return result, total_collected
