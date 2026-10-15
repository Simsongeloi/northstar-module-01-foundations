# generate_bakery_data.py
# Lesson 1.2: Types of Data and where to find it
# Author: Simsong Eloi
# Date: 10/14/2026
#
# Generate a synthetic dataset of 50 fictional Crescent Bakery customers
# illustrating the four scales of measurement (nominal, ordinal, interval, ratio). Saves the result as bakery_customers.csv.

import random
import numpy as np
import pandas as pd
from datetime import date

random.seed(42)
np.random.seed(42)

n_customers = 50

# Region (nominal scale: categorical with no order)
regions = np.random.choice(
    ["Downtown", "North Side", "South Side", "West End"],
    size=n_customers,
    p=[0.40, 0.25, 0.20, 0.15],
   
)

# Satisfaction (ordinal scale: ordered categories with unequal gaps)
satisfaction = np.random.choice(
    [1, 2, 3, 4, 5],
    size=n_customers,
    p=[0.05, 0.10, 0.20, 0.35, 0.30],
    
)

# Year of first visit (interval scale: ordered with equal gaps, no true zero)
first_visit_year = np.random.randint(2018, 2026, size=n_customers)

# Total spent in dollars (ratio scale: ordered, equal gaps, true zero)
total_spent = np.random.normal(loc=250, scale=80, size=n_customers)
total_spent = np.round(total_spent, 2)
total_spent = np.maximum(total_spent, 0)


# Visits in the last year (ratio scale)
visits_last_year = np.random.poisson(lam=8, size=n_customers)

# Customer ID (nominal: numerical-looking labels with no order)
customer_ids = [f"CUST-{random.randint(10000, 99999)}" for _ in range(n_customers)]

# Combine all six columns into a Pandas DataFrame
bakery_customers = pd.DataFrame({
    "customer_id": customer_ids,
    "region": regions,
    "first_visit_year": first_visit_year,
    "satisfaction": satisfaction,
    "total_spent_usd": total_spent,
    "visits_last_year": visits_last_year,
})

# Display the first 10 customers
print(bakery_customers.head(10))

# Display the number of rows and columns
print(f"\nShape: {bakery_customers.shape}")

# Display the data type of each column
print(f"\nColumn types:\n{bakery_customers.dtypes}")
# Display the first 10 customers
print(bakery_customers.head(10))

# Display the number of rows and columns
print(f"\nShape: {bakery_customers.shape}")

# Display the data type of each column
print(f"\nColumn types:\n{bakery_customers.dtypes}")

# Save the DataFrame as a CSV file
bakery_customers.to_csv("bakery_customers.csv", index=False)

print("\nDataset saved successfully!")