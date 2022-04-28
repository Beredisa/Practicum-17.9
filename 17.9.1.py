a = input("Введите последовательность чисел через пробел : ")
n = int(input("Введите любое число : "))


print("# 1. Преобразуем в строку")

L = a.split(" ")
l = list(map(int,L))
print("Приобразованная строка :" , l)
print("***")


print("# 2. Сортируем строку")

# l = sorted(l) # :)

def merge_sort(l):
    if len(l) < 2:
        return l[:]
    else:
        middle = len(l) // 2
        left = merge_sort(l[:middle])
        right = merge_sort(l[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print("Отсортированная строка :", merge_sort(l))
print("***")


print("# 3. Ищем индексы чисел  до и после")

a = merge_sort(l)

def f_min(n):
    if n<a[0]:
        return "Число не принадлежит заданной последовательности."
    for i, j in enumerate(a):
        if n < j:
            return f"Индекс числа меньше заданного:{i - 1}, больше заданного:{i} "
        elif n == j:
            if n== j == a[0]:
                return f"Индекс числа больше заданного:{i + 1} , число меньше заданного не пренадлежит последовательности."
            elif n == j == a[-1]:
                return f"Индекс числа меньше заданного:{i - 1} , число больше заданного не пренадлежит последовательности."
            else:
                return f"Индекс числа меньше заданного:{i - 1}, больше заданного:{i + 1} "
    else:
        return "Число не принадлежит заданной последовательности."

print("Result: ", f_min(n))

