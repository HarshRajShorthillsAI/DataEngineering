import pandas as pd
import pandas_clean
import os
import sys

def join_in_dataset()->None:
    pass

def dataframe_filter()->None:
    original_stdout = sys.stdout

    sys.stdout = open(os.devnull, 'w') #this supresses any output
    df = pandas_clean.clean_dataset()
    sys.stdout = original_stdout

    print("dataframe printed")

    print(df.head(1))

    filteredDF = df.filter(items=['model', 'price($)'], axis=1)[df['price($)']>1000000]

    print(f"Car model name and price with price > $1M:\n{filteredDF}")

    filteredDF = df.filter(regex='e$', axis=1)
    print(filteredDF)

def dataframe_clean()->None:
    pd.set_option('display.max_column', None)          # Prints all the columns in dataframe
    pd.set_option("display.expand_frame_repr", False)  # Prevent line wrapping for dataframe
    df2 = pd.read_csv("Data/car_owners.csv", header=0)
    #print(df2.head(5))
    #print(df2.dtypes)
    df2 = df2.convert_dtypes()
    #print(df2.dtypes)

    df3 = pd.read_csv("Data/service_history.csv", header=0)
    # print(df3.head(5))
    #print(df3.dtypes)
    df3 = df3.convert_dtypes()
    #print(df3.dtypes)
    df3 = df3.rename(mapper={'service_cost': 'service_cost($)'}, axis='columns')
    #print(df3.head(5))
    print(df3.shape)

    df_joined = df2.set_index('model').join(df3.set_index('model'), how='left', rsuffix='(service_history)').query("model_year > 2013")
    print(f"The resultant dataframe for df2(car_owners) left join df3(service_history):\n{df_joined.head(5)}\n{df_joined.describe()}")

    df_joined = df2.join(df3, how='right', rsuffix='(service_history)')
    print(f"The resultant dataframe for df2(car_owner) right join df3(service_history):\n{df_joined.head(5)}\n{df_joined.describe()}")

    df_joined = df2.join(df3, how="inner", rsuffix='(service_history)')
    print(f"The resultant dataframe for df2(car_owner) inner join df3(service_history):\n{df_joined.head(5)}\n{df_joined.describe()}")

    df_joined = df2.join(df3, how='outer', rsuffix='(service_history)')
    print(f"The resultant dataframe for df2(car_owner) outer join df3(service_history):\n{df_joined.head(5)}\n{df_joined.describe()}")
    
if __name__=="__main__":
    dataframe_clean()