from val_empolyeid import val_empolyeeid 
from experienceverify import validate_experience 
from data import  display_employee_info


emp_id = val_empolyeeid (input("Enter Employee ID: "))
name = input("Enter Employee Name: ")

experience = validate_experience (int(input("Enter Years of Experience: ")))
tier =  (int(input("Enter which tier employee you are: ")))

if tier == 1 :
            basic_salary = 90000
        
elif tier == 2 :
            basic_salary = 70000
        
else :
            basic_salary = 35000 
        
       


       




emp_tuple = (emp_id, name,basic_salary , experience)
display_employee_info(emp_tuple)

