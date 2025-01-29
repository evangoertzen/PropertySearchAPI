from homeharvest import scrape_property
from datetime import datetime

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

def propSearch(location: str):

    properties = scrape_property(
        location=location,
        listing_type="for_sale",  # or (for_sale, for_rent, pending)
        past_days=30,  # sold in last 30 days - listed in last 30 days if (for_sale, for_rent)
        extra_property_data=True,
        # property_type=['single_family','multi_family'],
        # date_from="2023-05-01", # alternative to past_days
        # date_to="2023-05-28",
        # foreclosure=True
        # mls_only=True,  # only fetch MLS listings
        # limit=1
    )

    print(f"Number of properties: {len(properties)}")

    properties = properties.applymap(lambda x: x['0'] if isinstance(x, dict) else x)

    # print(column_names)
    json_data = properties.to_dict(orient="records")


    print(properties.head())
    return json_data