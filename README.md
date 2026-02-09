# Pandas Assignment – Series, DataFrame, Functions, Filtering & Analysis

## Overview

This assignment demonstrates the use of core Pandas functionalities for data manipulation and analysis. The tasks cover working with Pandas Series and DataFrames, performing mathematical and logical operations, filtering data, grouping, and basic visualization using only built-in Pandas plotting methods.



## File Structure

* `pandas_assignment.py`  – Contains all tasks in sequential order with comments.
* `README.md` – Documentation of the assignment.



## Tasks Description

### Task 1 – Pandas Series Basics

* Created a Pandas Series from a list of marks.
* Displayed values, index, and data type.
* Accessed first element and last two elements.

### Task 2 – Mathematical Operations on Series

* Added, subtracted, multiplied, and divided the Series values.
* Displayed result after each operation.

### Task 3 – Python Functionalities on Series

* Calculated maximum, minimum, sum, and mean.
* Used lambda function to check pass or fail (marks ≥ 70).
* Counted number of students who passed.

### Task 4 – Creating a DataFrame

* Created a DataFrame containing Name, Marks, and Subject.
* Displayed first 3 rows and last 2 rows.
* Printed shape and column names.

### Task 5 – Important DataFrame Functions

* Used info(), describe(), head(), and tail().
* Sorted data by marks in descending order.
* Reset the index after sorting.

### Task 6 – Filtering & Conditional Selection

* Filtered students with:

  * marks greater than 75
  * subject Math
  * marks above average
  * failed students (marks < 70)

### Task 7 – Grouping & Basic Analysis

* Calculated average marks per subject.
* Counted number of students per subject.
* Found maximum marks per subject.

### Task 8 – Pandas Plotting

* Bar plot of student names vs marks.
* Line graph of marks.
* Histogram of marks.
  Only DataFrame.plot() and Series.plot() were used.

### Task 9 – Sales Data Analysis

* Created sales DataFrame with revenue per day.
* Calculated:

  * total revenue
  * average revenue
  * day with highest revenue
  * days with revenue above average
* Plotted revenue vs day.



## Technologies Used

* Python
* Pandas Library
* Built-in Pandas Plotting


## How to Run

1. Install pandas if not installed:

   ```
   pip install pandas
   ```

2. Run the script:

   ```
   python pandas_assignment.py
   ```






