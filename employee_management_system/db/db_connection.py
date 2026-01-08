import pyodbc

class DatabaseConnection:

    DRIVER_NAME="ODBC Driver 18 for SQL Server"
    SERVER_NAME=r"DESKTOP-K48JCJ8\SQLEXPRESS"
    DATABASE_NAME="employee_management_system"
    
    def __init__(self):
        
        
        connection_string = (
        f"DRIVER={{{self.DRIVER_NAME}}};"
        f"SERVER={self.SERVER_NAME};"
        f"DATABASE={self.DATABASE_NAME};"
        "Trusted_Connection=yes;"
        "Encrypt=no;"    )
        
        try:
            
            self.conn = pyodbc.connect(connection_string)
            self.cursor = self.conn.cursor()
            
        except pyodbc.Error as e:
            print("Error: ",e)
        
        else:
            print("Database Connected")

if __name__ == "__main__":
    DbConn = DatabaseConnection()