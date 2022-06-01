import pygame
from random import randint
pygame.init()
#window_size = pygame.display.get_desktop_sizes()[0]
#window = pygame.display.set_mode((384,window_size[1]))#768
window = pygame.display.set_mode((384,768),flags=pygame.FULLSCREEN )
pygame.display.set_caption("TETRIS")
font = pygame.font.Font('freesansbold.ttf', 20)
cl = pygame.time.Clock()
pygame.mixer.music.load("music/Tetris_Main_Theme.mp3")
window_size = pygame.display.get_window_size()
print(window_size)
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
color = [0,(26,29,125),(212,205,246),
        (99, 202, 211),
        (68, 90, 163),
        (235, 174, 56),
        (234, 231, 66),
        (95, 188, 82),
        (140, 93, 165),
        (187, 52, 45),
        (50,50,50),
        (120,37,179),
        (45,94,56),
        (255,20,31),
        (31,234,32),
        (42,32,247),
        (234,235,21),
        (234,35,214),
        (23,235,21),
        (125,142,111)]
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
piece = piece_list[randint(0,len(piece_list)-3)]

def piece_turn(right):
    global piece,p,piece_y,piece_x
    temp_piece = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    if right:
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                temp_piece[i][j] = piece[len(piece[0])-1-j][i]
        for k in range(len(temp_piece)):
            for m in range(len(temp_piece[0])):
                if temp_piece[k][m] != 0 and p[k+piece_y][m+piece_x] != 0:
                    return
    piece = temp_piece


def piece_mov():
    global piece_x,piece_y,piece,p,piece_list
    for i in range(4):
        for j in range(4):
            if piece[i][j] != 0 and p[piece_y+1+i][piece_x+j] != 0:
                for k in range(len(piece)):
                    for l in range(len(piece[1])):
                        if piece[k][l] != 0:
                            p[k+piece_y][l+piece_x] = piece[k][l]
                piece_x,piece_y = 6,0
                piece = piece_list[randint(0,len(piece_list)-3)]
                piece = eval(str(piece).replace('1',str(randint(3,9))))
                for i in range(0,randint(0,3)):
                    piece_turn(True)
                return False
    return True
def piece_dep_d():
    global piece,piece_x,piece_y,p
    cond = True
    for i in range(4):
        for j in range(4):
            if piece[i][j] != 0 and p[piece_y+i][piece_x+j+1] != 0:
                cond = False
    if cond:
        piece_x += 1

def piece_dep_g():
    global piece,piece_x,piece_y,p
    cond = True
    for i in range(4):
        for j in range(4):
            if piece[i][j] != 0 and p[piece_y+i][piece_x+j-1] != 0:
                cond = False
    if cond:
        piece_x -= 1

def check():
    global p
    for i in range(len(p)-2):
        if str(p[i]).count(', 0,') == 0:
            del p[i]
            p.insert(0,[2,0,0,0,0,0,0,0,0,0,0,2])

def draw():
    global p,piece_x,piece_y,piece,cl
    pygame.draw.rect(window, (20,20,20), [0, 0, 384,768],0)
    p_f = str(p)
    p_fu = eval(p_f)
    for i in range(len(piece)):
        for j in range(len(piece[1])):
            if piece[i][j] != 0:
                p_fu[i+piece_y][j+piece_x] = piece[i][j]

    for i in range(len(p_fu)):
        for j in range(len(p_fu[i])):
            '''if p_fu[i][j] == 1:
                pygame.draw.rect(window, (200,200,200), [j * 32, i * 32, 32-2, 32-2],0)
            elif p_fu[i][j] == 2:
                pygame.draw.rect(window, (200,20,50), [j * 32, i * 32, 32-2, 32-2],0)'''
            co = p_fu[i][j]
            if co != 0:
                pygame.draw.rect(window, color[co], [j * 32, i * 32, 32-2, 32-2],0)

def draw_menu():
    pass






draw()
pygame.mixer.music.play(loops=-1, start=0.0)#, fade_ms=10000)
while loop==True:
    piece_y += 1
    piece_mov()
    check()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                loop = False
            #fenetre.set_at((200, 200), color)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            piece_dep_d()
            """if p[piece_y][piece_x+1] == 0:
                piece_x += 1
            for k in range(len(piece)):
                for l in range(len(piece[1])):
                    if 0 == 1:
                        pass"""
        if keys[pygame.K_LEFT]:
            piece_dep_g()
        if keys[pygame.K_UP]:
            piece_turn(True)
        if str(p[1]).count('0') < 10:
            loop = False
            break
        elif keys[pygame.K_DOWN]:
            while piece_mov():
                piece_y += 1
            '''
        elif keys[pygame.K_z]:
            direction1 = 'haut2'
    '''

    draw()
    pygame.display.update()
    cl.tick(8)

pygame.mixer.music.stop()
#pygame.mixer.music.unload()
pygame.quit()
