###MOVE ALL CLASSES OUT OF RUN()
###REMOVE WHILE LOOP, DISPLAY UPDATE AND CLOCK AS ALREADY ACTIVE IN MAIN

from Config import *
import MAIN
class game():
    def __init__(self):
        self.active = False
        
    def run(self):
        class Bike():
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
                Main.screen.blit(self.font.render("{0}".format(self.x),True,(0,0,255)),((self.x+15),(self.y+5)))
                Main.screen.blit(self.font.render("{0}".format(self.y),True,(0,0,255)),((self.x+15),(self.y+15)))

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
                self.x = (random.randint(2,10)*100)
                self.y = (random.randint(1,2)*100)
                for check_spawn in All_Bikes:
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
                    continue
                path = a-star.main(self.x//40, self.y//40, player.x//40, player.y//40)
                if path == None:
                    self.Retreat()
                    continue
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
                self.rect = pygame.Rect(400,0,200,40)
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
                self.rect = pygame.Rect(40,0,200,40)
                self.font = pygame.font.SysFont("Sans",18)
                self.curr_score = 0
                self.hi_score = 0
            def Display(self):
                Main.screen.blit(self.font.render("Score: {0}".format(self.curr_score),True,(0,0,255)),(41, 19))
                Main.screen.blit(self.font.render("High Score: {0}".format(self.hi_score),True,(0,0,255)),(41,0))
            def Increase_Score(self,amount):
                self.curr_score += amount
                if self.curr_score < 0:
                    self.curr_score = 0
                if self.curr_score > self.hi_score:
                    self.New_Hi_Score()
                self.Display()
            def New_Hi_Score(self):
                self.hi_score = self.curr_score


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
        All_Bikes = []
        player1 = Player(1) #pass in 1 for player 1, 2 for player 2
        All_Bikes.append(player1)
        
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
            if player2 in All_Bikes:#enable player 2 inputs if in 2P
                elif key[pygame.K_UP]:
                    player2.next = "up"
                elif key[pygame.K_DOWN]:
                    player2.next = "down"
                elif key[pygame.K_LEFT]:
                    player2.next = "left"
                elif key[pygame.K_RIGHT]:
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

            Main.screen.fill((0,0,0))

            for trail in Temp_Walls:
                try:
                    if trail.parent.rect.colliderect(trail.rect) == False:
                        Walls.append(trail)
                        Temp_Walls.remove(trail)
                        if ((trail.x - 15) % 40) == 0 and ((trail.y - 15) % 40) == 0:
                            a-star.maze[trail.y // 40][trail.x // 40] = 1
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
                
                

            Main.clock.tick(60)#game's internal timer is limited to 60fps to avoid the game running faster on more powerful computers
            if Match_Timer.paused == False:#match timer will not continue to tick when game is paused
                Match_Timer.tick += 1
        

            pygame.display.update()
