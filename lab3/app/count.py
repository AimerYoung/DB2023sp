from .forms import *
from .models import *
from flask import flash
import jinja2
import markdown
import pdfkit

def COUNT(form: Count_Form):
    teacher_id = form.teacher_id.data
    start_year = form.start_year.data or 0000
    end_year = form.end_year.data or 9999
    
    with conn.cursor() as cursor:
        select_teacher_query = "SELECT * FROM teacher WHERE id = %s"
        cursor.execute(select_teacher_query, (teacher_id))
        teacher = cursor.fetchone()
        if not teacher:
            flash('Teacher not found.')
            return None


        publish_paper_query = """
            SELECT p.id, p.name, p.source, p.year, p.type, p.level, pu.ranking, pu.iscorrespondingauthor
            FROM publish pu
            JOIN paper p ON pu.paper_id = p.id
            WHERE pu.teacher_id = %s AND p.year BETWEEN %s AND %s;
        """
        cursor.execute(publish_paper_query, (teacher_id, str(start_year)+'-01-01', str(end_year)+'-12-31'))
        publish_papers = cursor.fetchall()
        print(publish_papers)

        teach_course_query = """
            SELECT t.course_id, t.semester, c.name AS course_name, c.hours
            FROM Teach t
            INNER JOIN Course c ON t.course_id = c.id
            WHERE t.teacher_id = %s AND t.year BETWEEN %s AND %s
        """
        cursor.execute(teach_course_query, (teacher_id, start_year, end_year))
        teach_courses = cursor.fetchall()

        undertake_project_query = """
            SELECT u.project_id, p.name AS project_name, p.source, p.start_year, p.end_year, u.expense, u.expense AS total_cost
            FROM Undertake u
            INNER JOIN Project p ON u.project_id = p.id
            WHERE u.teacher_id = %s AND p.start_year BETWEEN %s AND %s
        """
        cursor.execute(undertake_project_query, (teacher_id, start_year, end_year))
        undertake_projects = cursor.fetchall()

        return publish_papers, teach_courses, undertake_projects
    
def COUNT_DOWNLOAD(form: Count_Form):
    start_year = form.start_year.data or 0
    end_year = form.end_year.data or 9999
    publish_papers, teach_courses, undertake_projects = COUNT(form)

    with conn.cursor() as cursor:
        teacher_query = """
            SELECT t.id, t.name, t.gender, t.title
            FROM teacher t
            WHERE t.id = %s
        """
        cursor.execute(teacher_query, (form.teacher_id.data))
        teacher = cursor.fetchone()

    template = """
## 教师教学科研工作统计（{{ start_year }}-{{ end_year }}）

#### 教师基本信息

---

工号：{{ teacher.id }}    姓名：{{ teacher.name }}      性别：{{ teacher.gender }}      职称：{{ teacher.title }}

#### 教学情况：

---
{% for course in courses %}
课程号：{{ course.course_id }} 课程名：{{ course.course_name }} 主讲学时：{{ course.course_academic_hours }} 学期：{{ course.semester }}
{% endfor %}

#### 发表论文情况

---
{% for paper in papers %}
{{ loop.index }}. {{ paper.id }}:{{ paper.name }},{{ paper.source }}，{{ paper.year }}，{{ paper.type }}，{{ paper.level }}，排名：{{ paper.ranking }}，{{ paper.iscorrespondingauthor }}通讯作者
{% endfor %}

#### 承担项目情况

---
{% for project in projects %}
{{ loop.index }}. {{ project.name }}，{{ project.source }}，{{ project.level }}，{{ project.start_year }}-{{ project.end_year }}，总经费：{{ project.total_cost }}，承担经费：{{ project.expense }} 
{% endfor %}
"""
    rendered_template = jinja2.Template(template).render(
        start_year=start_year,
        end_year=end_year,
        teacher=teacher,
        courses=teach_courses,
        papers=publish_papers,
        projects=undertake_projects
    )

    with open('report.md', 'w', encoding='utf-8') as file:
        file.write(rendered_template)
    
    with open('report.md', 'r', encoding='utf-8') as file:
        html = markdown.markdown(file.read())
    html = '<meta charset="utf-8">' + html
    pdfkit.from_string(html, 'report.pdf')

    return 'report.pdf'
    








    