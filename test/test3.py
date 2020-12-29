#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time    : 2020/12/29 14:38
# @Author  : Gavin

import pytest
import allure

@allure.feature("myfirst allure")
def test_one():
    print("hello pytest")
    assert 1<2

if __name__ =='__main__':
    pytest.main(['-s','test3.py','-q','--alluredir','./report'])