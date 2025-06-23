import pandas as pd
import wfdb

def convert_dat_to_csv(dat_file, csv_file=None):

    record = wfdb.rdrecord(dat_file)

    fs = record.fs
    time = [i / fs for i in range(len(record.p_signal))]

    df = pd.DataFrame(record.p_signal, columns=record.sig_name)

    df.insert(0, 'Time (s)', time)
    csv_file = f"{dat_file}.csv"
    df.to_csv(csv_file, index=False)


    # Save the DataFrame to a .csv file
    print(f"Archive '{csv_file}' has been created successfully.")
    