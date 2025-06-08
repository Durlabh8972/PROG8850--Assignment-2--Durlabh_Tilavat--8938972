import mysql.connector

def execute_sql(file_path):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='companydb'
        )
        cursor = conn.cursor()
        with open(file_path, 'r') as file:
            sql_commands = file.read().split(';')
            for command in sql_commands:
                if command.strip():
                    try:
                        cursor.execute(command)
                    except mysql.connector.Error as cmd_err:
                        print(f"SQL Command Error: {cmd_err}")
        conn.commit()
        print("SQL executed successfully.")
    except mysql.connector.Error as err:
        print(f"Connection Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

execute_sql('schema_update.sql')
