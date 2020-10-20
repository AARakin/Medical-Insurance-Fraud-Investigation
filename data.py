# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.backends.qt_editor.formsubplottool

#%matplotlib inline 

import matplotlib.pyplot as plt
import sidetable
matplotlib.rcParams['font.size'] = 18

sns.set_context('talk', font_scale=1.2);

df = pd.read_csv('PovidersUnique.csv')
df.head()

605670/132

df.dtypes

df.columns

df.stb.freq(['Fraud'])[:5]

amt= pd.pivot_table(df, index = 'Fraud',  values = 'AmtReimbursed', aggfunc = 'sum')
amt.plot(kind='bar', figsize=(10,5))
amt.style.format({'In':'${0:,.0f}','Out':'${0:,.0f}'})