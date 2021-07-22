#!/usr/bin/env python3
#
# File: ei_data.py
# About: Create test e-Invoices using fake data sets.  
# Development: Kelly Kinney
# Date: 2021-06-22 (June 22, 2021)
#
# LICENSE
# Copyright (C) 2021 Business Payments Coalition
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files 
# (the "Software"), to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, 
# publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH 
# THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
Classes and functions to generate sample/test e-Invoices.

Short for "e-Invoice Data Generator."
Test data is generated in two ways.
1. Loaded into TinyDB from CSV files.
2. Additonal dummy data is genearted on the fly by the Faker package.
Data generated by Faker is new every run. Data sets from the CSV files
are static.
Data items are combined into an e-Invoice line item and stored as a list.
The output of this sample list of line items is writen to a JSON file.

    Usage:
    genLI = generateLineItems()
    genLI.

"""
from faker import Faker
from csv import reader
from random import randint, choice
from logging import basicConfig, logging
from json import dumps


# Create a logger.
FORMAT='%(asctime)s - $(levelname)s - $(funcName)s - $(message)s'
DATEFMT='%m/%d/%Y %I:%M:%S %p'
logging.basicConfig(format=FORMAT, datefmt=DATEFMT, level=logging.INFO)




class InvoiceDataGen:

    def __init__(self):
        logging.info("Generating e-Invoice Data!")
"""An instance of the InvoiceDataGen object.  

The job of this class/object is to generate sample data for
an e-Invoice.

Args:

Attributes:
    Items[]: A list of lineItems to populate an e-Invoice.  Populated by
        reading in from a CSV file.
    PerItem[]: A list of item sizes/groups/types to populate an e-Invoice.  
        Populated by reading in from a CSV file.

Returns:

Raises:
"""


# Read the CSV files in

Items = []
with open('./items.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        Items.append(row)

PerItem = []
with open('./peritem.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        PerItem.append(row)


fake = Faker()
Faker.seed(0)

def generateFakeCo(_count=1):
    """Generate as many fake addresses as requested.

    Args:
        _count:
            The number of addresses reqested.

    Raises:

    Returns:
        A list of JSON entries with each one representing an
        address.
    """

    companies = []

    for _ in range (_count):
        orgID = fake.bothify(text='????-######',
            letters='ACDEFGHIJKLMNOPQRSQSTeUVWXYZ')
        name = fake.company()
        addr_1 = "Attn: " + fake.name()
        addr_2 = fake.street_address()
        city = fake.city()
        state = fake.state()
        zip = fake.postcode()

        # Create a JSON string of the Company.
        company = str({'orgID': orgID, "name": name, "addr_1":addr_1,
            "addr_2":addr_2, "city":city, "state":state, "zip":zip})

        companies.append(company)

        logging.debug("Created a data for comapny: " + company)

    return companies





def generateFakeLI(_count=1):
    """Generate as many fake lineItems as requested.
    
    Args:
        _count:
            The number of lineItems reqested.

    Raises:

    Returns:
        A list of JSON entries with each one representing a line item.
    """

    lineItems = []

    for _ in range (_count):
        LIID = fake.bothify(text='??????-###',
            letters='ACDEFGHIJKLMNOPQRSQSTeUVWXYZ')
        LIQty = random.randint(1,10)
        LIPerItem = random.choice(PerItem)
        LIPPI = (random.randint(100, 10000))/100
        LIName = random.choice(Items)
        LITotal = LIQty * LIPPI
        
        # Create a JSON string of the lineItem
        lineItem = str({'Item ID':LIID, 'Quantity':LIQty,
            'Per Item':LIPerItem, 'Price per Item':LIPPI, 'Item':LIName,
            'Total':LITotal})

        lineItems.append(lineItem)

        logging.debug("Created line item entry: " + lineItem)

    return lineItems


def writeJSONtoStr(_object):
    if len(_object) < 1:
        logging.warn("Do you WANT an index out of bounds " 
            "error, cuz you're just asking for one.")
        return
    
    for i in range(len(_object)):
        jsonStr = json.dumps(_object[i].__dict__)
        logging.debug("List item " + str(i) + ": " + jsonStr)
        print(jsonStr)

    