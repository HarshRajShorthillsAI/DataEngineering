import pandas as pd
import numpy as np

def clean_dataset()->pd.DataFrame: 
    pd.set_option('display.max_columns',None)

    data = pd.read_csv('Data/used_cars.csv', header=0, delimiter=',')

    print(f"Following is the pandas dataframe created from csv:\n{data.head(5)}")

    print(data.dtypes)

    print(f"Following is the datatypes for the dataframe created:\n{data.dtypes}")

    converted_data = data.convert_dtypes()

    print(f"Converted the data to proper datatypes using pandas:\n{converted_data.dtypes}")

    print(f"Converted data:\n{converted_data.head(5)}")

    # Modify column data like mileage, price

    df1 = converted_data.fillna('')

    df1 = df1.rename(mapper={'milage': 'milage(mi.)'}, axis='columns')

    print(df1.dtypes)

    print(df1['milage(mi.)'])

    df1['milage(mi.)'] = df1['milage(mi.)'].str.replace(',','').str.replace('mi.','')

    print(f"Dataframe after replacing ',' and 'mi.' from clean_title:\n{df1['milage(mi.)']}")

    df1 = df1.rename(mapper={"price": "price($)"}, axis='columns')

    print(df1.dtypes)

    print(df1['price($)'])

    df1['price($)'] = df1['price($)'].str.replace(',','').str.replace('$', '')

    print(f"Dataframe after replaceing ',' and '$' from price:\n{df1['price($)']}")

    print(df1.head())

    df1.convert_dtypes()

    print(f"Dataframe column types after applying convert dtypes{df1.dtypes}")
    df1['milage(mi.)'] = df1['milage(mi.)'].astype(dtype='Int64')
    df1['price($)'] = df1['price($)'].astype(dtype='Int64')
    print(f"Since convert dtypes seems to be converting only to string[python], lets manually typecast the columns appropriately{df1.dtypes}")

    return df1