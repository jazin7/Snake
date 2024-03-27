import pygame
from random import randint
from time import sleep

pygame.init()

heigth = 720
width = 1080
screen = pygame.display.set_mode(size=(width, heigth))
clock = pygame.time.Clock()
pygame.display.set_caption("Vorkurs Gruppe 2 Pygame: Snake")
screen.fill((0, 0, 0))
score = 0

n = 1

snakehead = [250, 250]
snakebody = [
    [250, 250],     # x,y
    [240, 250],
    [230, 250],
]
fruit = [randint(20, width - 20), randint(20, heigth - 20)]

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and n!=2:
                #snakehead[0] = snakehead[0] + 20
                n = 1
            if event.key == pygame.K_LEFT and n!=1:
               # snakehead[0] = snakehead[0] - 20
                n = 2
            if event.key == pygame.K_UP and n!=4:
              #  snakehead[1] = snakehead[1] - 20
                n = 3
            if event.key == pygame.K_DOWN and n!=3:
               # snakehead[1] = snakehead[1] + 20
                n = 4 
    

    if n == 1:
        snakehead[0] = snakehead[0] + 20
    if n == 2:
        snakehead[0] = snakehead[0] - 20
    if n == 3:
        snakehead[1] = snakehead[1] - 20
    if n == 4:
        snakehead[1] = snakehead[1] + 20
    
    snakebody.insert(0, list(snakehead))


# negative value nicht beachtet. kann randomrespawnen
    if abs(fruit[0] - snakehead[0]) < 20 and abs(fruit[1] - snakehead[1]) < 20:
        fruit = [randint(20, width - 20), randint(20, heigth - 20)]
        score += 1
    else:
        snakebody.pop()

    screen.fill((0, 0, 0)) 

    for bodypart in snakebody:
        pygame.draw.circle(screen, (0, 255, 0), (bodypart[0], bodypart[1]), 10)
    pygame.draw.rect(screen, (255, 0, 0), [fruit[0], fruit[1], 20, 20])

    if snakehead[0] > width-20 or snakehead[0] < 20:
        running = False

    if snakehead [1] > heigth-20 or snakehead[1] < 20:
        running = False

    if running == False:
        gameoverSchrift = pygame.font.SysFont(
            'Arial', 65, bold=True, italic=True)
        gameoverText = gameoverSchrift.render(
            'Game Over!', True, (42, 42, 42))
        screen.blit(gameoverText, dest=[width // 2, heigth // 2])
        sleep(1)
    
    punkteSchrift = pygame.font.SysFont('Arial', 20 * 2)
    punkteText = punkteSchrift.render(
        f'Punkte: {score}', True, pygame.Color(255, 255, 255))
    screen.blit(punkteText, dest=[0, 0])






    pygame.display.flip()
    clock.tick(8)

sleep(3)
pygame.quit()



