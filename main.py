import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

# Constants
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# App title
st.title("Stock Prediction App")

# Dropdown for selecting stock ticker
stocks = ('AAPL', 'MSFT', 'AMZN', 'GOOGL', 'FB', 'TSLA', 'BRK.B', 'NVDA', 'JPM', 'JNJ', 
    'V', 'PG', 'UNH', 'HD', 'DIS', 'MA', 'PYPL', 'BAC', 'VZ', 'CMCSA', 'ADBE', 'NFLX', 
    'PFE', 'INTC', 'KO', 'MRK', 'PEP', 'T', 'ABT', 'CSCO', 'XOM', 'NKE', 'CVX', 'WMT', 
    'LLY', 'ABBV', 'MCD', 'DHR', 'TMO', 'NEE', 'PM', 'COST', 'MDT', 'BMY', 'HON', 
    'UNP', 'AVGO', 'TXN', 'CRM', 'QCOM', 'LOW', 'ACN', 'LIN', 'UPS', 'SCHW', 'RTX', 
    'MS', 'INTU', 'SBUX', 'IBM', 'AMD', 'MMM', 'GE', 'ISRG', 'AXP', 'NOW', 'GS', 
    'AMGN', 'AMT', 'MU', 'BKNG', 'TGT', 'AMAT', 'BLK', 'C', 'CAT', 'DE', 'LMT', 
    'SPGI', 'PLD', 'MO', 'CHTR', 'SYK', 'CI', 'MDLZ', 'FIS', 'ZTS', 'EL', 'ADP', 
    'CVS', 'ADSK', 'CME', 'TJX', 'DUK', 'APD', 'BDX', 'ADI', 'ITW', 'EW', 'MMC', 
    'REGN', 'ECL', 'PGR', 'NSC', 'ILMN', 'PRU', 'D', 'GILD', 'MNST', 'FDX', 'NOC', 
    'AON', 'SO', 'TFC', 'MCO', 'EXC', 'CL', 'BSX', 'HUM', 'KHC', 'AEP', 'CNC', 
    'MET', 'FISV', 'WM', 'HCA', 'DOW', 'SRE', 'BAX', 'PSA', 'F', 'HAL', 'STZ', 
    'VLO', 'WELL', 'KMB', 'VTRS', 'PXD', 'BKR', 'EOG', 'DLR', 'SYY', 'TRV', 'HSY', 
    'AIG', 'ORCL', 'SLB', 'MAR', 'PPL', 'ADM', 'LVS', 'CB', 'VRSK', 'XEL', 'ANET', 
    'CTSH', 'MLM', 'ROST', 'CARR', 'IDXX', 'MPC', 'GPN', 'CINF', 'NUE', 'ROK', 
    'K', 'DHI', 'LEN', 'AEE', 'EFX', 'TT', 'APTV', 'YUM', 'ODFL', 'CAG', 'HIG', 
    'FITB', 'PAYX', 'FE', 'ETR', 'PCAR', 'MCK', 'WMB', 'PEG', 'CMG', 'CNP', 'OKE', 
    'DTE', 'DOV', 'IFF', 'TSN', 'AWK', 'AFL', 'WEC', 'SJM', 'MTB', 'AES', 'LUV', 
    'SNA', 'ULTA', 'RJF', 'ETSY', 'WDC', 'MOS', 'GRMN', 'FMC', 'UAL', 'TXT', 'XRAY', 
    'AES', 'LW', 'A', 'ALK', 'LNT', 'UAL', 'NTAP', 'ATO', 'RF', 'BXP', 'EQR', 'HBI', 
    'STT', 'HPE', 'ZBH', 'IVZ', 'KSS', 'HBAN', 'NLOK', 'RL', 'WYNN', 'ALLE', 'NVR', 
    'PVH', 'JBHT', 'ROL', 'HAS', 'AAP', 'CZR', 'WRK', 'UHS', 'DVA', 'VMC', 'WBA', 
    'VFC', 'J', 'WY', 'WAT', 'L', 'TPR', 'TTWO', 'HOLX', 'MAS', 'ATO', 'IPG', 'MRO', 
    'KEYS', 'GEHC', 'IRM', 'KMX', 'WHR', 'CMS', 'SIVB', 'HWM', 'CF', 'HSIC', 'MPWR', 
    'IP', 'TXT', 'MGM', 'PNW', 'MTD', 'EXR', 'CAH', 'PWR', 'GLW', 'AKAM', 'NDAQ', 
    'LKQ', 'RCL', 'URI', 'ALB', 'FTV', 'NWL', 'VTR', 'VRSN', 'ES', 'LKQ', 'HBAN', 
    'LNC', 'RHI', 'ZBRA', 'QRVO', 'POOL', 'IEX', 'RE', 'LYV', 'DISH', 'DXC', 'MLM', 
    'FLT', 'ARE', 'WDC', 'UHS', 'VMC', 'FRT', 'COO', 'TFX', 'AVY', 'DRI', 'CMA', 
    'ALLE', 'KEY', 'CDAY', 'BR', 'CMS', 'EXPE', 'DRE', 'ZION', 'LUMN', 'IPGP', 
    'XRAY', 'HST', 'DISCA', 'WRK', 'NDSN', 'LEG', 'XYL', 'MTD', 'ROL', 'RHI', 
    'FRT', 'PKG', 'SEE', 'AOS', 'NRG', 'HAS', 'CTXS', 'NDSN', 'PPG', 'PKI', 'IPGP', 
    'AVY', 'MSI', 'SBNY', 'TDY', 'LYB', 'CTVA', 'HII', 'BWA', 'BEN', 'NWSA', 
    'AAL', 'NWS', 'REG', 'FLS', 'CE', 'FMC', 'CDW', 'MOS', 'MLM', 'APA', 'DOV', 
    'EVRG', 'APA', 'CBOE', 'SLG', 'MHK', 'UAL', 'WAB', 'CHD', 'IEX', 'HRB', 'KMX', 
    'NRG', 'BKR', 'AIZ', 'APA', 'PNC', 'NDSN', 'DRI', 'AEE', 'OKE', 'JBHT', 'SBAC', 
    'EXR', 'AJG', 'PFG', 'CNP', 'RMD', 'ALLE', 'ETSY', 'SWKS', 'BAX', 'GRMN', 
    'POOL', 'CDAY', 'GNRC', 'NVR', 'HII', 'BXP', 'TFX', 'EQR', 'FFIV', 'AAP', 'ALLE', 
    'VLO', 'EXR', 'TYL', 'MPWR', 'RHI', 'FDS', 'MKTX', 'CDAY', 'MCO', 'NTRS', 
    'ABMD', 'VRSN', 'EMN', 'KIM', 'ZBRA', 'BAX', 'TYL', 'BKR', 'ALB', 'CINF', 'TDY', 
    'TPR', 'SEE', 'LNT', 'SIVB', 'EXPE', 'ATO', 'SNA', 'FLS', 'PKG', 'PNR', 'TAP', 
    'CHRW', 'FAST', 'CBOE', 'XYL', 'BEN', 'RCL', 'PNR', 'PH', 'OKE', 'JNPR', 'XYL', 
    'MAS', 'NVR', 'TSCO', 'SIVB', 'CAH', 'MHK', 'NLSN', 'DISH', 'ARE', 'SBAC', 
    'FLS', 'OKE', 'CMS', 'GNRC', 'FDS', 'SWKS', 'MKTX', 'TDY', 'GPC', 'ABMD', 'HRL', 
    'UAL', 'NVR', 'MKTX', 'PH', 'AAL', 'SBNY', 'FMC', 'EXPE', 'AJG', 'NVR', 'LYV', 
    'XYL', 'EMN', 'TRIP', 'HRL', 'ZION', 'LYB', 'UAL', 'KMX', 'WRK', 'NRG', 'SIVB', 
    'CF', 'APA', 'CMS', 'XYL', 'PKG', 'RCL', 'LNT', 'SEE', 'NRG', 'FFIV', 'CDAY', 'PLTR',
    'VOO', 'SCHG', 'LUNR', "RKLB")

selected_stock = st.selectbox("Select dataset for prediction", stocks)

# Slider for selecting number of years for prediction
n_years = st.slider("Years of prediction:", 1, 4)
period = n_years * 365

# Function to load stock data
@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

# Load data
data_load_state = st.text("Loading data...")
data = load_data(selected_stock)
data_load_state.text("Loading data...done!")

# Display raw data
st.subheader('Raw data')
st.write(data.tail())

# Function to plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

# Plot raw data
plot_raw_data()

# Prepare data for forecasting
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# Train the model
m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Display forecast data
st.subheader('Forecast data')
st.write(forecast.tail())

# Plot forecast data
st.write('Forecast data')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

# Plot forecast components
st.write('Forecast components')
fig2 = m.plot_components(forecast)
st.write(fig2)