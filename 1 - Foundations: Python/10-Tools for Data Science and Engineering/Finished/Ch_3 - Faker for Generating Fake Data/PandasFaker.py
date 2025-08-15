# Example file for Advanced Python: Top Tools for Data Science
# Using the Faker library along with Pandas to generate testing data


import faker
import pandas as pd


# Create Faker instance
fake = faker.Faker()

# Create Faker instance and set seed for reproducibility
faker.Faker.seed(12345)

def generate_personnel_data(num_records=20):
    # Define departments
    departments = ['sales', 'engineering', 'marketing', 'HR']
    
    # Initialize lists to store data
    employee_data = []
    
    for _ in range(num_records):
        emp_id = f"EMP{fake.unique.random_number(digits=5, fix_len=True)}"
        
        # Generate name components
        first_name = fake.first_name()
        last_name = fake.last_name()
        
        # Generate unique company email
        email = f"{first_name.lower()}.{last_name.lower()}@company.com"
        
        # Create employee record
        employee = {
            'employee_id': emp_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': fake.phone_number(),
            'address': fake.address().replace('\n', ', '),
            'salary': fake.pyfloat(min_value=50000,max_value=150000,right_digits=2),
            'years_employed': fake.random_int(min=1, max=20),
            'department': fake.random_element(elements=departments)
        }
        
        employee_data.append(employee)
    
    # Create DataFrame
    df = pd.DataFrame(employee_data)
    df = df.set_index("employee_id")
    
    # Sort by the number of years of service
    df = df.sort_values('years_employed')
    
    return df


# Generate the personnel data
employees_df = generate_personnel_data()

# Display the data
print("Personnel Records:")
print(employees_df.to_string())

# Display some basic statistics
print("\nDataset Statistics:")
print(f"Total Employees: {len(employees_df)}")
print("\nEmployees per Department:")
print(employees_df['department'].value_counts())
print("\nSalary Statistics:")
print(employees_df['salary'].describe())
