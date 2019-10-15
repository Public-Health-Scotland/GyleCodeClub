'''
Add a single month to the latest_data.csv
'''

# Standard library imports
from datetime import datetime
import random

# External libarary imports
import pandas as pd


def simulate():
    '''
    Returns full 2017 data + a random allocation of continuous months from 2018
    '''

    df_full = pd.read_csv("data/full_data.csv")
    df_full['Reporting Date'] = pd.to_datetime(df_full['Reporting Date'], dayfirst=True)

    df_2017 = df_full[df_full['Reporting Date'] <= datetime(2017, 12, 1)]

    rand_months = random.randint(1, 12)
    df_extra = df_full[
        (datetime(2017, 12, 1) < df_full['Reporting Date']) &
        (df_full['Reporting Date'] <= datetime(2018, rand_months, 1))
        ]

    return pd.concat([df_2017, df_extra])

def main():
    '''
    Main function
    '''
    sim_df = simulate()
    sim_df.to_csv("latest_data.csv", index=False)
    print("done")

if __name__ == "__main__":
    main()
