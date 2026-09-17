from pathlib import Path
from html import escape as e

P = Path(__file__).parent

# Candidate Information
name = "PHUNG XUAN QUY THANH"
role = "BACKEND .NET · SQL SERVER DEVELOPER"
contact_items = [
    ("phone", "0975 748 203"),
    ("email", "phungxuanquythanh@gmail.com", "mailto:phungxuanquythanh@gmail.com"),
    ("github", "github.com/Xuanthanh-dzz", "https://github.com/Xuanthanh-dzz"),
    ("location", "Hanoi, Vietnam")
]

summary = (
    "Backend .NET Developer with nearly 2.5 years of hands-on experience at UniCloud (05/2024 – Present), "
    "specializing in high-performance SQL Server database engineering and complex business logic processing. "
    "Proven track record of developing and optimizing ~80 Stored Procedures, architecting high-throughput bulk import "
    "workflows, and standardizing enterprise-wide multilingual notification frameworks. Proficient in building robust Web APIs "
    "on the .NET platform following Clean Architecture and CQRS patterns."
)

skills = [
    {
        "category": "DATABASE & SQL",
        "items": "SQL Server, T-SQL, Database Design, Query Optimization, Stored Procedures"
    },
    {
        "category": "BACKEND .NET",
        "items": "C#, ASP.NET Core Web API, Clean Architecture, CQRS, Dapper, Entity Framework"
    },
    {
        "category": "ARCHITECTURE & INTEGRATION",
        "items": "RESTful API, Repository Pattern, Shared Libraries, FlexCel, Keycloak"
    },
    {
        "category": "WORKFLOW & TOOLS",
        "items": "Git, GitLab, CI/CD, Database Migration, Docker, Postman, ADR"
    }
]

projects_page1 = [
    {
        "name": "Resident — Smart Urban & Resident Management System",
        "date": "05/2024 – Present",
        "location": "Hanoi",
        "role": "Backend .NET & SQL Developer",
        "team_size": "8 members",
        "tech": "C#, ASP.NET Core, SQL Server, Repository Pattern",
        "bullets": [
            "Architected a high-throughput vehicle bulk import engine: concurrently processed 1,000+ Excel records per batch, reducing processing time from 2 minutes to under 3 seconds and eliminating 95% of API-to-database round-trips via a two-tier database-level validation mechanism.",
            "Engineered an enterprise-wide shared multilingual notification framework: dynamically resolved localized messages with a resilient fallback mechanism; standardized and adopted across 100% of newly developed Stored Procedures and Web APIs.",
            "Developed end-to-end business workflows and APIs for vehicle and resident card lifecycle management: issuance, card renewal, activation/suspension with audit logging; automated service fee computation and refunds; implemented role-based access control (RBAC)."
        ]
    },
    {
        "name": "UniHRM — Human Resource & Payroll Management System",
        "date": "05/2024 – Present",
        "location": "Hanoi",
        "role": "Backend .NET & SQL Developer",
        "team_size": "10 members",
        "tech": "C#, ASP.NET Core, SQL Server, Dapper, FlexCel",
        "bullets": [
            "Optimized social insurance adjustment processing: leveraged Dapper Multiple Result Sets to retrieve master lookup catalogs and reconciliation datasets in a single database query, drastically minimizing network latency and overhead.",
            "Automated candidate onboarding and interview scheduling workflows: built business filtering logic by organizational unit, batch-grouping candidates to trigger automated push notifications.",
            "Developed insurance and payroll reporting modules: orchestrated and mapped complex relational data to APIs; flexibly handled dynamic fields, custom aggregation rules, and enterprise payroll cycles."
        ]
    }
]

projects_page2 = [
    {
        "name": "Bizzone & HR Portal — Enterprise HRM Portal",
        "date": "05/2024 – Present",
        "location": "Hanoi",
        "role": "Backend .NET & SQL Developer",
        "team_size": "12 members",
        "tech": "C#, ASP.NET Core, SQL Server, FlexCel, Keycloak",
        "bullets": [
            "Engineered core Stored Procedures for 360-degree competency evaluation reporting: processed multi-criteria evaluation matrices, computing department and company-wide percentile rankings and averages for 5,000+ employees on the Web Portal.",
            "Automated enterprise report generation using FlexCel: mapped relational database records into dynamic templates, delivering highly accurate Excel and PDF survey evaluation exports.",
            "Synchronized employee lifecycle workflows and maintained Core HRM systems: implemented automated conversion pipelines from accepted candidates to full-time staff; handled maternity and training bond policies; maintained centralized Keycloak SSO authentication."
        ]
    }
]

personal_projects = [
    {
        "name": "AI-Powered Cinema Platform",
        "role": "Personal Project (Owner)",
        "team_size": "1 member",
        "link": "https://github.com/Xuanthanh-dzz/AI-Powered-Cinema-Platform",
        "tech": "C#, .NET 10, Clean Architecture, CQRS, MediatR, FluentValidation, Docker",
        "bullets": [
            "Architected the backend following Clean Architecture and CQRS, decoupling Command and Query handlers via MediatR and FluentValidation.",
            "Standardized architectural decision-making via Architecture Decision Records (ADRs) to document system trade-offs and structural choices."
        ]
    },
    {
        "name": "Full-Stack Engineering Handbook",
        "role": "Technical Writer & Developer",
        "team_size": "1 member",
        "link": "https://github.com/Xuanthanh-dzz/full-stack",
        "tech": "Computer Science, C / C++, C# (.NET 10), Markdown, GitHub Pages",
        "bullets": [
            "Synthesized core computer science fundamentals and resource optimization: C/C++ memory management, object-oriented principles, and advanced techniques on the .NET platform."
        ]
    }
]

contributions = [
    "<strong>Database versioning and schema synchronization:</strong> established automated deployment workflows via database migration scripts, maintaining absolute schema consistency across multiple environments.",
    "<strong>Shared library maintenance:</strong> engineered and optimized shared enterprise utility libraries (string manipulation, standardized API response envelopes, and centralized configuration loaders)."
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
  margin-bottom: 4.5mm;
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
  line-height: 1.52;
}

/* Skills Grid */
.skills-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2.2mm 3.5mm;
}
.page1 .skills-grid {
  gap: 2.8mm 4mm;
}
.skill-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-left: 3px solid #1e40af;
  border-radius: 3px;
  padding: 2mm 3mm;
}
.page1 .skill-card {
  padding: 2.4mm 3.5mm;
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
  line-height: 1.42;
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
    date_loc = f'{e(p.get("date", ""))} | {e(p.get("location", "Hanoi"))}' if "date" in p else ""
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
    team_size_html = f'<span class="meta-item"><strong>Team size:</strong> {e(p["team_size"])}</span>' if "team_size" in p else ""
    return (
        f'<div class="project-card">'
        f'<div class="project-top-row">'
        f'<div><span class="project-title">Project: {e(p["name"])}</span>'
        f'<a href="{p["link"]}" target="_blank" class="repo-tag">GitHub ↗</a></div>'
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

# Page 1 HTML
contact_html = (
    '<div class="contact-item"><span>📞</span> <span>0975 748 203</span></div>'
    '<span class="sep">•</span>'
    '<div class="contact-item"><span>✉️</span> <a href="mailto:phungxuanquythanh@gmail.com">phungxuanquythanh@gmail.com</a></div>'
    '<span class="sep">•</span>'
    '<div class="contact-item"><span>🔗</span> <a href="https://github.com/Xuanthanh-dzz" target="_blank">github.com/Xuanthanh-dzz</a></div>'
    '<span class="sep">•</span>'
    '<div class="contact-item"><span>📍</span> <span>Hanoi, Vietnam</span></div>'
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
    <div class="section-title">Professional Summary</div>
    <p class="summary-text">{summary}</p>
  </div>

  <div class="section">
    <div class="section-title">Technical Skills</div>
    {skills_html}
  </div>

  <div class="section">
    <div class="section-title">Professional Experience</div>
    <div class="company-header">
      <div>
        <span class="company-name">UniCloud</span>
        <span class="company-title">— Enterprise Software & Cloud Solutions</span>
      </div>
      <span class="company-date">05/2024 – Present | Hanoi</span>
    </div>
    {render_project(projects_page1[0])}
    {render_project(projects_page1[1])}
  </div>

  <footer class="footer">
    <span>{name} · BACKEND .NET & SQL SERVER DEVELOPER</span>
    <span>Page 01 / 02</span>
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
    <span>{name} · BACKEND .NET & SQL SERVER DEVELOPER</span>
    <span>Technical Profile & Experience</span>
  </div>

  <div class="section">
    <div class="section-title">Professional Experience (Continued)</div>
    {render_project(projects_page2[0])}
  </div>

  <div class="section">
    <div class="section-title">Personal & Open-Source Projects (GitHub)</div>
    {render_personal(personal_projects[0])}
    {render_personal(personal_projects[1])}
  </div>

  <div class="section">
    <div class="section-title">Technical Contributions & Practices</div>
    {contributions_html}
  </div>

  <div class="section">
    <div class="section-title">Education</div>
    <div class="edu-row">
      <div>
        <div class="edu-school">Ha Tay Community College</div>
        <div class="edu-detail">Major in Information Technology</div>
      </div>
      <div class="edu-date">Graduated in 2024</div>
    </div>
  </div>

  <footer class="footer">
    <span>{name} · BACKEND .NET & SQL SERVER DEVELOPER</span>
    <span>Page 02 / 02</span>
  </footer>
</section>
"""

full_html = f"""<!doctype html>
<html lang="en">
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

(P / "CV_Phung_Xuan_Quy_Thanh_EN.html").write_text(full_html, encoding="utf-8")

# Generate Markdown
md_content = f"""# {name}

**{role}**

0975 748 203 · phungxuanquythanh@gmail.com · [github.com/Xuanthanh-dzz](https://github.com/Xuanthanh-dzz) · Hanoi, Vietnam

---

## Professional Summary

{summary}

---

## Technical Skills

"""

for s in skills:
    md_content += f"- **{s['category']}:** {s['items']}\n"

md_content += f"""
---

## Professional Experience

**UniCloud — Enterprise Software & Cloud Solutions**  
*05/2024 – Present | Hanoi*

### Project: {projects_page1[0]['name']}
*{projects_page1[0]['date']} | {projects_page1[0]['location']}*  
**Role:** {projects_page1[0]['role']} | **Team size:** {projects_page1[0]['team_size']}  
**Tech:** {projects_page1[0]['tech']}  

"""
for b in projects_page1[0]['bullets']:
    clean_b = b.replace('<strong>', '**').replace('</strong>', '')
    md_content += f"- {clean_b}\n"

md_content += f"""
### Project: {projects_page1[1]['name']}
*{projects_page1[1]['date']} | {projects_page1[1]['location']}*  
**Role:** {projects_page1[1]['role']} | **Team size:** {projects_page1[1]['team_size']}  
**Tech:** {projects_page1[1]['tech']}  

"""
for b in projects_page1[1]['bullets']:
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

## Personal & Open-Source Projects (GitHub)

### Project: {personal_projects[0]['name']}
*[{personal_projects[0]['link']}]({personal_projects[0]['link']})*  
**Role:** {personal_projects[0]['role']} | **Team size:** {personal_projects[0]['team_size']}  
**Tech:** {personal_projects[0]['tech']}  

"""
for b in personal_projects[0]['bullets']:
    md_content += f"- {b}\n"

md_content += f"""
### Project: {personal_projects[1]['name']}
*[{personal_projects[1]['link']}]({personal_projects[1]['link']})*  
**Role:** {personal_projects[1]['role']} | **Team size:** {personal_projects[1]['team_size']}  
**Tech:** {personal_projects[1]['tech']}  

"""
for b in personal_projects[1]['bullets']:
    clean_b = b.replace('&lt;', '<').replace('&gt;', '>')
    md_content += f"- {clean_b}\n"

md_content += f"""
---

## Technical Contributions & Practices

"""
for c in contributions:
    clean_c = c.replace('<strong>', '**').replace('</strong>', '')
    md_content += f"- {clean_c}\n"

md_content += f"""
---

## Education

**Ha Tay Community College**  
Major in Information Technology · Graduated in 2024
"""

(P / "CV_Phung_Xuan_Quy_Thanh_EN.md").write_text(md_content, encoding="utf-8")
print("English CV build completed successfully: HTML and Markdown generated.")
