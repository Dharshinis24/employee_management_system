class LeaveRequest:

    def __init__(self,emp_id, start_date, end_date, reason):
        self.emp_id = emp_id
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason