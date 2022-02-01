from datetime import datetime
from numpy import double
import streamlit as st
from pandas import DataFrame

import numpy as np

import pymongo

#data = pd.read_csv("data.csv")
myclient = pymongo.MongoClient("mongodb://localhost:27017/", username='root', password='example')
mydb = myclient['docstreaming']
mycol = mydb['invoices']

# the first chart add a input field for the invoice number
cust_id = st.sidebar.text_input("CustomerID:")
#st.text(cust_id) # to print out the content of the input field

# if enter has been used on the input field
if cust_id:

    myquery = {"CustomerID": cust_id}
    # only includes or excludes
    mydoc = mycol.find(myquery, {"_id": 0, "Stockcode": 0, "Description": 0, "Quantity": 0, "Country": 0, "UnitPrice": 0})

    # create dataframe from resulting documents
    df = DataFrame(mydoc)

    # drop duplicates
    df.drop_duplicates(subset="InvoiceNo", keep="first", inplace=True)

    # add the table with a headline
    st.header("Output Customer Invoices")
    table2 = st.dataframe(data=df)

# below the first chart which add an input field for the invoice number
inv_no = st.sidebar.text_input("InvoiceNo:")
#st.text(inv_no) # to print out the content of the input field

# if enter has been used on the input field
if inv_no:

    myquery = {"InvoiceNo": inv_no}
    mydoc = mycol.find(myquery, {"_id": 0, "InvoiceDate": 0, "Country": 0, "CustomerID": 0})

    # create dataframe
    df = DataFrame(mydoc)

    # reindex columns to be ordered in lexicographically
    reindexed = df.reindex(sorted(df.columns), axis=1)

    # add the table with a headline
    st.header("Output by Invoice ID")
    table2 = st.dataframe(datetime=reindexed)