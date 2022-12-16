# Напишите функцию, которая переворачивает строку
#
# def reverse(input_str):
#     out_str=''
#     for i in range(len(input_str)-1,-1,-1):
#         out_str += input_str[i]
#     return out_str
# some_str = input('Введите строку: ')
# print(reverse(some_str))

# Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2] Надо вернуть их пересечение [1, 2, 2, 3](порядок неважен)
#
# a = [1, 2, 3, 2, 0]
# b = [5, 1, 2, 7, 3, 2]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# c.sort()
# print(c)

# Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему добавляется количество повторений
#
# input_str = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
# encoding = ''
# prev_char = ''
# count = 1
# for char in input_str:
#     if char != prev_char:
#         if prev_char and count != 1:
#             encoding += prev_char + str(count)
#         else:
#             encoding += prev_char
#         count = 1
#         prev_char = char
#     else:
#         count += 1
# else:
#     if count == 1:
#         encoding += prev_char
#     else:
#         encoding += prev_char + str(count)
# print(encoding)