from alpha_vantage.timeseries import TimeSeries
import pandas as pd

ts = TimeSeries(key='EVLE1IR0H06PISXC',output_format='pandas')

# returns historical stock price for ticker input as a csv
def stockPriceToCSV(ticker,outputFileName):
    data, meta_data = ts.get_daily(symbol=ticker,outputsize='full')
    data.to_csv(outputFileName)

# e.g
stockPriceToCSV("FB","fboutput.csv")
