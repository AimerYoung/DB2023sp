## 	                教师教学科研工作统计（{{start_year}}-{{end_year}}）

#### 教师基本信息

---

工号：{{ teacher_id }}    姓名：{{ teacher_name}}      性别：{{ teacher_gender }}      职称：{{teacher_title}}

#### 教学情况：

---
{{% for course in courses %}}
课程号：{{ course_id }} 课程名：{{ course_name }} 主讲学时：{{ course_academic_hours }} 学期：{{ semester}}
{{% endfor %}}

#### 发表论文情况

---
{{% for paper in papers %}}
{{loop.index}}. {{paper.id}}:{{paper.name}},{{paper.source}}，{{paper.year}}，{{paper.type}}，{{paper.level}}，排名：{{paper.ranking}}，{{paper.iscorrespondingauthor}}通讯作者
{{% endfor %}}

#### 承担项目情况

---
{% for project in projects %}
{{ loop.index }}. {{ project.name }}，{{ project.source }}，{{ project.level }}，{{ project.start_year }}-{{ project.end_year }}，总经费：{{project.total_cost}}，承担经费：{{project.expense}} 
{% endfor %}