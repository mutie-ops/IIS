import pandas as pd


def header_extraction(data):
    df = pd.read_excel(data)
    # extract the header
    header = df.columns.tolist()
    for headers in enumerate(header, start=1):
        print(headers)
    return df


data_frame = header_extraction('C:\\Users\\HP\\PycharmProjects\\IIS\data\\test2.xlsx')


def name_combination():
    first_name = data_frame['First Name']
    second_name = data_frame['Last Name']
    data_frame['FULL NAMES'] = first_name + '' + second_name
    print('...name extraction')


name_combination()


def name_hours_extraction():
    unique_individuals = data_frame['FULL NAMES'].unique()
    employee_id = data_frame['Employee ID'].unique()

    data_frame['Date'] = pd.to_datetime(data_frame['Date'], format='%d-%m-%Y', errors='coerce')
    data_frame['Date'] = data_frame['Date'].dt.date

    date_worked = data_frame.groupby('Employee ID')['Date'].min().reset_index()
    date_worked.set_index('Employee ID', inplace=True)
    #  group by employee id a get minimum date worked

    individual_hours = []
    for full_name in unique_individuals:
        total_hours = (data_frame[data_frame['FULL NAMES'] == full_name]['Work done in hours'] > 0).sum()
        individual_hours.append(total_hours)

    result_df = pd.DataFrame(
        {'FULL NAMES': unique_individuals,
         'Employee ID': employee_id,
         'Date Worked': date_worked.loc[employee_id]['Date'].values,
         'Days Worked': individual_hours,
         'Overtime 1.5': 0,
         'Overtime 2.0': 0})

    return result_df


def overtime_extraction():
    unique_day_types = data_frame['Day Type'].unique()
    results = pd.DataFrame(columns=list(unique_day_types))

    for full_name in data_frame['FULL NAMES'].unique():
        individual_totals = []

        for day_type in unique_day_types:
            # Filter the DataFrame for the specific full name and day type
            filtered_df = data_frame[(data_frame['FULL NAMES'] == full_name) & (data_frame['Day Type'] == day_type)]
            total_overtime = filtered_df['Overtime'].sum()

            individual_totals.append(total_overtime)

        results.loc[len(results)] = individual_totals

    return results


def save(savefile):
    results1 = name_hours_extraction()
    results2 = overtime_extraction()
    combined = pd.concat([results1, results2], axis=1)
    combined.to_excel(savefile, index=False)


savefile = 'output_excel_file4.xlsx'
save(savefile)
print('Data saved first time')


def final_excel_sheet(file, save_file):
    df = pd.read_excel(file)
    # print(df.columns)
    df['Overtime 1.5'] = df['Workday  O']
    df['Overtime 2.0'] = df['Holiday OT'] + df['Restday OT']
    df.to_excel(save_file, index=False)
    print('saved second time')


final_excel_sheet(file=savefile, save_file=savefile)
