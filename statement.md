Problem Statement
Many individuals struggle with manually tracking and understanding their spending habits, leading to poor financial awareness and difficulty in setting and achieving budget goals. Existing complex budgeting software often has a steep learning curve or requires constant internet access. There is a need for a simple, accessible, and fast tool that allows users to record daily expenses and immediately visualize their spending breakdown without relying on external services or complex interfaces.

Scope of the Project
The scope of this project is to create a fully functional, console-based application that manages personal expense tracking.

In-Scope:

Implementing a command-line interface (CLI) for user interaction.

Recording expense details (Date, Category, Amount).

Saving and loading data using a local CSV file (expenses.csv).

Generating a basic summary, including total spending and categorical breakdown (amount and percentage).

Input validation for dates and amounts.

Out-of-Scope (Future Enhancements):

Handling income or savings.

Setting budget limits or targets.

Advanced features like data filtering, sorting by date/category, or data visualization (graphs).

User authentication or multi-user support.

Target Users
The primary target users are individuals who:

Prefer Simplicity: People who want a quick and straightforward way to log expenses without the overhead of heavy graphical applications or mobile apps.

Students and Developers: Users familiar with the command line who need a basic utility for personal finance management.

Beginners in Finance Tracking: Individuals who are starting to track their spending and require an accessible tool to build the habit.

High-Level Features
Expense Logging: Provide a clear interactive prompt for users to input a date (defaulting to today), a category (e.g., Food, Rent, Transport), and the expense amount.

Data Persistence: Automatically save all recorded expense data to a local expenses.csv file, ensuring data is retained across sessions.

Summary Generation: Calculate and display the total sum of all recorded expenses.

Categorical Analysis: Show a summary table listing each unique expense category, its total accumulated spending, and its proportional contribution (percentage) to the overall total.