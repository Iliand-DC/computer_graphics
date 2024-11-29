import sys
import sdl2.ext
from sdl2 import *
from model.model_2d import *
from camera.camera_2d import *
from shape.axis import *
from graphics.graphics import *


from math import sin, cos, sqrt, pi, exp, log


class Function:

    @staticmethod
    def function(x):
        """ lognormal distribution
        """
        NU = -1
        SIGMA = 2
        return 1 / (x * SIGMA * sqrt(2 * pi)) * exp(- ((log(x) - NU) ** 2) / 2 * SIGMA**2)

    @staticmethod
    def func2(x):
        return x**2


    @staticmethod
    def func3(x):
        return x**3


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


        self.create_x_array(1, 100)
        self.y = self.get_y(Function.function)


        graphic1 = Graphics(self.model, self.x, self.y, 0x0000ff)
        graphic1.create_graphic()


        self.create_x_array(-100, 100)
        self.y = self.get_y(Function.func2)
        graphic2 = Graphics(self.model, self.x, self.y, 0xff0000)
        graphic2.create_graphic()


        self.y = self.get_y(Function.func3)
        graphic3 = Graphics(self.model, self.x, self.y, 0x00ff00)
        graphic3.create_graphic()


    def redraw_window(self):
        SDL_FillRect(self.surface, None, 0xffffff)
        self.model.draw(self.surface, self.camera)
        self.axis.draw(self.surface, self.camera,
                       self.model.pos_x,
                       self.model.pos_y)
        SDL_UpdateWindowSurface(self.window, self.surface)


    def create_x_array(self, start, stop):
        self.x = [float(i/100) for i in range(start, stop + 1)]


    def get_y(self, function):
        result = []
        for i in self.x:
            result.append(-function(i))

        return result



class Application:
    def run(self):
        try:
            sdl2.ext.init()

            event = SDL_Event()

            main = MainWindow()
            main.redraw_window()

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


                    elif event.type == SDL_MOUSEWHEEL:
                        zoom = 1.1 if event.wheel.y > 0 else 0.9
                        main.camera.zoom = main.camera.zoom * zoom


                    elif event.type == SDL_KEYDOWN:
                        if event.key.keysym.sym == SDLK_q:
                            main.model.rotate(5)

                        elif event.key.keysym.sym == SDLK_r:
                            main.model.rotate(-5)


                    main.redraw_window()

        except Exception as err:
            print(err)



if __name__ == "__main__":
    app = Application()
    app.run()


