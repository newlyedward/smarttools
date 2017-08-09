# -*- coding: utf-8 -*-

"""
功能：对照片按照拍摄时间进行归类
使用方法：将脚本和照片放于同一目录，双击运行脚本即可
作者：冰蓝
"""

import os
import random
import re
import exifread


class ReadFailException(Exception):
    pass


def exif_info(filename):
    try:
        fd = open(filename, 'rb')
    except:
        raise (ReadFailException, "Cannot open file[{}]\n".format(filename))
    data = exifread.process_file(fd)
    if data:
        try:
            t = str(data['EXIF DateTimeOriginal'])
            t = re.sub("[:\s]+", '.', t)
            m = str(data['Image Model'])
            m = re.sub("\s+", '.', m)
            return t, m
        except:
            print('There is no exif info in {}'.format(filename))
            return None


def classify_photos(pathname):
    for root, dirs, files in os.walk(pathname, True):
        print(root)
        # dirs[:] = []
        for file in files:
            filename = os.path.join(root, file)
            f, e = os.path.splitext(filename)
            if e.lower() not in ('.jpg', '.png', '.mp4', '.bmp', '.tiff', '.gif', 'png', '.wmv', '.mov'):
                continue
            info = "文件名: {0} ".format(filename)
            t = ""
            try:
                t, m = exif_info(filename)
            except Exception as e:
                # print(e)
                continue
            info = "{0}拍摄时间：{1} ".format(info, t)
            pwd = pathname + os.sep + t[:7]
            dst = os.path.join(pwd, t + '.' + m + e)

            if dst == filename:
                continue

            if os.path.exists(dst):
                print('{} Photo already handled!--{}'.format(dst, filename))
                if os.path.getsize(dst) == os.path.getsize(filename):
                    os.remove(filename)
                    print('Photo already existed!')
                    continue
                else:
                    dst = os.path.join(pwd, t + '.' + m + str(random.random()) + e)

            if not os.path.exists(pwd):
                os.mkdir(pwd)
            # print(info, dst)
            os.renames(filename, dst)
            # os.remove(filename)


if __name__ == "__main__":
    pathname = r"K:\Photos"
    classify_photos(pathname)
