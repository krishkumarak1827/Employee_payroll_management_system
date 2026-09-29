# Employee_payroll_management_system


A Python console program that gathers employee details checks them. Works out the final salary.

---

## 📌 Overview

Counting salaries by hand is slow. Can lead to mistakes. This project helps with that by taking employee data checking the employee ID and work experience and then working out the salary. It is made in Python and each part is kept in a separate file.

---

## ✨ Features

- Gets employee data from a command‑line interface

- Checks that the employee ID format is correct

- Confirms the employee has work experience

- Computes the final salary

- Code is split into modules: input, validation and calculation are separate

- Can be expanded easily to add tax, PF, allowances or bonuses

---

## 🛠️ Technologies / Tools Used

| Tool | Purpose |

|------|---------|

Python 3.8+ | Core programming language |

| Git & GitHub | Version control and hosting |

| VS Code / any editor Development |

No external libraries are needed.

---

## 📁 Project Structure

```

Employee_payroll_management_system/

├── README.md              # Project documentation

├── input.py               # Takes employee details as input

├── val_empolyeid.py       # Validates the employee ID

├── experienceverify.py    # Verifies employee experience

├── data.py                # Employee / salary data

└── final_salary.py        # Calculates the salary

```

---

## 🚀 Installation & Running the Project

### Prerequisites

- [Python 3.8 or higher](https://www.python.org/downloads/)

- [Git](https://git-scm.com/downloads)

Check your Python version:

```bash

python --version

```

### Steps

1. **Clone the repository**

```bash

git clone https://github.com/krishkumarak1827/Employee_payroll_management_system.git

```

2. **Go into the project folder**

```bash

cd Employee_payroll_management_system

```

3. **Run the program**

```bash

python input.py

```

> If the program starts from a file, such as `final_salary.py` run that file instead.

4. **Follow the prompts** in the terminal to enter the employee details and view the salary.

---

## 🧪 Instructions for Testing

The project has no automated test suite yet so test it manually with the cases

### Manual test cases

| # | Test | Input | Expected result

|---|------|-------|-----------------|

| 1 | Valid employee | Valid ID, experience | Salary is calculated and displayed |

2 | Invalid employee ID | Wrong-format or empty ID | Error message; ID is rejected |

| 3 Zero experience | Experience = 0 | Handled correctly ( salary only) |

| 4 | Negative experience | Experience = -1 | Rejected with an error message |

| 5 Non-numeric input | Letters where a number is expected Rejected without crashing |

| 6 High experience | Experience = 30+ | Salary is calculated correctly |

### Running modules

```bash

python val_empolyeid.py

python experienceverify.py

python final_salary.py

```

### (Optional) Automated tests with `pytest`

```bash

pip install pytest

pytest

```

Create a `tests/` folder with files such as `test_validation.py` and `test_salary.py` to add unit tests.

---

## 📸 Screenshots

> Add screenshots of the program running in your terminal.

| Screen Screenshot |

|--------|-----------|

| Employee input | `![Input](screenshots/input.png)`

| Validation error | `![Error](screenshots/error.png)`

| Final salary output | `![Output](screenshots/output.png)` |

Create a `screenshots/` folder in the repo add your images and update the paths above.

---

## 🔮 Future Improvements

- Add tax, PF and allowance calculations

- Save employee records in a file or database such as CSV, SQLite or MySQL

- Generate pay slips, in PDF format

- Provide a GUI or web interface

- Write automated unit tests

---

## 🤝 Contributing

1. Fork the repository

2. Create a branch: `git checkout -b feature/your-feature`

3. Commit your changes: `git commit -m "Add your feature"`. Commit with a message.

4.. Open a Pull Request. Push your changes. Open the Pull Request.

---

## 👤 Author

**krishkumarak1827**

GitHub: [@krishkumarak1827](https://github.com/krishkumarak1827)
