from CONFIG import *
import MENU_1P
import Menu_2P
import MENU_ENDLESS
Menu_1P = MENU_1P.Menu_1P()
Menu_2P = MENU_2P.Menu_2P()
Menu_Endless = MENU_ENDLESS.Menu_Endless()
class Main_Menu():
    def __init__(self,screen,clock):
        global screen
        global clock
        self.font = pygame.font.SysFont("Sans", 20)
    def create_buttons(self):
        Play_1P_Button = BUTTON.Button(500,200,100,50,(0,0,0))
        Play_2P_Button = BUTTON.Button(500,350,100,50,(0,0,0))
        Play_Endless_Button = BUTTON.Button(500,500,100,50,(0,0,0))
        Quit_Button = BUTTON.Button(500,650,100,50,(0,0,0))
    def run(self):
        
        run_main_menu = True
        while run_main_menu:
            for event in pygame.event.get():
                if event.type = pygame.QUIT:
                pygame.quit(); sys.exit()
                
            screen.fill((0,128,255))
            
            screen.blit(self.font.render("1 Player Mode",True,(0,0,255)),(501, 201))
            screen.blit(self.font.render("2 Player Mode",True,(0,0,255)),(501, 351))
            screen.blit(self.font.render("Endless Mode",True,(0,0,255)),(501, 501))
            screen.blit(self.font.render("Quit Game",True,(0,0,255)),(501, 651))
            if Play_1P_Button:
                run_main_menu = False
                Menu_1P.run(screen,clock)
            elif Play_2P_Button:
                run_main_menu = False
                Menu_2P.run((screen,clock)
            elif Play_Endless_Button:
                run_main_menu = False
                Menu_Endless.run((screen,clock)
            elif Quit_Button:
                pygame.quit(); sys.exit()
            clock.tick(60)
            pygame.display.update()
             
