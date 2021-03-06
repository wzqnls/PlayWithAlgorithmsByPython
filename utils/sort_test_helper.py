#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 21:09
# @Author  : Lee
# @File    : sort_test_helper.py
# @Software: PyCharm

import random
from datetime import datetime


class SortTestHelper(object):

    @staticmethod
    def generate_random_list(length, start, end):
        lists = [int(random.random() * (end + 1 - start)) for i in range(length)]
        return lists

    @staticmethod
    def generate_near_ordered_list(length, swap_times):
        lists = [i for i in range(length)]
        for i in range(swap_times):
            num1 = int(random.random() * len(lists))
            num2 = int(random.random() * len(lists))
            lists[num1], lists[num2] = lists[num2], lists[num1]
        return lists

    @staticmethod
    def is_sorted(lists):
        for i in range(len(lists) - 1):
            return False if lists[i] > lists[i + 1] else True

    @classmethod
    def test_sort(cls, class_name, lists):
        start_time = datetime.now()
        class_name.sort(lists)
        end_time = datetime.now()
        spend_time = end_time - start_time
        if cls.is_sorted(lists):
            print(class_name.__name__ + ": " + str(spend_time.total_seconds()) + ' s\n')
        else:
            print("Sorting failed, please check your fucking code!")
