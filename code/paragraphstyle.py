# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 21:44
# @Author  : Zheng Jinkun
# @FileName: paragraphstyle.py
# @Software: PyCharm
# @Github  ：https://github.com/zhengjk1992

from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_JUSTIFY
from fontsizemap import TWO, SMALL_TWO, THREE, SMALL_THREE, FOUR, SMALL_FOUR, FIVE
from reportlab.lib.units import mm

pdfmetrics.registerFont(TTFont('方正小标宋', '../font/FZXBSK.TTF'))
pdfmetrics.registerFont(TTFont('方正黑体', '../font/FZHTK.TTF'))
pdfmetrics.registerFont(TTFont('方正楷体', '../font/FZKTK.TTF'))
pdfmetrics.registerFont(TTFont('方正仿宋', '../font/FZFSK.TTF'))


def customerparagraphstyle():
    styles = getSampleStyleSheet()
    # 主要作为标题的方正小标宋二号
    styles.add(ParagraphStyle(name='方正小标宋二号',
                              fontName='方正小标宋',
                              fontSize=TWO,
                              leading=28,
                              alignment=TA_CENTER))
    # 一级标题的方正黑体
    styles.add(ParagraphStyle(name='方正黑体三号',
                              fontName='方正黑体',
                              fontSize=THREE,
                              leading=28,
                              firstLineIndent=THREE * 2,
                              alignment=TA_JUSTIFY,
                              wordWrap='CJK'))
    # 二级标题的方正楷体
    styles.add(ParagraphStyle(name='方正楷体三号',
                              fontName='方正楷体',
                              fontSize=THREE,
                              leading=28,
                              firstLineIndent=THREE * 2,
                              alignment=TA_JUSTIFY,
                              wordWrap='CJK'))
    # 正文内容的方正仿宋
    styles.add(ParagraphStyle(name='方正仿宋三号',
                              fontName='方正仿宋',
                              fontSize=THREE,
                              leading=28,
                              firstLineIndent=THREE * 2,
                              alignment=TA_JUSTIFY,
                              wordWrap='CJK'))

    # 作为页眉的方正仿宋
    styles.add(ParagraphStyle(name='页眉',
                              fontName='方正仿宋',
                              fontSize=FIVE,
                              alignment=TA_RIGHT,
                              wordWrap='CJK'))

    # 作为页脚的方正仿宋
    styles.add(ParagraphStyle(name='页脚',
                              fontName='方正仿宋',
                              fontSize=FIVE,
                              alignment=TA_CENTER,
                              wordWrap='CJK'))

    return styles
