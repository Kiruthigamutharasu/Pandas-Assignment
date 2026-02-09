
# Assignment 10: Pandas (Series, DataFrame, Functions, Filtering & Analysis)


# Task 1: Pandas Series Basics


# 1. Import pandas
import pandas as pd

# 2. Create a Pandas Series
marks = pd.Series([78, 85, 90, 66, 72])

# 3. Print Series details
print("Series Values:")
print(marks.values)

print("\nSeries Index:")
print(marks.index)

print("\nData Type:")
print(marks.dtype)

# 4. Access elements
print("\nFirst Element:")
print(marks[0])

print("\nLast Two Elements:")
print(marks.tail(2))



# Task 2: Mathematical Operations on Series


print("\nAdd 5 grace marks:")
print(marks + 5)

print("\nSubtract 2 marks:")
print(marks - 2)

print("\nMultiply marks by 1.05:")
print(marks * 1.05)

print("\nDivide marks by 2:")
print(marks / 2)



# Task 3: Python Functionalities on Series

print("\nMaximum Marks:", marks.max())
print("Minimum Marks:", marks.min())
print("Sum of Marks:", marks.sum())
print("Mean Marks:", marks.mean())

# Lambda function to check pass (>=70)
passed = marks.apply(lambda x: "Pass" if x >= 70 else "Fail")
print("\nPass/Fail Status:")
print(passed)

# Count how many students passed
count_passed = marks[marks >= 70].count()
print("\nNumber of students passed:", count_passed)



# Task 4: Create a DataFrame


students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nShape of DataFrame:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)



# Task 5: Important DataFrame Functions


print("\nInfo of DataFrame:")
print(df.info())

print("\nDescription:")
print(df.describe())

print("\nHead:")
print(df.head())

print("\nTail:")
print(df.tail())

# Sort by Marks descending
sorted_df = df.sort_values(by='Marks', ascending=False)
print("\nSorted by Marks Descending:")
print(sorted_df)

# Reset index
sorted_df = sorted_df.reset_index(drop=True)
print("\nAfter Reset Index:")
print(sorted_df)



# Task 6: Filtering & Conditional Selection

print("\nStudents with more than 75 marks:")
print(df[df['Marks'] > 75])

print("\nStudents belonging to Math:")
print(df[df['Subject'] == 'Math'])

print("\nStudents with marks more than average:")
print(df[df['Marks'] > df['Marks'].mean()])

print("\nStudents who failed (marks < 70):")
print(df[df['Marks'] < 70])



# Task 7: Grouping & Basic Analysis


print("\nAverage marks per subject:")
print(df.groupby('Subject')['Marks'].mean())

print("\nNumber of students per subject:")
print(df.groupby('Subject')['Name'].count())

print("\nMaximum marks per subject:")
print(df.groupby('Subject')['Marks'].max())



# Task 8: Pandas Plotting (Simple Graphs)


# 1. Bar plot: student names vs marks
df.plot(x='Name', y='Marks', kind='bar', title='Student Marks')

# 2. Line graph of marks
df['Marks'].plot(kind='line', title='Marks Line Graph')

# 3. Histogram of marks
df['Marks'].plot(kind='hist', title='Marks Distribution')


# Task 9: Mini Use Case – Sales Data Analysis

sales = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
})

print("\nTotal Revenue:", sales['Revenue'].sum())

print("Average Daily Revenue:", sales['Revenue'].mean())

print("Day with Highest Revenue:")
print(sales[sales['Revenue'] == sales['Revenue'].max()])

print("\nDays where revenue > average:")
print(sales[sales['Revenue'] > sales['Revenue'].mean()])

# Plot revenue vs day
sales.plot(x='Day', y='Revenue', kind='bar', title='Revenue per Day')



