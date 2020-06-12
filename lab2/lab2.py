import turtle
turtle.shape('turtle')


# Упражнение "Больше квадратов"
'''
import turtle
turtle.shape('turtle')
Length_of_line = 10
Angle = 90
for i in range(10):
	Length_of_line += 5
	turtle.goto (i * -2, i * -2)
	for y in range (4):
		turtle.forward(Length_of_line)
		turtle.left(Angle)
input ('Ай да Я')
'''

# Упражнение "Паук"
'''
import turtle
turtle.shape('turtle')
Length_of_line = 100
Count_Pows = 12
Angle = 360 / Count_Pows
for i in range (Count_Pows):
	turtle.goto(0, 0)
	turtle.left(Angle)
	turtle.forward(Length_of_line)
	turtle.stamp()
input ('Ай да Я')
'''

# Упражнение "Спираль"
'''
import turtle
turtle.shape('turtle')
Length_of_line = 10
Angle = 12
for i in range(150):
	Length_of_line += 0.1
	turtle.forward(Length_of_line)
	turtle.left(Angle)
input ('Ай да Я')
'''

# Упражнение "Правильные N-угольники"
'''
import turtle
turtle.shape('turtle')
def Regular_Polygon (Quant_angle, Length_of_line):
	Angle = 360 / Quant_angle
	for i in range(Quant_angle):
		turtle.left(Angle)
		turtle.forward(Length_of_line)
otstup_x = 0
otstup_y = 0
Length_of_line = 0
for i in range(8):
	Length_of_line += 10
	Regular_Polygon(i+3, Length_of_line)
	otstup_x += 10
	otstup_y -= 10
	turtle.penup()
	turtle.goto (otstup_x, otstup_y)
	turtle.pendown()
input ('Ай да Я')
'''

