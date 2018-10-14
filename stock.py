from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='H497805MA4UF89U1')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
