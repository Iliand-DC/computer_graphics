import sys
import sdl2.ext
from sdl2 import *
from model.model_2d import *
from camera.camera_2d import *
from shape.axis import *



class MainWindow:
    WIDTH = 1024
    HEIGHT = 1024

    def __init__(self):
        SDL_Init(SDL_INIT_VIDEO)
        self.window = SDL_CreateWindow(b"Computer Graphics", 
                                       SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 
                                       self.WIDTH, self.HEIGHT, 
                                       SDL_WINDOW_SHOWN | SDL_WINDOW_RESIZABLE)

        self.surface = SDL_GetWindowSurface(self.window)
        self.model = Model2D()
        self.camera = Camera2D(self.WIDTH, self.HEIGHT)
        self.axis = Axis()


    def draw_lines(self):
        self.model.add_line(-1, -1, 1, 1, 0xff0000)
        self.model.rotation = 0
        self.redraw_window()


    def redraw_window(self):
        SDL_FillRect(self.surface, None, 0xffffff)
        self.model.draw(self.surface, self.camera)
        self.axis.draw(self.surface, self.camera,
                       self.model.pos_x,
                       self.model.pos_y)
        SDL_UpdateWindowSurface(self.window, self.surface)


if __name__ == "__main__":
    sdl2.ext.init()


    # window = sdl2.ext.Window("Computer Graphics", size = (640, 480))
    # window.show()

    event = SDL_Event()

    main = MainWindow()
    main.draw_lines()

    while True:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if (event.type == SDL_QUIT):
                sys,exit(0)

            main.redraw_window()



