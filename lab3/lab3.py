# lab3 Пример1 "Домик"
'''
from graph import *
penColor(255,0,255)
penSize(5)
brushColor("blue")
rectangle(100, 100, 300, 200)
brushColor("yellow")
polygon([(100,100), (200,50),
         (300,100), (100,100)])
penColor("white")
brushColor("green")
circle(200, 150, 50)

run()
'''

# lab3 Пример2 "Забор"
'''
from graph import *

x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
rectangle (x1, y1, x2, y2)
h = (x2 - x1) / (N + 1)
x = x1 + h
for i in range(N):
  line(x, y1, x, y2)
  x += h

run()
'''

# lab3 Задание1 "Злой смайлик"
'''
from graph import *

# Зададим координаты начальной точки
x1 = 300
y1 = 300
r1 = 150 # Радиус лица

# Нарисуем овал лица
brushColor("yellow")
circle (x1, y1, r1)

# Нарисуем рот
k = 0.5
x2 = x1 - r1*k
print (x2)
y2 = y1 + r1*k
brushColor("black")
rectangle (x2, y2, x2+(x1 - x2)*2, y2+r1*0.2)

run()
'''

# lab3 Задание1 "Пустыня"
from graph import *

# Нарисуем первое небо
brushColor("#e3b089"); penColor("#e3b089")
rectangle (0, 0, 500, 150)

# Нарисуем второе небо
brushColor("#e3e389"); penColor("#e3e389")
rectangle (0, 150, 500, 300)

# Нарисуем третье небо
brushColor("#d5f1c7"); penColor("#d5f1c7")
rectangle (0, 300, 500, 450)

# Нарисуем солнышко
brushColor("Yellow"); penColor("Yellow")
circle (250, 150, 50)

# Нарисуем верхнюю гряду
brushColor("#be8c0e"); penColor("#be8c0e")
poly_coord = [(3,300), (480,270), (440,150), 
			  (250,250), (100,100), (20,270), (3,300)]
polygon (poly_coord)

run()