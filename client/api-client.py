import linecache
import json
from urllib import response

import requests

# set starting id and ending id
start = 1
end = 50

# Loop over the JSON file
i = start

while i <= 50:

    # Read a specific line
    line = linecache.getline('client/output.txt', i)
    # print(line)

    # write the line to the API
    myjson = json.loads(line)

    print(myjson)

    response = requests.post("http://localhost:80/invoiceitem", json=myjson)

    # debugging
    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.json())

    # increase i
    i+=1