from Config import *

class Game():
    def __init__(self, screen, clock, game_length):
        global screen
        global clock
        self.game_length = game_length
    
    def run(self):
        class Player():
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
                for check_spawn in All_Bikes:
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
                screen.blit(self.font.render("{0}".format(self.x),True,(0,0,255)),((self.x+15),(self.y+5)))
                screen.blit(self.font.render("{0}".format(self.y),True,(0,0,255)),((self.x+15),(self.y+15)))


        class Timer():
            def __init__(self):
                self.rect = pygame.Rect(400,0,200,40)
                self.font = pygame.font.SysFont("Sans",18)
                self.time = 0
                self.tick = 0
                self.round = 0
                self.paused = False
            def Display(self):#displays match time and current round
                screen.blit(self.font.render("Match Time: {0}".format(self.time),True,(0,0,255)),(400,19))
                screen.blit(self.font.render("Current Round: {0}".format(self.round),True,(0,0,255)),(400,0))
            def Time(self):Calculates time to show on Display
                self.time = int(self.tick/60)
                self.Display()

        class Score():
            def __init__(self):
                self.rect = pygame.Rect(40,0,200,40)
                self.font = pygame.font.SysFont("Sans",18)
                self.T1_Score = 0
                self.T2_Score = 0
                self.curr_score ="0:0"
            def Display(self):
                screen.blit(self.font.render("Score: {0}".format(self.curr_score),True,(0,0,255)),(41, 0))
            def T1_Win(self):
                self.T1_Score += 1
                self.Update_Score()
            def T2_Win(self):
                self.T2_Score += 1
                self.Update_Score()
            def Update_Score(self):
                self.curr_score = (str(self.T1_Score) + ":" + (str(self.T2_Score)))


        class Wall(): #create wall object
            def __init__(self,pos,length, height):
                Temp_Walls.append(self)
                self.parent = None #walls do not have a parent
                self.rect = pygame.Rect(pos[0],pos[1],length,height)


        class Trail(Wall): #create trail object
            def __init__(self, pos, size, parent):
                super().__init__(pos, size, size)
                self.parent = parent #parent is used to keep track of which bike created the trail

        Walls = []
        Temp_Walls = []
        All_Players = []
        player1 = Player(1) #pass in 1 for player 1, 2 for player 2
        player2 = Player(2)
        All_Players.append(player1)
        All_Players.append(player2)
        
        def DrawMap(): #Border walls
            Wall((0,0),1280,30)
            Wall((0,690),1280,30)
            Wall((0,0),30,720)
            Wall((1250,0),30,720)

        def PressKey():#Handles all keyboard inputs
            key = pygame.key.get_pressed()
            if key[pygame.K_a] and player1.direction != "right":#player 1 left
                player1.next = "left"
            elif key[pygame.K_d] and player1.direction != "left":#player 1 right
                player1.next = "right"
            elif key[pygame.K_s] and player1.direction != "up":#player 1 down
                player1.next = "down"
            elif key[pygame.K_w] and player1.direction != "down":#player 1 up
                player1.next = "up"
            if key[pygame.K_p] or key[pygame.K_ESCAPE]:#pause game
                pass
            if key[pygame.K_UP] and player2.direction != "down":
                player2.next = "up"
            elif key[pygame.K_DOWN] and player2.direction != "up":
                player2.next = "down"
            elif key[pygame.K_LEFT] and player2.direction != "right":
                player2.next = "left"
            elif key[pygame.K_RIGHT] and player2.direction != "left":
                player2.next = "right"


        #game starts here
        Scoreboard = Score()
        Match_Timer = Timer()
        game = True
        DrawMap()
        while game:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    pygame.quit(); sys.exit()

            screen.fill((0,0,0))
            clock.tick(60)#game's internal timer is limited to 60fps to avoid the game running faster on more powerful computers
            if Match_Timer.paused == False:#match timer will not continue to tick when game is paused
                Match_Timer.tick += 1
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
            
                for check_alive in All_Bikes:#only draw bikes that havent been eliminated
                    if check_alive.dead == False:
                        pygame.draw.rect(screen,((255,255,255)),check_alive)
                        check_alive.Display()
                    
                Scoreboard.Display()
                Match_Timer.Time()

                PressKey()
            
                for bike in All_Bikes:
                    if bike.x % 40 == 0 and bike.y % 40 ==0:#update direction if at a junction
                        bike.direction = bike.next
                    match bike.direction:
                        case "up":
                            bike.FaceUp()
                        case "down":
                            bike.FaceDown()
                        case "left":
                            bike.FaceLeft()
                        case "right":
                            bike.FaceRight()

                    if bike.x % 10 == 0 and bike.y % 10 == 0:#trail draws
                        Trail(((bike.x)+15,(bike.y)+15),10,bike)
                
                
        

            pygame.display.update()
