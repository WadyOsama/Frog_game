first
if (x[5][0] + rect1.right) >= 1200:
    x[5][0] = -200
elif (x[5][1] + rect2.right) >= 1200:
    x[5][1] = -600
elif (x[5][2] + rect3.right) >= 1200:
    x[5][2] = -1000
x[5][0] = x[5][0] + speed[2]
x[5][1] = x[5][1] + speed[2]
x[5][2] = x[5][2] + speed[2]

second
if (x[6][0] + rect1.left) <= -160:
    x[6][0] = 760
elif (x[6][1] + rect2.left) <= -160:
    x[6][1] = 440
elif (x[6][2] + rect3.left) <= -160:
    x[6][2] = 120

x[6][0] = x[6][0] - speed[0]
x[6][1] = x[6][1] - speed[0]
x[6][2] = x[6][2] - speed[0]

third
if (x[7][0] + rect1.right) >= 1600:
    x[7][0] = -370
elif (x[7][1] + rect2.right) >= 1600:
    x[7][1] = -1170

x[7][0] = x[7][0] + speed[1]
x[7][1] = x[7][1] + speed[1]

fourth

if (x[8][0] + rect1.left) <= -160:
    x[8][0] = 760
elif (x[8][1] + rect2.left) <= -160:
    x[8][1] = 600
elif (x[8][2] + rect3.left) <= -160:
    x[8][2] = 440
elif (x[8][3] + rect4.left) <= -160:
    x[8][3] = 280
elif (x[8][4] + rect5.left) <= -160:
    x[8][4] = 120
elif (x[8][5] + rect6.left) <= -160:
    x[8][5] = -40

x[8][0] = x[8][0] - speed[1]
x[8][1] = x[8][1] - speed[1]
x[8][2] = x[8][2] - speed[1]
x[8][3] = x[8][3] - speed[1]
x[8][4] = x[8][4] - speed[1]
x[8][5] = x[8][5] - speed[1]

fifth

if (x[9][0] + rect1.right) >= 1200:
    x[9][0] = -200
elif (x[9][1] + rect2.right) >= 1200:
    x[9][1] = -500
elif (x[9][2] + rect3.right) >= 1200:
    x[9][2] = -800
elif (x[9][3] + rect4.right) >= 1200:
    x[9][3] = -1100

x[9][0] = x[9][0] + speed[1]
x[9][1] = x[9][1] + speed[1]
x[9][2] = x[9][2] + speed[1]
x[9][3] = x[9][3] + speed[1]
