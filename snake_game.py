import pygame
import os
import sys
import math
import random

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.seed()


SPEED = 0.30
SNAKE_SIZE = 9
APPLE_SIZE= SNAKE_SIZE
SEPERATION = 10
SCREEN_HEIGHT =600
SCREEN_WIDTH = 800
FPS = 25
KEY ={"UP":1, "DOWN":2, "LEFT":3, "RIGHT":4}


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWSURFACE)

score_font = pygame.font.Font(None, 38)
score_numb_font = pygame.font.Font(None, 28)
game_over_font = pygame.font.Font(None, 48)
play_again_font = score_numb_font
score_msg = score_font.render("Score: ", 1,pygame.Color("green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color("black")
apple_color = pygame.Color("red")
black = pygame.Color(0,0,0)


gameclock = pygame.time.Clock()

def checkCOllision(posA, As, posB, Bs):
    if(posA.x < posB.x + Bs and posA.x + As > posB.x and posA.y < posB.y + Bs and posA.y + As > posB.y):
        return True
    return False

def checkLimits(snake):
    if(snake.x < SCREEN_WIDTH):
        snake.x = SNAKE_SIZE
    if(snake.x < 0):
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if(snake.y > SCREEN_HEIGHT):
        snake.y = SNAKE_SIZE
    if (snake.y < 0):
        snake.y = SCREEN_HEIGHT - SNAKE_SIZE

class Apple:
    def __init__(self,x,y,state):
        self.x = x
        self.y = y
        self.state = state
        self.color = pygame.color.Color("orange")
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, APPLE_SIZE, APPLE_SIZE),0)
        
class segment:
    def __init__(self,x,y):
        self.x =x
        self.y =y
        self.direction = KEY["UP"]
        self.color = "white"

class snake:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.direction = KEY["UP"]
        self.stack = []
        self.stack.append(self)
        blackBox = segment(self.x, self.y + SEPERATION)
        blackBox.direction = KEY["UP"]
        blackBox.color = "NULL"
        self.stack.append(blackBox)

    def move(self):
        last_element = len(self.stack) - 1
        while(last_element != 0):
            self.stack[last_element].direction = self.stack[last_element].direction
            self.stack[last_element].x = self.stack[last_element - 1].x
            self.stack[last_element].y = self.stack[last_element - 1].y
            last_element -= 1
        # if(di):
        #     last_element = self
        else:
            last_element = self.stack.pop(last_element)
        last_element.direction = self.stack [0].direction
        if(self.stack[0].direction == KEY["UP"]):
            last_element.y = self.stack[0].y -(SPEED * FPS)
        elif(self.stack[0].direction == KEY["DOWN"]):
            last_element.y = self.stack[0].y + (SPEED * FPS)
        elif(self.stack[0].direction == KEY["LEFT"]):
            last_element.x = self.stack[0].x -(SPEED * FPS)
        elif(self.stack[0].direction == KEY["RIGHT"]):
            last_element.x = self.stack[0].x +(SPEED * FPS)
        self.stack.insert(0, last_element)
    def getHead(self):
        return(self.stack[0])
    def grow(self):
        last_element = len(self.stack)-1
        self.stack[last_element].direction = self.stack[last_element].direction
        if(self.stack[last_element].direction == KEY["UP"]):
            newSgement = segment(self.stack[last_element].x, self.stack[last_element].y - SNAKE_SIZE)
            blackBox = segment(newSgement.x, newSgement.y - SEPERATION)
        elif(self.stack[last_element].direction == KEY["DOWN"]):
            newSgement = segment(self.stack[last_element].x, self.stack[last_element].y + SNAKE_SIZE)
            blackBox = segment(newSgement.x, newSgement.y + SEPERATION)
        elif(self.stack[last_element].direction == KEY["LEFT"]):
            newSgement = segment(self.stack[last_element].x - SNAKE_SIZE, self.stack[last_element].y)
            blackBox = segement(newSgement.x - SEPERATION, newSgement.y)
        elif(self.stack[last_element].direction == KEY["RIGHT"]):
            newSgement = segment(self.stack[last_element].x + SNAKE_SIZE, self.stack[last_element].y)
            blackBox = segement(newSgement.x + SEPERATION, newSgement.y)
        blackBox.color ="NULL"
        self.stack.append(newSgement)
        self.stack.append(blackBox)
    def iterateSegment(self, delta):
        pass
    def setDirection(self, direction):
        if(self.direction == KEY["RIGHT"] and direction == KEY["LEFT"] or self.direction == KEY["RIGHT"]):
            pass
        elif(self.direction == KEY["UP"] and direction == KEY["DOWN"] or self.direction == KEY["RIGHT"]):
            pass
        else:
            self.direction = direction
    def get_rect(self):
        rect = (self.x, self.y)
        return rect
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    def checkCrash(self):
        counter = 1
        while(counter < len(slef.stack)-1):
            if(checkCOllision(self.stack[0], SNAKE_SIZE, self.stack[counter], SNAKE_SIZE)and self.stack[counter].color != "NULL"):
                return True
            counter += 1
            return False
    def draw(self, screen):
        pygame.draw.rect(screen, pygame.color.Color("green"), (self.stack[0].x, self.stack[0].y, SNAKE_SIZE, SNAKE_SIZE), 0)
        counter = 1
        while(counter < len(self.stack)):
            if(self.stack[counter].color == "NULL"):
                counter += 1
                continue
            pygame.draw.rect(screen, pygame.color.Color("white"), (self.stack[counter].x, self.stack[counter].y, SNAKE_SIZE, SNAKE_SIZE), 0)
            counter += 1
    





        
        
def geyGameKey():
    for event in pygame.event.get():
        if event.key == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["UP"]
            elif event.key == pygame.K_DOWN:
                return KEY["DOWN"]
            elif event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            elif event.key == pygame.K_RIGHT:
                return KEY["RIGHT"]
            elif event.key == pygame.K_ESCAPE:
                return "exit"
                
            elif event.key == pygame.K_y:
                return "yes"
            elif event.key == pygame.K_n:
                return "no"
        if event.type == pygame.QUIT:
            return sys.exit(0)
def endGame():         
    message = game_over_font.render("Game Over!!!", 1, pygame.Color("red"))
    message_play_again = play_again_font.render("Play Again? (y/n)", 1, pygame.Color("green"))
    screen.blit(message, (320,240))
    screen.blit(message_play_again, (320+12,240 +40))

    pygame.display.flip()
    pygame.display.update()

    mKey = geyGameKey()
    while (mkey != "exit"):
        if(mKey == "yes"):
            main()
        elif(mKey == "no"):
            break
        mKey = geyGameKey()
        gameclock.tick(FPS)
    sys.exit(0)

def drawScore(score):
    score_numb = score_numb_font.render(str(score), 1, pygame.Color("green"))
    screen.blit(score_msg, (SCREEN_WIDTH - score_msg_size[0] - 60, 10))
    screen.blit(score_numb, (SCREEN_WIDTH - 45,14))

def drawGameTime(gameTime):
    game_time = score_font.render("Time: ", 1, pygame.Color("white"))
    game_time_numb = score_numb_font.render(str(gameTime), 1, pygame.Color("white"))
    screen.blit(game_time, (30,10))
    screen.blit(game_time_numb, (105, 14))


def exitScreen():
    pass

def respawnApple(apples, index, sx, sy):
    radius = math.sqrt((SCREEN_WIDTH/2 * SCREEN_WIDTH/2 + SCREEN_HEIGHT/2 * SCREEN_HEIGHT/2))/2
    angle = 999
    while(angle >radius):
        angle = random.uniform(0, 800)* math.pi *2
        x = SCREEN_WIDTH/2 + radius * math.cos(angle)
        y = SCREEN_HEIGHT/2 + radius * math.sin(angle)
        if(x == sx and y ==sy):
            continue
        newApple = Apple(x, y,1)
        apples[index] = newApple
def respawnApples(apples, quantity , sx, sy):
    counter =0
    del apples[:]
    radius = math.sqrt((SCREEN_WIDTH/2 * SCREEN_WIDTH/2 + SCREEN_HEIGHT/2 * SCREEN_HEIGHT/2))/2
    angle  = 999
    while(counter < quantity):
        while(angle > radius):
            angle = random.uniform(0, 800)* math.pi *2
            x = SCREEN_WIDTH /2 + radius *math.cos(angle)
            y = SCREEN_HEIGHT /2 + radius * math.sin(angle)
            if(x + APPLE_SIZE == sx or x + APPLE_SIZE ==sx)and (y - APPLE_SIZE == sy or y- APPLE_SIZE == sy or radius - angle <= 10 ):
                continue
            apples.append(Apple(x, y, 1))
            angle = 999
            counter += 1
            



def main():
    score = 0
    
    mySnake = snake(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    mySnake.setDirection(KEY["UP"])
    mySnake.move()
    start_segments = 3
    while(start_segments > 0):
        mySnake.grow()
        mySnake.move()
        start_segments -= 1
    max_apples = 1
    eaten_apple = False
    apples = [Apple(random.randint(60, SCREEN_WIDTH - SNAKE_SIZE), random.randint(60, SCREEN_HEIGHT - SNAKE_SIZE),1)]
    respawnApples(apples, max_apples, mySnake.x, mySnake.y)

    startTime = pygame.time.get_ticks()
    endGame = 0
    while (endGame != 1):
        gameclock.tick(FPS)

        keyPress = getGameKey()
        if keyPress == "exit":
            endGame = 1
        checkLimits(mySnake)
        if(mySnake.checkCrash() == True):
            endGame()
        
        for myApple in apples:
            if(myApple.state == 1):
                if(checkCOllision(mySnake.getHead(), SNAKE_SIZE, myApple, APPLE_SIZE ) == True ):



                    mySnake.grow()
                 
                    myApple.state = 0
                    score += 10
                    eaten_apple = True
        if(keyPress):
            mySnake.setDirection(keyPress)
        mySnake.move()

        if(eaten_apple == True):
            eaten_apple = False
            respawnApples(apples, 0, mySnake.grow(), mySnake.getHead().y)
        
        screen.fill(background_color)

        for myApple in apples:
            if(myApple.state == 1):
                myApple.draw(screen)
        mySnake.draw(screen)
        drawScore(score)
        gameTime = pygame.time.get_ticks() - startTime
        drawGameTime(gameTime)   

        pygame.display.flip()
        pygame.display.update() 
main()




