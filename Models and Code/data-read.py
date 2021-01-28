import pandas as pd
import scipy.io
import os

filenames = []

for filename in os.listdir('.'):
    if '.mat' in filename:
        filenames.append(filename)

for filename in filenames:
    print(f'Processing file: {filename}')
    mat = scipy.io.loadmat(filename)

    headings = [
        'Timestamp', 'Voltage', 'Current', 'Ah',
        'Wh', 'Power', 'Battery Temp',
        'Time', 'Chamber Temp'
    ]

    data = {}

    for i, heading in enumerate(headings):
        if heading == 'Timestamp':
            continue

        data[heading] = [point[0] for point in mat['meas'][0][0][i]]

    df = pd.DataFrame(data)

    csv_filename = filename.replace('.mat', '.csv')
    df.to_csv('csv-data/' + csv_filename, index=False)
