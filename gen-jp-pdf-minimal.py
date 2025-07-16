#!/usr/bin/env python3

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# フォントを登録
pdfmetrics.registerFont(
    TTFont("NotoSansCJKjp", "files/NotoSansJP-Regular.ttf")
)

# PDF生成
c = canvas.Canvas("output.pdf")
c.setFont("NotoSansCJKjp", 14)
c.drawString(100, 750, "これは埋め込みフォントの日本語です。")
c.save()
