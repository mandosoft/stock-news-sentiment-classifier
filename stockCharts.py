from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style

# Description: stockCharts.py pulls historical stock data and includes functions for visualization

style.use('dark_background')

ts = TimeSeries(key='EVLE1IR0H06PISXC',output_format='pandas')

# return dataframe from ticker input. adds column that calculates 1-day % change
def getData(ticker):
    # pulls date, open, high, low, volume and closing prices
    df, meta_data = ts.get_daily(symbol=ticker,outputsize='full')
    
    # change/duplicate this for more calcs
    df["6. 1-day % change"] = (df['4. close'] / df['1. open']) - 1 
    
    return df

# output dataFrame as a csv
def stockPriceToCSV(df,outputFileName):
    df.to_csv(outputFileName)

# output line plot of daily return % with start and end date inputs
def plotDailyReturn(df, start_date, end_date):
    df["7. date"] = pd.to_datetime(df.index.values)
    mask = (df["7. date"] > start_date) & (df["7. date"] <= end_date)
    df = df.loc[mask]

    # modify x or y with other df column names
    df.plot(x='7. date',y='6. 1-day % change')

    
# e.g
# stockPriceToCSV(getData("TSLA"),"tslaoutput.csv")
# plotDailyReturn(getData("FB"), "01-31-2013", "05-05-2014")