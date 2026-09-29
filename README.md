Employee Payroll Management System

This is a command-line Python tool that gathers employee details checks them and then calculates the final salary by adding a bonus based on experience. It works automatically and reliably.

Problem It Solves

When we calculate salaries by hand using paper or spreadsheets we often make mistakes. Data can be wrong or inconsistent effort repeats and rules may be applied in ways by different people. This tool fixes that by checking data using the rules every time and showing a clear result.

Features

Collects employee details via the command line

Validates the Employee ID (must be 10 characters)

Validates years of experience (must be between 0 and 35)

Assigns basic salary based on employee tier

Calculates the bonus and final salary using experience‑based rules

Modular code: input, validation, calculation and display are separate files

Project Structure

.

├── input.py            # Entry point: collects input. Runs the program

├── val_empolyeid.py    # Employee ID validation

├── experienceverify.py # Experience validation

├── final_salary.py     # Bonus and final salary calculation

├── data.py             # Formats and prints employee details

├── main.py             # single-file version (see note below)

└── statement.md        # Project statement, scope and target users

Requirements

Python 3.6 or newer (uses f‑strings)

No external libraries needed

How to Run

From the project folder:

bash

python input.py

You will be prompted for:

Employee ID: 10 characters

Employee Name

Years of Experience: a whole number from 0 to 35

Tier: 1, 2 or any other number (see tables below)

Business Rules

Basic Salary by Tier

Tier	Basic Salary

1	$90,000

2	$70,000

Any other	$35,000

Bonus by Experience

Experience	Bonus

10+ years	20%

5 to 9 years	10%

Under 5 years	5%

Salary = Basic Salary + (Basic Salary × Bonus %)

Example Run

Enter Employee ID: EMP0001234

Enter Employee Name: Asha Patel

Enter Years of Experience: 7

Enter which tier employee you are: 2

Employee detail

ID: EMP0001234

Name: Asha Patel

Basic Salary: $70000

Experience: 7 years

Bonus Tier: 10.0%

Final Salary: $77000.0

How the Modules Fit Together

input.py

├── val_empolyeid.validate ID        → val_empolyeeid()

├── experienceverify.validate years  → validate_experience()

└── data.display_employee_info()

└── final_salary.calculate_final_salary()

input.py. Checks the data builds an employee tuple (emp_id, name, basic_salary experience) and sends it to display_employee_info() which then calls calculate_final_salary() and prints the outcome.

Note on main.py

main.py is a single‑file version of the same program. It differs from the version because it has no upper limit on experience uses $350,000 for tier 3 and does not handle an invalid tier safely. Use input.py as the entry point; main.py can be removed or kept only for reference.

Known Limitations

Non‑numeric input for experience or tier will raise a ValueError

Experience re‑prompts inside the validator show generic messages

Data is not saved anywhere; each run handles one employee

The Employee ID is checked for length only not for format or duplicates

Out of Scope (Current Version)

Graphical or web interface

Database or storage

Tax, PF or insurance deductions

PDF or printable pay slips

Multi‑user login or role‑based access

Attendance or leave tracking

Future Improvements

Handle non‑numeric input

Process multiple employees in one run

Save records to a file or database

Add deductions, allowances and pay slip generation

Add unit tests for each module

Target Users

Small business owners: quick salary calculation, without payroll software

HR / accounts staff: saves time and reduces errors

Students and beginners: an example of modular Python programming

Developers: a base to extend with new features
