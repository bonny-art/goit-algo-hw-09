"""
Модуль для порівняння жадібного алгоритму та алгоритму динамічного програмування
для знаходження оптимальних монетних розрядів, щоб досягти заданої суми.
"""

import timeit
from src.find_coins_greedy import find_coins_greedy
from src.find_min_coins import find_min_coins

# ANSI-коди для кольорового тексту
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

if __name__ == "__main__":
    cases = [
        ([25, 10, 1], 30),
        ([50, 20, 10, 5], 113),
        ([100, 50, 20], 87),
        ([7, 6, 2], 10),
        ([50, 25, 10, 5, 2, 1], 2573)
    ]

    total_greedy_time = 0
    total_dp_time = 0

    for denominations, amount in cases:
        print(f"\nСума:           {BLUE}{amount}{RESET}")
        print(f"Номінали монет: {', '.join(map(str, denominations))}")

        amount_digits = len(str(amount))

        # Жадібний алгоритм
        greedy_time = timeit.timeit(lambda: find_coins_greedy(amount, denominations), number=1)
        total_greedy_time += greedy_time
        greedy_result, greedy_reached_sum = find_coins_greedy(amount, denominations)
        greedy_total_coins = sum(greedy_result.values())
        greedy_color = GREEN if greedy_reached_sum == amount else RED
        print(f"Жадібний алгоритм:       Час: {greedy_time * 1000:.4f} мс, "
              f"Сума: {greedy_color}{str(greedy_reached_sum).rjust(amount_digits)}{RESET}, "
              f"Монет: {greedy_total_coins}, Монети: {greedy_result}")

        # Динамічне програмування
        dp_time = timeit.timeit(lambda: find_min_coins(amount, denominations), number=1)
        total_dp_time += dp_time
        min_coins_result, min_coins_reached_sum = find_min_coins(amount, denominations)
        min_coins_total = sum(min_coins_result.values())
        min_coins_color = GREEN if min_coins_reached_sum == amount else RED
        print(f"Динамічне програмування: Час: {dp_time * 1000:.4f} мс, "
              f"Сума: {min_coins_color}{str(min_coins_reached_sum).rjust(amount_digits)}{RESET}, "
              f"Монет: {min_coins_total}, Монети: {min_coins_result}")

    average_greedy_time = (total_greedy_time / len(cases)) * 1000
    average_dp_time = (total_dp_time / len(cases)) * 1000

    print(f"\nСередній час виконання жадібного алгоритму:       {average_greedy_time:.4f} мс")
    print(f"Середній час виконання динамічного програмування: {average_dp_time:.4f} мс")
