s = str(input("Введите список узлов от корня до последнего узла\n"))
chisla = s.split(",")

for i in range(len(chisla)):
    if len(chisla[i]) > 0:
        if chisla[i].isdigit() or (chisla[i][0] == '-' and chisla[i][1:].isdigit()):
            chisla[i] = int(chisla[i])

if len(chisla) == 0:
    print("Ввод осуществлён неверно. Повторите попытку")
    exit()

for x in chisla:
    if not (isinstance(x, int) or x == ''):
        print("Ввод осуществлён неверно. Повторите попытку")
        exit()

i, k = 0, 1

d = {}
d[str(chisla[0])] = chisla[0]

posledn = [chisla[0]]
extra_keys = list()
k_p = 0


while i != (len(chisla) - 1):
    q = 0
    a = list()
    if (i + 1 + k*2) > len(chisla):
        print("Ввод осуществлён неверно. Повторите попытку")
        exit()
    d1 = {}
    for j in range(i+1, i+1+k*2):
        if isinstance(chisla[j], int):
            a.append(chisla[j])
            q += 1
            for key in d.keys():
                if "->" not in key:
                    if (key == str(posledn[(j - i - 1) // 2])):
                        d1[key + "->" + str(chisla[j])] = d[key] + chisla[j]
                        extra_keys.append(key)
                elif (key[key.rfind('>') + 1:] == str(posledn[(j - i - 1) // 2])) and (key.count('>') == k_p):
                    d1[key + "->" + str(chisla[j])] = d[key] + chisla[j]
                    extra_keys.append(key)
    if len(a) == 0:
        print("Ввод осуществлён неверно. Повторите попытку")
        exit()
    for key1 in d1.keys():
        d[key1] = d1[key1]
    posledn = a
    i += k*2
    k = q
    k_p += 1

summ = int(input("Введите целевую сумму\n"))

print("Результат поиска путей:")
g = 0
for key, value in d.items():
    if (value == summ) and not (key in extra_keys):
        print(key)
        g += 1

if g == 0:
    print("Пути не найдены")
