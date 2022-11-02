from sys import argv
from tile import Tile
from config import TILES, RESOLUTION

def generate_map(map):
    return [[Tile(TILES[tile], colidable =  tile == "red", pos = (j * RESOLUTION, i * RESOLUTION)) for j, tile in enumerate(row)] for i, row in enumerate(map)]




def design_map(filename):
    print(filename)

def main():
    filename = argv[1]
    if not filename.endswith(".py"):
        filename += ".py"
    design_map(filename)

if __name__ == '__main__':
    main()