from asyncore import write
import pandas as pd
import csv


def clean_data():
    df = pd.read_csv('./data_1.csv')

    # Drop NAN Values
    df = df.dropna(axis=0)

    # Convert Values to Floats
    df['Radius'] = df['Radius'].astype(float)
    df['Mass'] = df['Mass'].astype(float)

    # Convert Values to Solar Values
    df['Radius'] = df['Radius'] * 0.102763
    df['Mass'] = df['Mass'] * 0.000954588

    # Create New CSV File
    df.to_csv('cleaned_data.csv', index=False)

    merge_data()


def merge_data():
    # Get the Data
    dataset_1 = []
    dataset_2 = []

    with open('cleaned_data.csv', 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            dataset_1.append(row)

    with open('data_2.csv', 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            dataset_2.append(row)

    # Prepare the Merge
    labels = dataset_1[0]

    data_1 = dataset_1[1:]
    data_2 = dataset_2[1:]

    data = data_1 + data_2

    print(data[:10])
    write_CSV(data, labels)


def write_CSV(data, labels):
    with open('output.csv', 'a+') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(labels)
        csv_writer.writerows(data)


clean_data()
