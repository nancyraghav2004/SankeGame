import pygame
import random
import os

pygame.mixer.init()

pygame.init()

screen_width = 900
screen_height = 600
#Creating Window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Backgroung Image
bgimg = pygame.image.load("D:\\Python_Pyscripter\\snakeimg.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()



#Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)



# Game Title
pygame.display.set_caption("Snakes Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def  plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.ellipse(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233, 220, 229))
        text_screen("Welcome to Snakes Game", black, 200, 250)
        text_screen("Press Space Bar To Play Game", black, 160, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("D:\\Python_Pyscripter\\A Truly Dazzling Dream - National Sweetheart.mp3")
                    pygame.mixer.music.play()

                    gameloop()
        pygame.display.update()
        clock.tick(60) #60 is fps here#


def gameloop():

    # Gsame specific variables
    exit_game = False
    game_over = False
    snake_x = 30
    snake_y = 40
    velocity_x =0
    velocity_y = 0
    score = 0

    food_x = random.randint(20, screen_width//2)
    food_y = random.randint(20, screen_height//2)
    init_velocity = 5
    snake_size = 20
    fps = 60

    snk_list = []
    snk_length = 1


    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = int(f.read())

    '''with open("hiscore.txt", "r") as f:
        hiscore = f.read()'''


    #Game loop
    while not exit_game:

        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 200)

            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x =  - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = + init_velocity
                        velocity_x = 0

                    # Cheat Code
                    if event.key == pygame.K_q:
                        score += 10


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score += 10
                food_x = random.randint(20, screen_width//2)
                food_y = random.randint(20, screen_height//2)
                snk_length += 5

                if score > int(hiscore):
                    hiscore = score



            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), red, 5, 5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("D:\\Python_Pyscripter\\Big Explosion Cut Off.mp3")
                pygame.mixer.music.play()



            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("D:\\Python_Pyscripter\\Big Explosion Cut Off.mp3")
                pygame.mixer.music.play()


            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            #pygame.draw.ellipse(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()
#gameloop()













'''#Creating Window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("Snakes Game")

#Game specified variables
exit_game = False
game_over = False

#Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key.")


pygame.quit()
quit()'''


