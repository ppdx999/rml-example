#!/usr/bin/env python3

from reportlab.platypus import BaseDocTemplate, PageTemplate, FrameBreak, PageBreak
from reportlab.platypus import Paragraph, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import cidfonts
from reportlab.platypus.frames import Frame

# 日本語フォントの登録
pdfmetrics.registerFont(cidfonts.UnicodeCIDFont("HeiseiKakuGo-W5"))

# フォントスタイルの設定
PS = ParagraphStyle
style_body = PS(name = 'body',
       fontName = "HeiseiKakuGo-W5",
       fontSize = 12,
       leading = 13)

# DocTemplateの生成
file_path = "./pdf/gen-by-flowable.pdf"
doc = BaseDocTemplate(file_path, 
    title="テスト",
    pagesize=portrait(A4),
    )
width, height = A4   # 595px, 842px

# Frameの定義
show = 1 #Frameの枠を表示
frames = [
    Frame(15*mm, 15*mm, width / 2 - 15*mm, height - 30*mm, showBoundary=show),
    Frame(width / 2, 15*mm, width / 2 - 15*mm, height - 30*mm, showBoundary=show),
]

# PageTemplateの定義とDocTemplateへの登録
page_template = PageTemplate("test", frames=frames)
doc.addPageTemplates(page_template)

# 日本語フォントの登録
pdfmetrics.registerFont(cidfonts.UnicodeCIDFont("HeiseiKakuGo-W5"))

# フォントスタイルの設定
PS = ParagraphStyle
style_body = PS(name = 'body',
       fontName = "HeiseiKakuGo-W5",
       fontSize = 12,
       textColor=colors.Color(0,1,0,1),
       leading = 13)

## 内容記入
flowables = [] # 資料全体のflowableの格納用リスト
para = Paragraph("Hello, world!", style_body)
flowables.append(para)
para = Paragraph("Hello, world2!", style_body)
flowables.append(para)

#次のフレームへ
flowables.append(FrameBreak())
para = Paragraph("Hello, world3!", style_body)
flowables.append(para)

#ページへ
flowables.append(PageBreak())
para = Paragraph("Hello, next page!", style_body)
flowables.append(para)
para = Paragraph("すごく長い文章も勝手に折り返しされて表示されます。この機能が非常に便利なのでもうdrawStringでの書き方には戻れなさそうですね。", style_body)
flowables.append(para)

# 表の作成
flowables.append(FrameBreak()) #次のフレームへ
para = Paragraph("Table. 果物価格", style_body)
flowables.append(para)
data = [['ID', '名前', '価格'],
        ['0', 'リンゴ', 100],
        ['1', 'ミカン', 400],
        ['2', 'イチゴ', 300],
        ['3', 'ブドウ', 1000],
        ]
table = Table(data, colWidths=20*mm, rowHeights=10*mm)
table.setStyle(TableStyle([
                ('FONT', (0, 0), (2, 4), 'HeiseiKakuGo-W5', 12),
                ('BOX', (0, 0), (2, 4), 1, colors.black),
                ('INNERGRID', (0, 0), (2, 4), 1, colors.black),
                ('VALIGN', (0, 0), (2, 4), 'MIDDLE'),
                ]))
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (2, 0), colors.lightskyblue),
]))
flowables.append(table)

doc.multiBuild(flowables) # flowableのリストをDocTemplateに登録し、PDFを作成
