# Stock Prediction App

This Stock Prediction App is a web-based application built using Streamlit that allows users to predict future stock prices using historical data and the Prophet forecasting model.

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
    pip install -r requirements.txt
    ```

    The `requirements.txt` should include:

    ```plaintext
    streamlit
    yfinance
    prophet
    plotly
    ```

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

## Contributing

1. **Fork the Repository**:
    Click the "Fork" button at the top-right corner of the repository page.

2. **Clone Your Fork**:
    ```bash
    git clone <your-forked-repository-url>
    cd stock-prediction-app
    ```

3. **Create a Branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```

4. **Make Changes**:
    Implement your feature or bug fix.

5. **Commit and Push**:
    ```bash
    git add .
    git commit -m "Description of your changes"
    git push origin feature/your-feature-name
    ```

6. **Create a Pull Request**:
    Open a pull request to the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Streamlit for providing an easy-to-use framework for building web apps with Python.
- Yahoo Finance for providing the stock market data.
- Prophet for the powerful forecasting model.
