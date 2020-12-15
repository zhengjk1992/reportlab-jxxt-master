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

def main(pdf_file):
	doc = SimpleDocTemplate(pdf_file, rightMargin=31.8*mm, leftMargin=31.8*mm, topMargin=25.4*mm, bottomMargin=25.4*mm)
	elements = []
	styles = customerparagraphstyle()

	elements.append(Paragraph("数字化审计本地差异化改造思路", styles["方正小标宋二号"]))

	elements.append(Paragraph("一、提取脚本所涉及的源系统表", styles["方正黑体三号"]))
	elements.append(Paragraph("""以营销专业“用户电量电费”模型为例，通过编写脚本获取该审计中间表涉及的模型表（标准表），得到结果。<br/>以营销专业“用户电量电费”模型为例，通过编写脚本获取该审计中间表涉及的模型表（标准表），得到结果。""",
	                          styles["方正仿宋三号"]))
	txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,'

	for line in range(200):
		paragraph = Paragraph(txt, styles["方正仿宋三号"])
		elements.append(paragraph)
	doc.build(elements, onFirstPage=header, onLaterPages=footer)

if __name__ == '__main__':
	main(pdf_file='main.pdf')