from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)


my_turtle.color("pink")
my_turtle.circle(50)
my_turtle.up()
my_turtle.goto(-15, 55)
my_turtle.down()
my_turtle.circle(10)
my_turtle.up()
my_turtle.goto(15, 55)
my_turtle.down()
my_turtle.circle(10)
my_turtle.up()
my_turtle.goto(0, 0)
my_turtle.down()
my_turtle.circle(100)
my_turtle.up()
my_turtle.goto(-40, 110)
my_turtle.down()
my_turtle.setheading(270)
my_turtle.circle(20, -180)
my_turtle.setheading(270)
my_turtle.circle(20, -180)
my_turtle.up()
my_turtle.goto(-80, 160)
my_turtle.down()
my_turtle.setheading(-40)
my_turtle.circle(50, -90)
my_turtle.setheading(-160)
my_turtle.circle(55, -90)
my_turtle.up()
my_turtle.goto(80, 160)
my_turtle.down()
my_turtle.setheading(-150)
my_turtle.circle(-50, -90)
my_turtle.setheading(-20)
my_turtle.circle(-55, -90)



# # Нарисовать квадрат
# def draw_rect(t):
#     for x in range(0, 4):
#         t.right(90)
#         t.forward(100)

# # Рисует квадраты в цикле
# for x in range(0, 360):
#     draw_rect(my_turtle)
#     my_turtle.right(1)

# Необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()