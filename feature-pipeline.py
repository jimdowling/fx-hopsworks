import yfinance as yf
import pandas as pd
import hopsworks
import modal

name="fx_daily"
stub = modal.Stub(name)
image = modal.Image.debian_slim().pip_install(["hopsworks", "yfinance"])


@stub.function(image=image, schedule=modal.Period(days=1), secret=modal.Secret.from_name("jim-hopsworks-gcp"))
def update_fx():
    forex_data_minute = yf.download('EURUSD=X', period='1d', interval='1m')
    forex_data_minute.rename(columns = {'Adj Close':'adj_close'}, inplace = True)
    forex_data_minute = forex_data_minute.reset_index()
    forex_data_minute.rename(columns = {'Datetime':'Date'}, inplace = True)
    forex_data_minute['fx'] = "EURUSD=X"
    proj = hopsworks.login()
    fs = proj.get_feature_store()
    fg = fs.get_or_create_feature_group(name="eurusd", version=1)
    fg.insert(forex_data_minute, write_options={"wait_for_job": False})

if __name__ == "__main__":
    stub.deploy(name)
    with stub.run():
        update_fx()