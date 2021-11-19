import pandas as pd
import numpy as np

def unprocessed(data): ## load unprocessed dataset 
    df = pd.read_csv("../images/data/raw/projectdataset.csv")
    return df

# Method Chain 1 (Load data and skip rows and columns as needed including Deal with “incorrect” and missing data)
def load_and_process(data):
    df = pd.read_csv("../images/data/raw/projectdataset.csv")
    df1= (df.dropna(subset=["VALUE"])
    .drop(columns=['VECTOR','COORDINATE','DGUID','STATUS','UOM','UOM_ID','SYMBOL','TERMINATED','DECIMALS','SCALAR_FACTOR','SCALAR_ID'])
         )

## Method chain 2 (drop rows of Canadian provinical data as they are not part of the analysis but were included in data. Double check for rows that may contain undesired value(the zeros). Reset the index for our analysis to wrangle data)
    df2 = (
          df1 
    .loc[df['Air passenger traffic'] == 'Total, passenger sector']
    .loc[df['GEO'] != 'Canada']
    .loc[df['GEO'] != 'Ontario']
    .loc[df['GEO'] != 'Nunavut']
    .loc[df['GEO'] != 'British Columbia']
    .loc[df['GEO'] != 'Alberta']
    .loc[df['GEO'] != 'Yukon']
    .loc[df['GEO'] != 'Quebec']
    .loc[df['GEO'] != 'Nova Scotia']
    .loc[df['GEO'] != 'New Brunswick']
    .loc[df['GEO'] != 'Manitoba']
    .loc[df['GEO'] != 'Saskatchewan']
    .loc[df['GEO'] != 'Newfoundland and Labrador']
    .loc[df['GEO'] != 'Prince Edward Island']
    .loc[df['GEO'] != 'Northwest Territories']
    .loc[df['VALUE'] != 0]
    .reset_index(drop=True)
               )
    return df2