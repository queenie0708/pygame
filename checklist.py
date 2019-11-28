import sys
import pygame
from pygame.locals import QUIT

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
IMAGEWIDTH = 300
IMAGEHEIGHT = 200
FPS = 60
step_list=["Check MTBF SW version and download","Flash MTBF devices",
"Power on and check flashed device SW","Check Sdcard format","Reboot test system before test start",
"Check system disk space wheter enough, if not, please free it","Check network connection",
"Check use right scripts", "Check config file settings caselist","Check config file settings simcard",
"Check config file settings languagepack","Check config file settings sw version",
"Check referphone connection","check simcard enough money","Check some manual precondition done",
"Check simcard contact removed","Check all sms message deleted","Check port set correctly for Bsim ,Chanel server & armlog",
"Check earpiece and simcard correctly installed"]

def main():
    pygame.init()
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('MTBF checklist')
    head_font = pygame.font.SysFont(None, 30)
    steps = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                steps = steps +1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                   steps = steps -1
                elif event.key == pygame.K_DOWN:
                   steps = steps +1 
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        window_surface.fill((129, 216, 208))
        check_item = step_list[steps]
        title_surface = head_font.render('MTBF Check List', True, (0,0,0))
        text_surface = head_font.render(check_item, True, (255, 255, 255))
        window_surface.blit(title_surface, (10, 10))
        window_surface.blit(text_surface, (50, 50))
        pygame.display.update()
   
if __name__ == '__main__':    
    main()
