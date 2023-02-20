strong_string = ('пара-ра-рам рам-пам-папам па-ра-па-дам').split()

x = len(strong_string)

f = list()
for i in strong_string:
    count = 0
    for j in i:
        if j == 'а':
            count += 1
    # print(count)
    f.append(count)
print(f)

d = f[0]
tount = 0

for i in f:
    if i == d:
        tount += 1
if tount == len(f):
    print("same")
else:
    print("none")


    
fount = 0
def winnie_the_pooh(strong_string):
    
    list_count_string = [(j) for i in strong_string for j in i if j == "а"]
    list_count = [fount + 1 for i in list_count_string]
    return j, list_count

print(winnie_the_pooh(strong_string))






strong_string = ('пара-ра-рам рам-пам-папам па-ра-па-дам').split()
# strong_string = input("Введите ваше произведение искусства: ").lower().split()
vowels = ['а', 'о', 'у', 'э', 'ы', 'я', 'ё', 'е', 'ю', 'и']
answer = ["Парам пам-пам", "Пам парам"]
# сокращенное решение
fes = list()
def winnie_the_pooh(strong_string):
    fes = [sum(j in vowels for j in i) for i in strong_string]
    return set(fes)

if len(winnie_the_pooh(strong_string)) == 1:
     print('Парам пам-пам')
else:
     print("Пам парам")



# простое решение
# f = list()
# for i in strong_string:
#     count = 0
#     for j in i:
#         if j == 'а':
#             count += 1
#     # print(count)
#     f.append(count)
# print(f)

# d = f[0]
# count_2 = 0

# for i in f:
#     if i == d:
#         count_2 += 1
# if count_2 == len(f):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

# strong_string = input("Введите ваше произведение искусства: ").lower().split() # пара-ра-рам рам-пам-папам па-ра-па-дам

# res = list()
# for i in strong_string:
#     count = 0
#     for j in i:
#         if j in vowels:
#             count += 1
#     res.append(count)
# print(len(set(res)))
# if len(set(res)) == 1:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')