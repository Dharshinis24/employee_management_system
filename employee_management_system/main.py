from services.employee_service import EmployeeService
from services.attendance_service import AttendanceService
from services.leave_service import LeaveService

from models.employee import Employee
from models.attendance import Attendance
from models.leave_request import LeaveRequest


employee_service = EmployeeService()
attendance_service = AttendanceService()
leave_service = LeaveService()


while True:
    print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
    print("1. Add Employee")
    print("2. View Employees")

    print("\n----- Attendance -----")
    print("3. Mark Attendance")
    print("4. Check-In")
    print("5. Check-Out")
    print("6. View Attendance")

    print("\n----- Leave -----")
    print("7. Apply Leave")
    print("8. View All Leave Requests")
    print("9. Approve Leave")
    print("10. Reject Leave")

    print("0. Exit")

    choice = input("\nEnter your choice: ")

    try:
        # ---------------- EMPLOYEE ----------------
        if choice == "1":
            name = input("Enter Employee Name: ")
            dept = input("Enter Department: ")
            joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
            salary = float(input("Enter Salary: "))

            emp = Employee(name, dept, joining_date, salary)
            employee_service.add_employee(emp)

        elif choice == "2":
            employee_service.view_employee()

        # ---------------- ATTENDANCE ----------------
        elif choice == "3":
            emp_id = int(input("Enter Employee ID: "))
            attendance_date = input("Enter Date (YYYY-MM-DD): ")
            status = input("Enter Status (Present/Absent): ")
            att = Attendance(emp_id, attendance_date, status)
            attendance_service.mark_attendance(att)

        elif choice == "4":
            emp_id = int(input("Enter Employee ID: "))
            date = input("Enter Date (YYYY-MM-DD): ")
            check_in = input("Enter Check-In Time (HH:MM): ")

            attendance_service.check_in(emp_id, date, check_in)

        elif choice == "5":
            emp_id = int(input("Enter Employee ID: "))
            date = input("Enter Date (YYYY-MM-DD): ")
            check_out = input("Enter Check-Out Time (HH:MM): ")

            attendance_service.check_out(emp_id, date, check_out)

        elif choice == "6":
            attendance_service.view_attendance()

        # ---------------- LEAVE ----------------
        elif choice == "7":
            emp_id = int(input("Enter Employee ID: "))
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            reason = input("Enter Reason: ")

            leave = LeaveRequest(emp_id, start_date, end_date, reason)
            leave_service.apply_leave(leave)

        elif choice == "8":
            leave_service.view_all_leave_request()

        elif choice == "9":
            leave_id = int(input("Enter Leave ID to Approve: "))
            leave_service.approve_leave(leave_id)

        elif choice == "10":
            leave_id = int(input("Enter Leave ID to Reject: "))
            leave_service.reject_leave(leave_id)

        elif choice == "0":
            print("Thank you! Exiting system...")
            break

        else:
            print("Invalid choice! Try again.")

    except Exception as e:
        print("Error:", e)
