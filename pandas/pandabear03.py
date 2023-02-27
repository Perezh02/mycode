#!/usr/bin/python3

import pandas as pd

def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")
    
    # display first 5 entries of the ciscocsv dataframe
    print(ciscocsv.head())

    # display first 5 entries of the ciscojson dataframe            
    print(ciscojson.head())
    
    ciscodf = pd.concat([ciscocsv, ciscojson])
    # uncomment the line below to "fix" the index issue
    # ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)
    
    print(ciscodf)

    # create a dataframe ciscocsv
    ciscocsv = pd.read_csv("ciscodata.csv")
    # create a dataframe ciscojson
    ciscojson = pd.read_json("ciscodata2.json")

    # The line below concats and reapplies the index value
    ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)

    ## print to the screen the re-indexed dataframe
    print(ciscodf)

    ## print a blankline
    print()

    ## export to json
    ciscodf.to_json("combined_ciscodata.json")

    ## export to csv
    ciscodf.to_csv("combined_ciscodata.csv")

    ## export to Excel
    ciscodf.to_excel("combined_ciscodata.xls")

    ## create a python dictionary
    x = ciscodf.to_dict()
    print(x)

    
if __name__ == "__main__":
    main()

