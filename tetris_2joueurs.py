
import pygame
from random import randint
class tetris:
    def __init__(self):
        global window,p_j1,p_j2,score_j1,score_j2,font,cl,loop,color,piece_x_j1,piece_y_j1,piece_x_j2,piece_y_j2,piece_list,piece_j1,piece_j2,tick,window_x,window_y
        pygame.init()
        window = pygame.display.set_mode((0,0),flags=pygame.FULLSCREEN )
        pygame.display.set_caption("TETRIS")
        font = pygame.font.Font('freesansbold.ttf', 65)
        cl = pygame.time.Clock()
        pygame.mixer.music.load("music/Tetris_Main_Theme.mp3")
        window_x = pygame.display.Info().current_w
        window_y = pygame.display.Info().current_h
        loop = True
        score_j1 = 0
        score_j2 = 0
        p_j1 = []
        for i in range(22):
            p_j1.append([2,0,0,0,0,0,0,0,0,0,0,2])
        p_j1.append([2,2,2,2,2,2,2,2,2,2,2,2])
        p_j1.append([2,2,2,2,2,2,2,2,2,2,2,2])
        p_j2 = []
        for i in range(22):
            p_j2.append([2,0,0,0,0,0,0,0,0,0,0,2])
        p_j2.append([2,2,2,2,2,2,2,2,2,2,2,2])
        p_j2.append([2,2,2,2,2,2,2,2,2,2,2,2])
        piece_x_j1 = 6
        piece_y_j1 = 0
        piece_x_j2 = 6
        piece_y_j2 = 0
        color = [0,(26,29,125),(212,205,246),(99, 202, 211),
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
        piece_j1 = []
        piece_j2 = []
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
        #piece = piece_list[1]
        piece_j1 = piece_list[randint(0,len(piece_list)-3)]
        piece_j2 = piece_list[randint(0,len(piece_list)-3)]
        tick = 0
        self.draw_j1()
        self.draw_j2()
        pygame.display.update()
        self.mainloop()

    def piece_turn_j1(self,right):
        global piece_j1,p_j1,piece_y_j1,piece_x_j1
        temp_piece = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        if right:
            for i in range(len(piece_j1)):
                for j in range(len(piece_j1[0])):
                    temp_piece[i][j] = piece_j1[len(piece_j1[0])-1-j][i]
            for k in range(len(temp_piece)):
                for m in range(len(temp_piece[0])):
                    if temp_piece[k][m] != 0 and p_j1[k+piece_y_j1][m+piece_x_j1] != 0:
                        return
        piece_j1 = temp_piece

    def piece_turn_j2(self,right):
        global piece_j2,p_j2,piece_y_j2,piece_x_j2
        temp_piece = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        if right:
            for i in range(len(piece_j2)):
                for j in range(len(piece_j2[0])):
                    temp_piece[i][j] = piece_j2[len(piece_j2[0])-1-j][i]
            for k in range(len(temp_piece)):
                for m in range(len(temp_piece[0])):
                    if temp_piece[k][m] != 0 and p_j2[k+piece_y_j2][m+piece_x_j2] != 0:
                        return
        piece_j2 = temp_piece


    def piece_mov(self):
        global piece_y_j1,piece_y_j2,piece_x_j1,piece_x_j2,piece_j1,piece_j2,p_j1,p_j2,piece_list
        for i in range(4):
            for j in range(4):
                if piece_j1[i][j] != 0 and p_j1[piece_y_j1+1+i][piece_x_j1+j] != 0:
                    for k in range(len(piece_j1)):
                        for l in range(len(piece_j1[1])):
                            if piece_j1[k][l] != 0:
                                p_j1[k+piece_y_j1][l+piece_x_j1] = piece_j1[k][l]
                    piece_x_j1,piece_y_j1 = 6,0
                    piece_j1 = piece_list[randint(0,len(piece_list)-3)]
                    piece_j1 = eval(str(piece_j1).replace('1',str(randint(3,9))))
                    for i in range(0,randint(0,3)):
                        self.piece_turn_j1(True)

        for i in range(4):
            for j in range(4):
                if piece_j2[i][j] != 0 and p_j2[piece_y_j2+1+i][piece_x_j2+j] != 0:
                    for k in range(len(piece_j2)):
                        for l in range(len(piece_j2[1])):
                            if piece_j2[k][l] != 0:
                                p_j2[k+piece_y_j2][l+piece_x_j2] = piece_j2[k][l]
                    piece_x_j2,piece_y_j2 = 6,0
                    piece_j2 = piece_list[randint(0,len(piece_list)-3)]
                    piece_j2 = eval(str(piece_j2).replace('1',str(randint(3,9))))
                    for i in range(0,randint(0,3)):
                        self.piece_turn_j2(True)

        return True
    def piece_dep_d_j1(self):
        global piece_j1,piece_x_j1,piece_y_j1,p_j1
        cond = True
        for i in range(4):
            for j in range(4):
                if piece_j1[i][j] != 0 and p_j1[piece_y_j1+i][piece_x_j1+j+1] != 0:
                    cond = False
        if cond:
            piece_x_j1 += 1
            self.draw_j1()
            pygame.display.init()

    def piece_dep_d_j2(self):
        global piece_j2,piece_x_j2,piece_y_j2,p_j2
        cond = True
        for i in range(4):
            for j in range(4):
                if piece_j2[i][j] != 0 and p_j2[piece_y_j2+i][piece_x_j2+j+1] != 0:
                    cond = False
        if cond:
            piece_x_j2 += 1
            self.draw_j2()
            pygame.display.init()

    def piece_dep_g_j1(self):
        global piece_j1,piece_x_j1,piece_y_j1,p_j1
        cond = True
        for i in range(4):
            for j in range(4):
                if piece_j1[i][j] != 0 and p_j1[piece_y_j1+i][piece_x_j1+j-1] != 0:
                    cond = False
        if cond:
            piece_x_j1 -= 1
            self.draw_j1()
            pygame.display.init()

    def piece_dep_g_j2(self):
        global piece_j2,piece_x_j2,piece_y_j2,p_j2
        cond = True
        for i in range(4):
            for j in range(4):
                if piece_j2[i][j] != 0 and p_j2[piece_y_j2+i][piece_x_j2+j-1] != 0:
                    cond = False
        if cond:
            piece_x_j2 -= 1
            self.draw_j2()
            pygame.display.init()

    def check_j1(self):
        global p_j1,score_j1
        for i in range(len(p_j1)-2):
            if str(p_j1[i]).count(', 0,') == 0:
                del p_j1[i]
                p_j1.insert(0,[2,0,0,0,0,0,0,0,0,0,0,2])
                score_j1 += 10
    def check_j2(self):
        global p_j2,score_j2
        for i in range(len(p_j2)-2):
            if str(p_j2[i]).count(', 0,') == 0:
                del p_j2[i]
                p_j2.insert(0,[2,0,0,0,0,0,0,0,0,0,0,2])
                score_j2 += 10

    def draw_j1(self):
        global p_j1,piece_x_j1,piece_y_j1,piece_j1,cl
        pygame.draw.rect(window, (20,20,20), [0, 0, 384,768],0)
        p_f = str(p_j1)
        p_fu = eval(p_f)
        for i in range(len(piece_j1)):
            for j in range(len(piece_j1[1])):
                if piece_j1[i][j] != 0:
                    p_fu[i+piece_y_j1][j+piece_x_j1] = piece_j1[i][j]

        for i in range(len(p_fu)):
            for j in range(len(p_fu[i])):
                '''if p_fu[i][j] == 1:
                    pygame.draw.rect(window, (200,200,200), [j * 32, i * 32, 32-2, 32-2],0)
                elif p_fu[i][j] == 2:
                    pygame.draw.rect(window, (200,20,50), [j * 32, i * 32, 32-2, 32-2],0)'''
                co = p_fu[i][j]
                if co != 0:
                    pygame.draw.rect(window, color[co], [j * 32, i * 32, 32-2, 32-2],0)
                    pygame.draw.rect(window, (color[co][0]-20,color[co][1]-20,color[co][2]-20), [j * 32+6, i * 32+6, 32-10, 32-10],0)

    def draw_j2(self):

        global p_j2,piece_x_j2,piece_y_j2,piece_j2,cl,window_x,window_y
        x_rl = window_x - 32*12
        pygame.draw.rect(window, (20,20,20), [x_rl, 0, 384,768],0)
        p_f = str(p_j2)
        p_fu = eval(p_f)
        for i in range(len(piece_j2)):
            for j in range(len(piece_j2[1])):
                if piece_j2[i][j] != 0:
                    p_fu[i+piece_y_j2][j+piece_x_j2] = piece_j2[i][j]

        for i in range(len(p_fu)):
            for j in range(len(p_fu[i])):
                '''if p_fu[i][j] == 1:
                    pygame.draw.rect(window, (200,200,200), [j * 32, i * 32, 32-2, 32-2],0)
                elif p_fu[i][j] == 2:
                    pygame.draw.rect(window, (200,20,50), [j * 32, i * 32, 32-2, 32-2],0)'''
                co = p_fu[i][j]
                if co != 0:
                    pygame.draw.rect(window, color[co], [x_rl + j * 32, i * 32, 32-2, 32-2],0)
                    pygame.draw.rect(window, (color[co][0]-20,color[co][1]-20,color[co][2]-20), [x_rl +j * 32+6, i * 32+6, 32-10, 32-10],0)



    def mainloop(self):
        global loop,tick,piece_y_j1,piece_y_j2,piece_x_j1,piece_x_j2,cl
        pygame.mixer.music.play(loops=-1, start=0.0)#, fade_ms=10000)
        while loop:
            if tick > 10:
                piece_y_j1 += 1
                piece_y_j2 += 1
                tick = 0
            self.piece_mov()
            #self.piece_mov_j2()
            self.check_j1()
            self.check_j2()
            if str(p_j1[1]).count('0') < 10:
                loop = False
                break
            if str(p_j2[1]).count('0') < 10:
                loop = False
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.unicode == 'p':
                        loop = False
                    #fenetre.set_at((200, 200), color)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT]:
                    self.piece_dep_d_j2()
                if keys[pygame.K_LEFT]:
                    self.piece_dep_g_j2()
                if keys[pygame.K_UP]:
                    self.piece_turn_j2(True)
                if keys[pygame.K_d]:
                    self.piece_dep_d_j1()
                if keys[pygame.K_a]:
                    self.piece_dep_g_j1()
                if keys[pygame.K_w]:
                    self.piece_turn_j1(True)
                '''
                elif keys[pygame.K_DOWN]:
                    while self.piece_mov():
                        piece_y += 1

                elif keys[pygame.K_z]:
                    c = 'haut'
            '''

            self.draw_j1()
            self.draw_j2()
            pygame.display.update()
            tick += 1
            cl.tick(50)

        pygame.mixer.music.stop()
        #pygame.mixer.music.unload()
        fin = font.render("GAME OVER", True, (213,52,134))
        window.blit(fin,(50,50))
        window.blit(font.render("score joueur 1 : " + str(score_j1), True, (213,52,134)),(50,100))
        window.blit(font.render("score joueur 2 : " + str(score_j2), True, (213,52,134)),(50,150))
        pygame.display.update()
        cl.tick(0.2)
        pygame.quit()
tetris()
