use lab1;
drop trigger if exists book_reserve_trigger;
drop trigger if exists book_unreserve_trigger;
drop trigger if exists book_borrow_trigger;
DELIMITER //
CREATE TRIGGER book_reserve_trigger
AFTER INSERT ON reserve
FOR EACH ROW
BEGIN
    -- 预约时将图书状态改为 2，增加预约次数
    UPDATE Book SET status = 2, reserve_Times = reserve_Times + 1 WHERE ID = NEW.book_ID;
END;
//
CREATE TRIGGER book_unreserve_trigger
AFTER DELETE ON reserve
FOR EACH ROW
BEGIN
    -- 取消预约时减少预约次数
    DECLARE Times INT;
    UPDATE book SET reserve_Times = reserve_Times - 1 WHERE ID = OLD.book_ID;
    -- 当预约次数为0时，书的status转为0
    select reserve_Times into Times FROM book where ID = OLD.book_ID;
    IF Times = 0 THEN 
		update book SET status = 0;
	END IF;
END;
//
CREATE TRIGGER book_borrow_trigger
AFTER INSERT ON Borrow
FOR EACH ROW
BEGIN
    -- 借出时减少预约次数
    UPDATE book SET reserve_Times = 0, status = 1 WHERE ID = NEW.book_ID;
END;
//

