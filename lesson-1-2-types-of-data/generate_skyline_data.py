
# generate_skyline_data.py
# Lesson: Creation of Synthetic Data
# Author: Simsong Eloi
# Date: 10/15/2026

# Generate a synthetic dataset of 100 rows and 6 columns

import random
import numpy as np
import pandas as pd

# Set random seeds for reproducible results
random.seed(123)
np.random.seed(123)

size = 100

# Generate enrollment IDs
enrollment_ids = []
for number in range(1, size + 1):
    enrollment_ids.append(f"ENR-{number:06d}")

# Generate course names
courses = [
    "Intro to Analytics",
    "Python for Beginners",
    "SQL Basics",
    "Tableau Fundamentals",
    "Statistics 101"
]

course_names = []
for number in range(size):
    course_names.append(random.choice(courses))

# Generate enrollment years
enrollment_years = []
for number in range(size):
    enrollment_years.append(random.randint(2022, 2025))

# Generate final grades
grades = ["A", "B", "C", "D", "F"]

final_grades = random.choices(
    grades,
    weights=[0.10, 0.45, 0.35, 0.07, 0.03],
    k=size
)

# Generate hours studied using normal distribution
hours_studied = np.random.normal(
    loc=30,
    scale=8,
    size=size
)
hours_studied = np.round(hours_studied, 2)

# Generate completion statuses
completion_status = ["Completed", "Dropped", "in Progress"]

completion_scale = random.choices(
    completion_status,
    weights=[0.7, 0.1, 0.2],
    k=size
)

# Create pandas DataFrame
skyline_enrollments = pd.DataFrame({
    "enrollment_id": enrollment_ids,
    "course_name": course_names,
    "enrollment_year": enrollment_years,
    "final_grade": final_grades,
    "hours_studied": hours_studied,
    "completion_status": completion_scale
})

# Export DataFrame to CSV
skyline_enrollments.to_csv(
    "skyline_enrollments.csv",
    index=False
)

print("CSV file generated successfully!")

# Display dataset information
print("\nDataset shape:")
print(skyline_enrollments.shape)

print("\nColumn data types:")
print(skyline_enrollments.dtypes)

print("\nFirst 10 enrollment records:")
print(skyline_enrollments.head(10))

# Completion status analysis
print("\nCompletion status counts:")
print(skyline_enrollments["completion_status"].value_counts())

completed = completion_scale.count("Completed")
dropped = completion_scale.count("Dropped")
in_progress = completion_scale.count("in Progress")

print(f"\nTotal enrollment records: {len(skyline_enrollments)}")
print(f"Total completed: {completed}")
print(f"Total dropped: {dropped}")
print(f"Total in progress: {in_progress}")

# Study hours statistics
print(f"\nAverage hours studied: {hours_studied.mean():.2f}")
print(f"Minimum hours studied: {hours_studied.min():.2f}")
print(f"Maximum hours studied: {hours_studied.max():.2f}")

# Calculate completion rate
completion_rate = (completed / size) * 100
print(f"Completion rate: {completion_rate:.2f}%")

# Validate dataset
print("\nDataset validation:")
print(f"Total enrollment IDs: {len(enrollment_ids)}")
print(f"Unique enrollment IDs: {len(set(enrollment_ids))}")
print(f"Total course names: {len(course_names)}")
print(f"Total grades: {len(final_grades)}")
print(f"Enrollment year range: {min(enrollment_years)} - {max(enrollment_years)}")
