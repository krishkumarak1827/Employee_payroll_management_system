def calculate_final_salary(employee):
    emp_id, name, basic_salary, experience = employee
    
    if experience >= 10:
        bonus_pct = 0.20
    elif experience >= 5:
        bonus_pct = 0.10
    else:
        bonus_pct = 0.05
        
    bonus_amount = basic_salary * bonus_pct
    final_salary = basic_salary + bonus_amount
    return final_salary, bonus_pct * 100
