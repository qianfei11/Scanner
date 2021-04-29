#-*- encoding=utf-8 -*-
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn # 中文格式
from docx.shared import Pt # 磅数
from docx.shared import Inches # 图片尺寸

import time

today = time.strftime("%Y{y}%m{m}%d{d}", time.localtime()).format(y="年", m="月", d="日")
print today

document = Document()

paragraph = document.add_paragraph('hello world')

document.save("2021-4-28.docx")
