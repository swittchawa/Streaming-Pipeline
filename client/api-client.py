import linecache
import json

import requests

# set starting id and ending id
start = 1
end = 50

# Loop over the JSON file
i = start

while i <= 50:

    # Read a specific line
    line = linecache.getline('client/output.txt', i)
    print(line)

    # write the line to the API
    myjson = json.loads(line)

    i+=1