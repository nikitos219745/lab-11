f = open('f.txt', 'r', encoding='utf-8')  #відкриваем файл f
g = open('g.txt', 'r+', encoding='utf-8')  #відкриваем g для записування
for i in f:
    if len(i) > 20:       #використовуем цикл прицьому перевіряєм довжину
        g.write(i)     #якщо умова спрацьовує переписуємо
    else:
        continue
print(g.read())#виводим результат
