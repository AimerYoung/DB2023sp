import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='AimerYoung@0207',
    database='teachersys',
)

cursor = connection.cursor()

drop_table_Teacher = "drop table if exists Teacher;"

create_table_Teacher = """
    /*==============================================================*/
    /* Table: Teacher                                               */
    /*==============================================================*/
    create table Teacher 
    (
        id                   char(5)                        not null,
        name                 varchar(256)                   null,                    
        gender               integer                        null,                            
        title                integer                        null,                    
        constraint PK_TEACHER primary key clustered (id)
    );
"""

drop_table_Paper = "drop table if exists Paper;"

create_table_Paper = """
    /*==============================================================*/
    /* Table: Paper                                                 */
    /*==============================================================*/
    create table Paper 
    (
        id                   integer                        not null,
        name                 varchar(256)                      null,
        source               varchar(256)                      null,
        year                 date                           null,
        type                 integer                        null,
        level                integer                        null,
        constraint PK_PAPER primary key clustered (id)
    );
"""

drop_table_Course = "drop table if exists Course;"

create_table_Course = """
    /*==============================================================*/
    /* Table: Course                                                */
    /*==============================================================*/
    create table Course 
    (
        id                   varchar(256)                      not null,
        name                 varchar(256)                      null,
        hours                integer                           null,
        type                 integer                           null,
        constraint PK_COURSE primary key clustered (id)
    );
"""

drop_table_Project = "drop table if exists Project;"

create_table_Project = """
    /*==============================================================*/
    /* Table: Project                                               */
    /*==============================================================*/
    create table Project 
    (
        id                   varchar(256)                      not null,
        name                 varchar(256)                      null,
        source               varchar(256)                      null,
        type                 integer                        null,
        total_cost           float                          null,
        start_year           integer                        null,
        end_year             integer                        null,
        constraint PK_PROJECT primary key clustered (id)
    );
"""

drop_table_Publish = "DROP TABLE IF EXISTS Publish;"

create_table_Publish = """
    CREATE TABLE Publish 
    (
       teacher_id           CHAR(5) not null,
       paper_id             INTEGER not null,
       ranking               INTEGER not null,
       iscorrespondingauthor BOOLEAN not null,
       CONSTRAINT PK_PUBLISH PRIMARY KEY CLUSTERED (teacher_id, paper_id)
    );
"""

drop_table_Teach = "drop table if exists Teach;"

create_table_Teach = """
    /*==============================================================*/
    /* Table: Teach                                                 */
    /*==============================================================*/
    create table Teach 
    (
        year                 integer                        not null,
        semester             integer                        not null,
        academic_hours       integer                        not null,
        teacher_id           char(5)                        not null,
        course_id            varchar(256)                   not null,
        constraint PK_TEACH primary key clustered (year, semester, teacher_id, course_id)
    );
"""

drop_table_Undertake = "drop table if exists UnderTake;"

create_table_Undertake = """
    /*==============================================================*/
    /* Table: Undertake                                             */
    /*==============================================================*/
    create table Undertake 
    (
        ranking                 integer                     not null,
        expense              float                          not null,
        teacher_id           char(5)                        not null,
        project_id           varchar(256)                   not null,
        constraint PK_UNDERTAKE primary key clustered (teacher_id, project_id)
    );
"""


try:
    cursor.execute(drop_table_Teacher)
    cursor.execute(create_table_Teacher)
    cursor.execute(drop_table_Paper)
    cursor.execute(create_table_Paper)
    cursor.execute(drop_table_Course)
    cursor.execute(create_table_Course)
    cursor.execute(drop_table_Project)
    cursor.execute(create_table_Project)
    cursor.execute(drop_table_Publish)
    cursor.execute(create_table_Publish)
    cursor.execute(drop_table_Teach)
    cursor.execute(create_table_Teach)
    cursor.execute(drop_table_Undertake)
    cursor.execute(create_table_Undertake)

    connection.commit()
    print("Table created successfully")
except pymysql.Error as e:
    print(f"Error creating table: {e}")
    connection.rollback()
finally:
    cursor.close()
    connection.close()