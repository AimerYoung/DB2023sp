




<h1 align = "center">教师教学科研等级系统</h1>











<h2 align = "center">系统设计与实现报告</h2>

​	







<div style="page-break-after:always;">

<h3 align = "center">姓名：葛哲凯</h3>

<h3 align = "center">学号：PB20000126</h3>









<h3 align = "center">计算机科学与技术学院</h3>

<h3 align = "center">中国科学技术大学</h3>

<h3 align = "center">2023年6月</h3>

<div style="page-break-after:always;"></div>

<h1 align = "center">目录</h1>

### 1. [概述](#overview)

#### 1.1 [系统目标](#system-objectives)

#### 1.2 [需求说明](#requirements)

#### 1.3 [本报告的主要贡献](#MainContribution)

### 2. [总体设计](#OverallDesign)

#### 2.1 [系统模块结构](#System-Module-Structure)

#### 2.2 [系统工作流程](#System-Workflow)

#### 2.3 [数据库设计](#Database-Design)

### 3. [详细设计](#Detailed-Design)

#### 3.1 [用户模块](#User-Module)

#### 3.2 [增添模块](#Add-Module)

#### 3.3 [删除模块](#Delete-Module)

#### 3.4 [修改模块](#****-模块)

#### 3.5 [查找模块](#Search-Module)

#### 3.6 [统计模块](#Count-Module)

### 4. [实现与测试](#Implementation-Testing)

#### 4.1 [实现结果](#Implementation-Result)

#### 4.2 [测试结果](#Test-Result)

#### 4.3 [实现中的难点问题及解决](#Issues-Solutions)

### 5. [总结与讨论](#Summary-Discussion)

<div style="page-break-after:always;"></div>

# <a name="overview"></a>1 概述

### <a name="system-objectives"></a>1.1 系统目标

​		本系统主要目标为开发一个教师教学科研等级系统。采用B/S架构，Python语言，前端开发框架为Flask，后端DBMS采用Mysql 

### <a name="requirements"></a>1.2 需求说明

#### 1.2.1 数据需求

1. 数据库名称：teachersys
2. 表格结构：
   - Teacher表：存储教师信息
     - 字段：id（教师ID，字符型，长度为5，非空），name（教师姓名，字符串型，最大长度256，可为空），gender（性别，整数型，可为空），title（职称，整数型，可为空）
     - 主键：id
   - Paper表：存储论文信息
     - 字段：id（论文ID，整数型，非空），name（论文名称，字符串型，最大长度256，可为空），source（来源，字符串型，最大长度256，可为空），year（发表年份，日期型，可为空），type（类型，整数型，可为空），level（级别，整数型，可为空）
     - 主键：id
   - Course表：存储课程信息
     - 字段：id（课程ID，字符串型，最大长度256，非空），name（课程名称，字符串型，最大长度256，可为空），hours（学时，整数型，可为空），type（类型，整数型，可为空）
     - 主键：id
   - Project表：存储项目信息
     - 字段：id（项目ID，字符串型，最大长度256，非空），name（项目名称，字符串型，最大长度256，可为空），source（来源，字符串型，最大长度256，可为空），type（类型，整数型，可为空），total_cost（总成本，浮点型，可为空），start_year（开始年份，整数型，可为空），end_year（结束年份，整数型，可为空）
     - 主键：id
   - Publish表：存储教师与论文之间的关联关系
     - 字段：teacher_id（教师ID，字符型，长度为5，非空），paper_id（论文ID，整数型，非空），ranking（排名，整数型，非空），iscorrespondingauthor（是否为通讯作者，布尔型，非空）
     - 主键：(teacher_id, paper_id)
   - Teach表：存储教师与课程之间的关联关系
     - 字段：year（年份，整数型，非空），semester（学期，整数型，非空），academic_hours（学时，整数型，非空），teacher_id（教师ID，字符型，长度为5，非空），course_id（课程ID，字符串型，最大长度256，非空）
     - 主键：(year, semester, teacher_id, course_id)
   - Undertake表：存储教师与项目之间的关联关系
     - 字段：ranking（排名，整数型，非空），expense（费用，浮点型，非空），teacher_id（教师ID，字符型，长度为5，非空），project_id（项目ID，字符串型，最大长度256，非空）
     - 主键：(teacher_id, project_id)
3. 数据完整性约束：
   - Teacher表：主键为id，保证每个教师记录的唯一性。
   - Paper表：主键为id，保证每篇论文记录的唯一性。
   - Course表：主键为id，保证每门课程记录的唯一性。
   - Project表：主键为id，保证每个项目记录的唯一性。
   - Publish表：主键为(teacher_id, paper_id)，确保每个教师与论文的关联记录的唯一性。
   - Teach表：主键为(year, semester, teacher_id, course_id)，确保每个教师与课程的关联记录的唯一性。
   - Undertake表：主键为(teacher_id, project_id)，确保每个教师与项目的关联记录的唯一性。

#### 1.2.2 功能需求	

- 登记发表论文情况：提供教师论文发表信息的的增、删、改、查功能；输入时要求检 查：一篇论文只能有一位通讯作者，论文的作者排名不能有重复，论文的类型和级别只 能在约定的取值集合中选取（实现时建议用下拉框）。
- 登记承担项目情况：提供教师承担项目信息的增、删、改、查功能；输入时要求检查： 排名不能有重复，一个项目中所有教师的承担经费总额应等于项目的总经费，项目类型 只能在约定的取值集合中选取。 
- 登记主讲课程情况：提供教师主讲课程信息的增、删、改、查功能；输入时要求检查： 一门课程所有教师的主讲学时总额应等于课程的总学时，学期。 
- 实现按教师工号和给定年份范围汇总查询该教师的教学科研情况的功能；例如输入 工号“01234”，“2023-2023”可以查询 01234 教师在 2023 年度的教学科研工 作情况。 

#### 1.2.3 附加实现

- 实现按教师工号和给定年份范围生成教学科研工作量统计表并导出文档的 功能，导出文档格式可以是 PDF、Word、Excel 



### <a name = "MainContribution"></a>1.3 本报告的主要贡献

​		本报告主要根据需求提供相应的体系架构设计，概述数据库设计、数据库实现、具体变成细节以及网页设计与实现。并根据具体实现细节提供相关功能的说明，展示最终效果。

<div style="page-break-after:always;"></div>

# <a name = "OverallDesign"></a>2 总体设计

###  <a name = "System-Module-Structure"></a>2.1 系统模块结构

![image-20230621165119667](C:\Users\AimerYoung\AppData\Roaming\Typora\typora-user-images\image-20230621165119667.png)

- Web前端部分实现用户交互界面，提供相关接口操作
- 服务器处理前端的操作请求，与数据库进行交互，实现下述子模块的功能：
  - 增添记录
  - 删除记录
  - 修改记录
  - 查找记录
  - 统计查找
- 数据库模块提供了上述信息的存储结构，并且通过事务过程，实现在数据库部分的功能

### <a name = "System-Workflow"></a>2.2 系统工作流程

![image-20230621170559115](C:\Users\AimerYoung\AppData\Roaming\Typora\typora-user-images\image-20230621170559115.png)

<div style="page-break-after:always;"></div>

## <a name = "Database-Design"></a>2.3 数据库设计

**E-R概念模型：**

![image-20230621105411250](C:\Users\AimerYoung\AppData\Roaming\Typora\typora-user-images\image-20230621105411250.png)

**PDM:**

![PDM](C:\Users\AimerYoung\OneDrive\USTC\大三下\数据库系统及应用\lab\lab3\doc\PDM.png)

<div style="page-break-after:always;"></div>

# <a name = "Detailed-Design"></a>3 详细设计

### <a name = "User-Module"></a>3.1 用户模块

##### 功能：提供系统使用者的注册功能

##### 详细：对于未输入姓名的，显示Stranger，否则显示输入的姓名

##### URL:http://localhost:5000/

##### 展示：![image-20230621171608002](C:\Users\AimerYoung\AppData\Roaming\Typora\typora-user-images\image-20230621171608002.png)

![image-20230621171620991](C:\Users\AimerYoung\AppData\Roaming\Typora\typora-user-images\image-20230621171620991.png)

### <a name = "Add-Module"></a>3.2 增添模块

- ##### 功能：提供对教师、课程、发表论文、教授课程、承担项目等表的插入记录功能

- ##### 详细

  - 对教师表：
    - 检查：教师是否存在，若是则会报错，并提示前往Alt界面修改信息
    - 否则正常插入
  - 对课程表：
    - 检查：课程是否存在，若是则会报错，并提示前往Alt界面修改信息
    - 否则正常插入
  - 对发表论文表
    - 检查：一篇论文只能有一位通讯作者，若否则会报错
    - 检查：论文的作者排名不能有重复，若否则会报错
    - 检查：当前教师-论文记录是否已经存在，若是则会报错，并提示前往Alt界面修改信息
    - 论文的类型和级别只 能在约定的取值集合中选取，使用下拉框实现
    - 检查插入的记录的教师和论文是否已存在，若否则自动在教师和论文表插入
    - 都通过则正常插入
  - 对承担项目表
    - 检查：排名不能有重复
    - 检查：一个项目中所有教师的承担经费总额应小于等于项目的总经费
    - 检查：项目类型 只能在约定的取值集合中选取，使用下拉框实现
    - 检查：项目的开始年份是否小于结束年份，若否则会报错
    - 检查：当前教师-项目记录是否已经存在，若是则会报错，并提示前往Alt界面修改信息
    - 检查插入的记录的教师和项目是否已存在，若否则自动在教师和项目表插入
    - 都通过则正常插入
  - 对教授课程表
    - 检查：一门课程所有教师的主讲学时总额应小于等于课程的总学时
    - 检查：当前教师-课程记录是否已经存在，若是则会报错，并提示前往Alt界面修改信息
    - 检查插入的记录的教师和课程是否已存在，若否则自动在教师和课程表插入
    - 都通过则正常插入

  

  ##### 部分展示：

  ![image-20230621175324160](C:\Users\AimerYoung\AppData\Roaming\Typora\typora-user-images\image-20230621175324160.png)

![image-20230621175400224](C:\Users\AimerYoung\AppData\Roaming\Typora\typora-user-images\image-20230621175400224.png)



### <a name = "Delete-Module"></a>3.3 删除模块

- ##### 功能：提供对教师、课程、项目、论文、发表论文、教授课程、承担项目等表的搜索以及删除记录功能

- ##### 详细：

  - 对教师表
    - 检查：是否存在将要删除的记录
    - 删除一条教师记录会级联删除他绑定的发表论文、教授课程、承担项目记录
  - 对课程表：
    - 检查：是否存在将要删除的记录
    - 删除一条课程记录会级联删除它绑定的教程课程记录
    - 删除对应记录
  - 对项目表
    - 检查：是否存在将要删除的记录
    - 删除一条项目记录会级联删除它绑定的承担项目记录
    - 删除对应记录
  - 对论文表
    - 检查：是否存在将要删除的记录
    - 删除一条论文记录问级联删除它绑定的发表论文记录
    - 删除对应记录
  - 对教授课程表
    - 检查：是否存在将要删除的记录
    - 删除对应记录
  - 对承担项目表
    - 检查：是否存在将要删除的记录
    - 删除对应记录
  - 对发表论文表
    - 检查：是否存在将要删除的记录
    - 删除对应记录

  ##### 部分展示：

  ![image-20230621180045446](C:\Users\AimerYoung\AppData\Roaming\Typora\typora-user-images\image-20230621180045446.png)

![image-20230621180230193](C:\Users\AimerYoung\AppData\Roaming\Typora\typora-user-images\image-20230621180230193.png)

![image-20230621180242921](C:\Users\AimerYoung\AppData\Roaming\Typora\typora-user-images\image-20230621180242921.png)

### <a name = "Alt-Module"></a>3.4 修改模块

- ##### 功能：提供对教师、课程、项目、论文、发表论文、教授课程、承担项目等表的搜索以及修改记录功能

- ##### 详细：

  - 对教师表
    - 检查：是否存在将要修改的记录
    - 修改记录
  - 对项目表
    - 检查：是否存在将要修改的记录
    - 检查：修改总经费后，所有教师的承担经费总额是否小于等于项目的总经费，若否则报错
    - 检查：修改开始或结束年份后，开始年份是否小于结束年份，若否则报错
    - 修改记录
  - 对课程表
    - 检查：是否存在将要修改的记录
    - 检查：修改总学时后，所有教师的授课学时总和是否小于等于课程的总学时，若否则报错
    - 修改记录
  - 对论文表
    - 检查：是否存在将要修改的记录
    - 修改记录
  - 对发表论文表
    - 检查：是否存在将要修改的记录
    - 检查：修改后，一篇论文的通讯作者数量是否仍旧小于等于1，若否则报错
    - 检查：修改后，一篇论文的作者排名是否有重复，若是则报错
    - 修改记录
  - 对承担项目表
    - 检查：是否存在将要修改的记录
    - 检查：修改后，所有教师的承担经费总额是否小于等于项目的总经费，若否则报错
    - 修改记录
  - 对教授课程表
    - 检查：是否存在将要修改的记录
    - 检查：修改后，项目参与者的排名是否有重复，若是则报错
    - 检查：修改后，所有教师的授课学时总和是否小于等于课程的总学时，若否则报错
    - 修改记录

##### 部分展示：

![image-20230621200649087](C:\Users\AimerYoung\AppData\Roaming\Typora\typora-user-images\image-20230621200649087.png)

### <a name = "Search-Module"></a>3.5 查找模块

- ##### 功能：提供对教师、课程、项目、论文、发表论文、教授课程、承担项目等表的查找记录功能

- ##### 详细：

  - 对于各个表，可以使用其中的任意属性查找，但是推荐使用主键来精确查找

### <a name = "Count-Module"></a>3.6 统计模块

##### 功能：提供按教师工号和给定年份范围汇总查询该教师的教学科研情况的功能

##### 附加功能：实现按教师工号和给定年份范围生成教学科研工作量统计表并导出文档的功能，导出文档格式是 PDF

![image-20230621201708733](C:\Users\AimerYoung\AppData\Roaming\Typora\typora-user-images\image-20230621201708733.png)

# <a name = "Implementation-Testing"></a>4 实现与测试

### <a name ="Implementation-Result" ></a>4.1 实现结果

##### 见第三部分

### <a name = "Test-Result"></a>4.2 测试结果

##### 见第三部分

### <a name = "Issues-Solutions"></a>4.3 实现中的难点问题及解决

1. 界面设计。虽然结果还是很丑，但没有学习过html+css，还是费了很多劲。

2. 前端和后端交互。使用了python-flask框架，非常方便

3. 代码量非常大，但是复用量也非常大。没有解决，需要提高程序架构能力

   ![image-20230621202605461](C:\Users\AimerYoung\AppData\Roaming\Typora\typora-user-images\image-20230621202605461.png)

4. 导出pdf功能实现困难。先写好markdown的模板，使用markdown和pdfkit库转化为pdf

5. 数据库数据一致性的设计困难，例如约束“一门课程所有教师的主讲学时总额应等于课程的总学时”。讨论会认为，仅需小于等于既是满足要求的

   <div style="page-break-after:always;"></div>

# <a name = "Summary-Discussion"></a>5 总结与讨论

##### 		我写了一个工作量非常大的教师科研教学管理系统。这个系统旨在帮助教师更好地管理科研和教学任务，提高工作效率和质量。

##### 		在这个系统中，我采用了Flask作为后端框架，它提供了轻量级的Web开发环境和丰富的扩展库，使得系统的搭建和扩展变得相对容易。同时，我使用了Flask的模板引擎来实现前端页面的渲染和展示，使得用户界面更加友好和美观。

##### 系统的功能包括但不限于以下几个方面：

1. 教师信息管理：包括教师基本信息、科研项目、教学任务等的录入、查看和修改。通过这个功能，教师可以方便地管理和更新自己的个人信息和工作任务。
2. 科研管理：包括科研项目的立项、进度跟踪、成果上传等。这个功能可以帮助教师有效地管理科研项目，记录项目进展和成果，方便与其他教师和研究人员的合作与交流。
3. 教学管理：包括教学任务的分配、课程计划的制定、学生成绩的录入和统计等。这个功能可以帮助教师更好地组织教学活动，管理学生成绩和评估教学效果。

​	4.论文管理：帮助教师管理他们的论文，包括论文的投稿、审稿、修改和发表等流程。

##### 总结收获有：

1. 开发前需要制定完善的项目架构，开发途中一旦有更改，代价将是惨重的
2. 自主从网上学习flask框架
3. 对mysql数据库有了更深的理解
4. 变量名、函数名、文件名使用更科学的命名方式，可以让工作变得简单
5. 每实现一个小功能即debug
6. 如果不会架构，多复用已经测试过的代码，可以极大的减少工作量
