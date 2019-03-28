from field_gen import field_gen
import config
from UI import MinesweeperApp

if __name__ == '__main__':
    config.field = field_gen(config.size)
    MinesweeperApp().run()
