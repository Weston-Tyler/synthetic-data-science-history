import pandas as pd

def process_data(file_path):
    data = pd.read_csv(file_path)
    total = data['value'].sum()
    return total

if __name__ == "__main__":
    file_path = 'sample_data.csv'
    total_value = process_data(file_path)
    print(f"The total value of the 'value' column is: {total_value}")
