# -*- coding:utf-8 -*-
#!/usr/bin/env python3


# 将两个列表是s1，s2按顺序融合为一个列表s,s为原列表
def merge(s1, s2, s):
    # j和i就相当于两个指向的位置，i指s1，j指s2
    raise NotImplementedError("请实现此函数")


# 合并排序
def merge_sort(s):

    n = len(s)

    # 当只剩一个元素或没有元素时，该序列不在需要进行排序，直接返回。
    # merge_sort函数在此处到达递归的尽头，递归从此处开始返回。
    if n < 2:
        return

    # 拆分子序列
    raise NotImplementedError('请补全代码块')

    # 递归调用合并排序函数对子序列进行排序
    raise NotImplementedError('请补全代码块')

    # 合并
    merge(s1, s2, s)


if __name__ == '__main__':
    pass
