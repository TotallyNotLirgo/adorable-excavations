import pyray as pr
from tiles import Tile
from buildings import Building
from logging import getLogger
from calculations import pixel_to_tile
from general.config import get_config

logger = getLogger(__name__)
config = get_config()

class Engine:
    grass_texture: pr.Texture
    mine_texture: pr.Texture

    grass_tiles: list[Tile]
    mine: Building


    def load_textures(self):
        self.grass_texture = pr.load_texture("sprites/tile_grass.png")
        self.mine_texture = pr.load_texture("sprites/building_mine.png")
        self.grass_tiles = [Tile(self.grass_texture, x, y) for x in range(10) for y in range(10)]
        self.indentation_map = [-1] * 4
        self.mine = Building(self.mine_texture, 4, 4)


    def render(self):
        pr.clear_background(pr.WHITE)
        for grass in self.grass_tiles:
            grass.draw()
        self.mine.draw()
        mouse = pr.get_mouse_position()
        tile = pixel_to_tile(int(mouse.x), int(mouse.y - config.TILE_SIZE * config.SCALE // 4))
        if(pr.is_mouse_button_pressed(0)) and 0 <= tile[0] < 9 and 0 <= tile[1] < 9:
            self.mine.set_position(*tile)
        mouse_delta = pr.get_mouse_delta()
        if mouse_delta.x == 0 and mouse_delta.y == 0:
            return
        for tile_index in self.indentation_map:
            if tile_index != -1:
                self.grass_tiles[tile_index].outdent()
        tile_indexes = [(tile[0] + offset_x) * 10 + (tile[1] + offset_y) for offset_x in range(2) for offset_y in range(2)]
        if 0 <= tile[0] < 9 and 0 <= tile[1] < 9:
            for i, tile_index in enumerate(tile_indexes):
                self.grass_tiles[tile_index].indent()
                self.indentation_map[i] = tile_index