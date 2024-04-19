#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:29:44 2024

@author: sean
"""

import pandas as pd
import numpy as np

# Read csv

od_year = pd.read_csv('CA_Fentanyl-Related OverdoseDeath_TimeTrend_04.16.2024.csv')

# Set CA OD data columns to row 1

od_year.columns = od_year.iloc[1]

# Drop rows w/ missing data

od_year = od_year.replace(r'^\s$', np.nan, regex=True)
od_year = od_year.dropna()
od_year = od_year.drop(1)

# Write to csv

od_year.to_csv('od_year.csv')
