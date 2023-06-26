from .forms import *
from .models import *
from flask import flash

def DELETE_TEACHER(form: Search_Teacher_Form):
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
    
    select_query = f"SELECT id FROM teacher {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return flash("No records match the criteria!")
        else:
            teacher_id = result[0].get('id')
            conn.commit()

    delete_teach_query = f"DELETE FROM Teach WHERE teacher_id = '{teacher_id}'"
    delete_teacher_query = f"DELETE FROM Teacher WHERE id = '{teacher_id}'"
    delete_undertake_query = f"DELETE FROM Undertake WHERE teacher_id = '{teacher_id}'"
    delete_publish_query = f"DELETE FROM Publish WHERE teacher_id = '{teacher_id}'"

    with conn.cursor() as cursor:
        cursor.execute(delete_teacher_query)
        affected_rows = cursor.rowcount
        cursor.execute(delete_teach_query)
        affected_rows += cursor.rowcount
        cursor.execute(delete_undertake_query)
        affected_rows += cursor.rowcount
        cursor.execute(delete_publish_query)
        affected_rows += cursor.rowcount
        conn.commit()

    if affected_rows > 0:
        flash(f"{affected_rows} records deleted successfully!")
    else:
        flash("No records match the criteria!")

    
def DELETE_PAPER(form: Search_Paper_Form):
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
    select_query = f"SELECT * FROM paper {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(select_query)
        results = cursor.fetchall()
        if not results:
            return flash("No records match the criteria!")
        else:
            paper_id = results[0].get('id')
            conn.commit()

    delete_paper_query = f"DELETE FROM paper where id = '{paper_id}'"
    delete_publish_query = f"DELETE FROM publish where paper_id = '{paper_id}'"

    with conn.cursor() as cursor:
        cursor.execute(delete_paper_query)
        affected_rows = cursor.rowcount
        cursor.execute(delete_publish_query)
        affected_rows += cursor.rowcount
        conn.commit()

    if affected_rows > 0:
        flash(f"{affected_rows} records deleted successfully!")
    else:
        flash("No records match the criteria!")

def DELETE_PROJECT(form: Search_Project_Form):
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

    select_query = f"SELECT id FROM Project {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return flash("No records match the criteria!")
        else:
            project_id = result[0].get('id')
            conn.commit()

    delete_project_query = f"DELETE FROM project where id = '{project_id}'"
    delete_undertake_query = f"DELETE FROM undertake where project_id = '{project_id}'"

    with conn.cursor() as cursor:
        cursor.execute(delete_project_query)
        affected_rows = cursor.rowcount
        cursor.execute(delete_undertake_query)
        affected_rows += cursor.rowcount
        conn.commit()

    if affected_rows > 0:
        flash(f"{affected_rows} records deleted successfully!")
    else:
        flash("No records match the criteria!")

def DELETE_COURSE(form: Search_Course_Form):
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
    select_query = f"SELECT id FROM Course {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return flash("No records match the criteria!")
        else:
            course_id = result[0].get('id')
            conn.commit()

    delete_course_query = f"DELETE FROM course where id = '{course_id}'"
    delete_teach_query = f"DELETE FROM teach where course_id = '{course_id}'"

    with conn.cursor() as cursor:
        cursor.execute(delete_course_query)
        affected_rows = cursor.rowcount
        cursor.execute(delete_teach_query)
        affected_rows += cursor.rowcount
        conn.commit()

    if affected_rows > 0:
        flash(f"{affected_rows} records deleted successfully!")
    else:
        flash("No records match the criteria!")

def DELETE_TEACH(form):
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

    delete_teach_query = f"DELETE FROM teach {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(delete_teach_query)
        affected_rows = cursor.rowcount
        conn.commit()

    if affected_rows > 0:
        flash(f"{affected_rows} records deleted successfully!")
    else:
        flash("No records match the criteria!")

def DELETE_UNDERTAKE(form):
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

    delete_undertake_query = f"DELETE FROM undertake {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(delete_undertake_query)
        affected_rows = cursor.rowcount

        select_query = "SELECT id FROM Project"
        cursor.execute(select_query)
        projects = cursor.fetchall()

        for project in projects:
            project_id = project.get('id')
            select_query = f"SELECT project_id FROM Undertake WHERE project_id = '{project_id}'"
            cursor.execute(select_query)
            result = cursor.fetchone()

            if not result:
                delete_query = f"DELETE FROM Project WHERE id = '{project_id}'"
                affected_rows += 1
                cursor.execute(delete_query)
        
        conn.commit()

    if affected_rows > 0:
        flash(f"{affected_rows} records deleted successfully!")
    else:
        flash("No records match the criteria!")

def DELETE_PUBLISH(form):
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

    delete_query = f"DELETE FROM Publish {where_clause}"

    with conn.cursor() as cursor:
        cursor.execute(delete_query)
        affected_rows = cursor.rowcount

        select_query = "SELECT id FROM paper"
        cursor.execute(select_query)
        papers = cursor.fetchall()

        for paper in papers:
            paper_id = paper.get('id')
            select_query = f"SELECT paper_id FROM publish WHERE paper_id = '{paper_id}'"
            cursor.execute(select_query)
            result = cursor.fetchone()

            if not result:
                delete_query = f"DELETE FROM paper WHERE id = '{paper_id}'"
                affected_rows += 1
                cursor.execute(delete_query)
        
        conn.commit()

    if affected_rows > 0:
        flash(f"{affected_rows} records deleted successfully!")
    else:
        flash("No records match the criteria!")
