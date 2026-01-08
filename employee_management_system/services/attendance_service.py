from db.db_connection import DatabaseConnection

"""Mark Attendance

Check-in

Check-out

View Attendance

View Attendance by Date

Update Attendance Status

Delete Attendance Record"""

class AttendanceService:

    def __init__(self):
        self.dbco = DatabaseConnection()

    def mark_attendance(self,attendance):
    
        if not attendance.emp_id or not attendance.attendance_date or not attendance.status:
            raise ValueError("Invalid data")
        self.dbco.cursor.execute(""" 
        Insert into attendance (emp_id,attendance_date,status) values(?,?,?)
        """,(attendance.emp_id,attendance.attendance_date,attendance.status))
        self.dbco.conn.commit()
        print("Attendance marked")

    def check_in(self,emp_id,attendance_date,check_intime):

        if not emp_id or not attendance_date or not check_intime:
            raise ValueError("Invalid details")
        
        self.dbco.cursor.execute(""" 
        select * from attendance
        where emp_id = ? and attendance_date = ?
        and check_in is Null
        """,(emp_id,attendance_date))

        rows = self.dbco.cursor.fetchall()

        if(rows):
            self.dbco.cursor.execute("""
            update attendance
            set check_in = ? 
            where emp_id = ? and attendance_date = ?                         
            """,(check_intime,emp_id,attendance_date))
            
            self.dbco.conn.commit()
            print("Check_in updated")

        else:
            print("The entered employee has no attendance")
        
       

    def check_out(self,emp_id,attendance_date,check_outtime):

        if not emp_id or not attendance_date or not check_outtime:
            raise ValueError("Invalid details")
         
        
        self.dbco.cursor.execute(""" 
        select * from attendance
        where emp_id = ? 
        and attendance_date = ? and check_in is not Null
        """,(emp_id,attendance_date))

        rows = self.dbco.cursor.fetchall()

        if(rows):
            self.dbco.cursor.execute("""
            update attendance
            set check_out = ? 
            where emp_id = ?  and attendance_date = ?                       
            """,(check_outtime,emp_id,attendance_date))
            self.dbco.conn.commit()
            print("Check_out updated")

        else:
            print("The entered employee has no check-in")
        
       

    def view_attendance(self):

        self.dbco.cursor.execute(""" 
        select * from attendance
        """)
        rows = self.dbco.cursor.fetchall()
        if(rows):
            for i in rows:
                print(i)

    def view_attendance_by_date(self,date):

        self.dbco.cursor.execute(""" 
        select * from attendance
        where attendance_date = ?
        """,(date,))
        rows = self.dbco.cursor.fetchall()
        if(rows):
            for i in rows:
                print(i)
        
    def update_status(self,emp_id,attendance_date,status):
        
        if not emp_id or not attendance_date:
            raise ValueError("Invalid details")
        if status not in ("Present", "Absent"):
            raise ValueError("Invalid status")

        self.dbco.cursor.execute("""
        select * from attendance
        where emp_id = ? and attendance_date = ?   
        """,(emp_id,attendance_date))
        rows = self.dbco.cursor.fetchall()
        if(rows):
            self.dbco.cursor.execute(""" 
            update attendance
            set status = ?
            where emp_id = ? and attendance_date = ?
            """,(status,emp_id,attendance_date))
            self.dbco.conn.commit()
            print("Status updated")

    def delete_attendance(self,emp_id,attendance_date):

        self.dbco.cursor.execute(""" 
        delete from attendance
        where emp_id = ? and attendance_date = ?
        """,(emp_id,attendance_date))
        self.dbco.conn.commit()
        print("Record deleted!")



