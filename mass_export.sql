DECLARE
    TYPE query_rec IS RECORD (
        query_name VARCHAR2(100),  -- This will now be the table name
        query_text CLOB
    );
    TYPE query_list IS TABLE OF query_rec;

    v_queries query_list := query_list(
        query_rec('table1', 'SELECT column1, column2, column3 FROM table1'),
        query_rec('table2', 'SELECT column1, column2, column3, column4 FROM table2'),
        -- Add all your 43 queries here in the same format
        query_rec('table43', 'SELECT column1, column2, column3 FROM table43')
    );

    -- Other variables and code remain unchanged
BEGIN
    FOR i IN 1..v_queries.COUNT LOOP
        -- Open a new file with the table name as the file name
        v_file := UTL_FILE.FOPEN('DIRECTORY_NAME', v_queries(i).query_name || '.csv', 'W', 32767);

        BEGIN
            -- Parsing and executing the query, writing data to the file, etc.
            -- Code remains the same as the previous example
        END;

        -- Close the file
        UTL_FILE.FCLOSE(v_file);
    END LOOP;

EXCEPTION
    -- Exception handling code remains the same as the previous example
END;
/