# fred_plot.py
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import sys

def get_fred_data(series):
    data = web.DataReader(series, "fred")
    data.to_csv(f"{series}.csv")
    data.plot(title=series)
    plt.savefig(f"{series}.png")
    print(f"{series} data saved and plotted!")

if __name__ == "__main__":
    # Read the series name from command line
    if len(sys.argv) > 1:
        series = sys.argv[1]  # first argument
    else:
        series = "GDP"  # default series
    get_fred_data(series)
