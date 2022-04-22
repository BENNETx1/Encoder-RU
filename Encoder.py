# Encoder RU from BENNETx1
# Шифратор RU от BENNETx1
import random as r
print("Введи любое слово а я его зашифрую!")
print("Рaзшифровать этот шифр НЕВОЗМОЖНО так как шифратор основан на рандоме.")
while True:
    Long = int(input('Впиши насколько будет умножена длина шифра(в цифрах)(рекомендованное число - 4 или 5)\n'))
    print(f"Длина шифра будет умножена в {Long} символа.")
    YW = input("Введите слово чтобы его зашифровали.\n")
    print(f"Зашифровываем слово {YW}...")
    a = ''
    b = ''
    c = ''
    d = ''
    e = ''
    f = ''
    g = ''
    u = ''
    for x in range(1):
        a = a + r.choice(list(YW))
        b = b + r.choice(list(YW))
        c = c + r.choice(list(YW))
        d = d + r.choice(list(YW))
        e = e + r.choice(list(YW))
        f = f + r.choice(list(YW))
        g = g + r.choice(list(YW))
        u = u + r.choice(list(YW))
        if a == b or c or d or e or f or g or u:
            a = a + r.choice(list(YW))
        if b == a or c or d or e or f or g or u:
            b = b + r.choice(list(YW))
        if c == b or a or d or e or f or g or u:
            c = c + r.choice(list(YW))
        if d == b or c or a or e or f or g or u:
            d = d + r.choice(list(YW))
        if e == b or c or d or a or f or g or u:
            e = e + r.choice(list(YW))
        if f == b or c or d or e or a or g or u:
            f = f + r.choice(list(YW))
        if g == b or c or d or e or f or a or u:
            a = a + r.choice(list(YW))
        if u == b or c or d or e or f or g or a:
            u = u + r.choice(list(YW))
        abcdefgu = a + b + c + d + e + f + g + u
        shfr = abcdefgu * Long
        print(f"Слово {YW} успешно зашифровано в: {shfr}")
