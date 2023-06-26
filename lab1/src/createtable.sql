use lab1;

drop table if exists book;
create table book(
    ID char(8),
    name varchar(10) not null,
    author varchar(10),
    price float,
    status int default 0 comment '为 0 表示可借，1 表示书被借出, 2 表示已被预约, 默认值为 0',
    borrow_Times int default 0,
    reserve_Times int default 0,
    constraint PK_ID primary key (ID)
);

drop table if exists reader;
create table reader (
	ID char(8), 
    name varchar(10), 
    age int, 
    address varchar(20),
    constraint PK_ID primary key (ID)
);

drop table if exists borrow;
create table borrow (
	book_ID char(8), 
    reader_ID char(8), 
    borrow_Date date,
	return_Date date default NULL comment 'NULL 表示该书未还',
    constraint PK_brb primary key (book_ID,reader_ID,borrow_Date),
    constraint FK_bookID foreign key(book_ID) references book(ID),
    constraint FK_readerID foreign key (reader_ID) references Reader(ID)
);

drop table if exists reserve;
create table reserve(
	book_ID char(8), 
    reader_ID char(8), 
    reserve_Date date default (now()), 
	take_Date date,
    constraint PK_brr primary key (book_ID,reader_ID,reserve_Date),
    constraint later check (take_Date > reserve_Date)
)
