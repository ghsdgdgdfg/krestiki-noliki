import time
import pygame
import asyncio
pygame.init()

WIDTH = 1800
HEIGHT = 860
FPS = 60

screen = pygame.display.set_mode((0,0))
clock = pygame.time.Clock()
BG = (90, 150, 150)

placed = []
for i in range(9):
    placed.append([pygame.Rect(175*(i//3)+500,175*(i%3)+250,150,150),"пусто"])
xod = "ходят крестики"

def win():
    global placed,xod,text_lus
    check_win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in check_win:
        if placed [i[0]][1] == placed [i[1]][1] == placed [i[2]][1] !="пусто":
            print("победили:",placed [i[0]][1])
            time.sleep(2)
            placed = []
            for i in range(9):
                placed.append([pygame.Rect(175*(i//3)+500,175*(i%3)+250,150,150),"пусто"])
                xod = "ходят крестики"
                text_lus = font2.render("ХОДЯТ КРЕСТИКИ",True , "#ff0000")
            return
            
    for i in placed:
        if i [1] == "пусто":
            return
        
    print("ничья")
    time.sleep(2)
    placed = []
    for i in range(9):
        placed.append([pygame.Rect(175*(i//3)+500,175*(i%3)+250,150,150),"пусто"])
        xod = "ходят крестики"
        text_lus = font2.render("ХОДЯТ КРЕСТИКИ",True , "#ff0000")

font2 = pygame.font.SysFont(None,100)
text_lus = font2.render("ХОДЯТ КРЕСТИКИ",True , "#ff0000")

async def main():

    while True:
        clock.tick(FPS)

        screen.fill(BG)
        screen.blit(text_lus,(400,150))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    maus = pygame.mouse.get_pos()
                    for i in range(9):
                        if placed[i][0].collidepoint(maus):
                            if xod == "ходят крестики":
                                if placed[i][1] == "пусто":
                                    text_lus = font2.render("ХОДЯТ НОЛИКИ",True , "#006aff")
                                    placed[i][1] = "крестик"
                                    xod = "ходят нолики"
                            elif xod == "ходят нолики":
                                if placed[i][1] == "пусто":
                                    placed[i][1] = "нолик"
                                    xod = "ходят крестики"
                                    text_lus = font2.render("ХОДЯТ КРЕСТИКИ",True , "#ff0000")


            if event.type == pygame.QUIT:
                pygame.quit()

        for i in placed:
            pygame.draw.rect(screen,(255,0,0),i[0])
            if i[1]=="крестик":
                pygame.draw.line(screen,(255,90,200),i[0].topleft,i[0].bottomright,10)
                pygame.draw.line(screen,(100,90,200),i[0].topright,i[0].bottomleft,10)
            if i[1]=="нолик":
                pygame.draw.circle(screen,(180,50,190),i[0].center,60,10)

        pygame.display.update()
        await asyncio.sleep(0)
        win()
asyncio.run(main())
#                                 & "C:\Users\Ваня\AppData\Local\Programs\Python\Python310\python.exe" d:/payton/KRESTIKI_NOLIKI.py