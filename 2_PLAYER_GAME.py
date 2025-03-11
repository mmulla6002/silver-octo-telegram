from Config import *
class 2_Player_Game():
    def __init__(self):
        self.active = False
        
    def run(self):
        Walls = GAME.Walls
        Temp_Walls = GAME.Temp_Walls
        All_Players = GAME.All_Players
        player1 = GAME.Player(1) #pass in 1 for player 1, 2 for player 2
        All_Players.append(player1)
        player2 = GAME.Player(2)
        Scoreboard = GAME.Score()
        Match_Timer = GAME.Timer()
        GAME.DrawMap()
        Match_Timer.paused = True
        if Match_Timer.paused == False:
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
            
            for check_alive in All_Players:#only draw players that havent been eliminated
                if check_alive.dead == False:
                    pygame.draw.rect(screen,((255,255,255)),check_alive)
                    check_alive.Display()
                    
            Scoreboard.Display()
            Match_Timer.Time()

            GAME.PressKey()
            
            for person in All_Players:
                if person.x % 40 == 0 and person.y % 40 ==0:#update direction if at a junction
                    person.direction = person.next
                match person.direction:
                    case "up":
                        person.FaceUp()
                    case "down":
                        person.FaceDown()
                    case "left":
                        person.FaceLeft()
                    case "right":
                        person.FaceRight()

                if person.x % 10 == 0 and person.y % 10 == 0 and person.dead == False:#trail draws
                    Trail(((person.x)+15,(person.y)+15),10,person)
                
                
            if Match_Timer.paused == False:#match timer will not continue to tick when game is paused
                Match_Timer.tick += 1
        
    def close(): #closing the file, emptying lists and variables, making sure nothing is being drawn on the screeen, etc.
        Walls = []
        Temp_Walls = []
        All_Players = []
        self.active = False
