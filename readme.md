Project Title
Simple Command-Line Budget Tracker

Overview of the Project
This project is a user-friendly, console-based budget tracking application written in Python. It provides a simple interface for users to record their daily expenses and view an organized summary of their spending.

The application uses the built-in Python csv module for data management, storing all expense records in a file named expenses.csv. This ensures data persistence and allows for easy inspection or modification of records outside the program.

Features
Expense Recording: Allows users to input the date, category, and amount for a new expense.

Automated Date: Defaults the date to today's date if the input is left blank.

Input Validation: Ensures that dates are in the correct YYYY-MM-DD format and amounts are positive numbers.

Expense Summary: Calculates and displays the Total Recorded Spending.

Category Analysis: Presents a detailed breakdown of spending by category, showing the total amount spent per category and its corresponding percentage of the overall spending. Categories are sorted by amount (highest to lowest).

Data Storage: Persists data in a standard CSV file (expenses.csv).

Technologies/Tools Used
Programming Language: Python 3.x

Core Libraries:

csv: For reading and writing the expense data file.

datetime: For handling and validating date inputs.

os: For checking and creating the data file.

Steps to Install & Run the Project
The project is a standalone Python script and requires no external packages.

Save the Code: Save the provided Python source code into a file (e.g., budget_tracker.py).

Open Terminal: Navigate to the directory where you saved the file using your command-line interface.

Execute the Script: Run the application using the Python interpreter:

Instructions for Testing
Initial Run: Run the script. A file named expenses.csv should be created automatically in the same directory if it doesn't already exist.

Adding Expenses (Option 1):

Select 1.

Test entering a custom date (YYYY-MM-DD).

Test leaving the date blank to use today's date.

Test entering different categories (e.g., Food, Transport, Rent).

Test entering valid amounts (e.g., 45.99) and invalid inputs (non-numeric, negative).

Viewing Summary (Option 2):

Select 2.

Verify the Total Recorded Spending matches the sum of all entered amounts.

Verify the Category Breakdown accurately reflects the total spent per category and its percentage share.

Exit: Select 3 to close the application.
