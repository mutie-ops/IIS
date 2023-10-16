import pandas as pd


def header_extraction(data):
    df = pd.read_excel(data)
    # extract the header
    header = df.columns.tolist()
    for headers in enumerate(header, start=1):
        print(headers)
    return df


data_frame = header_extraction('C:\\Users\\Benjamin Mutie\\Desktop\\IIS\data\\test2.xlsx')

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

    result_df = pd.DataFrame({'FULL NAMES': unique_individuals, 'Days Worked': individual_hours})
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

    # create new columns OT 1.5 AND OT 2.0
    overtime_1_5=
    result_df = pd.concat([results, pd.DataFrame(rows_to_append, columns=results.columns)], ignore_index=True)

    return result_df


def save(savefile):
    results1 = name_hours_extraction()
    results2 = overtime_extraction()

    # Concatenate the DataFrames along the columns (axis=1)
    combined = pd.concat([results1, results2], axis=1)

    combined.to_excel(savefile, index=False)


savefile = 'output_excel_file3.xlsx'
save(savefile)
print('Data saved')
