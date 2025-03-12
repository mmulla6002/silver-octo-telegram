###MOVE ALL CLASSES OUT OF RUN()
###REMOVE WHILE LOOP, DISPLAY UPDATE AND CLOCK AS ALREADY ACTIVE IN MAIN
import pygame
import MAIN


class Character():
    def __init__(self,team):
        self.team = team
        self.x = 0
        self.y = 0
        self.direction = "up"
        self.next = "up"#buffer inputs since can only turn at junctions
        self.rect = self.Spawn()
        self.dead = False
    def Spawn(self):#can also be used for respawning
        self.x = (random.randint(2,10)*100)
        self.y = (random.randint(5,6)*100)
        for check_spawn in All_Players:
            while (self.x,self.y) == (check_spawn.x,check_spawn.y):
                self.x = (random.randint(2,10)*100)
                self.y = (random.randint(1,6)*100)
        return pygame.Rect(self.x,self.y,40,40)

                
    def FaceUp(self):
        self.Move(0,-2)
        self.y -= 2
    def FaceDown(self):
        self.Move(0,2)
        self.y += 2
    def FaceLeft(self):
        self.Move(-2,0)
        self.x -= 2
    def FaceRight(self):
        self.Move(2,0)
        self.x += 2
    def Death(self):
        pass
                
    def Move(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
        for check_wall in Walls:#Wall collisions
            if self.rect.colliderect(check_wall.rect):
                self.Death()
                        
    def Display(self):#for debugging
        self.font = pygame.font.SysFont("Sans",8)
        Main.screen.blit(self.font.render("{0}".format(self.x),True,(0,0,255)),((self.x+15),(self.y+5)))
        Main.screen.blit(self.font.render("{0}".format(self.y),True,(0,0,255)),((self.x+15),(self.y+15)))

class Player(Character):
    def __init__(self,team):
        super().__init__(team)


class AI_Player(Character):
    def __init__(self):
        super().__init__(2)
        self.direction = "down"
        self.targetx = 0
        self.targety = 0
    def Spawn(self):
        self.x = (random.randint(2,10)*100)
        self.y = (random.randint(1,2)*100)
        for check_spawn in All_Players:
            while (self.x,self.y) == (check_spawn.x,check_spawn.y):
                self.x = (random.randint(2,10)*100)
                self.y = (random.randint(1,2)*100)
        return pygame.Rect(self.x,self.y,40,40)
    def SetTarget(self,vector_x,vector_y):
        self.targetx = self.x + vector_x
        self.targety = self.y + vector_y
    def CalculateTarget(self,player):
        if (abs(player.x - self.x) < 80) and (abs(player.y - self.y) < 80):
            self.CloseEncounter()
        path = a-star.main(self.x//40, self.y//40, player.x//40, player.y//40)
        if path == None:
            self.Retreat()
        vector_x = (player.x - self.x)
        vector_y = (player.y - self.y)
        self.SetTarget(vector_x,vector_y)
                
        while self.targetx > 1240 or self.targetx < 0:
            vector_x -= (vector_x/(vector_x + (abs(1240 - self.targetx))))
            self.SetTarget(vector_x,vector_y)
                    
        while self.targety > 680 or self.targety < 0:
            vector_y -= (vector_y/(vector_y + (abs(680 - self.targety))))
            self.SetTarget(vector_x,vector_y)
                    
        if player.y > 100:
            path = a-star.main(self.x//40, self.y//40, self.targetx//40, self.targety//40)
            while self.targety < 60:
                self.targety += 40
                path = a-star.main(self.x//40, self.y//40, self.targetx//40, self.targety//40)

            if 
                



class Timer():
    def __init__(self):
        self.rect = pygame.Rect(500,0,200,30)
        self.font = pygame.font.SysFont("Sans",18)
        self.time = 0
        self.tick = 0
        self.round = 0
        self.paused = False
    def Display(self):#displays match time and current round
        Main.screen.blit(self.font.render("Match Time: {0}".format(self.time),True,(0,0,255)),(400,19))
        Main.screen.blit(self.font.render("Current Round: {0}".format(self.round),True,(0,0,255)),(400,0))
    def Time(self):Calculates time to show on Display
        self.time = int(self.tick/60)
        self.Display()

class Score():
    def __init__(self):
        self.rect = pygame.Rect(150,0,200,30)
        self.font = pygame.font.SysFont("Sans",18)
        self.curr_score = 0
    def Display(self):
        MAIN.screen.blit(self.font.render("Score: {0}".format(self.curr_score),True,(0,0,255)),(41, 19))
        
class Score_Endless(Score):
    def __init__(self):
        super().__init__()
        self.hi_score = 0
    def Display(self):
        super().Display(self)
        MAIN.screen.blit(self.font.render("High Score: {0}".format(self.hi_score),True,(0,0,255)),(41,0))
    def Increase_Score(self,amount):
        self.curr_score += amount
        if self.curr_score < 0:
            self.curr_score = 0
        if self.curr_score > self.hi_score:
            self.New_Hi_Score()
    def New_Hi_Score(self):
        self.hi_score = self.curr_score

class Score_Multiplayer(Score):
    def __init__(self):
        super().__init__()
        self.t1_score = 0
        self.t2_score = 0
        self.curr_score = "0:0"
    def T1_Win(self):
        self.t1_score += 1
        self.Set_Curr_Score()
    def T2_Win(self):
        self.t2_score += 1
        self.Set_Curr_Score()
    def Set_Curr_Score(self):
        self.curr_score = (str(self.t1_score)+":"+str(self.t2_score))

class Wall(): #create wall object
    def __init__(self,pos,length, height):
        Temp_Walls.append(self)
        self.parent = None #walls do not have a parent
        self.rect = pygame.Rect(pos[0],pos[1],length,height)


class Trail(Wall): #create trail object
    def __init__(self, pos, size, parent):
        super().__init__(pos, size, size)
        self.parent = parent #parent is used to keep track of who created the trail

        
def DrawMap(): #Border walls
    Wall((0,0),1280,30)
    Wall((0,690),1280,30)
    Wall((0,0),30,720)
    Wall((1250,0),30,720)

def PressKey():#Handles all keyboard inputs
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:#player 1 left
        player1.next = "left"
    elif key[pygame.K_d]:#player 1 right
        player1.next = "right"
    elif key[pygame.K_s]:#player 1 down
        player1.next = "down"
    elif key[pygame.K_w]:#player 1 up
        player1.next = "up"
    if key[pygame.K_p] or key[pygame.K_ESCAPE]:#pause game
        pass
    if 2_PLAYER_GAME.active == True:#enable player 2 inputs if in 2P
        if key[pygame.K_UP]:
            player2.next = "up"
        elif key[pygame.K_DOWN]:
            player2.next = "down"
        elif key[pygame.K_LEFT]:
            player2.next = "left"
        elif key[pygame.K_RIGHT]:
            player2.next = "right"


Walls = []
Temp_Walls = []
All_Players = []
