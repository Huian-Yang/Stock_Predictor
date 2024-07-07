# Stock Prediction App

This Stock Prediction App is a web-based application built using Streamlit that allows users to predict future stock prices using historical data and the Prophet forecasting model.

[Deployed Website](https://huian-yang-stock-predictor-main-dntgnw.streamlit.app/)

## Before Anything

Please do all of the cloning and running of the code inside a virtual environment.

### Setting up a Virtual Environment

1. **Create a Virtual Environment**:
   
    ```bash
    python -m venv venv
    ```

2. **Activate the Virtual Environment**:

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

## Features

- **Stock Ticker Selection**: Choose from a wide range of stock tickers to analyze.
- **Customizable Prediction Period**: Select the number of years for which you want to predict stock prices.
- **Data Visualization**: Visualize the raw stock data and the forecasted prices.
- **Forecast Components**: Examine different components of the forecast to understand the trends, seasonality, and other factors affecting stock prices.


## Installation

1. **Clone the Repository**:

    ```bash
    git clone <repository-url>
    cd stock-prediction-app
    ```

2. **Install Dependencies**:

    Ensure you have Python installed. Then, install the required packages using pip:

    ```bash
    pip install streamlit yfinance prophet plotly
    ```

    note: Inside the virtual enviroment, locate the prophet libaray and go into the forecaster.py file and update np.float_ to np.float64 for it to work. 

3. **Run the Application**:

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Open the Application**:
    Once you run the app using Streamlit, it will open in your default web browser.

2. **Select a Stock Ticker**:
    Use the dropdown menu to select a stock ticker from the available list.

3. **Choose Prediction Period**:
    Use the slider to select the number of years for which you want to predict the stock prices.

4. **View Raw Data**:
    The application displays the most recent raw data for the selected stock.

5. **Visualize Data**:
    The app provides visualizations for the historical stock prices (open and close prices) and the forecasted prices.

6. **Forecast Components**:
    View the components of the forecast to understand the underlying patterns in the data.

## File Structure

- `app.py`: The main application file containing the Streamlit app code.
- `requirements.txt`: A list of Python packages required to run the app.

## Final Notes
   Following these steps will allow you to run this locally but if you want to deploy it, it will take extra work. 
