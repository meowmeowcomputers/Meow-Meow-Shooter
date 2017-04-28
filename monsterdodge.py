import pygame
from random import randint
import time

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
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
    hero = Hero(256, 240)
    monsterX = 300
    monsterY = 300
    stop_game = False
    background = pygame.image.load('images/background.png')
    heroImg = pygame.image.load('link.gif')
    monsterImg = pygame.image.load('images/monster.png')

    screen.blit(background, (0,0))
    screen.blit(heroImg, (hero.x, hero.y))
    screen.blit(monsterImg, (monsterX, monsterY))

    pygame.key.set_repeat(10)

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
        screen.blit(heroImg, (hero.x, hero.y))
        #
        monsterY += randint(1,100)
        monsterX += randint(-100,100)
        if monsterX >= 512:
            monsterX -= 512
        if monsterY >= 480:
            monsterY -= 480
        if monsterY <= 0:
            monsterY += 480
        if monsterX <= 0:
            monsterX += 480
        screen.blit(monsterImg, (monsterX, monsterY))
        # if heroX >460:
        #     heroX = 460
        # elif heroX < 12:
        #     heroX = 12
        # elif heroY > 428:
        #     heroY =428
        # elif heroY < 12:
        #     heroY = 12

        # heroHitX = range(heroX, heroX+32)
        # heroHitY = range(heroY, heroY+32)

        # # if monsterX >= heroX and monsterX <= heroX-32 and monsterY >= heroY and monsterY <= heroY +32 and monsterY >= heroY:
        #     print('HIT')


        # Game logic
        hero.update()
        hero.limit()
        if next_action_time <= int(time.time()):
        #    monster.mov()
            time_started = time.time()
            next_action_time = int(time_started) + 2
        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
