from Config import *

class game():
    def __init__(self):
        pygame.init()
        global screen 
        screen = pygame.display.set_mode((1280,720), pygame.FULLSCREEN)#creates pygame window, scales to fullscreen
        self.clock = pygame.time.Clock()#clock object to handle time
    
    def game(self):
        class Bike():
            def __init__(self,team):
                self.team = team
                self.x = 0
                self.y = 0
                self.direction = "up"
                self.rect = self.Spawn()
                self.dead = False
            def Spawn(self):#can also be used for respawning
                self.x = (random.randint(2,10)*100) + 20#rectangle draws from top left, we want to consider coordinates from center
                self.y = (random.randint(5,6)*100) + 20
                for check_spawn in All_Bikes:
                    while (self.x - 20,self.y - 20) == (check_spawn.x - 20,check_spawn.y - 20):
                        self.x = (random.randint(2,10)*100) + 20
                        self.y = (random.randint(1,6)*100) + 20
                return pygame.Rect(self.x - 20,self.y - 20,40,40)

                
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
                screen.blit(self.font.render("{0}".format(self.x),True,(0,0,255)),((self.x+15),(self.y+5)))
                screen.blit(self.font.render("{0}".format(self.y),True,(0,0,255)),((self.x+15),(self.y+15)))

        class Player(Bike):
            def __init__(self,team):
                super().__init__(team)


        class AI_Bike(Bike):
            def __init__(self):
                super().__init__(2)
                self.direction = "down"
                self.targetx = 0
                self.targety = 0
            def Spawn(self):
                self.x = (random.randint(2,10)*100) + 20
                self.y = (random.randint(1,2)*100) + 20
                for check_spawn in All_Bikes:
                    while (self.x - 20,self.y - 20) == (check_spawn.x - 20,check_spawn.y - 20):
                        self.x = (random.randint(2,10)*100) + 20
                        self.y = (random.randint(1,2)*100) + 20
                return pygame.Rect(self.x - 20,self.y - 20,40,40)
                
            def TargetPos(self,player):
                self.targetx = player.x
                self.targety = player.y
                match player.direction:
                    case "up":
                        pass
                    case "down":
                        pass
                    case "left":
                        pass
                    case "right":
                        pass

            def PlayerFacingUp(self,player):
                distance = (player.x - self.x) + (player.y - self.y)
                if player.y > 100:
                    self.targety -= distance
                    path = a-star.main(self.x//40, self.y//40, self.targetx//40, self.targety//40)
                    while self.targety < 60:
                        self.targety += 40
                        path = a-star.main(self.x//40, self.y//40, self.targetx//40, self.targety//40)

                    if 
                



        class Timer():
            def __init__(self):
                self.rect = pygame.Rect(400,0,200,40)
                self.font = pygame.font.SysFont("Sans",18)
                self.time = 0
                self.tick = 0
                self.round = 0
                self.paused = False
            def Display(self):
                screen.blit(self.font.render("Match Time: {0}".format(self.time),True,(0,0,255)),(400,19))
                screen.blit(self.font.render("Current Round: {0}".format(self.round),True,(0,0,255)),(400,0))
            def Time(self):
                self.time = int(self.tick/60)
                self.Display()

        class Score():
            def __init__(self):
                self.rect = pygame.Rect(40,0,200,40)
                self.font = pygame.font.SysFont("Sans",18)
                self.curr_score = 0
                self.hi_score = 0
            def Display(self): #for debugging
                screen.blit(self.font.render("Score: {0}".format(self.curr_score),True,(0,0,255)),(41, 19))
                screen.blit(self.font.render("High Score: {0}".format(self.hi_score),True,(0,0,255)),(41,0))
            def Increase_Score(self,amount):
                self.curr_score += amount
                if self.curr_score < 0:
                    self.curr_score = -1
                if self.curr_score > self.hi_score:
                    self.New_Hi_Score()
                self.Display()
            def New_Hi_Score(self):
                self.hi_score = self.curr_score


        class Wall():
            def __init__(self,pos,length, height):
                Temp_Walls.append(self)
                self.rect = pygame.Rect(pos[0],pos[1],length,height)


        class Trail(Wall):
            def __init__(self, pos, size, parent):
                super().__init__(pos, size, size)
                self.parent = parent

        Walls = []
        Temp_Walls = []
        All_Bikes = []
        player1 = Player(1)
        All_Bikes.append(player1)
        
        def DrawMap():
            Wall((0,0),1280,30)
            Wall((0,690),1280,30)
            Wall((0,0),30,720)
            Wall((1250,0),30,720)

        def PressKey():
            key = pygame.key.get_pressed()
            if key[pygame.K_a] == True:
                player1.direction = "left"
            elif key[pygame.K_d] == True:
                player1.direction = "right"
            elif key[pygame.K_s] == True:
                player1.direction = "down"
            elif key[pygame.K_w] == True:
                player1.direction = "up"
            elif key[pygame.K_p] == True:
                pass
            if player2 in All_Bikes:
                elif key[pygame.K_UP] == True:
                    player2.direction = "up"
                elif key[pygame.K_DOWN] == True:
                    player2.direction = "down"
                elif key[pygame.K_LEFT] == True:
                    player2.direction = "left"
                elif key[pygame.K_RIGHT] == True:
                    player2.direction = "right"



        Scoreboard = Score()
        Match_Timer = Timer()
        game = True
        DrawMap()
        while game:

        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    pygame.quit(); sys.exit()

        
            screen.fill((0,0,0))#remove this line to leave trail

            for trail in Temp_Walls:
                try:
                    if trail.parent.rect.colliderect(trail.rect) == False:
                        Walls.append(trail)
                        Temp_Walls.remove(trail)
                except AttributeError:
                    Walls.append(trail)
                    Temp_Walls.remove(trail)
                    
            for wall in Walls:
                pygame.draw.rect(screen,(0,0,255),wall.rect)
            pygame.draw.rect(screen,(255,0,0),Scoreboard)
            pygame.draw.rect(screen,(255,0,0),Match_Timer)
            
            for check_alive in All_Bikes:
                if check_alive.dead == False:
                    pygame.draw.rect(screen,((255,255,255)),check_alive)
                    check_alive.Display()
            Scoreboard.Display()
            Match_Timer.Time()

            PressKey()
            for bike in All_Bikes:
                match bike.direction:
                    case "up":
                        bike.FaceUp()
                    case "down":
                        bike.FaceDown()
                    case "left":
                        bike.FaceLeft()
                    case "right":
                        bike.FaceRight()

                Trail(((bike.x)+15,(bike.y)+15),10,bike)
                

            self.clock.tick(60)
            if Match_Timer.paused == False:
                Match_Timer.tick += 1
        

            pygame.display.update()
