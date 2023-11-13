import pyray as pr
from tiles import Tile
from buildings import Building

class Engine:

    grass_texture: pr.Texture
    mine_texture: pr.Texture

    grass_tiles: list[Tile]
    mine: Building


    def load_textures(self):
        self.grass_texture = pr.load_texture("sprites/tile_grass.png")
        self.mine_texture = pr.load_texture("sprites/building_mine.png")
        self.grass_tiles = [Tile(self.grass_texture, x, y) for x in range(10) for y in range(10)]
        self.mine = Building(self.mine_texture, 4, 4)


    def render(self):
        pr.clear_background(pr.WHITE)
        for grass in self.grass_tiles:
            grass.draw()
        self.mine.draw()