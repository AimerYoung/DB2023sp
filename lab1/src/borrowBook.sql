drop procedure if exists borrowBook;
DELIMITER //
CREATE PROCEDURE borrowBook(IN bookID CHAR(8), IN readerID CHAR(8), IN borrowDate DATE, OUT state CHAR(100)) 
BEGIN
    DECLARE borrowCount INT;
    DECLARE reserveCount INT;
    DECLARE i INT DEFAULT 1;
    DECLARE text varchar(100);
    DECLARE bookstatus INT;
    Declare s varchar(10) default '';
    declare continue HANDLER FOR SQLEXCEPTION SET s = '4';
    START TRANSACTION;
    -- 执行DML语句
    -- 检查同一天不允许同一个读者重复借阅同一本读书
    SELECT COUNT(*) INTO borrowCount FROM borrow WHERE reader_ID = readerID AND book_ID = bookID AND borrow_Date = borrowDate;
    IF borrowCount > 0 THEN
        SET s = IFNULL(concat(s, 'a'),'');
    END IF;

    -- 如果该图书存在预约记录，而当前借阅者没有预约，则不允许借阅
	SELECT COUNT(*) INTO reserveCount FROM reserve WHERE book_ID = bookID AND reader_ID = readerID;
     IF reserveCount = 0 THEN
 		SELECT COUNT(*) INTO reserveCount FROM reserve WHERE book_ID = bookID AND reader_ID != readerID;
			IF reserveCount > 0 THEN
			set s = IFNULL(concat(s , 'b'),'');
		END IF;
    END IF;

    -- 一个读者最多只能借阅 3 本图书
    SELECT COUNT(*) INTO borrowCount FROM borrow WHERE reader_ID = readerID AND return_Date IS NULL;
    IF borrowCount >= 3 THEN
       set s = IFNULL(concat(s, 'c'),'');
    END IF;
    
    -- 如果图书的status是2，即已经被借阅，则不能借阅
	SELECT status into bookstatus from book where ID = bookID;
    IF bookstatus = 1 THEN 
		set s = IFNULL(concat(s, 'd'),'');
	END IF;

    -- 如果借阅者已经预约了该图书，则删除预约记录
    delete from reserve WHERE book_ID = bookID AND reader_ID = readerID;

    -- 借阅成功后修改图书表中的 status
    UPDATE Book SET status = 1, borrow_Times = borrow_Times + 1 WHERE ID = bookID;
    
    -- 插入借阅记录updateReaderIDupdateReaderID
    INSERT INTO Borrow (book_ID, reader_ID, borrow_Date) VALUES (bookID, readerID, borrowDate);
    
    IF s = '' THEN
		set state = 'Success!';
        COMMIT;
	ELSE
		SET text = '';
		while MID(s,i,1) != '' DO
			CASE MID(s,i,1)
				WHEN 'a' THEN SET text = concat(text,'同一天不允许同一个读者重复借阅同一本读书！\n');
                WHEN 'b' THEN SET text = concat(text,'如果该图书存在预约记录，而当前借阅者没有预约，则不允许借阅！\n');
                WHEN 'c' THEN SET text = concat(text,'一个读者最多只能借阅 3 本图书，意味着如果读者已经借阅了 3 本图书并
且未归还则不允许再借书！\n');
				WHEN 'd' THEN SET text = concat(text,'图书正在被借阅中！');
                ELSE SET text = 'SQLEXEPTION';
			END CASE;
			SET i = i + 1;
		END WHILE;
        SET state = text;
        ROLLBACK;
	END IF;
END //
DELIMITER ;


