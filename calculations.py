from general.config import get_config

config = get_config()

def pixel_to_tile(x: int, y: int) -> tuple[int, int]:
    return x, y

def tile_to_pixel(x: int, y: int) -> tuple[int, int]:
    X_0 = config.WINDOW_WIDTH // 2 - config.TILE_SIZE // 2 * config.SCALE
    Y_0 = config.TILE_SIZE * 2

    x *= config.SCALE
    y *= config.SCALE

    return X_0 + x * config.TILE_SIZE // 2 - y * config.TILE_SIZE // 2 , Y_0 + x * config.TILE_SIZE // 4 + y * config.TILE_SIZE // 4