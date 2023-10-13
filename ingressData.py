import pandas as pd

#  get the data
excel_data_path = 'C:\\Users\\Benjamin Mutie\\Desktop\\IIS\data\\test2.xlsx'

# read the data in excel format
data_frame = pd.read_excel(excel_data_path)

# extract the header
header = data_frame.columns.tolist()
print(header)

first_name = data_frame['First Name']
second_name = data_frame['Last Name']
week_day = data_frame['Weekday']

data_frame['FULLNAMES'] = first_name + second_name
hours_worked_header = 'Work done in hours'

unique_individuals = []
individual_hours = []

current_individual = None
total_hours = 0
# convert hours worked to numeric
for index, row in data_frame.iterrows():
    full_names = row['FULLNAMES']
    hours_worked =  row[hours_worked_header]

    if full_names != current_individual:
        if total_hours > 0:
            unique_individuals.append(current_individual)
            individual_hours.append(total_hours)
        current_individual = full_names
        total_hours = 0

    if hours_worked > 0:
        total_hours += 1

if total_hours > 0:
    unique_individuals.append(current_individual)
    individual_hours.append(total_hours)

    # Create a new DataFrame with unique full names and total hours worked
result_df = pd.DataFrame({'Full Name': unique_individuals, 'Days Worked': individual_hours})

# Specify the path for the output Excel file
output_excel_file = 'output_excel_file2.xlsx'

# Write the result DataFrame to a new Excel file
result_df.to_excel(output_excel_file, index=False)

print(f"Data has been saved to {output_excel_file}")
