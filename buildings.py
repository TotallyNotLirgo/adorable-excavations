import pyray as pr
from calculations import tile_to_pixel
from general.config import get_config

config = get_config()

class Building:
    def __init__(self, texture: pr.Texture, x: int, y: int) -> None:
        self.texture = texture
        self.x = x
        self.y = y
    
    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def draw(self) -> None:
        x, y = tile_to_pixel(self.x, self.y)
        pr.draw_texture_ex(self.texture, [x - config.SCALE * config.TILE_SIZE // 2, y - config.SCALE * config.TILE_SIZE // 4 * 3], 0, config.SCALE, pr.WHITE)