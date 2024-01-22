"""Boilerplate pygame stuff
"""
import pathlib
import os                                               # Import os to set pygame env vars
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"          # Set pygame env var to hide "Hello" msg
import pygame as pg                                     # This goes AFTER setting pygame env vars


def shutdown() -> None:
    """Clean up whatever needs cleaning up before exiting.

    Do not call shutdown; it is always called automatically when the program exits,
    regardless of why the program exits.
    """
    print("Shutdown")
    pg.quit()                                           # Shutdown all pygame modules
import atexit
atexit.register(shutdown)                               # Auto-shutdown before program exits


#####
# API
#####

class PGG:
    """Global singleton to hold pygame stuff

    Simple example just to test the module is working:

    # Create an instance with OS window size 640x360
    >>> pGG = PGG(640,360)                              # pGG : collection of pygame globals
    >>> print(dir(pGG))                                 # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    ['Clock', 'Debug_Font', 'Debug_font_h', 'Debug_font_w', 'Font', 'Surf',
    '__class__',..., '__weakref__',
    'font_h', 'font_w', 'quit', 'setup', 'surf_h', 'surf_w']

    Clock: at the end of the game loop:

        pGG.Clock.tick(60)

    Get FPS for debug HUD:
    >>> print(f"FPS: {pGG.Clock.get_fps():0.1f}")
    FPS: 0.0

    Font: the base PGG has a font in two sizes: one for "normal" text and one for debug text.
    >>> print(f"Normal font size is: {pGG.font_w} x {pGG.font_h}")
    Normal font size is: 14 x 26
    >>> print(f"Debug font size is: {pGG.Debug_font_w} x {pGG.Debug_font_h}")
    Debug font size is: 7 x 13

    Practical usage is to first create a child class to add application-specific
    functionality, then make an instance of the child class.
    (Then you don't make an instance of PGG as in the examples above.)

    Create a child class to add attributes and methods:

        class GUI(PGG):
            N_grid_lines = 5                            # Add attribute
            def handle_keydown(self,e,kmod) -> None:    # Add method for key events
                if e.key == pg.K_ESCAPE:
                    self.quit = True
                elif e.key == pg.K_q:
                    self.quit = True
                elif e.key == pg.K_n:
                    if(kmod & pg.KMOD_SHIFT):
                        self.N_grid_lines -= 1
                    else:
                        self.N_grid_lines += 1

    Create an instance of the child class with OS window size 640x360:

        gui = GUI(640,360)
    """

    def __init__(self, w, h):
        self.setup(w,h)

    def setup(self, w, h) -> None:
        self.quit = False
        os.environ["PYGAME_BLEND_ALPHA_SDL2"] = "1"     # Use SDL2 alpha blending
        pg.display.init()                               # Init video module
        self.Clock = pg.time.Clock();
        def setup_window(w,h) -> None:
            """Create self.Surf : the main renderer surface

            Example
            -------
            OS_WIN_SCALE = 60
            gui = GUI(
                    w=16*OS_WIN_SCALE,                              # 16*40 = 640
                    h=9*OS_WIN_SCALE)                               #  9*40 = 360
            """
            self.surf_w = w
            self.surf_h = h
            self.Surf = pg.display.set_mode((self.surf_w,self.surf_h)) #  OS window : 640 x 360
        setup_window(w,h)
        def init_font() -> None:
            """Create self.Font, self.Debug_Font, and store the _w, _h for both.

            Store TTFs (for drawing text) in self.Font and self.Debug_Font.
            Store size of self.Font in self.font_w,self.font_h.
            Store size of self.Debug_Font in self.Debug_font_w,self.Debug_font_h.
            """
            pg.font.init()                              # Init TTF fonts module
            this_path = pathlib.Path(__file__).parent   # Path to this script's folder
            _font_path = pathlib.Path('fonts/ProggyClean.ttf')
            font_path = this_path.joinpath(_font_path)  # Absolute path to ProggyClean.ttf
            assert font_path.exists()
            FontSize_SMALL  = 8
            FontSize_NORMAL = 2*FontSize_SMALL
            FontSize_LARGE  = 2*FontSize_NORMAL
            # Store Font, font_w, font_h for drawing text
            self.Font = pg.font.Font(font_path, FontSize_LARGE)
            self.font_w,self.font_h = self.Font.size("a")
            # Store Debug.Font, Debug.font_w, Debug.font_h for drawing debug text
            self.Debug_Font = pg.font.Font(font_path, FontSize_NORMAL)
            self.Debug_font_w,self.Debug_font_h = self.Debug_Font.size("a")
        init_font()

