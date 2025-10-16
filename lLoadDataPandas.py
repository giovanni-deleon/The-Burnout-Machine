# Method definition to load student data via Pandas

import pandas as pd

def load_data_pandas(): # Creates Pandas DataFrame
    df = pd.read_csv("simulated_Student_burnOut_One.txt")
    print(df.head(), ",")
    return df
