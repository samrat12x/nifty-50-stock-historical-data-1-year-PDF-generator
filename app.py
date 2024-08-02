import yfinance as yf
from pdfGenerator import data_2_pdf
from tqdm import tqdm

nifty50 = 'DIVISLAB.NS HDFCBANK.NS DRREDDY.NS SUNPHARMA.NS BRITANNIA.NS NESTLEIND.NS KOTAKBANK.NS ASIANPAINT.NS APOLLOHOSP.NS ADANIPORTS.NS BPCL.NS CIPLA.NS TITAN.NS HINDUNILVR.NS BAJFINANCE.NS BAJAJFINSV.NS NTPC.NS BHARTIARTL.NS AXISBANK.NS HDFCLIFE.NS POWERGRID.NS ITC.NS INDUSINDBK.NS ICICIBANK.NS SBILIFE.NS BAJAJ-AUTO.NS RELIANCE.NS TATACONSUM.NS HEROMOTOCO.NS SBIN.NS ADANIENT.NS INFY.NS HCLTECH.NS ULTRACEMCO.NS GRASIM.NS TECHM.NS TCS.NS M&M.NS TATASTEEL.NS COALINDIA.NS LT.NS ONGC.NS LTIM.NS WIPRO.NS HINDALCO.NS JSWSTEEL.NS MARUTI.NS TATAMOTORS.NS'
nifty_50_tickers = nifty50.split()

tickers = yf.Tickers(nifty50)

all_data = {}

# Initialize the progress bar
with tqdm(total=len(nifty_50_tickers), desc="Processing Stocks", unit="stock") as pbar:
    for ticker in nifty_50_tickers:
        # Get historical data for 1 year
        historical_data = tickers.tickers[ticker].history(period="1y")
        # Store the historical data in the dictionary
        all_data[ticker] = historical_data
        # Update the progress bar
        pbar.update(1)

# Save all historical data to a single PDF
data_2_pdf(all_data)
print("Historical data for all stocks saved to nifty50_dataframe.pdf.")
