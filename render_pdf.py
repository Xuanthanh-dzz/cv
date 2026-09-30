from pathlib import Path
import runpy
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4

pdfmetrics.registerFont(TTFont('CV', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('CVBold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('CV', normal='CV', bold='CVBold', italic='CV', boldItalic='CVBold')
styles = {
 'body': ParagraphStyle('body', fontName='CV', fontSize=8.3, leading=12, textColor=HexColor('#334155'), spaceAfter=5),
 'title': ParagraphStyle('title', fontName='CVBold', fontSize=20, leading=24, spaceAfter=7),
 'section': ParagraphStyle('section', fontName='CVBold', fontSize=10, leading=14, textColor=HexColor('#1e40af'), spaceBefore=10, spaceAfter=7),
 'project': ParagraphStyle('project', fontName='CVBold', fontSize=9, leading=13, spaceBefore=7, spaceAfter=4),
}
def paragraph(text, kind='body'):
 return Paragraph(text.replace('<strong>', '<b>').replace('</strong>', '</b>'), styles[kind])
def footer(canvas, doc):
 canvas.setFont('CV', 7)
 canvas.setFillColor(HexColor('#64748b'))
 canvas.drawString(43, 23, 'PHUNG XUAN QUY THANH | BACKEND .NET · SQL SERVER')
 canvas.drawRightString(A4[0]-43, 23, str(doc.page) + ' / 2')
for suffix, script in [('', 'build_cv.py'), ('_EN', 'build_cv_en.py')]:
 d=runpy.run_path(script)
 vi=not suffix
 story=[]
 def add(t, k='body'): story.append(paragraph(t,k))
 def project(p, personal=False):
  add(p['name'], 'project')
  if 'date' in p: add(p['date']+' | '+p['location'])
  add(p['role']+' | Team: '+p['team_size']+'<br/>Tech: '+p['tech'])
  if personal: add('<link href="'+p['link']+'">'+p['link']+'</link>')
  for b in p['bullets']: add('• '+b)
 add(d['name'],'title')
 add(d['role'])
 add('0975 748 203 | phungxuanquythanh@gmail.com<br/>github.com/Xuanthanh-dzz | '+('Hà Nội' if vi else 'Hanoi, Vietnam'))
 add('Tóm tắt chuyên môn' if vi else 'Professional Summary','section')
 add(d['summary'])
 add('Kỹ năng chuyên môn' if vi else 'Technical Skills','section')
 for s in d['skills']: add('<b>'+s['category']+':</b> '+s['items'])
 add('Kinh nghiệm làm việc' if vi else 'Professional Experience','section')
 add('<b>UniCloud — Enterprise Software &amp; Cloud Solutions</b><br/>05/2024 – '+('Hiện tại | Hà Nội' if vi else 'Present | Hanoi'))
 for p in d['projects_page1']: project(p)
 story.append(PageBreak())
 add('Kinh nghiệm làm việc (tiếp theo)' if vi else 'Professional Experience (continued)','section')
 for p in d['projects_page2']: project(p)
 add('Dự án cá nhân &amp; Open Source' if vi else 'Personal &amp; Open-Source Projects','section')
 for p in d['personal_projects']: project(p,True)
 add('Quy trình &amp; Đóng góp kỹ thuật khác' if vi else 'Technical Contributions &amp; Practices','section')
 for c in d['contributions']: add('• '+c)
 add('Học vấn' if vi else 'Education','section')
 add('<b>'+('Trường Cao đẳng Cộng đồng Hà Tây' if vi else 'Ha Tay Community College')+'</b><br/>'+('Công nghệ Thông tin · Tốt nghiệp năm 2024' if vi else 'Information Technology · Graduated in 2024'))
 SimpleDocTemplate('CV_Phung_Xuan_Quy_Thanh'+suffix+'.pdf',pagesize=A4,rightMargin=43,leftMargin=43,topMargin=35,bottomMargin=40).build(story,onFirstPage=footer,onLaterPages=footer)
