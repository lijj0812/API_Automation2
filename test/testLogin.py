#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time    : 2020/12/11 14:45
# @Author  : Gavin

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 18:45
# @Author  : Gavin
import requests
import hashlib
import re

loginUrl = "http://rtzentao3.recloud.com.cn/zentao/user-login.html"
headers_1 = {"Content-Type": "application/x-www-form-urlencoded"}  # 定义headers

username = "gavinli"
pwd = "P@ssw0rd"

get_sid = requests.get(loginUrl)  # get方法请求登录页面，用于获取SID
get_sid.encoding = 'utf-8'
verifyRand = re.findall(
    r"id='verifyRand' value='(\d+)'",
    get_sid.text)[0]  # 获取verifyRand值
#print(get_sid.text)
print("verifyRand="+verifyRand)
SID = get_sid.cookies["zentaosid"]
#print(SID)

hlFirst = hashlib.md5()
hlFirst.update(pwd.encode(encoding='utf-8'))  # 第一次对密码进行加密
# print('Md5 第一次加密结果 = ' + hlFirst.hexdigest())
passwordResult = hlFirst.hexdigest() + verifyRand
print("passwordResult=" + passwordResult)
hlLast = hashlib.md5()
hlLast.update(passwordResult.encode(encoding='utf-8'))  # 第二次加密
print('Md5 第二次加密结果 = ' + hlLast.hexdigest())

# 定义请求参数body
bodyRequest = {
    "account": username,
    "password": hlLast.hexdigest(),
    "passwordStrength": 1,
    "referer": "/zentao/",
    "verifyRand": verifyRand,
    # "referer":"http://rtzentao3.recloud.com.cn/zentao/my/",
    "keepLogin": 1}

# 定义cookies
loginCookies = dict(zentaosid=SID, lang='zh-cn', keepLogin='on')
loginRequest = requests.post(loginUrl, data=bodyRequest, cookies=loginCookies)

print(loginRequest.content)
token = loginRequest.cookies['zp']  # 从cookies中获取token
print("koken=" + token)
loginRequest1 = requests.get("http://rtzentao3.recloud.com.cn/zentao/my/", cookies=loginCookies)
#print(loginRequest1.text)
