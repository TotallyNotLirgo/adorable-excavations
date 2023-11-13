import pyray as pr
from calculations import tile_to_pixel
from general.config import get_config

config = get_config()

class Tile:
    def __init__(self, texture: pr.Texture, x: int, y: int) -> None:
        self.texture = texture
        self.x = x
        self.y = y
        self.indented = False
        self.offset_y = 0
    
    def draw(self) -> None:
        position = list(tile_to_pixel(self.x, self.y))
        position[1] -= self.offset_y
        pr.draw_texture_ex(self.texture, position, 0, config.SCALE, pr.WHITE)
    
    def indent(self):
        if not self.indented:
            self.offset_y -= config.SCALE * config.TILE_SIZE // 8
        self.indented = True
    
    def outdent(self):
        if self.indented:
            self.offset_y += config.SCALE * config.TILE_SIZE // 8
        self.indented = False