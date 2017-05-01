import pygame
from random import randint
import time

class Character:
    def __init__(self, x, y, dire, condition):
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
        self.dire = dire
        self.condition = condition
    def update(self):
        self.x += self.speedX
        self.y += self.speedY
    def conditionCheck(self, condition):
        self.condition = condition
#    def display(self):
#        screen.blit(heroImg, (self.x, self.y))

class Hero(Character):
    def limit(self):
        if self.x >= 460:
            self.x = 460
        elif self.x <= 12:
            self.x = 12
        elif self.y >= 428:
            self.y = 428
        elif self.y <= 12:
            self.y = 12
    def hitDetect(self, targetX, targetY, fire):
        if fire:
            if self.x + 32 > targetX and targetX + 32 > self.x and self.y + 32 > targetY and targetY + 32 > self.y:
                return True
    def heroInput(self, event, speed):
        if event == pygame.K_RIGHT:
            self.speedX = speed
        if event == pygame.K_LEFT:
            self.speedX = -speed
        if event == pygame.K_UP:
            self.speedY = -speed
        if event == pygame.K_DOWN:
            self.speedY = speed

class Monster(Character):
    def limit(self, width, height):
        if self.x > width:
            self.x -= width
        if self.y >= height:
            self.y -= height
        if self.y <= 0:
            self.y += height
        if self.x <= 0:
            self.x += width
    def selfMoveGen(self):
        mov = randint(1,6)
        self.dire = mov
    def selfMove(self):
        if self.dire == 1: #right
            self.speedX = 2
        if self.dire == 2: #left
            self.speedX = -2
        if self.dire == 3: #up
            self.speedY = -2
        if self.dire == 4: # down
            self.speedY = 2
        if self.speedX == 0 or self.speedY == 0:
            pass
        else:
            if self.dire == 6: #stopY
                self.speedY = 0
        if self.speedY == 0:
            pass
        else:
            if self.dire == 5: #stopX
                self.speedX = 0

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)



    # Game initialization
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Meow Meow Shooting')
    clock = pygame.time.Clock()
    time_started = time.time()
    next_action_time = time_started +2
    hero = Hero(256, 240, 0, 'alive')
    background = pygame.image.load('space.png')
    backgroundAlt = pygame.image.load('spaceinverse.png')
    heroImg = pygame.image.load('crosshair2.png')
    monsterImg = pygame.image.load('cat.png')
    explosion = pygame.image.load('explosion.png')
    monster = []
    monstartposX = []
    monstartposY = []
    level = 20
    for i in range(level*3):
        monstartposX.append(randint(0, width))
        monstartposY.append(randint(0, height))
        monster.append(Monster(monstartposX[i], monstartposY[i], 1, 'alive'))
        screen.blit(monsterImg, (monster[i].x, monster[i].y))

    stop_game = False

    screen.blit(background, (0,0))
    screen.blit(heroImg, (hero.x, hero.y))

    pygame.key.set_repeat(10)

    hit = 0 #hit detection
    loopIteration = 0 #loop count

    while not stop_game:
            # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True
            if event.type == pygame.KEYDOWN: #Keydown input from user
                hero.heroInput(event.key, 10)
                if event.key == pygame.K_SPACE: #Space keydown condition
                    print('SPACE')
                    screen.blit(backgroundAlt, (0,0))
                    bgShoot = backgroundAlt.copy()
                    pygame.draw.line(bgShoot,(255,0,0),(0,480),(hero.x+16,hero.y+16), 5)
                    pygame.draw.line(bgShoot,(255,0,0),(512,480),(hero.x+16,hero.y+16), 5)
                    screen.blit(bgShoot, (0,0))
                    pygame.display.update()
                    pygame.time.delay(5)
                    for i in range(level*3):
                        if hero.hitDetect(monster[i].x, monster[i].y, True): #Check to see if monster was hit
                            print('Monster hit!')
                            monster[i].conditionCheck('dead')
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    hero.speedY = 0
                elif event.key == pygame.K_UP:
                    hero.speedY = 0
                elif event.key == pygame.K_LEFT:
                    hero.speedX = 0
                elif event.key == pygame.K_RIGHT:
                    hero.speedX = 0
        screen.blit(background, (0,0))
        #Instanced Monster looping

        for i in range(level*3): #Instanced monster handling
            monster[i].limit(width, height)
            if monster[i].condition == 'dead': #Checks to see if monster is dead
                screen.blit(explosion, (monster[i].x, monster[i].y)) #Explosion pic
                monster[i].condition == 'gone'

            elif monster[i].condition == 'alive':
                screen.blit(monsterImg, (monster[i].x, monster[i].y)) #Display monster
                monster[i].selfMove()
                monster[i].update()
            else:
                screen.blit(background, (0,0))

        # Game logic

        hero.limit() #Hero limited to the bounds of the game
        hero.update() #Sets Hero speed to user input
        screen.blit(heroImg, (hero.x, hero.y)) #Draws Hero in new position



        if next_action_time <= int(time.time()): #2 second wait loop
            for i in range(level*3):
                monster[i].selfMoveGen()
            time_started = time.time() #Part of 2 second wait loop
            next_action_time = int(time_started) + 2 #Part of 2 second wait loop
        # Game display


        pygame.display.update()
        clock.tick(60)


    pygame.quit()


if __name__ == '__main__':
    main()
