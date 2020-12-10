#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time    : 2020/12/10 17:09
# @Author  : Gavin


import configparser
import logging

from bin.unit.replaceRandomly import replace_random


def get_relevance_conf(_path):
    """
    读取关联文件配置
    :param _path:
    :return:
    """
    logging.info("初始化关联文件")
    config = configparser.ConfigParser()
    config.read(_path, encoding="utf-8")
    relevance = config["relevance"]
    relevance_conf = dict()
    logging.debug("读取关联文件内容： %s" % relevance.items())
    for key, value in relevance.items():
        relevance_conf[key] = replace_random(value)
    logging.debug("初始化关联的数据：%s" % relevance_conf)
    return relevance_conf


def ini_relevance(_path, file):
    """
    初始化关联文件
    :param _path: 文件路径
    :param file: 文件名称
    :return:
    """
    relevance = get_relevance_conf(_path + '/' + file + '.ini')
    return relevance