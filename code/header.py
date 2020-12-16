# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 21:39
# @Author  : Zheng Jinkun
# @FileName: header.py
# @Software: PyCharm
# @Github  ：https://github.com/zhengjk1992

from reportlab.platypus import Paragraph
from paragraphstyle import customerparagraphstyle
from reportlab.lib.units import mm
from reportlab.lib.units import mm, inch


def header(canvas, doc):
    width, heigth = doc.pagesize
    canvas.setFont('方正仿宋', 10.5)  # 设置字体
    canvas.drawRightString(width - 30 * mm, 280 * mm, "技术规范书")
