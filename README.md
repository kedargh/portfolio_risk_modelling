# portfolio_risk_modelling

## Description
The "portfolio_risk_modelling" project is designed to assess and manage the risk associated with investment portfolios. It utilizes various financial models and statistical techniques to evaluate potential risks and returns, helping investors make informed decisions.

## Features
- Calculation of returns from historical data.
- Fetching and processing time series data for stocks.
- Calculation of portfolio weights and value.
- Construction of covariance matrices for risk assessment.
- Calculation of portfolio variance and standard deviation.

## Installation

### Prerequisites
- Python 3.x
- Required libraries: pandas, numpy, yfinance

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/kedargh/portfolio_risk_modelling.git
   ```

2. Navigate to the project directory:
   ```bash
   cd portfolio_risk_modelling
   ```

3. Install the dependencies:
   ```bash
   pip install pandas numpy yfinance
   ```

## Usage
1. Run the main script to perform risk assessment and portfolio optimization:
   ```bash
   python src/risk_modelling.py
   ```

2. The script will calculate and display the risk metrics for the portfolio defined in the CSV file.

## Project Structure
- `src/risk_modelling.py`: The main script for risk assessment and portfolio optimization.
- `README.md`: Project documentation (this file).

## Functions in `risk_modelling.py`
- `calculate_returns_csv(time_series_file)`: Calculates returns from a CSV file containing time series data.
- `calculate_last_price(stock)`: Fetches and prints the last price of a stock from a CSV file.
- `time_series_construction(portfolio_file)`: Constructs time series data for stocks in a portfolio file using Yahoo Finance.
- `calculate_weight(stock_name, portfolio_file)`: Calculates the weight of a stock in the portfolio.
- `weight_matrix_construction(weight_list)`: Constructs weight matrices.
- `calculate_portfolio_stats_master_function(portfolio_file)`: Master function to calculate portfolio statistics, including covariance matrix, variance, and standard deviation.

## Example CSV Structure
The CSV files should have the following structure:

### Portfolio File (`portfolio_1.csv`)
| Stockname | Quantity |
|-----------|----------|
| AAPL      | 50       |
| MSFT      | 30       |
| ...       | ...      |

### Time Series File (`AAPL.csv`)
| Date       | Value  |
|------------|--------|
| 2023-01-01 | 150.00 |
| 2023-01-02 | 152.30 |
| ...        | ...    |


## Contact
For any questions or inquiries, please contact me at [kedarkenjalkar@gmail.com].
