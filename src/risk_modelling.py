import pandas as pd
import numpy as np
import os
portfolio_path="/home/kedar/NASDAQ_Quarterly_Returns.csv"
import yfinance as yf

def calculate_returns_csv(time_series_file):
    df = pd.read_csv(time_series_file)
    list_of_time_series = df["Value"].tolist()
    return_array=[]
    for i in range(500):
        return_array.append((list_of_time_series[i+1] - list_of_time_series[i])/list_of_time_series[i])
    #print(return_array)
    return return_array

def calculate_last_price(stock):
    df = pd.read_csv(f"/home/kedar/portfolio_analysis/data/{stock}.csv")
    list_of_prices = df["Value"].tolist()
    last_price = list_of_prices[-1]
    print(f"The last price of {stock}" , last_price)
    return last_price

def time_series_construction(portfolio_file):
    df = pd.read_csv(portfolio_file)
    stocks_for_fetching_data = df["Stockname"].tolist()
    for stock in stocks_for_fetching_data:
        data = yf.download(stock, period=f"2y")
        if data.empty:
            print(f"No data found for ticker {stock}.")
            return
        eod_data = data[["Close"]].reset_index()
        eod_data.columns = ["Date", "Value"]
        file_name = f"/home/kedar/portfolio_analysis/data/{stock}.csv"
        eod_data.to_csv(file_name , index=False)
        print(f"700 EOD for {stock} extracted and file created")

def calculate_weight(stock_name,portfolio_file):
    df = pd.read_csv(portfolio_file)
    list_of_stocks = df["Stockname"].tolist()
    # total_stocks = df["Quantity"].sum()
    quantity_of_stock = df.loc[df["Stockname"] == stock_name, "Quantity"].values[0]
    last_price_of_stock = calculate_last_price(stock_name)
    portfolio_value = 0

    for stock in list_of_stocks:
        last_price = calculate_last_price(stock)
        print("last price=", last_price)

        qty = df.loc[df["Stockname"] == stock, "Quantity"].values[0]
        print("Qty=", qty)

        portfolio_value += last_price*qty
        print("portfolio value", portfolio_value)

    weight = (quantity_of_stock*last_price_of_stock)/portfolio_value
    print(weight)
    return weight
        

def weight_matrix_construction(weight_list):
    matrix = np.array(weight_list)
    row_matrix = matrix[np.newaxis, :]
    transpose_matrix = row_matrix.T
    return row_matrix,transpose_matrix
    #return the weight matrix 1xN and weight matrix tra

def calculate_portfolio_stats_master_function(portfolio_file):
    df = pd.read_csv(portfolio_file)
    list_of_stocks = df["Stockname"].tolist()
    list_of_avg_returns = []
    weights_matrix = []

    #--------MODELLED AVERAGE RETURNS----------------------------------------------------------------------
    average_returns_dictionary = {}
    #------------------------------------------------------------------------------------------------------
    for stock in list_of_stocks:
        average_returns_dictionary[stock] = calculate_returns_csv(f"/home/kedar/portfolio_analysis/data/{stock}.csv")
        weights_matrix.append(calculate_weight(stock,portfolio_file))
    print("Weight matrix = " , weights_matrix)
    print("Average RETURNS DICT ______________________________________________________",average_returns_dictionary)
    cov_matrix_data = pd.DataFrame(average_returns_dictionary)
    #-------------------------------------RISK FUNCTION-----------------------------------------------------------------
    covariance_matrix = cov_matrix_data.cov()
    print("COVARIANCE MATRIX -------------" , covariance_matrix)
    covariance_matrix = covariance_matrix.values
    print(covariance_matrix)
    print("Covariance matrix shape is = ",covariance_matrix.shape)

    #row_matrix_weights,column_matrix_weights = weight_matrix_construction(weights_matrix)
    weights_matrix = np.array(weights_matrix).reshape(1, -1)
    weights_transpose_matrix = weights_matrix.T
    print(f"Weight matrix {weights_matrix}")
    # print(row_matrix_weights[0])
    #print("Row matrix shape is = ",weights_matrix.shape)
    # print(row_matrix_weights[0].T)
    #print("Column matrix shape is = ",weights_matrix.T.shape)

    output_matrix_of_variance = weights_matrix @ covariance_matrix @ weights_matrix.T
    print(output_matrix_of_variance[0])
    #-----------------------------------RISK FUNCTION-------------------------------------------------------------------

    modelled_variance = output_matrix_of_variance[0]
    print("The given portfolio has the risk variance percentage as",modelled_variance[0] * 100)
    print("The given portfolio has the risk standard dev of", (modelled_variance[0] * 100)**0.5)

    


        
        
if __name__ == "__main__":
    #time_series_construction("/home/kedar/portfolio_analysis/data/portfolios/portfolio_1.csv")
    calculate_portfolio_stats_master_function("/home/kedar/portfolio_analysis/data/portfolios/portfolio_1.csv")
