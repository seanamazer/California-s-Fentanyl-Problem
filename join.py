#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  19 11:17:45 2024

@author: sean
"""

import pandas as pd
import geopandas as gpd

# Read pop by county data

fips = {'GEOID': str}
merged = pd.read_csv('merged.csv',dtype=fips)

# Set pop index to GEOID

merged = merged.set_index('GEOID')

# Add column for people of color and a column for percent of county

merged['poc'] = merged['pop'] - merged['white']
merged ['poc_percent'] = merged['poc']/merged['pop']

# Add column for pop in Millions

merged ['pop_mils'] = merged ['pop'] / 1000000

# Add column for count percent of CA

merged ['count_percent'] = (merged ['Counts'] / 
                            merged ['Counts'].sum())*100

# Read Census 2020 shape file

counties = gpd.read_file('cb_2022_us_county_5m.zip')
counties = counties.query("STATEFP=='06'")

# Extract the GEOID and geometry

keep_cols = ['GEOID', 'geometry']
counties = counties[keep_cols]

# Merge merged data onto counties, print value counts and then delete the col

counties = counties.merge(merged, on='GEOID', validate='1:1', indicator=True)
print(counties['_merge'].value_counts())
counties = counties.drop(columns='_merge') 

# Remove excess text beyond county name

counties['County'] = counties['County'].replace({'County, California': ''}, regex = True)

# Save the counties layer as gpkg

counties.to_file('counties.gpkg', layer='County')
counties.to_csv('counties.csv')
