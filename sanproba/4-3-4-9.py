# for i in range(1, 21):
#     print(i)
# # Не забывать указывать максильное значение списка на одно больше, чем нужно, так как последняя цифра не выводится
# billion = list(range(1, 1000001))
# # print(billion)
#
# # for i in billion:
# #         print(i)
#
# print(min(billion))
# print(max(billion))
# print(sum(billion))
#
# # Два варианта вывода списка чисел. Второй варинт с генерацией списка и сохранием списка в переменной.
# for ii in range(1, 21, 2):
#     print(ii)
# kkk = list(range(1, 21, 2))
# for m in kkk:
#     print(m)
#
#
# for iii in range(3, 30, 3):
#     print(iii)
# # Так работать не будет, точнее элементы не сохранятся в списке spis
# spis = [print(mmm) for mmm in list(range(3, 30, 3))]
# print(spis)
# # Так выведет на печать вертикально все цифры
# [print(mmm) for mmm in range(3, 30, 3)]
# # А так выведет горизонтально весь список - spis
# spis = [mmm*2 for mmm in range(3, 30, 3)]
# print(spis)

for ooo in range(1, 10):
    print(ooo**3)

kub = [yy**3 for yy in range(1, 10)]
print(kub)

