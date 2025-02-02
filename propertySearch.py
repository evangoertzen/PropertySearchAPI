from homeharvest import scrape_property
from sampleHousingData import DATA
import random
import numpy as np
import calculator as calc
import pandas as pd

# allFields = ['property_url', 'property_id', 'listing_id', 'mls', 'mls_id', 'status', 'text', 
#              'style', 'full_street_line', 'street', 'unit', 'city', 'state', 'zip_code', 'beds',
#              'full_baths', 'half_baths', 'sqft', 'year_built', 'days_on_mls', 'list_price',
#              'list_price_min', 'list_price_max', 'list_date', 'sold_price', 'last_sold_date',
#              'assessed_value', 'estimated_value', 'tax', 'tax_history', 'new_construction',
#              'lot_sqft', 'price_per_sqft', 'latitude', 'longitude', 'neighborhoods',
#              'county', 'fips_code', 'stories', 'hoa_fee', 'parking_garage', 'agent_id',
#              'agent_name', 'agent_email', 'agent_phones', 'agent_mls_set',
#              'agent_nrds_id', 'broker_id', 'broker_name', 'builder_id', 'builder_name',
#              'office_id', 'office_mls_set', 'office_name', 'office_email', 'office_phones', 
#              'nearby_schools', 'primary_photo', 'alt_photos']

importantFields = ['property_url', 'property_id', 'listing_id', 'mls', 'mls_id', 'status', 'text', 
             'style', 'full_street_line', 'street', 'unit', 'city', 'state', 'zip_code', 'beds',
             'full_baths', 'half_baths', 'sqft', 'year_built', 'days_on_mls', 'list_price',
             'list_date', 'assessed_value', 'estimated_value', 'tax', 'tax_history', 'lot_sqft',
             'price_per_sqft', 'latitude', 'longitude', 'county', 'hoa_fee', 'nearby_schools',
             'primary_photo']

def propSearch(location: str, limit: int, minPrice: int, maxPrice: int, listingType: str):


    # properties = scrape_property(
    #     location=location,
    #     # listing_type=listingType,  # for_sale, for_rent, pending
    #     past_days=30,  # sold in last 30 days - listed in last 30 days if (for_sale, for_rent)
    #     extra_property_data=True,
    #     # property_type=['single_family','multi_family'],
    #     # date_from="2023-05-01", # alternative to past_days
    #     # date_to="2023-05-28",
    #     # foreclosure=True
    #     # mls_only=True,  # only fetch MLS listings
    #     limit=limit
    # )

    # load fake properties so I don't have to keep querying apartments.com
    properties = getFakeProperties()

    # use this to write to a file if you want to store/use fake data without querying
    # # Convert to dictionary
    # df_dict = properties.to_dict(orient='list')
    # # Write to a Python file
    # with open("sampleHousingData.py", "w") as f:
    #     f.write(f"DATA = {df_dict}")


    # filter out unnecessary fields 
    properties = properties[importantFields]

    # get values instead of dictionaries
    properties = properties.map(lambda x: x['0'] if isinstance(x, dict) else x)
    
    # replace inf/nan values before converting to json
    properties.replace([np.inf, -np.inf], np.nan, inplace=True)
    properties.fillna('', inplace=True)
   
    properties = properties[(properties['list_price'] <= maxPrice) & (properties['list_price'] >= minPrice)]


    # add rent for each property
    # properties['rent'] = properties.apply(calc.getRent, axis=1)

    # get in json format
    json_data = properties.to_dict(orient="records")

    return json_data


def getFakeProperties():
    return pd.DataFrame(DATA)

def calcRent(address: str):
    print("Calculating rent for address: " + address)
    return random.randint(1000, 5000)

# print(propSearch('Denver', 10000, 0, 10000000, 'nothin'))
