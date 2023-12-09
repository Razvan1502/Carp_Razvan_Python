import pandas as pd
import matplotlib.pyplot as plt

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        middle1 = sorted_data[n // 2 - 1]
        middle2 = sorted_data[n // 2]
        return (middle1 + middle2) / 2
    else:
        return sorted_data[n // 2]

def calculate_standard_deviation(data):
    mean_value = calculate_mean(data)
    squared_diff = [(x - mean_value) ** 2 for x in data]
    variance = sum(squared_diff) / len(data)
    return variance ** 0.5

def calculate_min_max(data):
    min_value = data[0]
    max_value = data[0]

    for value in data[1:]:
        if value < min_value:
            min_value = value

        if value > max_value:
            max_value = value

    return min_value, max_value

def calculate_quartiles(data):
    sorted_data = sorted(data)

    q1_index = int(len(sorted_data) * 0.25)
    q3_index = int(len(sorted_data) * 0.75)

    q1 = (sorted_data[q1_index] + sorted_data[q1_index - 1]) / 2
    q2 = calculate_median(sorted_data)
    q3 = (sorted_data[q3_index] + sorted_data[q3_index - 1]) / 2

    return q1, q2, q3

def calculate_covariance(data1, data2):
    mean_data1 = calculate_mean(data1)
    mean_data2 = calculate_mean(data2)
    covariance = sum((x - mean_data1) * (y - mean_data2) for x, y in zip(data1, data2)) / len(data1)
    return covariance

def calculate_correlation(data1, data2):
    covariance = calculate_covariance(data1, data2)
    std_dev_data1 = calculate_standard_deviation(data1)
    std_dev_data2 = calculate_standard_deviation(data2)
    correlation = covariance / (std_dev_data1 * std_dev_data2)
    return correlation

def main():
    data1 = [1, 2, 3, 4, 5,]
    data2 = [2, 3, 4, 5, 6]

    print("Mean: ", calculate_mean(data1))
    print("Median: ", calculate_median(data1))
    print("Standard deviation: ", calculate_standard_deviation(data1))
    print("Min and max: ", calculate_min_max(data1))
    print("Quartiles: ", calculate_quartiles(data1))
    print("Covariance: ", calculate_covariance(data1, data2))
    print("Correlation: ", calculate_correlation(data1, data2))


if __name__ == "__main__":
    main()