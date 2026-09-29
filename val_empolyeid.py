def val_empolyeeid (emp_id):
    while len(emp_id)!=10:
        print("Invalid Empolyee ID, Employee ID exactly 10 chartacter")
        emp_id = input("Enter Employee ID")
    return emp_id


