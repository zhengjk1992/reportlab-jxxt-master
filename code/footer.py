# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 22:17
# @Author  : Zheng Jinkun
# @FileName: footer.py
# @Software: PyCharm
# @Github  ：https://github.com/zhengjk1992

from reportlab.platypus import Paragraph
from paragraphstyle import customerparagraphstyle

def footer(canvas, doc):
	width, heigth = doc.pagesize
	styles = customerparagraphstyle()



	ptext = str(canvas.getPageNumber())
	p = Paragraph(ptext, styles['页脚'])
	p.wrapOn(canvas, width, heigth)
	p.drawOn(canvas, 400, 100)


