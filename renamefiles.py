# -*- coding: utf-8 -*-
import os
import re
from utils import chinese2digits


def not_empty(s):
    return s and s.strip()


def format_comic_name(path_name):
    sep = re.compile("[^a-zA-z0-9]+")
    comic_name = sep.split(path_name.title())
    return '.'.join(list(filter(not_empty, comic_name)))


def format_season_name(comic, season):
    pattern = re.compile("(?<=第)\w+(?=季)|(?<=season)\s*\d+|(?<=show)\s*\d+", re.I)

    try:
        m = pattern.search(season).group().strip()
    except AttributeError as e:
        print(e)

    assert len(m) <= 2

    if m.isdigit():
        return "{}.S{:02d}".format(comic, int(m))
    elif m.isnumeric():
        m = chinese2digits(m)
        return "{}.S{:02d}".format(comic, m)
    else:
        print('Get wrong season name!')
        return None


def format_file_name(file, comic, season=''):
    extension = ['.mkv', '.mp4', '.avi', '.mpg', '.srt']
    ext = os.path.splitext(file)[1].lower()

    # only handle video file
    if ext.lower() not in extension:
        return ''

    # delete extra words and captial the first letter
    pattern = re.compile("720p|1080p|WEBRip|x264|AAC|\[.+?\]|\(.+?\)", re.I)
    file = pattern.sub('', file).title()

    # get num in the str
    num = re.findall("\d+", file)

    # extension includes num, delete the last num in the list num
    if re.search("\d", ext):
        num.pop()

    length = len(num)

    if length not in [1, 2]:
        return ''

    if season:
        if length == 1:
            e = num[0]
        else:
            e = num[1]

        prefix = "{}E{:02d}".format(season, int(e) % 100)

    else:
        if length == 1:
            digit = int(num[0])
            if digit < 100:
                s = 1
                e = digit
            elif digit < 10000:
                s = int(digit / 100)
                e = digit % 100
            else:
                print('Season number {:d} is too big'.format(digit))
                return ''
        else:
            s = int(num[0])
            e = int(num[1]) % 100

        prefix = "{}.S{:02d}E{:02d}".format(comic, s, e)

    if file[:-4].isdigit():
        return prefix + ext

    if length > 1:
        pattern = num[1]
    else:
        pattern = num[0]

    postfix = re.split(pattern, file)[-1]

    if len(re.findall("-", postfix)) == 1:
        sep = re.compile('[\s_.]+')
    else:
        sep = re.compile("[-\s_.]+")

    postfix = list(filter(not_empty, sep.split(postfix)))
    postfix[-1] = postfix[-1].lower()
    postfix = '.'.join(postfix)

    return prefix + '.' + postfix


def rename(tv_path='.'):
    comics = os.listdir(tv_path)

    for comic in comics:

        comic_name = os.path.join(tv_path, comic)

        assert os.path.isdir(comic_name):
            # rename the dir
            rename(comic_name)

        elif os.path.isfile(comic_name):
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
            print('{} is not a file or dir'.format(comic_name))
