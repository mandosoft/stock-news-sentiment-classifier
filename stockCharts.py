from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Description: stockCharts.py pulls historical stock data and includes functions for visualization

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
def plotDailyReturn(df, start_date, end_date, ticker):
    df["7. date"] = pd.to_datetime(df.index.values)
    mask = (df["7. date"] > start_date) & (df["7. date"] <= end_date)
    df = df.loc[mask]
    
    fig = plt.figure(1)

    # chart formatting
    plt.title(ticker + ': Historical Daily % Returns')
    plt.ylabel("Daily % Return")
    plt.xlabel("Date")
    plt.xticks(rotation=90)
    # set y-axis to %
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(5.0))
    
    plt.plot(df['7. date'],df['6. 1-day % change'])
    
    plt.show()
    

# output line plot of daily return % with start and end date inputs
def plotPrice(df, start_date, end_date, ticker):
    df["7. date"] = pd.to_datetime(df.index.values)
    mask = (df["7. date"] > start_date) & (df["7. date"] <= end_date)
    df = df.loc[mask]
    
    # chart formatting
    fig = plt.figure(2)
    plt.title(ticker + ': Historical Stock Prices')
    plt.ylabel("Price")
    plt.xlabel("Date")
    plt.xticks(rotation=90)
    
    plt.plot(df['7. date'], df['4. close'])

    plt.show()
    
# e.g
# stockPriceToCSV(getData("TSLA"),"tslaoutput.csv")
plotPrice(getData("AAPL"), "01-31-2019", "03-30-2019", "AAPL")
plotDailyReturn(getData("FB"), "01-31-2019", "03-30-2019", "FB")
