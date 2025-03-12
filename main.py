#Game made by logipoo inc
#I imagine this is really messed up ):
'''GAYME
GYATT
UwU/OwO
You found the secrets, now you know de way'''
import pygame, time, sys
from pygame.locals import *

# pygame setup
pygame.init()
X = 1280
Y = 720
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
running = True
dt = 0
playerLeft = pygame.image.load("PlayerLEFT.png")
playerRight = pygame.image.load("PlayerRIGHT.png")
desk = pygame.image.load("Desk.png")
pricecoLogo = pygame.image.load('PricecoLogo.png')
taxbox = pygame.image.load('OutofitTax.png')
bed = pygame.image.load('BedSprite.png')

rect = pygame.Rect(980, 590, 30, 30) 
vel = 5
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
BROWN = (88, 57, 39)

player_x = 980
player_y = 540
player_speed = 1
player = playerLeft
money = 0
boss = 5
taxCard = False
slept = False

inspect = False
tutFin = False
door = False
buy = False
insPos = False

sysfont = pygame.font.get_default_font()
print('system font :', sysfont)

t0 = time.time()
font = pygame.font.SysFont('chalkduster.ttf', 72)
font2 = pygame.font.SysFont('chalkduster.ttf', 40)
fontL = pygame.font.SysFont('chalkduster.ttf', 100)
fontmini = pygame.font.SysFont('chalkduster.ttf', 20)
fontXXXL = pygame.font.SysFont('chalkduster.ttf', 300)

#This is where text is renderd
#Also when you wont font, you can type screen.blit(font.render('Text', True, Color), (Pos_x, Pos_y))
#I perfer this
img1 = font.render('Move with A/D or ARROWS; get to the green door.', True, BLUE)
img1_2 = font2.render('To go through doors (once moved onto them) press E.', True, BLUE)#Yeah I messed the name up sorry future logan
img2 = font.render('You can jump with SPACEBAR; again you need', True, BLUE)
img3 = font.render('to get to the green door.', True, BLUE)
img4 = font2.render('Move on an ! and press L to show something, ESC to close;', True, BLUE)
img5 = font2.render('then you know what to do.', True, BLUE)
img6 = font.render('Then the tutorial is done!', True, GREEN)
look = font2.render('!', True, RED)
tutMenu = font.render('Finished! Enter the door.', True, GREEN)
houseTxt = font.render('House:', True, BROWN)
houseMenu = font.render('This is your house, taxes are do.', True, GREEN)
houseMenu2 = font.render('Go to your job to earn money.', True, GREEN)
jobDoorTxt = font2.render('Job:', True, BLACK)
jobTxt = font.render('Job:', True, BROWN)
deskMenu = font.render('Job Job Job Job Job Job', True, GREEN)
deskMenu2 = font2.render('This is the only computer you have access to.', True, BLACK)
houseDoorTxt = font2.render('House:', True, BROWN)
fired = fontL.render('YOUR FIRED!', True, RED)
storeDoorTxt = font2.render('Store:', True, BLACK)
buyExplain = font2.render('Standing on item to buy;', True, BLUE)
buyExplain2 = font2.render('press l to vew the product; press P and you own it,', True, BLUE)
buyExplain3 = font2.render("unless you're 2 broke 4 item (Tax = 8%)", True, BLUE)
taxCardExplain = font2.render('OutOfIt ImmidiateTax Supreme; $80.00', True, BLACK)
taxCardExplain2=font2.render('Do taxes quickly on any Windows/Pear computer', True, BLACK)
bedTxt = font2.render('Sleep with E', True, BLACK)
hire = font2.render('Hireing:', True, BLACK)
hireRoomTxt = font.render('Hired!', True, GREEN)



fonts = pygame.font.get_fonts()
print(len(fonts))
for i in range(7):
    print(fonts[i])

#level1 = True all others = False
level1 = True
level2 = False
level3 = False
house = False
job = False
store = False
hireRoom = False
Finished = False

pygame.display.set_caption('TAXES! The Game')


        
while running:
    moneyR = 'Money = ' + str(money)
    moneyBar = font.render(moneyR, True, GREEN )


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if inspect == False:
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_x -= 300 * dt
            player = playerLeft
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_x += 300 * dt
            player = playerRight
        if keys[pygame.K_SPACE]:
            player_y -= 7
        elif player_y < 560:
            player_y += 7
        if keys[pygame.K_e]:
                door = True
        else:
            door = False
        if keys[pygame.K_p]:
            buy = True
        else:
            buy = False
        if keys[pygame.K_l] and insPos == True:
            inspect = True
    if player_y > 560:
        player_y = 560
    if player_x < 0:
        player_x = 0
    if player_x > 1220:
        player_x = 1220
    if player_y < 0:
        player_y = 0
    if keys[pygame.K_RCTRL]:
        if keys[pygame.K_r]:
            level1 = True
            level2 = False
    if keys[pygame.K_RCTRL]:
        if keys[pygame.K_s]:
            level1 = False
            level2 = False
            level3 = False
            house = True
    if keys[pygame.K_ESCAPE]:
        inspect = False

    if level2 == True:
        level1 = False
        screen.fill(white)
        screen.blit(img2, (20, 20))
        screen.blit(img3, (20, 92))
        gate = pygame.draw.rect(screen, (0,255,0), (1240, 540, 40, 80))
        pygame.draw.rect(screen, (64, 64, 64), (0, 620, 1280, 100))
        pygame.draw.rect(screen, (64, 64, 64), (700, 520, 100, 100))
        screen.blit(player, (player_x, player_y))
        pygame.display.update()
        if player_y > 540:
            if player_x > 1200:
                if door == True:
                    level3 = True

        if player_x > 649:
                if player_x < 788:
                    if player_y > 490:
                        if player_x > 700:
                            player_x = 790
                        if player_x < 700:
                            player_x = 649
        if player_y > 455:
            if player_x > 660:
                if player_x < 785:
                    player_y = 455
                    


    if level1 == True:
        level2 = False
        level3 = False
        house = False
        screen.fill(white)
        screen.blit(img1, (20, 20))
        screen.blit(img1_2, (20, 92))
        gate = pygame.draw.rect(screen, (0,255,0), (0, 540, 40, 80))
        pygame.draw.rect(screen, (64, 64, 64), (0, 620, 1280, 100))
        screen.blit(player, (player_x, player_y))
        pygame.display.update()
        if player_x < 40:
            if player_y > 540:
                if door == True:
                    level2 = True
    
    if level3 == True:
        level2 = False
        lavel1 = False
        screen.fill(white)
        pygame.draw.rect(screen, (0,255,0), (0, 540, 40, 80))
        pygame.draw.rect(screen, (64, 64, 64), (0, 620, 1280, 100))
        screen.blit(img4, (20, 20))
        screen.blit(img5, (20, 60))
        screen.blit(look, (450, 520))
        screen.blit(player, (player_x, player_y))
        if tutFin == True:
            screen.blit(img6, (20, 100))
            if player_x < 40:
                if player_y > 540:
                    if door == True:
                        house = True
        if 360 < player_x < 440:
            if player_y > 535:
                insPos = True
                if inspect == True:
                    pygame.draw.rect(screen, GRAY, (200, 100, 880, 570))
                    screen.blit(tutMenu, (260, 130))
                    tutFin = True
            else:
                insPos = False
        pygame.display.update()
    
    if house == True:
        level1 = False
        level2 = False
        level3 = False
        job = False
        screen.fill(white)
        pygame.draw.rect(screen, BROWN, (200, 590, 100, 30))
        pygame.draw.rect(screen, (64, 64, 64), (0, 620, 1280, 100))
        screen.blit(bed, (900, 560))
        screen.blit(houseTxt, (20, 20))
        screen.blit(look, (250, 560))
        screen.blit(look, (950, 560))
        screen.blit(jobDoorTxt, (400, 510))
        screen.blit(storeDoorTxt, (600, 510))
        screen.blit(moneyBar, (20, 630))
        pygame.draw.rect(screen, GREEN, (400, 540, 60, 80))
        pygame.draw.rect(screen, GREEN, (600, 540, 60, 80))
        screen.blit(player, (player_x, player_y))
        if door == True:
            if 900 < player_x < 1000:
                if player_y > 500:
                    slept = True
        if 900 < player_x < 1000:
            insPos = True
        else:
            insPos = False    
        if inspect == True:
            if 900 < player_x < 1000:
                pygame.draw.rect(screen, GRAY, (200, 100, 880, 570))
                screen.blit(bedTxt, (220, 120))
        if player_x > 200:
            if player_x < 300:
                insPos = True
                if inspect == True:
                    pygame.draw.rect(screen, GRAY, (200, 100, 880, 570))
                    screen.blit(houseMenu, (260, 130))
                    screen.blit(houseMenu2, (260, 202))
        if player_x > 350:
            if player_x < 460:
                if player_y > 540:
                    if door == True:
                        if boss > 0:
                            job = True
                            house = False
                        if boss == 0:
                            print("If you found this, you're still FIRED!")
        if player_x > 550:
            if player_x < 660:
                if player_y > 540:
                    if door == True:
                        store = True
                        house = False
        pygame.display.update()

    if job == True:
        house = False
        screen.fill(white)
        screen.blit(jobTxt, (20, 20))
        screen.blit(desk, (300, 560))
        screen.blit(look, (350, 540))
        screen.blit(moneyBar, (20, 630))
        pygame.draw.rect(screen, (0,255,0), (0, 540, 40, 80))
        pygame.draw.rect(screen, (64, 64, 64), (0, 620, 1280, 100))
        screen.blit(player, (player_x, player_y))
        if inspect == True:
            if player_x < 400:
                if player_x > 300:
                    pygame.draw.rect(screen, GRAY, (200, 100, 880, 570))
                    screen.blit(deskMenu, (260, 130))
                    screen.blit(deskMenu2, (220, 180))
                    if taxCard == True:
                        screen.blit(font.render('YOU HAVE THE WRONG PC FOR TAXES!', True, RED), (220, 252))
        if player_x < 400:
            if player_x > 300:
                insPos = True
            else:
                insPos = False
        if player_x < 40:
            if player_y > 540:
                if door == True:
                    job = False
                    house = True
                    if boss > 0: 
                        money += 20
                        boss -= 1
                    if boss == 0:
                        money += 50
                        screen.blit(fired, (20, 400))
                        pygame.display.update()
                        time.sleep(5)
        pygame.display.update()
    
    if store == True:
        house = False
        screen.fill(white)
        screen.blit(pricecoLogo, (20, 20))
        pygame.draw.rect(screen, (64, 64, 64), (0, 620, 1280, 100))
        pygame.draw.rect(screen, (0,255,0), (0, 540, 40, 80))
        screen.blit(taxbox, (200, 570))
        screen.blit(moneyBar, (20, 630))
        if slept == True and boss == 0:
             pygame.draw.rect(screen, GREEN, (1000, 540, 60, 80))
             screen.blit(hire, (1000, 500))
             if door == True:
                 if 980 < player_x < 1060:
                     if player_y > 500:
                         hireRoom = True
                         store = False
        screen.blit(player, (player_x, player_y))
        screen.blit(buyExplain, (20, 100))
        screen.blit(buyExplain2, (20, 140))
        screen.blit(buyExplain3, (20, 180))
        if 160 < player_x < 230:
            insPos = True
            if inspect == True:
                pygame.draw.rect(screen, GRAY, (200, 100, 880, 570))
                screen.blit(taxCardExplain, (220, 120))
                screen.blit(taxCardExplain2, (220, 190))
            if taxCard == False:
                if buy == True and money >= 86.4:
                    money -= 80
                    money -= 6.4
                    taxCard = True
        else:
            insPos = False
        if player_x < 40:
            if player_y > 540:
                if door == True:
                    store = False
                    house = True
        pygame.display.update()
    if hireRoom == True:
        store = False
        screen.fill(white)
        screen.blit(hireRoomTxt, (20,100))
        screen.blit(desk, (300, 560))
        screen.blit(look, (350, 540))
        screen.blit(moneyBar, (20, 630))
        pygame.draw.rect(screen, (0,255,0), (0, 540, 40, 80))
        screen.blit(player, (player_x, player_y))
        pygame.draw.rect(screen, (64, 64, 64), (0, 620, 1280, 100))
        screen.blit(pricecoLogo, (20, 20))
        if inspect == True:
            if player_x < 400:
                if player_x > 300:
                    pygame.draw.rect(screen, GRAY, (200, 100, 880, 570))
                    screen.blit(deskMenu, (260, 130))
                    screen.blit(deskMenu2, (220, 180))
                    if taxCard == True:
                        screen.blit(font.render('TAXES DONE! You Win', True, GREEN), (220, 252))
                        Finished = True
        if player_x < 400:
            if player_x > 300:
                insPos = True
        else:
            insPos = False
        if player_x < 40:
            if player_y > 540:
                if door == True:
                    player_x = 1200
                    hireRoom = False
                    store = True
        pygame.display.update()
    if Finished == True:
        hireRoom = False
        time.sleep(5)
        screen.fill(white)
        screen.blit(fontXXXL.render('WIN!!!', True, GREEN), (200, 100))
        screen.blit(fontmini.render('Please rate our game at: https://sites.google.com/view/logipoo-inc/taxes-the-game/reviews?authuser=2, we will try to add more features in the future.', True, BLACK), (20,20))
        pygame.display.update()


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics
    dt = clock.tick(60) / 1000




pygame.quit()