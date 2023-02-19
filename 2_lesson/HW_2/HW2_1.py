# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

n = int(input())
count_one = count_zero = 0

for i in range(n):
    coin = int(input())
    if coin:
        count_one += 1
    else:
        count_zero += 1

if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)

# -------------------- 2 вариант

n = int(input())
count = 0

for i in range(n):
    coin = int(input())
    if coin:
        count += 1

if count > n // 2:
    count = n - count

print(count)
