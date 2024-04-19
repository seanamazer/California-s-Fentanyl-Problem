#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 08:15:36 2024

@author: sean
"""

import pandas as pd

# Read csvs

fips = {'GEOID': str}
od_data = pd.read_csv('CA_Fentanyl-Related Overdose_Death_by County_2022_04.16.2024.csv')
pop_data = pd.read_csv('pop_by_county.csv',dtype=fips)

# Set CA OD data columns to row 1

od_data.columns = od_data.iloc[1]

# Add string County, California to od data for join

od_data ['County'] = od_data['County'] + ' ' + 'County, California' 

# Left join od_data onto pop_data, utilizing county name

merged = pop_data.merge(od_data,left_on=['NAME'], right_on=['County'], how='left')

# Truncate data

keep_cols = ['GEOID', 'pop', 'white', 'County', 'Rate', 'Counts']
merged = merged[keep_cols]

# Set index to GEOID, write to csv

merged = merged.set_index(['GEOID'])
merged.to_csv('merged.csv')
