# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 22:58
# @Author  : Zheng Jinkun
# @FileName: test.py
# @Software: PyCharm
# @Github  ：https://github.com/zhengjk1992

from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
from reportlab.lib.units import cm


class MyDocTemplate(BaseDocTemplate):

    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, **kw)
        template = PageTemplate('normal', [Frame(2.5 * cm, 2.5 * cm, 16 * cm, 25 * cm, id='Frame1')])  # 页面模版
        self.addPageTemplates(template)  # 将页面模版加入到文档对象

    def afterFlowable(self, flowable):
        """目录TOC、索引关键字和生成outline"""

        if isinstance(flowable, Paragraph):  # 判断是否为段落类型的flowable
            styleName = flowable.style.name  # 取出段落格式名
            if styleName == 'Heading1':  # 第一级标题
                text = flowable.getPlainText()  # 取出段落的文本
                pageNum = self.page  # 取出当前页
                self.notify('TOCEntry', (0, text, pageNum))
                # 'TOCEntry'通知加入目录条目，(0, text, pageNum)指明第一级标题，标题内容，所在页数

                # 添加outline entries
                key = str(hash(flowable))  # 生成key，flowable()定义了__hash__()所以可以用hash()，返回独一的整数
                # print(key)
                self.canv.bookmarkPage(key)  # 生成书签页
                self.canv.addOutlineEntry(text, key, level=0, closed=0)
                # 生成Outline entry，指定文本，关联的书签页，第一级，默认是关闭的

            # 对选定的关键字进行索引
            try:
                text = flowable.getPlainText()  # 取出段落里的文本
            except:
                return  # 没文本可取的直接跳过后面那个for循环
            for phrase in ['uniform', 'depraved', 'finger', 'Fraudulin']:  # 给这些关键字建立索引
                if text.find(phrase) > -1:  # find()返回在段落里找到的第一个子串的索引，啥也没找到返回-1，
                    self.notify('IndexEntry', (phrase, self.page))


"This makes one long multi-page paragraph in multi-pass for testing docWhile etc etc"
from reportlab.platypus.flowables import DocAssign, DocExec, DocPara, DocIf, DocWhile
from reportlab.platypus.tableofcontents import TableOfContents, SimpleIndex
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib import colors
from reportlab.lib.randomtext import randomText, PYTHON

# Build story.
story = []

styleSheet = getSampleStyleSheet()
h1 = styleSheet['Heading1']
h1.pageBreakBefore = 1
h1.keepWithNext = 1  # 标题不跟段落分开（指分在不同页）
h1.outlineLevel = 0  # 在outline上的层级

h2 = styleSheet['Heading2']
h2.backColor = colors.cyan  # 背景色
h2.keepWithNext = 1
h2.outlineLevel = 1

bt = styleSheet['BodyText']  # 普通正文

story.append(Paragraph("""Cross-Referencing Test""", styleSheet["Title"]))  # 第0级标题
story.append(Paragraph("""                                                            
Subsequent pages test cross-references: indexes, tables and individual
cross references.  The number in brackets at the end of each paragraph
is its position in the story. ({})""".format(len(story)), bt))

story.append(Paragraph("""Table of Contents:""", styleSheet["Title"]))
toc = TableOfContents()  # 目录对象
story.append(toc)

chapterNum = 1  # 记录章节
for i in range(10):  # 共10章
    story.append(Paragraph('Chapter {}: Chapters always starts a new page'.format(chapterNum), h1))
    # 每一个章节的标题
    chapterNum += chapterNum
    story.append(DocAssign('chapterNum', chapterNum))
    for j in range(3):
        story.append(Paragraph('Heading1 paragraphs should always'
                               'have a page break before.  Heading 2 on the other hand'
                               'should always have a FRAME break before ({})'.format(len(story)), bt))
        # 普通文本
        story.append(Paragraph('Heading 2 should always be kept with the next thing ({})'.format(len(story)), h2))
        # 二级标题
        for p in range(3):
            story.append(Paragraph(randomText(theme=PYTHON, sentences=2) + ' ({})'.format(len(story)), bt))
            # 两句，内容随机产生，普通文本
            story.append(Paragraph('I should never be at the bottom of a frame ({})'.format(len(story)), h2))
            # 二级标题
            story.append(Paragraph(randomText(theme=PYTHON, sentences=1) + ' ({})'.format(len(story)), bt))
            # 一句，内容随机产生，普通文本
    story.extend([
        DocAssign('currentFrame', 'doc.frame.id'),
        DocAssign('currentPageTemplate', 'doc.pageTemplate.id'),
        DocAssign('aW', 'availableWidth'),
        DocAssign('aH', 'availableHeight'),
        DocAssign('aWH', 'availableWidth,availableHeight'),
        DocAssign('i', 3),
        DocIf('i>3', Paragraph('The value of i is larger than 3', bt),
              Paragraph('The value of i is not larger than 3', bt)),
        DocIf('i==3', Paragraph('The value of i is equal to 3', bt),
              Paragraph('The value of i is not equal to 3', bt)),
        DocIf('i<3', Paragraph('The value of i is less than 3', bt),
              Paragraph('The value of i is not less than 3', bt)),
        DocWhile('i', [DocPara('i', format='The value of i is %(__expr__)d', style=bt), DocExec('i-=1')]),
        DocPara('repr(doc._nameSpace)'),
    ])

story.append(Paragraph('The Index which goes at the back', h1))  # 索引的标题
story.append(SimpleIndex())  # 添加索引
doc = MyDocTemplate('multipass.pdf')
doc.multiBuild(story)
