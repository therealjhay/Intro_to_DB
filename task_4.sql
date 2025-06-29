-- task_4.sql
-- Script to print the full description of the 'Books' table
-- from the database 'alx_book_store' in your MySQL server.
-- The database name will be passed as an argument of the mysql command.
-- Example usage: mysql -u user -p alx_book_store < task_4.sql

SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books';
