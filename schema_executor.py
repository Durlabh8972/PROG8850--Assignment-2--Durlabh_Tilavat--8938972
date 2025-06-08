import sys
import mysql.connector

def main():
    if len(sys.argv) != 6:
        print("Usage: python execute_sql_script.py <sql_file> <host> <user> <password> <database>")
        sys.exit(1)

    sql_file, host, user, password, database = sys.argv[1:]

    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor()

    with open(sql_file, 'r') as f:
        sql = f.read().split(';')
        for command in sql:
            if command.strip():
                cursor.execute(command)

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ SQL script executed successfully.")

if __name__ == "__main__":
    main()
