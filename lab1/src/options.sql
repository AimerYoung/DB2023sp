-- call updateReaderID('r23','r233');
-- -- Delete from reader where ID = 'r5';

--  call returnBook('b10','r20','2023-04-18',@state);
--  select @state;

-- call returnBook('r3','b7','2023-05-19',@state);
-- select @state;

-- insert into reserve values('b11','r3','2022-02-22',null)

-- delete from reserve;
-- delete from borrow;
-- delete from reader;
-- delete from book

delete from reserve where book_ID = 'b11' and reader_ID = 'r3' 