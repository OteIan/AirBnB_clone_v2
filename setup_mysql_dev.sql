-- Create database if it doesn't exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a user they do not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant all priviledges to hbnb_dev on database hbnb_dev_to
GRANT SELECT ON performance_schema.* TO  'hbnb_dev'@'localhost';
