# -*- coding:utf-8 -*-
#!/usr/bin/env python3


# 将两个列表是s1，s2按顺序融合为一个列表s,s为原列表
def merge(s1, s2, s):
    # j和i就相当于两个指向的位置，i指s1，j指s2
    i = j = 0
    while i+j < len(s):
        # j==len(s2)时说明s2走完了，或者s1没走完并且s1中该位置是最小的,将没走完的列表里的数直接赋值到s里
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1


# 合并排序
def merge_sort(s):

    n = len(s)

    # 当只剩一个元素或没有元素时，该序列不在需要进行排序，直接返回。
    # merge_sort函数在此处到达递归的尽头，递归从此处开始返回。
    if n < 2:
        return

    # 拆分子序列
    mid = n // 2

    s1 = s[0:mid]
    s2 = s[mid:n]

    # 递归调用合并排序函数对子序列进行排序
    merge_sort(s1)
    merge_sort(s2)

    # 合并
    merge(s1, s2, s)


if __name__ == '__main__':
    s = [1, 7, 3, 5, 4, 2, 8, 9]

    print(f'origin list: {s}')
    merge_sort(s)
    print(f'sorted : {s}')
