import matplotlib.pyplot as plt
import DataBase
import numpy as np

def plotGraph():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    dbBaseObject = DataBase.DataBase()
    list_lux, list_time = dbBaseObject.getData()
    ax.plot(list_time, list_lux)  # Plot some data on the axes.
    ax.set_ylabel("ILLumination - LUX")
    ax.set_xlabel("Time(sec) ")
    fig.show()