import os
import re


def not_empty(s):
    return s and s.strip()


def format_comic_name(path_name):
    sep = re.compile("[^a-zA-z0-9]+")
    comic_name = sep.split(path_name.title())
    return '.'.join(list(filter(not_empty, comic_name)))

common_used_numerals_tmp ={'零':0, '一':1, '二':2, '两':2, '三':3, '四':4, '五':5, '六':6, '七':7,

def format_season_name(comic, season):
    pattern = re.compile("(?<='第')\w+(?='季')", re.I)
    m = pattern.search(season).group()

    pass


def format_file_name(file_name):
    pass


def rename(tv_path='.'):
    files = os.listdir(tv_path)

    for file in files:

        filename = os.path.join(tv_path, file)
        if os.path.isdir(filename):
            # rename the dir
            rename(filename)

        elif os.path.isfile(filename):
            # os.renames(old, new) 方法用于递归重命名目录或文件。类似rename()。
            #  new --文件或目录的新名字。甚至可以是包含在目录中的文件，或者完整的目录树。

            # rename the file
            # 1st dir name : words joined by '.'

            # 2nd dir-name.seasonxx
            # '第05季', '第1季', 'Season 2'

            # 3rd file name.Sxx.Exx.subname.extension, if only one number change two at least 2 digits.
            # only renames file with extension '.mp4, .mkv, .avi' last '.'as extension
            # sep = '-', '_', '.', ' '
            # delete words like '[xxxx], 720p, 1080p, (2012)'
            #
            pass

        else:
            print('{} is not a file or dir'.format(filename))



'''
Little.Charmers.S01E01.Prince.Not.So.Charming.-.A.Charming.Outfit.720p.mp4
Bing_S01E01_Fireworks.mp4
Everythings_Rosie_S01E01_How_To_Hide_An_Oak_Tree.avi
01.mkv
4.mp4
11.mkv.baiduyun.downloading
[洪恩小乌龟学美语].Franklin.-.hurry.up,franklin.avi
Tumble.Leaf.S01E03.Beat.of.the.Drumsticks.-.Springy.Surprise[www.lxwc.com.cn].mp4
Little.Charmers.S01E21.Somewhere.Over.the.Rainbow.-.Circus.Surprise.720p.WEBRip.x264.AAC.mp4
07_Franklin_s_Masterpiece.avi
Little.Charley.Bear.S01E01.10Jan2011.avi

Mickey.Mouse.Clubhouse.S04E08.Minnie's.Pet.Salon.720p.mp4
Mickey.Mouse.Clubhouse.S04E08.Minnie's.Pet.Salon.720p.srt

Little.Charley.Bear.S01E10-teddy-on-a-string.srt
Little.Charley.Bear.S01E10.21Jan2011.avi

105.avi
02.mpg
1105.avi
'''
