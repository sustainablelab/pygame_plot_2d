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

Keyboard controls
-----------------

N : increase number of grid lines
Shift+N : decrease number of grid lines
"""

import pygame as pg
from mjg_pygame import PGG
import mjg_calc
import mjg_plot

class GUI(PGG):
    """ PGG : collection of pygame globals"""
    N_grid_lines = 5                                   # N x N grid lines
    def handle_keydown(self,e,kmod) -> None:
        if e.key == pg.K_ESCAPE:                        # Esc : quit
            self.quit = True
        elif e.key == pg.K_q:                           # q : quit
            self.quit = True
        elif e.key == pg.K_n:                           # N_grid_lines
            if(kmod & pg.KMOD_SHIFT):
                self.N_grid_lines -= 1                  # N : less grid lines
            else:
                self.N_grid_lines += 1                  # n : more grid lines

OS_WIN_SCALE = 60
gui = GUI(
        w=16*OS_WIN_SCALE,                              # 16*40 = 640
        h=9*OS_WIN_SCALE)                               #  9*40 = 360

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
    debug_vars = f"N = {gui.N_grid_lines:0.1f}"
    def render_FPS() -> None:
        tex = gui.Font.render(FPS, True, 'white')
        gui.Surf.blit(tex,(0,0))
    render_FPS()
    def render_debug_vars() -> None:
        tex = gui.Font.render(debug_vars, True, 'white')
        gui.Surf.blit(tex,(0,gui.font_h))
    render_debug_vars()
    def render_PlotBgnd() -> None:
        # Create plot grid lines
        hlines,vlines = mjg_plot.create_grid_lines(gui.N_grid_lines)
        #
        # Plot size (percentage of OS window)
        size = 0.90                                     # Fraction of OS window (0:1)
        assert size > 0
        assert size < 1
        #
        # Get size of OS window
        w = gui.Surf.get_width()                        # w : OS window width
        h = gui.Surf.get_height()                       # h : OS window height
        #
        # Size the plot area
        pb_w = w*size
        pb_h = h*size
        #
        # Create the plot area surface
        # Why +1 to w and h? Otherwise the x-axis and right-hand y-axis are clipped.
        tex = pg.Surface((pb_w+1,pb_h+1), pg.SRCALPHA)
        #
        # Draw grid lines
        color = (60,60,50)
        for line in hlines:
            start = mjg_calc.normxy_to_window((pb_w, pb_h), line[0])
            end = mjg_calc.normxy_to_window((pb_w, pb_h), line[1])
            pg.draw.line(tex, color, start, end)
        for line in vlines:
            start = mjg_calc.normxy_to_window((pb_w, pb_h), line[0])
            end = mjg_calc.normxy_to_window((pb_w, pb_h), line[1])
            pg.draw.line(tex, color, start, end)
        #
        # Render the plot area in the center of the OS window
        ctr = ((w-pb_w)//2, (h-pb_h)//2)
        gui.Surf.blit(tex,(ctr))

    render_PlotBgnd()
    pg.display.flip()                                   # Present updated drawing to screen
    gui.Clock.tick(60)

