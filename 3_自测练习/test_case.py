#!/usr/bin/env python3

from my_solution import merge_sort


# 测试用例
def test_solution():
    origin_list = [1, 7, 3, 5, 4, 2, 8, 9, 6]
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    merge_sort(origin_list)

    assert sorted_list == origin_list
