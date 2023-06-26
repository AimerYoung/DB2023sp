# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, IntegerField, FloatField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError, Optional

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators = [DataRequired()])
    submit = SubmitField('Submit')

class Add_Teacher_Form(FlaskForm):
    teacher_id = StringField('Teacher_ID', validators = [DataRequired()])
    teacher_name = StringField('Teacher_Name')
    teacher_gender = SelectMultipleField('Teacher_Gender', choices=[('1','male'),('2','female')], validators=[Length(min=0, max=1)])
    teacher_title = SelectMultipleField('Teacher_Title', choices=[('1','postdoctoral fellow'),('2','teaching assistant'),('3','lecturer'),('4','Associate Professor'),('5','Distinguished Professor'),('6','Professor')], validators=[Length(min=0, max=1)])
    
    submit = SubmitField('Submit')

class Add_Course_Form(FlaskForm):
    course_id = StringField('Course_ID', validators = [DataRequired()])
    course_name = StringField('Course_Name')
    course_hours = IntegerField('Course_Hours', validators=[Optional()])
    course_type = StringField('Course_Type')

    submit = SubmitField('Submit')

class Add_Publish_Form(FlaskForm):
    paper_id = IntegerField('Paper_ID(supposed to be an integer)')
    paper_name = StringField('Paper_Name')
    paper_source = StringField('Paper_Source')
    paper_date = StringField('Paper_Date(xxxx-xx-xx)')
    paper_type = SelectMultipleField('Paper_Type', choices=[('1','1-full paper'),('2','2-short paper'),('3','3-poster paper'),('4','4-demo paper')], validators=[Length(min=0, max=1)])
    paper_level = SelectMultipleField('Paper_Level', choices=[('1','1-CCF-A'),('2','2-CCF-B'),('3','3-CCF-C'),('4','4-Chinese-CCF-A'),('5','5-Chinese-CCFB'),('6','NO level')], validators=[Length(min=0, max=1)])
    teacher_id = StringField('Teacher_ID', validators = [DataRequired()])
    teacher_name = StringField('Teacher_Name')
    teacher_gender = SelectMultipleField('Teacher_Gender', choices=[('1','male'),('2','female')], validators=[Length(min=0, max=1)])
    teacher_title = SelectMultipleField('Teacher_Title', choices=[('1','postdoctoral fellow'),('2','teaching assistant'),('3','lecturer'),('4','Associate Professor'),('5','Distinguished Professor'),('6','Professor')], validators=[Length(min=0, max=1)])
    ranking = StringField('Ranking(supposed to be an integer)', validators = [DataRequired()])
    is_corresponding_author = BooleanField('Is Corresponding Author')
    
    submit = SubmitField('Submit')

class Add_Teach_Form(FlaskForm):
    teacher_id = StringField('Teacher_ID', validators = [DataRequired()])
    course_id = StringField('Course_ID', validators = [DataRequired()])
    semester = SelectMultipleField('Semester', choices=[('1', 'Spring'),('2','Summer'),('3','Fall')], validators=[Length(min=0, max=1)])
    academic_hours = IntegerField('Academic_Hours', validators=[Optional()])
    year =IntegerField('Year(xxxx)', validators=[Optional()])
    teacher_name = StringField('Teacher_Name')
    teacher_gender = SelectMultipleField('Teacher_Gender', choices=[('1','male'),('2','female')], validators=[Length(min=0, max=1)])
    teacher_title = SelectMultipleField('Teacher_Title', choices=[('1','postdoctoral fellow'),('2','teaching assistant'),('3','lecturer'),('4','Associate Professor'),('5','Distinguished Professor'),('6','Professor')], validators=[Length(min=0, max=1)])
    course_hours = IntegerField('Course_Hours', validators=[Optional()])
    course_name = StringField('Course_Name')
    course_type = StringField('Course_Type')
    
    submit = SubmitField('Submit')

class Add_Undertake_Form(FlaskForm):
    project_id = StringField('Project_ID', validators = [DataRequired()])
    project_name = StringField('Project_Name')
    project_source = StringField('Project_Source')
    project_type = SelectMultipleField('Project_Type', choices=[('1','National project'),('2','Provincial and ministerial level projects'),('3','City Hall Project'),('4','Enterprise cooperation project'),('5','Other types of projects')])
    total_cost = FloatField('Total_Cost', validators=[Optional()])
    start_year = IntegerField('Start_Year(xxxx)', validators=[Optional()])
    end_year = IntegerField('End_Year(xxxx)', validators=[Optional()])
    teacher_id = StringField('Teacher_ID', validators = [DataRequired()])
    teacher_name = StringField('Teacher_Name')
    teacher_gender = SelectMultipleField('Teacher_Gender', choices=[('1','male'),('2','female')], validators=[Length(min=0, max=1)])
    teacher_title = SelectMultipleField('Teacher_Title', choices=[('1','postdoctoral fellow'),('2','teaching assistant'),('3','lecturer'),('4','Associate Professor'),('5','Distinguished Professor'),('6','Professor')], validators=[Length(min=0, max=1)])
    ranking = IntegerField('Ranking')
    expense = FloatField('Expense')

    submit = SubmitField('Submit')

class Search_Teacher_Form(FlaskForm):
    teacher_id = StringField('Teacher_ID')
    teacher_name = StringField('Teacher_Name')
    teacher_gender = SelectMultipleField('Teacher_Gender', choices=[('1','male'),('2','female')], validators=[Length(min=0, max=1)])
    teacher_title = SelectMultipleField('Teacher_Title', choices=[('1','postdoctoral fellow'),('2','teaching assistant'),('3','lecturer'),('4','Associate Professor'),('5','Distinguished Professor'),('6','Professor')], validators=[Length(min=0, max=1)])    

    submit = SubmitField('Submit')

class Search_Paper_Form(FlaskForm):
    paper_id = IntegerField('Paper_ID', validators=[Optional()])
    paper_name = StringField('Paper_Name')
    source = StringField('Source')
    year = StringField('Year')
    paper_type = SelectMultipleField('Paper_Type', choices=[('1','1-full paper'),('2','2-short paper'),('3','3-poster paper'),('4','4-demo paper')], validators=[Length(min=0, max=1)])
    paper_level = SelectMultipleField('Paper_Level', choices=[('1','1-CCF-A'),('2','2-CCF-B'),('3','3-CCF-C'),('4','4-Chinese-CCF-A'),('5','5-Chinese-CCFB'),('6','NO level')], validators=[Length(min=0, max=1)])
    
    submit = SubmitField('Submit')

class Search_Project_Form(FlaskForm):
    project_id = StringField('Project_ID')
    project_name = StringField('Project_Name')
    source = StringField('Source')
    project_type = SelectMultipleField('Project_Type', choices=[('1','National project'),('2','Provincial and ministerial level projects'),('3','City Hall Project'),('4','Enterprise cooperation project'),('5','Other types of projects')])
    total_cost = StringField('Total_Cost')
    start_year = IntegerField('Start_Year(xxxx)', validators=[Optional()])
    end_year = IntegerField('End_Year(xxxx)', validators=[Optional()])

    submit = SubmitField('Submit')

class Search_Course_Form(FlaskForm):
    course_id = StringField('Course ID')
    course_name = StringField('Course Name')
    course_hours = IntegerField('Course Hours', validators=[Optional()])
    course_type = StringField('Course Type')

    submit = SubmitField('Search')

class Search_Teach_Form(FlaskForm):
    teacher_id = StringField('Teacher ID')
    course_id = StringField('Course ID')
    year = IntegerField('Year', validators=[Optional()])
    semester = SelectMultipleField('Semester', choices=[('1', 'Spring'),('2','Summer'),('3','Fall')], validators=[Length(min=0, max=1)])
    academic_hours = IntegerField('Academic Hours', validators=[Optional()])

    submit = SubmitField('Search')

class Search_Undertake_Form(FlaskForm):
    teacher_id = StringField('Teacher ID')
    project_id = StringField('Project ID')
    ranking = IntegerField('Ranking', validators=[Optional()])
    expense = FloatField('Expense', validators=[Optional()])

    submit = SubmitField('Search')

class Search_Publish_Form(FlaskForm):
    teacher_id = StringField('Teacher ID')
    paper_id = IntegerField('Paper ID', validators=[Optional()])
    ranking = IntegerField('Ranking', validators=[Optional()])
    is_corresponding_author = BooleanField('Is Corresponding Author')

    submit = SubmitField('Search')

class Delete_Teacher_Form(FlaskForm):
    teacher_id = StringField('Teacher ID')
    teacher_name = StringField('Teacher Name')
    teacher_gender = SelectMultipleField('Teacher Gender', choices=[('1', 'Male'), ('2', 'Female')], validators=[Length(min=0, max=1)])
    teacher_title = SelectMultipleField('Teacher Title', choices=[('1', 'Postdoctoral Fellow'), ('2', 'Teaching Assistant'), ('3', 'Lecturer'), ('4', 'Associate Professor'), ('5', 'Distinguished Professor'), ('6', 'Professor')], validators=[Length(min=0, max=1)])    

    submit_search = SubmitField('Search')
    submit_delete = SubmitField('Delete')

class Delete_Paper_Form(FlaskForm):
    paper_id = IntegerField('Paper ID', validators=[Optional()])
    paper_name = StringField('Paper Name')
    source = StringField('Source')
    year = StringField('Year')
    paper_type = SelectMultipleField('Paper Type', choices=[('1', 'Full Paper'), ('2', 'Short Paper'), ('3', 'Poster Paper'), ('4', 'Demo Paper')], validators=[Length(min=0, max=1)])
    paper_level = SelectMultipleField('Paper Level', choices=[('1', 'CCF-A'), ('2', 'CCF-B'), ('3', 'CCF-C'), ('4', 'Chinese CCF-A'), ('5', 'Chinese CCF-B'), ('6', 'No Level')], validators=[Length(min=0, max=1)])
    
    submit_search = SubmitField('Search')
    submit_delete = SubmitField('Delete')

class Delete_Project_Form(FlaskForm):
    project_id = StringField('Project ID')
    project_name = StringField('Project Name')
    source = StringField('Source')
    project_type = SelectMultipleField('Project Type', choices=[('1', 'National Project'), ('2', 'Provincial and Ministerial Level Projects'), ('3', 'City Hall Project'), ('4', 'Enterprise Cooperation Project'), ('5', 'Other Types of Projects')])
    total_cost = StringField('Total Cost')
    start_year = IntegerField('Start Year (xxxx)', validators=[Optional()])
    end_year = IntegerField('End Year (xxxx)', validators=[Optional()])

    submit_search = SubmitField('Search')
    submit_delete = SubmitField('Delete')

class Delete_Course_Form(FlaskForm):
    course_id = StringField('Course ID')
    course_name = StringField('Course Name')
    course_hours = IntegerField('Course Hours', validators=[Optional()])
    course_type = StringField('Course Type')

    submit_search = SubmitField('Search')
    submit_delete = SubmitField('Delete')

class Delete_Teach_Form(FlaskForm):
    teacher_id = StringField('Teacher ID')
    course_id = StringField('Course ID')
    year = IntegerField('Year', validators=[Optional()])
    semester = SelectMultipleField('Semester', choices=[('1', 'Spring'),('2','Summer'),('3','Fall')], validators=[Length(min=0, max=1)])
    academic_hours = IntegerField('Academic Hours', validators=[Optional()])

    submit_search = SubmitField('Search')
    submit_delete = SubmitField('Delete')

class Delete_Undertake_Form(FlaskForm):
    teacher_id = StringField('Teacher ID')
    project_id = StringField('Project ID')
    ranking = IntegerField('Ranking', validators=[Optional()])
    expense = FloatField('Expense', validators=[Optional()])

    submit_search = SubmitField('Search')
    submit_delete = SubmitField('Delete')

class Delete_Publish_Form(FlaskForm):
    teacher_id = StringField('Teacher ID')
    paper_id = IntegerField('Paper ID', validators=[Optional()])
    ranking = IntegerField('Ranking', validators=[Optional()])
    is_corresponding_author = BooleanField('Is Corresponding Author')

    submit_search = SubmitField('Search')
    submit_delete = SubmitField('Delete')

class Alt_Teacher_Form(FlaskForm):
    teacher_id = StringField('Select with Teacher_ID:', validators = [DataRequired()])
    teacher_name = StringField('Teacher_Name')
    teacher_gender = SelectMultipleField('Teacher_Gender', choices=[('1','male'),('2','female')], validators=[Length(min=0, max=1)])
    teacher_title = SelectMultipleField('Teacher_Title', choices=[('1','postdoctoral fellow'),('2','teaching assistant'),('3','lecturer'),('4','Associate Professor'),('5','Distinguished Professor'),('6','Professor')], validators=[Length(min=0, max=1)])

    submit = SubmitField('Submit')

class Alt_Project_Form(FlaskForm):
    project_id  = StringField('Select with Project_ID:', validators = [DataRequired()])
    project_name = StringField('Project_Name')
    project_source = StringField('Project_Source')
    project_type = SelectMultipleField('Project_Type', choices=[('1','National project'),('2','Provincial and ministerial level projects'),('3','City Hall Project'),('4','Enterprise cooperation project'),('5','Other types of projects')])
    total_cost = FloatField('Total_Cost', validators=[Optional()])
    start_year = IntegerField('Start_Year(xxxx)', validators=[Optional()])
    end_year = IntegerField('End_Year(xxxx)', validators=[Optional()])

    submit = SubmitField('Submit')

class Alt_Paper_Form(FlaskForm):
    paper_id = IntegerField('Select with Paper_ID:')
    paper_name = StringField('Paper_Name')
    paper_source = StringField('Paper_Source')
    year = StringField('Year(xxxx-xx-xx)')
    paper_type = SelectMultipleField('Paper_Type', choices=[('1','1-full paper'),('2','2-short paper'),('3','3-poster paper'),('4','4-demo paper')], validators=[Length(min=0, max=1)])
    paper_level = SelectMultipleField('Paper_Level', choices=[('1','1-CCF-A'),('2','2-CCF-B'),('3','3-CCF-C'),('4','4-Chinese-CCF-A'),('5','5-Chinese-CCFB'),('6','NO level')], validators=[Length(min=0, max=1)])

    submit = SubmitField('Submit')

class Alt_Course_Form(FlaskForm):
    course_id = StringField('Select with Course_ID', validators = [DataRequired()])
    course_name = StringField('Course_Name')
    course_hours = IntegerField('Course_Hours', validators=[Optional()])
    course_type = StringField('Course_Type')

    submit = SubmitField('Submit')

class Alt_Teach_Form(FlaskForm):
    teacher_id = StringField('Teacher_ID', validators=[Optional()])
    course_id = StringField('Course_ID', validators=[Optional()])
    year = IntegerField('Year', validators=[Optional()])
    semester = SelectMultipleField('Semester', choices=[('1', 'Spring'),('2','Summer'),('3','Fall')], validators=[Length(min=0, max=1)])
    academic_hours = FloatField('Academic_Hours', validators=[Optional()])
    
    submit = SubmitField('Submit')

class Alt_Undertake_Form(FlaskForm):
    teacher_id = StringField('Teacher_ID', validators=[DataRequired()])
    project_id = StringField('Project_ID', validators=[DataRequired()])
    ranking = IntegerField('Ranking', validators=[Optional()])
    expense = FloatField('Expense', validators=[Optional()])

    submit = SubmitField('Submit')

class Alt_Publish_Form(FlaskForm):
    teacher_id = StringField('Teacher_ID', validators=[DataRequired()])
    paper_id = IntegerField('Paper_ID')
    ranking = IntegerField('Ranking', validators=[Optional()])
    is_corresponding_author = SelectMultipleField('Is_Corresponding_Author', choices=[('1','Yes'),('0','No')], validators=[Length(min=0, max=1)])

    submit = SubmitField('Submit')

class Count_Form(FlaskForm):
    teacher_id = StringField('Teacher ID', validators=[DataRequired()]) 
    start_year = IntegerField('Start Year', validators=[Optional()])
    end_year = IntegerField('End Year', validators=[Optional()])

    submit = SubmitField('Submit')   
    download = SubmitField('Download')





