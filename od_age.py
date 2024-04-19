#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:51:15 2024

@author: sean
"""

import pandas as pd
import numpy as np

# Read csv

od_age = pd.read_csv('CA_Fentanyl-Related Overdose_Death_by Age Groups_2022_04.16.2024.csv')

# Set CA OD data columns to row 1

od_age.columns = od_age.iloc[1]

# Drop rows w/ missing data

od_age = od_age.replace(r'^\s$', np.nan, regex=True)
od_age = od_age.dropna()
od_age = od_age.drop(1)

# Write to csv

od_age.to_csv('od_age.csv')