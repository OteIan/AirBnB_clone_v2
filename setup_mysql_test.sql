-- Create database if it doesn't exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a user they do not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant all priviledges to hbnb_test on database hbnb_test_to
GRANT SELECT ON performance_schema.* TO  'hbnb_test'@'localhost';
