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

import pygame as pg
from mjg_pygame import PGG

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
    def render_PlotBgnd() -> None:
        w = gui.Surf.get_width()                        # w : OS window width
        h = gui.Surf.get_height()                       # h : OS window height
        #
        # Size the plot area
        margin = 15                                     # margin as a percentage
        pb_w = (1 - margin/100)*w                       # Plot Bgnd WIDTH
        pb_h = (1 - margin/100)*h                       # Plot Bgnd HEIGHT
        #
        # Create the plot area surface
        tex = pg.Surface((pb_w+1,pb_h+1), pg.SRCALPHA)
        #
        # Draw y-axis
        pg.draw.line(tex, (80,80,40), (0,pb_h),(0,0), width=1)
        # Draw x-axis
        pg.draw.line(tex, (80,80,40), (0,pb_h),(pb_w,pb_h), width=1)
        color = (60,60,50)
        grid_pitch = 15
        # Draw vertical grid lines
        sx = 0
        x_pitch = grid_pitch
        while(sx < pb_w):
            sx += x_pitch
            pg.draw.line(tex, color, (sx,pb_h), (sx,0))
        # Draw horizontal grid lines
        y_pitch = grid_pitch
        sy = pb_h - y_pitch
        while(sy > 0):
            pg.draw.line(tex, color, (0,sy), (pb_w,sy))
            sy -= y_pitch
        # for i in range(1,NL+1):
        #     pg.draw.line(tex, "grey", (i*s,0),(i*s,pb_h))
        #     pg.draw.line(tex, "grey", (0,i*s),(pb_w,i*s))
        #
        # Render the plot area in the center of the OS window
        ctr = ((w-pb_w)//2, (h-pb_h)//2)
        gui.Surf.blit(tex,(ctr))
    render_PlotBgnd()
    pg.display.flip()                                   # Present updated drawing to screen
    gui.Clock.tick(60)

