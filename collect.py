#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 07:27:44 2024

@author: sean
"""

import requests
import pandas as pd

# Establish variables for Census API call

variables = {'B02001_001E':'pop_total', 
             'B02001_002E':'pop_white',
             'NAME': 'county'}
var_list = variables.keys()
var_string =','.join(var_list)

# API call

api = "https://api.census.gov/data/2020/acs/acs5"

# Set clauses for API call

get_clause = var_string
for_clause = 'county:*'
in_clause = 'state:06'

# Set key_value to Census API key

key_value = '50eae7b523e5a7d7080722d89617a2d9b9ecfcdd'

# Set payload to dictionary with keys and values for the API call

payload = { 'get':get_clause, 'for':for_clause, 'in':in_clause, 'key':key_value }

# Set response to the API call

response = requests.get(api,payload)

# If block to determine status code if not equal to 200

if response.status_code != 200:
    print( '\n' )
    print( 'status:', response.status_code )
    print( response.text )
    assert False
    
# Parse the JSON returned by the Census in a list of rows
    
row_list = response.json()

# Convert the data into a DF

colnames = row_list[0]
datarows = row_list[1:]
pop = pd.DataFrame(columns=colnames, data=datarows)

# Create GEOID column

pop['GEOID'] = pop['state'] + pop['county']

# Set the index by zip, then sort the index

pop=pop.set_index('GEOID')
pop=pop.sort_index()

# Create dictionary to rename columns in pop

new_names = {'B02001_001E':'pop', 'B02001_002E':'white' }
pop = pop.rename(columns=new_names)

# Discard columns used to create the GEOID

pop = pop.drop(columns=['state', 'county'])

# Save pop to csv

pop.to_csv('pop_by_county.csv')

