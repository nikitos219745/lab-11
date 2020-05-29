f = open('f.txt', 'r', encoding='utf-8')    #відкриваем файл f
g = open('g.txt', 'r+', encoding='utf-8')   #відкриваем g для записування

for lines in f:          #користуємся циклом і методом lower для заміни букв
    g.write(lines.lower())  

print(g.read())         #виводим результат
