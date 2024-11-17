import turtle as t
t.setup(640,640)
t.bgcolor('white')
G = 1.618
R = 1
t.speed(10)
t.up()
t.fd(115)
t.rt(90)
t.fd(60)
t.rt(90)
t.down()
for i in range(13):
    t.pensize(1)
    t.color('gray')
    for j in range(4):
        t.fd(R)
        t.lt(90)
    t.pensize(2)
    t.color('black')
    t.circle(R)
    R *= G
    t.done()
