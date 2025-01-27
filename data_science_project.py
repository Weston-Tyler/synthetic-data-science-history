import numpy as np

def calculate_mean(data):
    return np.mean(data)

if __name__ == "__main__":
    sample_data = [1, 2, 3, 4, 5]
    mean_value = calculate_mean(sample_data)
    print(f"The mean of the sample data is: {mean_value}")
