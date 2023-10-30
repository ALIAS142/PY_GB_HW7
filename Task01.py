# Задача 34:  Написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Пример:
# Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

# Вариант 1:
poem = "пара-ра-рам рам-пам-папам па-ра-па-да рам-пам-папам"
lines = poem.split('-')

list1 = [sum(x in 'уеыаоэяию' for x in line) for line in lines]

if len(list1) % 2 == 0:
    res = "Парам пам-пам"
else:
    res = "Пам парам"

print(res)



# Вариант 2:
#
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# def rhythm(stroka):
#     stroka = stroka.split()
#     list = []
#     for word in stroka:
#         result = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 result += 1
#         list.append(result)
#     return len(list) == list.count(list[0])
#
# print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
# str = input()
# if rhythm(stroka):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

# Вариант 3:
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = stroka.split()
if len(phrases) < 2:
 print('Количество фраз должно быть больше одной!')
else:
 countVowels = []

 for i in phrases:
  countVowels.append(len([x for x in i if x.lower() in vowels]))

 if countVowels.count(countVowels[0]) == len(countVowels):
  print('Парам пам-пам')
 else:
  print('Пам парам')
