from CONFIG import *
import MAIN_MENU
import GAME_ENDLESS
Main_Menu = MAIN_MENU.Main_Menu()
Game_Endless = GAME_ENDLESS.Game_Endless()
class Menu_Endless():
    def __init__(self,screen,clock):
        global screen
        global clock
        self.font = pygame.font.SysFont("Sans", 20)
        self.diffculty = 1
    def create_buttons(self):
        Back_Button = BUTTON.Button(0,0,100,50,(0,0,0))
        Difficulty_Button = BUTTON.Button(500,350,100,50,(0,0,0))
        Play_Button = BUTTON.Button(500,650,100,50,(0,0,0))
    def run(self):
        
        run_menu_endless = True
        while run_menu_endless:
            for event in pygame.event.get():
                if event.type = pygame.QUIT:
                pygame.quit(); sys.exit()
            clock.tick(60)
            screen.fill((0,128,255))
            
            screen.blit(self.font.render("Back to Main Menu",True,(0,0,255)),(1, 1))
            screen.blit(self.font.render("Number of enemies: {0}".format(self.difficulty),True,(0,0,255)),(501, 351))
            screen.blit(self.font.render("Play Game",True,(0,0,255)),(501, 651))
            if Back_Button:
                run_menu_endless = False
                Main.Menu.run(screen,clock)
            elif Difficulty_Button:
                self.difficulty += 1
                if self.difficulty > 3:
                    self.difficulty -= 3
            elif Play_Button:
                run_menu_endless = False
                Game_Endless.run(screen, clock, self.difficulty)
            else:
                pygame.display.update()
