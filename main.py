# from UI import MinesweeperApp
from field_gen import field_gen

if __name__ == '__main__':
    fld = field_gen(5, 2)
    for i in fld:
        print(i)
    # MinesweeperApp().run()
