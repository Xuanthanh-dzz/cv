from pathlib import Path
from html import escape as e

P = Path(__file__).parent

# Candidate Information
name = "PHÙNG XUÂN QUÝ THÀNH"
role = "FULL-STACK DEVELOPER (.NET / ANGULAR / SQL SERVER)"
contact_items = [
    ("phone", "0975 748 203"),
    ("email", "phungxuanquythanh@gmail.com", "mailto:phungxuanquythanh@gmail.com"),
    ("github", "github.com/Xuanthanh-dzz", "https://github.com/Xuanthanh-dzz"),
    ("location", "Hà Nội")
]

summary = (
    "Lập trình viên Full-stack .NET với hơn 2 năm kinh nghiệm thực chiến tại UniCloud (06/2022 – Hiện tại), "
    "thành thạo phát triển Web API bằng ASP.NET Core, xây dựng giao diện người dùng Angular và xử lý chuyên sâu "
    "cơ sở dữ liệu SQL Server. Có kinh nghiệm áp dụng Clean Architecture, SOLID, CQRS, tối ưu hiệu năng Stored Procedure, "
    "tích hợp Redis caching và xử lý tác vụ bất đồng bộ qua Kafka."
)

skills = [
    {
        "category": "CƠ SỞ DỮ LIỆU",
        "items": "SQL Server, T-SQL, Thiết kế CSDL, Tối ưu hóa truy vấn, Stored Procedure, Indexing"
    },
    {
        "category": "BACKEND .NET",
        "items": "C#, ASP.NET Core Web API, Clean Architecture, SOLID, CQRS, Dapper, Entity Framework, LINQ"
    },
    {
        "category": "FRONTEND & TÍCH HỢP",
        "items": "Angular, TypeScript, RESTful API, Redis Caching, Kafka, Docker, FlexCel, Keycloak"
    },
    {
        "category": "QUY TRÌNH & CÔNG CỤ",
        "items": "Git, GitLab, CI/CD, Database Migration, Postman, Code Review, Testing, ADR"
    }
]

projects_page1 = [
    {
        "name": "Enterprise HRM System",
        "date": "06/2022 – Hiện tại",
        "location": "Hà Nội",
        "role": "Full-stack Developer",
        "team_size": "10 thành viên",
        "tech": ".NET Core, Angular, SQL Server, Redis, Kafka, Docker",
        "bullets": [
            "Phát triển và maintain các module Employee, Contract, Salary, Process.",
            "Xây dựng RESTful API bằng ASP.NET Core và frontend bằng Angular.",
            "Tối ưu SQL Server query, Stored Procedure, Index và LINQ.",
            "Áp dụng Clean Architecture, SOLID và CQRS.",
            "Sử dụng Redis cho caching và Kafka cho asynchronous processing.",
            "Tham gia code review, debugging, testing và deployment."
        ]
    }
]

projects_page2 = [
    {
        "name": "Smart Resident Management System",
        "date": "05/2024 – Hiện tại",
        "location": "Hà Nội",
        "role": "Backend .NET & SQL Developer",
        "team_size": "8 thành viên",
        "tech": ".NET Core, SQL Server, Redis, Docker, Dapper",
        "bullets": [
            "Thiết kế giải pháp bulk import phương tiện: xử lý đồng thời hơn 1.000 bản ghi/lần từ file Excel, rút ngắn thời gian xử lý từ 2 phút xuống dưới 3 giây và loại bỏ 95% round-trip giữa API và Database.",
            "Xây dựng giải pháp thông báo đa ngôn ngữ dùng chung với cơ chế fallback dự phòng an toàn, chuẩn hóa áp dụng nhất quán cho 100% Stored Procedure mới và Web API trên toàn hệ thống.",
            "Phát triển toàn diện nghiệp vụ & API quản lý phương tiện, vòng đời thẻ cư dân, biểu phí dịch vụ và phân quyền người dùng theo vai trò và cây chức năng.",
            "Tối ưu hiệu năng truy vấn, Stored Procedure và cấu trúc cơ sở dữ liệu cho phân hệ quản lý vận hành đô thị."
        ]
    }
]

personal_projects = [
    {
        "name": "AI-Powered Cinema Platform",
        "role": "Personal Project (Owner)",
        "link": "https://github.com/Xuanthanh-dzz/AI-Powered-Cinema-Platform",
        "tech": "C#, .NET 10, Clean Architecture, CQRS, MediatR, FluentValidation, Docker",
        "bullets": [
            "Thiết kế hệ thống theo Clean Architecture kết hợp mô hình CQRS phân tách Command và Query qua MediatR và FluentValidation.",
            "Chuẩn hóa quy trình kỹ thuật qua Architecture Decision Records (ADR) nhằm lưu vết các quyết định thiết kế kiến trúc hệ thống."
        ]
    },
    {
        "name": "Full-Stack Engineering Handbook",
        "role": "Technical Writer & Developer",
        "link": "https://github.com/Xuanthanh-dzz/full-stack",
        "tech": "Computer Science, C / C++, C# (.NET 10), Markdown, GitHub Pages",
        "bullets": [
            "Hệ thống hóa kiến thức nền tảng khoa học máy tính và tối ưu tài nguyên: quản lý bộ nhớ C/C++, nguyên lý hướng đối tượng và kỹ thuật chuyên sâu trên nền tảng .NET."
        ]
    }
]

contributions = [
    "<strong>Quản lý phiên bản và đồng bộ cơ sở dữ liệu:</strong> xây dựng quy trình triển khai bằng migration scripts, bảo đảm tính nhất quán cấu trúc dữ liệu giữa các môi trường.",
    "<strong>Bảo trì thư viện dùng chung:</strong> phát triển và tối ưu các module tiện ích dùng chung (xử lý chuỗi, chuẩn hóa mã phản hồi API và cấu hình tài nguyên hệ thống)."
]

# CSS Stylesheet
css = """@page {
  size: A4;
  margin: 0;
}
* {
  box-sizing: border-box;
}
body {
  margin: 0;
  background: #e2e8f0;
  color: #1e293b;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 9.3pt;
  line-height: 1.48;
}
.page {
  width: 210mm;
  height: 297mm;
  margin: 15px auto;
  background: #ffffff;
  position: relative;
  overflow: hidden;
  padding: 13mm 15mm 13mm 15mm;
  box-shadow: 0 4px 20px rgba(15, 23, 42, 0.08);
}
@media print {
  body { background: white; }
  .page { margin: 0; box-shadow: none; break-after: page; }
  .page:last-child { break-after: auto; }
  * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
}

/* Header */
.header {
  border-bottom: 2px solid #0f172a;
  padding-bottom: 3.5mm;
  margin-bottom: 4mm;
}
.candidate-name {
  font-size: 21pt;
  font-weight: 800;
  color: #0f172a;
  letter-spacing: 0.5px;
  margin: 0 0 1.5mm;
  line-height: 1.15;
}
.candidate-role {
  font-size: 10.5pt;
  font-weight: 700;
  color: #1e40af;
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-bottom: 2.5mm;
}
.contact-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 4mm;
  font-size: 8.8pt;
  color: #475569;
}
.contact-bar a {
  color: #1e40af;
  text-decoration: none;
}
.contact-bar a:hover {
  text-decoration: underline;
}
.contact-item {
  display: flex;
  align-items: center;
  gap: 1.5mm;
}
.sep {
  color: #cbd5e1;
}

/* Running header for page 2 */
.running-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1.5px solid #e2e8f0;
  padding-bottom: 2mm;
  margin-bottom: 4.5mm;
  font-size: 8.2pt;
  color: #64748b;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

/* Sections */
.section {
  margin-bottom: 3.8mm;
}
.page1 .section {
  margin-bottom: 5mm;
}
.section-title {
  font-size: 9.8pt;
  font-weight: 800;
  color: #0f172a;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  border-bottom: 1.5px solid #cbd5e1;
  padding-bottom: 1.2mm;
  margin-bottom: 2.8mm;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.summary-text {
  font-size: 9.1pt;
  line-height: 1.5;
  text-align: justify;
  margin: 0;
  color: #334155;
}
.page1 .summary-text {
  line-height: 1.58;
}

/* Skills Grid */
.skills-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2.2mm 3.5mm;
}
.page1 .skills-grid {
  gap: 3mm 4mm;
}
.skill-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-left: 3px solid #1e40af;
  border-radius: 3px;
  padding: 2mm 3mm;
}
.page1 .skill-card {
  padding: 2.6mm 3.5mm;
}
.skill-cat {
  font-size: 8.2pt;
  font-weight: 700;
  color: #1e40af;
  margin-bottom: 0.8mm;
  letter-spacing: 0.3px;
}
.skill-items {
  font-size: 8.4pt;
  color: #334155;
  line-height: 1.38;
}
.page1 .skill-items {
  line-height: 1.45;
}

/* Work Experience */
.company-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 2.5mm;
  background: #f1f5f9;
  padding: 1.8mm 3mm;
  border-radius: 3px;
}
.company-name {
  font-size: 10.8pt;
  font-weight: 800;
  color: #0f172a;
}
.company-title {
  font-size: 8.8pt;
  color: #475569;
  font-weight: 600;
  margin-left: 2mm;
}
.company-date {
  font-size: 8.6pt;
  font-weight: 700;
  color: #1e40af;
}

/* Projects */
.project-card {
  margin-bottom: 3.5mm;
}
.project-top-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 1mm;
}
.project-title {
  font-size: 10pt;
  font-weight: 800;
  color: #0f172a;
}
.project-date-loc {
  font-size: 8.6pt;
  font-weight: 700;
  color: #1e40af;
}
.project-meta-box {
  background: #f8fafc;
  border-left: 3px solid #1e40af;
  padding: 1.5mm 3mm;
  margin-bottom: 2mm;
  border-radius: 2px;
  font-size: 8.5pt;
  color: #334155;
  display: flex;
  flex-wrap: wrap;
  gap: 1mm 6mm;
}
.meta-item strong {
  color: #0f172a;
}
.meta-tech {
  flex-basis: 100%;
}
.repo-tag {
  font-size: 7.8pt;
  color: #1e40af;
  font-weight: 600;
  text-decoration: none;
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  padding: 1px 6px;
  border-radius: 3px;
  margin-left: 2mm;
}
.repo-tag:hover {
  background: #dbeafe;
}
ul.bullets {
  margin: 0;
  padding-left: 4.5mm;
}
ul.bullets li {
  font-size: 8.8pt;
  line-height: 1.45;
  color: #334155;
  margin-bottom: 1.2mm;
  text-align: justify;
}
ul.bullets li strong {
  color: #0f172a;
}

/* Education & Other */
.edu-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}
.edu-school {
  font-size: 9.5pt;
  font-weight: 700;
  color: #0f172a;
}
.edu-detail {
  font-size: 8.8pt;
  color: #475569;
}
.edu-date {
  font-size: 8.6pt;
  font-weight: 600;
  color: #64748b;
}

/* Footer */
.footer {
  position: absolute;
  bottom: 6mm;
  left: 15mm;
  right: 15mm;
  border-top: 1px solid #e2e8f0;
  padding-top: 2mm;
  display: flex;
  justify-content: space-between;
  font-size: 8pt;
  color: #94a3b8;
}
"""

def render_project(p):
    team_size_html = f'<span class="meta-item"><strong>Team size:</strong> {e(p["team_size"])}</span>' if "team_size" in p else ""
    date_loc = f'{e(p.get("date", ""))} | {e(p.get("location", "Hà Nội"))}' if "date" in p else ""
    return (
        f'<div class="project-card">'
        f'<div class="project-top-row">'
        f'<div class="project-title">Project: {e(p["name"])}</div>'
        f'<div class="project-date-loc">{e(date_loc)}</div>'
        f'</div>'
        f'<div class="project-meta-box">'
        f'<span class="meta-item"><strong>Role:</strong> {e(p["role"])}</span>'
        f'{team_size_html}'
        f'<div class="meta-item meta-tech"><strong>Tech:</strong> {e(p["tech"])}</div>'
        f'</div>'
        f'<ul class="bullets">'
        + "".join(f"<li>{b}</li>" for b in p["bullets"])
        + f"</ul></div>"
    )

def render_personal(p):
    return (
        f'<div class="project-card">'
        f'<div class="project-top-row">'
        f'<div><span class="project-title">Project: {e(p["name"])}</span>'
        f'<a href="{p["link"]}" target="_blank" class="repo-tag">GitHub ↗</a></div>'
        f'</div>'
        f'<div class="project-meta-box">'
        f'<span class="meta-item"><strong>Role:</strong> {e(p["role"])}</span>'
        f'<div class="meta-item meta-tech"><strong>Tech:</strong> {e(p["tech"])}</div>'
        f'</div>'
        f'<ul class="bullets">'
        + "".join(f"<li>{b}</li>" for b in p["bullets"])
        + f"</ul></div>"
    )

# Page 1 HTML
contact_html = (
    '<div class="contact-item"><span>📞</span> <span>0975 748 203</span></div>'
    '<span class="sep">•</span>'
    '<div class="contact-item"><span>✉️</span> <a href="mailto:phungxuanquythanh@gmail.com">phungxuanquythanh@gmail.com</a></div>'
    '<span class="sep">•</span>'
    '<div class="contact-item"><span>🔗</span> <a href="https://github.com/Xuanthanh-dzz" target="_blank">github.com/Xuanthanh-dzz</a></div>'
    '<span class="sep">•</span>'
    '<div class="contact-item"><span>📍</span> <span>Hà Nội</span></div>'
)

skills_html = '<div class="skills-grid">' + "".join(
    f'<div class="skill-card"><div class="skill-cat">{s["category"]}</div><div class="skill-items">{s["items"]}</div></div>'
    for s in skills
) + '</div>'

page1_html = f"""
<section class="page page1">
  <header class="header">
    <h1 class="candidate-name">{name}</h1>
    <div class="candidate-role">{role}</div>
    <div class="contact-bar">{contact_html}</div>
  </header>

  <div class="section">
    <div class="section-title">Tóm tắt chuyên môn</div>
    <p class="summary-text">{summary}</p>
  </div>

  <div class="section">
    <div class="section-title">Kỹ năng chuyên môn</div>
    {skills_html}
  </div>

  <div class="section">
    <div class="section-title">Kinh nghiệm làm việc</div>
    <div class="company-header">
      <div>
        <span class="company-name">UniCloud</span>
        <span class="company-title">— Enterprise Software & Cloud Solutions</span>
      </div>
      <span class="company-date">06/2022 – Hiện tại | Hà Nội</span>
    </div>
    {render_project(projects_page1[0])}
  </div>

  <footer class="footer">
    <span>{name} · HỒ SƠ ỨNG TUYỂN FULL-STACK DEVELOPER</span>
    <span>Trang 01 / 02</span>
  </footer>
</section>
"""

# Page 2 HTML
contributions_html = '<ul class="bullets">' + "".join(
    f"<li>{c}</li>" for c in contributions
) + '</ul>'

page2_html = f"""
<section class="page">
  <div class="running-header">
    <span>{name} · FULL-STACK DEVELOPER (.NET / ANGULAR)</span>
    <span>Hồ sơ năng lực & kinh nghiệm</span>
  </div>

  <div class="section">
    <div class="section-title">Kinh nghiệm làm việc (tiếp theo)</div>
    {render_project(projects_page2[0])}
  </div>

  <div class="section">
    <div class="section-title">Dự án cá nhân & Open Source (GitHub)</div>
    {render_personal(personal_projects[0])}
    {render_personal(personal_projects[1])}
  </div>

  <div class="section">
    <div class="section-title">Quy trình & Đóng góp kỹ thuật khác</div>
    {contributions_html}
  </div>

  <div class="section">
    <div class="section-title">Học vấn</div>
    <div class="edu-row">
      <div>
        <div class="edu-school">Trường Cao đẳng Cộng đồng Hà Tây</div>
        <div class="edu-detail">Chuyên ngành Công nghệ Thông tin</div>
      </div>
      <div class="edu-date">Tốt nghiệp năm 2024</div>
    </div>
  </div>

  <footer class="footer">
    <span>{name} · HỒ SƠ ỨNG TUYỂN FULL-STACK DEVELOPER</span>
    <span>Trang 02 / 02</span>
  </footer>
</section>
"""

full_html = f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{name} | {role}</title>
  <style>{css}</style>
</head>
<body>
{page1_html}
{page2_html}
</body>
</html>
"""

(P / "CV_Phung_Xuan_Quy_Thanh.html").write_text(full_html, encoding="utf-8")

# Generate Markdown
md_content = f"""# {name}

**{role}**

0975 748 203 · phungxuanquythanh@gmail.com · [github.com/Xuanthanh-dzz](https://github.com/Xuanthanh-dzz) · Hà Nội

---

## Tóm tắt chuyên môn

{summary}

---

## Kỹ năng chuyên môn

"""

for s in skills:
    md_content += f"- **{s['category']}:** {s['items']}\n"

md_content += f"""
---

## Kinh nghiệm làm việc

**UniCloud — Enterprise Software & Cloud Solutions**  
*06/2022 – Hiện tại | Hà Nội*

### Project: {projects_page1[0]['name']}
*{projects_page1[0]['date']} | {projects_page1[0]['location']}*  
**Role:** {projects_page1[0]['role']} | **Team size:** {projects_page1[0]['team_size']}  
**Tech:** {projects_page1[0]['tech']}  

"""
for b in projects_page1[0]['bullets']:
    clean_b = b.replace('<strong>', '**').replace('</strong>', '')
    md_content += f"- {clean_b}\n"

md_content += f"""
### Project: {projects_page2[0]['name']}
*{projects_page2[0]['date']} | {projects_page2[0]['location']}*  
**Role:** {projects_page2[0]['role']} | **Team size:** {projects_page2[0]['team_size']}  
**Tech:** {projects_page2[0]['tech']}  

"""
for b in projects_page2[0]['bullets']:
    clean_b = b.replace('<strong>', '**').replace('</strong>', '')
    md_content += f"- {clean_b}\n"

md_content += f"""
---

## Dự án cá nhân & Open Source (GitHub)

### Project: {personal_projects[0]['name']}
*[{personal_projects[0]['link']}]({personal_projects[0]['link']})*  
**Role:** {personal_projects[0]['role']}  
**Tech:** {personal_projects[0]['tech']}  

"""
for b in personal_projects[0]['bullets']:
    md_content += f"- {b}\n"

md_content += f"""
### Project: {personal_projects[1]['name']}
*[{personal_projects[1]['link']}]({personal_projects[1]['link']})*  
**Role:** {personal_projects[1]['role']}  
**Tech:** {personal_projects[1]['tech']}  

"""
for b in personal_projects[1]['bullets']:
    clean_b = b.replace('&lt;', '<').replace('&gt;', '>')
    md_content += f"- {clean_b}\n"

md_content += f"""
---

## Quy trình & Đóng góp kỹ thuật khác

"""
for c in contributions:
    clean_c = c.replace('<strong>', '**').replace('</strong>', '')
    md_content += f"- {clean_c}\n"

md_content += f"""
---

## Học vấn

**Trường Cao đẳng Cộng đồng Hà Tây**  
Chuyên ngành Công nghệ Thông tin · Tốt nghiệp năm 2024
"""

(P / "CV_Phung_Xuan_Quy_Thanh.md").write_text(md_content, encoding="utf-8")
print("Build completed successfully: HTML and Markdown generated.")
