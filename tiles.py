import pyray as pr
from calculations import tile_to_pixel
from general.config import get_config

config = get_config()

class Tile:
    def __init__(self, texture: pr.Texture, x: int, y: int) -> None:
        self.texture = texture
        self.x = x
        self.y = y
    
    def draw(self) -> None:
        pr.draw_texture_ex(self.texture, tile_to_pixel(self.x, self.y), 0, config.SCALE, pr.WHITE)