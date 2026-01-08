from db.db_connection import DatabaseConnection

"""Add employee 

View employees

Update employee

Delete employee

Search by department

Salary increment"""


class EmployeeService:
    def __init__(self):
        self.dbco = DatabaseConnection()

    def add_employee(self,employee):
        
        if not employee.emp_name or not employee.dept:
            raise ValueError("Invalid employee data")
        
        if (employee.salary <= 0):
            raise ValueError("Salary must be greater than zero")
        
        if employee.joining_date is None:
            raise ValueError("Joining date is required")
    
        self.dbco.cursor.execute(""" Insert into employee (emp_name,dept,joining_date,salary) values (?,?,?,?)""",(employee.emp_name,employee.dept,employee.joining_date,employee.salary))
        self.dbco.conn.commit()
        print("Employee added successfully!")


    def view_employee(self):

        self.dbco.cursor.execute(""" 
        Select * from employee 
       """)
        rows = self.dbco.cursor.fetchall()

        if(rows):
            for i in rows:
                print(i)
            
        else:
            print("No employees found")

    def salary_increment(self,new_salary,emp_id):

        if new_salary <= 0:
            raise ValueError("Invalid salary")

        self.dbco.cursor.execute(""" 
        Update employee set salary = ? where emp_id = ?
        """,(new_salary,emp_id))
        self.dbco.conn.commit()
        print("Salary incremented successfully.")

    def update_employee(self,new_dept,emp_id):
        if not new_dept:
             raise ValueError("Department cannot be empty")

        self.dbco.cursor.execute("""
        update employee 
        set dept = ?
        where emp_id = ?
        """,(new_dept,emp_id))
        self.dbco.conn.commit()
        print("Updated successfully!")

    def delete_employee(self,emp_id):

        self.dbco.cursor.execute(""" 
        Delete from employee
        where emp_id = ?
        """,(emp_id,))
        self.dbco.conn.commit()
        print("Deleted successfully!")

    def search_by_dept(self,dept):

        self.dbco.cursor.execute(""" 
        Select * from employee
        where dept = ?
        """,(dept,))
        rows = self.dbco.cursor.fetchall()
        
        if(rows):
            for i in rows:
                print(i)

        else:
            print("No employees found in this department")


