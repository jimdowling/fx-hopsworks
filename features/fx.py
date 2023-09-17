import pandas as pd

def load_fx(fx_rate: str, start_date : str, end_date: str) -> pd.Dataframe:
    forex_data = yf.download(fx_rate, start=start_date, end=end_date)
    forex_data['fx'] = fx_rate
    forex_data = forex_data.reset_index()
    forex_data.rename(columns = {'Adj Close':'adj_close'}, inplace = True)
    forex_data.rename(columns = {'Datetime':'Date'}, inplace = True)
    return forex_data