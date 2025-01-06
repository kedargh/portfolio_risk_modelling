import pandas as pd
import random
import os
from datetime import datetime, timedelta
import shutil

# Define the number of stocks and records per stock
num_stocks = 10
num_records = 2800

# Define output directory for CSV files
output_dir = '/home/kedar/portfolio_analysis/data'
os.makedirs(output_dir, exist_ok=True)

# Generate random stock data
def generate_stock_data(stock_name, num_records):
    start_date = datetime.now() - timedelta(days=num_records)
    data = {
        "Date": [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(num_records)],
        "Value": [round(random.uniform(100, 500), 2) for _ in range(num_records)],
    }
    return pd.DataFrame(data)

# Generate CSV files for 10 NASDAQ stocks
for i in range(num_stocks):
    stock_name = f"NASDAQ_Stock_{i+1}"
    stock_data = generate_stock_data(stock_name, num_records)
    file_path = os.path.join(output_dir, f"{stock_name}.csv")
    stock_data.to_csv(file_path, index=False)

# Create a zip file containing all the generated CSV files
zip_file_path = 'NASDAQ_stocks.zip'
shutil.make_archive('NASDAQ_stocks', 'zip', output_dir)

print(f"CSV files generated and compressed into {zip_file_path}")
