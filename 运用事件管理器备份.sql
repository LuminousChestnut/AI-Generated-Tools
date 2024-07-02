-- 使用事件计划器进行备份
DELIMITER //
CREATE EVENT backup_event
ON SCHEDULE EVERY 1 DAY
DO
  BEGIN
    SET @command = CONCAT('mysqldump -u username -ppassword database_name > /path/to/backup/backup_', DATE_FORMAT(NOW(), '%Y%m%d'), '.sql');
    SET @result = sys_exec(@command);
  END //
DELIMITER ;
