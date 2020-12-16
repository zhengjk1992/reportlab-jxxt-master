# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 22:24
# @Author  : Zheng Jinkun
# @FileName: main.py
# @Software: PyCharm
# @Github  ：https://github.com/zhengjk1992

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.units import mm
from header import header
from footer import footer
from paragraphstyle import customerparagraphstyle
from reportlab.platypus import Paragraph
from reportlab.platypus import PageBreak
from fontsizemap import TWO, SMALL_TWO, THREE, SMALL_THREE, FOUR, SMALL_FOUR, FIVE
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate  # 用于生成页面模版，文档模版
from reportlab.platypus.tableofcontents import TableOfContents  # 用于生成目录
from reportlab.platypus.frames import Frame
# 生成页面模版是定义页面内的框架frame
from reportlab.lib.units import cm, inch, mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.pagesizes import A4


class MyDocTemplate(BaseDocTemplate):

    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, **kw)
        template = PageTemplate('normal', [
            Frame(0, 0, A4[0], A4[1], leftPadding=31.8 * mm, bottomPadding=25.4 * mm, rightPadding=31.8 * mm,
                  topPadding=25.4 * mm)], onPageEnd=self.footer)
        # 定义页面模版，页脚可有可无
        self.addPageTemplates(template)  # 加入页面模版

    def afterFlowable(self, flowable):  # 注册目录的条目
        if flowable.__class__.__name__ == 'Paragraph':
            text = flowable.getPlainText()  # 取出文字
            style = flowable.style.name  # 取出段落格式
            if style == '方正黑体三号':  # 第一级标题
                key = 'h1-{}'.format(self.seq.nextf('方正黑体三号'))  # 生成书签名
                self.notify('TOCEntry', (0, text, self.page))
                self.canv.bookmarkPage(key)  # 生成书签页
                self.canv.addOutlineEntry(text, key, level=0, closed=0)
            if style == '方正楷体三号':  # 第二级标题
                key = 'h2-{}'.format(self.seq.nextf('方正楷体三号'))  # 生成书签名
                self.notify('TOCEntry', (1, text, self.page, key))
                self.canv.bookmarkPage(key)  # 生成书签页
                self.canv.addOutlineEntry(text, key, level=1, closed=0)  # 生成Outline entry，指定文本，关联的书签页，第一级，默认是关闭的

    def footer(self, canvas, doc):
        width, heigth = doc.pagesize
        canvas.setFont('方正仿宋', 10.5)  # 设置字体
        canvas.drawRightString(width / 2 - 1 * mm, 17.5 * mm, "{}".format(doc.page))


if __name__ == '__main__':
    toc = TableOfContents()  # 生成目录对象
    styles = customerparagraphstyle()
    h1 = ParagraphStyle(name='方正小标宋二号', fontName='方正小标宋', fontSize=TWO, leading=28, alignment=TA_CENTER)
    h2 = ParagraphStyle(name='方正黑体三号', fontName='方正黑体', fontSize=THREE, leading=28, alignment=TA_JUSTIFY,
                        wordWrap='CJK')
    h3 = ParagraphStyle(name='方正楷体三号', fontName='方正楷体', fontSize=THREE, leading=28, firstLineIndent=THREE * 2,
                        alignment=TA_JUSTIFY, wordWrap='CJK')

    toc.levelStyles = [h2, h3]
    # 定义目录的格式，三层，每层的格式用段落格式定义

    story = []
    story.append(toc)
    story.append(PageBreak())  # 分页符
    docPDF = MyDocTemplate('mintoc.pdf')
    story.append(Paragraph("数字化审计本地差异化改造思路", styles["方正小标宋二号"]))

    story.append(Paragraph("一、提取脚本所涉及的源系统表", styles["方正黑体三号"]))
    story.append(Paragraph(
        """以营销专业“用户电量电费”模型为例，通过编写脚本获取该审计中间表涉及的模型表（标准表），得到结果。以营销专业“用户电量电费”模型为例，通过编写脚本获取该审计中间表涉及的模型表（标准表），得到结果。""",
        styles["方正仿宋三号"]))
    txt = "以营销专业“用户电量电费”模型为例，通过编写脚本获取该审计中间表涉及的模型表（标准表），得到结果。以营销专业“用户电量电费”模型为例，通过编写脚本获取该审计中间表涉及的模型表（标准表），得到结果。"

    for line in range(30):
        paragraph = Paragraph(txt, styles["方正仿宋三号"])
        if line % 11 == 7:
            paragraph = Paragraph(txt, styles["方正楷体三号"])
        if line % 20 == 7:
            paragraph = Paragraph(txt, styles["方正黑体三号"])
        story.append(paragraph)
    # docPDF.build(story, onFirstPage=header, onLaterPages=footer)
    docPDF.multiBuild(story)
