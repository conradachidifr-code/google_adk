from sqlalchemy import create_engine, text

db = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/company?ssl_disabled=true")

def run_sql(query: str) -> str:
    """
    Executes a SQL query against the MySQL database and returns the results as a formatted string.
    
    Args:
        query: The SQL query to execute
    
    Returns:
        A formatted string with the query results or error message
    """
    try:
        with db.connect() as conn:
            result = conn.execute(text(query)).mappings().fetchall()
            rows = [dict(row) for row in result]
        
        if not rows:
            return "Query executed successfully but returned no results."
        
        # Format results as readable string
        output = ""
        for row in rows:
            output += str(row) + "\n"
        return output.strip()

    except Exception as e:
        return f"Error executing query: {str(e)}"
