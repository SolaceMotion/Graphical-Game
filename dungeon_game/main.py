import pygame as p
from application import Application
from config import WIDTH, HEIGHT

clock = p.time.Clock()
prev = p.time.get_ticks()

def main() -> None:
    app = Application(WIDTH, HEIGHT, clock)
    app.run()

if __name__ == '__main__':
    main()