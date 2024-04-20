# California's Fentanyl Problem

California has experienced an unprecedented climb in overdose deaths over the past four years, primarily contributed to the opioid Fentanyl. This GitHub repository analyzes the State's data related to these deaths combined with data from the U.S. Census Bureau. Please visit the Tableau dashboard listed below to interact with the data. Below is an overview of my process to repeat this analysis for future data releases and all py scripts are embedded with comments. Furthermore, I provide my findings in the data with some reccomendations for the State to ensure support and enforcement mechanisms are focused proportionately in the appropriate counties.

<b> Tableau Dashboard: </b> 
https://public.tableau.com/app/profile/sean.mazer/viz/ca_fentanyl/CaliforniasFentanylProblem

<b> Sources:</b> 

California Department of Public Health (Overdose Data):
https://skylab.cdph.ca.gov/ODdash/?tab=Home

U.S. Census Bureau (Population Data API): 
https://api.census.gov/data/2020/acs/acs5

U.S. Census Bureau (County Cartographic Boundaries): 
https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html

<b> Overdose Definition:</b> 
Drug overdose deaths caused by acute poisonings that involve fentanyl or fentanyl analogs as a contributing cause of death, regardless of intent (e.g., unintentional, suicide, assault, or undetermined). Fentanyl and associated analogs are strong synthetic opioid analgesics that may be prescribed or obtained illegally. Deaths related to chronic use of drugs (e.g., damage to organs from long-term drug use), are excluded from this indicator.

<b> Acknowledgements:</b> 
This project was built for the Advanced Policy Analysis course (PAI 789) at Syrcause University, taught by Professor Peter Wilcoxen. Without his detailed lessons and deep care for his students, this project would not have been possible. 

# The Process
Below is a list of scripts, downloads and outpus utilized to conduct this analysis. 

<b> Scripts: </b> 
collect.py, county_merge.py, join.py, year.py, od_age.py

<b>Dowloands:</b> (These can be downloaded from California State's Department of Health (CDPH) and U.S. Census site listed above)

CA_Fentanyl-Related OverdoseDeath_TimeTrend_04.16.2024.csv

CA_Fentanyl-Related Overdose_Death_by Age Groups_2022_04.16.2024.csv

CA_Fentanyl-Related Overdose_Death_by County_2022_04.16.2024.csv

cb_2022_us_county_5m.zip

<b>Outputs: </b> (These csvs and shapefile were utilized to create the Tableau dashboard linked above)

pop_by_county.csv, merged.csv, counties.csv, od_year.csv, od_age.csv, counties.shp

<b>Steps:</b>
1. Collect the Census data with an API call by running the collect.py script, ensure you have a Census API key and replace it with mine. This call will produce a data frame (df) with County names in California with their respective population count and number of citizens that report themselves as "White".
2. I downloaded the California data files mentioned above by clicking on their dashboard at the website linked above,selecting the Display Options, checking deaths, fentanyl, total population, crude rate, annual, 2022. You then can cick download as .csv file for analysis.
3. The second script, county_merge.py, joins together the Census df and the county overdose data from the State of California.
4. Then I joined this merged data onto the Census' cartographic boundaries (5m) with join.py, this allowed for me to build the geometry for each county which will be utilized later in QGIS and Tableau to build the dashboard.
5. The next two scripts, year.py and od_age.py, were rather short to clean up the data to allow Tableau to read the csvs properly. This was for the last two csvs, by age and by year.
6. I then utilized QGIS to convert counties into a shape file, counties.shp.
7. I then uploaded all three products into Tableau to create the dashboard linked above. (counties.shp, od_year.csv and od_age.csv)

# Findings
California State's Department of Public Health does an incredible job of collecting overdose data with several types and units to filter by over several years. They utilize this data to create a dashboard which is what inspired me to take on this project, however this also where I struggled with which data they chose to display in their county map. They display their death counts (crude/age-adjusted) in the measurment of per 100K residents. This is standard in the public health and government sectors, however I feel it does a deservice when highlighting the concentration of overdoses by a raw count. They allow for us to download these counts in the data which provides, in my opinion, a much more meaningful figure for public health and government officials. From a public health support perspective for resources and a government perspective for enforcement. I also feel by highlighting counties based on the per 100K measure, it seems like the problem counties aren't the major metropolitan areas where a majority of residents live. Perhaps to calm the nerves of residents that this is a major problem? I reproduced their dashboard in my Tableau project, with additional figures to include population and the percent that are "non-white" in the county. However, once I analyzed the counties based on overdose counts, you see a much different picture to the right. It highlights the major metropolitan areas and the southern part of California being the area of concern. I believe this is critical for the public and policy makers to understand because it can influence decisions and where resources are invested. With more research, I am sure there is a positive correlation to how much fentanyl is smuggled/present in these counties with the number of overdose deaths. Of all overdose deaths in California, here are some of the top counties. Los Angeles (24%), San Diego (10.3%), Riverside (8%), San Bernardino (5.6%) and San Francisco (5%). It is also interesting to see what percent of these counties are "non-white", the trend seems to be fairly positive, those counties with a higher percent "non-white" tend to have on average, higher overdose counts. Reverting back to the first analysis by per 100K measure, we find that the highest counties by that mneasure have some of the lowest percent "non-white" communities.

The other two charts in the overview tab ended up being very similar to the State of California, however I added them to provide some contect and present an overview of the accelerating trend of overdoses related to Fentanyl. This data analysis can be done on a much deeper level with more time as the county level is downloadable by year to csv and by type such as sex, age, ethinicity. This would take an immense amount of time, files and merging but I encourage those who can to do so. This is a national crisis that calls for a stronger response. In 2022, California established the Fentanyl Enforcement Program to improve collaboration amongst local, state and federal agencies to crack down on the smuggling of this contraband. I imagine this is just the start of such programs and will probably take a greater response, in the meantime analysis of data sets like this will provide voice and insight to greater trends which can have an impact on policy. 
