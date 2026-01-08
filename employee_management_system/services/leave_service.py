from db.db_connection import DatabaseConnection

"""
Apply leave
view all leave requests
view leave by employee
cancel leave
leave approval
leave rejection
"""

class LeaveService:

    def __init__(self):
        self.dbco = DatabaseConnection()

    def apply_leave(self,leave_request):

        if not leave_request.emp_id or not leave_request.start_date or not leave_request.end_date or not leave_request.reason:
            raise ValueError("Invalid data")
        
        if leave_request.start_date > leave_request.end_date:
            raise ValueError("End date cannot be before start date")

        if(leave_request.end_date >= leave_request.start_date):
            self.dbco.cursor.execute(""" 
                Insert into leave_request 
                (emp_id,start_date,end_date,reason)
                values (?,?,?,?)
                """,(leave_request.emp_id,leave_request.start_date,leave_request.end_date,leave_request.reason))
            self.dbco.conn.commit()
            print("Leave request added!")

       
    def view_all_leave_request(self):

        self.dbco.cursor.execute(""" 
        Select * from leave_request
        """)
        rows = self.dbco.cursor.fetchall()

        if(rows):
            for i in rows:
                print(i)
        else:
            print("No record found")

    def view_leave_by_employee(self,emp_id):

        self.dbco.cursor.execute(""" 
        select * from leave_request
        where emp_id = ?
        """,(emp_id,))

        rows = self.dbco.cursor.fetchall()

        if(rows):
            for i in rows:
                print(i)
        else:
            print("No record found")

    def cancel_leave(self,leave_id):

        if not leave_id:
            raise ValueError("Invalid leave id")
        
        status = "Canceled"

        self.dbco.cursor.execute("""
        select * from leave_request 
        where leave_id = ? and status = 'Pending'                        
        """,(leave_id))
        
        rows = self.dbco.cursor.fetchall()
        if(rows):
            self.dbco.cursor.execute(""" 
            update leave_request
            set status = ?
            where leave_id = ? and status = 'Pending'
            """,(status,leave_id))
            self.dbco.conn.commit()
            print("leave cancelled")

        else:
            print("Leave id not found")
       

    def approve_leave(self,leave_id):

        if not leave_id: 
            raise ValueError("Invalid data")
        
        upd_status = "Approved"

        self.dbco.cursor.execute("""
        select * from leave_request 
        where leave_id = ? and status = 'Pending'                        
        """,(leave_id))
        
        rows = self.dbco.cursor.fetchall()
        if(rows):
            self.dbco.cursor.execute(""" 
            update leave_request 
            set status = ?
            where leave_id = ? and status = 'Pending'
            """,(upd_status,leave_id,))
            self.dbco.conn.commit()
            print("Leave approved")
        
        else:
            print("Leave id not found")
        

    def reject_leave(self,leave_id):

        if not leave_id:
            raise ValueError("Invalid data")
        
        status = "Rejected"

        self.dbco.cursor.execute("""
        select * from leave_request 
        where leave_id = ? and status = 'Pending'                        
        """,(leave_id))
        
        rows = self.dbco.cursor.fetchall()
        if(rows):
            self.dbco.cursor.execute(""" 
            update leave_request 
            set status = ?
            where leave_id = ? and status = 'Pending'
            """,(status,leave_id,))
            self.dbco.conn.commit()
            print("Leave Rejected")
    
        else:
            print("Leave id not found")
       
       