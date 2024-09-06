SELECT 'employees' AS table_name, 
       field_name, 
       value
FROM   (SELECT employee_id, 
               first_name, 
               last_name, 
               salary 
        FROM employees
        WHERE employee_id = 101) -- Use the specific record condition here
UNPIVOT (value FOR field_name IN (employee_id AS 'Employee ID', 
                                  first_name AS 'First Name', 
                                  last_name AS 'Last Name', 
                                  salary AS 'Salary'));