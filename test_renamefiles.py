from renamefiles import *


def test_format_comic_name():
    origin = '''Everythings.Rosie
                    Little Charmers梦幻魔法师
                    Franklin
                     tumble leaf飘零叶'''.splitlines()

    formated = '''Everythings.Rosie
                      Little.Charmers
                      Franklin
                      Tumble.Leaf'''.splitlines()

    formated = list(map(str.strip, formated))

    transfered = map(format_comic_name, origin)

    for t, f in zip(transfered, formated):
        assert t == f


def test_format_season_name():
    comic = '''
        Curious.George
        Curious.George
        Curious.George
        Curious.George
        Curious.George
        '''

    origin = '''
        Curious George - Season 1（40集）(缺4和7集）
        第二季
        Littlest Pet Shop (2012) - Season 2 1080p
        第1季
        第01季
        '''.splitlines()

    origin = list(map(str.strip, origin))

    formated = '''
        Curious.George.S01
        Curious.George.S02
        Curious.George.S02
        Curious.George.S01
        Curious.George.S01
        '''.splitlines()

    formated = list(map(str.strip, formated))

    transfered = map(format_season_name, comic, origin)

    for t, f in zip(transfered, formated):
        assert t == f
