import pandas as pd
import pandas_clean
import numpy as np
import os
import sys

def join_in_dataset(df2:pd.DataFrame, df3:pd.DataFrame)->None:
    df_joined = df2.set_index('model').join(df3.set_index('model'), how='left', rsuffix='(service_history)').query("model_year > 2013")
    print(f"The resultant dataframe for df2(car_owners) left join df3(service_history):\n{df_joined.head(5)}\n{df_joined.describe()}")

    df_joined = df2.join(df3, how='right', rsuffix='(service_history)')
    print(f"The resultant dataframe for df2(car_owner) right join df3(service_history):\n{df_joined.head(5)}\n{df_joined.describe()}")

    df_joined = df2.join(df3, how="inner", rsuffix='(service_history)')
    print(f"The resultant dataframe for df2(car_owner) inner join df3(service_history):\n{df_joined.head(5)}\n{df_joined.describe()}")

    df_joined = df2.join(df3, how='outer', rsuffix='(service_history)')
    print(f"The resultant dataframe for df2(car_owner) outer join df3(service_history):\n{df_joined.head(5)}\n{df_joined.describe()}")

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

def dataframe_readData()->None:
    pd.set_option('display.max_column', None)          # Prints all the columns in dataframe
    # pd.set_option("display.expand_frame_repr", False)  # Prevent line wrapping for dataframe
    df = pandas_clean.clean_dataset()
    test_data = df.copy()
    test_data = test_data.convert_dtypes()
    print(f"test_data.iloc[0]:\n{test_data.iloc[0]}\n")
    print(f"test_data.index:\n{test_data.index}\n")
    print(f"test_data.loc[3]:\n{test_data.loc[3]}\n")
    print(f"test_data.at(2, 'model'):\n{test_data.at[2, 'model']}")
    xs_data = test_data.set_index(['brand', 'model', 'model_year'])
    print(f"test_data.xs('Porche'):\n{xs_data.xs('Porsche')}\n")
    print(f"test_data.at[2, 3]:\n{test_data.iat[2, 3]}")
    print(f"This dataframe contain NaNs:\n{test_data['clean_title'].hasnans}")
    print(f"This dataframe is empty:\n{test_data.empty}")
    print(f"The name of the series test_data['model'] is:\n{test_data['model'].name}")
    print(f"flags with this dataframe:\n{test_data.flags}")
    print(f"cast model column datatype to string using astype:\n{test_data.astype({'model': 'string[python]'}).dtypes}")
    print(f"Convert cleant_title column to categorical type:\n{test_data['clean_title'].astype('category')}")
    print(f"test_data.infer_objects().dtypes:\n{test_data.infer_objects().dtypes}")
    print(f"test_data.to_numpy():\n{test_data.to_numpy()}")
    print(f"pd.Series([1, 2, 3], index=pd.PeriodIndex(['2023', '2024', '2025'])):\n{pd.Series([1, 2, 3], index=pd.PeriodIndex(['2023', '2024', '2025'], freq='Y'))}")
    print(f"test_data.get(1, '[unknown]'):\n{test_data['model'].get(1, '[unknown]')}")
    
    num_data1 = pd.Series([0, 1, 2, 3])
    num_data2 = pd.Series([-1, 2, -3, 4])
    print(f"num_data1.dot(num_data2):\n{num_data1.dot(num_data2)}")
    print(f"num_data2@num_data1:\n{num_data2@num_data1}")
    print(f"num_data1.apply(lambda a: a**2):\n{num_data1.apply(lambda a: a**2)}")
    print(f"num_data2.agg('min'):{num_data2.agg('min')}")
    print(f"num_data1.agg(['min', 'max']):{num_data1.agg(['min', 'max'])}")
    print(f"num_data2.transform([np.exp, np.log]):\n{num_data2.transform([np.exp, np.log])}")
    print(f"Mapping model names from dataframe:\n{test_data['model'].map('Car delivered -> {}'.format)}")
    print(f"Number of car models group by brand:\n{test_data['model'].groupby(test_data['brand']).count()}")
    print(f"Rolling sum of car model prices with window length 4:\n{test_data['price($)'].rolling(4).max()}")

    print(f"Car price after reducing 5% gst, 2.5% road tax and 1% shipment tax:\n{pd.concat([test_data['model'], test_data['price($)'].pipe(lambda a: 1.05*a).pipe(lambda a: 1.025*a).pipe(lambda a: 1.001*a)], axis=1)}")

    print(f"Checking for any Yes in the clean_title:\n{(test_data['clean_title']=='Yes').any()}")
    print(f"List all the car models with price range from $500K to $5M:\n{test_data[test_data['price($)'].between(500000, 5000000)].get(['model', 'price($)'])}")
    print(f"Clip list of car models based on price range of $500k to $5M and model year 2010 to 2020:\n{test_data[['model_year', 'price($)']].clip([2010, 50000], [2020, 5000000])}")
    print(f"Correlation of columns both ways in the dataframe:\n{num_data1.corr(num_data2)}, {num_data2.corr(num_data1)}")
    print(f"count of non nan values in clean_title column:\n{test_data['clean_title'].count()}")

def dataframe_test()->None:
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

    join_in_dataset(df2, df3)
    print("############################################################################################")
    dataframe_filter() #independent function call
    print("############################################################################################")
    
if __name__=="__main__":
    dataframe_readData()