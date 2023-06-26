from .forms import *
from .models import *
from flask import flash
from flask import redirect,url_for

def ALT_TEACHER(form: Alt_Teacher_Form):
    id = form.teacher_id.data 
    name = form.teacher_name.data or None
    gender = form.teacher_gender.data or None
    title = form.teacher_title.data or None    

    if check_quotes(id):
        flash("Add Failed!!")
        flash("Teacher's ID can't include quotes!")
        return 
    if check_quotes(name):
        flash("Add Failed!!")
        flash("Teacher's Name can't include quotes!")
        return 

    with conn.cursor() as cursor:
        select_teacher_query = "SELECT * FROM teacher WHERE id = %s;"
        cursor.execute(select_teacher_query, (id))
        if cursor.rowcount == 0:
            flash("ALT failed! Teacher not found!")
            return
        if name:
            cursor.execute("UPDATE teacher set name = %s WHERE id = %s;", (name, id))
        if gender:
            cursor.execute("UPDATE teacher set gender = %s WHERE id = %s", (gender, id))
        if title:
            cursor.execute("UPDATE teacher set title = %s WHERE id = %s", (title, id))
        
        conn.commit()
        flash("ALT success!")
        return 
    
def ALT_PROJECT(form: Alt_Project_Form):
    id = form.project_id.data
    name = form.project_name.data or None
    source = form.project_source.data or None
    type = form.project_type.data or None
    total_cost = form.total_cost.data or None
    start_year = form.start_year.data or None
    end_year = form.end_year.data or None

    if check_quotes(id):
        flash("Add Failed!!")
        flash("Project's ID can't include quotes!")
        return
    if check_quotes(name):
        flash("Add Failed!!")
        flash("Project's Name can't include quotes!")
        return
    if check_quotes(source):
        flash("Add Failed!!")
        flash("Project's Source can't include quotes!")
        return
    if start_year:
        if not check_year_format(start_year):
            flash("Add Failed!!")
            flash("Project's Start_year must be in the form of xxxx!")
            return
    if end_year:
        if not check_year_format(end_year):
            flash("Add Failed!!")
            flash("Project's End_year must be in the form of xxxx!")
            return

    with conn.cursor() as cursor:
        select_project_query = "SELECT * FROM project WHERE id = %s;"
        cursor.execute(select_project_query, (id))
        if cursor.rowcount == 0:
            flash("ALT failed! Project not found!")
            return
        if name:
            cursor.execute("UPDATE project set name = %s WHERE id = %s;", (name, id))
        if source:
            cursor.execute("UPDATE project set source = %s WHERE id = %s", (source, id))
        if type:
            cursor.execute("UPDATE project set type = %s WHERE id = %s", (type, id))
        if total_cost:
            cursor.execute("UPDATE project set total_cost = %s WHERE id = %s", (total_cost, id))
            cursor.execute("SELECT * FROM undertake WHERE project_id = %s;", (id))
            results = cursor.fetchall()
            sum = 0
            for result in results:
                sum += float(result['expense'])
            if sum > float(total_cost):
                flash('ALT Failed!!')
                flash('Total_cost must be larger than sum of expense!!!')
                return
        if start_year:
            cursor.execute("UPDATE project set start_year = %s WHERE id = %s", (start_year, id))
            cursor.execute("SELECT end_year FROM project WHERE id = %s", (id))
            end_year = cursor.fetchone()['end_year']
            if start_year and end_year and int(start_year) > int(end_year):
                flash('Start_year must be smaller than end_year!!!')
                return 
        if end_year:
            cursor.execute("UPDATE project set end_year = %s WHERE id = %s", (end_year, id))
            cursor.execute("SELECT start_year FROM project WHERE id = %s", (id))
            start_year = cursor.fetchone()['start_year']
            if start_year and end_year and int(start_year) > int(end_year):
                flash('Start_year must be smaller than end_year!!!')
                return 
        
        conn.commit()
        flash("ALT success!")
        return 

def ALT_PAPER(form: Alt_Paper_Form):
    id = form.paper_id.data
    name = form.paper_name.data or None
    source = form.paper_source.data or None
    year = form.year.data or None
    type = form.paper_type.data or None
    level = form.paper_level.data or None

    if check_quotes(name):
        flash("Add Failed!!")
        flash("Paper's Name can't include quotes!")
        return
    if check_quotes(source):
        flash("Add Failed!!")
        flash("Paper's Source can't include quotes!")
        return
    if not check_date_format(year):
        flash("Add Failed!!")
        flash("Paper's Year must be in the form of xxxx!")
        return


    with conn.cursor() as cursor:
        select_paper_query = "SELECT * FROM paper WHERE id = %s;"
        cursor.execute(select_paper_query, (id))
        if cursor.rowcount == 0:
            flash("ALT failed! Paper not found!")
            return
        if name:
            cursor.execute("UPDATE paper set name = %s WHERE id = %s;", (name, id))
        if source:
            cursor.execute("UPDATE paper set source = %s WHERE id = %s", (source, id))
        if year:
            cursor.execute("UPDATE paper set year = %s WHERE id = %s", (year, id))
        if type:
            cursor.execute("UPDATE paper set type = %s WHERE id = %s", (type, id))
        if level:
            cursor.execute("UPDATE paper set level = %s WHERE id = %s", (level, id))

        conn.commit()
        flash("ALT success!")
        return

def ALT_COURSE(form: Alt_Course_Form):
    id = form.course_id.data
    name = form.course_name.data or None
    hours = form.course_hours.data or None
    type = form.course_type.data or None
    
    if check_quotes(name):
        flash("Add Failed!!")
        flash("Course's Name can't include quotes!")
        return
    if check_quotes(id):
        flash("Add Failed!!")
        flash("Course's ID can't include quotes!")
        return
    if check_quotes(type):
        flash("Add Failed!!")
        flash("Course's Type can't include quotes!")
        return

    with conn.cursor() as cursor:
        select_course_query = "SELECT * FROM course WHERE id = %s;"
        cursor.execute(select_course_query, (id))
        if cursor.rowcount == 0:
            flash("ALT failed! Course not found!")
            return
        if name:
            cursor.execute("UPDATE course set name = %s WHERE id = %s;", (name, id))
        if hours:
            cursor.execute("UPDATE course set hours = %s WHERE id = %s", (hours, id))
            
            cursor.execute("SELECT * FROM teach WHERE course_id = %s;", (id))
            results = cursor.fetchall()
            sum = 0
            for result in results:
                sum += int(result['academic_hours'])
            if sum > int(hours):
                flash('ALT Failed!!')
                flash('Total_hours must be larger than sum of academic_hours!!!')
                return
        if type:
            cursor.execute("UPDATE course set type = %s WHERE id = %s", (type, id))

        conn.commit()
        flash("ALT success!")
        return
    
def ALT_TEACH(form: Alt_Course_Form):
    teacher_id = form.teacher_id.data or None
    course_id = form.course_id.data or None
    year = form.year.data or None
    semester = form.semester.data or None
    academic_hours = form.academic_hours.data or None

    condition = []
    if teacher_id:
        condition.append(f"teacher_id = '{ teacher_id }'")
    if course_id:
        condition.append(f"course_id = '{ course_id }'")
    if not condition:
        where_clause = ""
    else:
        where_clause = "WHERE " + "AND ".join(condition)

    with conn.cursor() as cursor:
        select_query = "SELECT * FROM teach WHERE teacher_id = %s AND course_id = %s;"
        cursor.execute(select_query, (teacher_id, course_id))
        if cursor.rowcount == 0:
            flash("ALT failed! Teach record not found!")
            return

        if year:
            cursor.execute(f"UPDATE teach SET year = { year } { where_clause };")
        if semester:
            cursor.execute(f"UPDATE teach SET semester = { semester } { where_clause };")
        if academic_hours:
            select_course_query = "SELECT hours FROM course WHERE id = %s;"
            cursor.execute(select_course_query, (course_id))
            course_hours = cursor.fetchone()['hours']
    
            select_teach_query = "SELECT * FROM teach WHERE course_id = %s AND teacher_id <> %s;"
            cursor.execute(select_teach_query, (course_id, teacher_id))
            teaches = cursor.fetchall()
            sum = float(academic_hours)
            for teach in teaches:
                sum += teach.academic_hours
                if sum > course_hours:
                    flash('ALT Failed!!')
                    flash('Total_hours must be larger than sum of academic_hours!!!')
                    return
            cursor.execute(f"UPDATE teach SET academic_hours = { academic_hours } { where_clause };")
        conn.commit()
        flash("ALT success!")
        return
        

def ALT_UNDERTAKE(form: Alt_Undertake_Form):
    teacher_id = form.teacher_id.data
    project_id = form.project_id.data
    expense = form.expense.data or None
    ranking = form.ranking.data or None
    
    condition = []
    condition.append(f"teacher_id = '{ teacher_id }'")
    condition.append(f"project_id = '{project_id }'")
    where_clause = "WHERE " + "AND ".join(condition)

    with conn.cursor() as cursor:
        select_query = "SELECT * FROM undertake WHERE teacher_id = %s AND project_id = %s;"
        cursor.execute(select_query, (teacher_id, project_id))
        if cursor.rowcount == 0:
            flash("ALT failed! Undertake record not found!")
            return

        if expense:
            sum = float(expense)
            select_project_query = "SELECT total_cost FROM project WHERE id = %s;"
            cursor.execute(select_project_query, (project_id))
            total_cost = cursor.fetchone()['total_cost']
            select_undertake_query = "SELECT * FROM undertake WHERE project_id = %s AND teacher_id <> %s;"
            cursor.execute(select_undertake_query, (project_id, teacher_id))
            undertakes = cursor.fetchall()
            for undertake in undertakes:
                sum += float(undertake['expense'])
                if sum > total_cost:
                    flash('ALT Failed!!')
                    flash('Total_cost must be larger than sum of expense!!!')
                    return
            cursor.execute(f"UPDATE undertake SET expense = { expense } { where_clause };")
        if ranking:
            select_undertake_query = "SELECT * FROM undertake WHERE project_id = %s;"
            cursor.execute(select_undertake_query, (project_id))
            undertakes = cursor.fetchall()
            for undertake in undertakes:
                if ranking == undertake['ranking']:
                    flash('ALT Failed!!')
                    flash('Ranking must be unique!!!')
                    return
            cursor.execute(f"UPDATE undertake SET ranking = { ranking } { where_clause };") 
        conn.commit()
        flash("ALT success!")
        return

def ALT_PUBLISH(form: Alt_Publish_Form):
    teacher_id = form.teacher_id.data or None
    paper_id = form.paper_id.data or None
    ranking = form.ranking.data or None
    is_corresponding_author = int(form.is_corresponding_author.data[0]) if form.is_corresponding_author.data else None

    condition = []
    if teacher_id:
        condition.append(f"teacher_id = '{ teacher_id }'")
    if paper_id:
        condition.append(f"paper_id = '{ paper_id }'")
    if not condition:
        where_clause = ""
    else:
        where_clause = "WHERE " + "AND ".join(condition)

    with conn.cursor() as cursor:
        if ranking:
            select_publish_query = "SELECT * FROM publish WHERE paper_id = %s;"
            cursor.execute(select_publish_query, (paper_id))
            publishes = cursor.fetchall()
            for publish in publishes:
                if ranking == publish['ranking']:
                    flash('ALT Failed!!')
                    flash('Ranking must be unique!!!')
                    return
            cursor.execute(f"UPDATE publish SET ranking = { ranking } { where_clause };")
        if is_corresponding_author == 1:
            select_publish_query = "SELECT * FROM publish WHERE paper_id = %s;"
            cursor.execute(select_publish_query, (paper_id))
            publishes = cursor.fetchall()
            for publish in publishes:
                if publish['iscorrespondingauthor'] == 1:
                    flash('ALT Failed!!')
                    flash('Corresponding_author must be unique!!!')
                    return redirect(url_for('alt_publish'))
        cursor.execute(f"UPDATE publish SET iscorrespondingauthor = { is_corresponding_author } { where_clause };")
        
        conn.commit()
        flash("ALT success!")
        return