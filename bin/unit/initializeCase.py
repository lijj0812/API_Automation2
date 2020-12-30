#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time    : 2020/12/10 17:08
# @Author  : Gavin


import yaml

def ini_case(_path, case_file):
    """
    case初始化.yml测试用例
    :param _path: case路径
    :param case_file: case名称
    :return:
    """
    try:
        with open(_path + '/' + case_file + '.yml', 'r', encoding="utf-8") as f:
            project_dict = yaml.load(f)
    except FileNotFoundError:
        with open(_path + '/' + case_file + '.yaml', 'r', encoding="utf-8") as f:
            project_dict = yaml.load(f)
    return project_dict
