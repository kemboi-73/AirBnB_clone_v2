-- This script sets a weak password for the created user
-- One way is to use:
-- 	SHOW VARIABLES LIKE 'validate%';
-- This will list any validation policies set, which can be edited by:
-- 	SET GLOBAL validate_password.check_user_name = 'OFF';
-- Make sure to replace 'validate_password.check_user_name' with the appropriate policy

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
