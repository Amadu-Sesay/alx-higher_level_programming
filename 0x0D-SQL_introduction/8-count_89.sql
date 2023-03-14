-- displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
-- SELECT COUNT(column_name) FROM table_name -> It is a function that takes the name of a column as argument and counts the number of rows when the column is not NULL
SELECT COUNT(id) FROM first_table WHERE id = 89;
