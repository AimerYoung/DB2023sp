from .forms import *
from .models import *
from flask import flash

def SEARCH_TEACHER(form: Search_Teacher_Form):
    teacher_id = form.teacher_id.data or None
    teacher_name = form.teacher_name.data or None
    gender = int(form.teacher_gender.data[0]) if form.teacher_gender.data else None
    title = int(form.teacher_title.data[0]) if form.teacher_title.data  else None

    conditions = []
    if teacher_id:
        conditions.append(f"id = '{teacher_id}'")
    if teacher_name:
        conditions.append(f"name = '{teacher_name}'")
    if gender:
        conditions.append(f"gender = {gender}")
    if title:
        conditions.append(f"title = {title}")
    
    if not conditions:
        where_clause = ""
    else:
        where_clause = "WHERE " + " AND ".join(conditions)
    search_query = f"SELECT * FROM teacher {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(search_query)
        results = cursor.fetchall()

    if results:
        return results
    else:
        flash("No records match the criteria!")
        return []
    
def SEARCH_PAPER(form: Search_Paper_Form):
    paper_id = form.paper_id.data or None
    paper_name = form.paper_name.data or None
    source = form.source.data or None
    year = form.year.data or None
    paper_type = int(form.paper_type.data[0]) if form.paper_type.data else None
    paper_level = int(form.paper_level.data[0]) if form.paper_level.data else None 

    conditions = []
    if paper_id:
        conditions.append(f"id = '{paper_id}'")
    if paper_name:
        conditions.append(f"name = '{paper_name}'")
    if source:
        conditions.append(f"source = '{source}'")
    if year:
        conditions.append(f"year = {year}")
    if paper_type:
        conditions.append(f"type = {paper_type}")
    if paper_level:
        conditions.append(f"level = {paper_level}")
    
    if not conditions:
        where_clause = ""
    else:
        where_clause = "WHERE " + " AND ".join(conditions)
    search_query = f"SELECT * FROM paper {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(search_query)
        results = cursor.fetchall()

    if results:
        return results
    else:
        flash("No records match the criteria!")
        return []

def SEARCH_PROJECT(form: Search_Project_Form):
    project_id = form.project_id.data or None
    project_name = form.project_name.data or None
    source = form.source.data or None
    project_type = int(form.project_type.data[0]) if form.project_type.data else None
    total_cost = form.total_cost.data or None
    start_year = form.start_year.data or None
    end_year = form.end_year.data or None

    conditions = []
    if project_id:
        conditions.append(f"id = '{project_id}'")
    if project_name:
        conditions.append(f"name = '{project_name}'")
    if source:
        conditions.append(f"source = '{source}'")
    if project_type:
        conditions.append(f"type = {project_type}")
    if total_cost:
        conditions.append(f"total_cost = {total_cost}")
    if start_year:
        conditions.append(f"start_year = {start_year}")
    if end_year:
        conditions.append(f"end_year = {end_year}")

    if not conditions:
        where_clause = ""
    else:
        where_clause = "WHERE " + " AND ".join(conditions)
    search_query = f"SELECT * FROM Project {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(search_query)
        results = cursor.fetchall()

    if results:
        return results
    else:
        flash("No records match the criteria!")
        return []

def SEARCH_COURSE(form: Search_Course_Form):
    course_id = form.course_id.data or None
    course_name = form.course_name.data or None
    course_hours = form.course_hours.data or None
    course_type = form.course_type.data or None

    conditions = []
    if course_id:
        conditions.append(f"id = '{course_id}'")
    if course_name:
        conditions.append(f"name = '{course_name}'")
    if course_hours:
        conditions.append(f"hours = {course_hours}")
    if course_type:
        conditions.append(f"type = {course_type}")

    if not conditions:
        where_clause = ""
    else:
        where_clause = "WHERE " + " AND ".join(conditions)
    search_query = f"SELECT * FROM Course {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(search_query)
        results = cursor.fetchall()

    if results:
        return results
    else:
        flash("No records match the criteria!")
        return []

def SEARCH_TEACH(form):
    year = form.year.data or None
    semester = form.semester.data or None
    academic_hours = form.academic_hours.data or None
    teacher_id = form.teacher_id.data or None
    course_id = form.course_id.data or None

    conditions = []
    if year:
        conditions.append(f"year = {year}")
    if semester:
        conditions.append(f"semester = {semester}")
    if academic_hours:
        conditions.append(f"academic_hours = {academic_hours}")
    if teacher_id:
        conditions.append(f"teacher_id = '{teacher_id}'")
    if course_id:
        conditions.append(f"course_id = '{course_id}'")

    if not conditions:
        where_clause = ""
    else:
        where_clause = "WHERE " + " AND ".join(conditions)

    search_query = f"SELECT * FROM Teach {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(search_query)
        results = cursor.fetchall()

    if results:
        return results
    else:
        flash("No records match the criteria!")
        return []

def SEARCH_UNDERTAKE(form):
    ranking = form.ranking.data or None
    expense = form.expense.data or None
    teacher_id = form.teacher_id.data or None
    project_id = form.project_id.data or None

    conditions = []
    if ranking:
        conditions.append(f"ranking = {ranking}")
    if expense:
        conditions.append(f"expense = {expense}")
    if teacher_id:
        conditions.append(f"teacher_id = '{teacher_id}'")
    if project_id:
        conditions.append(f"project_id = '{project_id}'")

    if not conditions:
        where_clause = ""
    else:
        where_clause = "WHERE " + " AND ".join(conditions)

    search_query = f"SELECT * FROM Undertake {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(search_query)
        results = cursor.fetchall()

    if results:
        return results
    else:
        flash("No records match the criteria!")
        return []

def SEARCH_PUBLISH(form):
    teacher_id = form.teacher_id.data or None
    paper_id = form.paper_id.data or None
    ranking = form.ranking.data or None
    if form.is_corresponding_author.data:
        is_corresponding_author = int(form.is_corresponding_author.data[0])
    else:
        is_corresponding_author = None

    conditions = []
    if teacher_id:
        conditions.append(f"teacher_id = '{teacher_id}'")
    if paper_id:
        conditions.append(f"paper_id = {paper_id}")
    if ranking:
        conditions.append(f"ranking = {ranking}")
    if is_corresponding_author is not None:
        conditions.append(f"iscorrespondingauthor = {is_corresponding_author}")

    if not conditions:
        where_clause = ""
    else:
        where_clause = "WHERE " + " AND ".join(conditions)

    search_query = f"SELECT * FROM Publish {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(search_query)
        results = cursor.fetchall()

    if results:
        return results
    else:
        flash("No records match the criteria!")
        return []



