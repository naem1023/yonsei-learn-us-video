# -*- coding: utf-8 -*-
from setuptools import setup

# name, description, version등의 정보는 일반적인 setup.py와 같습니다.
setup(name="yd",
      description="yonsei video downloader via py2app",
      version="1.0.0",
      # 설치시 의존성 추가
      setup_requires=["py2app"],
      app=["main.py"],
      options={
          "py2app": {
              "includes": [
                  "bs4",
                  "os",
                  "sys",
                  "traceback",
                  "subprocess"
                  ],
              "packages": [
                  "BeautifulSoup", 
                  "sp"
                  ]
          }
      })