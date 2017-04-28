import pygame
from random import randint
import time

class Character:
    def __init__(self, x, y, dire):
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
        self.dire = dire
    def update(self):
        self.x += self.speedX
        self.y += self.speedY
#    def display(self):
#        screen.blit(heroImg, (self.x, self.y))

class Hero(Character):
    def limit(self):
        if self.x >460:
            self.x = 460
        elif self.x < 12:
            self.x = 12
        elif self.y > 428:
            self.y =428
        elif self.y < 12:
            self.y = 12
    def hitDetect(self, targetX, targetY):
        if self.x + 32 > targetX and targetX + 32 > self.x and self.y + 32 > targetY and targetY + 32 > self.y:
            return True

class Monster(Character):
    def limit(self):
        if self.x >= 512:
            self.x -= 512
        if self.y >= 480:
            self.y -= 480
        if self.y <= 0:
            self.y += 480
        if self.x <= 0:
            self.x += 480
    def selfMoveGen(self):
        mov = randint(1,6)
        self.dire = mov
    def selfMove(self):
        if self.dire == 1: #right
            self.speedX = 5
        if self.dire == 2: #left
            self.speedX = -5
        if self.dire == 3: #up
            self.speedY = -5
        if self.dire == 4: # down
            self.speedY = 5
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

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Monster Dodge 2')
    clock = pygame.time.Clock()

    # Game initialization
    time_started = time.time()
    next_action_time = time_started +2
    hero = Hero(256, 240, 0)
    monster = Monster(300, 300, 1)

    stop_game = False
    background = pygame.image.load('space.png')
    backgroundAlt = pygame.image.load('spaceinverse.png')
    heroImg = pygame.image.load('crosshair2.png')
    monsterImg = pygame.image.load('images/monster.png')

    screen.blit(background, (0,0))
    screen.blit(heroImg, (hero.x, hero.y))
    screen.blit(monsterImg, (monster.x, monster.y))

    pygame.key.set_repeat(10)

    hit = 0 #hit detection
    loopIteration = 0 #loop count

    while not stop_game:
            # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    hero.speedX = 10
                if event.key == pygame.K_LEFT:
                    hero.speedX = -10
                if event.key == pygame.K_UP:
                    hero.speedY = -10
                if event.key == pygame.K_DOWN:
                    hero.speedY = 10
                if event.key == pygame.K_SPACE:
                    print('SPACE')
                    screen.blit(backgroundAlt, (0,0))
                    pygame.display.update()
                    pygame.time.delay(5)
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
        if hero.hitDetect(monster.x, monster.y):
        #if monster.x + 32 > hero.x and hero.x + 32 > monster.x and monster.y + 32 > hero.y and hero.y + 32 > monster.y:
            hit +=1
            print(hit)
        #
        # Game logic
        monster.selfMove()
        monster.limit()
        monster.update()
        hero.limit()
        hero.update()
        screen.blit(heroImg, (hero.x, hero.y))
        screen.blit(monsterImg, (monster.x, monster.y))

        if next_action_time <= int(time.time()):
            loopIteration += 1
            print('Loop',loopIteration)
            print(monster.dire)
            monster.selfMoveGen()
            time_started = time.time()
            next_action_time = int(time_started) + 2
        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
