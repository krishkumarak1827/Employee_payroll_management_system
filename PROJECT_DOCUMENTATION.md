# Project Documentation – Employee Payroll Management System

## 1. Overview
A modular Python command-line application that collects employee information, validates key inputs, assigns a tier-based basic salary, applies an experience-based bonus, and displays the resulting salary details.

## 2. Modules
- `input.py`: coordinates user input and calls the validation/calculation/output modules.
- `val_empolyeid.py`: validates that the employee ID contains exactly 10 characters.
- `experienceverify.py`: validates experience in the range 0–35 years.
- `final_salary.py`: applies the bonus rule and calculates final salary.
- `data.py`: formats and displays employee information.
- `main.py`: contains an integrated version of the logic in one file.

## 3. Bonus Rules
- 10 or more years → 20% bonus
- 5–9 years → 10% bonus
- below 5 years → 5% bonus

## 4. Tier Rules in the modular input flow
- Tier 1 → 90,000 basic salary
- Tier 2 → 70,000 basic salary
- Other values → 35,000 basic salary

## 5. Processing Sequence
Input → Validation → Tier salary assignment → Bonus calculation → Output.

## 6. Current Limitations
No persistent database, GUI/web interface, tax/PF deductions, payslip generation, authentication, or employee record storage is implemented in the supplied version.

## 7. Future Enhancements
Add persistent storage, tax and deduction rules, payslip generation, employee search/update/delete, GUI/web interface, stronger ID validation, and automated test cases.
