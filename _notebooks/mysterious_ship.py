import pandas as pd
import numpy as np

def data(t_max=1000, dt=1):
    """Load data from mysterious ship

    Args:
        n (int, optional): [description]. Defaults to 1000.
    """

    t = np.arange(0,t_max, dt)
    df = pd.DataFrame()

    rev = 10
    

