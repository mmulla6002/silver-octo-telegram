from CONFIG import *
import MAIN_MENU
import GAME_1P
Main_Menu = MAIN_MENU.Main_Menu()
Game_1P = GAME_1P.Game_1P()
class Menu_1P():
    def __init__(self,screen,clock):
        global screen
        global clock
        self.font = pygame.font.SysFont("Sans", 20)
        self.game_length = 1
        self.diffculty = 1
    def create_buttons(self):
        Back_Button = BUTTON.Button(0,0,100,50,(0,0,0))
        Game_Length_Button = BUTTON.Button(500,350,100,50,(0,0,0))
        Difficulty_Button = BUTTON.Button(500,500,100,50,(0,0,0))
        Play_Button = BUTTON.Button(500,650,100,50,(0,0,0))
    def run(self):
        
        run_menu_1P = True
        while run_menu_1P:
            for event in pygame.event.get():
                if event.type = pygame.QUIT:
                pygame.quit(); sys.exit()
            clock.tick(60)
            screen.fill((0,128,255))
            
            screen.blit(self.font.render("Back to Main Menu",True,(0,0,255)),(1, 1))
            screen.blit(self.font.render("Number of rounds: {0}".format(self.game_length),True,(0,0,255)),(501, 351))
            screen.blit(self.font.render("Number of enemies: {0}".format(self.difficulty),True,(0,0,255)),(501, 501))
            screen.blit(self.font.render("Play Game",True,(0,0,255)),(501, 651))
            if Back_Button:
                run_menu_1P = False
                Main.Menu.run(screen,clock)
            elif Game_Length_Button:
                self.game_length += 1
                if self.game_length > 5:
                    self.game_length -= 5
            elif Difficulty_Button:
                self.difficulty += 1
                if self.difficulty > 3:
                    self.difficulty -= 3
            elif Play_Button:
                run_menu_1P = False
                Game_1P.run(screen, clock, self.game_length, self.difficulty)
            else:
                pygame.display.update()
