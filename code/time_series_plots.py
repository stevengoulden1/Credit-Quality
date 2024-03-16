import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_pacf
import matplotlib.dates as mdates

def plot_time_series(df, columns, title = 'Time Series Plot', acc=False, pacf=False, pacflags=12, covid_start=False):
    """
    Plots time series data, with options for decomposition and PACF plots, formatting the x-axis to show only years.

    Parameters:
    - df (pandas.DataFrame): The dataframe containing the time series data.
    - columns (list): List of column names in df to be plotted.
    - acc (bool, optional): If True, plots decomposition plots for each column. Defaults to False.
    - pacf (bool, optional): If True, plots PACF plot for each column. Defaults to 36 lags. Defaults to False.
    - pacflags (int, optional): Number of lags for the PACF plot. Defaults to 12.
    - covid_start (bool, optional): If True, adds a vertical line on Feb 1st to indicate the start of COVID-19. Defaults to False.


    Returns:
    - Plots of time series data, decomposition, and/or PACF based on input flags, with x-axis showing only years.
    """
    sns.set_style("darkgrid")

    # plot each column on the same time plot
    plt.figure(figsize=(11, 8))
    for column in columns:
        plt.plot(df.index, df[column], label=column)

    if covid_start:
        plt.axvline(pd.Timestamp('2020-02-01'), color='grey', linestyle='--', lw=1, label='COVID-19 Start')


    plt.gca().xaxis.set_major_locator(mdates.YearLocator())  # set major locator to every year.
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # set formatter to only display the year.
    plt.gcf().autofmt_xdate()  # auto-rotate lables

    plt.title(title)
    plt.legend()
    plt.show()

    # if acc is true, plot decomposition plots for each column
    if acc:
        for column in columns:
            result = seasonal_decompose(df[column], model='additive', period=1)
            result.plot()
            plt.gca().xaxis.set_major_locator(mdates.YearLocator())  # only display year
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
            plt.gcf().autofmt_xdate()  # auto-rotate
            plt.suptitle(f'Decomposition Plot for {column}', y=1.05)
            plt.tight_layout()
            plt.show()

    # if pacf is true, plot pacf for each column
    if pacf:
        for column in columns:
            plt.figure(figsize=(10, 6))
            plot_pacf(df[column], lags=pacflags)

            plt.title(f'PACF for {column}')
            plt.show()
