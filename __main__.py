from general.config import get_config
from general.logger import init_logger
from logging import getLogger
import pyray as pr
from engine import Engine

config = get_config()
init_logger(config.LOG_LEVEL, config.LOG_FILE, config.CONSOLE_ENABLED)
logger = getLogger(__name__)

def main():
    pr.init_window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT, config.WINDOW_NAME)
    engine = Engine()
    engine.load_textures()
    while not pr.window_should_close():
        pr.begin_drawing()
        engine.render()
        pr.end_drawing()
    pr.close_window()

if __name__ == "__main__":
    main()