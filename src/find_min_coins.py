"""
Модуль для знаходження мінімальної кількості монет для досягнення заданої суми.

Функція `find_min_coins` реалізує алгоритм динамічного програмування для вирішення задачі про монети,
забезпечуючи оптимальний розрахунок монет, які використовуються для досягнення заданої суми.
"""

from typing import Dict, Tuple

def find_min_coins(amount: int, denominations: list) -> Tuple[Dict[int, int], int]:
    """
    Знаходить мінімальну кількість монет для досягнення заданої суми.

    :param amount: Цільова сума, яку потрібно досягти.
    :param denominations: Список доступних номіналів монет.
    :return: Кортеж, що містить словник з номіналами монет і їх кількістю,
             а також максимальну досяжну суму.
    """
    denominations.sort()
    dp = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in denominations:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[amount] == float('inf'):
        max_reachable = amount
        while max_reachable > 0 and dp[max_reachable] == float('inf'):
            max_reachable -= 1
    else:
        max_reachable = amount

    if max_reachable == 0:
        return {}, 0

    coins_count = {}
    current_amount = max_reachable

    while current_amount > 0:
        coin = coin_used[current_amount]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        current_amount -= coin

    coins_count_ordered = {coin: coins_count[coin] for coin in sorted(coins_count.keys(), reverse=True)}
    return coins_count_ordered, max_reachable
