import sys
import sdl2.ext
from sdl2 import *
from model.model_2d import *
from camera.camera_2d import *
from shape.axis import *
from graphics.graphics import *


from math import sin



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


        x = []
        y = []
        for i in range(-10, 11):
            x.append(float(i/10))
            y.append(self.function(float(i/10)))


        self.graphics = Graphics(self.model, x, y, 0x0000ff)
        self.graphics.create_graphic()


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


    def function(self, x):
        return x**2



class Application:
    def run(self):
        try:
            sdl2.ext.init()


            # window = sdl2.ext.Window("Computer Graphics", size = (640, 480))
            # window.show()

            event = SDL_Event()

            main = MainWindow()
            main.draw_lines()

            mouse_dragging = False


            while True:
                while SDL_PollEvent(ctypes.byref(event)) != 0:
                    if event.type == SDL_MOUSEBUTTONDOWN:
                        mouse_dragging = True
                        last_mouse_x = event.button.x
                        last_mouse_y = event.button.y


                    elif event.type == SDL_MOUSEBUTTONUP:
                        mouse_dragging = False


                    elif event.type == SDL_MOUSEMOTION and mouse_dragging:
                        delta_x = event.motion.x - last_mouse_x
                        delta_y = event.motion.y - last_mouse_y

                        main.camera.move(-delta_x, -delta_y)

                        last_mouse_x = event.motion.x
                        last_mouse_y = event.motion.y

                    elif event.type == SDL_QUIT:
                        sys.exit(0)

                    main.redraw_window()

        except Exception as err:
            print(err)



if __name__ == "__main__":
    app = Application()
    app.run()


