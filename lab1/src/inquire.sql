use lab1;
-- # (1) 查询读者 Rose 借过的读书（包括已还和未还）的图书号、书名和借期；
-- SELECT b.ID, b.name, br.borrow_Date
-- FROM Book b, Borrow br, Reader r 
-- WHERE b.ID = br.book_ID AND br.reader_ID = r.ID AND r.name = 'Rose';


-- # (2) 查询从没有借过图书也从没有预约过图书的读者号和读者姓名
-- SELECT r.ID, r.name
-- FROM Reader r
-- WHERE r.ID NOT IN (
--   SELECT DISTINCT reader_ID
--   FROM Borrow
--   UNION
--   SELECT DISTINCT reader_ID
--   FROM Reserve
-- );


-- # (3) 查询被借阅次数最多的作者（注意一个作者可能写了多本书）
-- SELECT b.author, SUM(b.borrow_Times) AS total_borrow_times
-- FROM Book b
-- GROUP BY b.author
-- ORDER BY total_borrow_times DESC
-- LIMIT 1;


-- # (4) 查询目前借阅未还的书名中包含“MySQL”的的图书号和书名
SELECT b.ID, b.name
FROM Book b, Borrow br
WHERE b.ID = br.book_ID AND b.name LIKE '%MySQL%'AND br.return_Date IS NULL;


-- # (5)  查询借阅图书数目超过 10 本的读者姓名
-- SELECT reader.name 
-- from reader 
-- where reader.ID in(
-- select reader.ID
-- FROM reader, borrow 
-- WHERE reader.ID = borrow.reader_ID
-- GROUP BY reader.ID
-- HAVING count(*) > 10);


-- # (6)  查询没有借阅过任何一本 John 所著的图书的读者号和姓名
SELECT r.ID, r.name
FROM Reader r
WHERE NOT EXISTS (
    SELECT *
    FROM Book b
    WHERE b.author = 'John'
    AND b.ID IN (
        SELECT book_ID
        FROM Borrow br
        WHERE br.reader_ID = r.ID
    )
);


-- # (7) 查询 2022 年借阅图书数目排名前 10 名的读者号、姓名以及借阅图书数
SELECT r.ID, r.name, COUNT(*) AS borrow_count
FROM Reader r, Borrow b
WHERE r.ID = b.reader_ID
AND YEAR(b.borrow_Date) = 2022
GROUP BY r.ID
ORDER BY borrow_count desc
LIMIT 10;


-- # (8) 创建一个读者借书信息的视图,该视图包含读者号、姓名、所借图书号、图书名和借期
drop view if exists ReaderBorrowInfo;
CREATE VIEW ReaderBorrowInfo AS
SELECT r.ID AS reader_ID, r.name AS reader_name, b.book_ID, bk.name AS book_name, b.borrow_Date
FROM Reader r, Borrow b, Book bk
WHERE r.ID = b.reader_ID AND b.book_ID = bk.ID;

-- # 并使用该视图查询最近一年所有读者的读者号以及所借阅的不同图书数
SELECT reader_ID, COUNT(DISTINCT book_ID) AS book_count
FROM ReaderBorrowInfo
WHERE borrow_Date between date_sub(curdate(),interval 1 year) and curdate()	
GROUP BY reader_ID;

