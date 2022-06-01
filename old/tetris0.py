import pygame

pygame.init()
window = pygame.display.set_mode((384,768))
pygame.display.set_caption("TETRIS")
font = pygame.font.Font('freesansbold.ttf', 20)
cl = pygame.time.Clock()
loop=True
p = [[2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2]]
piece_x = 6
piece_y = 0
def piece_slot() :
    global piece_x,piece_y
    if p[piece_y+1][piece_x] != 0:
        p[piece_y][piece_x] = 1
        piece_x,piece_y = 6,0

def draw():
    global p,piece_x,piece_y
    pygame.draw.rect(window, (20,20,20), [0, 0, 384,768],0)
    for i in range(len(p)):
        for j in range(len(p[i])):
            if p[i][j] == 1 or i == piece_y and j == piece_x:
                pygame.draw.rect(window, (200,200,200), [j * 32, i * 32, 32-1, 32-1],0)
            elif p[i][j] == 2:
                pygame.draw.rect(window, (200,20,50), [j * 32, i * 32, 32-1, 32-1],0)







draw()

while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                loop = False
            #fenetre.set_at((200, 200), color)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if p[piece_y][piece_x+1] == 0:
            piece_x += 1
    elif keys[pygame.K_LEFT]:
        if p[piece_y][piece_x-1] == 0:
            piece_x -= 1
    '''
    if keys[pygame.K_UP]:    #est-ce la touche UP
        direction1 = 'haut'
    elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
        direction1 = 'bas'
    elif keys[pygame.K_z]:    #est-ce la touche UP
        direction1 = 'haut2'
    elif keys[pygame.K_s]:  #est-ce la touche DOWN
        direction1 = 'bas2'
    elif keys[pygame.K_d]:  #est-ce la touche RIGHT
        direction1 = 'droite2'
    elif keys[pygame.K_q]:  #est-ce la touche LEFT
        direction1 = 'gauche2'
'''
    piece_slot()
    piece_y += 1
    draw()
    cl.tick(8)

    pygame.display.update()
pygame.quit()