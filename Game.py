from Config import *

class game():
    def __init__(self):
        pygame.init()
        global screen 
        screen = pygame.display.set_mode((1280,720), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
    
    def game(self):
        class Bike():
            def __init__(self,team):
                self.team = team
                self.x = 0
                self.y = 0
                self.direction = "up"
                self.rect = self.spawn()
                self.dead = False
            def spawn(self):
                self.x = (random.randint(2,10)*100)
                self.y = (random.randint(1,6)*100)
                for check_spawn in All_Bikes:
                    while (self.x,self.y) == (check_spawn.x,check_spawn.y):
                        self.x = (random.randint(2,10)*100)
                        self.y = (random.randint(1,6)*100)
                return pygame.Rect(self.x,self.y,40,40)

                
            def face_up(self):
                self.move(0,-3)
                self.y -= 3
            def face_down(self):
                self.move(0,3)
                self.y += 3
            def face_left(self):
                self.move(-3,0)
                self.x -= 3
            def face_right(self):
                self.move(3,0)
                self.x += 3
            def death(self):
                pass
                
            def move(self,dx,dy):
                self.rect.x += dx
                self.rect.y += dy
                for check_wall in Walls:#Wall collisions
                    if self.rect.colliderect(check_wall.rect):
                        self.death()
                        
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
        
        def draw_map():
            map = [
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "W                              W",
                "W                              W",
                "W  L                           W",
                "W                              W",
                "W                              W",
                "W                              W",
                "W                              W",
                "W                              W",
                "W                              W",
                "W                              W",
                "W                              W",
                "W                              W",
                "W                              W",
                "W                              W",
                "W                              W",
                "W                              W",
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            ]

            x = 0
            y = 0
            for row in map:
                for column in row:
                    if column == "W":
                        Wall((x,y),40,40)
                    elif column == "L":
                        haha = pygame.Rect(x,y,40,40)
                    x += 40
                y += 40
                x = 0

        def press_key():
            key = pygame.key.get_pressed()
            if key[pygame.K_a] == True:
                player1.direction = "left"
            elif key[pygame.K_d] == True:
                player1.direction = "right"
            elif key[pygame.K_s] == True:
                player1.direction = "down"
            elif key[pygame.K_w] == True:
                player1.direction = "up"



        Scoreboard = Score()
        Match_Timer = Timer()
        game = True
        draw_map()
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

            press_key()
            for bike in All_Bikes:
                match bike.direction:
                    case "up":
                        bike.face_up()
                    case "down":
                        bike.face_down()
                    case "left":
                        bike.face_left()
                    case "right":
                        bike.face_right()

                Trail(((bike.x)+15,(bike.y)+15),10,bike)
                

            self.clock.tick(60)
            if Match_Timer.paused == False:
                Match_Timer.tick += 1
        

            pygame.display.update()
