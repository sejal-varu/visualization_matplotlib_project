import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    pddf = ipl_df.groupby("batting_team")['delivery'].count()
    pddf.plot(kind="bar")
    plt.show()
