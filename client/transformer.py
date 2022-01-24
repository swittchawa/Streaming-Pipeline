import numpy as np
from numpy import add
import pandas as pd

# Read CSV
df = pd.read_csv('client/small_dataset.csv')
#print(df)

# Add a json column to the dataframe
# splitlines will split the JSON into multiple rows not a single one
df['json'] = df.to_json(orient='records', lines=True).splitlines()
#print(df)

# Only take JSON column of the data frame
dfjson = df['json']
print(dfjson)

# Print out the dataframe to a file
# Timestamp forward slash will be escapted to stay true to JSON schema
np.savetxt(r'client/output.txt', dfjson.values, fmt='%s')