import yfinance as yf
import matplotlib.pyplot as plt


nifty50 = 'DIVISLAB.NS HDFCBANK.NS DRREDDY.NS SUNPHARMA.NS BRITANNIA.NS NESTLEIND.NS KOTAKBANK.NS ASIANPAINT.NS APOLLOHOSP.NS ADANIPORTS.NS BPCL.NS CIPLA.NS TITAN.NS HINDUNILVR.NS BAJFINANCE.NS BAJAJFINSV.NS NTPC.NS BHARTIARTL.NS AXISBANK.NS HDFCLIFE.NS POWERGRID.NS ITC.NS INDUSINDBK.NS ICICIBANK.NS SBILIFE.NS BAJAJ-AUTO.NS RELIANCE.NS TATACONSUM.NS HEROMOTOCO.NS SBIN.NS ADANIENT.NS INFY.NS HCLTECH.NS ULTRACEMCO.NS GRASIM.NS TECHM.NS TCS.NS M&M.NS TATASTEEL.NS COALINDIA.NS LT.NS ONGC.NS LTIM.NS WIPRO.NS HINDALCO.NS JSWSTEEL.NS MARUTI.NS TATAMOTORS.NS'

nifty_50_tickers = nifty50.split()  #[kotak.ns , hdfc.ns ...]

tickers = yf.Tickers(nifty50)

stockDict ={}

for ticker in nifty_50_tickers:
    data= yf.download(ticker,period="1y") #fetch 1 year fo history

    if not data.empty: # ensure data is available
        highest_price = data['High'].max()
        closing_price = data['Close'].iloc[-1] # Get the most recent closing price
        fall_from_high_pct = ((highest_price - closing_price) / highest_price) * 100
        
        stockDict[ticker] = {'52weekHigh' : highest_price , 'Last_Closing_price':closing_price , 'fall_from_high_%': round(fall_from_high_pct,2)}

#sort StokDict by 'fall_from_high_%' in decreasing order
sorted_stockDict=dict(sorted(stockDict.items(),key=lambda item:item[1]['fall_from_high_%'],reverse=True))  

#preparing the data for plotting
# Prepare data for plotting
tickers = list(sorted_stockDict.keys())



falls = [sorted_stockDict[ticker]['fall_from_high_%'] for ticker in tickers]
for i in range(len(tickers)):
     tickers[i]=tickers[i][:-3]

# Plotting
plt.figure(figsize=(15, 8))
plt.bar(tickers, falls, color='skyblue')
plt.xlabel('Ticker')
plt.ylabel('Fall from High (%)')
plt.title('Percentage Fall from 52-week High for Nifty 50 Stocks')
plt.xticks(rotation=90)  # Rotate ticker names for better readability
plt.ylim(0, 100)  # Set y-axis range from 0 to 100%
plt.tight_layout()  # Adjust layout to fit labels

# Show plot
plt.show()

