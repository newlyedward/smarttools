# -*- coding: utf-8 -*-
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
    comic = '''Curious.George
        Curious.George
        Curious.George
        Curious.George
        Curious.George
        Curious.George
        Curious.George'''.splitlines()

    comic = list(map(str.strip, comic))

    origin = '''Curious George - Season 1（40集）(缺4和7集）
        第二季
        Littlest Pet Shop (2012) - Season 2 1080p
        第1季
        加菲猫和朋友们第7季
        Mr Men show1
        第06季'''.splitlines()

    origin = list(map(str.strip, origin))

    formated = '''Curious.George.S01
        Curious.George.S02
        Curious.George.S02
        Curious.George.S01
        Curious.George.S07
        Curious.George.S01
        Curious.George.S06'''.splitlines()

    formated = list(map(str.strip, formated))

    transfered = map(format_season_name, comic, origin)

    for t, f in zip(transfered, formated):
        assert t == f


def test_format_file_name():
    # Test case 1
    comic = "Curious.George"
    season = "Curious.George.S04"
    origin = "Little.Charmers.S01E01.Prince.Not.So.Charming.-.A.Charming.Outfit.720p.mp4"
    formated = "Curious.George.S04E01.Prince.Not.So.Charming.-.A.Charming.Outfit.mp4"

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 2
    origin = "Bing_S01E01_Fireworks.mp4"
    season = ""
    formated = "Curious.George.S01E01.Fireworks.mp4"

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 3
    origin = "Everythings_Rosie_S01E01_How_To_Hide_An_Oak_Tree.avi"
    season = ""
    formated = "Curious.George.S01E01.How.To.Hide.An.Oak.Tree.avi"

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 4
    origin = "01.mkv"
    season = ""
    formated = "Curious.George.S01E01.mkv"

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 5
    origin = "4.mp4"
    season = ""
    formated = "Curious.George.S01E04.mp4"

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 6
    origin = "11.mkv.baiduyun.downloading"
    season = "Curious.George.S01"
    formated = ""

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 7
    origin = "[洪恩小乌龟学美语].Franklin.-.hurry.up,franklin.avi"
    season = "Curious.George.S01"
    formated = ""

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 8
    origin = "Tumble.Leaf.S01E03.Beat.of.the.Drumsticks.-.Springy.Surprise[www.lxwc.com.cn].mp4"
    season = ""
    formated = "Curious.George.S01E03.Beat.Of.The.Drumsticks.-.Springy.Surprise.mp4"

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 9
    origin = "Little.Charmers.S01E21.Somewhere.Over.the.Rainbow.-.Circus.Surprise.720p.WEBRip.x264.AAC.mp4"
    season = ""
    formated = "Curious.George.S01E21.Somewhere.Over.The.Rainbow.-.Circus.Surprise.mp4"

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 10
    origin = "07_Franklin_s_Masterpiece.avi"
    season = ""
    formated = "Curious.George.S01E07.Franklin.S.Masterpiece.avi"

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 11
    origin = "Little.Charley.Bear.S01E01.10Jan2011.avi"
    season = ""
    formated = ""

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 12
    origin = "Mickey.Mouse.Clubhouse.S04E08.Minnie's.Pet.Salon.720p.srt"
    season = ""
    formated = "Curious.George.S04E08.Minnie'S.Pet.Salon.srt"

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 13
    origin = "Little.Charley.Bear.S01E10-teddy-on-a-string.srt"
    season = ""
    formated = "Curious.George.S01E10.Teddy.On.A.String.srt"

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 14
    origin = "105.avi"
    season = ""
    formated = "Curious.George.S01E05.avi"

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 15
    origin = "1105.avi"
    season = ""
    formated = "Curious.George.S11E05.avi"

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

    # Test case 15
    origin = "02.mpg"
    season = ""
    formated = "Curious.George.S01E02.mpg"

    transfered = format_file_name(origin, comic, season)

    assert transfered == formated

