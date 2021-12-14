
import pandas as pd
import numpy as np

def data_loader(path,limit=0,chunksize_=10000):
    """ Description: this function will load data for each file and specified path

        Parameters:
        -----------
        path: path of the json file compressed with bz2
        limit: will limit the number of chunck loaded if bigger than 0
        chunksize_ = the number of quotes extracted for each chunk

        Total number of quotes = limit*chunksize_
        if you want to load all quotes put limit = 0

        Outputs:
        --------
        df_quotes: pandas dataframe quotes with necessary columns

    """
    eps=1e-1 # precision for progression

    print(f"\nLoading file: \"{path}\"")
    print("Beginning: Loading Quotes...")


    df_reader = pd.read_json(path, lines=True, compression='bz2', chunksize = chunksize_, nrows=1e12) # here we only loaded the quotes from 2016, but we can simply change the year to have the others

    for i,chunk in enumerate(df_reader):

        # Keep track of progression
        if limit!=0 and (i/limit%0.1<eps):
            print(f"    Loading... {i/limit*100:.2f} %")

    # Initialize the DataFrame columns with first chunk
        if i == 0:
          df_quotes = pd.DataFrame(chunk)
        else:
          # Concatenation of new chunk into the DataFrame
           df_quotes = pd.concat([df_quotes,chunk])

        # We don't want to read it all as long as we do not have the final code
        if i>=limit and limit!=0:
            break

    clean_data(df_quotes)
    print(f"Number of quotes loaded in {path}:", len(df_quotes))

    return df_quotes


def clean_data(data):
    """ Description: this function will load data for each file and specified path

        Parameters:
        -----------
        data: pandas dataframe from the quotebank datasets

        Outputs:
        --------
        df_quotes: pandas dataframe quotes without the phase and qids columns

    """
    eps=1

    # Drop duplicated rows
    data.drop_duplicates(subset="quoteID")

    # Drop columns: phase and qids that are not of interest to us
    data.drop(columns=['phase','qids'])


def get_slice(df_quotes,month,start_date=-1,end_date=32):


    df_quotes.sort_values(by=['date'], inplace=True, ascending=True)

    ##### IMPORTANT: we take only a subset of quotes for a given time window
    df_quotes = df_quotes[df_quotes.date.dt.month == month] # The 2016 United States elections were held on Tuesday, November 8, 2016, let's look around this period (this month)
    df_quotes = df_quotes[df_quotes.date.dt.day <= 30]
    df_quotes = df_quotes[df_quotes.date.dt.day >= 0]
    return df_quotes
