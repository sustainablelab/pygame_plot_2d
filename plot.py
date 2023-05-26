#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
USAGE
-----

$ pydev
(pydev) $ ./plot.py

Or in Vim:

$ pydev
(pydev) $ vim plot.py
Vim shortcut: ;so
"""

from mjg_pygame import *

class GUI(PGG):
    """ PGG : collection of pygame globals"""
    def handle_keydown(self,e,kmod) -> None:
        if e.key == pg.K_ESCAPE:                        # Esc : quit
            self.quit = True
        elif e.key == pg.K_q:                           # q : quit
            self.quit = True
        elif e.key == pg.K_0:                             # 0 : P0 on
            if(kmod & pg.KMOD_SHIFT):
                self.P0 = False
            else:
                self.P0 = True
        elif e.key == pg.K_1:                             # 1 : P1 on
            if(kmod & pg.KMOD_SHIFT):
                self.P1 = False
            else:
                self.P1 = True
        elif e.key == pg.K_2:                             # 2 : P2 on
            if(kmod & pg.KMOD_SHIFT):
                self.P2 = False
            else:
                self.P2 = True

gui = GUI()

while (not gui.quit):
    ####
    # UI
    ####
    kmod = pg.key.get_mods()
    for e in pg.event.get():
        if e.type == pg.QUIT: gui.quit = True
        elif e.type == pg.KEYDOWN: gui.handle_keydown(e,kmod)

    ########
    # RENDER
    ########
    gui.Surf.fill("black")                             # pg.surface.Surface.fill()
    FPS = f"FPS: {gui.Clock.get_fps():0.1f}"
    def render_FPS() -> None:
        tex = gui.Font.render(FPS, True, 'white')
        gui.Surf.blit(tex,(0,0))
    render_FPS()
    pg.display.flip()                                   # Present updated drawing to screen
    gui.Clock.tick(60)

