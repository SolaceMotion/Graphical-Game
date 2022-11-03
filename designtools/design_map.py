from sys import argv
from tile import Tile
from config import TILES, RESOLUTION, WIDTH, HEIGHT
from application import Application

def generate_map(map):
    return [[Tile(TILES[tile], colidable = True, pos = (j * RESOLUTION, i * RESOLUTION)) for j, tile in enumerate(row)] for i, row in enumerate(map)]

def design_map(filename):
    app = Application(WIDTH, HEIGHT, filename)
    app.run()
    print(filename)

def main():
    filename = argv[1]
    if not filename.endswith(".py"):
        filename += ".py"
    design_map(filename)

if __name__ == '__main__':
    main()