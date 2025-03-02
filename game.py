import pyxel
import pygame
import random

############
# Constant #
############

WIDTH = 240
HEIGHT = 180
GAME_STATE = "menu"
SHOT_STATE = "noshot"
RANDOM_RESET = False
METEORTORIGHT = 0
METEORTOLEFT = 227
Y_PLANE = 0
X_SHOT = 22
Y_SHOT = 0
COUNT = 0
COUNT_SPACE_BUTTON = 0
RANDOM_Y_METEOR = [20,80,160]
RANDOM_X_METEOR = [227,220,210]
KILL_COUNT = 0
HEIGHT_METEOR_ONE = []
HEIGHT_METEOR_TWO = []
HEIGHT_METEOR_THREE = []

##############
# Logic Game #
##############
# Code The Game
class App :
    def __init__(self) -> None:
        pygame.mixer.init()
 
        pyxel.init(WIDTH,HEIGHT,fps=30,title="アストロセテリケ",display_scale=4)
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update,self.main_draw)
    
    def update(self) -> None:
        global METEORTOLEFT,METEORTORIGHT,GAME_STATE,Y_PLANE,X_SHOT,Y_SHOT,SHOT_STATE,COUNT_SPACE_BUTTON,RANDOM_RESET,RANDOM_Y_METEOR,RANDOM_X_METEOR,COUNT,KILL_COUNT,HEIGHT_METEOR_ONE,HEIGHT_METEOR_TWO,HEIGHT_METEOR_THREE
        
        if pyxel.btnp(pyxel.KEY_RETURN) :
            GAME_STATE = "game"
            pyxel.mouse(False)

        """Menu And Game State Session"""
        # Menu State Session
        # Code For Meteor Animation Object In Menu State
        if GAME_STATE == "menu" :
            pyxel.mouse(True)
            METEORTORIGHT += 3
            if METEORTORIGHT > 240 :
                METEORTORIGHT = 0
            METEORTOLEFT -= 3
            if METEORTOLEFT < 0 :
                METEORTOLEFT = 227

        # Game State Session
        elif GAME_STATE == "game" :
            COUNT += 1 
            RANDOM_X_METEOR[0] -= 1
            RANDOM_X_METEOR[1] -= 1
            RANDOM_X_METEOR[2] -= 1
            if COUNT == 240 :
                RANDOM_RESET = True
                COUNT = 0

            if KILL_COUNT == 50 :
                KILL_COUNT = 0
                GAME_STATE = "win"

            # Set-Random X And Y Cordinate three Meteor
            if RANDOM_RESET :
                RANDOM_RESET = False
                RANDOM_X_METEOR.clear()
                RANDOM_Y_METEOR.clear()

                for i in range (0,3) :
                    RANDOM_Y_METEOR.append(random.randint(20,160))
                    RANDOM_X_METEOR.append(random.randint(220,240))

            if SHOT_STATE == "shot" :
                X_SHOT += 4
                if X_SHOT > 240 :
                    COUNT_SPACE_BUTTON = 0
                    SHOT_STATE = "noshot"
                    X_SHOT = 22

            if abs(X_SHOT - RANDOM_X_METEOR[0]) <= 5 and abs(Y_SHOT - RANDOM_Y_METEOR[0]) <= 13 :
                RANDOM_Y_METEOR[0] = 200
                KILL_COUNT += 1
            elif abs(X_SHOT - RANDOM_X_METEOR[1]) <= 5 and abs(Y_SHOT - RANDOM_Y_METEOR[1]) <= 13 :
                RANDOM_Y_METEOR[1] = 200
                KILL_COUNT += 1
            elif abs(X_SHOT - RANDOM_X_METEOR[2]) <= 5 and abs(Y_SHOT - RANDOM_Y_METEOR[2]) <= 13 :
                RANDOM_Y_METEOR[2] = 200
                KILL_COUNT += 1

            if pyxel.btnp(pyxel.KEY_Q) :
                GAME_STATE = "menu"
                KILL_COUNT = 0

            if pyxel.btn(pyxel.KEY_DOWN) :
                Y_PLANE += 3
                if Y_PLANE > 156 :
                    Y_PLANE = 156
            
            if pyxel.btn(pyxel.KEY_UP) :
                Y_PLANE -= 3
                if Y_PLANE < 0 :
                    Y_PLANE = 0

            if pyxel.btnp(pyxel.KEY_SPACE):
                COUNT_SPACE_BUTTON += 1
                if COUNT_SPACE_BUTTON == 1 :
                    SHOT_STATE = "shot"
                    Y_SHOT = Y_PLANE
        
        elif GAME_STATE == "win" :
            if pyxel.btnp(pyxel.KEY_Q) :
                GAME_STATE = "menu"
    """Drawing Session"""

    """Main Drawing"""
    def main_draw(self)-> None:
        pyxel.cls(1)

        if GAME_STATE == "menu" :
            self.menu_draw()
            self.meteorToRight_draw()
            self.meteorToLeft_draw()
        
        elif GAME_STATE == "game" :
            self.plane()
            self.meteorOne()
            self.meteorTwo()
            self.meteorThree()
            self.infoKill()
            self.credits()

            if SHOT_STATE == "shot" :
                self.shot()
        
        elif GAME_STATE == "win" :
            self.winGame_draw()
            

    ############
    #  Object  #
    ############

    """Menu"""
    def menu_draw(self)-> None:
        pyxel.text(WIDTH // 2 - 20,HEIGHT // 2 -20,"Astro Strike",pyxel.frame_count % 15)
        pyxel.text(WIDTH // 2 - 35,HEIGHT // 2 ,"Press Enter To Start",7)
    """Game Over"""
    def winGame_draw(self)-> None:
        pyxel.text(WIDTH // 2 - 20,HEIGHT // 2 -20,"You Win ^-^",pyxel.frame_count % 15)
    """Meteor To Right"""
    def meteorToRight_draw(self)-> None:
        pyxel.blt(METEORTORIGHT,20,0,1,17,13,7,0)
    """Meteor To Left"""
    def meteorToLeft_draw(self)-> None:
        pyxel.blt(METEORTOLEFT,160,0,17,17,13,7,0)
    """Plane"""
    def plane(self) -> None:
        pyxel.blt(0,Y_PLANE,0,12,41,22,24,0)
    """Shot"""
    def shot(self)-> None:
        pyxel.blt(X_SHOT,Y_SHOT + 13,0,16,67,1,5,0)
    """Enemy 1"""
    def meteorOne(self) -> None:
        pyxel.blt(RANDOM_X_METEOR[0],RANDOM_Y_METEOR[0],0,17,17,13,7,0)
    """Enemy 2"""
    def meteorTwo(self) -> None:
        pyxel.blt(RANDOM_X_METEOR[1],RANDOM_Y_METEOR[1],0,17,17,13,7,0)
    """Enemy 3"""
    def meteorThree(self) -> None:
        pyxel.blt(RANDOM_X_METEOR[2],RANDOM_Y_METEOR[2],0,17,17,13,7,0)
    
    def infoKill(self) -> None :
        pyxel.text(0,0,f"KILL:{KILL_COUNT}",7)

    def credits(self) -> None :
        pyxel.text(WIDTH // 2 -20,170,"Game By Sanmi",7)

# Run Game
App()
