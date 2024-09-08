from turtle import Screen, Turtle

screen = Screen()
screen.title('Snake Game')
screen.bgcolor('white')

pen = Turtle()
k = 10
pen.dot(k, 'red')
pen.hideturtle()

positons = [(0, 0)] # tracking head's old and new positons

def draw_snake_segment(position, color):
    pen.penup()
    pen.goto(position)
    pen.dot(k, color)

draw_snake_segment(positons[0], 'red')

for i in range(3):
    head_x, head_y = positons[-1] #(0, 0)
    new_head_x = head_x + k

    positons.append((new_head_x, head_y))
    draw_snake_segment((new_head_x, head_y), 'red')

    tail = positons.pop(0) # old head positon
    draw_snake_segment(tail, 'white')

screen.mainloop() # avoid closing automatically