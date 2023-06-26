drop procedure if exists returnBook;
DElIMITER //
CREATE PROCEDURE returnBook(IN bookID CHAR(8), IN readerID CHAR(8), IN returnDate DATE, OUT state CHAR(100))
BEGIN
	DECLARE returnCount INT;
    DECLARE borrowCount INT;
    DECLARE bookstatus INT;
    DECLARE i INT DEFAULT 1;
    DECLARE text varchar(100);
    Declare s varchar(10) default '';
    declare continue HANDLER FOR SQLEXCEPTION SET s = '4';
    
     START TRANSACTION;
    -- 执行DML语句
    
    -- 同一天不允许同一个读者重复返还同一本读书
    SELECT COUNT(*) INTO returnCount FROM borrow WHERE reader_ID = readerID AND book_ID = bookID AND return_Date = returnDate;
    IF returnCount > 0 THEN
        SET s = IFNULL(concat(s, 'a'),'');
    END IF;
    
    -- 如果该图书存在借阅记录，而且并没有被返还，而且借阅者不是当前读者，则不允许返还
    SELECT COUNT(*) INTO borrowCount FROM borrow WHERE book_ID = bookID AND reader_ID != readerID AND return_Date = NULL;
    IF borrowCount > 0 THEN
        set s = IFNULL(concat(s , 'b'),'');
    END IF;

	-- 如果图书的status不是1，即图书不处于被借阅的状态，则不能被返还
    select status into bookstatus from book where ID = bookID;
    IF bookstatus != 1 THEN
		SET s = IFNULL(concat(s,'c'),'');
	END IF;

	-- 如果借阅者已经借阅了该图书，则允许返还，但要求返还完成后设置借阅表中的 return_Date 为返还日期
	update borrow SET return_Date = returnDate where reader_id = readerID AND book_id = bookID;
    
    -- 返还成功后修改 status
    update book SET status = 0 where ID = bookID;
    
    IF s = '' THEN
		set state = 'Success!';
        COMMIT;
	ELSE
		SET text = '';
		while MID(s,i,1) != '' DO
			case MID(s,i,1)
				WHEN 'a' THEN SET text = concat(text,'同一天不允许同一个读者重复返还同一本读书！\n');
                WHEN 'b' THEN SET text = concat(text,'如果该图书存在借阅记录，而且并没有被返还，而且借阅者不是当前读者，则不允许返还！\n');
                WHEN 'c' THEN SET text = concat(text,'图书未被借阅中！');
                ELSE SET text = 'SQLEXEPTION';
			END CASE;
			SET i = i + 1;
		END WHILE;
        SET state = text;
        ROLLBACK;
	END IF;
END //
DELIMITER ;
