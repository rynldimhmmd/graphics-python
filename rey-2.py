from turtle import*
import colorsys
hideturtle ()
speed ('fastest')
bgcolor('black')
width(2)
h=0.0
for i in range (50):
    col = colorsys.hsv_to_rgb(h, 1, 1)
    color(col)
    for j in range(10):
        circle(i * 2)
        right(36)
    h+=0.1
done()