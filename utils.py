# -*- coding: utf-8 -*-
import os


def delete_dir(path_name):
    if not os.path.isdir(path_name):
        print("{} is not a dir".format(path_name))
        return False

    dirs = os.listdir(path_name)

    if not dirs:
        os.rmdir(path_name)

        print("移除空目录：" + path_name)
        return True

    "Thumbs.db"
    need_review = False

    for item in dirs:
        subpath = os.path.join(path_name, item)

        if item == "Thumbs.db":
            try:
                os.remove(subpath)
                need_review = True
            except:
                print("Cannot delete file {}".format(subpath))
            continue

        if os.path.isdir(subpath):
            need_review = need_review or delete_dir(subpath)

    if need_review:
        print("Reivew {}".format(path_name))
        return delete_dir(path_name)



chs_arabic_map = {u'零': 0, u'一': 1, u'二': 2, u'三': 3, u'四': 4,
                  u'五': 5, u'六': 6, u'七': 7, u'八': 8, u'九': 9,
                  u'十': 10, u'百': 100, u'千': 10 ** 3, u'万': 10 ** 4,
                  u'〇': 0, u'壹': 1, u'贰': 2, u'叁': 3, u'肆': 4,
                  u'伍': 5, u'陆': 6, u'柒': 7, u'捌': 8, u'玖': 9,
                  u'拾': 10, u'佰': 100, u'仟': 10 ** 3, u'萬': 10 ** 4,
                  u'亿': 10 ** 8, u'億': 10 ** 8, u'幺': 1,
                  u'０': 0, u'１': 1, u'２': 2, u'３': 3, u'４': 4,
                  u'５': 5, u'６': 6, u'７': 7, u'８': 8, u'９': 9}


def chinese2digits(chinese):
    """
    :param chinese: chinese numbers
    :return: digits

    >>> chinese2digits('九')
    9
    >>> chinese2digits('十一')
    11
    >>> chinese2digits('一百二十三')
    123
    >>> chinese2digits('一千二百零三')
    1203
    >>> chinese2digits('一万一千一百零一')
    11101
    >>> chinese2digits('十万零三千六百零九')
    103609
    >>> chinese2digits('一百二十三万四千五百六十七')
    1234567
    >>> chinese2digits('一千一百二十三万四千五百六十七')
    11234567
    >>> chinese2digits('一亿一千一百二十三万四千五百六十七')
    111234567
    >>> chinese2digits('一百零二亿五千零一万零一千零三十八')
    10250011038
    >>> chinese2digits('一千一百一十一亿一千一百二十三万四千五百六十七')
    111111234567
    """

    assert isinstance(chinese, str)

    result = 0
    tmp = 0
    hnd_mln = 0
    for count in range(len(chinese)):
        curr_char = chinese[count]
        curr_digit = chs_arabic_map.get(curr_char, None)
        # meet 「亿」 or 「億」
        if curr_digit == 10 ** 8:
            result = result + tmp
            result = result * curr_digit
            # get result before 「亿」 and store it into hnd_mln
            # reset `result`
            hnd_mln = hnd_mln * 10 ** 8 + result
            result = 0
            tmp = 0
        # meet 「万」 or 「萬」
        elif curr_digit == 10 ** 4:
            result = result + tmp
            result = result * curr_digit
            tmp = 0
        # meet 「十」, 「百」, 「千」 or their traditional version
        elif curr_digit >= 10:
            tmp = 1 if tmp == 0 else tmp
            result = result + curr_digit * tmp
            tmp = 0
        # meet single digit
        elif curr_digit is not None:
            tmp = tmp * 10 + curr_digit
        else:
            return result
    result = result + tmp
    result = result + hnd_mln
    return result

# ---------------------- scientific calculation--------------------------------
def perf_comp_data(func_list, data_list, rep=3, number=1):
    """Function to compare the performance of different functions

    :param func_list: list
        list with function names as string
    :param data_list: list
        list with data set names as strings
    :param rep: int
        number of repetitions of the whole comparison
    :param number: int
        number of executions for every function
    :return:
    """
    from timeit import repeat
    res_list = {}
    for name in enumerate(func_list):
        stmt = name[1] + '(' + data_list[name[0]] + ')'
        setup = "from __main__ import " + name[1] + ',' + data_list[name[0]]
        results = repeat(stmt=stmt, setup=setup, repeat=rep, number=number)
        res_list[name[1]] = sum(results) / rep
    res_sort = sorted(res_list.items(),
                      key=lambda x: x[1])
    for item in res_sort:
        rel = item[1] / res_sort[0][1]
        print('function:' + item[0] + ', av. time sec: %9.5f, ' % item[1] + 'relative: %6.1f' % rel)


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()

    path_name = r"K:\Photos\unhandle"
    delete_dir(path_name)
