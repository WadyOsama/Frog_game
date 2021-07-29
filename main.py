from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame

texture_names = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
speed = [1, 1.2, 1.5, 1.7, 2]
x = [[0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0],
     [0, 0, 0, 0, 0, 0], [0, 0, 0, 0]]
keyboard_x = 380
keyboard_y = 55
lives = 3
score = 0
highest_score = 0
done = 0
time_interval = 10
animation = 1


class Car:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top


class Wood:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top


class Frog:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top


car_1_1 = Car(85, 105, 155, 145)
car_1_2 = Car(485, 105, 555, 145)
car_1_3 = Car(885, 105, 955, 145)

car_2_1 = Car(100, 155, 170, 195)
car_2_2 = Car(365, 155, 435, 195)
car_2_3 = Car(630, 155, 700, 195)
car_2_4 = Car(895, 155, 965, 195)

car_3_1 = Car(45, 205, 115, 245)
car_3_2 = Car(205, 205, 275, 245)
car_3_3 = Car(365, 205, 435, 245)
car_3_4 = Car(525, 205, 595, 245)
car_3_5 = Car(685, 205, 755, 245)
car_3_6 = Car(845, 205, 915, 245)

car_4_1 = Car(5, 255, 75, 295)
car_4_2 = Car(115, 255, 185, 295)
car_4_3 = Car(405, 255, 475, 295)
car_4_4 = Car(515, 255, 585, 295)
car_4_5 = Car(805, 255, 875, 295)
car_4_6 = Car(915, 255, 985, 295)

car_5_1 = Car(0, 305, 120, 345)
car_5_2 = Car(270, 305, 390, 345)
car_5_3 = Car(540, 305, 660, 345)
car_5_4 = Car(810, 305, 930, 345)

wood_1_1 = Wood(0, 405, 200, 445)
wood_1_2 = Wood(400, 405, 600, 445)
wood_1_3 = Wood(800, 405, 1000, 445)

wood_2_1 = Wood(40, 455, 200, 495)
wood_2_2 = Wood(360, 455, 520, 495)
wood_2_3 = Wood(680, 455, 840, 495)

wood_3_1 = Wood(50, 505, 370, 545)
wood_3_2 = Wood(850, 505, 1170, 545)

wood_4_1 = Wood(40, 555, 120, 595)
wood_4_2 = Wood(200, 555, 280, 595)
wood_4_3 = Wood(360, 555, 440, 595)
wood_4_4 = Wood(520, 555, 600, 595)
wood_4_5 = Wood(680, 555, 760, 595)
wood_4_6 = Wood(840, 555, 920, 595)

wood_5_1 = Wood(0, 605, 200, 645)
wood_5_2 = Wood(300, 605, 500, 645)
wood_5_3 = Wood(600, 605, 800, 645)
wood_5_4 = Wood(900, 605, 1100, 645)


def texture_setup(texture, texture_name, width, height):
    glBindTexture(GL_TEXTURE_2D, texture_name)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture)


def loadTextures():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    images = []
    images.append(pygame.image.load("Water.png"))
    images.append(pygame.image.load("Street.png"))
    images.append(pygame.image.load("sidewalk.jpg"))
    images.append(pygame.image.load("Car.png"))
    images.append(pygame.image.load("Car2.png"))
    images.append(pygame.image.load("Wood.png"))
    images.append(pygame.image.load("truck.png"))
    images.append(pygame.image.load("turtle.png"))
    images.append(pygame.image.load("player.png"))
    images.append(pygame.image.load("cover.png"))
    images.append(pygame.image.load("game_over.jpg"))



    textures = [pygame.image.tostring(images[i], "RGBA", 1) for i in range(11)]

    glGenTextures(11, texture_names)

    for i in range(11):
        texture_setup(textures[i], texture_names[i],
                      images[i].get_width(), images[i].get_height())


def initGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, Width, 0, Height, -2, 2)
    glMatrixMode(GL_MODELVIEW)



def water(texture_names, index):
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0, 400, 0)
    glTexCoord2f(1.0, 0)
    glVertex3f(800, 400, 0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(800, 650, 0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(0, 650, 0)
    glEnd()


def street(texture_names, index):
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0, 100, 0)
    glTexCoord2f(1.0, 0)
    glVertex3f(800, 100, 0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(800, 350, 0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(0, 350, 0)
    glEnd()


def sidewalk(texture_names, index):
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0, 50, 0)
    glTexCoord2f(1.5, 0)
    glVertex3f(800, 50, 0)
    glTexCoord2f(1.5, 1.5)
    glVertex3f(800, 700, 0)
    glTexCoord2f(0.0, 1.5)
    glVertex3f(0, 700, 0)
    glEnd()


def cover(texture_names, index):
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.58, 0.0)
    glVertex3f(0, 700, 0)
    glTexCoord2f(2, 0)
    glVertex3f(800, 700, 0)
    glTexCoord2f(2, 1)
    glVertex3f(800, 800, 0)
    glTexCoord2f(0.58, 1)
    glVertex3f(0, 800, 0)
    glEnd()
    glLoadIdentity()

    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0, 0, 0)
    glTexCoord2f(0.5, 0)
    glVertex3f(800, 0, 0)
    glTexCoord2f(0.5, 1)
    glVertex3f(800, 50, 0)
    glTexCoord2f(0, 1)
    glVertex3f(0, 50, 0)
    glEnd()
    glLoadIdentity()


def first_row(texture_names, index, rect1, rect2, rect3):
    glTranslate(x[0][0], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect1.left, rect1.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect1.right, rect1.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect1.right, rect1.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect1.left, rect1.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[0][1], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect2.left, rect2.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect2.right, rect2.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect2.right, rect2.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect2.left, rect2.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[0][2], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect3.left, rect3.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect3.right, rect3.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect3.right, rect3.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect3.left, rect3.top, 1.0)
    glEnd()
    glLoadIdentity()

    if (x[0][0] + rect1.right) >= 1200:
        x[0][0] = -160
    elif (x[0][1] + rect2.right) >= 1200:
        x[0][1] = -560
    elif (x[0][2] + rect3.right) >= 1200:
        x[0][2] = -960
    x[0][0] = x[0][0] + speed[2]
    x[0][1] = x[0][1] + speed[2]
    x[0][2] = x[0][2] + speed[2]


def second_row(texture_names, index, rect1, rect2, rect3, rect4):
    glTranslate(x[1][0], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect1.left, rect1.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect1.right, rect1.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect1.right, rect1.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect1.left, rect1.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[1][1], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect2.left, rect2.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect2.right, rect2.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect2.right, rect2.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect2.left, rect2.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[1][2], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect3.left, rect3.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect3.right, rect3.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect3.right, rect3.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect3.left, rect3.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[1][3], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect4.left, rect4.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect4.right, rect4.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect4.right, rect4.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect4.left, rect4.top, 1.0)
    glEnd()
    glLoadIdentity()

    if (x[1][0] + rect1.left) <= -265:
        x[1][0] = 705

    if (x[1][1] + rect2.left) <= -265:
        x[1][1] = 440

    if (x[1][2] + rect3.left) <= -265:
        x[1][2] = 175

    if (x[1][3] + rect4.left) <= -265:
        x[1][3] = -95

    x[1][0] = x[1][0] - speed[0]
    x[1][1] = x[1][1] - speed[0]
    x[1][2] = x[1][2] - speed[0]
    x[1][3] = x[1][3] - speed[0]


def third_row(texture_names, index, rect1, rect2, rect3, rect4, rect5, rect6):
    glTranslate(x[2][0], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect1.left, rect1.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect1.right, rect1.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect1.right, rect1.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect1.left, rect1.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[2][1], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect2.left, rect2.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect2.right, rect2.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect2.right, rect2.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect2.left, rect2.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[2][2], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect3.left, rect3.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect3.right, rect3.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect3.right, rect3.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect3.left, rect3.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[2][3], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect4.left, rect4.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect4.right, rect4.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect4.right, rect4.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect4.left, rect4.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[2][4], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect5.left, rect5.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect5.right, rect5.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect5.right, rect5.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect5.left, rect5.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[2][5], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect6.left, rect6.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect6.right, rect6.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect6.right, rect6.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect6.left, rect6.top, 1.0)
    glEnd()
    glLoadIdentity()

    if (x[2][0] + rect1.right) >= 960:
        x[2][0] = -120
    elif (x[2][1] + rect2.right) >= 960:
        x[2][1] = -280
    elif (x[2][2] + rect3.right) >= 960:
        x[2][2] = -440
    elif (x[2][3] + rect4.right) >= 960:
        x[2][3] = -600
    elif (x[2][4] + rect5.right) >= 960:
        x[2][4] = -760
    elif (x[2][5] + rect6.right) >= 960:
        x[2][5] = -920

    x[2][0] = x[2][0] + speed[0]
    x[2][1] = x[2][1] + speed[0]
    x[2][2] = x[2][2] + speed[0]
    x[2][3] = x[2][3] + speed[0]
    x[2][4] = x[2][4] + speed[0]
    x[2][5] = x[2][5] + speed[0]


def fourth_row(texture_names, index, rect1, rect2, rect3, rect4, rect5, rect6):
    glTranslate(x[3][0], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect1.left, rect1.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect1.right, rect1.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect1.right, rect1.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect1.left, rect1.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[3][1], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect2.left, rect2.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect2.right, rect2.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect2.right, rect2.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect2.left, rect2.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[3][2], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect3.left, rect3.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect3.right, rect3.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect3.right, rect3.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect3.left, rect3.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[3][3], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect4.left, rect4.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect4.right, rect4.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect4.right, rect4.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect4.left, rect4.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[3][4], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect5.left, rect5.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect5.right, rect5.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect5.right, rect5.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect5.left, rect5.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[3][5], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect6.left, rect6.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect6.right, rect6.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect6.right, rect6.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect6.left, rect6.top, 1.0)
    glEnd()
    glLoadIdentity()

    if (x[3][0] + rect1.left) <= -400:
        x[3][0] = 800
    elif (x[3][1] + rect2.left) <= -400:
        x[3][1] = 690
    elif (x[3][2] + rect3.left) <= -400:
        x[3][2] = 400
    elif (x[3][3] + rect4.left) <= -400:
        x[3][3] = 290
    elif (x[3][4] + rect5.left) <= -400:
        x[3][4] = 0
    elif (x[3][5] + rect6.left) <= -400:
        x[3][5] = -110

    x[3][0] = x[3][0] - speed[1]
    x[3][1] = x[3][1] - speed[1]
    x[3][2] = x[3][2] - speed[1]
    x[3][3] = x[3][3] - speed[1]
    x[3][4] = x[3][4] - speed[1]
    x[3][5] = x[3][5] - speed[1]


def fifth_row(texture_names, index, rect1, rect2, rect3, rect4):
    glTranslate(x[4][0], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect1.left, rect1.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect1.right, rect1.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect1.right, rect1.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect1.left, rect1.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[4][1], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect2.left, rect2.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect2.right, rect2.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect2.right, rect2.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect2.left, rect2.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[4][2], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect3.left, rect3.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect3.right, rect3.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect3.right, rect3.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect3.left, rect3.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[4][3], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect4.left, rect4.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect4.right, rect4.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect4.right, rect4.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect4.left, rect4.top, 1.0)
    glEnd()
    glLoadIdentity()

    if (x[4][0] + rect1.right) >= 1070:
        x[4][0] = -120
    elif (x[4][1] + rect2.right) >= 1070:
        x[4][1] = -390
    elif (x[4][2] + rect3.right) >= 1070:
        x[4][2] = -660
    elif (x[4][3] + rect4.right) >= 1070:
        x[4][3] = -930

    x[4][0] = x[4][0] + speed[1]
    x[4][1] = x[4][1] + speed[1]
    x[4][2] = x[4][2] + speed[1]
    x[4][3] = x[4][3] + speed[1]


def first_row_up(texture_names, index, rect1, rect2, rect3):
    glTranslate(x[5][0], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect1.left, rect1.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect1.right, rect1.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect1.right, rect1.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect1.left, rect1.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[5][1], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect2.left, rect2.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect2.right, rect2.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect2.right, rect2.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect2.left, rect2.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[5][2], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect3.left, rect3.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect3.right, rect3.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect3.right, rect3.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect3.left, rect3.top, 1.0)
    glEnd()
    glLoadIdentity()

    if (x[5][0] + rect1.right) >= 1200:
        x[5][0] = -200
    elif (x[5][1] + rect2.right) >= 1200:
        x[5][1] = -600
    elif (x[5][2] + rect3.right) >= 1200:
        x[5][2] = -1000
    x[5][0] = x[5][0] + speed[2]
    x[5][1] = x[5][1] + speed[2]
    x[5][2] = x[5][2] + speed[2]


def second_row_up(texture_names, index, rect1, rect2, rect3):
    glTranslate(x[6][0], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect1.left, rect1.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect1.right, rect1.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect1.right, rect1.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect1.left, rect1.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[6][1], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect2.left, rect2.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect2.right, rect2.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect2.right, rect2.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect2.left, rect2.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[6][2], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect3.left, rect3.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect3.right, rect3.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect3.right, rect3.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect3.left, rect3.top, 1.0)
    glEnd()
    glLoadIdentity()

    if (x[6][0] + rect1.left) <= -160:
        x[6][0] = 760
    elif (x[6][1] + rect2.left) <= -160:
        x[6][1] = 440
    elif (x[6][2] + rect3.left) <= -160:
        x[6][2] = 120

    x[6][0] = x[6][0] - speed[0]
    x[6][1] = x[6][1] - speed[0]
    x[6][2] = x[6][2] - speed[0]


def third_row_up(texture_names, index, rect1, rect2):
    glTranslate(x[7][0], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect1.left, rect1.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect1.right, rect1.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect1.right, rect1.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect1.left, rect1.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[7][1], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect2.left, rect2.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect2.right, rect2.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect2.right, rect2.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect2.left, rect2.top, 1.0)
    glEnd()
    glLoadIdentity()

    if (x[7][0] + rect1.right) >= 1600:
        x[7][0] = -370
    elif (x[7][1] + rect2.right) >= 1600:
        x[7][1] = -1170

    x[7][0] = x[7][0] + speed[1]
    x[7][1] = x[7][1] + speed[1]


def fourth_row_up(texture_names, index, rect1, rect2, rect3, rect4, rect5, rect6):
    glTranslate(x[8][0], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect1.left, rect1.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect1.right, rect1.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect1.right, rect1.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect1.left, rect1.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[8][1], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect2.left, rect2.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect2.right, rect2.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect2.right, rect2.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect2.left, rect2.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[8][2], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect3.left, rect3.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect3.right, rect3.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect3.right, rect3.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect3.left, rect3.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[8][3], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect4.left, rect4.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect4.right, rect4.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect4.right, rect4.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect4.left, rect4.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[8][4], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect5.left, rect5.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect5.right, rect5.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect5.right, rect5.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect5.left, rect5.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[8][5], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect6.left, rect6.bottom, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect6.right, rect6.bottom, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect6.right, rect6.top, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect6.left, rect6.top, 1.0)
    glEnd()
    glLoadIdentity()

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


def fifth_row_up(texture_names, index, rect1, rect2, rect3, rect4):
    glTranslate(x[9][0], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect1.left, rect1.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect1.right, rect1.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect1.right, rect1.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect1.left, rect1.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[9][1], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect2.left, rect2.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect2.right, rect2.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect2.right, rect2.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect2.left, rect2.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[9][2], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect3.left, rect3.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect3.right, rect3.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect3.right, rect3.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect3.left, rect3.top, 1.0)
    glEnd()
    glLoadIdentity()

    glTranslate(x[9][3], 0, 0)
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect4.left, rect4.bottom, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect4.right, rect4.bottom, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect4.right, rect4.top, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect4.left, rect4.top, 1.0)
    glEnd()
    glLoadIdentity()

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


def draw_player(texture_names, index, rect1):
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(rect1.left, rect1.bottom, 1.2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(rect1.right, rect1.bottom, 1.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(rect1.right, rect1.top, 1.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(rect1.left, rect1.top, 1.2)
    glEnd()
    glLoadIdentity()


def test_down(frog):
    if frog.left >= (car_1_1.left+x[0][0]) and frog.left <= (car_1_1.right+x[0][0]-10) and frog.bottom >=100 and frog.top <=150:
        return True
    elif frog.left >= (car_1_2.left+x[0][1]) and frog.left <= (car_1_2.right+x[0][1]-10) and frog.bottom >=100 and frog.top <=150:
        return True
    elif frog.left >= (car_1_3.left+x[0][2]) and frog.left <= (car_1_3.right+x[0][2]-10) and frog.bottom >=100 and frog.top <=150:
        return True

    elif frog.left >= (car_2_1.left+x[1][0]) and frog.left <= (car_2_1.right+x[1][0]-10) and frog.bottom >=150 and frog.top <=200:
        return True
    elif frog.left >= (car_2_2.left+x[1][1]) and frog.left <= (car_2_2.right+x[1][1]-10) and frog.bottom >=150 and frog.top <=200:
        return True
    elif frog.left >= (car_2_3.left+x[1][2]) and frog.left <= (car_2_3.right+x[1][2]-10) and frog.bottom >=150 and frog.top <=200:
        return True
    elif frog.left >= (car_2_4.left+x[1][3]) and frog.left <= (car_2_4.right+x[1][3]-10) and frog.bottom >=150 and frog.top <=200:
        return True

    elif frog.left >= (car_3_1.left+x[2][0]) and frog.left <= (car_3_1.right+x[2][0]-10) and frog.bottom >=200 and frog.top <=250:
        return True
    elif frog.left >= (car_3_2.left+x[2][1]) and frog.left <= (car_3_2.right+x[2][1]-10) and frog.bottom >=200 and frog.top <=250:
        return True
    elif frog.left >= (car_3_3.left+x[2][2]) and frog.left <= (car_3_3.right+x[2][2]-10) and frog.bottom >=200 and frog.top <=250:
        return True
    elif frog.left >= (car_3_4.left+x[2][3]) and frog.left <= (car_3_4.right+x[2][3]-10) and frog.bottom >=200 and frog.top <=250:
        return True
    elif frog.left >= (car_3_5.left+x[2][4]) and frog.left <= (car_3_5.right+x[2][4]-10) and frog.bottom >=200 and frog.top <=250:
        return True
    elif frog.left >= (car_3_6.left+x[2][5]) and frog.left <= (car_3_6.right+x[2][5]-10) and frog.bottom >=200 and frog.top <=250:
        return True

    elif frog.left >= (car_4_1.left+x[3][0]) and frog.left <= (car_4_1.right+x[3][0]-10) and frog.bottom >=250 and frog.top <=300:
        return True
    elif frog.left >= (car_4_2.left+x[3][1]) and frog.left <= (car_4_2.right+x[3][1]-10) and frog.bottom >=250 and frog.top <=300:
        return True
    elif frog.left >= (car_4_3.left+x[3][2]) and frog.left <= (car_4_3.right+x[3][2]-10) and frog.bottom >=250 and frog.top <=300:
        return True
    elif frog.left >= (car_4_4.left+x[3][3]) and frog.left <= (car_4_4.right+x[3][3]-10) and frog.bottom >=250 and frog.top <=300:
        return True
    elif frog.left >= (car_4_5.left+x[3][4]) and frog.left <= (car_4_5.right+x[3][4]-10) and frog.bottom >=250 and frog.top <=300:
        return True
    elif frog.left >= (car_4_6.left+x[3][5]) and frog.left <= (car_4_6.right+x[3][5]-10) and frog.bottom >=250 and frog.top <=300:
        return True

    elif frog.left >= (car_5_1.left+x[4][0]) and frog.left <= (car_5_1.right+x[4][0]-10) and frog.bottom >=300 and frog.top <=350:
        return True
    elif frog.left >= (car_5_2.left+x[4][1]) and frog.left <= (car_5_2.right+x[4][1]-10) and frog.bottom >=300 and frog.top <=350:
        return True
    elif frog.left >= (car_5_3.left+x[4][2]) and frog.left <= (car_5_3.right+x[4][2]-10) and frog.bottom >=300 and frog.top <=350:
        return True
    elif frog.left >= (car_5_4.left+x[4][3]) and frog.left <= (car_5_4.right+x[4][3]-10) and frog.bottom >=300 and frog.top <=350:
        return True

    elif frog.right <= (car_1_1.right+x[0][0]) and frog.right >= (car_1_1.left+x[0][0]+10) and frog.bottom >=100 and frog.top <=150:
        return True
    elif frog.right <= (car_1_2.right+x[0][1]) and frog.right >= (car_1_2.left+x[0][1]+10) and frog.bottom >=100 and frog.top <=150:
        return True
    elif frog.right <= (car_1_3.right+x[0][2]) and frog.right >= (car_1_3.left+x[0][2]+10) and frog.bottom >=100 and frog.top <=150:
        return True

    elif frog.right <= (car_2_1.right+x[1][0]) and frog.right >= (car_2_1.left+x[1][0]+10) and frog.bottom >=150 and frog.top <=200:
        return True
    elif frog.right <= (car_2_2.right+x[1][1]) and frog.right >= (car_2_2.left+x[1][1]+10) and frog.bottom >=150 and frog.top <=200:
        return True
    elif frog.right <= (car_2_3.right+x[1][2]) and frog.right >= (car_2_3.left+x[1][2]+10) and frog.bottom >=150 and frog.top <=200:
        return True
    elif frog.right <= (car_2_4.right+x[1][3]) and frog.right >= (car_2_4.left+x[1][3]+10) and frog.bottom >=150 and frog.top <=200:
        return True

    elif frog.right <= (car_3_1.right+x[2][0]) and frog.right >= (car_3_1.left+x[2][0]+10) and frog.bottom >=200 and frog.top <=250:
        return True
    elif frog.right <= (car_3_2.right+x[2][1]) and frog.right >= (car_3_2.left+x[2][1]+10) and frog.bottom >=200 and frog.top <=250:
        return True
    elif frog.right <= (car_3_3.right+x[2][2]) and frog.right >= (car_3_3.left+x[2][2]+10) and frog.bottom >=200 and frog.top <=250:
        return True
    elif frog.right <= (car_3_4.right+x[2][3]) and frog.right >= (car_3_4.left+x[2][3]+10) and frog.bottom >=200 and frog.top <=250:
        return True
    elif frog.right <= (car_3_5.right+x[2][4]) and frog.right >= (car_3_5.left+x[2][4]+10) and frog.bottom >=200 and frog.top <=250:
        return True
    elif frog.right <= (car_3_6.right+x[2][5]) and frog.right >= (car_3_6.left+x[2][5]+10) and frog.bottom >=200 and frog.top <=250:
        return True

    elif frog.right <= (car_4_1.right+x[3][0]) and frog.right >= (car_4_1.left+x[3][0]+10) and frog.bottom >=250 and frog.top <=300:
        return True
    elif frog.right <= (car_4_2.right+x[3][1]) and frog.right >= (car_4_2.left+x[3][1]+10) and frog.bottom >=250 and frog.top <=300:
        return True
    elif frog.right <= (car_4_3.right+x[3][2]) and frog.right >= (car_4_3.left+x[3][2]+10) and frog.bottom >=250 and frog.top <=300:
        return True
    elif frog.right <= (car_4_4.right+x[3][3]) and frog.right >= (car_4_4.left+x[3][3]+10) and frog.bottom >=250 and frog.top <=300:
        return True
    elif frog.right <= (car_4_5.right+x[3][4]) and frog.right >= (car_4_5.left+x[3][4]+10) and frog.bottom >=250 and frog.top <=300:
        return True
    elif frog.right <= (car_4_6.right+x[3][5]) and frog.right >= (car_4_6.left+x[3][5]+10) and frog.bottom >=250 and frog.top <=300:
        return True

    elif frog.right <= (car_5_1.right+x[4][0]) and frog.right >= (car_5_1.left+x[4][0]+10) and frog.bottom >=300 and frog.top <=350:
        return True
    elif frog.right <= (car_5_2.right+x[4][1]) and frog.right >= (car_5_2.left+x[4][1]+10) and frog.bottom >=300 and frog.top <=350:
        return True
    elif frog.right <= (car_5_3.right+x[4][2]) and frog.right >= (car_5_3.left+x[4][2]+10) and frog.bottom >=300 and frog.top <=350:
        return True
    elif frog.right <= (car_5_4.right+x[4][3]) and frog.right >= (car_5_4.left+x[4][3]+10) and frog.bottom >=300 and frog.top <=350:
        return True


def test_up(frog):
    global keyboard_x
    if frog.left >= (wood_1_1.left+x[5][0]-15) and frog.right <= (wood_1_1.right+x[5][0]+15) and frog.bottom >=400 and frog.top <=450:
        keyboard_x = keyboard_x + speed[2]
        if keyboard_x <= 790:
            return True
        else:
            return False
    elif frog.left >= (wood_1_2.left+x[5][1]-15) and frog.right <= (wood_1_2.right+x[5][1]+15) and frog.bottom >=400 and frog.top <=450:
        keyboard_x = keyboard_x + speed[2]
        if keyboard_x <= 790:
            return True
        else:
            return False
    elif frog.left >= (wood_1_3.left+x[5][2]-15) and frog.right <= (wood_1_3.right+x[5][2]+15) and frog.bottom >=400 and frog.top <=450:
        keyboard_x = keyboard_x + speed[2]
        if keyboard_x <= 790:
            return True
        else:
            return False

    elif frog.left >= (wood_2_1.left+x[6][0]-15) and frog.right <= (wood_2_1.right+x[6][0]+15) and frog.bottom >=450 and frog.top <=500:
        keyboard_x = keyboard_x - speed[0]
        if keyboard_x >= -10:
            return True
        else:
            return False
    elif frog.left >= (wood_2_2.left+x[6][1]-15) and frog.right <= (wood_2_2.right+x[6][1]+15) and frog.bottom >=450 and frog.top <=500:
        keyboard_x = keyboard_x - speed[0]
        if keyboard_x >= -10:
            return True
        else:
            return False
    elif frog.left >= (wood_2_3.left+x[6][2]-15) and frog.right <= (wood_2_3.right+x[6][2]+15) and frog.bottom >=450 and frog.top <=500:
        keyboard_x = keyboard_x - speed[0]
        if keyboard_x >= -10:
            return True
        else:
            return False

    elif frog.left >= (wood_3_1.left+x[7][0]-15) and frog.right <= (wood_3_1.right+x[7][0]+15) and frog.bottom >=500 and frog.top <=550:
        keyboard_x = keyboard_x + speed[1]
        if keyboard_x <= 790:
            return True
        else:
            return False
    elif frog.left >= (wood_3_2.left+x[7][1]-15) and frog.right <= (wood_3_2.right+x[7][1]+15) and frog.bottom >=500 and frog.top <=550:
        keyboard_x = keyboard_x + speed[1]
        if keyboard_x <= 790:
            return True
        else:
            return False

    elif frog.left >= (wood_4_1.left+x[8][0]-15) and frog.right <= (wood_4_1.right+x[8][0]+15) and frog.bottom >=550 and frog.top <=600:
        keyboard_x = keyboard_x - speed[1]
        if keyboard_x >= -10:
            return True
        else:
            return False
    elif frog.left >= (wood_4_2.left+x[8][1]-15) and frog.right <= (wood_4_2.right+x[8][1]+15) and frog.bottom >=550 and frog.top <=600:
        keyboard_x = keyboard_x - speed[1]
        if keyboard_x >= -10:
            return True
        else:
            return False
    elif frog.left >= (wood_4_3.left+x[8][2]-15) and frog.right <= (wood_4_3.right+x[8][2]+15) and frog.bottom >=550 and frog.top <=600:
        keyboard_x = keyboard_x - speed[1]
        if keyboard_x >= -10:
            return True
        else:
            return False
    elif frog.left >= (wood_4_4.left+x[8][3]-15) and frog.right <= (wood_4_4.right+x[8][3]+15) and frog.bottom >=550 and frog.top <=600:
        keyboard_x = keyboard_x - speed[1]
        if keyboard_x >= -10:
            return True
        else:
            return False
    elif frog.left >= (wood_4_5.left+x[8][4]-15) and frog.right <= (wood_4_5.right+x[8][4]+15) and frog.bottom >=550 and frog.top <=600:
        keyboard_x = keyboard_x - speed[1]
        if keyboard_x >= -10:
            return True
        else:
            return False
    elif frog.left >= (wood_4_6.left+x[8][5]-15) and frog.right <= (wood_4_6.right+x[8][5]+15) and frog.bottom >=550 and frog.top <=600:
        keyboard_x = keyboard_x - speed[1]
        if keyboard_x >= -10:
            return True
        else:
            return False

    elif frog.left >= (wood_5_1.left+x[9][0]-15) and frog.right <= (wood_5_1.right+x[9][0]+15) and frog.bottom >=600 and frog.top <=650:
        keyboard_x = keyboard_x + speed[1]
        if keyboard_x <= 790:
            return True
        else:
            return False
    elif frog.left >= (wood_5_2.left+x[9][1]-15) and frog.right <= (wood_5_2.right+x[9][1]+15) and frog.bottom >=600 and frog.top <=650:
        keyboard_x = keyboard_x + speed[1]
        if keyboard_x <= 790:
            return True
        else:
            return False
    elif frog.left >= (wood_5_3.left+x[9][2]-15) and frog.right <= (wood_5_3.right+x[9][2]+15) and frog.bottom >=600 and frog.top <=650:
        keyboard_x = keyboard_x + speed[1]
        if keyboard_x <= 790:
            return True
        else:
            return False
    elif frog.left >= (wood_5_4.left+x[9][3]-15) and frog.right <= (wood_5_4.right+x[9][3]+15) and frog.bottom >=600 and frog.top <=650:
        keyboard_x = keyboard_x + speed[1]
        if keyboard_x <= 790:
            return True
        else:
            return False
    else:
        return False


def test_done(frog):
    if frog.bottom >= 650 and frog.top <= 700:
        return True
    return False


def game_over(texture_names, index):
    glBindTexture(GL_TEXTURE_2D, texture_names[index])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, -0.1)
    glVertex3f(0, 0, 1.95)
    glTexCoord2f(1.0, -0.1)
    glVertex3f(800, 0, 1.95)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(800, 800, 1.95)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(0, 800, 1.95)
    glEnd()
    glLoadIdentity()



def drawText(string, X, Y):
    glLineWidth(3)
    glColor4f(1, 1, 0, 1)
    glLoadIdentity()
    glTranslate(X, Y, 1.9)
    glScale(0.2, 0.2, 1)
    string = string.encode()
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, c)


def draw():
    global speed
    global x
    global lives
    global score
    global highest_score
    global done
    global keyboard_x
    global keyboard_y
    global animation

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    string = "Score: " + str(score)
    drawText(string, 220, 770)
    string = "Highest Score: " + str(highest_score)
    drawText(string, 220, 720)
    string = "Lives: " + str(lives)
    drawText(string, 315, 20)

    glColor(1, 1, 1)

    glLoadIdentity()
    water(texture_names, 0)
    street(texture_names, 1)
    sidewalk(texture_names, 2)
    cover(texture_names, 9)

    first_row(texture_names, 3, car_1_1, car_1_2, car_1_3)
    glLoadIdentity()

    second_row(texture_names, 4, car_2_1, car_2_2, car_2_3, car_2_4)
    glLoadIdentity()

    third_row(texture_names, 3, car_3_1, car_3_2, car_3_3, car_3_4, car_3_5, car_3_6)
    glLoadIdentity()

    fourth_row(texture_names, 4, car_4_1, car_4_2, car_4_3, car_4_4, car_4_5, car_4_6)
    glLoadIdentity()

    fifth_row(texture_names, 6, car_5_1, car_5_2, car_5_3, car_5_4)
    glLoadIdentity()

    first_row_up(texture_names, 5, wood_1_1, wood_1_2, wood_1_3)
    glLoadIdentity()

    second_row_up(texture_names, 5, wood_2_1, wood_2_2, wood_2_3)
    glLoadIdentity()

    third_row_up(texture_names, 5, wood_3_1, wood_3_2)
    glLoadIdentity()

    fourth_row_up(texture_names, 7, wood_4_1, wood_4_2, wood_4_3, wood_4_4, wood_4_5, wood_4_6)
    glLoadIdentity()

    fifth_row_up(texture_names, 5, wood_5_1, wood_5_2, wood_5_3, wood_5_4)
    glLoadIdentity()

    frog = Frog(keyboard_x, keyboard_y, keyboard_x + 40, keyboard_y + 40)
    draw_player(texture_names, 8, frog)

    if animation == 0 :
        game_over(texture_names, 10)
        speed = [1, 1.2, 1.5, 1.7, 2]

    if test_down(frog) is True:
        lives = lives - 1
        keyboard_x = 380
        keyboard_y = 55
        if lives == 0:
            animation = 0
            done = 0


    elif frog.bottom >= 400 and frog.top <= 650 and test_up(frog) is False:
        lives = lives - 1
        keyboard_x = 380
        keyboard_y = 55
        if lives == 0:
            animation = 0
            done = 0

    if test_done(frog) is True:
        score = score + 50
        done = done + 1
        keyboard_x = 380
        keyboard_y = 55
        if score >= highest_score:
            highest_score = score
        if done == 5:
            speed[0] = speed[0] * 1.2
            speed[1] = speed[1] * 1.2
            speed[2] = speed[2] * 1.2
            speed[3] = speed[3] * 1.2
            done = 0

    glutSwapBuffers()


def keyboard_special(key, x, y):
    global keyboard_x
    global keyboard_y
    if key == GLUT_KEY_LEFT:
        keyboard_x = max(keyboard_x - 50, 0)
    elif key == GLUT_KEY_RIGHT:
        keyboard_x = min(keyboard_x + 50, 760)
    elif key == GLUT_KEY_DOWN:
        keyboard_y = max(keyboard_y - 50, 55)
    elif key == GLUT_KEY_UP:
        keyboard_y = keyboard_y + 50


def keyboard(key, x, y):
    global animation
    global score
    global lives
    global keyboard_x
    global keyboard_y
    if key == b"c":
        animation = 1
        lives = 3
        score = 0
        keyboard_x = 380
        keyboard_y = 55


    if key == b"q":
        sys.exit()


def Timer(v):

    draw()

    glutTimerFunc(time_interval, Timer, 1)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH | GLUT_ALPHA)
    glutInitWindowPosition(20, 20)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Frogger")
    loadTextures()
    glutDisplayFunc(draw)
    glutTimerFunc(time_interval, Timer, 1)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(keyboard_special)
    initGL(800, 800)
    glutMainLoop()




main()
