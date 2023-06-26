use lab1;

drop procedure if exists updateReaderID; 
DELIMITER //
CREATE PROCEDURE updateReaderID(
  IN old_id CHAR(8),
  IN new_id CHAR(8)
)
BEGIN
DECLARE tempname varchar(10);
DECLARE tempage int;
DECLARE tempaddress varchar(20);
-- SET SQL_SAFE_UPDATES=0;
start transaction;
	select name,age,address from READER where ID = old_id into tempname,tempage,tempaddress;
	INSERT INTO Reader(ID,name,age,address) Values(new_id,tempname,tempage,tempaddress); 
    
	UPDATE borrow SET reader_ID = new_id WHERE reader_ID = old_id;
	UPDATE reserve SET reader_ID = new_id WHERE reader_ID = old_id;
    
    Delete From Reader where ID = old_id;
	COMMIT;
    -- SET SQL_SAFE_UPDATES=1;
END //
DELIMITER ;

