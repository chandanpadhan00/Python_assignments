# List of original queries
queries = [
    "select col1, col2 from table1;",
    "select col3, col4 from table2;",
    # Add all your 43 lines here
    # ...
]

# Process each query
formatted_queries = []
for query in queries:
    # Extract the table name (assuming it always comes after 'from')
    table_name = query.split('from')[1].strip().replace(';', '')

    # Form the new line
    formatted_query = f"'{table_name}', '{query.strip()}'"
    formatted_queries.append(formatted_query)

# Print all formatted queries
for formatted_query in formatted_queries:
    print(formatted_query)