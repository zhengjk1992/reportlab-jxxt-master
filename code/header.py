# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 21:39
# @Author  : Zheng Jinkun
# @FileName: header.py
# @Software: PyCharm
# @Github  ：https://github.com/zhengjk1992

from reportlab.platypus import Paragraph
from paragraphstyle import customerparagraphstyle
from reportlab.lib.units import mm

def header(canvas, doc):
	width, heigth = doc.pagesize
	styles = customerparagraphstyle()
	print(styles['页眉'])
	ptext = '技术规范书'
	p = Paragraph(ptext, styles['页眉'])
	p.wrapOn(canvas, width, heigth)
	p.drawOn(canvas, 400, 800)
