# Завдання

Маємо набір монет `[50, 25, 10, 5, 2, 1]`. Уявіть, що ви розробляєте систему для касового апарату, яка повинна визначити оптимальний спосіб видачі решти покупцеві.

Вам необхідно написати дві функції для касової системи, яка видає решту покупцеві:

- **Функція жадібного алгоритму `find_coins_greedy`.** Ця функція повинна приймати суму, яку потрібно видати покупцеві, і повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми. Наприклад, для суми `113` це буде словник `{50: 2, 10: 1, 2: 1, 1: 1}`. Алгоритм повинен бути жадібним, тобто спочатку вибирати найбільш доступні номінали монет.
- **Функція динамічного програмування `find_min_coins`.** Ця функція також повинна приймати суму для видачі решти, але використовувати метод динамічного програмування, щоб знайти мінімальну кількість монет, необхідних для формування цієї суми. Функція повинна повертати словник із номіналами монет та їх кількістю для досягнення заданої суми найефективнішим способом. Наприклад, для суми `113` це буде словник `{1: 1, 2: 1, 10: 1, 50: 2}`

Порівняйте ефективність жадібного алгоритму та алгоритму динамічного програмування, базуючись на часі їх виконання або О великому та звертаючи увагу на їхню продуктивність при великих сумах. Висвітліть, як вони справляються з великими сумами та чому один алгоритм може бути більш ефективним за інший у певних ситуаціях. Свої висновки додайте у файл `readme.md` домашнього завдання.