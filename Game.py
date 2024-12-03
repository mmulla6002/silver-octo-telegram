from Config import *

class game():
    def __init__(self):
        pygame.init()
        global screen 
        screen = pygame.display.set_mode((1280,720), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
    
    def game(self):
        class Bike():
            def __init__(self,x,y):
                self.x = x
                self.y = y
                self.direction = "up"
                self.rect = pygame.Rect(self.x,self.y,40,40)

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

            def move(self,dx,dy):
                self.rect.x += dx
                self.rect.y += dy
                for check_wall in Walls:#Wall collisions
                    if self.rect.colliderect(check_wall.rect):
                        if dx > 0:#dw
                            self.rect.right = check_wall.rect.left
                        if dx < 0:#a
                            self.rect.left = check_wall.rect.right
                        if dy > 0:#s
                            self.rect.bottom = check_wall.rect.top
                        if dy < 0:#w
                            self.rect.top = check_wall.rect.bottom
                        self.x -= dx
                        self.y -= dy
                        Scoreboard.Increase_Score(-10)
        class Player(Bike):
            def __init__(self,x,y):
                super().__init__(x, y)
            def Display(self):
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
            def Display(self):
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
            def __init__(self,pos,size):
                Temp_Walls.append(self)
                self.rect = pygame.Rect(pos[0],pos[1],size,size)


        class Trail(Wall):
            def __init__(self, pos, size, parent):
                super().__init__(pos, size)
                self.parent = parent

        Walls = []
        Temp_Walls = []
        player = Player((random.randint(2,10)*100),(random.randint(4,6)*100))

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
                        Wall((x,y),40)
                    elif column == "L":
                        haha = pygame.Rect(x,y,40,40)
                    x += 40
                y += 40
                x = 0

        def press_key():
            key = pygame.key.get_pressed()
            if key[pygame.K_a] == True:
                player.direction = "left"
            elif key[pygame.K_d] == True:
                player.direction = "right"
            elif key[pygame.K_s] == True:
                player.direction = "down"
            elif key[pygame.K_w] == True:
                player.direction = "up"



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
            pygame.draw.rect(screen,((255,255,255)),player)
            pygame.draw.rect(screen,(255,0,0),Scoreboard)
            pygame.draw.rect(screen,(255,0,0),Match_Timer)
            Scoreboard.Display()
            Match_Timer.Time()

            press_key()

            match player.direction:
                case "up":
                    player.face_up()
                case "down":
                    player.face_down()
                case "left":
                    player.face_left()
                case "right":
                    player.face_right()

            Trail(((player.x)+15,(player.y)+15),10,player)
            player.Display()
            self.clock.tick(60)
            if Match_Timer.paused == False:
                Match_Timer.tick += 1
        

            pygame.display.update()