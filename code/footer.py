# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 22:17
# @Author  : Zheng Jinkun
# @FileName: footer.py
# @Software: PyCharm
# @Github  ：https://github.com/zhengjk1992

from reportlab.platypus import Paragraph
from paragraphstyle import customerparagraphstyle
from reportlab.lib.units import mm, inch


def footer(canvas, doc):
    width, heigth = doc.pagesize
    canvas.setFont('方正仿宋', 10.5)  # 设置字体
    # canvas.translate(inch, inch)
    canvas.drawRightString(width / 2 - 1 * mm, 17.5 * mm, "{}".format(doc.page))
