import pygame

pygame.init()
window = pygame.display.set_mode((384,768))
pygame.display.set_caption("TETRIS")
font = pygame.font.Font('freesansbold.ttf', 20)
cl = pygame.time.Clock()
loop = True
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
piece = []
piece_list = [[[0,1,0,0],
         [0,1,0,0],
         [0,1,0,0],
         [0,1,0,0]],
        [[0,0,0,0],
         [1,1,0,0],
         [0,1,1,0],
         [0,0,0,0]],
        [[0,1,0,0],
         [0,1,1,0],
         [0,1,0,0],
         [0,0,0,0]],
        [[0,1,0,0],
         [0,1,0,0],
         [0,1,1,0],
         [0,0,0,0]],
        [[0,0,0,0],
         [0,1,1,0],
         [0,1,1,0],
         [0,0,0,0]],
        [[1,1,1,1],
         [1,0,0,0],
         [1,0,0,0],
         [1,0,0,0]],
        [[1,1,1,1],
         [1,0,0,1],
         [1,0,0,1],
         [1,1,1,1]]]
piece = piece_list[1]

def piece_turn(right):
    global piece
    temp_piece = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    if right:
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                print(len(piece)-1-i,j)
                temp_piece[i][j] = piece[len(piece)-1-i][len(piece[0])-j]
    piece = temp_piece

def piece_mov():
    global piece_x,piece_y,piece,p
    for i in range(4):
        for j in range(4):
            if piece[i][j] != 0 and p[piece_y+1+i][piece_x+j] != 0:
                p[piece_y][piece_x] = 2
                for k in range(len(piece)):
                    for l in range(len(piece[1])):
                        if piece[k][l] == 1:
                            p[k+piece_y][l+piece_x] = 1
                piece_x,piece_y = 6,0
                return

def check():
    global p
    for i in range(len(p)-2):
        if str(p[i]).count('0') == 0:
            del p[i]
            p.insert(0,[2,0,0,0,0,0,0,0,0,0,0,2])

def draw():
    global p,piece_x,piece_y,piece,cl
    pygame.draw.rect(window, (20,20,20), [0, 0, 384,768],0)
    p_f = str(p)
    p_fu = eval(p_f)
    for i in range(len(piece)):
        for j in range(len(piece[1])):
            if piece[i][j]:
                p_fu[i+piece_y][j+piece_x] = 1

    for i in range(len(p_fu)):
        for j in range(len(p_fu[i])):
            #rel_y = i-piece_y
            #rel_x = j-piece_x
            if p_fu[i][j] == 1:# or 0<=rel_y<=3 and 0<=rel_x<=3 and i == piece[rel_y][rel_x]:
                pygame.draw.rect(window, (200,200,200), [j * 32, i * 32, 32-2, 32-2],0)
            elif p_fu[i][j] == 2:
                pygame.draw.rect(window, (200,20,50), [j * 32, i * 32, 32-2, 32-2],0)







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
        for k in range(len(piece)):
            for l in range(len(piece[1])):
                if 0 == 1:
                    pass
    elif keys[pygame.K_LEFT]:
        if p[piece_y][piece_x-1] == 0:
            piece_x -= 1
    '''
    if keys[pygame.K_UP]:
        direction1 = 'haut'
    elif keys[pygame.K_DOWN]:
        direction1 = 'bas'
    elif keys[pygame.K_z]:
        direction1 = 'haut2'
    elif keys[pygame.K_s]:
        direction1 = 'bas2'
    elif keys[pygame.K_d]:
        direction1 = 'droite2'
    elif keys[pygame.K_q]:
        direction1 = 'gauche2'
'''
    piece_mov()
    check()
    piece_y += 1
    draw()
    pygame.display.update()
    cl.tick(8)


pygame.quit()
