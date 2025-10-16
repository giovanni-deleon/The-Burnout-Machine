# Method definition to compare student data

import matplotlib.pyplot as plt
import seaborn as sns # The line on the plot.

def compare_hours_worked(df, x_listname, y_listname, x_label, y_label): # Supposed to display scatter plot comparing student data
    x = df[x_listname].tolist()
    y = df[y_listname].tolist()

    sns.regplot(x=x, y=y, ci=None)

    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.show()
