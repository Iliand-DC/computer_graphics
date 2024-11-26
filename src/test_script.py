from sdl2 import *;
import sys;
import ctypes;

SDL_Init(SDL_INIT_VIDEO);
win = SDL_CreateWindow(b"test",
        SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
        640, 480, 0);
surf = SDL_GetWindowSurface(win);

# get pointer to pixels as uint32[]
u32_pixels = ctypes.cast(surf[0].pixels, ctypes.POINTER(ctypes.c_uint32));
# get surface width
width = surf[0].w;

# main loop
while True:
    # process events, exit if window is closed
    # (spinning event loop is a must, even if you don't react to events)
    ev = SDL_Event();
    while(SDL_PollEvent(ev)):
        if(ev.type == SDL_QUIT):
            sys.exit(0);

    # clear surface
    SDL_FillRect(surf, None, 0);

    # draw diagonal line
    for i in range(0, 480):
        u32_pixels[i*width+i] = 0xffffffff;

    # signal SDL that surface is ready to be presented on screen
    SDL_UpdateWindowSurface(win, surf);
