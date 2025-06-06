import mysql.connector

def execute_sql(file_path):
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
                    cursor.execute(command)
        conn.commit()
        print("SQL executed successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

execute_sql('schema_update.sql')
