-- task_5.sql
-- Script to insert a single row into the 'customer' table
-- in the alx_book_store database.
-- The database name will be passed as an argument to the mysql command.
-- Example usage: mysql -u user -p alx_book_store < task_5.sql

INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
