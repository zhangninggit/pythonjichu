import pygame
import time
from pygame.locals import *
import random 


def key_control(hero_temp):
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:

            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_lift()

            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()

            # 检测按键是否是w或者up
            elif event.key == K_w or event.key == K_UP:
                print('up')
                hero_temp.move_up()

            # 检测按键是否是s或者down
            elif event.key == K_s or event.key == K_DOWN:
                print('down')
                hero_temp.move_down()

            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()

class BasePlane(object):
    def __init__(self, screen_temp ,x ,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name) #添加英雄飞机的图片模型
        self.bullet_list = [] #存储发射子弹的引用

class HeroPlane(BasePlane):

    def __init__(self, screen_temp):
        BasePlane.__init__(self,screen_temp, 210,700, "./feiji/hero1.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y)) #显示英雄飞机

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

    def move_up(self):
        self.y -= 5  #控制英雄飞机上移动

    def move_down(self):
        self.y += 5  #控制英雄飞机下移动

    def move_lift(self):
        self.x -= 5  #控制英雄飞机左移动

    def move_right(self):
        self.x += 5  #控制英雄飞机右移动

    def fire(self): #开火
        self.bullet_list.append(Bullet(self.screen,self.x,self.y)) #将子弹对象添加到列表中，子弹对象参数self.screen是在main函数中已经创建好的窗口

class BaseBullet(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x = x
        self.y = y 
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)

#创建子弹
class Bullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp, x + 40, y - 20, "./feiji/bullet.png")
            
            
            
           

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y-=10
    
    def judge(self):
        if self.y <0:
            return True
        else:
            return False


class Enemylane(BasePlane):
    '''敌机的类'''
    def __init__(self, screen_temp):
        BasePlane.__init__(self,screen_temp, 0,0, "./feiji/enemy0.png")   
        self.direction = "right"#用来存储飞机默认的显示方向

    def display(self):
        self.screen.blit(self.image, (self.x, self.y)) #显示飞机

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

            if bullet.judge():
                self.bullet_list.remove(bullet)
    def move(self):
        
        if self.direction =="right":
             self.x += 5
        
        elif self.direction =="left":
             self.x -= 5

        if self.x > 430:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self): #开火
        randombullet = random.randint(1,100)
        if randombullet == 5 or randombullet == 77:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y)) #将子弹对象添加到列表中，子弹对象参数self.screen是在main函数中已经创建好的窗口
            

class EnemyBullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp, x + 20, y + 20, "./feiji/bullet1.png")


    def display(self):
        print("-----------------------------------")
        self.screen.blit(self.image, (self.x, self.y))



    def move(self):
        self.y+=5
    
    def judge(self):
        if self.y>850:
            return True
        else:
            return False


def main():
    # 1.创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2.创建一个背景图片
    background = pygame.image.load("./feiji/background.png")

    # 3.创建一个飞机对象
    hero1 = HeroPlane(screen)
    
    #4.创建一个敌机
    enemy = Enemylane(screen)

    while True:
        screen.blit(background, (0, 0)) #在窗口中添加一张背景图片，图片左上角与窗口左上角重合
        hero1.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        pygame.display.update() #更新窗口显示内容

        key_control(hero1) #调用key_control函数

        time.sleep(0.01)


if __name__ == "__main__":
    main()
