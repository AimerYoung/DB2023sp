# app.py

from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template, session, redirect, url_for, flash
from .forms import *
from .add import *
from .alt import *
from .delete import *
from .search import *
from .models import *
from .count import *
from flask import send_file

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

# ... 其他相关设置 ...

if __name__ == '__main__':
    app.run()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form = form, name = session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    return render_template('add/add.html', name = session.get('name')) 

@app.route('/add/teacher', methods = ['GET', 'POST'])
def add_teacher():
    form = Add_Teacher_Form()
    if form.validate_on_submit():
        ADD_TEACHER(form)
        return redirect(url_for('add_teacher'))
    return render_template('add/add_teacher.html',form = form, name = session.get('name'))

@app.route('/add/course', methods = ['GET', 'POST'])
def add_course():
    form = Add_Course_Form()
    if form.validate_on_submit():
        ADD_COURSE(form)
        return redirect(url_for('add_course'))
    return render_template('add/add_course.html', form = form, name = session.get('name'))

@app.route('/add/publish', methods = ['GET', 'POST'])
def add_publish():
    form = Add_Publish_Form()
    if form.validate_on_submit():
        ADD_PUBLISH(form)
        return redirect(url_for('add_publish'))
    return render_template('add/add_publish.html', form = form, name = session.get('name'))

@app.route('/add/teach', methods = ['GET', 'POST'])
def add_teach():
    form = Add_Teach_Form()
    if form.validate_on_submit():
        ADD_TEACH(form)
        return redirect(url_for('add_teach'))
    return render_template('add/add_teach.html', form = form, name = session.get('name'))

@app.route('/add/undertake', methods = ['GET', 'POST'])
def add_undertake():
    form = Add_Undertake_Form()
    if form.validate_on_submit():
        ADD_UNDERTAKE(form)
        return redirect(url_for('add_undertake'))
    return render_template('add/add_undertake.html', form = form, name = session.get('name'))

@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    return render_template('delete/delete.html')

@app.route('/delete/teacher', methods = ['GET', 'POST'])
def delete_teacher():
    form = Delete_Teacher_Form()
    if form.validate_on_submit():
        if form.submit_search.data:
            session['result'] = SEARCH_TEACHER(form)
            return render_template('delete/delete_teacher.html', form = form, result = session.get('result'), name = session.get('name'))
        elif form.submit_delete.data:
            DELETE_TEACHER(form)
            return render_template('delete/delete_teacher.html', form = form, name = session.get('name'))
    return render_template('delete/delete_teacher.html', form = form, name = session.get('name'))

@app.route('/delete/paper', methods = ['GET', 'POST'])
def delete_paper():
    form = Delete_Paper_Form()
    if form.validate_on_submit():
        if form.submit_search.data:
            session['result'] = SEARCH_PAPER(form)
            return render_template('delete/delete_paper.html', form = form, result = session.get('result'), name = session.get('name'))
        elif form.submit_delete.data:
            DELETE_PAPER(form)
            return render_template('delete/delete_paper.html', form = form, name = session.get('name'))
    return render_template('delete/delete_paper.html', form = form, name = session.get('name'))

@app.route('/delete/course', methods = ['GET', 'POST'])
def delete_course():
    form = Delete_Course_Form()
    if form.validate_on_submit():
        if form.submit_search.data:
            session['result'] = SEARCH_COURSE(form)
            return render_template('delete/delete_course.html', form = form, result = session.get('result'), name = session.get('name'))
        elif form.submit_delete.data:
            DELETE_COURSE(form)
            return render_template('delete/delete_course.html', form = form, name = session.get('name'))
    return render_template('delete/delete_course.html', form = form, name = session.get('name'))

@app.route('/delete/teach', methods = ['GET', 'POST'])
def delete_teach():
    form = Delete_Teach_Form()
    if form.validate_on_submit():
        if form.submit_search.data:
            session['result'] = SEARCH_TEACH(form)
            return render_template('delete/delete_teach.html', form = form, result = session.get('result'), name = session.get('name'))
        elif form.submit_delete.data:
            DELETE_TEACH(form)
            return render_template('delete/delete_teach.html', form = form, name = session.get('name'))
    return render_template('delete/delete_teach.html',form = form, name = session.get('name'))

@app.route('/delete/publish', methods = ['GET', 'POST'])
def delete_publish():
    form = Delete_Publish_Form()
    if form.validate_on_submit():
        if form.submit_search.data:
            session['result'] = SEARCH_PUBLISH(form)
            return render_template('delete/delete_publish.html', form = form, result = session.get('result'), name = session.get('name'))
        elif form.submit_delete.data:
            DELETE_PUBLISH(form)
            return render_template('delete/delete_publish.html', form = form, name = session.get('name'))
    return render_template('delete/delete_publish.html', form = form, name = session.get('name'))

@app.route('/delete/undertake', methods = ['GET', 'POST'])
def delete_undertake():
    form = Delete_Undertake_Form()
    if form.validate_on_submit():
        if form.submit_search.data:
            session['result'] = SEARCH_UNDERTAKE(form)
            return render_template('delete/delete_undertake.html', form = form, result = session.get('result'), name = session.get('name'))
        elif form.submit_delete.data:
            DELETE_UNDERTAKE(form)
            return render_template('delete/delete_undertake.html', form = form, name = session.get('name'))
    return render_template('delete/delete_undertake.html', form = form, name = session.get('name'))

@app.route('/delete/project', methods = ['GET', 'POST'])
def delete_project():
    form = Delete_Project_Form()
    if form.validate_on_submit():
        if form.submit_search.data:
            session['result'] = SEARCH_PROJECT(form)
            return render_template('delete/delete_project.html', form = form, result = session.get('result'), name = session.get('name'))
        elif form.submit_delete.data:
            DELETE_PROJECT(form)
            return render_template('delete/delete_project.html', form = form, name = session.get('name'))
    return render_template('delete/delete_project.html', form = form, name = session.get('name'))

@app.route('/alt', methods = ['GET', 'POST'])
def alt():
    return render_template('alt/alt.html')

@app.route('/alt/teacher', methods = ['GET', 'POST'])
def alt_teacher():
    form = Alt_Teacher_Form()
    if form.validate_on_submit():
        ALT_TEACHER(form)
        return redirect(url_for('alt_teacher'))
    return render_template('alt/alt_teacher.html', form = form, name = session.get('name'))

@app.route('/alt/paper', methods = ['GET', 'POST'])
def alt_paper():
    form = Alt_Paper_Form()
    if form.validate_on_submit():
        ALT_PAPER(form)
        return redirect(url_for('alt_paper'))
    return render_template('alt/alt_paper.html', form = form, name = session.get('name'))

@app.route('/alt/course', methods = ['GET', 'POST'])
def alt_course():
    form = Alt_Course_Form()
    if form.validate_on_submit():
        ALT_COURSE(form)
        return redirect(url_for('alt_course'))
    return render_template('alt/alt_course.html', form = form, name = session.get('name'))

@app.route('/alt/project', methods = ['GET', 'POST'])
def alt_project():
    form = Alt_Project_Form()
    if form.validate_on_submit():
        ALT_PROJECT(form)
        return redirect(url_for('alt_project'))
    return render_template('alt/alt_project.html', form = form, name = session.get('name')) 

@app.route('/alt/teach', methods = ['GET', 'POST'])
def alt_teach():
    form = Alt_Teach_Form()
    if form.validate_on_submit():
        ALT_TEACH(form)
        return redirect(url_for('alt_teach'))
    return render_template('alt/alt_teach.html', form = form, name = session.get('name'))

@app.route('/alt/publish', methods = ['GET', 'POST'])
def alt_publish():
    form = Alt_Publish_Form()
    if form.validate_on_submit():
        ALT_PUBLISH(form)
        return redirect(url_for('alt_publish'))
    return render_template('alt/alt_publish.html', form = form, name = session.get('name'))

@app.route('/alt/undertake', methods = ['GET', 'POST'])
def alt_undertake():
    form = Alt_Undertake_Form()
    if form.validate_on_submit():
        ALT_UNDERTAKE(form)
        return redirect(url_for('alt_undertake'))
    return render_template('alt/alt_undertake.html', form = form, name = session.get('name')) 


@app.route('/search', methods = ['GET', 'POST'])
def search():
    return render_template('search/search.html', name = session.get('name'))

@app.route('/search/teacher', methods = ['GET', 'POST'])
def search_teacher():
    form = Search_Teacher_Form()
    if form.validate_on_submit():
        session['result'] = SEARCH_TEACHER(form)
        return render_template('search/search_teacher.html', form = form, result = session.get('result'), name = session.get('name'))
    return render_template('search/search_teacher.html', form = form, name = session.get('name'))

@app.route('/search/paper', methods = ['GET', 'POST'])
def search_paper():
    form = Search_Paper_Form()
    if form.validate_on_submit():
        session['result'] = SEARCH_PAPER(form)
        return render_template('search/search_paper.html', form = form, result = session.get('result'), name = session.get('name'))
    return render_template('search/search_paper.html', form = form, name = session.get('name'))

@app.route('/search/course', methods = ['GET', 'POST'])
def search_course():
    form = Search_Course_Form()
    if form.validate_on_submit():
        session['result'] = SEARCH_COURSE(form)
        return render_template('search/search_course.html', form = form, result = session.get('result'), name = session.get('name'))
    return render_template('search/search_course.html', form = form, name = session.get('name'))

@app.route('/search/teach', methods = ['GET', 'POST'])
def search_teach():
    form = Search_Teach_Form()
    if form.validate_on_submit():
        session['result'] = SEARCH_TEACH(form)
        return render_template('search/search_teach.html', form = form, result = session.get('result'), name = session.get('name'))
    return render_template('search/search_teach.html',form = form, name = session.get('name'))

@app.route('/search/publish', methods = ['GET', 'POST'])
def search_publish():
    form = Search_Publish_Form()
    if form.validate_on_submit():
        session['result'] = SEARCH_PUBLISH(form)
        return render_template('search/search_publish.html', form = form, result = session.get('result'), name = session.get('name'))
    return render_template('search/search_publish.html', form = form, name = session.get('name'))

@app.route('/search/undertake', methods = ['GET', 'POST'])
def search_undertake():
    form = Search_Undertake_Form()
    if form.validate_on_submit():
        session['result'] = SEARCH_UNDERTAKE(form)
        return render_template('search/search_undertake.html', form = form, result = session.get('result'), name = session.get('name'))
    return render_template('search/search_undertake.html', form = form, name = session.get('name'))

@app.route('/search/project', methods = ['GET', 'POST'])
def search_project():
    form = Search_Project_Form()
    if form.validate_on_submit():
        session['result'] = SEARCH_PROJECT(form)
        return render_template('search/search_project.html', form = form, result = session.get('result'), name = session.get('name'))
    return render_template('search/search_project.html', form = form, name = session.get('name'))

@app.route('/count', methods = ['GET', 'POST'])
def count():
    form = Count_Form()
    if form.validate_on_submit():
        if form.download.data:
            COUNT_DOWNLOAD(form)
            file_path = 'report.pdf'
            return send_file(file_path, as_attachment=True)
        publish_papers, teach_courses, undertake_projects = COUNT(form) if COUNT(form) else ([], [], [])
        return render_template('count/count.html', form = form, publish_papers=publish_papers, teach_courses=teach_courses, undertake_projects=undertake_projects, name = session.get('name'))
    return render_template('count/count.html', form = form, name = session.get('name'))

   
