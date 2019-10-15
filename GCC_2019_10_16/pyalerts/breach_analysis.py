'''
Mini-module to house code tasked with analysing latest data file
'''

# Standard library imports
from dateutil.relativedelta import relativedelta

# External library imports
import pandas as pd

def identify_breaches(data_path=None):
    '''
    Returns a nested dictionary for each board with each 
    indicator breach as an inner dictionary with the following fields:

        date: latest Reporting Date for that indicator
        indicator_id: corresponds to INDICATOR_ID
        indicator_name: corresponds to INDICATOR_SHORT_NAME
        board_rate: RATE CALCULATION BY MONTH
        target: TARGET
        timetrend: list of tuples [(date, rate), ...]
        boxplot: list of tuples [(location, rate), ...]

    Check that quarterly indicators aren't flagged up every month
    '''

    if data_path is None:
        data_path = "latest_data.csv"

    df = pd.read_csv(data_path)
    df['Reporting Date'] = pd.to_datetime(df['Reporting Date'], dayfirst=True)

    breach_info = {}

    for hb in df['Location Treatment Desc'].unique():

        #build a list of indicators that we'll be sending an alert about:
        mask = (
            (df['Location Treatment Desc'] == hb) &
            (df['Target_Breach']) &
            (df['Reporting Date'] == df['Reporting Date'].max())
        )

        breaching_indicators = df[mask]['INDICATOR_ID'].unique()

        #initialise outer breach dict if there aren't any breaches
        if df[mask].shape[0] == 0:
            continue
            
        breach_info[hb] = {}

        #populate the breach_info dictionary
        for i, ind in enumerate(breaching_indicators):
            #subset of the dataframe used for the iteration
            breach_df = df[df['INDICATOR_ID'] == ind]

            #define filters
            mask_hb = (
                (breach_df['Location Treatment Desc'] == hb) &
                (breach_df['Reporting Date'] >
                 df['Reporting Date'].max() - relativedelta(months=12))
            )
            
            mask_latest = (breach_df['Reporting Date'] == df['Reporting Date'].max())

            #further subset the dataframe using filters
            breach_hb = breach_df[mask_hb]
            breach_latest = breach_df[mask_latest]
            breach_hb_latest = breach_df[mask_hb & mask_latest]

            #start populating the inner dictionaries
            breach_info[hb][f"breach_{i}"] = {}
            breach_dict = breach_info[hb][f"breach_{i}"]

            time_cols = ['Reporting Date', 'Rate Calculation By Month']
            box_cols = ['Location Treatment Desc', 'Rate Calculation By Month']

            breach_dict["date"] = breach_df['Reporting Date'].max()
            breach_dict["indicator_id"] = ind
            breach_dict["indicator_name"] = breach_df['INDICATOR_SHORT_NAME'].iloc[0]
            breach_dict["board_rate"] = breach_hb_latest['Rate Calculation By Month'].iloc[0]
            breach_dict["target"] = breach_hb_latest['Target'].iloc[0]
            breach_dict["timetrend"] = [tuple(x) for x in breach_hb[time_cols].values]
            breach_dict["boxplot"] = [tuple(x) for x in breach_latest[box_cols].values]

    return breach_info
    