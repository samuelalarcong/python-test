import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Step 1: Import data from FRED
gdp = web.DataReader("GDP", "fred")

# Step 2: Save data to CSV
gdp.to_csv("gdp.csv")
print("GDP data saved to gdp.csv")

# Step 3: Make a plot
plt.figure(figsize=(8,5))
gdp.plot(title="US GDP")
plt.savefig("gdp_plot.png")
print("Plot saved to gdp_plot.png")
