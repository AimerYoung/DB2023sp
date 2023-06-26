import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='AimerYoung@0207',
    database='teachersys',
)

cursor = connection.cursor()

publish_test1_publish = "INSERT INTO publish values ('tea01','01',1,1);"
publish_test1_teacher = "INSERT INTO teacher values ('tea01','tea01_name',1,1);"
publish_test1_paper = "INSERT INTO paper values ('01','paper01_name','paper01_source','2020-01-01',1,1);"
undertake_test1_project = "INSERT INTO project values ('01','project01_name','project01_source',1,10,2020,2021);"
undertake_test1_undertake = "INSERT INTO undertake values (1, 2, 'tea01', '01');"
teach_test1_course = "INSERT INTO course values ('01','course01_name',3,1);"
teach_test1_teach = "INSERT INTO teach values (1, 2, 1, 'tea01', '01');"

undertake_test2_project = "INSERT INTO project values ('02','project02_name','project02_source',1,15,2020,2021);"
undertake_test2_undertake = "INSERT INTO undertake values (2, 2, 'tea02', '02');"
publish_test2_publish = "INSERT INTO publish values ('tea02', '02', 2, 0)"
publish_test2_paper = "INSERT INTO paper values ('02', 'paper-2_name', 'paper02_source', '2021-02-02', 2, 3)"
publish_test3_publish = "INSERT INTO publish values ('tea01', '02', 3, 0);"

try:
    cursor.execute(publish_test1_publish)
    cursor.execute(publish_test1_teacher)
    cursor.execute(publish_test1_paper)
    cursor.execute(undertake_test1_project)
    cursor.execute(undertake_test1_undertake)
    cursor.execute(teach_test1_course)
    cursor.execute(teach_test1_teach)
    cursor.execute(undertake_test2_project)
    cursor.execute(undertake_test2_undertake)
    cursor.execute(publish_test2_paper)
    cursor.execute(publish_test2_publish)

    connection.commit()
    print("Data inited successfully")
except pymysql.Error as e:
    print(f"Error initing data: {e}")
    connection.rollback()
finally:

    cursor.close()
    connection.close()