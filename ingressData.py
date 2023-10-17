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
    individual_hours = []
    for full_name in unique_individuals:
        total_hours = (data_frame[data_frame['FULL NAMES'] == full_name]['Work done in hours'] > 0).sum()
        individual_hours.append(total_hours)

    result_df = pd.DataFrame({'FULL NAMES': unique_individuals, 'Days Worked': individual_hours,
                              'Overtime 1.5': 0, 'Overtime 2.0': 0})

    return result_df


def overtime_extraction():
    unique_day_types = data_frame['Day Type'].unique()
    results = pd.DataFrame(columns=list(unique_day_types))

    individual_totals = {}  # Dictionary to store individual totals for each day type

    for index, row in data_frame.iterrows():
        full_name = row['FULL NAMES']
        day_type = row['Day Type']
        overtime = row['Overtime']

        if full_name not in individual_totals:
            individual_totals[full_name] = {day_type: overtime}
        else:
            if day_type not in individual_totals[full_name]:
                individual_totals[full_name][day_type] = overtime
            else:
                individual_totals[full_name][day_type] += overtime

    rows_to_append = []

    for day_type_totals in individual_totals.values():
        row = [day_type_totals.get(dt, 0) for dt in unique_day_types]
        rows_to_append.append(row)

    result_df = pd.concat([results, pd.DataFrame(rows_to_append, columns=results.columns)],
                          ignore_index=True)

    return result_df


def save(savefile):
    results1 = name_hours_extraction()
    results2 = overtime_extraction()

    # data_frame['Workday O'] = data_frame['Overtime1.5']
    # Concatenate the DataFrames along the columns (axis=1)

    combined = pd.concat([results1, results2], axis=1)

    combined.to_excel(savefile, index=False)


savefile = 'output_excel_file3.xlsx'
save(savefile)
print('Data saved first time')


def column_correction(file, save_file):
    df = pd.read_excel(file)
    print(df.columns)
    df['Overtime 1.5'] = df['Workday  O']
    df['Overtime 2.0'] = df['Holiday OT'] + df['Restday OT']
    df.to_excel(save_file, index=False)
    print('saved second time')


column_correction(file=savefile, save_file=savefile)
