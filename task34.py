strong_string = ('пара-ра-рам рам-пам-папам па-ра-па-дам').split()
# strong_string = input("Введите ваше произведение искусства: ").lower().split()

vowels = ['а', 'о', 'у', 'э', 'ы', 'я', 'ё', 'е', 'ю', 'и']
answer = ["Парам пам-пам", "Пам парам"]

# сокращенное решение
res = list()
def winnie_the_pooh(strong_string):
    res = [sum(j in vowels for j in i) for i in strong_string]
    return set(res)

if len(winnie_the_pooh(strong_string)) == 1:
     print(answer[0])
else:
     print(answer[1])



# 2 решение
# f = list()
# for i in strong_string:
#     count = 0
#     for j in i:
#         if j in vowels:
#             count += 1

#     f.append(count)

# d = f[0]
# tount = 0

# for i in f:
#     if i == d:
#         tount += 1
# if tount == len(f):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")



# 3 решение
# res = list()
# for i in strong_string:
#     count = 0
#     for j in i:
#         if j in vowels:
#             count += 1
#     res.append(count)
# # print(len(set(res)))
# if len(set(res)) == 1:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')
