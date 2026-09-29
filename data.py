from  final_salary import calculate_final_salary




def display_employee_info(employee):
    emp_id, name, basic_salary, experience = employee
    final_salary, bonus_rate = calculate_final_salary(employee)
    
    print("\n Employee detail")
    print("ID:", emp_id)
    print(f"Name: {name}")
    print(f"Basic Salary: ${basic_salary}")
    print(f"Experience: {experience} years")
    print(f"Bonus Tier: {bonus_rate}%")
    print(f"Final Salary: ${final_salary}")