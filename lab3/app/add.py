from .forms import *
from .models import *
from flask import flash
from flask import redirect,url_for

def ADD_TEACHER(form: Add_Teacher_Form):
    teacher_id = form.teacher_id.data or None
    teacher_name = form.teacher_name.data or None
    teacher_gender = form.teacher_gender.data or None
    teacher_title = form.teacher_title.data or None

    if check_quotes(teacher_id):
        flash("Add Failed!!")
        flash("Teacher's ID can't include quotes!")
        return 
    if check_quotes(teacher_name):
        flash("Add Failed!!")
        flash("Teacher's Name can't include quotes!")
        return 
    
    with conn.cursor() as cursor:
        select_teacher_query = "SELECT id FROM Teacher WHERE id = %s;"
        cursor.execute(select_teacher_query, teacher_id)
        if cursor.rowcount:
            flash("This teacher has been existed! ADD Failed!!")
            flash("Go to Alt Page!")
            return 
        insert_teacher_query = "INSERT INTO teacher values (%s, %s, %s, %s);"
        cursor.execute(insert_teacher_query, (teacher_id, teacher_name, teacher_gender, teacher_title))
        conn.commit()
        flash("You have successfully added a new teacher!")
        return

def ADD_COURSE(form: Add_Course_Form):
    course_id = form.course_id.data or None
    course_name = form.course_name.data or None
    course_hours = form.course_hours.data or None
    course_type = form.course_type.data or None

    if check_quotes(course_id):
        flash("Add Failed!!")
        flash("Course's ID can't include quotes!")
        return
    if check_quotes(course_name):
        flash("Add Failed!!")
        flash("Course's Name can't include quotes!")
        return
    
    with conn.cursor() as cursor:
        select_course_query = "SELECT id FROM course WHERE id = %s;"
        cursor.execute(select_course_query, course_id)
        if cursor.rowcount:
            flash("This course has been existed! ADD Failed!!")
            flash("Go to Alt Page!")
            return 
        insert_course_query = "INSERT INTO course values (%s, %s, %s, %s);"
        cursor.execute(insert_course_query, (course_id, course_name, course_hours, course_type))
        conn.commit()
        flash("You have successfully added a new course!")
        return

def ADD_PUBLISH(form: Add_Publish_Form):
    paper_id = form.paper_id.data or None
    paper_name = form.paper_name.data or None
    paper_source = form.paper_source.data or None
    paper_date = form.paper_date.data or None
    paper_type = form.paper_type.data or None
    paper_level = form.paper_level.data or None
    teacher_id = form.teacher_id.data or None
    teacher_name = form.teacher_name.data or None
    teacher_gender = form.teacher_gender.data or None
    teacher_title = form.teacher_title.data or None
    ranking = form.ranking.data or None
    iscorrespondingauthor = form.is_corresponding_author.data or 0

    if check_quotes(paper_name):
        flash("Add Failed!!")
        flash("Paper's Name can't include quotes!")
        return
    if check_quotes(paper_source):
        flash("Add Failed!!")
        flash("Paper's Source can't include quotes!")
        return
    if paper_date:
        if not check_date_format(paper_date):
            flash("Add Failed")
            flash("Paper's Date should be like xxxx-xx-xx!")
    if check_quotes(teacher_id):
        flash("Add Failed!!")
        flash("Teacher's ID can't include quotes!")
        return 
    if check_quotes(teacher_name):
        flash("Add Failed!!")
        flash("Teacher's Name can't include quotes!")
        return   


    print()

    with conn.cursor() as cursor:
        select_paper_query = "SELECT id FROM Paper WHERE id = %s;"
        cursor.execute(select_paper_query, int(paper_id))
        existing_paper = cursor.fetchone()

    with conn.cursor() as cursor:
        select_teacher_query = "SELECT id FROM Teacher WHERE id = %s;"
        cursor.execute(select_teacher_query, teacher_id)
        existing_teacher = cursor.fetchone()

    #check if the paper_id exists
    if existing_paper:
        with conn.cursor() as cursor:
            #check if the paper-teacher record exists
            check_exits_paper_teacher = "SELECT * FROM Publish WHERE paper_id = %s AND teacher_id = %s;"
            cursor.execute(check_exits_paper_teacher, (paper_id, teacher_id))
            exits_paper_teacher = cursor.fetchone()

            if exits_paper_teacher:
                flash("This paper-teacher record has been existed! ADD Failed!!")
                flash ("If you want to change the ranking or corresponding author of this paper, please use the alter function!")
                return redirect(url_for('add_publish'))

            select_author_query = "SELECT teacher_id, ranking, iscorrespondingauthor FROM Publish WHERE paper_id = %s;"
            cursor.execute(select_author_query, (paper_id,))
            existing_authors = cursor.fetchall()

            for author in existing_authors:
                existing_ranking = author['ranking']
                existing_iscorrespondingauthor = author['iscorrespondingauthor']

                if existing_ranking == int(ranking):
                    flash("The ranking of this paper has been occupied! ADD Failed!!")
                    return redirect(url_for('add_publish'))

                if iscorrespondingauthor == 1 and existing_iscorrespondingauthor == 1:
                    flash("The corresponding author of this paper has been occupied! ADD Failed!!")
                    return redirect(url_for('add_publish'))

            insert_publish = "INSERT INTO publish (teacher_id, paper_id, ranking, iscorrespondingauthor) values (%s, %s, %s, %s);"    
            insert_paper = "UPDATE paper SET name=%s, source=%s, year=%s, type=%s, level=%s where id = %s;"        
            if existing_teacher:
                insert_teacher = "UPDATE teacher SET name=%s, gender=%s, title=%s where id = %s;"
            else:
                insert_teacher = "INSERT INTO teacher (name, gender, title, id) values (%s, %s, %s, %s);"
        
            cursor.execute(insert_publish, (teacher_id, int(paper_id), ranking, iscorrespondingauthor))
            cursor.execute(insert_paper, (paper_name, paper_source, paper_date, paper_type, paper_level, int(paper_id)))
            cursor.execute(insert_teacher, (teacher_name,teacher_gender, teacher_title, teacher_id))
            conn.commit()
            flash("You have successfully added a new paper-teacher record!")
            return redirect(url_for('add_publish'))


    insert_publish = "INSERT INTO publish (teacher_id, paper_id, ranking, iscorrespondingauthor) values (%s, %s, %s, %s);"        
    insert_paper = "INSERT INTO paper (id, name, source, year, type, level) values (%s, %s, %s, %s, %s, %s);"              
    if existing_teacher:
        insert_teacher = "UPDATE teacher SET name=%s, gender=%s, title=%s where id = %s;"
    else:
        insert_teacher = "INSERT INTO teacher (name, gender, title, id) values (%s, %s, %s, %s);"

    with conn.cursor() as cursor:
        cursor.execute(insert_publish, (teacher_id, int(paper_id), ranking, iscorrespondingauthor))
        cursor.execute(insert_paper, (int(paper_id), paper_name, paper_source, paper_date, paper_type, paper_level))
        cursor.execute(insert_teacher, ( teacher_name,teacher_gender, teacher_title, teacher_id))
        conn.commit()
        flash("You have successfully added a new paper-teacher record!")
        return redirect(url_for('add_publish'))
        
def ADD_TEACH(form: Add_Teach_Form):
    teacher_id = form.teacher_id.data or None
    course_id = form.course_id.data or None
    semester = form.semester.data or None
    academic_hours = form.academic_hours.data or None
    year = form.year.data or None
    teacher_name = form.teacher_name.data or None
    teacher_gender = form.teacher_gender.data or None
    teacher_title = form.teacher_title.data or None
    course_hours = form.course_hours.data or None
    course_name = form.course_name.data or None
    course_type = form.course_name.data or None

    if check_quotes(teacher_id):
        flash("Add Failed!!")
        flash("Teacher's ID can't include quotes!")
        return 
    if check_quotes(teacher_name):
        flash("Add Failed!!")
        flash("Teacher's Name can't include quotes!")
        return   
    if check_quotes(course_id):
        flash("Add Failed!!")
        flash("Course's ID can't include quotes!")
        return
    if check_quotes(course_name):
        flash("Add Failed!!")
        flash("Course's Name can't include quotes!")
        return
    if check_quotes(course_type):
        flash("Add Failed!!")
        flash("Course's type can't include quotes")
        
    with conn.cursor() as cursor:
        select_course_query = "SELECT id FROM course WHERE id = %s;"
        cursor.execute(select_course_query, int(course_id))
        existing_course = cursor.fetchone()

    with conn.cursor() as cursor:
        select_teacher_query = "SELECT id FROM Teacher WHERE id = %s;"
        cursor.execute(select_teacher_query, teacher_id)
        existing_teacher = cursor.fetchone()

    #check if paper exists
    if existing_course:
        with conn.cursor() as cursor:
            select_course_sum = "SELECT hours FROM course where id = %s;"
            cursor.execute(select_course_sum, (course_id))
            hours = cursor.fetchone().get('hours')
            check_exist_course_teacher = "SELECT * FROM teach WHERE course_id = %s AND teacher_id = %s;"
            cursor.execute(check_exist_course_teacher, (course_id,teacher_id))
            exits_course_teacher = cursor.fetchone()

            if exits_course_teacher:
                flash("This course-teacher record has been existed! ADD Failed!!")
                flash ("If you want to change the record, please use the alter function!")
                return redirect(url_for('add_teach'))

            #check sum <= hours
            #check ranking not repeat
            select_teacher_query = "SELECT teacher_id, academic_hours FROM teach WHERE course_id = %s AND year= %s AND semester = %s;"
            cursor.execute(select_teacher_query, (course_id, year, semester))
            existing_teachers = cursor.fetchall()

            sum = float(academic_hours)
            for teacher in existing_teachers:
                sum += teacher['academic_hours']

                if sum > hours:
                    flash("Sum of teacher's teach hours larger than courses's Total_hours!!")
                    return redirect(url_for('add_teach'))

            #insert (course exist)
            insert_teach = "INSERT INTO teach (year, semester, academic_hours, teacher_id, course_id) values (%s,%s,%s,%s,%s);"
            insert_course = "UPDATE course SET name=%s, hours=%s, type=%s WHERE id=%s;"
            if existing_teacher:
                insert_teacher = "UPDATE teacher SET name=%s, gender=%s, title=%s WHERE id=;"
            else:
                insert_teacher = "INSERT INTO teacher (name, gender, title, id) values (%s, %s, %s, %s);"
                    
            cursor.execute(insert_teach, (year, semester, float(academic_hours), teacher_id, course_id))
            cursor.execute(insert_course, (course_name, hours, course_type, course_id))
            cursor.execute(insert_teacher, (teacher_name,teacher_gender, teacher_title, teacher_id))
            conn.commit()
            flash("You have successfully added a new project-teacher record!")
            return redirect(url_for('add_publish'))

    #check enter total_cost
    if course_hours:
        flash('Enter total_hours for this course!!!')
        return redirect(url_for('add_teach'))

    if float(academic_hours) > float(course_hours):
        flash('Total_hours must be larger than sum of academic_hours!!!')
        return redirect(url_for('add_teach'))

    insert_teach = "INSERT INTO teach (year, semester, academic_hours, teacher_id, course_id) values (%s,%s,%s,%s,%s);"
    insert_course = "INSERT INTO course (id, name, hours, type) values (%s, %s, %s, %s);"
    if existing_teacher:
        insert_teacher = "UPDATE teacher SET name=%s, gender=%s, title=%s WHERE id=%s;"
    else:
        insert_teacher = "INSERT INTO teacher (name, gender, title, id) values (%s, %s, %s, %s);"

    with conn.cursor() as cursor:                
        cursor.execute(insert_teach, (year, semester, float(academic_hours), teacher_id, course_id))
        cursor.execute(insert_course, (course_id, course_name, course_hours, course_type))
        cursor.execute(insert_teacher, (teacher_name,teacher_gender, teacher_title, teacher_id))
        conn.commit()
        flash("You have successfully added a new project-teacher record!")
        return redirect(url_for('add_publish'))

def ADD_UNDERTAKE(form: Add_Undertake_Form):
    project_id = form.project_id.data or None
    project_name = form.project_name.data or None
    project_source = form.project_source.data or None
    project_type = form.project_type.data or None
    total_cost = form.total_cost.data or None
    start_year = form.start_year.data or None
    end_year = form.end_year.data or None
    teacher_id = form.teacher_id.data or None
    ranking = form.ranking.data or None
    expense = form.expense.data or None
    teacher_name = form.teacher_name.data or None
    teacher_gender = form.teacher_gender.data or None
    teacher_title = form.teacher_title.data or None

    if check_quotes(teacher_id):
        flash("Add Failed!!")
        flash("Teacher's ID can't include quotes!")
        return 
    if check_quotes(teacher_name):
        flash("Add Failed!!")
        flash("Teacher's Name can't include quotes!")
        return 
    if check_quotes(project_id):
        flash("Add Failed!!")
        flash("Project's ID can't include quotes!")
        return
    if check_quotes(project_name):
        flash("Add Failed!!")
        flash("Project's Name can't include quotes!")
        return
    if check_quotes(project_source):
        flash("Add Failed!!")
        flash("Project's Source can't include quotes!")
        return
    if not check_year_format(start_year):
        flash("Add Failed")
        flash("Project's start_year should be like xxxx!")
        return
    if not check_year_format(end_year):
        flash("Add Failed")
        flash("Project's end_year should be like xxxx!")
        return

    with conn.cursor() as cursor:
        select_project_query = "SELECT id FROM project WHERE id = %s;"
        cursor.execute(select_project_query, int(project_id))
        existing_project = cursor.fetchone()

    with conn.cursor() as cursor:
        select_teacher_query = "SELECT id FROM Teacher WHERE id = %s;"
        cursor.execute(select_teacher_query, teacher_id)
        existing_teacher = cursor.fetchone()

    #check if paper exists
    if existing_project:
        with conn.cursor() as cursor:
            select_project_sum = "SELECT total_cost FROM project where id = %s;"
            cursor.execute(select_project_sum, (project_id))
            total_cost = cursor.fetchone().get('total_cost')
            check_exist_project_teacher = "SELECT * FROM undertake WHERE project_id = %s AND teacher_id = %s;"
            cursor.execute(check_exist_project_teacher, (project_id,teacher_id))
            exits_project_teacher = cursor.fetchone()

            if exits_project_teacher:
                flash("This project-teacher record has been existed! ADD Failed!!")
                flash ("If you want to change the record, please use the alter function!")
                return redirect(url_for('add_undertake'))

            #check sum <= total
            #check ranking not repeat
            select_teacher_query = "SELECT teacher_id, ranking, expense FROM undertake WHERE project_id = %s;"
            cursor.execute(select_teacher_query, (project_id))
            existing_teachers = cursor.fetchall()

            sum = float(expense)
            for teacher in existing_teachers:
                existing_ranking = teacher['ranking']
                sum += teacher['expense']

                if existing_ranking == int(ranking):
                    flash("The ranking of this project has been occupied! ADD Failed!!")
                    return redirect(url_for('add_undertake'))
                   
                if float(sum) > float(total_cost):
                    flash("Sum of teacher's expense larger than Total_cost!!")
                    return redirect(url_for('add_undertake'))

            if start_year and end_year:    
                if int(start_year) > int(end_year):
                    flash('Start_year must be smaller than end_year!!!')
                    return redirect(url_for('add_undertake'))

            #insert (project exist)
            insert_undertake = "INSERT INTO undertake (ranking, expense, teacher_id, project_id) values (%s,%s,%s,%s);"
            insert_project = "UPDATE project SET name=%s, source=%s, type=%s, total_cost=%s, start_year=%s, end_year=%s WHERE id=%s;"
            if existing_teacher:
                insert_teacher = "UPDATE teacher SET name=%s, gender=%s, title=%s WHERE id=%s;"
            else:
                insert_teacher = "INSERT INTO teacher (name, gender, title, id) values (%s, %s, %s, %s);"

            cursor.execute(insert_undertake, (int(ranking), float(expense), teacher_id, project_id))
            cursor.execute(insert_project, (project_name, project_source, project_type, float(total_cost), start_year, end_year, project_id))
            cursor.execute(insert_teacher, (teacher_name,teacher_gender, teacher_title, teacher_id))
            conn.commit()
            flash("You have successfully added a new project-teacher record!")
            return redirect(url_for('add_publish'))

    #check enter total_cost
    if not total_cost:
        flash('Enter total_cost!!!')
        return redirect(url_for('add_undertake'))

    if float(expense) > float(total_cost):
        flash('Total_cost must be larger than sum of expense!!!')
        return redirect(url_for('add_undertake'))

    if start_year and end_year:    
        if int(start_year) > int(end_year):
            flash('Start_year must be smaller than end_year!!!')
            return redirect(url_for('add_undertake'))

    insert_undertake = "INSERT INTO undertake (ranking, expense, teacher_id, project_id) values (%s,%s,%s,%s);"
    insert_project = "INSERT INTO project (id, name, source, type, total_cost, start_year, end_year) values (%s,%s,%s,%s,%s,%s,%s);"
    if existing_teacher:
        insert_teacher = "UPDATE teacher SET name=%s, gender=%s, title=%s WHERE id=%s;"
    else:
        insert_teacher = "INSERT INTO teacher (name, gender, title, id) values (%s, %s, %s, %s);"

    with conn.cursor() as cursor:                
        cursor.execute(insert_undertake, (int(ranking), expense, teacher_id, project_id))
        cursor.execute(insert_project, (project_id, project_name, project_source, project_type, float(total_cost), start_year, end_year))
        cursor.execute(insert_teacher, (teacher_name,teacher_gender, teacher_title, teacher_id))
        conn.commit()
        flash("You have successfully added a new project-teacher record!")
        return redirect(url_for('add_publish'))


