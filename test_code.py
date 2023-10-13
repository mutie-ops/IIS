import pandas as pd

# Specify the path to your Excel file
excel_data_path = 'your_input_excel_file.xlsx'

# Read the data from the Excel file
data_frame = pd.read_excel(excel_data_path)

# Combine first name and last name into a single column
data_frame['Full Name'] = data_frame['First Name'] + ' ' + data_frame['Last Name']

# Specify the header for hours worked
hours_worked_header = 'Hours Worked'

# Initialize lists to store the results
unique_individuals = []
individual_hours = []

# Initialize variables to keep track of the current individual and their total hours
current_individual = None
total_hours = 0

# Iterate through the rows
for index, row in data_frame.iterrows():
    full_name = row['Full Name']
    hours_worked = row[hours_worked_header]

    if full_name != current_individual:
        # If a new individual is encountered, add the previous individual's total hours (if > 0)
        if total_hours > 0:
            unique_individuals.append(current_individual)
            individual_hours.append(total_hours)
        current_individual = full_name
        total_hours = 0

    if hours_worked > 0:
        total_hours += 1

# Add the last individual's total hours (if > 0)
if total_hours > 0:
    unique_individuals.append(current_individual)
    individual_hours.append(total_hours)

# Create a new DataFrame with unique full names and total hours worked
result_df = pd.DataFrame({'Full Name': unique_individuals, 'Total Hours Worked': individual_hours})

# Specify the path for the output Excel file
output_excel_file = 'output_excel_file.xlsx'

# Write the result DataFrame to a new Excel file
result_df.to_excel(output_excel_file, index=False)

print(f"Data has been saved to {output_excel_file}")
