import pygame
import time 
import random

pygame.init()

dis_width=600
dis_height=400
dis=pygame.display.set_mode((dis_width,dis_height))

pygame.display.set_caption('Project_Kalinovskiy')

green=(0,128,0)
blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
yellow=(255,255,0)

clock=pygame.time.Clock()

snake_block=10 
snake_speed=12


font_style=pygame.font.SysFont("Arial",19)
score_font=pygame.font.SysFont(None,35)

def your_score(score):
    """Выводит счётчик очков в левом верхнем углу"""
    value=score_font.render("Счёт: "+str(score),True,blue)
    dis.blit(value,[0,0])

def our_snake(snake_block, snake_list):
    """Рисует змейку заданного цвета и размера"""
    for x in snake_list:
        pygame.draw.rect(dis,green,[x[0],x[1],snake_block, snake_block])

def message(msg,color):
    """Настраивает сообщение, которое выводится в случае проигрыша"""
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg, [10,180])

def gameLoop():
    """Настраивает игровой цикл"""
    game_over=False
    game_close=False

    x1=dis_width/2
    y1=dis_height/2

    x1_change=0
    y1_change=0
    
    snake_List=[]
    Length_of_snake=1

    foodx=round(random.randrange(0, dis_width-snake_block)/10.0)*10.0
    foody=round(random.randrange(0, dis_height-snake_block)/10.0)*10.0

    while not game_over:

        while game_close==True:
            dis.fill(black)
            message("Ты проиграл! Нажми кнопку З-чтобы начать Заново или Щ-чтобы выйти из игры.", red)
            your_score(Length_of_snake-1)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_o:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:  
                if event.key==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_UP:
                    y1_change=-snake_block
                    x1_change=0
                elif event.key==pygame.K_DOWN:
                    y1_change=snake_block
                    x1_change=0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1<0:
            game_close=True
    
        x1+=x1_change
        y1+=y1_change
        dis.fill(yellow)
        pygame.draw.rect(dis,red,[foodx,foody,snake_block,snake_block])
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List)>Length_of_snake:
            del snake_List[0]
        
        for x in snake_List[:-1]:
            if x==snake_head:
                game_close=True

        our_snake(snake_block,snake_List)
        your_score(Length_of_snake-1)

        pygame.display.update()
        
        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0, dis_width-snake_block)/10.0)*10.0
            foody=round(random.randrange(0, dis_height-snake_block)/10.0)*10.0
            Length_of_snake +=1
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()
gameLoop()