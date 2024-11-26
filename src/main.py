import sys
import sdl2.ext


if __name__ == "__main__":
    sdl2.ext.init()

    window = sdl2.ext.Window("Computer Graphics", size = (640, 480))
    window.show()

    processor = sdl2.ext.TestEventProcessor()
    processor.run(window)
    sdl2.ext.quit()
