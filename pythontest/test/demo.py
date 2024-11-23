import mysql.connector

def connect_to_database():
    try:
        # Replace the connection parameters with your database credentials
        connection = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port="3306",
            database="mydb"
        )

        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()

        # Perform database operations here
        # Example: Execute a query
        cursor.execute("SELECT * FROM user")
        result = cursor.fetchall()
        for row in result:
            print(row)

        

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print("Error connecting to the database:", error)

if __name__ == "__main__":
    connect_to_database()
