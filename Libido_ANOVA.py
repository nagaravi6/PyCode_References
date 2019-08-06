import numpy as np
import pandas as pd
import scipy as sc
import seaborn as sns
from scipy import stats
import math
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import researchpy as rp
import statsmodels.api as sm

# Reading .csv file placed under project folder
df = pd.read_csv("Libido.csv")

# as column person is not useful for analysis drop column 'person'
df.drop('person', axis= 1, inplace= True)

# Map drug effect values under dose column as placebo , low , high
df['dose'].replace({1: 'placebo', 2: 'low', 3: 'high'}, inplace= True)

# to check column libido column statistics.
print(rp.summary_cont(df['libido']))
