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
    unique_individuals = []
    individual_hours = []
    current_individual = None
    total_hours = 0
    for index, row in data_frame.iterrows():
        full_names = row['FULL NAMES']
        hours_worked = row['Work done in hours']

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
    return result_df


def overtime_extraction():
    unique_day_type = []
    number_of_day_types = []
    current_day_type = None
    total_day_types = 0

    day_type = 'Day Type'
    for index, row in data_frame.iterrows():
        if row[day_type] != current_day_type:
            if total_day_types > 0:
                unique_day_type.append(current_day_type)
                number_of_day_types.append(total_day_types)
            total_day_types = 0

        if pd.to_numeric(row['Day Type'], errors='coerce') > 0:
            total_day_types += 1

    if total_day_types > 0:
        unique_day_type.append(current_day_type)
        number_of_day_types.append(total_day_types)

    results = pd.DataFrame({'Day type': unique_day_type, 'total day types': number_of_day_types})
    return results


def save(savefile):
    results = name_hours_extraction()
    results2 = overtime_extraction()

    combined = pd.concat([results, results2], axis=0)
    combined.to_excel(savefile, index=False)


save(savefile='output_excel_file3.xlsx')
print('data saved')

# WHEN YOU READ THIS I KNOW YOU WILL BE CONFUSED BUT HERE IS THE THING
#  ARRANGE THE DAY TYPES IN ITS OWN COLUMN SO YOU CAN GET THE BEST RESULTS