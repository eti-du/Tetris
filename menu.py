import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((0,0),flags=pygame.FULLSCREEN )
pygame.display.set_caption("TETRIS")
font = pygame.font.Font('freesansbold.ttf', 200)
font2 = pygame.font.Font('freesansbold.ttf', 70)
cl = pygame.time.Clock()
window_x = pygame.display.Info().current_w
window_y = pygame.display.Info().current_h
print(window_x,window_y)
loop = True
color = [0,(26,29,125),(212,205,246),(99, 202, 211),(68, 90, 163),(235, 174, 56),(234, 231, 66),
        (95, 188, 82),(140, 93, 165),(187, 52, 45),(50,50,50),(120,37,179),(45,94,56),
        (255,20,31),(31,234,32),(42,32,247),(234,235,21),(234,35,214),(23,235,21),(125,142,111)]

pygame.draw.rect(window, (30,30,30), [0, 0, 30, 30],0)
pygame.draw.rect(window, (184, 100, 80), [0, 0, window_x, window_y] ,0)

window.blit(font.render("TETRIS", True, (113,52,134)),(window_x//2-350,window_y//2-300))
window.blit(font2.render("1 joueur", True, (134,152,14)),(window_x//2-200,window_y//2+100))
window.blit(font2.render("2 joueur", True, (13,152,134)),(window_x//2-200,window_y//2+200))

pygame.display.update()
cl.tick(5)
select = 0
selecte = 1
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                loop = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            select -= 1
            selecte = 0
            window.blit(font2.render("1 joueur", True, (13,152,134)),(window_x//2-200,window_y//2+100))
            window.blit(font2.render("2 joueur", True, (134,152,14)),(window_x//2-200,window_y//2+200))
            pygame.display.update()
        elif keys[pygame.K_UP]:
            select += 1
            selecte = 1
            window.blit(font2.render("1 joueur", True, (134,152,14)),(window_x//2-200,window_y//2+100))
            window.blit(font2.render("2 joueur", True, (13,152,134)),(window_x//2-200,window_y//2+200))
            pygame.display.update()
        elif keys[pygame.K_RETURN]:
            loop = False
    cl.tick(50)

if selecte == 1:
    from tetris import tetris
elif selecte == 0:
    from tetris_2joueurs import tetris
    #tetris()
pygame.quit()

