#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time    : 2020/12/10 17:47
# @Author  : Gavin


import allure
import pytest
from setupMain import project_path
from bin.config.confManage import dir_manage
from bin.unit.initializeCase import ini_case
from bin.unit.initializePremise import ini_request
from bin.unit.apiSendCheck import api_send_check

PATH = project_path + dir_manage('${page_dir}$') + "api"

case_dict = ini_case(PATH, "login1")


@allure.feature(case_dict["test_info"]["title"])
class login1:

    @pytest.mark.parametrize("case_data", case_dict["test_case"], ids=[])
    @allure.story("login1")
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_login1(self, case_data):
        """

        :param case_data: 测试用例
        :return:
        """
        self.init_relevance = ini_request(case_dict, PATH)
        # 发送测试请求
        api_send_check(case_data, case_dict, self.init_relevance, PATH)

