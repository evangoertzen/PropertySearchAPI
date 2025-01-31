import json
import propertySearch as ps
import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular app URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/random")
def get_random_number():
    return {"random_number": random.randint(1, 100)}

@app.get("/getProperties")
def get_properties(location: str, limit: int, minPrice: int, maxPrice: int, listingType: str):
    return {"properties": ps.propSearch(location, limit, minPrice, maxPrice, listingType)}
    json_text = '''
    {
    "properties": [
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1005-Gateway-Ln_Chico_CA_95926_M19282-02035",
        "property_id": "1928202035",
        "listing_id": "2977779801",
        "mls": "MRCA",
        "mls_id": "SN25021100",
        "status": "FOR_SALE",
        "text": "Location, location, location! Nestled in a peaceful neighborhood yet just minutes from Emma Wilson Elementary, local dining, shopping, CSUC, and a quick drive to downtown Chico, this charming home offers the perfect blend of comfort and convenience. Step inside and be greeted by modern elegance, featuring beautiful new flooring, soft neutral tones that enhance the bright and airy feel, soaring vaulted ceilings, skylights and seamlessly connected family and living roomsideal for effortless entertaining. Designed for the everyday chef, the kitchen boasts beautiful wood cabinetry, tile countertops, an electric range for easy cooking, a dishwasher, and a cozy breakfast bar for quick meals. The primary suite is a true retreat, offering generous space to unwind, private backyard access, built-in storage, a walk-in closet, and an en suite bath complete with a spacious walk-in shower. Additional highlights include ceiling fans throughout, two roomy guest bedrooms, a convenient half-bath for visitors, owned solar, and an attached two-car garage with built-in cabinetry. The backyard is perfect for summer fun, featuring a large covered patio for outdoor gatherings and a lush lawn where pets can roam or enjoy a game of catch. With its prime location and extensive list of amenities, this home is a rare find. Dont let it slip away!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "1005 Gateway Ln",
        "street": "1005 Gateway Ln",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 1,
        "sqft": 1848,
        "year_built": 1989,
        "days_on_mls": 0,
        "list_price": 485000,
        "list_date": "2025-01-30",
        "assessed_value": 423300,
        "estimated_value": 468944,
        "tax": 4722,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4722,
            "assessment": {
                "building": 204000,
                "land": 219300,
                "total": 423300
            }
            },
            {
            "year": 2022,
            "tax": 2414,
            "assessment": {
                "building": 139696,
                "land": 75221,
                "total": 214917
            }
            },
            {
            "year": 2021,
            "tax": 2290,
            "assessment": {
                "building": 136957,
                "land": 73747,
                "total": 210704
            }
            },
            {
            "year": 2020,
            "tax": 2283,
            "assessment": {
                "building": 135553,
                "land": 72991,
                "total": 208544
            }
            },
            {
            "year": 2019,
            "tax": 2240,
            "assessment": {
                "building": 132896,
                "land": 71560,
                "total": 204456
            }
            },
            {
            "year": 2018,
            "tax": 2198,
            "assessment": {
                "building": 130291,
                "land": 70157,
                "total": 200448
            }
            },
            {
            "year": 2017,
            "tax": 2159,
            "assessment": {
                "building": 127737,
                "land": 68782,
                "total": 196519
            }
            },
            {
            "year": 2016,
            "tax": 1971,
            "assessment": {
                "building": 125233,
                "land": 67434,
                "total": 192667
            }
            },
            {
            "year": 2015,
            "tax": 1970,
            "assessment": {
                "building": 123352,
                "land": 66422,
                "total": 189774
            }
            },
            {
            "year": 2014,
            "tax": 1921,
            "assessment": {
                "building": 120936,
                "land": 65121,
                "total": 186057
            }
            },
            {
            "year": 2013,
            "tax": 1944,
            "assessment": {
                "building": 120390,
                "land": 64827,
                "total": 185217
            }
            },
            {
            "year": 2012,
            "tax": 1831,
            "assessment": {
                "building": 118030,
                "land": 63556,
                "total": 181586
            }
            },
            {
            "year": 2010,
            "tax": 1809,
            "assessment": {
                "building": 115716,
                "land": 62310,
                "total": 178026
            }
            },
            {
            "year": 2009,
            "tax": 1841,
            "assessment": {
                "building": 114852,
                "land": 61845,
                "total": 176697
            }
            },
            {
            "year": 2008,
            "tax": 1768,
            "assessment": {
                "building": 112868,
                "land": 60777,
                "total": 173645
            }
            },
            {
            "year": 2007,
            "tax": 1727,
            "assessment": {
                "building": 110655,
                "land": 59586,
                "total": 170241
            }
            }
        ],
        "lot_sqft": 7405,
        "price_per_sqft": 262,
        "latitude": 39.731258,
        "longitude": -121.868497,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/e2de6b4b560bf95ed74eaeadd87dc5ael-m3427559936od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4375
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/277-E-8th-Ave_Chico_CA_95926_M28419-74317",
        "property_id": "2841974317",
        "listing_id": "2977538546",
        "mls": "MRCA",
        "mls_id": "SN25016823",
        "status": "CONTINGENT",
        "text": "Opportunity knocks as this attractive Craftsman home is priced to sell!! Close to Enloe Hospital, this 2 bedroom, 1 bath classic home is on a nice lot with a garage in back.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "277 E 8th Ave",
        "street": "277 E 8th Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 2,
        "full_baths": 1,
        "half_baths": 0,
        "sqft": 744,
        "year_built": 1910,
        "days_on_mls": 7,
        "list_price": 289000,
        "list_date": "2025-01-23",
        "assessed_value": 106527,
        "estimated_value": 264500,
        "tax": 1196,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1196,
            "assessment": {
                "building": 35505,
                "land": 71022,
                "total": 106527
            }
            },
            {
            "year": 2022,
            "tax": 1176,
            "assessment": {
                "building": 34809,
                "land": 69630,
                "total": 104439
            }
            },
            {
            "year": 2021,
            "tax": 1154,
            "assessment": {
                "building": 34127,
                "land": 68265,
                "total": 102392
            }
            },
            {
            "year": 2020,
            "tax": 1151,
            "assessment": {
                "building": 33778,
                "land": 67566,
                "total": 101344
            }
            },
            {
            "year": 2019,
            "tax": 1130,
            "assessment": {
                "building": 33116,
                "land": 66242,
                "total": 99358
            }
            },
            {
            "year": 2018,
            "tax": 1110,
            "assessment": {
                "building": 32467,
                "land": 64944,
                "total": 97411
            }
            },
            {
            "year": 2017,
            "tax": 1087,
            "assessment": {
                "building": 31831,
                "land": 63671,
                "total": 95502
            }
            },
            {
            "year": 2016,
            "tax": 992,
            "assessment": {
                "building": 31207,
                "land": 62423,
                "total": 93630
            }
            },
            {
            "year": 2015,
            "tax": 992,
            "assessment": {
                "building": 30739,
                "land": 61486,
                "total": 92225
            }
            },
            {
            "year": 2014,
            "tax": 981,
            "assessment": {
                "building": 30137,
                "land": 60282,
                "total": 90419
            }
            },
            {
            "year": 2013,
            "tax": 988,
            "assessment": {
                "building": 30001,
                "land": 60010,
                "total": 90011
            }
            },
            {
            "year": 2012,
            "tax": 932,
            "assessment": {
                "building": 29413,
                "land": 58834,
                "total": 88247
            }
            },
            {
            "year": 2010,
            "tax": 922,
            "assessment": {
                "building": 28837,
                "land": 57681,
                "total": 86518
            }
            },
            {
            "year": 2009,
            "tax": 938,
            "assessment": {
                "building": 28622,
                "land": 57250,
                "total": 85872
            }
            },
            {
            "year": 2008,
            "tax": 906,
            "assessment": {
                "building": 28128,
                "land": 56261,
                "total": 84389
            }
            },
            {
            "year": 2007,
            "tax": 882,
            "assessment": {
                "building": 27577,
                "land": 55158,
                "total": 82735
            }
            }
        ],
        "lot_sqft": 5227,
        "price_per_sqft": 388,
        "latitude": 39.746129,
        "longitude": -121.848307,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/3d0e0b319805f2db61819291c052aca5l-b3533027017od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4569
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1257-E-9th-St_Chico_CA_95928_M29206-05455",
        "property_id": "2920605455",
        "listing_id": "2977537701",
        "mls": "MRCA",
        "mls_id": "SN25016839",
        "status": "FOR_SALE",
        "text": "Prime Development Opportunity Double Lot in R2 Zone! Unlock the potential of this double lot zoned R2 Medium Density Residential. Conveniently located near Highway 99, Chico State University, and Bidwell Park, this property sits in a highly desirable area with excellent redevelopment prospects. This property currently features two homes, one on each lot, that are in need of extensive repairs or redevelopment. The possibilities are endless with R2 zoning perfect for a developer or investor looking to maximize the potential of this property. Asbestos removal has already been completed by the seller, saving you a major step in the redevelopment process. Located in a neighborhood with strong demand, this property offers the ideal opportunity for creative redevelopment to meet modern housing needs. Per Cal Trans, no frontage improvements will be required. Don't miss out on this rare chance to transform this centrally located property into a lucrative investment. Bring your vision and your cash offer today!",
        "style": "LAND",
        "full_street_line": "1257 E 9th St",
        "street": "1257 E 9th St",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 0,
        "full_baths": 0,
        "half_baths": 0,
        "sqft": 0,
        "year_built": 0,
        "days_on_mls": 7,
        "list_price": 245000,
        "list_date": "2025-01-23",
        "assessed_value": 28622,
        "estimated_value": 237385,
        "tax": 9653,
        "tax_history": [
            {
            "year": 2023,
            "tax": 9653,
            "assessment": {
                "building": 13556,
                "land": 15066,
                "total": 28622
            }
            },
            {
            "year": 2022,
            "tax": 253,
            "assessment": {
                "building": 13291,
                "land": 14771,
                "total": 28062
            }
            },
            {
            "year": 2021,
            "tax": 246,
            "assessment": {
                "building": 13031,
                "land": 14482,
                "total": 27513
            }
            },
            {
            "year": 2020,
            "tax": 245,
            "assessment": {
                "building": 12898,
                "land": 14334,
                "total": 27232
            }
            },
            {
            "year": 2019,
            "tax": 240,
            "assessment": {
                "building": 12646,
                "land": 14053,
                "total": 26699
            }
            },
            {
            "year": 2018,
            "tax": 232,
            "assessment": {
                "building": 12399,
                "land": 13778,
                "total": 26177
            }
            },
            {
            "year": 2017,
            "tax": 226,
            "assessment": {
                "building": 12156,
                "land": 13508,
                "total": 25664
            }
            },
            {
            "year": 2016,
            "tax": 207,
            "assessment": {
                "building": 11918,
                "land": 13244,
                "total": 25162
            }
            },
            {
            "year": 2015,
            "tax": 205,
            "assessment": {
                "building": 11739,
                "land": 13046,
                "total": 24785
            }
            },
            {
            "year": 2014,
            "tax": 213,
            "assessment": {
                "building": 11510,
                "land": 12791,
                "total": 24301
            }
            },
            {
            "year": 2013,
            "tax": 207,
            "assessment": {
                "building": 11458,
                "land": 12734,
                "total": 24192
            }
            },
            {
            "year": 2012,
            "tax": 192,
            "assessment": {
                "building": 11234,
                "land": 12485,
                "total": 23719
            }
            },
            {
            "year": 2010,
            "tax": 186,
            "assessment": {
                "building": 11014,
                "land": 12241,
                "total": 23255
            }
            },
            {
            "year": 2009,
            "tax": 189,
            "assessment": {
                "building": 10932,
                "land": 12150,
                "total": 23082
            }
            },
            {
            "year": 2008,
            "tax": 185,
            "assessment": {
                "building": 10744,
                "land": 11941,
                "total": 22685
            }
            },
            {
            "year": 2007,
            "tax": 176,
            "assessment": {
                "building": 10534,
                "land": 11707,
                "total": 22241
            }
            }
        ],
        "lot_sqft": 12632,
        "price_per_sqft": 0,
        "latitude": 39.733234,
        "longitude": -121.822846,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/dfb92a4f7ccb9d0eec6be60e5c9eb58dl-m2124963196od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3355
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/3094-Gallatin-Gtwy_Chico_CA_95973_M22299-56812",
        "property_id": "2229956812",
        "listing_id": "2977770872",
        "mls": "MRCA",
        "mls_id": "SN25020833",
        "status": "FOR_SALE",
        "text": "Built in 2011, this beautiful home offers an inviting living space with a functional layout. The tile entry and living area create a lovely, yet durable and easy to maintain foundation. The kitchen is designed for both style and convenience, featuring granite countertops, an eating bar, and a pantry, all seamlessly open to the living area. Additionally, there is a versatile bonus room that provides endless possibilities to suit your personal needs use it as an office, sitting room, formal dining area, playroom or... The spacious primary bedroom is a true retreat, boasting a trey ceiling, ample natural light, private access to the backyard, and a lovely en-suite bathroom with a walk-in closet. Additional highlights include an indoor laundry room and a thoughtfully designed floor plan that maximizes comfort. This home is situated in a quiet neighborhood close to Wildwood Park, Hancock Park, Bidwell Park and is just steps from the neighborhood scenic walking path. A fantastic location with a peaceful setting and an opportunity you do not want to miss!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "3094 Gallatin Gtwy",
        "street": "3094 Gallatin Gtwy",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1519,
        "year_built": 2011,
        "days_on_mls": 0,
        "list_price": 475000,
        "list_date": "2025-01-30",
        "assessed_value": 337997,
        "estimated_value": 480900,
        "tax": 4014,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4014,
            "assessment": {
                "building": 204137,
                "land": 133860,
                "total": 337997
            }
            },
            {
            "year": 2022,
            "tax": 3983,
            "assessment": {
                "building": 200135,
                "land": 131236,
                "total": 331371
            }
            },
            {
            "year": 2021,
            "tax": 3817,
            "assessment": {
                "building": 196211,
                "land": 128663,
                "total": 324874
            }
            },
            {
            "year": 2020,
            "tax": 3802,
            "assessment": {
                "building": 194200,
                "land": 127344,
                "total": 321544
            }
            },
            {
            "year": 2019,
            "tax": 3707,
            "assessment": {
                "building": 190393,
                "land": 124848,
                "total": 315241
            }
            },
            {
            "year": 2018,
            "tax": 3606,
            "assessment": {
                "building": 186660,
                "land": 122400,
                "total": 309060
            }
            },
            {
            "year": 2017,
            "tax": 3533,
            "assessment": {
                "building": 183000,
                "land": 120000,
                "total": 303000
            }
            },
            {
            "year": 2016,
            "tax": 3400,
            "assessment": {
                "building": 177192,
                "land": 95492,
                "total": 272684
            }
            },
            {
            "year": 2015,
            "tax": 3141,
            "assessment": {
                "building": 174531,
                "land": 94058,
                "total": 268589
            }
            },
            {
            "year": 2014,
            "tax": 3054,
            "assessment": {
                "building": 171113,
                "land": 92216,
                "total": 263329
            }
            },
            {
            "year": 2013,
            "tax": 2843,
            "assessment": {
                "building": 170340,
                "land": 91800,
                "total": 262140
            }
            },
            {
            "year": 2012,
            "tax": 2052,
            "assessment": {
                "building": 156500,
                "land": 40490,
                "total": 196990
            }
            }
        ],
        "lot_sqft": 4792,
        "price_per_sqft": 313,
        "latitude": 39.770904,
        "longitude": -121.819831,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/32734be175b3c08b85ab1ea579dabcffl-b134036683od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4936
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/480-Weymouth-Way_Chico_CA_95973_M23287-68422",
        "property_id": "2328768422",
        "listing_id": "2977732951",
        "mls": "MRCA",
        "mls_id": "SN25011183",
        "status": "FOR_SALE",
        "text": "Stunning, Spacious, and Serene! This beautiful 4 bedroom 3.5 bath home sits peacefully at the end of the cul-de-sac and is an entertainer's dream! The remodeled kitchen has great natural light, a large kitchen island, 15 ft ceilings, tons of storage, 6 burner stove, built-in microwave, instant hot water spout, pantry, wine refrigerator, and is open to the living and eating areas with tons of windows, a fireplace, and access to the outdoor patio. With the split floor plan, the primary suite sits on one side and features beautiful views of the backyard through the various windows, a large walk-in closet, separate shower and soaking tub, and access to the covered outdoor patio. Not only are there 3 other bedrooms, one with an en suite full bathroom, but there is a gorgeous office with French doors, built-in shelves and a desk, as well as a large media/bonus room with a custom barn door, indoor laundry room with a utility sink and tons of storage and counter space, owned solar, and a huge 3 car garage! The outside of this home is just as amazing as the inside - with a covered patio perfect for relaxing, an outdoor kitchen area with a built-in BBQ, 2 burners, and an eating bar, a beautiful L-shaped salt water pool, a fire pit area, 2 lawn areas perfect for playing or gardening, a custom built storage shed, privacy and more - this home has it all! Dont miss out on this one of a kind home!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "480 Weymouth Way",
        "street": "480 Weymouth Way",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 4,
        "full_baths": 3,
        "half_baths": 1,
        "sqft": 3129,
        "year_built": 2005,
        "days_on_mls": 1,
        "list_price": 998000,
        "list_date": "2025-01-29",
        "assessed_value": 956760,
        "estimated_value": 908922,
        "tax": 11030,
        "tax_history": [
            {
            "year": 2023,
            "tax": 11030,
            "assessment": {
                "building": 768060,
                "land": 188700,
                "total": 956760
            }
            },
            {
            "year": 2022,
            "tax": 6691,
            "assessment": {
                "building": 422544,
                "land": 144869,
                "total": 567413
            }
            },
            {
            "year": 2021,
            "tax": 6585,
            "assessment": {
                "building": 414259,
                "land": 142029,
                "total": 556288
            }
            },
            {
            "year": 2020,
            "tax": 6582,
            "assessment": {
                "building": 410012,
                "land": 140573,
                "total": 550585
            }
            },
            {
            "year": 2019,
            "tax": 6412,
            "assessment": {
                "building": 401973,
                "land": 137817,
                "total": 539790
            }
            },
            {
            "year": 2018,
            "tax": 6267,
            "assessment": {
                "building": 394092,
                "land": 135115,
                "total": 529207
            }
            },
            {
            "year": 2017,
            "tax": 6164,
            "assessment": {
                "building": 386365,
                "land": 132466,
                "total": 518831
            }
            },
            {
            "year": 2016,
            "tax": 5615,
            "assessment": {
                "building": 378790,
                "land": 129869,
                "total": 508659
            }
            },
            {
            "year": 2015,
            "tax": 5651,
            "assessment": {
                "building": 373101,
                "land": 127919,
                "total": 501020
            }
            },
            {
            "year": 2014,
            "tax": 5530,
            "assessment": {
                "building": 365793,
                "land": 125414,
                "total": 491207
            }
            },
            {
            "year": 2013,
            "tax": 5580,
            "assessment": {
                "building": 364140,
                "land": 124848,
                "total": 488988
            }
            },
            {
            "year": 2012,
            "tax": 5335,
            "assessment": {
                "building": 357000,
                "land": 122400,
                "total": 479400
            }
            },
            {
            "year": 2010,
            "tax": 5906,
            "assessment": {
                "building": 385000,
                "land": 140000,
                "total": 525000
            }
            },
            {
            "year": 2009,
            "tax": 6411,
            "assessment": {
                "building": 385000,
                "land": 140000,
                "total": 525000
            }
            },
            {
            "year": 2008,
            "tax": 7208,
            "assessment": {
                "building": 483816,
                "land": 192474,
                "total": 676290
            }
            },
            {
            "year": 2007,
            "tax": 7095,
            "assessment": {
                "building": 449820,
                "land": 188700,
                "total": 638520
            }
            }
        ],
        "lot_sqft": 13504,
        "price_per_sqft": 319,
        "latitude": 39.771676,
        "longitude": -121.89076,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/1cb4df68c810510b68691399b95ad4c6l-m1809612175od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1701
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/111-Gooselake-Cir_Chico_CA_95973_M10023-54851",
        "property_id": "1002354851",
        "listing_id": "2977612863",
        "mls": "MRCA",
        "mls_id": "SN25011669",
        "status": "FOR_SALE",
        "text": "Welcome to 111 Gooselake Circle, a beautifully designed 3-bedroom, 2-bathroom home offering 1, 610 square feet of stylish and functional living space. From the moment you enter through the inviting entryway, you'll feel at home in this open floor plan, thoughtfully designed for entertaining and modern living. The main living area features beautiful LVP flooring throughout, with a cozy gas fireplace serving as the centerpiece of the spacious living room. The kitchen, open to the living room, is a chef's dream boasting stunning quartz countertops, stainless steel appliances (including a gas stove), a walk-in pantry, and a clever built-in trash drawer to keep things tidy. The adjoining dining area overlooks the backyard, seamlessly blending indoor and outdoor living. Off the kitchen, you'll find a well-appointed laundry room with a built-in shelf for easy folding and direct access to the two-car garage, which includes an electric car charger. The home offers 2 generously sized bedrooms, each filled with natural light streaming through well-placed windows. The primary suite offers a private retreat, featuring an en-suite with dual sinks, a walk-in shower, and a large walk-in closet to keep everything organized. Head out to your private backyard oasis, complete with a refreshing pool to beat the summer heat, a lush grassy area where your furry friends can play, and raised garden beds ready for your green thumb to flourish! A convenient storage shed ensures your tools and supplies stay organized and easily accessible. And the best part? This home features an oversized OWNED solar system with 28 panels, delivering incredible energy savings - Sellers reported $0 electric bills during the summer! Located just minutes from DeGarmo Park and the new Card Community Park, this home is perfectly situated for those outdoor enthusiasts. Don't miss your chance to see this incredible property - schedule your private tour today!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "111 Gooselake Cir",
        "street": "111 Gooselake Cir",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1610,
        "year_built": 2010,
        "days_on_mls": 4,
        "list_price": 560000,
        "list_date": "2025-01-26",
        "assessed_value": 582624,
        "estimated_value": 566100,
        "tax": 6718,
        "tax_history": [
            {
            "year": 2023,
            "tax": 6718,
            "assessment": {
                "building": 384948,
                "land": 197676,
                "total": 582624
            }
            },
            {
            "year": 2022,
            "tax": 6639,
            "assessment": {
                "building": 377400,
                "land": 193800,
                "total": 571200
            }
            },
            {
            "year": 2021,
            "tax": 4633,
            "assessment": {
                "building": 229534,
                "land": 166949,
                "total": 396483
            }
            },
            {
            "year": 2020,
            "tax": 4530,
            "assessment": {
                "building": 227181,
                "land": 165238,
                "total": 392419
            }
            },
            {
            "year": 2019,
            "tax": 4407,
            "assessment": {
                "building": 222727,
                "land": 161999,
                "total": 384726
            }
            },
            {
            "year": 2018,
            "tax": 4268,
            "assessment": {
                "building": 218360,
                "land": 158823,
                "total": 377183
            }
            },
            {
            "year": 2017,
            "tax": 3944,
            "assessment": {
                "building": 215000,
                "land": 135000,
                "total": 350000
            }
            },
            {
            "year": 2016,
            "tax": 3513,
            "assessment": {
                "building": 205000,
                "land": 130000,
                "total": 335000
            }
            },
            {
            "year": 2015,
            "tax": 3510,
            "assessment": {
                "building": 210000,
                "land": 120000,
                "total": 330000
            }
            },
            {
            "year": 2014,
            "tax": 3245,
            "assessment": {
                "building": 185000,
                "land": 120000,
                "total": 305000
            }
            },
            {
            "year": 2013,
            "tax": 3345,
            "assessment": {
                "building": 215000,
                "land": 95000,
                "total": 310000
            }
            },
            {
            "year": 2012,
            "tax": 3222,
            "assessment": {
                "building": 215000,
                "land": 95000,
                "total": 310000
            }
            },
            {
            "year": 2010,
            "tax": 891,
            "assessment": {
                "building": 166242,
                "land": 141054,
                "total": 307296
            }
            }
        ],
        "lot_sqft": 8712,
        "price_per_sqft": 348,
        "latitude": 39.773024,
        "longitude": -121.885866,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/4cd2daf798a04424c68ac63baeac270cl-m1575221315od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4968
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/Highway-32_Chico_CA_95973_M22305-11948",
        "property_id": "2230511948",
        "listing_id": "2977592631",
        "mls": "MRCA",
        "mls_id": "SN25018030",
        "status": "FOR_SALE",
        "text": "Enjoy a total of beautiful 160 acres of land.",
        "style": "LAND",
        "full_street_line": "Cohasset",
        "street": 0,
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 0,
        "full_baths": 0,
        "half_baths": 0,
        "sqft": 0,
        "year_built": 0,
        "days_on_mls": 5,
        "list_price": 320000,
        "list_date": "2025-01-25",
        "assessed_value": 0,
        "estimated_value": 0,
        "tax": 0,
        "tax_history": 0,
        "lot_sqft": 6969600,
        "price_per_sqft": 0,
        "latitude": 0,
        "longitude": 0,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": 0,
        "primary_photo": "http://ap.rdcpix.com/bec45950edfc49a236b987dd807d39c1l-b1248293801od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1741
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/13966-Carriage-Estates-Way_Chico_CA_95973_M21651-76163",
        "property_id": "2165176163",
        "listing_id": "2977659309",
        "mls": "MRCA",
        "mls_id": "SN25018974",
        "status": "FOR_SALE",
        "text": "Welcome to your Dream Home: A Story of Luxury and Serenity! Nestled in a private and serene setting, this exceptional property is a harmonious blend of elegance, practicality, & tranquility. From the moment you arrive, the wide circular driveway welcomes you into a world of comfort & thoughtful design. Step inside and discover a home crafted for both beauty & functionality. The interior boasts seamless accessibility, with wide hallways & no steps, making every corner of the house easy to navigate. The heart of the home is the gourmet kitchen, where modern convenience meets classic charm. Soft-close drawers, a stunning wood-paneled Thermador refrigerator, a Bosch dishwasher, & an induction cooktop with easy-clean features make cooking a pleasure. The heated floors provide an added touch of luxury, ensuring every step feels warm and inviting. The great room is a cozy retreat, with a gas fireplace & expansive windows that frame the breathtaking backyard. Just beyond the glass lies a tranquil oasis, complete with koi ponds, waterfalls, and lush landscaping that comes alive with hummingbirds, butterflies, & dragonflies. This is a space where mornings begin with coffee on the patio & evenings end with peaceful relaxation. The primary suite is a true haven, offering stunning views of the backyard & direct access to a hot tub-ready patio. The en-suite bathroom is a spa-like escape, featuring a jacuzzi tub, & heated floors for ultimate comfort. Outdoors, the resort-style beckons with a sparkling pool with a Baja shelf perfect for lounging in the sun, while the cascading waterfalls adds a tranquil ambiance. The expansive patio, equipped with misters, a natural gas hookup for a BBQ, & water access for an outdoor kitchen, is ideal for entertaining or simply enjoying the beauty around you. This property also includes a two-bedroom ADU, perfect for guests or extended family, & a fully equipped shop that accommodates an RV, Trailer, or Boat! The shop features air compressor reels, hot water spigots, & a versatile attic space ready to be transformed into a game room, additional storage, or hobby room, the options are endless. With smart home features controlling sprinklers, irrigation, and pool systems, as well as a whole-house generator & a robust well system delivering ample water, this property is as efficient as it is beautiful. This is more than a home - it's a sanctuary designed for living life to the fullest. Schedule your private tour today!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "13966 Carriage Estates Way",
        "street": "13966 Carriage Estates Way",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 4,
        "full_baths": 4,
        "half_baths": 0,
        "sqft": 3795,
        "year_built": 2003,
        "days_on_mls": 3,
        "list_price": 1865000,
        "list_date": "2025-01-27",
        "assessed_value": 896916,
        "estimated_value": 1094200,
        "tax": 8322,
        "tax_history": [
            {
            "year": 2023,
            "tax": 8322,
            "assessment": {
                "building": 704438,
                "land": 192478,
                "total": 896916
            }
            },
            {
            "year": 2022,
            "tax": 8280,
            "assessment": {
                "building": 690626,
                "land": 188704,
                "total": 879330
            }
            },
            {
            "year": 2021,
            "tax": 8121,
            "assessment": {
                "building": 677085,
                "land": 185004,
                "total": 862089
            }
            },
            {
            "year": 2020,
            "tax": 7361,
            "assessment": {
                "building": 555000,
                "land": 230000,
                "total": 785000
            }
            },
            {
            "year": 2019,
            "tax": 7246,
            "assessment": {
                "building": 550000,
                "land": 220000,
                "total": 770000
            }
            },
            {
            "year": 2018,
            "tax": 6826,
            "assessment": {
                "building": 525000,
                "land": 200000,
                "total": 725000
            }
            },
            {
            "year": 2017,
            "tax": 6526,
            "assessment": {
                "building": 495000,
                "land": 200000,
                "total": 695000
            }
            },
            {
            "year": 2016,
            "tax": 5525,
            "assessment": {
                "building": 450000,
                "land": 190000,
                "total": 640000
            }
            },
            {
            "year": 2015,
            "tax": 4854,
            "assessment": {
                "building": 425000,
                "land": 145000,
                "total": 570000
            }
            },
            {
            "year": 2014,
            "tax": 4519,
            "assessment": {
                "building": 410000,
                "land": 130000,
                "total": 540000
            }
            },
            {
            "year": 2013,
            "tax": 4648,
            "assessment": {
                "building": 410000,
                "land": 130000,
                "total": 540000
            }
            },
            {
            "year": 2012,
            "tax": 4291,
            "assessment": {
                "building": 390000,
                "land": 130000,
                "total": 520000
            }
            },
            {
            "year": 2010,
            "tax": 6570,
            "assessment": {
                "building": 572054,
                "land": 156310,
                "total": 728364
            }
            },
            {
            "year": 2009,
            "tax": 6690,
            "assessment": {
                "building": 567779,
                "land": 155142,
                "total": 722921
            }
            },
            {
            "year": 2008,
            "tax": 6475,
            "assessment": {
                "building": 557969,
                "land": 152462,
                "total": 710431
            }
            },
            {
            "year": 2007,
            "tax": 7466,
            "assessment": {
                "building": 547029,
                "land": 149473,
                "total": 696502
            }
            }
        ],
        "lot_sqft": 57935,
        "price_per_sqft": 491,
        "latitude": 39.811898,
        "longitude": -121.903368,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/f02d45bc203ff2213b79c078348bb4ecl-m2801911965od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1925
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/3320-Shadybrook-Ln_Chico_CA_95928_M29366-60137",
        "property_id": "2936660137",
        "listing_id": "2977637458",
        "mls": "MRCA",
        "mls_id": "SN25019018",
        "status": "FOR_SALE",
        "text": "This parcel is one of the highest points in Canyon Oaks. 4.58 acres that borders Bidwell Park. The back yard bluff is adjacent to the Park. Panoramic breathtaking views that combine the serenity of nature and vibrant cityscape. Situated in the sought after Canyon Oaks near the Jim Summers designed Canyon Oaks Country Club course. VIEWS: Enjoy unparalled backyard vista of the picturesque Upper Bidwell Park, while the front of the property boasts stunning views, perfect for watching the sunsets over Chico.",
        "style": "LAND",
        "full_street_line": "3320 Shadybrook Ln",
        "street": "3320 Shadybrook Ln",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 0,
        "full_baths": 0,
        "half_baths": 0,
        "sqft": 0,
        "year_built": 0,
        "days_on_mls": 3,
        "list_price": 306000,
        "list_date": "2025-01-27",
        "assessed_value": 278827,
        "estimated_value": 352000,
        "tax": 3109,
        "tax_history": [
            {
            "year": 2023,
            "tax": 3109,
            "assessment": {
                "building": null,
                "land": 278827,
                "total": 278827
            }
            },
            {
            "year": 2022,
            "tax": 3054,
            "assessment": {
                "building": null,
                "land": 273360,
                "total": 273360
            }
            },
            {
            "year": 2021,
            "tax": 2996,
            "assessment": {
                "building": null,
                "land": 268000,
                "total": 268000
            }
            },
            {
            "year": 2020,
            "tax": 3729,
            "assessment": {
                "building": null,
                "land": 331074,
                "total": 331074
            }
            },
            {
            "year": 2019,
            "tax": 3661,
            "assessment": {
                "building": null,
                "land": 324583,
                "total": 324583
            }
            },
            {
            "year": 2018,
            "tax": 3594,
            "assessment": {
                "building": null,
                "land": 318219,
                "total": 318219
            }
            },
            {
            "year": 2017,
            "tax": 3522,
            "assessment": {
                "building": null,
                "land": 311980,
                "total": 311980
            }
            },
            {
            "year": 2016,
            "tax": 3213,
            "assessment": {
                "building": null,
                "land": 305863,
                "total": 305863
            }
            },
            {
            "year": 2015,
            "tax": 3213,
            "assessment": {
                "building": null,
                "land": 301269,
                "total": 301269
            }
            },
            {
            "year": 2014,
            "tax": 2654,
            "assessment": {
                "building": null,
                "land": 250000,
                "total": 250000
            }
            },
            {
            "year": 2013,
            "tax": 2169,
            "assessment": {
                "building": null,
                "land": 200000,
                "total": 200000
            }
            },
            {
            "year": 2012,
            "tax": 2084,
            "assessment": {
                "building": null,
                "land": 200000,
                "total": 200000
            }
            },
            {
            "year": 2010,
            "tax": 3876,
            "assessment": {
                "building": null,
                "land": 282617,
                "total": 282617
            }
            },
            {
            "year": 2009,
            "tax": 3023,
            "assessment": {
                "building": null,
                "land": 280505,
                "total": 280505
            }
            },
            {
            "year": 2008,
            "tax": 2919,
            "assessment": {
                "building": null,
                "land": 275659,
                "total": 275659
            }
            },
            {
            "year": 2007,
            "tax": 2839,
            "assessment": {
                "building": null,
                "land": 270254,
                "total": 270254
            }
            }
        ],
        "lot_sqft": 199505,
        "price_per_sqft": 0,
        "latitude": 39.767098,
        "longitude": -121.765624,
        "county": "Butte",
        "hoa_fee": 127,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/ba6d47bec5853fc9f81694106a20f34dl-m969951133od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1544
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1595-Manzanita-Ave-Unit-45_Chico_CA_95926_M25948-55750",
        "property_id": "2594855750",
        "listing_id": "2977686789",
        "mls": "MRCA",
        "mls_id": "SN25020036",
        "status": "FOR_SALE",
        "text": "Welcome to this beautifully maintained home in popular Chico Creek Mobile Estates. This is a gardeners delight with a pet friendly fenced yard, many plants, trees, shrubbery and a water drip system for easy care. Youll spend hours of peaceful relaxation on the expansive covered porch off the living room. Inside there is an easy flow floor plan with two nice sized bedrooms, a primary bathroom suite with a jetted bathtub and stall shower. The kitchen is perfectly suited for the cook with lots of counter and cupboard space, double oven, microwave, dishwasher, refrigerator plus pantry. The living room features cathedral ceilings, laminate flooring and a built in desk and China cabinet. There is plenty of space to park your vehicle under the covered carport, store tools and goods in the storage shed. Chico Creek Mobile Estates is in close proximity to the Safeway shopping center, eateries, professional offices, Pleasant Valley High School and Bidwell Park. This is senior living at its best with a safe, quiet and well-maintained community.",
        "style": "MOBILE",
        "full_street_line": "1595 Manzanita Ave Unit 45",
        "street": "1595 Manzanita Ave",
        "unit": "Unit 45",
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 2,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1272,
        "year_built": 1984,
        "days_on_mls": 2,
        "list_price": 110000,
        "list_date": "2025-01-28",
        "assessed_value": 0,
        "estimated_value": 89000,
        "tax": 1102,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1102
            },
            {
            "year": 2022,
            "tax": 1083
            },
            {
            "year": 2021,
            "tax": 1061
            },
            {
            "year": 2020,
            "tax": 1058
            },
            {
            "year": 2019,
            "tax": 315
            },
            {
            "year": 2016,
            "tax": 293,
            "assessment": {
                "building": null,
                "land": null,
                "total": 28000
            }
            },
            {
            "year": 2009,
            "tax": 569,
            "assessment": {
                "building": 54500,
                "land": null,
                "total": 54500
            }
            },
            {
            "year": 2008,
            "tax": 561,
            "assessment": {
                "building": 60000,
                "land": null,
                "total": 60000
            }
            },
            {
            "year": 2007,
            "tax": 556,
            "assessment": {
                "building": 60000,
                "land": null,
                "total": 60000
            }
            }
        ],
        "lot_sqft": 0,
        "price_per_sqft": 86,
        "latitude": 39.757269,
        "longitude": -121.809593,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/53143a10a4f4ee93e4a3802bcbf5b607l-m673704418od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3831
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1901-Dayton-Rd-Spc-141_Chico_CA_95928_M21172-37701",
        "property_id": "2117237701",
        "listing_id": "2977742553",
        "mls": "MRCA",
        "mls_id": "SN25019854",
        "status": "FOR_SALE",
        "text": "Beautiful manufactured home nestled within the serene 55+ community of Chico Mobile Country Club! Positioned on the outskirts of Chico, just minutes away from dining, shopping, and the vibrant Downtown Chico scene. This residence boasts an attached covered carport, a generously-sized patio with trex decking, a shed for additional storage and a fenced yard. Step inside to discover a meticulously maintained home with laminate flooring and dual pane windows throughout. The living area features a wall of illuminating windows, a charming wood stove that transitions into the designated dining space with a stunning built-in hutch. The kitchen showcases classic white cabinetry complemented with laminate countertops, well appointed appliances and a gas range. There is also a cozy nook right off the kitchen, ideal for a secondary dining area, craft room, or office space. A full laundry room with built-in storage that leads directly to access the carport. The oversized master bedroom offers the luxury of a sleeping area and a sitting area/ TV room with a sliding glass door that leads directly to the porch, an ensuite master bathroom with a walk-in shower. Residents also enjoy access to the community amenities including a pool, hot tub, gym, RV parking and much more! This community offers the ultimate convenience and leisure and essence of community living.",
        "style": "MOBILE",
        "full_street_line": "1901 Dayton Rd Spc 141",
        "street": "1901 Dayton Rd",
        "unit": "Spc 141",
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 2,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1440,
        "year_built": 1973,
        "days_on_mls": 1,
        "list_price": 68000,
        "list_date": "2025-01-29",
        "assessed_value": 0,
        "estimated_value": 56000,
        "tax": 210,
        "tax_history": [
            {
            "year": 2023,
            "tax": 210
            },
            {
            "year": 2022,
            "tax": 205
            },
            {
            "year": 2021,
            "tax": 200
            },
            {
            "year": 2020,
            "tax": 198
            },
            {
            "year": 2019,
            "tax": 193
            },
            {
            "year": 2016,
            "tax": 157,
            "assessment": {
                "building": null,
                "land": null,
                "total": 15000
            }
            },
            {
            "year": 2009,
            "tax": 86,
            "assessment": {
                "building": 15000,
                "land": null,
                "total": 15000
            }
            },
            {
            "year": 2008,
            "tax": 84,
            "assessment": {
                "building": 15000,
                "land": null,
                "total": 15000
            }
            },
            {
            "year": 2007,
            "tax": 84,
            "assessment": {
                "building": 15000,
                "land": null,
                "total": 15000
            }
            }
        ],
        "lot_sqft": 0,
        "price_per_sqft": 47,
        "latitude": 39.701473,
        "longitude": -121.846427,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/cc29ce7760adc75af9b095eec1e1f122l-m6252735od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1948
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/2057-Huntington-Dr_Chico_CA_95928_M28277-38726",
        "property_id": "2827738726",
        "listing_id": "2977591987",
        "mls": "MRCA",
        "mls_id": "SN25017635",
        "status": "FOR_SALE",
        "text": "Welcome to 2057 Huntington Drive in Chico, CA a home that perfectly combines comfort, convenience, and sustainability! This charming property boasts NEM II solar with net-positive energy generation, providing eco-friendly living and lower utility costs. In the past five years, the home has been thoughtfully updated with a new HVAC system, luxury vinyl flooring throughout, a new hot water heater, and several new dual-pane windows, ensuring energy efficiency and comfort. A standout feature is the She Shed complete with electrical and wall AC, making it the perfect retreat, home office, or hobby space. The open floor plan is designed for easy living and entertaining, with a cozy gas stove in the living room and vaulted ceilings in both the living room and master bedroom. The kitchen features solid surface counters, a stainless steel sink and appliances, a gas range, and a breakfast bar that connects seamlessly to the dining and living spaces. Both bathrooms have been stylishly updated with tile flooring, and ceiling fans throughout enhance comfort year-round. Conveniently located near shopping, Meriam Park, freeway access, and public transportation, this home is perfectly situated for an active lifestyle. Dont miss the chance to make this beautiful, energy-efficient property your own!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "2057 Huntington Dr",
        "street": "2057 Huntington Dr",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1215,
        "year_built": 1997,
        "days_on_mls": 5,
        "list_price": 419000,
        "list_date": "2025-01-25",
        "assessed_value": 255672,
        "estimated_value": 390986,
        "tax": 2879,
        "tax_history": [
            {
            "year": 2023,
            "tax": 2879,
            "assessment": {
                "building": 143743,
                "land": 111929,
                "total": 255672
            }
            },
            {
            "year": 2022,
            "tax": 2838,
            "assessment": {
                "building": 140925,
                "land": 109735,
                "total": 250660
            }
            },
            {
            "year": 2021,
            "tax": 2779,
            "assessment": {
                "building": 138162,
                "land": 107584,
                "total": 245746
            }
            },
            {
            "year": 2020,
            "tax": 2777,
            "assessment": {
                "building": 136746,
                "land": 106481,
                "total": 243227
            }
            },
            {
            "year": 2019,
            "tax": 2727,
            "assessment": {
                "building": 134065,
                "land": 104394,
                "total": 238459
            }
            },
            {
            "year": 2018,
            "tax": 2676,
            "assessment": {
                "building": 131437,
                "land": 102348,
                "total": 233785
            }
            },
            {
            "year": 2017,
            "tax": 2623,
            "assessment": {
                "building": 128860,
                "land": 100342,
                "total": 229202
            }
            },
            {
            "year": 2016,
            "tax": 2397,
            "assessment": {
                "building": 126334,
                "land": 98375,
                "total": 224709
            }
            },
            {
            "year": 2015,
            "tax": 2396,
            "assessment": {
                "building": 124437,
                "land": 96898,
                "total": 221335
            }
            },
            {
            "year": 2014,
            "tax": 2160,
            "assessment": {
                "building": 115000,
                "land": 85000,
                "total": 200000
            }
            },
            {
            "year": 2013,
            "tax": 2100,
            "assessment": {
                "building": 113000,
                "land": 85000,
                "total": 198000
            }
            },
            {
            "year": 2012,
            "tax": 1798,
            "assessment": {
                "building": 102000,
                "land": 75000,
                "total": 177000
            }
            },
            {
            "year": 2010,
            "tax": 2137,
            "assessment": {
                "building": 120000,
                "land": 75000,
                "total": 195000
            }
            },
            {
            "year": 2009,
            "tax": 2174,
            "assessment": {
                "building": 130151,
                "land": 76295,
                "total": 206446
            }
            },
            {
            "year": 2008,
            "tax": 2101,
            "assessment": {
                "building": 127903,
                "land": 74978,
                "total": 202881
            }
            },
            {
            "year": 2007,
            "tax": 2040,
            "assessment": {
                "building": 125396,
                "land": 73508,
                "total": 198904
            }
            }
        ],
        "lot_sqft": 4356,
        "price_per_sqft": 345,
        "latitude": 39.72513,
        "longitude": -121.798417,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/67fbaa80c25f89c24b0f3c690c63f92dl-b2932503296od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2558
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/2159-Elm-St-Unit-4_Chico_CA_95928_M21733-04356",
        "property_id": "2173304356",
        "listing_id": "2977522080",
        "mls": "MRCA",
        "mls_id": "SN25016207",
        "status": "FOR_SALE",
        "text": "Welcome to 2159 Elm St #4, a charming townhouse nestled in a 10-unit community. This delightful townhouse offers a perfect blend of comfort, functionality, and convenience. Built in 2003, this spacious 4-bedroom, 2-bathroom home boasts thoughtful design features and a welcoming atmosphere. The covered front porch provides a charming spot to enjoy views of the community's lush green lawn and mature landscaping. Head inside to discover a light-filled living room with upgraded luxury vinyl plank (LVP) flooring that flows throughout the home, and carpet reserved for the stairs. The kitchen is designed for convenience, featuring plenty of cabinetry, durable Formica countertops, and a cozy under-stairs closet that doubles as a pantry for added storage. Sliding glass doors open to a private, fully fenced patio - an ideal space for relaxing, gardening, or hosting a small gathering. Downstairs, you'll find a versatile bedroom perfect for guests, a home office, or a playroom, situated just steps from a full bathroom that also functions as the laundry area. Upstairs, the LVP flooring continues in the hallway and the three additional bedrooms. The upstairs bathroom offers a vanity area and a shower/tub combo with a private toilet, making it perfect for shared living. Additional highlights include dual-pane windows for energy efficiency, central HVAC for year-round comfort, and dedicated off-street parking. Conveniently located behind the iconic Sierra Nevada Brewery, this home is just minutes from the Chico Community Children's Center, the Silver Dollar Fairgrounds, and vibrant Downtown Chico. Whether you're seeking a primary residence or a smart investment, 2159 Elm St #4 offers low-maintenance living in a convenient location. Don't miss your chance to own this wonderful property - schedule a private showing today!",
        "style": "TOWNHOMES",
        "full_street_line": "2159 Elm St Unit 4",
        "street": "2159 Elm St",
        "unit": "Unit 4",
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 4,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1344,
        "year_built": 2003,
        "days_on_mls": 7,
        "list_price": 225000,
        "list_date": "2025-01-23",
        "assessed_value": 162930,
        "estimated_value": 224000,
        "tax": 1827,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1827,
            "assessment": {
                "building": 99861,
                "land": 63069,
                "total": 162930
            }
            },
            {
            "year": 2022,
            "tax": 1798,
            "assessment": {
                "building": 97903,
                "land": 61833,
                "total": 159736
            }
            },
            {
            "year": 2021,
            "tax": 1763,
            "assessment": {
                "building": 95984,
                "land": 60621,
                "total": 156605
            }
            },
            {
            "year": 2020,
            "tax": 1048,
            "assessment": {
                "building": 74649,
                "land": 17225,
                "total": 91874
            }
            },
            {
            "year": 2019,
            "tax": 1030,
            "assessment": {
                "building": 73186,
                "land": 16888,
                "total": 90074
            }
            },
            {
            "year": 2018,
            "tax": 1009,
            "assessment": {
                "building": 71751,
                "land": 16557,
                "total": 88308
            }
            },
            {
            "year": 2017,
            "tax": 989,
            "assessment": {
                "building": 70345,
                "land": 16233,
                "total": 86578
            }
            },
            {
            "year": 2016,
            "tax": 904,
            "assessment": {
                "building": 68966,
                "land": 15915,
                "total": 84881
            }
            },
            {
            "year": 2015,
            "tax": 903,
            "assessment": {
                "building": 67931,
                "land": 15676,
                "total": 83607
            }
            },
            {
            "year": 2014,
            "tax": 883,
            "assessment": {
                "building": 66601,
                "land": 15369,
                "total": 81970
            }
            },
            {
            "year": 2013,
            "tax": 893,
            "assessment": {
                "building": 66300,
                "land": 15300,
                "total": 81600
            }
            },
            {
            "year": 2012,
            "tax": 891,
            "assessment": {
                "building": 45000,
                "land": 35000,
                "total": 80000
            }
            },
            {
            "year": 2010,
            "tax": 1592,
            "assessment": {
                "building": 110000,
                "land": 40000,
                "total": 150000
            }
            },
            {
            "year": 2009,
            "tax": 1724,
            "assessment": {
                "building": 110000,
                "land": 40000,
                "total": 150000
            }
            },
            {
            "year": 2008,
            "tax": 2210,
            "assessment": {
                "building": 145656,
                "land": 62424,
                "total": 208080
            }
            },
            {
            "year": 2007,
            "tax": 2147,
            "assessment": {
                "building": 142800,
                "land": 61200,
                "total": 204000
            }
            }
        ],
        "lot_sqft": 871,
        "price_per_sqft": 167,
        "latitude": 39.72175,
        "longitude": -121.815876,
        "county": "Butte",
        "hoa_fee": 380,
        "nearby_schools": "Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/7c002341d04e587438e2fc3bcbc1b641l-m526860079od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2975
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/2507-Tuolumne-Dr_Chico_CA_95973_M27648-76186",
        "property_id": "2764876186",
        "listing_id": "2977729736",
        "mls": "SCCA",
        "mls_id": "225009651",
        "status": "FOR_SALE",
        "text": "This north Chico 1, 597 Sq. Ft., 3 bedroom and 2 full bathroom home is MOVE IN READY. The large open concept family room and kitchen area has a fireplace for cozy evenings in the fall and winter and a ceiling fan to help cool in the summer. This area includes a skylight to gather more natural light for this home. The three bedrooms have ceiling fans also. The two bathrooms have double sinks in both; the Master bathroom has a shower and the other bathroom has a tub and shower. There is a laundry area in the home with outlets for a washer and dryer. An added feature is the covered outdoor patio that that has a ceiling fan. There is a 2 car garage and landscaping in the front and back yards. This home is close to many parks, including Bidwell Park and Wildwood Park. Schools and shopping are also nearby, For easy commuting, Hwy. 99, 32, 191, and 70 are near by. Come and see this charming northern CA home.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "2507 Tuolumne Dr",
        "street": "2507 Tuolumne Dr",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1597,
        "year_built": 1994,
        "days_on_mls": 1,
        "list_price": 470000,
        "list_date": "2025-01-29",
        "assessed_value": 326997,
        "estimated_value": 473900,
        "tax": 3702,
        "tax_history": [
            {
            "year": 2023,
            "tax": 3702,
            "assessment": {
                "building": 184824,
                "land": 142173,
                "total": 326997
            }
            },
            {
            "year": 2022,
            "tax": 3644,
            "assessment": {
                "building": 181200,
                "land": 139386,
                "total": 320586
            }
            },
            {
            "year": 2021,
            "tax": 3576,
            "assessment": {
                "building": 177648,
                "land": 136653,
                "total": 314301
            }
            },
            {
            "year": 2020,
            "tax": 3567,
            "assessment": {
                "building": 175827,
                "land": 135252,
                "total": 311079
            }
            },
            {
            "year": 2019,
            "tax": 3503,
            "assessment": {
                "building": 172380,
                "land": 132600,
                "total": 304980
            }
            },
            {
            "year": 2018,
            "tax": 3407,
            "assessment": {
                "building": 169000,
                "land": 130000,
                "total": 299000
            }
            },
            {
            "year": 2017,
            "tax": 2010,
            "assessment": {
                "building": 107924,
                "land": 67533,
                "total": 175457
            }
            },
            {
            "year": 2016,
            "tax": 1870,
            "assessment": {
                "building": 105808,
                "land": 66209,
                "total": 172017
            }
            },
            {
            "year": 2015,
            "tax": 1847,
            "assessment": {
                "building": 104219,
                "land": 65215,
                "total": 169434
            }
            },
            {
            "year": 2014,
            "tax": 1826,
            "assessment": {
                "building": 102178,
                "land": 63938,
                "total": 166116
            }
            },
            {
            "year": 2013,
            "tax": 1848,
            "assessment": {
                "building": 101717,
                "land": 63650,
                "total": 165367
            }
            },
            {
            "year": 2012,
            "tax": 1744,
            "assessment": {
                "building": 99723,
                "land": 62402,
                "total": 162125
            }
            },
            {
            "year": 2010,
            "tax": 1718,
            "assessment": {
                "building": 97768,
                "land": 61179,
                "total": 158947
            }
            },
            {
            "year": 2009,
            "tax": 1736,
            "assessment": {
                "building": 97038,
                "land": 60722,
                "total": 157760
            }
            },
            {
            "year": 2008,
            "tax": 1666,
            "assessment": {
                "building": 95362,
                "land": 59674,
                "total": 155036
            }
            },
            {
            "year": 2007,
            "tax": 1630,
            "assessment": {
                "building": 93493,
                "land": 58504,
                "total": 151997
            }
            }
        ],
        "lot_sqft": 6098,
        "price_per_sqft": 294,
        "latitude": 39.762197,
        "longitude": -121.807078,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/da7d1eb77e3365db8189e80bd79947d5l-m868079187od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2800
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/767-Bridlewood-Ct_Chico_CA_95926_M20411-33615",
        "property_id": "2041133615",
        "listing_id": "2977652380",
        "mls": "MRCA",
        "mls_id": "SN25006014",
        "status": "FOR_SALE",
        "text": "Welcome to your dream home in one of Chico's most desirable west-side neighborhoods! Nestled at the end of the cul-de-sac, this stunning property offers privacy, charm, and a lifestyle of luxury. Sitting on a large lot, this home features OWNED SOLAR, ensuring energy efficiency and significant savings. The backyard is a true oasis, boasting a stunning POOL with a pool heater, perfect for year-round enjoyment. Surrounding the pool, youll find lush landscaping and a variety of fruit trees, including lemon, orange, pomegranate, grape vines, and so much more, a gardener's delight! Inside, the timeless interior exudes sophistication with high ceilings adorned with beautiful beams and a layout designed for both comfort and style. The chefs kitchen is a culinary masterpiece, equipped with premium appliances, ample counter space, and a flow ideal for entertaining. Spacious bedrooms throughout that provide plenty of room for everyone. The luxurious master suite is your very own private retreat! It features a large walk-in closet and a spa-like bathroom complete with a soaking tub for ultimate relaxation. Step outside to the backyard that is perfect for entertaining, whether you're hosting poolside gatherings, enjoying a meal under the stars, or simply relaxing in the serene setting. Dont miss this exceptional home that truly has it all!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "767 Bridlewood Ct",
        "street": "767 Bridlewood Ct",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 1,
        "sqft": 2355,
        "year_built": 1984,
        "days_on_mls": 3,
        "list_price": 775000,
        "list_date": "2025-01-27",
        "assessed_value": 471449,
        "estimated_value": 732417,
        "tax": 5185,
        "tax_history": [
            {
            "year": 2023,
            "tax": 5185,
            "assessment": {
                "building": 310167,
                "land": 161282,
                "total": 471449
            }
            },
            {
            "year": 2022,
            "tax": 5101,
            "assessment": {
                "building": 304086,
                "land": 158120,
                "total": 462206
            }
            },
            {
            "year": 2021,
            "tax": 5004,
            "assessment": {
                "building": 298124,
                "land": 155020,
                "total": 453144
            }
            },
            {
            "year": 2020,
            "tax": 4989,
            "assessment": {
                "building": 295068,
                "land": 153431,
                "total": 448499
            }
            },
            {
            "year": 2019,
            "tax": 4897,
            "assessment": {
                "building": 289283,
                "land": 150423,
                "total": 439706
            }
            },
            {
            "year": 2018,
            "tax": 4806,
            "assessment": {
                "building": 283611,
                "land": 147474,
                "total": 431085
            }
            },
            {
            "year": 2017,
            "tax": 4715,
            "assessment": {
                "building": 278050,
                "land": 144583,
                "total": 422633
            }
            },
            {
            "year": 2016,
            "tax": 4303,
            "assessment": {
                "building": 272599,
                "land": 141749,
                "total": 414348
            }
            },
            {
            "year": 2015,
            "tax": 4302,
            "assessment": {
                "building": 268505,
                "land": 139620,
                "total": 408125
            }
            },
            {
            "year": 2014,
            "tax": 3837,
            "assessment": {
                "building": 245000,
                "land": 120000,
                "total": 365000
            }
            },
            {
            "year": 2013,
            "tax": 3858,
            "assessment": {
                "building": 250000,
                "land": 110000,
                "total": 360000
            }
            },
            {
            "year": 2012,
            "tax": 3707,
            "assessment": {
                "building": 250000,
                "land": 110000,
                "total": 360000
            }
            },
            {
            "year": 2010,
            "tax": 3980,
            "assessment": {
                "building": 251882,
                "land": 130978,
                "total": 382860
            }
            },
            {
            "year": 2009,
            "tax": 2877,
            "assessment": {
                "building": 250000,
                "land": 130000,
                "total": 380000
            }
            },
            {
            "year": 2008,
            "tax": 2778,
            "assessment": {
                "building": 203888,
                "land": 62658,
                "total": 266546
            }
            },
            {
            "year": 2007,
            "tax": 2702,
            "assessment": {
                "building": 199891,
                "land": 61430,
                "total": 261321
            }
            }
        ],
        "lot_sqft": 12197,
        "price_per_sqft": 329,
        "latitude": 39.727803,
        "longitude": -121.871175,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/2cca8fed9400ececac9f602de50d88ccl-m546445052od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1680
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1268-Arch-Way_Chico_CA_95973_M16737-99887",
        "property_id": "1673799887",
        "listing_id": "2977681828",
        "mls": "MRCA",
        "mls_id": "SN25006023",
        "status": "FOR_SALE",
        "text": "Welcome to your dream home with a beautifully updated outdoor space, perfect for entertaining! The pool shines with new gunite and tiles, and all new pool equipment creating a relaxing retreat. The backyard also features a pergola, outdoor kitchen setup, and a gas-plumbed fireplace for effortless gatherings. Inside, enjoy a well-maintained home with modern updates, including sleek quartz countertops in the renovated kitchen. This property seamlessly combines indoor comfort with outdoor living. Don't miss your chance to call it home!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "1268 Arch Way",
        "street": "1268 Arch Way",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1810,
        "year_built": 2006,
        "days_on_mls": 2,
        "list_price": 575000,
        "list_date": "2025-01-28",
        "assessed_value": 500000,
        "estimated_value": 533000,
        "tax": 5534,
        "tax_history": [
            {
            "year": 2023,
            "tax": 5534,
            "assessment": {
                "building": 330000,
                "land": 170000,
                "total": 500000
            }
            },
            {
            "year": 2022,
            "tax": 5482,
            "assessment": {
                "building": 320000,
                "land": 170000,
                "total": 490000
            }
            },
            {
            "year": 2021,
            "tax": 4945,
            "assessment": {
                "building": 285000,
                "land": 160000,
                "total": 445000
            }
            },
            {
            "year": 2020,
            "tax": 4843,
            "assessment": {
                "building": 270000,
                "land": 160000,
                "total": 430000
            }
            },
            {
            "year": 2019,
            "tax": 4845,
            "assessment": {
                "building": 270000,
                "land": 160000,
                "total": 430000
            }
            },
            {
            "year": 2018,
            "tax": 3856,
            "assessment": {
                "building": 220000,
                "land": 125000,
                "total": 345000
            }
            },
            {
            "year": 2017,
            "tax": 3933,
            "assessment": {
                "building": 220000,
                "land": 130000,
                "total": 350000
            }
            },
            {
            "year": 2016,
            "tax": 3375,
            "assessment": {
                "building": 195000,
                "land": 125000,
                "total": 320000
            }
            },
            {
            "year": 2015,
            "tax": 3199,
            "assessment": {
                "building": 190000,
                "land": 115000,
                "total": 305000
            }
            },
            {
            "year": 2014,
            "tax": 3084,
            "assessment": {
                "building": 180000,
                "land": 105000,
                "total": 285000
            }
            },
            {
            "year": 2013,
            "tax": 2871,
            "assessment": {
                "building": 166000,
                "land": 94000,
                "total": 260000
            }
            },
            {
            "year": 2012,
            "tax": 2642,
            "assessment": {
                "building": 158000,
                "land": 94000,
                "total": 252000
            }
            },
            {
            "year": 2010,
            "tax": 2944,
            "assessment": {
                "building": 198000,
                "land": 105000,
                "total": 303000
            }
            },
            {
            "year": 2009,
            "tax": 3245,
            "assessment": {
                "building": 170000,
                "land": 105000,
                "total": 275000
            }
            },
            {
            "year": 2008,
            "tax": 4040,
            "assessment": {
                "building": 223380,
                "land": 163200,
                "total": 386580
            }
            },
            {
            "year": 2007,
            "tax": 4042,
            "assessment": {
                "building": 219000,
                "land": 160000,
                "total": 379000
            }
            }
        ],
        "lot_sqft": 7405,
        "price_per_sqft": 318,
        "latitude": 39.764864,
        "longitude": -121.819288,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/383907882c1ecb3b18476b6d8f69835al-m356944829od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4409
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1444-Warner-St_Chico_CA_95926_M20390-43388",
        "property_id": "2039043388",
        "listing_id": "2977591993",
        "mls": "MRCA",
        "mls_id": "SN25017653",
        "status": "FOR_SALE",
        "text": "Welcome to 1444 & 1448 Warner St, a charming triplex that offers an incredible rental opportunity just blocks from Chico State University and Downtown Chico. Whether you're looking to invest in student housing or a versatile income property, this triplex is packed with potential. The front house (1444 Warner St) is a darling 2-bedroom single-story home brimming with classic Chico charm. Inside, you'll find original hardwood floors, ceiling fans in every room, and a perfect balance of character and modern conveniences, including central HVAC. The kitchen features a convenient laundry area with extra storage space, and both bedrooms are generously sized, with one offering a walk-in closet. The front house also includes an off-street parking spot for added tenant convenience. Behind the front house sits the stacked duplex (1448 Warner St), featuring two spacious units, each with 4 bedrooms and 2 bathrooms. Unit A (downstairs) offers laminate flooring, and a fully enclosed private patio for outdoor enjoyment, while Unit B (upstairs) boasts updates like newer laminate flooring and a unique French door feature that allows two bedrooms to combine into one large primary suite. Both duplex units share access to an on-site coin-operated laundry room, generating additional income for the owner. The property also has alley access and a private parking lot with ample on-site parking for tenants. Located in the desirable Avenues, this property is just minutes from Chico State University, Downtown Chico, and a variety of local eateries and amenities. With its unbeatable location, strong rental history, and incredible versatility, this triplex is a fantastic addition to any portfolio. Don't miss your chance to own this amazing income-producing property - schedule your private showing today!",
        "style": "MULTI_FAMILY",
        "full_street_line": "1444 Warner St",
        "street": "1444 Warner St",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 10,
        "full_baths": 5,
        "half_baths": 0,
        "sqft": 3080,
        "year_built": 1983,
        "days_on_mls": 5,
        "list_price": 579000,
        "list_date": "2025-01-25",
        "assessed_value": 531815,
        "estimated_value": 612600,
        "tax": 5930,
        "tax_history": [
            {
            "year": 2023,
            "tax": 5930,
            "assessment": {
                "building": 369668,
                "land": 162147,
                "total": 531815
            }
            },
            {
            "year": 2022,
            "tax": 4816,
            "assessment": {
                "building": 273858,
                "land": 156171,
                "total": 430029
            }
            },
            {
            "year": 2021,
            "tax": 4725,
            "assessment": {
                "building": 268489,
                "land": 153109,
                "total": 421598
            }
            },
            {
            "year": 2020,
            "tax": 4712,
            "assessment": {
                "building": 265736,
                "land": 151540,
                "total": 417276
            }
            },
            {
            "year": 2019,
            "tax": 4626,
            "assessment": {
                "building": 260526,
                "land": 148569,
                "total": 409095
            }
            },
            {
            "year": 2018,
            "tax": 4542,
            "assessment": {
                "building": 255418,
                "land": 145656,
                "total": 401074
            }
            },
            {
            "year": 2017,
            "tax": 4449,
            "assessment": {
                "building": 250410,
                "land": 142800,
                "total": 393210
            }
            },
            {
            "year": 2016,
            "tax": 4061,
            "assessment": {
                "building": 245500,
                "land": 140000,
                "total": 385500
            }
            },
            {
            "year": 2015,
            "tax": 2603,
            "assessment": {
                "building": 172639,
                "land": 70330,
                "total": 242969
            }
            },
            {
            "year": 2014,
            "tax": 2541,
            "assessment": {
                "building": 169258,
                "land": 68953,
                "total": 238211
            }
            },
            {
            "year": 2013,
            "tax": 2571,
            "assessment": {
                "building": 168494,
                "land": 68642,
                "total": 237136
            }
            },
            {
            "year": 2012,
            "tax": 2422,
            "assessment": {
                "building": 165191,
                "land": 67297,
                "total": 232488
            }
            },
            {
            "year": 2010,
            "tax": 2396,
            "assessment": {
                "building": 161952,
                "land": 65978,
                "total": 227930
            }
            },
            {
            "year": 2009,
            "tax": 2438,
            "assessment": {
                "building": 160742,
                "land": 65485,
                "total": 226227
            }
            },
            {
            "year": 2008,
            "tax": 2354,
            "assessment": {
                "building": 157965,
                "land": 64354,
                "total": 222319
            }
            },
            {
            "year": 2007,
            "tax": 2290,
            "assessment": {
                "building": 154868,
                "land": 63093,
                "total": 217961
            }
            }
        ],
        "lot_sqft": 8712,
        "price_per_sqft": 188,
        "latitude": 39.738788,
        "longitude": -121.855628,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/56cd7bc49c0ca24a93c1db5ce429f042l-m1414570067od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4453
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1559-Champlain-Way_Chico_CA_95973_M20938-30409",
        "property_id": "2093830409",
        "listing_id": "2977542533",
        "mls": "MRCA",
        "mls_id": "SN25016235",
        "status": "CONTINGENT",
        "text": "Nestled in the desirable Hancock Park neighborhood, this stunning home offers the perfect blend of classic charm and modern convenience. Boasting a spacious split floor plan, the home features 3 bedrooms, 2 bathrooms, and an array of upgraded amenities designed for comfort and style. Step into your private outdoor sanctuary, complete with a large yard featuring a separate irrigated garden area, tranquil fountain, and a covered pergola patio perfect for entertaining. Tall fencing ensures privacy, creating an ideal setting to relax and unwind. The heart of the home is the gourmet kitchen, showcasing granite countertops, sleek white cabinetry, and stainless steel Whirlpool appliances. A cozy dining nook overlooks the backyard, with a large sliding glass door that floods the space with natural light. The inviting living room features vaulted ceilings, a gas fireplace, and abundant natural light, offering a warm and welcoming atmosphere. The spacious master bedroom boasts vaulted ceilings, a large slider to the backyard, and an attached spa-like bathroom with dual sinks, a soaking tub, a separate walk-in shower, and a generous walk-in closet. Enjoy the convenience of new LVP flooring, an oversized two-car garage, and indoor laundry with a utility sink and Whirlpool washer and dryer. This smart home includes owned solar, a programmable HVAC system, sprinkler controls, and Ring camera for added peace of mind. Located within walking distance to parks, trails, and the serene Bidwell Park, this home is also just minutes from shopping and restaurants, combining the best of nature and city living. Dont miss the chance to call this exceptional Hancock Park property your new home!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "1559 Champlain Way",
        "street": "1559 Champlain Way",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1679,
        "year_built": 2001,
        "days_on_mls": 7,
        "list_price": 510000,
        "list_date": "2025-01-23",
        "assessed_value": 453055,
        "estimated_value": 535975,
        "tax": 5675,
        "tax_history": [
            {
            "year": 2023,
            "tax": 5675,
            "assessment": {
                "building": 274356,
                "land": 178699,
                "total": 453055
            }
            },
            {
            "year": 2022,
            "tax": 5440,
            "assessment": {
                "building": 268977,
                "land": 175196,
                "total": 444173
            }
            },
            {
            "year": 2021,
            "tax": 5362,
            "assessment": {
                "building": 263703,
                "land": 171761,
                "total": 435464
            }
            },
            {
            "year": 2020,
            "tax": 5216,
            "assessment": {
                "building": 261000,
                "land": 170000,
                "total": 431000
            }
            },
            {
            "year": 2019,
            "tax": 4999,
            "assessment": {
                "building": 255000,
                "land": 160000,
                "total": 415000
            }
            },
            {
            "year": 2018,
            "tax": 4186,
            "assessment": {
                "building": 215000,
                "land": 135000,
                "total": 350000
            }
            },
            {
            "year": 2017,
            "tax": 4214,
            "assessment": {
                "building": 210000,
                "land": 140000,
                "total": 350000
            }
            },
            {
            "year": 2016,
            "tax": 3625,
            "assessment": {
                "building": 195000,
                "land": 130000,
                "total": 325000
            }
            },
            {
            "year": 2015,
            "tax": 3558,
            "assessment": {
                "building": 195000,
                "land": 120000,
                "total": 315000
            }
            },
            {
            "year": 2014,
            "tax": 3519,
            "assessment": {
                "building": 195000,
                "land": 115000,
                "total": 310000
            }
            },
            {
            "year": 2013,
            "tax": 3120,
            "assessment": {
                "building": 170000,
                "land": 105000,
                "total": 275000
            }
            },
            {
            "year": 2012,
            "tax": 2823,
            "assessment": {
                "building": 156000,
                "land": 96000,
                "total": 252000
            }
            },
            {
            "year": 2010,
            "tax": 3064,
            "assessment": {
                "building": 170000,
                "land": 105000,
                "total": 275000
            }
            },
            {
            "year": 2009,
            "tax": 3565,
            "assessment": {
                "building": 170000,
                "land": 105000,
                "total": 275000
            }
            },
            {
            "year": 2008,
            "tax": 4152,
            "assessment": {
                "building": 208080,
                "land": 166464,
                "total": 374544
            }
            },
            {
            "year": 2007,
            "tax": 4106,
            "assessment": {
                "building": 204000,
                "land": 163200,
                "total": 367200
            }
            }
        ],
        "lot_sqft": 6970,
        "price_per_sqft": 304,
        "latitude": 39.76965,
        "longitude": -121.814189,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/fd66e7d92e279ff324f74c9130ae5a72l-m3753377902od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3770
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/3294-Sloat-Run_Chico_CA_95973_M14593-07789",
        "property_id": "1459307789",
        "listing_id": "2977546911",
        "mls": "MRCA",
        "mls_id": "SN25013923",
        "status": "PENDING",
        "text": "Welcome to this stunning, modern home built in 2019, nestled at the back of the highly sought-after Meadowbrook Subdivision with Hartley park just a block and a half away.. Offering breathtaking sunset views, this west-facing property boasts an enviable location with no homes blocking your sightlinejust the serene levee and Chico's Greenlinek top and bar seating, striking pendant lighting, and a gorgeous tile backsplash. New stainless steel appliances, including a gas range, recessed lighting, and a pantry, complete this chefs dream kitchen. The light-filled living room features large windows, a sliding door to the covered patio, updated lighting, surround sound and an accent wood wall that adds a touch of warmth and charm. This home is as functional as it is beautiful, with a dedicated indoor laundry room, quietcool whole house fan and a versatile fourth bedroom, perfectly suited as a home office, guest room, or private retreat. The main bathroom with it's marble vanity and floor-to-ceiling tile is sure to attract attention from visiting guest. The luxurious primary suite includes a walk-in closet, coffered ceiling with fan, and a well-appointed en-suite bathroom featuring double sinks, a marble countertop, and a sleek glass-enclosed step-in shower. Step outside to your private oasis, where olive trees and white roses line the yard, a covered patio, a pergola seating area covered in wisteria, and a charming sandbox play area. The finished garage features painted walls and durable epoxy flooring, adding both functionality and style. All this home needs is you! Move in, relax, and enjoy everything this remarkable property has to offer.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "3294 Sloat Run",
        "street": "3294 Sloat Run",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 4,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1561,
        "year_built": 2019,
        "days_on_mls": 6,
        "list_price": 525000,
        "list_date": "2025-01-24",
        "assessed_value": 500000,
        "estimated_value": 513000,
        "tax": 5877,
        "tax_history": [
            {
            "year": 2023,
            "tax": 5877,
            "assessment": {
                "building": 325000,
                "land": 175000,
                "total": 500000
            }
            },
            {
            "year": 2022,
            "tax": 4902,
            "assessment": {
                "building": 293711,
                "land": 151422,
                "total": 445133
            }
            },
            {
            "year": 2021,
            "tax": 4808,
            "assessment": {
                "building": 287952,
                "land": 148453,
                "total": 436405
            }
            },
            {
            "year": 2020,
            "tax": 4809,
            "assessment": {
                "building": 285000,
                "land": 146931,
                "total": 431931
            }
            },
            {
            "year": 2019,
            "tax": 1091,
            "assessment": {
                "building": null,
                "land": 96580,
                "total": 96580
            }
            },
            {
            "year": 2018,
            "tax": 1071,
            "assessment": {
                "building": null,
                "land": 94687,
                "total": 94687
            }
            }
        ],
        "lot_sqft": 4792,
        "price_per_sqft": 336,
        "latitude": 39.773295,
        "longitude": -121.894144,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/af44244ec1272603687bc5553c51a43bl-m2783365941od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4000
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/390-White-Ave_Chico_CA_95926_M20469-06502",
        "property_id": "2046906502",
        "listing_id": "2977505182",
        "mls": "MRCA",
        "mls_id": "SN25015903",
        "status": "PENDING",
        "text": "Welcome to your next great investment! This centrally located four-unit property offers incredible income potential and peace of mind, even with a unit vacant. Each unit is approximately 900 sq. ft, featuring 2 bedrooms and 1 bathroom, and rents for approximately $1, 150 per month. With rental income that can cover your mortgage even if one unit is unoccupied, this property is a smart additional to any portfolio! Unit 1 has been recently updated with laminate wood flooring in the kitchen, fresh interior paint, plush carpet, and an updated bathroom featuring a brand-new shower/tub. The other units also feature updates throughout. Beyond rental income, this property includes an on-site laundry room with coin-operated machines, providing an additional revenue stream. On-site parking is available for all tenants, offering added convenience. This property is connected to City Sewer, features a newer roof, and has a history of long-term tenants. Centrally located with easy freeway access, close to schools, shopping and local amenities, this property is a gem that offers both convenience and profitability. Whether you're a seasoned investor or looking to begin building your portfolio, this 4-plex offers a rare opportunity in the heart of Chico! Schedule your showing today and start earning!",
        "style": "MULTI_FAMILY",
        "full_street_line": "390 White Ave",
        "street": "390 White Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 8,
        "full_baths": 4,
        "half_baths": 0,
        "sqft": 3484,
        "year_built": 1979,
        "days_on_mls": 8,
        "list_price": 525000,
        "list_date": "2025-01-22",
        "assessed_value": 247313,
        "estimated_value": 644271,
        "tax": 2795,
        "tax_history": [
            {
            "year": 2023,
            "tax": 2795,
            "assessment": {
                "building": 156530,
                "land": 90783,
                "total": 247313
            }
            },
            {
            "year": 2022,
            "tax": 2749,
            "assessment": {
                "building": 153461,
                "land": 89003,
                "total": 242464
            }
            },
            {
            "year": 2021,
            "tax": 2698,
            "assessment": {
                "building": 150452,
                "land": 87258,
                "total": 237710
            }
            },
            {
            "year": 2020,
            "tax": 2691,
            "assessment": {
                "building": 148910,
                "land": 86364,
                "total": 235274
            }
            },
            {
            "year": 2019,
            "tax": 2643,
            "assessment": {
                "building": 145991,
                "land": 84671,
                "total": 230662
            }
            },
            {
            "year": 2018,
            "tax": 2595,
            "assessment": {
                "building": 143129,
                "land": 83011,
                "total": 226140
            }
            },
            {
            "year": 2017,
            "tax": 2542,
            "assessment": {
                "building": 140323,
                "land": 81384,
                "total": 221707
            }
            },
            {
            "year": 2016,
            "tax": 2321,
            "assessment": {
                "building": 137572,
                "land": 79789,
                "total": 217361
            }
            },
            {
            "year": 2015,
            "tax": 2321,
            "assessment": {
                "building": 135506,
                "land": 78591,
                "total": 214097
            }
            },
            {
            "year": 2014,
            "tax": 2279,
            "assessment": {
                "building": 132852,
                "land": 77052,
                "total": 209904
            }
            },
            {
            "year": 2013,
            "tax": 2300,
            "assessment": {
                "building": 132252,
                "land": 76704,
                "total": 208956
            }
            },
            {
            "year": 2012,
            "tax": 2168,
            "assessment": {
                "building": 129659,
                "land": 75200,
                "total": 204859
            }
            },
            {
            "year": 2010,
            "tax": 2145,
            "assessment": {
                "building": 127117,
                "land": 73726,
                "total": 200843
            }
            },
            {
            "year": 2009,
            "tax": 2182,
            "assessment": {
                "building": 126167,
                "land": 73175,
                "total": 201342
            }
            },
            {
            "year": 2008,
            "tax": 2108,
            "assessment": {
                "building": 123988,
                "land": 71911,
                "total": 197899
            }
            },
            {
            "year": 2007,
            "tax": 2051,
            "assessment": {
                "building": 121557,
                "land": 70501,
                "total": 194058
            }
            }
        ],
        "lot_sqft": 12632,
        "price_per_sqft": 151,
        "latitude": 39.758563,
        "longitude": -121.854947,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/23acbcdb5185a9203f70b1ecbebc579dl-m237890189od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3632
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/235-W-1st-Ave_Chico_CA_95926_M28252-41908",
        "property_id": "2825241908",
        "listing_id": "2977563038",
        "mls": "MRCA",
        "mls_id": "SN25014851",
        "status": "FOR_SALE",
        "text": "Step into a storybook world with this enchanting three-bedroom, one-bath cottage, complete with an oversized bonus room. Nestled in the heart of Chicos cherished Avenues, this home is perfectly situated just a short stroll from Chico High, Chico State University, and Enloe Medical Center. This home radiates timeless charm, from its original plastered walls and soaring arched ceiling to the intricate woodwork and gleaming hardwood floors. Sunlight shines through the oversized front picture window, casting a golden glow on every magical detail within. Once a beloved short-term rental, this property has welcomed guests from near and far, and now its ready to embrace its next chapter with you. Imagine cozy evenings, rejuvenating mornings, and endless inspiration in this one-of-a-kind property. The detached garage offers endless possibilitiesstudio, workshop, or simply a haven for your treasures. With the citys best offerings just a bike ride awaySaturday morning Farmers Market, stylish boutiques, and an array of eateriesthis is not just a home; its a lifestyle. Let your cottage dreams unfold in this whimsical retreat. Dont just visit a homediscover a fairytale.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "235 W 1st Ave",
        "street": "235 W 1st Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 3,
        "full_baths": 1,
        "half_baths": 0,
        "sqft": 1861,
        "year_built": 1931,
        "days_on_mls": 6,
        "list_price": 529000,
        "list_date": "2025-01-24",
        "assessed_value": 318589,
        "estimated_value": 508390,
        "tax": 3554,
        "tax_history": [
            {
            "year": 2023,
            "tax": 3554,
            "assessment": {
                "building": 176362,
                "land": 142227,
                "total": 318589
            }
            },
            {
            "year": 2022,
            "tax": 3497,
            "assessment": {
                "building": 172904,
                "land": 139439,
                "total": 312343
            }
            },
            {
            "year": 2021,
            "tax": 3432,
            "assessment": {
                "building": 169514,
                "land": 136705,
                "total": 306219
            }
            },
            {
            "year": 2020,
            "tax": 3422,
            "assessment": {
                "building": 167776,
                "land": 135304,
                "total": 303080
            }
            },
            {
            "year": 2019,
            "tax": 3360,
            "assessment": {
                "building": 164487,
                "land": 132651,
                "total": 297138
            }
            },
            {
            "year": 2018,
            "tax": 3298,
            "assessment": {
                "building": 161262,
                "land": 130050,
                "total": 291312
            }
            },
            {
            "year": 2017,
            "tax": 3231,
            "assessment": {
                "building": 158100,
                "land": 127500,
                "total": 285600
            }
            },
            {
            "year": 2016,
            "tax": 2949,
            "assessment": {
                "building": 155000,
                "land": 125000,
                "total": 280000
            }
            },
            {
            "year": 2015,
            "tax": 626,
            "assessment": {
                "building": 50487,
                "land": 14350,
                "total": 64837
            }
            },
            {
            "year": 2014,
            "tax": 609,
            "assessment": {
                "building": 49499,
                "land": 14069,
                "total": 63568
            }
            },
            {
            "year": 2013,
            "tax": 610,
            "assessment": {
                "building": 49276,
                "land": 14006,
                "total": 63282
            }
            },
            {
            "year": 2012,
            "tax": 573,
            "assessment": {
                "building": 48310,
                "land": 13732,
                "total": 62042
            }
            },
            {
            "year": 2010,
            "tax": 565,
            "assessment": {
                "building": 47363,
                "land": 13463,
                "total": 60826
            }
            },
            {
            "year": 2009,
            "tax": 575,
            "assessment": {
                "building": 47010,
                "land": 13363,
                "total": 60373
            }
            },
            {
            "year": 2008,
            "tax": 554,
            "assessment": {
                "building": 46199,
                "land": 13133,
                "total": 59332
            }
            },
            {
            "year": 2007,
            "tax": 537,
            "assessment": {
                "building": 45294,
                "land": 12876,
                "total": 58170
            }
            }
        ],
        "lot_sqft": 6098,
        "price_per_sqft": 284,
        "latitude": 39.736429,
        "longitude": -121.848178,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/c454d0c987ea58abb1710164a2f3e1d7l-m2502001417od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2416
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/13804-Bosc-Dr_Chico_CA_95973_M16888-00575",
        "property_id": "1688800575",
        "listing_id": "2977592085",
        "mls": "MRCA",
        "mls_id": "SN25017449",
        "status": "FOR_SALE",
        "text": "Come see this beautiful North Chico home located in the Autumn Park subdivision! As you drive up, you'll notice the well manicured yard with mature landscape and the timeless charming front porch. When entering the home, you're immediately drawn to the light and bright living room that has lots of windows for natural light, white built-in cabinetry, a wood burning fireplace, crown moulding, and tall ceilings. The kitchen around the corner has been updated with granite counters, new light fixtures, cork flooring, and stainless steal appliances. There is a spacious walk-in pantry close to the dining room for any dinner items you may have forgotten! There is a lovely sitting room off the dining with French doors that is perfect for the after dinner coffee or wine. Leading down the hallway, you'll find two spacious bedrooms and a bathroom, as well as the master suite. The master has a vaulted ceiling, walk-in closet, en suite bathroom with a large tub, dual sink vanity, and second closet. On the other side of the home, there is the fourth bedroom, guest bathroom, and the laundry room. In the backyard, you'll fall in love with the sparkling pool and large patio that is perfect for upcoming summer entertaining. There are several producing fruit trees and plenty of space for outdoor activities! Other notable features include an OWNED 13.87 kW solar system, new glass roll-up garage doors, epoxy garage floor, a ductless mini split in the garage, a new pressure tank for the well, and a custom gate with RV parking potential. This property has so much to offer and is ready for you to call home!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "13804 Bosc Dr",
        "street": "13804 Bosc Dr",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 4,
        "full_baths": 3,
        "half_baths": 0,
        "sqft": 2839,
        "year_built": 2001,
        "days_on_mls": 5,
        "list_price": 1025000,
        "list_date": "2025-01-25",
        "assessed_value": 659834,
        "estimated_value": 946000,
        "tax": 7933,
        "tax_history": [
            {
            "year": 2023,
            "tax": 7933,
            "assessment": {
                "building": 471911,
                "land": 187923,
                "total": 659834
            }
            },
            {
            "year": 2022,
            "tax": 7737,
            "assessment": {
                "building": 462658,
                "land": 184239,
                "total": 646897
            }
            },
            {
            "year": 2021,
            "tax": 7445,
            "assessment": {
                "building": 453587,
                "land": 180627,
                "total": 634214
            }
            },
            {
            "year": 2020,
            "tax": 7424,
            "assessment": {
                "building": 448937,
                "land": 178775,
                "total": 627712
            }
            },
            {
            "year": 2019,
            "tax": 7296,
            "assessment": {
                "building": 440135,
                "land": 175270,
                "total": 615405
            }
            },
            {
            "year": 2018,
            "tax": 7168,
            "assessment": {
                "building": 431505,
                "land": 171834,
                "total": 603339
            }
            },
            {
            "year": 2017,
            "tax": 7045,
            "assessment": {
                "building": 423045,
                "land": 168465,
                "total": 591510
            }
            },
            {
            "year": 2016,
            "tax": 6455,
            "assessment": {
                "building": 414750,
                "land": 165162,
                "total": 579912
            }
            },
            {
            "year": 2015,
            "tax": 6121,
            "assessment": {
                "building": 380000,
                "land": 160000,
                "total": 540000
            }
            },
            {
            "year": 2014,
            "tax": 5751,
            "assessment": {
                "building": 380000,
                "land": 130000,
                "total": 510000
            }
            },
            {
            "year": 2013,
            "tax": 5860,
            "assessment": {
                "building": 380000,
                "land": 130000,
                "total": 510000
            }
            },
            {
            "year": 2012,
            "tax": 5646,
            "assessment": {
                "building": 380000,
                "land": 130000,
                "total": 510000
            }
            },
            {
            "year": 2010,
            "tax": 6037,
            "assessment": {
                "building": 383228,
                "land": 152611,
                "total": 535839
            }
            },
            {
            "year": 2009,
            "tax": 6137,
            "assessment": {
                "building": 380364,
                "land": 151471,
                "total": 531835
            }
            },
            {
            "year": 2008,
            "tax": 6111,
            "assessment": {
                "building": 373793,
                "land": 148854,
                "total": 522647
            }
            },
            {
            "year": 2007,
            "tax": 5575,
            "assessment": {
                "building": 366464,
                "land": 145936,
                "total": 512400
            }
            }
        ],
        "lot_sqft": 38333,
        "price_per_sqft": 361,
        "latitude": 39.802333,
        "longitude": -121.895151,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/657228be089a3d92cd33a26a1cffbe29l-m1027698234od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4756
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/11-Rose-Garden-Ct_Chico_CA_95973_M14563-63779",
        "property_id": "1456363779",
        "listing_id": "2977491743",
        "mls": "MRCA",
        "mls_id": "SN25014596",
        "status": "FOR_SALE",
        "text": "PRISTINE HOME located in Sanford Manor Subdivision is a craftsman style home built by Larry Porter Construction located on a quiet cul-de-sac, country feel while being close to local shopping. The 3, 183 sq. ft. home is situated on one professionally landscaped acre. Two master sized bedrooms and two additional spacious bedrooms. The fifth room for use as an office/sitting room. Large laundry room and two generous storage closets. The ensuite master bathroom provides a place to wind down with a luxurious bath or large walk-in shower with dual shower heads. Two additional full baths. Attention to detail throughout with crown molding, transom windows above interior bedroom doors, varied 9-to-12-foot ceilings. The modern kitchen dazzles with subway tile backsplash, undercounter/interior cabinet lights, suede quartz countertops, a large quartz island w/cabinets, top of the line stainless steel Kitchen Aid appliances. Backyard has areas that provide space to gather, play, or retreat. There is a 5 raised bed garden, apple and peach trees, LawnMaster pergola, Sundance hot tub, fire pit area, a large dog enclosure, 10 x 12 Tuff shed. Three car garage. Owned 9kW solar system.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "11 Rose Garden Ct",
        "street": "11 Rose Garden Ct",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 4,
        "full_baths": 3,
        "half_baths": 0,
        "sqft": 3183,
        "year_built": 2018,
        "days_on_mls": 8,
        "list_price": 1350000,
        "list_date": "2025-01-22",
        "assessed_value": 912734,
        "estimated_value": 1261900,
        "tax": 5280,
        "tax_history": [
            {
            "year": 2023,
            "tax": 5280,
            "assessment": {
                "building": 644686,
                "land": 268048,
                "total": 912734
            }
            },
            {
            "year": 2022,
            "tax": 10400,
            "assessment": {
                "building": 632046,
                "land": 262793,
                "total": 894839
            }
            },
            {
            "year": 2021,
            "tax": 10211,
            "assessment": {
                "building": 619653,
                "land": 257641,
                "total": 877294
            }
            },
            {
            "year": 2020,
            "tax": 10184,
            "assessment": {
                "building": 613300,
                "land": 255000,
                "total": 868300
            }
            },
            {
            "year": 2019,
            "tax": 9879,
            "assessment": {
                "building": 590000,
                "land": 250000,
                "total": 840000
            }
            },
            {
            "year": 2018,
            "tax": 2772,
            "assessment": {
                "building": null,
                "land": 210000,
                "total": 210000
            }
            },
            {
            "year": 2017,
            "tax": 1610,
            "assessment": {
                "building": null,
                "land": 107137,
                "total": 107137
            }
            }
        ],
        "lot_sqft": 32670,
        "price_per_sqft": 424,
        "latitude": 39.752065,
        "longitude": -121.882659,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/ede968e7aff53e1b022d37b3c0dfd26el-m692064937od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3660
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/2240-Notre-Dame-Blvd-Apt-5_Chico_CA_95928_M27529-08714",
        "property_id": "2752908714",
        "listing_id": "2977507207",
        "mls": "SCCA",
        "mls_id": "225007750",
        "status": "FOR_SALE",
        "text": "Super Cute and clean 2 Bedroom, 1 Bath condo for sale with a great south Chico location and easy freeway access. Experience the convenience of a location near shopping and transportation. located on the top level for even more privacy and beautiful balcony. Newer laminate flooring, big electric fireplace, newer stainless-steel appliances, light fixtures and bathroom vanity. Washer and dryer. HOA dues cover outside maintenance and landscaping, water, trash and sewer. Spacious laundry closet, outside storage and reserved parking spaces.",
        "style": "CONDOS",
        "full_street_line": "2240 Notre Dame Blvd Apt 5",
        "street": "2240 Notre Dame Blvd",
        "unit": "Apt 5",
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 2,
        "full_baths": 1,
        "half_baths": 0,
        "sqft": 864,
        "year_built": 1980,
        "days_on_mls": 7,
        "list_price": 177000,
        "list_date": "2025-01-23",
        "assessed_value": 178500,
        "estimated_value": 177038,
        "tax": 2016,
        "tax_history": [
            {
            "year": 2023,
            "tax": 2016,
            "assessment": {
                "building": 127500,
                "land": 51000,
                "total": 178500
            }
            },
            {
            "year": 2022,
            "tax": 1986,
            "assessment": {
                "building": 125000,
                "land": 50000,
                "total": 175000
            }
            },
            {
            "year": 2021,
            "tax": 697,
            "assessment": {
                "building": 45928,
                "land": 13910,
                "total": 59838
            }
            },
            {
            "year": 2020,
            "tax": 698,
            "assessment": {
                "building": 45458,
                "land": 13768,
                "total": 59226
            }
            },
            {
            "year": 2019,
            "tax": 688,
            "assessment": {
                "building": 44567,
                "land": 13499,
                "total": 58066
            }
            },
            {
            "year": 2018,
            "tax": 674,
            "assessment": {
                "building": 43694,
                "land": 13235,
                "total": 56929
            }
            },
            {
            "year": 2017,
            "tax": 657,
            "assessment": {
                "building": 42838,
                "land": 12976,
                "total": 55814
            }
            },
            {
            "year": 2016,
            "tax": 603,
            "assessment": {
                "building": 41999,
                "land": 12722,
                "total": 54721
            }
            },
            {
            "year": 2015,
            "tax": 602,
            "assessment": {
                "building": 41369,
                "land": 12531,
                "total": 53900
            }
            },
            {
            "year": 2014,
            "tax": 593,
            "assessment": {
                "building": 40559,
                "land": 12286,
                "total": 52845
            }
            },
            {
            "year": 2013,
            "tax": 598,
            "assessment": {
                "building": 40376,
                "land": 12231,
                "total": 52607
            }
            },
            {
            "year": 2012,
            "tax": 556,
            "assessment": {
                "building": 39585,
                "land": 11992,
                "total": 51577
            }
            },
            {
            "year": 2010,
            "tax": 544,
            "assessment": {
                "building": 38809,
                "land": 11757,
                "total": 50566
            }
            },
            {
            "year": 2009,
            "tax": 554,
            "assessment": {
                "building": 38519,
                "land": 11670,
                "total": 50189
            }
            },
            {
            "year": 2008,
            "tax": 547,
            "assessment": {
                "building": 37854,
                "land": 11469,
                "total": 49323
            }
            },
            {
            "year": 2007,
            "tax": 519,
            "assessment": {
                "building": 37112,
                "land": 11245,
                "total": 48357
            }
            }
        ],
        "lot_sqft": 871,
        "price_per_sqft": 205,
        "latitude": 39.722907,
        "longitude": -121.795915,
        "county": "Butte",
        "hoa_fee": 379,
        "nearby_schools": "Butte County Office Of Education School District, Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/977268effc60d25fa3ff9be50c581db5l-m1731112978od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1531
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/358-E-12th-St_Chico_CA_95928_M10195-83824",
        "property_id": "1019583824",
        "listing_id": "2977504810",
        "mls": "SCCA",
        "mls_id": "225007806",
        "status": "FOR_SALE",
        "text": "Are you in the market to purchase 2 charming homes on one lot in Chico? Then, you need to purchase this property. This property features 2 charming homes, the front home is a 2 bedroom 1.5 bath 928 sq. ft. home that was built in 1957. It has been recently remodeled with NEW exterior paint, NEW interior paint, NEW dual pane windows, NEW cabinets, NEW countertops, NEW appliances, NEW Flooring and a NEW updated downstairs bathroom. The back house is an adorable 3 bedroom 2 bathroom 800 sq. ft. ADU home that was built in 2022. Each home features their own privately fenced low maintenance yards, and separate utility meters. Don't miss your opportunity to purchase this property!",
        "style": "MULTI_FAMILY",
        "full_street_line": "358 E 12th St",
        "street": "358 E 12th St",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 1,
        "sqft": 928,
        "year_built": 1957,
        "days_on_mls": 8,
        "list_price": 599000,
        "list_date": "2025-01-22",
        "assessed_value": 337726,
        "estimated_value": 364000,
        "tax": 3803,
        "tax_history": [
            {
            "year": 2023,
            "tax": 3803,
            "assessment": {
                "building": 202474,
                "land": 135252,
                "total": 337726
            }
            },
            {
            "year": 2022,
            "tax": 3634,
            "assessment": {
                "building": 188700,
                "land": 132600,
                "total": 321300
            }
            },
            {
            "year": 2021,
            "tax": 1760,
            "assessment": {
                "building": 102648,
                "land": 51044,
                "total": 153692
            }
            },
            {
            "year": 2020,
            "tax": 1758,
            "assessment": {
                "building": 101596,
                "land": 50521,
                "total": 152117
            }
            },
            {
            "year": 2019,
            "tax": 1729,
            "assessment": {
                "building": 99604,
                "land": 49531,
                "total": 149135
            }
            },
            {
            "year": 2018,
            "tax": 1697,
            "assessment": {
                "building": 97651,
                "land": 48560,
                "total": 146211
            }
            },
            {
            "year": 2017,
            "tax": 1658,
            "assessment": {
                "building": 95737,
                "land": 47608,
                "total": 143345
            }
            },
            {
            "year": 2016,
            "tax": 759,
            "assessment": {
                "building": 53293,
                "land": 15023,
                "total": 68316
            }
            },
            {
            "year": 2015,
            "tax": 758,
            "assessment": {
                "building": 52493,
                "land": 14798,
                "total": 67291
            }
            },
            {
            "year": 2014,
            "tax": 745,
            "assessment": {
                "building": 51465,
                "land": 14509,
                "total": 65974
            }
            },
            {
            "year": 2013,
            "tax": 740,
            "assessment": {
                "building": 51233,
                "land": 14444,
                "total": 65677
            }
            },
            {
            "year": 2012,
            "tax": 690,
            "assessment": {
                "building": 50229,
                "land": 14161,
                "total": 64390
            }
            },
            {
            "year": 2010,
            "tax": 677,
            "assessment": {
                "building": 49245,
                "land": 13884,
                "total": 63129
            }
            },
            {
            "year": 2009,
            "tax": 689,
            "assessment": {
                "building": 48877,
                "land": 13781,
                "total": 62658
            }
            },
            {
            "year": 2008,
            "tax": 677,
            "assessment": {
                "building": 48034,
                "land": 13544,
                "total": 61578
            }
            },
            {
            "year": 2007,
            "tax": 645,
            "assessment": {
                "building": 47093,
                "land": 13279,
                "total": 60372
            }
            }
        ],
        "lot_sqft": 7841,
        "price_per_sqft": 645,
        "latitude": 39.725355,
        "longitude": -121.829217,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/e94894a865c5e9cc5466906e8318c752l-b3035122052od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2825
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1966-Vallombrosa-Ave_Chico_CA_95926_M21412-88694",
        "property_id": "2141288694",
        "listing_id": "2977473225",
        "mls": "MRCA",
        "mls_id": "SN25013778",
        "status": "FOR_SALE",
        "text": "Location, Location, Location! This BEAUTIFUL TURNKEY home is situated directly across from the serene Bidwell Park, offering stunning views and a lifestyle that embraces nature. With recent upgrades and a spacious open floor plan, this home is move-in ready! As you enter, you're greeted by luxury vinyl plank flooring and a large skylight that bathes the space in natural light. The living room boasts elegant tray ceilings, recessed lighting, and custom-built cabinets, providing both functionality and style. Step down into the cozy family room, where beamed ceilings, etched glass windows, and a gas fireplace to create a warm and inviting atmosphere. The kitchen is a chefs delight, featuring granite countertops, white shaker cabinets, stainless steel appliances, and a dual fuel range. A charming dining nook offers picturesque views of Bidwell Park, perfect for enjoying your morning coffee while watching the wildlife among the trees. The primary suite is surprisingly spacious, with a beautifully tiled step-in shower with dual shower heads, marble dual sink vanity, and a private slider leading to the backyard and HOT TUB! The thoughtfully designed en-suite includes a separate toilet area for added privacy. The backyard is perfect for entertaining or relaxing, with a pergola-covered patio, a large side yard ideal for a garden or play area. The garage is fully insulated and equipped with its own mini-split unit for climate control. It features custom-built shelves, including a desk space with tailored electrical outlets, specialty lockers for gear, and ample additional storage. A stacked washer and dryer are paired with a utility sink, complemented by dedicated storage cabinets above and below. The floors are finished with a Polytech-style coating for durability. At the opposite side of the home is a container shed that has been updated to complement the homes exterior. It includes a man door, a built-in workbench along one-third of a wall, and additional storage. Lighting and multiple outlets have also been installed for added functionality. Notable upgrades include OWNED SOLAR, new interior trim, doors, and hardware, as well as electrical, plumbing, HVAC (with a garage mini-split), attic insulation, whole house fan and carpet, all installed in 2019. This turnkey home is located just minutes from walking and biking trails, Big Chico Creek, Hooker Oak Park, and a scenic bike ride to downtown Chico. Dont miss the opportunity to make this your forever home!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "1966 Vallombrosa Ave",
        "street": "1966 Vallombrosa Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1698,
        "year_built": 1967,
        "days_on_mls": 8,
        "list_price": 649000,
        "list_date": "2025-01-22",
        "assessed_value": 401364,
        "estimated_value": 492396,
        "tax": 4397,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4397,
            "assessment": {
                "building": 182637,
                "land": 218727,
                "total": 401364
            }
            },
            {
            "year": 2022,
            "tax": 4325,
            "assessment": {
                "building": 179056,
                "land": 214439,
                "total": 393495
            }
            },
            {
            "year": 2021,
            "tax": 4242,
            "assessment": {
                "building": 175546,
                "land": 210235,
                "total": 385781
            }
            },
            {
            "year": 2020,
            "tax": 4229,
            "assessment": {
                "building": 173746,
                "land": 208080,
                "total": 381826
            }
            },
            {
            "year": 2019,
            "tax": 4151,
            "assessment": {
                "building": 170340,
                "land": 204000,
                "total": 374340
            }
            },
            {
            "year": 2018,
            "tax": 2447,
            "assessment": {
                "building": 135075,
                "land": 87795,
                "total": 222870
            }
            },
            {
            "year": 2017,
            "tax": 2395,
            "assessment": {
                "building": 132427,
                "land": 86074,
                "total": 218501
            }
            },
            {
            "year": 2016,
            "tax": 2185,
            "assessment": {
                "building": 129831,
                "land": 84387,
                "total": 214218
            }
            },
            {
            "year": 2015,
            "tax": 2184,
            "assessment": {
                "building": 127881,
                "land": 83120,
                "total": 211001
            }
            },
            {
            "year": 2014,
            "tax": 2130,
            "assessment": {
                "building": 125376,
                "land": 81492,
                "total": 206868
            }
            },
            {
            "year": 2013,
            "tax": 2157,
            "assessment": {
                "building": 124810,
                "land": 81124,
                "total": 205934
            }
            },
            {
            "year": 2012,
            "tax": 2030,
            "assessment": {
                "building": 122363,
                "land": 79534,
                "total": 201897
            }
            },
            {
            "year": 2010,
            "tax": 2006,
            "assessment": {
                "building": 119964,
                "land": 77975,
                "total": 197939
            }
            },
            {
            "year": 2009,
            "tax": 2042,
            "assessment": {
                "building": 119068,
                "land": 77393,
                "total": 196461
            }
            },
            {
            "year": 2008,
            "tax": 1970,
            "assessment": {
                "building": 117011,
                "land": 76056,
                "total": 193067
            }
            },
            {
            "year": 2007,
            "tax": 1915,
            "assessment": {
                "building": 114717,
                "land": 74565,
                "total": 189282
            }
            }
        ],
        "lot_sqft": 8712,
        "price_per_sqft": 382,
        "latitude": 39.754842,
        "longitude": -121.800694,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/49a21043de888ef495d725751381442al-m1838173988od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4525
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/701-E-Lassen-Ave-Unit-87_Chico_CA_95973_M23452-40272",
        "property_id": "2345240272",
        "listing_id": "2977594897",
        "mls": "MRCA",
        "mls_id": "SN25017511",
        "status": "FOR_SALE",
        "text": "Nestled in the charming Mobile Home Park, this delightful manufactured home offers a perfect blend of comfort and convenience. The spacious living room has multiple windows allowing light in, creating an inviting atmosphere. The home contains great insulation with double paned windows and sun screens, which help keep heat out and allow privacy during the day. With tons of cabinet space, your kitchen and storage needs are more than met, while the separate dining room provides a lovely spot to entertain or enjoy meals in peace. Both bedrooms are generously sized, ensuring restful nights, and the two bathrooms are equally roomy, offering all the comfort you could want. The neutral color scheme throughout adds a calm, modern touch, making it easy to personalize the space to your liking. Outside, enjoy the bonus of two sheds for extra storage or hobbies, and the large, fenced yard offers privacy and plenty of room to relax or garden. The landscaping has a drip system in the front and overall easy landscaping maintenance. The corner spot provides added space and seclusion, while the covered porch is an inviting place to unwind after a long day. With all these wonderful features, this home truly shines as a peaceful retreat in a welcoming community! Speaking of welcoming community, steps away from your home is the clubhouse, pool and spa. There is an exercise room available during office hours, 9-5 Monday through Friday. You'll always have something to do with tons of activities to enjoy free to residents, card room, pool tables, and Holiday dinners. Looking to join a group? There are many groups to choose from including: knitting, crocheting, sewing, quilting, weekly games, and residents use of clubhouse for birthdays and other occasions.",
        "style": "MOBILE",
        "full_street_line": "701 E Lassen Ave Unit 87",
        "street": "701 E Lassen Ave",
        "unit": "Unit 87",
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 2,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1152,
        "year_built": 1974,
        "days_on_mls": 5,
        "list_price": 74500,
        "list_date": "2025-01-25",
        "assessed_value": 0,
        "estimated_value": 62000,
        "tax": 738,
        "tax_history": [
            {
            "year": 2023,
            "tax": 738
            },
            {
            "year": 2022,
            "tax": 725
            },
            {
            "year": 2021,
            "tax": 194
            },
            {
            "year": 2020,
            "tax": 193
            },
            {
            "year": 2019,
            "tax": 188
            },
            {
            "year": 2016,
            "tax": 126,
            "assessment": {
                "building": null,
                "land": null,
                "total": 12000
            }
            },
            {
            "year": 2009,
            "tax": 129,
            "assessment": {
                "building": 19000,
                "land": null,
                "total": 19000
            }
            },
            {
            "year": 2008,
            "tax": 127,
            "assessment": {
                "building": 19000,
                "land": null,
                "total": 19000
            }
            },
            {
            "year": 2007,
            "tax": 126,
            "assessment": {
                "building": 19000,
                "land": null,
                "total": 19000
            }
            }
        ],
        "lot_sqft": 0,
        "price_per_sqft": 65,
        "latitude": 39.766376,
        "longitude": -121.853629,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/ae48283f571d05d07af0ba8123f7e6d4l-b517938358od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2673
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/10680-Player-Ln_Chico_CA_95928_M17812-08740",
        "property_id": "1781208740",
        "listing_id": "2977466142",
        "mls": "MRCA",
        "mls_id": "SN25013701",
        "status": "FOR_SALE",
        "text": "Create your dream home on this .29-acre lot at Butte Creek Country Club! Positioned on the 12th Tee and nestled in the gated Villas neighborhood, this corner lot offers an incredible opportunity to design the lifestyle you've always wanted. If you choose to become a member of Butte Creek Country Club, you'll gain access to top-tier amenities, including a championship 18-hole golf course, bocce courts, and a full-service restaurant perfect for entertaining friends and family. Find out more about seller/builder set of plans and fees that have already been paid to the county. Dont miss your chance to make your dream home a reality in this desirable community!",
        "style": "LAND",
        "full_street_line": "10680 Player Ln",
        "street": "10680 Player Ln",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 0,
        "full_baths": 0,
        "half_baths": 0,
        "sqft": 0,
        "year_built": 0,
        "days_on_mls": 9,
        "list_price": 135000,
        "list_date": "2025-01-21",
        "assessed_value": 116280,
        "estimated_value": 416000,
        "tax": 1303,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1303,
            "assessment": {
                "building": null,
                "land": 116280,
                "total": 116280
            }
            },
            {
            "year": 2022,
            "tax": 641,
            "assessment": {
                "building": null,
                "land": 114000,
                "total": 114000
            }
            },
            {
            "year": 2021,
            "tax": 1182,
            "assessment": {
                "building": null,
                "land": 105000,
                "total": 105000
            }
            },
            {
            "year": 2020,
            "tax": 1263,
            "assessment": {
                "building": null,
                "land": 111426,
                "total": 111426
            }
            },
            {
            "year": 2019,
            "tax": 1239,
            "assessment": {
                "building": null,
                "land": 109242,
                "total": 109242
            }
            },
            {
            "year": 2018,
            "tax": 1216,
            "assessment": {
                "building": null,
                "land": 107100,
                "total": 107100
            }
            },
            {
            "year": 2017,
            "tax": 1193,
            "assessment": {
                "building": null,
                "land": 105000,
                "total": 105000
            }
            },
            {
            "year": 2016,
            "tax": 1059,
            "assessment": {
                "building": null,
                "land": 100000,
                "total": 100000
            }
            },
            {
            "year": 2015,
            "tax": 968,
            "assessment": {
                "building": null,
                "land": 90000,
                "total": 90000
            }
            },
            {
            "year": 2014,
            "tax": 858,
            "assessment": {
                "building": null,
                "land": 80000,
                "total": 80000
            }
            },
            {
            "year": 2013,
            "tax": 875,
            "assessment": {
                "building": null,
                "land": 80000,
                "total": 80000
            }
            },
            {
            "year": 2012,
            "tax": 840,
            "assessment": {
                "building": null,
                "land": 80000,
                "total": 80000
            }
            },
            {
            "year": 2010,
            "tax": 1753,
            "assessment": {
                "building": null,
                "land": 80000,
                "total": 80000
            }
            },
            {
            "year": 2009,
            "tax": 1780,
            "assessment": {
                "building": null,
                "land": 165000,
                "total": 165000
            }
            },
            {
            "year": 2008,
            "tax": 2692,
            "assessment": {
                "building": null,
                "land": 253628,
                "total": 253628
            }
            },
            {
            "year": 2007,
            "tax": 2618,
            "assessment": {
                "building": null,
                "land": 248655,
                "total": 248655
            }
            }
        ],
        "lot_sqft": 12632,
        "price_per_sqft": 0,
        "latitude": 39.691613,
        "longitude": -121.776543,
        "county": "Butte",
        "hoa_fee": 285,
        "nearby_schools": "Butte County Office Of Education School District, Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/49dba951833208dd7cfd057659dbcbe0l-b4029251048od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1346
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/2883-Wingfield-Ave_Chico_CA_95928_M93410-43956",
        "property_id": "9341043956",
        "listing_id": "2977396414",
        "mls": "MRCA",
        "mls_id": "SN24185726",
        "status": "CONTINGENT",
        "text": "Fabulous location in the much sought-after Belvedere Heights neighborhood. It's the best of both worlds, with easy access to views of rolling green pastures, bike and nature trails, and amenities such as popular restaurants, coffee shops, health care, shopping and more. Beautifully maintained and nicely upgraded with owned solar, low maintenance landscaping, and fantastic covered rear patio. Make sure you pause for a moment to enjoy the views and unusual, peaceful quiet of the community! The open floorplan allows for an abundance of natural light and a seamless flow for entertaining. The primary suite is generous with a walk-in closet, ensuite bathroom, and access to the outdoor living space. Lightly lived in, this home is turnkey. All you have to do is move in. Call your favorite Realtor today for a private showing!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "2883 Wingfield Ave",
        "street": "2883 Wingfield Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1703,
        "year_built": 2020,
        "days_on_mls": 12,
        "list_price": 542000,
        "list_date": "2025-01-18",
        "assessed_value": 293647,
        "estimated_value": 533766,
        "tax": 3406,
        "tax_history": [
            {
            "year": 2023,
            "tax": 3406,
            "assessment": {
                "building": 208179,
                "land": 85468,
                "total": 293647
            }
            },
            {
            "year": 2022,
            "tax": 3267,
            "assessment": {
                "building": 199098,
                "land": 83793,
                "total": 282891
            }
            },
            {
            "year": 2021,
            "tax": 2477,
            "assessment": {
                "building": 90000,
                "land": 113001,
                "total": 203001
            }
            },
            {
            "year": 2020,
            "tax": 1431,
            "assessment": {
                "building": null,
                "land": 111843,
                "total": 111843
            }
            }
        ],
        "lot_sqft": 6534,
        "price_per_sqft": 318,
        "latitude": 39.728113,
        "longitude": -121.77575,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/a0433bb9f4f792df2ef04171ffb90d24l-m3636782989od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3502
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1202-West-Wind-Dr_Chico_CA_95926_M20971-41756",
        "property_id": "2097141756",
        "listing_id": "2977434012",
        "mls": "MRCA",
        "mls_id": "SN25007006",
        "status": "FOR_SALE",
        "text": "Welcome to this beauty located in the coveted Hillsboro Estates neighborhood! This elegant home boasts a fantastic location just minutes from downtown and Enloe Hospital, making it perfect for those who appreciate convenience without sacrificing tranquility. Step inside and be greeted by a bright and spacious living room, featuring vaulted ceilings, a cozy gas fireplace, and large picture windows that bring in natural light. The open floor plan creates a seamless flow between the living area, formal dining room, and charming breakfast nookideal for hosting gatherings or enjoying quiet meals. The heart of the home is designed to make entertaining a breeze with its ample counter space. The thoughtful layout places the primary suite on one side of the home for added privacy, while guest rooms are on the opposite side, perfect for visitors or family. Additional features include a walk through attic, surround sound, and a whole house fan. With a generous 3-car garage , there's plenty of room for all your toys, tools, and vehicles, ensuring you have the space you need. The beautifully landscaped corner lot has tons of curb appeal and provides a serene outdoor retreat. This home has been cherished as a second residence for many years, so it's turn-key and ready for new owners to create lasting memories. Dont miss the opportunity to own this stunning property in a sought-after neighborhood! Schedule your private tour today and experience the perfect blend of elegance and comfort.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "1202 West Wind Dr",
        "street": "1202 West Wind Dr",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 4,
        "full_baths": 2,
        "half_baths": 1,
        "sqft": 2700,
        "year_built": 2000,
        "days_on_mls": 10,
        "list_price": 810000,
        "list_date": "2025-01-20",
        "assessed_value": 604150,
        "estimated_value": 757284,
        "tax": 6674,
        "tax_history": [
            {
            "year": 2023,
            "tax": 6674,
            "assessment": {
                "building": 423188,
                "land": 180962,
                "total": 604150
            }
            },
            {
            "year": 2022,
            "tax": 6549,
            "assessment": {
                "building": 414891,
                "land": 177414,
                "total": 592305
            }
            },
            {
            "year": 2021,
            "tax": 6498,
            "assessment": {
                "building": 406756,
                "land": 173936,
                "total": 580692
            }
            },
            {
            "year": 2020,
            "tax": 6523,
            "assessment": {
                "building": 402586,
                "land": 172153,
                "total": 574739
            }
            },
            {
            "year": 2019,
            "tax": 6398,
            "assessment": {
                "building": 394693,
                "land": 168778,
                "total": 563471
            }
            },
            {
            "year": 2018,
            "tax": 5918,
            "assessment": {
                "building": 385000,
                "land": 135000,
                "total": 520000
            }
            },
            {
            "year": 2017,
            "tax": 5847,
            "assessment": {
                "building": 385000,
                "land": 135000,
                "total": 520000
            }
            },
            {
            "year": 2016,
            "tax": 4837,
            "assessment": {
                "building": 325000,
                "land": 135000,
                "total": 460000
            }
            },
            {
            "year": 2015,
            "tax": 4830,
            "assessment": {
                "building": 315000,
                "land": 130000,
                "total": 445000
            }
            },
            {
            "year": 2014,
            "tax": 4739,
            "assessment": {
                "building": 315000,
                "land": 125000,
                "total": 440000
            }
            },
            {
            "year": 2013,
            "tax": 4804,
            "assessment": {
                "building": 315000,
                "land": 125000,
                "total": 440000
            }
            },
            {
            "year": 2012,
            "tax": 4359,
            "assessment": {
                "building": 340000,
                "land": 120000,
                "total": 460000
            }
            },
            {
            "year": 2010,
            "tax": 2609,
            "assessment": {
                "building": 340000,
                "land": 120000,
                "total": 460000
            }
            },
            {
            "year": 2009,
            "tax": 2668,
            "assessment": {
                "building": 341093,
                "land": 145860,
                "total": 486953
            }
            },
            {
            "year": 2008,
            "tax": 2599,
            "assessment": {
                "building": 335200,
                "land": 143341,
                "total": 478541
            }
            },
            {
            "year": 2007,
            "tax": 5010,
            "assessment": {
                "building": 328628,
                "land": 140531,
                "total": 469159
            }
            }
        ],
        "lot_sqft": 13504,
        "price_per_sqft": 300,
        "latitude": 39.735784,
        "longitude": -121.878618,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/a4c76cd3a6168c41f8e13b0661c9d609l-m494132881od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1826
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/433-W-8th-St_Chico_CA_95928_M29771-75156",
        "property_id": "2977175156",
        "listing_id": "2977466171",
        "mls": "MRCA",
        "mls_id": "SN25014952",
        "status": "FOR_SALE",
        "text": "Here is your chance to own a prime rental property that has outstanding rental history! Located just blocks from Chico State and Downtown Chico, this two unit property features a main home with four bedrooms, two full bathrooms, and a detached ADU studio, and a pool. The main home is spacious with tall ceilings, dual pane windows, newer laminate flooring in the main living spaces, and newer kitchen appliances. The main home also features a large basement that could be utilized for storage or potential expansion. The ADU is set back on the property, cozy under the trees but has plenty of natural light with lots of windows and skylights. There is off street parking available for two vehicles as well. Current rents are $3, 200 for the main home and $850 for the ADU. Jump into ownership with this property!",
        "style": "MULTI_FAMILY",
        "full_street_line": "433 W 8th St",
        "street": "433 W 8th St",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 5,
        "full_baths": 3,
        "half_baths": 0,
        "sqft": 1720,
        "year_built": 1950,
        "days_on_mls": 9,
        "list_price": 500000,
        "list_date": "2025-01-21",
        "assessed_value": 455126,
        "estimated_value": 648000,
        "tax": 5108,
        "tax_history": [
            {
            "year": 2023,
            "tax": 5108,
            "assessment": {
                "building": 273076,
                "land": 182050,
                "total": 455126
            }
            },
            {
            "year": 2022,
            "tax": 5029,
            "assessment": {
                "building": 267722,
                "land": 178481,
                "total": 446203
            }
            },
            {
            "year": 2021,
            "tax": 4931,
            "assessment": {
                "building": 262473,
                "land": 174982,
                "total": 437455
            }
            },
            {
            "year": 2020,
            "tax": 4919,
            "assessment": {
                "building": 259782,
                "land": 173188,
                "total": 432970
            }
            },
            {
            "year": 2019,
            "tax": 4833,
            "assessment": {
                "building": 254689,
                "land": 169793,
                "total": 424482
            }
            },
            {
            "year": 2018,
            "tax": 4744,
            "assessment": {
                "building": 249696,
                "land": 166464,
                "total": 416160
            }
            },
            {
            "year": 2017,
            "tax": 4644,
            "assessment": {
                "building": 244800,
                "land": 163200,
                "total": 408000
            }
            },
            {
            "year": 2016,
            "tax": 4241,
            "assessment": {
                "building": 240000,
                "land": 160000,
                "total": 400000
            }
            },
            {
            "year": 2015,
            "tax": 1608,
            "assessment": {
                "building": 83120,
                "land": 63937,
                "total": 147057
            }
            },
            {
            "year": 2014,
            "tax": 1575,
            "assessment": {
                "building": 81492,
                "land": 62685,
                "total": 144177
            }
            },
            {
            "year": 2013,
            "tax": 1585,
            "assessment": {
                "building": 81124,
                "land": 62402,
                "total": 143526
            }
            },
            {
            "year": 2012,
            "tax": 1485,
            "assessment": {
                "building": 79534,
                "land": 61179,
                "total": 140713
            }
            },
            {
            "year": 2010,
            "tax": 1463,
            "assessment": {
                "building": 77975,
                "land": 59980,
                "total": 137955
            }
            },
            {
            "year": 2009,
            "tax": 1489,
            "assessment": {
                "building": 77393,
                "land": 59532,
                "total": 136925
            }
            },
            {
            "year": 2008,
            "tax": 1449,
            "assessment": {
                "building": 76056,
                "land": 58504,
                "total": 134560
            }
            },
            {
            "year": 2007,
            "tax": 1397,
            "assessment": {
                "building": 74565,
                "land": 57357,
                "total": 131922
            }
            }
        ],
        "lot_sqft": 8712,
        "price_per_sqft": 291,
        "latitude": 39.723723,
        "longitude": -121.83876,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/a85e2fde9f0c8b86d55129dd4d3a3644l-m3778311424od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4708
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/307-Bainbridge-Pl_Chico_CA_95973_M97824-25601",
        "property_id": "9782425601",
        "listing_id": "2977372479",
        "mls": "MRCA",
        "mls_id": "SN25012477",
        "status": "FOR_SALE",
        "text": "Step into your new sanctuary with this brand new single-story Bill Webb home, perfectly tailored for modern living. This charming residence spans 1998 square feet, offering 3 bedrooms, 2.25 bathrooms, 3 car garage, and a 3.60kW owned solar system! As you enter from the covered front patio, you are welcome's by a spacious entry way that leads to a guest bathroom, and a large den suitable for an office, or second living room. The large family room has coffered ceilings, and leads to an open concept kitchen and dining room ideal for family gatherings or relaxing evenings. The kitchen offers a large island, soft close doors and drawers, and stainless steel appliances. The primary bedroom enjoys a large walk-in closet, offering ample storage and privacy along with a bathroom with full tiled shower surround. Bedrooms 2 and 3 are generously sized, providing comfortable spaces for family or guests. The home includes a large covered back patio with access from both the family room, and the primary bedroom. This home is still under construction, and there is still time to make selections and finish choices.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "307 Bainbridge Pl",
        "street": "307 Bainbridge Pl",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 1,
        "sqft": 1998,
        "year_built": 2025,
        "days_on_mls": 13,
        "list_price": 595500,
        "list_date": "2025-01-17",
        "assessed_value": 0,
        "estimated_value": 0,
        "tax": 0,
        "tax_history": 0,
        "lot_sqft": 6150,
        "price_per_sqft": 298,
        "latitude": 39.78056,
        "longitude": -121.876129,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/656a57c8def2eabab680164e03b64737l-m3028231495od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1595
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/290-E-2nd-Ave_Chico_CA_95926_M28196-14751",
        "property_id": "2819614751",
        "listing_id": "2977373228",
        "mls": "MRCA",
        "mls_id": "SN25012532",
        "status": "PENDING",
        "text": "This charming duplex in the Avenues offers endless possibilities, whether youre looking to live in one unit and rent the other or maximize rental income from both. Situated on a corner lot with a classic picket fence and a beautifully landscaped yard, the property features a 2-bedroom, 1-bath unit and a studio. The 2/1 is adorable and has been tastefully updated with new luxury vinyl plank flooring, cozy carpet in the front bedroom, fresh paint, dual-pane windows (except one), updated bathroom flooring, modern light fixtures, and ceiling fans throughout plus new tile backsplash in the kitchen. It also includes a full-size washer and dryer. The studio unit is equally delightful, featuring a full kitchen with a dining nook, and a stackable washer and dryer in a laundry room off the kitchen. Both units have private front and backyard spaces and separate gas and electric meters for easy management. Additional features include a double car size converted garage thats perfect for a workshop or hobbies, fresh paint on both porches, a new roof on the house and garage in 2019, and front yard sprinklers. Dont miss this fantastic opportunity in one of the most charming neighborhoods around!",
        "style": "MULTI_FAMILY",
        "full_street_line": "290 E 2nd Ave",
        "street": "290 E 2nd Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1263,
        "year_built": 1913,
        "days_on_mls": 13,
        "list_price": 389500,
        "list_date": "2025-01-17",
        "assessed_value": 169041,
        "estimated_value": 310400,
        "tax": 1891,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1891,
            "assessment": {
                "building": 93912,
                "land": 75129,
                "total": 169041
            }
            },
            {
            "year": 2022,
            "tax": 930,
            "assessment": {
                "building": 92071,
                "land": 73656,
                "total": 165727
            }
            },
            {
            "year": 2021,
            "tax": 1825,
            "assessment": {
                "building": 90266,
                "land": 72212,
                "total": 162478
            }
            },
            {
            "year": 2020,
            "tax": 1820,
            "assessment": {
                "building": 89341,
                "land": 71472,
                "total": 160813
            }
            },
            {
            "year": 2019,
            "tax": 1787,
            "assessment": {
                "building": 87590,
                "land": 70071,
                "total": 157661
            }
            },
            {
            "year": 2018,
            "tax": 1754,
            "assessment": {
                "building": 85873,
                "land": 68698,
                "total": 154571
            }
            },
            {
            "year": 2017,
            "tax": 1718,
            "assessment": {
                "building": 84190,
                "land": 67351,
                "total": 151541
            }
            },
            {
            "year": 2016,
            "tax": 1569,
            "assessment": {
                "building": 82540,
                "land": 66031,
                "total": 148571
            }
            },
            {
            "year": 2015,
            "tax": 1569,
            "assessment": {
                "building": 81301,
                "land": 65040,
                "total": 146341
            }
            },
            {
            "year": 2014,
            "tax": 1531,
            "assessment": {
                "building": 79709,
                "land": 63766,
                "total": 143475
            }
            },
            {
            "year": 2013,
            "tax": 1549,
            "assessment": {
                "building": 79349,
                "land": 63478,
                "total": 142827
            }
            },
            {
            "year": 2012,
            "tax": 1459,
            "assessment": {
                "building": 77794,
                "land": 62234,
                "total": 140028
            }
            },
            {
            "year": 2010,
            "tax": 1369,
            "assessment": {
                "building": 76269,
                "land": 61014,
                "total": 137283
            }
            },
            {
            "year": 2009,
            "tax": 1393,
            "assessment": {
                "building": 75699,
                "land": 60558,
                "total": 136257
            }
            },
            {
            "year": 2008,
            "tax": 1343,
            "assessment": {
                "building": 74392,
                "land": 59512,
                "total": 133904
            }
            },
            {
            "year": 2007,
            "tax": 1306,
            "assessment": {
                "building": 72934,
                "land": 58346,
                "total": 131280
            }
            }
        ],
        "lot_sqft": 4792,
        "price_per_sqft": 308,
        "latitude": 39.740315,
        "longitude": -121.843625,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/e786544621a94ea9af3599edb404f49dl-m613029993od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1629
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/181-Connors-Ave_Chico_CA_95926_M10640-79359",
        "property_id": "1064079359",
        "listing_id": "2977422873",
        "mls": "MRCA",
        "mls_id": "SN25011521",
        "status": "FOR_SALE",
        "text": "This property offers both charm and versatility, featuring a 4-bedroom plus office or possible additional 5th bedroom, 2-bathroom main home and a separate 2-bedroom, 1-bathroom unit, making it perfect for multi-generational living or rental income. The main home is brimming with character, boasting a spacious living room with floor-to-ceiling windows, tall ceilings, and a cozy wood stove insert surrounded by an adorable rock accent wall. The open-concept kitchen connects seamlessly to the living area and includes bar top seating on a large wood countertop and two ovens. Down the hall, youll discover five unique bedrooms, each full of personality. One bedroom features a fun loft area, while the primary suite offers its own loft space, a large walk-in closet, and an en-suite bathroom. A generously sized laundry room adds to the home's functionality. The second unit was thoughtfully added and provides its own living space, full kitchen, two spacious bedrooms, one bathroom, and a separate laundry room with storage area that was formally part of the garage. Outside, enjoy the expansive backyard with endless possibilities. The second unit has a private yard area, offering added privacy. A large shed in the back can be used as a hobby room or for storage. Additional features include plenty of parking, an RV dump station, two water heaters, and solar panels to keep utility costs low. The main home also has two mini-splits for efficient heating and cooling. This home is truly one of a kinddont miss the opportunity to make it yours!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "181 Connors Ave",
        "street": "181 Connors Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 5,
        "full_baths": 1,
        "half_baths": 1,
        "sqft": 1653,
        "year_built": 1951,
        "days_on_mls": 10,
        "list_price": 439000,
        "list_date": "2025-01-20",
        "assessed_value": 127276,
        "estimated_value": 360392,
        "tax": 1350,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1350,
            "assessment": {
                "building": 74750,
                "land": 52526,
                "total": 127276
            }
            },
            {
            "year": 2022,
            "tax": 1403,
            "assessment": {
                "building": 73285,
                "land": 51497,
                "total": 124782
            }
            },
            {
            "year": 2021,
            "tax": 1377,
            "assessment": {
                "building": 71849,
                "land": 50488,
                "total": 122337
            }
            },
            {
            "year": 2020,
            "tax": 1373,
            "assessment": {
                "building": 71113,
                "land": 49971,
                "total": 121084
            }
            },
            {
            "year": 2019,
            "tax": 1349,
            "assessment": {
                "building": 69719,
                "land": 48992,
                "total": 118711
            }
            },
            {
            "year": 2018,
            "tax": 1324,
            "assessment": {
                "building": 68352,
                "land": 48032,
                "total": 116384
            }
            },
            {
            "year": 2017,
            "tax": 1297,
            "assessment": {
                "building": 67012,
                "land": 47091,
                "total": 114103
            }
            },
            {
            "year": 2016,
            "tax": 1184,
            "assessment": {
                "building": 65699,
                "land": 46168,
                "total": 111867
            }
            },
            {
            "year": 2015,
            "tax": 1184,
            "assessment": {
                "building": 64713,
                "land": 45475,
                "total": 110188
            }
            },
            {
            "year": 2014,
            "tax": 1168,
            "assessment": {
                "building": 63446,
                "land": 44585,
                "total": 108031
            }
            },
            {
            "year": 2013,
            "tax": 1178,
            "assessment": {
                "building": 63160,
                "land": 44384,
                "total": 107544
            }
            },
            {
            "year": 2012,
            "tax": 1111,
            "assessment": {
                "building": 61922,
                "land": 43514,
                "total": 105436
            }
            },
            {
            "year": 2010,
            "tax": 1099,
            "assessment": {
                "building": 60708,
                "land": 42661,
                "total": 103369
            }
            },
            {
            "year": 2009,
            "tax": 1118,
            "assessment": {
                "building": 60255,
                "land": 42343,
                "total": 102598
            }
            },
            {
            "year": 2008,
            "tax": 1080,
            "assessment": {
                "building": 59215,
                "land": 41612,
                "total": 100827
            }
            },
            {
            "year": 2007,
            "tax": 1051,
            "assessment": {
                "building": 58054,
                "land": 40797,
                "total": 98851
            }
            }
        ],
        "lot_sqft": 16117,
        "price_per_sqft": 266,
        "latitude": 39.756557,
        "longitude": -121.859456,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/de82fb1003ab7bd93f71c953ff02d349l-m4182057991od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3397
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1387-Hawthorne-Ave_Chico_CA_95926_M21070-41293",
        "property_id": "2107041293",
        "listing_id": "2977588138",
        "mls": "MRCA",
        "mls_id": "SN25008029",
        "status": "FOR_SALE",
        "text": "This charming home, located blocks from the desirable Bidwell Park, offers the perfect blend of comfort and convenience. Situated on a spacious corner lot with mature landscaping, this property provides both privacy and curb appeal. Inside, you'll find three bedrooms and two bathrooms, including a serene master suite. The home boasts beautiful hardwood floors throughout, dual-pane windows for energy efficiency, a new roof in 2022, an upgraded electric panel, and fresh paint, making it move-in ready! With solar panels for sustainable energy, plus battery backup, you can enjoy both eco-friendly living and lower utility costs. Located near Sierra View Elementary and within close proximity to Bidwell Park, this home is ideal for those looking for a peaceful retreat with easy access to outdoor activities and great schools. Dont miss the opportunity to make this well-maintained home yours!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "1387 Hawthorne Ave",
        "street": "1387 Hawthorne Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1469,
        "year_built": 1955,
        "days_on_mls": 5,
        "list_price": 449000,
        "list_date": "2025-01-25",
        "assessed_value": 453900,
        "estimated_value": 437100,
        "tax": 5059,
        "tax_history": [
            {
            "year": 2023,
            "tax": 5059,
            "assessment": {
                "building": 285600,
                "land": 168300,
                "total": 453900
            }
            },
            {
            "year": 2022,
            "tax": 3956,
            "assessment": {
                "building": 167273,
                "land": 193156,
                "total": 360429
            }
            },
            {
            "year": 2021,
            "tax": 3880,
            "assessment": {
                "building": 163994,
                "land": 189369,
                "total": 353363
            }
            },
            {
            "year": 2020,
            "tax": 3868,
            "assessment": {
                "building": 162313,
                "land": 187428,
                "total": 349741
            }
            },
            {
            "year": 2019,
            "tax": 3797,
            "assessment": {
                "building": 159131,
                "land": 183753,
                "total": 342884
            }
            },
            {
            "year": 2018,
            "tax": 3726,
            "assessment": {
                "building": 156011,
                "land": 180150,
                "total": 336161
            }
            },
            {
            "year": 2017,
            "tax": 3146,
            "assessment": {
                "building": 155000,
                "land": 130000,
                "total": 285000
            }
            },
            {
            "year": 2016,
            "tax": 2823,
            "assessment": {
                "building": 145000,
                "land": 130000,
                "total": 275000
            }
            },
            {
            "year": 2015,
            "tax": 2653,
            "assessment": {
                "building": 130000,
                "land": 125000,
                "total": 255000
            }
            },
            {
            "year": 2014,
            "tax": 2587,
            "assessment": {
                "building": 145000,
                "land": 105000,
                "total": 250000
            }
            },
            {
            "year": 2013,
            "tax": 2418,
            "assessment": {
                "building": 125000,
                "land": 105000,
                "total": 230000
            }
            },
            {
            "year": 2012,
            "tax": 2375,
            "assessment": {
                "building": 135000,
                "land": 100000,
                "total": 235000
            }
            },
            {
            "year": 2010,
            "tax": 2679,
            "assessment": {
                "building": 135000,
                "land": 100000,
                "total": 235000
            }
            },
            {
            "year": 2009,
            "tax": 2720,
            "assessment": {
                "building": 140000,
                "land": 120000,
                "total": 260000
            }
            },
            {
            "year": 2008,
            "tax": 3009,
            "assessment": {
                "building": 135147,
                "land": 156060,
                "total": 291207
            }
            },
            {
            "year": 2007,
            "tax": 2926,
            "assessment": {
                "building": 132498,
                "land": 153000,
                "total": 285498
            }
            }
        ],
        "lot_sqft": 6970,
        "price_per_sqft": 306,
        "latitude": 39.74835,
        "longitude": -121.819423,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/2034cf45822b892f7a345ee1129fd41bl-m975938834od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4034
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1080-Filbert-Ave_Chico_CA_95926_M20949-67127",
        "property_id": "2094967127",
        "listing_id": "2977375467",
        "mls": "MRCA",
        "mls_id": "SN25012610",
        "status": "FOR_SALE",
        "text": "DOUBLE LOT with 2 APNS Mid-Century Modern dream home 2 blocks to the famous Bidwell Park! Welcome to 1080 Filbert Ave, a one-of-a-kind property situated just 2 blocks from the historic and beautiful Lower Bidwell Park, offering walking, biking, and horse trails, along with a serene creek. Built in 1951, this charming 4-bedroom, 2-bathroom home boasts approximately 2, 400 sq. ft. of living space and has so many incredible amenities. If you're someone who loves to entertain, then this is the home for you! This property offers a large dining room, a homey living room, and an expansive 'party' room. The party room features vaulted ceilings, wall-to-wall cabinets for storage, a wet bar, a separate HVAC system, an indoor BBQ inlaid into a decorative brick wall, and a wood-burning stove, perfect for entertaining year-round. This extra large kitchen is a chef's delight with a built-in gas range, a large island with a prep sink, a dining nook, and an incredible pantry with space-saving shelves, two lazy Susan cabinets, and tile countertops. Plus, built-ins include a knife drawer and a cookbook holder. Also, enjoy the oversized back patio and the extra-large backyard and green space on a double lot, plenty of space for your four-legged friends or future pool. There's also a garden area and a custom greenhouse with a cool storage section. With a 1-car attached garage and a detached oversized carport, this home provides ample parking and storage options. Additional amenities include an exterior electric car charger, private driveway, and entrance to one of the bedrooms making it the perfect space for a home office, with the back wall lined with bookshelves. The proximity to Lower Bidwell Park is a huge draw and allows for you to enjoy the recreational activities this historic park has to offer. Located in a desirable Chico neighborhood, you'll have easy access to local amenities, schools, and shopping. Don't miss out on this entertainer's dream home and get ready to experience the charm, space, and unique features of 1080 Filbert Avenue - your future dream home!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "1080 Filbert Ave",
        "street": "1080 Filbert Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 4,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 2400,
        "year_built": 1951,
        "days_on_mls": 13,
        "list_price": 750000,
        "list_date": "2025-01-17",
        "assessed_value": 109778,
        "estimated_value": 704000,
        "tax": 1155,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1155,
            "assessment": {
                "building": 87269,
                "land": 22509,
                "total": 109778
            }
            },
            {
            "year": 2022,
            "tax": 1134,
            "assessment": {
                "building": 85558,
                "land": 22068,
                "total": 107626
            }
            },
            {
            "year": 2021,
            "tax": 1111,
            "assessment": {
                "building": 83881,
                "land": 21636,
                "total": 105517
            }
            },
            {
            "year": 2020,
            "tax": 1107,
            "assessment": {
                "building": 83021,
                "land": 21415,
                "total": 104436
            }
            },
            {
            "year": 2019,
            "tax": 1086,
            "assessment": {
                "building": 81394,
                "land": 20996,
                "total": 102390
            }
            },
            {
            "year": 2018,
            "tax": 1064,
            "assessment": {
                "building": 79799,
                "land": 20585,
                "total": 100384
            }
            },
            {
            "year": 2017,
            "tax": 1041,
            "assessment": {
                "building": 78235,
                "land": 20182,
                "total": 98417
            }
            },
            {
            "year": 2016,
            "tax": 949,
            "assessment": {
                "building": 76701,
                "land": 19787,
                "total": 96488
            }
            },
            {
            "year": 2015,
            "tax": 948,
            "assessment": {
                "building": 75549,
                "land": 19490,
                "total": 95039
            }
            },
            {
            "year": 2014,
            "tax": 924,
            "assessment": {
                "building": 74070,
                "land": 19109,
                "total": 93179
            }
            },
            {
            "year": 2013,
            "tax": 930,
            "assessment": {
                "building": 73736,
                "land": 19023,
                "total": 92759
            }
            },
            {
            "year": 2012,
            "tax": 874,
            "assessment": {
                "building": 72291,
                "land": 18650,
                "total": 90941
            }
            },
            {
            "year": 2010,
            "tax": 863,
            "assessment": {
                "building": 70874,
                "land": 18285,
                "total": 89159
            }
            },
            {
            "year": 2009,
            "tax": 878,
            "assessment": {
                "building": 70345,
                "land": 18149,
                "total": 88494
            }
            },
            {
            "year": 2008,
            "tax": 846,
            "assessment": {
                "building": 69131,
                "land": 17837,
                "total": 86968
            }
            },
            {
            "year": 2007,
            "tax": 822,
            "assessment": {
                "building": 67776,
                "land": 17488,
                "total": 85264
            }
            }
        ],
        "lot_sqft": 20473,
        "price_per_sqft": 313,
        "latitude": 39.742014,
        "longitude": -121.825696,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/261917ba76c9ae80da683a078b9f31cal-m4283183291od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2465
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/955-Aspen-St_Chico_CA_95928_M29429-27755",
        "property_id": "2942927755",
        "listing_id": "2977377025",
        "mls": "MRCA",
        "mls_id": "SN25012593",
        "status": "CONTINGENT",
        "text": "INCOME PRODUCING MULIT-FAMILY for an incredible price! Easy to rent due to its proximity to Chico State campus and Bidwell Park. Completely renovated throughout. Front unit has 2 large bedrooms and office that can be easily converted to a 3rd bedroom. White and bright kitchen with newer appliances. Separate entrances and parking for both units. HUGE BACKYARD that's pet friendly with a wood security fence to keep your fur babies safe. Back unit includes separate bedroom, living space, full bath and white kitchen. It's the perfect investment property for someone looking for another stream of income or can be used as a single-family with a guest house for kids/in-laws. This opportunity will not last long!",
        "style": "DUPLEX_TRIPLEX",
        "full_street_line": "955 Aspen St",
        "street": "955 Aspen St",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 4,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1215,
        "year_built": 1942,
        "days_on_mls": 12,
        "list_price": 385000,
        "list_date": "2025-01-18",
        "assessed_value": 358938,
        "estimated_value": 378205,
        "tax": 4023,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4023,
            "assessment": {
                "building": 192474,
                "land": 166464,
                "total": 358938
            }
            },
            {
            "year": 2022,
            "tax": 3958,
            "assessment": {
                "building": 188700,
                "land": 163200,
                "total": 351900
            }
            },
            {
            "year": 2021,
            "tax": 3338,
            "assessment": {
                "building": 157161,
                "land": 139126,
                "total": 296287
            }
            },
            {
            "year": 2020,
            "tax": 3329,
            "assessment": {
                "building": 155550,
                "land": 137700,
                "total": 293250
            }
            },
            {
            "year": 2019,
            "tax": 3270,
            "assessment": {
                "building": 152500,
                "land": 135000,
                "total": 287500
            }
            },
            {
            "year": 2018,
            "tax": 277,
            "assessment": {
                "building": 21703,
                "land": 7486,
                "total": 29189
            }
            },
            {
            "year": 2017,
            "tax": 269,
            "assessment": {
                "building": 21278,
                "land": 7340,
                "total": 28618
            }
            },
            {
            "year": 2016,
            "tax": 247,
            "assessment": {
                "building": 20861,
                "land": 7197,
                "total": 28058
            }
            },
            {
            "year": 2015,
            "tax": 245,
            "assessment": {
                "building": 20548,
                "land": 7089,
                "total": 27637
            }
            },
            {
            "year": 2014,
            "tax": 253,
            "assessment": {
                "building": 20146,
                "land": 6951,
                "total": 27097
            }
            },
            {
            "year": 2013,
            "tax": 237,
            "assessment": {
                "building": 20055,
                "land": 6920,
                "total": 26975
            }
            },
            {
            "year": 2012,
            "tax": 220,
            "assessment": {
                "building": 19662,
                "land": 6785,
                "total": 26447
            }
            },
            {
            "year": 2010,
            "tax": 214,
            "assessment": {
                "building": 19277,
                "land": 6652,
                "total": 25929
            }
            },
            {
            "year": 2009,
            "tax": 218,
            "assessment": {
                "building": 19133,
                "land": 6603,
                "total": 25736
            }
            },
            {
            "year": 2008,
            "tax": 213,
            "assessment": {
                "building": 18803,
                "land": 6490,
                "total": 25293
            }
            },
            {
            "year": 2007,
            "tax": 203,
            "assessment": {
                "building": 18435,
                "land": 6363,
                "total": 24798
            }
            }
        ],
        "lot_sqft": 6098,
        "price_per_sqft": 317,
        "latitude": 39.731169,
        "longitude": -121.82505,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/3515d62628ef6fe19c394bcb6e633829l-m3184689547od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1925
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/14401-State-Highway-99-N_Chico_CA_95973_M21423-32140",
        "property_id": "2142332140",
        "listing_id": "2977374653",
        "mls": "MRCA",
        "mls_id": "SN25009680",
        "status": "FOR_SALE",
        "text": "Discover Your Fully Furnished Private Oasis! This special property allows you the opportunity to step into a world of tranquility with this exceptional property, where a stunning 2-acre manmade pond creates a breathtaking centerpiece. Just minutes from Chico, yet it feels like a serene retreat a million miles away. As you pass through custom security gates and cross your own private bridge, the stresses of the day melt away. Designed with Mediterranean elegance and thoughtful detail, this fully furnished home offers a seamless blend of comfort and sophistication. Nearly every room is graced with views of the sparkling pond, luxurious pool, and multiple patios that wrap around the homeideal for both quiet moments of relaxation and hosting unforgettable gatherings. The heart of the home is the grand living room, featuring soaring corner windows framing the pond, a custom-designed fireplace, and a peaceful ambiance that soothes the soul. Stroll through the curved hallway to discover the chefs kitchen, complete with a cozy nook, sitting area with its own fireplace, and an impressive wine cellar. Adjacent is the elegant dining room, which opens to a charming courtyard, perfect for al fresco meals or evening cocktails. The propertys layout is as functional as it is beautiful. A versatile office/den opens to the pool patio, while a full bath nearby ensures convenient access after a swim. Downstairs, a private bedroom boasts its own half bath and storageideal for guests or family members seeking privacy. The luxurious primary suite is nothing short of a sanctuary. It features dual closets, vanities, and an exquisite shower you have to see to believe. Step outside to a private patio with a hot tubperfect for stargazing under the night sky. This home offers more than just beauty and comfortits also not located in any California Hazard Zones, providing peace of mind and security. The property is move-in ready and can welcome its new owner in no time. The true stars of this property are the meticulously designed grounds, offering unparalleled privacy. From the picturesque pond and dock to the sparkling pool and expansive acreage, this is a place where your family can create memories and enjoy the seclusion youve always dreamed of. Welcome to a home where elegance meets serenityyour personal retreat is ready and waiting.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "14401 State Highway 99 N",
        "street": "14401 State Highway 99",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 3,
        "half_baths": 1,
        "sqft": 4354,
        "year_built": 1991,
        "days_on_mls": 13,
        "list_price": 1850000,
        "list_date": "2025-01-17",
        "assessed_value": 656903,
        "estimated_value": 1147000,
        "tax": 7446,
        "tax_history": [
            {
            "year": 2023,
            "tax": 7446,
            "assessment": {
                "building": 554177,
                "land": 102726,
                "total": 656903
            }
            },
            {
            "year": 2022,
            "tax": 7331,
            "assessment": {
                "building": 543311,
                "land": 100712,
                "total": 644023
            }
            },
            {
            "year": 2021,
            "tax": 7195,
            "assessment": {
                "building": 532658,
                "land": 98738,
                "total": 631396
            }
            },
            {
            "year": 2020,
            "tax": 6508,
            "assessment": {
                "building": 485937,
                "land": 97726,
                "total": 583663
            }
            },
            {
            "year": 2019,
            "tax": 6590,
            "assessment": {
                "building": 476409,
                "land": 95810,
                "total": 572219
            }
            },
            {
            "year": 2018,
            "tax": 6472,
            "assessment": {
                "building": 467068,
                "land": 93932,
                "total": 561000
            }
            },
            {
            "year": 2017,
            "tax": 6344,
            "assessment": {
                "building": 457910,
                "land": 92091,
                "total": 550001
            }
            },
            {
            "year": 2016,
            "tax": 5806,
            "assessment": {
                "building": 448932,
                "land": 90286,
                "total": 539218
            }
            },
            {
            "year": 2015,
            "tax": 5805,
            "assessment": {
                "building": 442189,
                "land": 88930,
                "total": 531119
            }
            },
            {
            "year": 2014,
            "tax": 5668,
            "assessment": {
                "building": 433528,
                "land": 87188,
                "total": 520716
            }
            },
            {
            "year": 2013,
            "tax": 5753,
            "assessment": {
                "building": 431569,
                "land": 86794,
                "total": 518363
            }
            },
            {
            "year": 2012,
            "tax": 5227,
            "assessment": {
                "building": 423107,
                "land": 85093,
                "total": 508200
            }
            },
            {
            "year": 2010,
            "tax": 5168,
            "assessment": {
                "building": 414811,
                "land": 83425,
                "total": 498236
            }
            },
            {
            "year": 2009,
            "tax": 5259,
            "assessment": {
                "building": 411711,
                "land": 82802,
                "total": 494513
            }
            },
            {
            "year": 2008,
            "tax": 5077,
            "assessment": {
                "building": 404599,
                "land": 81372,
                "total": 485971
            }
            },
            {
            "year": 2007,
            "tax": 4938,
            "assessment": {
                "building": 396666,
                "land": 79777,
                "total": 476443
            }
            }
        ],
        "lot_sqft": 713513,
        "price_per_sqft": 425,
        "latitude": 39.819375,
        "longitude": -121.924414,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/3345076067df4bdfb49e050bc62c9421l-m352373282od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1742
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/433-W-8th-St_Chico_CA_95928_M29771-75156",
        "property_id": "2977175156",
        "listing_id": "2977464850",
        "mls": "MRCA",
        "mls_id": "SN25013380",
        "status": "FOR_SALE",
        "text": "Here is your chance to own a prime rental property that has outstanding rental history! Located just blocks from Chico State and Downtown Chico, this two unit property features a main home with four bedrooms, two full bathrooms, and a detached ADU studio, and a pool. The main home is spacious with tall ceilings, dual pane windows, newer laminate flooring in the main living spaces, and newer kitchen appliances. The main home also features a large basement that could be utilized for storage or potential expansion. The ADU is set back on the property, cozy under the trees but has plenty of natural light with lots of windows and skylights. There is off street parking available for two vehicles as well. Current rents are $3, 200 for the main home and $850 for the ADU. Jump into ownership with this property!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "433 W 8th St",
        "street": "433 W 8th St",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 5,
        "full_baths": 3,
        "half_baths": 0,
        "sqft": 1720,
        "year_built": 1950,
        "days_on_mls": 9,
        "list_price": 500000,
        "list_date": "2025-01-21",
        "assessed_value": 455126,
        "estimated_value": 648000,
        "tax": 5108,
        "tax_history": [
            {
            "year": 2023,
            "tax": 5108,
            "assessment": {
                "building": 273076,
                "land": 182050,
                "total": 455126
            }
            },
            {
            "year": 2022,
            "tax": 5029,
            "assessment": {
                "building": 267722,
                "land": 178481,
                "total": 446203
            }
            },
            {
            "year": 2021,
            "tax": 4931,
            "assessment": {
                "building": 262473,
                "land": 174982,
                "total": 437455
            }
            },
            {
            "year": 2020,
            "tax": 4919,
            "assessment": {
                "building": 259782,
                "land": 173188,
                "total": 432970
            }
            },
            {
            "year": 2019,
            "tax": 4833,
            "assessment": {
                "building": 254689,
                "land": 169793,
                "total": 424482
            }
            },
            {
            "year": 2018,
            "tax": 4744,
            "assessment": {
                "building": 249696,
                "land": 166464,
                "total": 416160
            }
            },
            {
            "year": 2017,
            "tax": 4644,
            "assessment": {
                "building": 244800,
                "land": 163200,
                "total": 408000
            }
            },
            {
            "year": 2016,
            "tax": 4241,
            "assessment": {
                "building": 240000,
                "land": 160000,
                "total": 400000
            }
            },
            {
            "year": 2015,
            "tax": 1608,
            "assessment": {
                "building": 83120,
                "land": 63937,
                "total": 147057
            }
            },
            {
            "year": 2014,
            "tax": 1575,
            "assessment": {
                "building": 81492,
                "land": 62685,
                "total": 144177
            }
            },
            {
            "year": 2013,
            "tax": 1585,
            "assessment": {
                "building": 81124,
                "land": 62402,
                "total": 143526
            }
            },
            {
            "year": 2012,
            "tax": 1485,
            "assessment": {
                "building": 79534,
                "land": 61179,
                "total": 140713
            }
            },
            {
            "year": 2010,
            "tax": 1463,
            "assessment": {
                "building": 77975,
                "land": 59980,
                "total": 137955
            }
            },
            {
            "year": 2009,
            "tax": 1489,
            "assessment": {
                "building": 77393,
                "land": 59532,
                "total": 136925
            }
            },
            {
            "year": 2008,
            "tax": 1449,
            "assessment": {
                "building": 76056,
                "land": 58504,
                "total": 134560
            }
            },
            {
            "year": 2007,
            "tax": 1397,
            "assessment": {
                "building": 74565,
                "land": 57357,
                "total": 131922
            }
            }
        ],
        "lot_sqft": 8712,
        "price_per_sqft": 291,
        "latitude": 39.723723,
        "longitude": -121.83876,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/f69cea78afeddf59ec3d1c43206e6fdcl-m519552096od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4913
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/303-Bainbridge-Pl_Chico_CA_95973_M93870-74480",
        "property_id": "9387074480",
        "listing_id": "2977369868",
        "mls": "MRCA",
        "mls_id": "SN25012192",
        "status": "FOR_SALE",
        "text": "Welcome to your new Bill Webb home, Plan 540, a spacious single-story corner lot floorplan spanning 2045 square feet. This thoughtfully designed home is under construction with some time left to choose your finishes! This home comes on a large lot, owned 3.60kW solar system, and enough room for RV parking. Upon entering, you are greeted by a welcoming covered porch leading into a bright entryway. The open concept living space includes a family room with cathedral ceiling, and a separate living room with 11' ceilings and large windows! The kitchen is designed for both the avid cook and those who love to host. Featuring stainless steel appliances, plenty of cabinet space, and ample counter space, it seamlessly flows into the generously sized dining area, ensuring meals, or studying, are both enjoyable and spacious. The primary bedroom offers a private retreat with a walk-in closet, providing ample storage and personal space, as well as a private exit to the large covered patio. Bedrooms #2 and #3 are well-sized for family members or guests, each offering comfort and privacy. A practical laundry room with sink is conveniently located near the kitchen, making household chores less of a hassle. The home also features a three-car garage (22' x 32') for your vehicles and additional storage. Come join our newest community in Chico of thoughtfully designed homes, that will eventually consist of a 1 acre community park, and bike path!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "303 Bainbridge Pl",
        "street": "303 Bainbridge Pl",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 2045,
        "year_built": 2025,
        "days_on_mls": 13,
        "list_price": 625500,
        "list_date": "2025-01-17",
        "assessed_value": 0,
        "estimated_value": 0,
        "tax": 0,
        "tax_history": 0,
        "lot_sqft": 9139,
        "price_per_sqft": 306,
        "latitude": 39.780544,
        "longitude": -121.876404,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/22ff96c8828e7262621feb6dddb48d18l-m3572631003od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3309
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/139-W-Lassen-Ave-Apt-18_Chico_CA_95973_M15256-71953",
        "property_id": "1525671953",
        "listing_id": "2977337121",
        "mls": "MRCA",
        "mls_id": "SN25011429",
        "status": "PENDING",
        "text": "Welcome to this exceptional 2-bedroom, 1-bathroom condo that combines thoughtful upgrades and modern comfort. Situated as an end unit, this home boasts unique features that truly set it apart. With only one shared wall, this condo offers enhanced privacy.Step inside to discover an open floor plan with elegant flooring, soft neutral tones, and a spacious living area centered around a rare brick-surrounded fireplaceone of the few in the community. The kitchen has been expanded, offering additional counter space and storage, making it perfect for those who love to cook or entertain. Granite countertops, stainless steel appliances, an electric range, and an eating counter complete the kitchens functional and stylish design. This unit offers even more storage, thanks to the removal of the furnace to create an extra closet. A ductless mini-split system provides personalized comfort and energy efficiency throughout the home.The beautifully updated bathroom features a modern vanity and a subway tiled tub-shower combination, while all interior and closet doors have been upgraded.Outside, enjoy your private outdoor space, ideal for relaxing or entertaining, and take advantage of the communitys sparkling in-ground pool on warm summer days. An assigned carport parking space and the convenience of being move-in ready make this condo a standout opportunity.Dont miss your chance to own one of the most unique units in the communityschedule your showing today!",
        "style": "CONDOS",
        "full_street_line": "139 W Lassen Ave Apt 18",
        "street": "139 W Lassen Ave",
        "unit": "Apt 18",
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 2,
        "full_baths": 1,
        "half_baths": 0,
        "sqft": 766,
        "year_built": 1962,
        "days_on_mls": 13,
        "list_price": 214900,
        "list_date": "2025-01-17",
        "assessed_value": 170000,
        "estimated_value": 203000,
        "tax": 1820,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1820,
            "assessment": {
                "building": 110000,
                "land": 60000,
                "total": 170000
            }
            },
            {
            "year": 2022,
            "tax": 2050,
            "assessment": {
                "building": 130000,
                "land": 60000,
                "total": 190000
            }
            },
            {
            "year": 2021,
            "tax": 1660,
            "assessment": {
                "building": 100000,
                "land": 55000,
                "total": 155000
            }
            },
            {
            "year": 2020,
            "tax": 1560,
            "assessment": {
                "building": 95000,
                "land": 50000,
                "total": 145000
            }
            },
            {
            "year": 2019,
            "tax": 1055,
            "assessment": {
                "building": 65000,
                "land": 35000,
                "total": 100000
            }
            },
            {
            "year": 2018,
            "tax": 943,
            "assessment": {
                "building": 60000,
                "land": 30000,
                "total": 90000
            }
            },
            {
            "year": 2017,
            "tax": 942,
            "assessment": {
                "building": 60000,
                "land": 30000,
                "total": 90000
            }
            },
            {
            "year": 2016,
            "tax": 825,
            "assessment": {
                "building": 55000,
                "land": 30000,
                "total": 85000
            }
            },
            {
            "year": 2015,
            "tax": 816,
            "assessment": {
                "building": 53000,
                "land": 30000,
                "total": 83000
            }
            },
            {
            "year": 2014,
            "tax": 568,
            "assessment": {
                "building": 40000,
                "land": 20000,
                "total": 60000
            }
            },
            {
            "year": 2013,
            "tax": 401,
            "assessment": {
                "building": 24000,
                "land": 20000,
                "total": 44000
            }
            },
            {
            "year": 2012,
            "tax": 385,
            "assessment": {
                "building": 26000,
                "land": 18000,
                "total": 44000
            }
            },
            {
            "year": 2010,
            "tax": 773,
            "assessment": {
                "building": 50000,
                "land": 30000,
                "total": 80000
            }
            },
            {
            "year": 2009,
            "tax": 1107,
            "assessment": {
                "building": 50000,
                "land": 30000,
                "total": 80000
            }
            },
            {
            "year": 2008,
            "tax": 1196,
            "assessment": {
                "building": 98940,
                "land": 66300,
                "total": 165240
            }
            }
        ],
        "lot_sqft": 871,
        "price_per_sqft": 281,
        "latitude": 39.760202,
        "longitude": -121.866697,
        "county": "Butte",
        "hoa_fee": 437,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/ed036a4b7d22090e17ec859c2aab60f0l-b2669991071od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4176
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/24-Westgrove-Ct_Chico_CA_95973_M10635-57636",
        "property_id": "1063557636",
        "listing_id": "2977360032",
        "mls": "MRCA",
        "mls_id": "SN25011659",
        "status": "FOR_SALE",
        "text": "This home is an absolute gem! Nestled on a 360 degree private lot with mature landscaping, it is truly an oasis yet still close to town. The spacious 4-bedroom layout, plus an office, provides ample space for any family. It also offers 3 full bathrooms which is hard to find. The open floor plan with a generous dining area and a bright living room, complete with a skylight and cozy fireplace, is perfect for both relaxation and entertaining. The primary suite, with its large walk-in shower featuring dual shower heads and sinks, is an ideal place to unwind. Plus, the large laundry room with tons of cabinetry for storage is a major bonus. The whole house fan is a thoughtful touch for keeping the temperature just right year-round. There is a 3-car garage, with a 1 car garage access to the backyard. You will want to spend your days out BBQing and playing in the pool with its 3 waterfalls. The outdoor kitchen has a BBQ, fridge, stovetop, sink and pullout trash compartment. This home is ideal for entertaining and enjoying the outdoors. Do not miss out on this stunning home!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "24 Westgrove Ct",
        "street": "24 Westgrove Ct",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 4,
        "full_baths": 3,
        "half_baths": 0,
        "sqft": 2464,
        "year_built": 2003,
        "days_on_mls": 13,
        "list_price": 779000,
        "list_date": "2025-01-17",
        "assessed_value": 426565,
        "estimated_value": 713600,
        "tax": 4677,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4677,
            "assessment": {
                "building": 361658,
                "land": 64907,
                "total": 426565
            }
            },
            {
            "year": 2022,
            "tax": 4601,
            "assessment": {
                "building": 354567,
                "land": 63635,
                "total": 418202
            }
            },
            {
            "year": 2021,
            "tax": 4513,
            "assessment": {
                "building": 347615,
                "land": 62388,
                "total": 410003
            }
            },
            {
            "year": 2020,
            "tax": 4499,
            "assessment": {
                "building": 344051,
                "land": 61749,
                "total": 405800
            }
            },
            {
            "year": 2019,
            "tax": 4416,
            "assessment": {
                "building": 337305,
                "land": 60539,
                "total": 397844
            }
            },
            {
            "year": 2018,
            "tax": 4334,
            "assessment": {
                "building": 330692,
                "land": 59352,
                "total": 390044
            }
            },
            {
            "year": 2017,
            "tax": 4244,
            "assessment": {
                "building": 324208,
                "land": 58189,
                "total": 382397
            }
            },
            {
            "year": 2016,
            "tax": 3872,
            "assessment": {
                "building": 317851,
                "land": 57049,
                "total": 374900
            }
            },
            {
            "year": 2015,
            "tax": 3871,
            "assessment": {
                "building": 313077,
                "land": 56193,
                "total": 369270
            }
            },
            {
            "year": 2014,
            "tax": 3789,
            "assessment": {
                "building": 306945,
                "land": 55093,
                "total": 362038
            }
            },
            {
            "year": 2013,
            "tax": 3845,
            "assessment": {
                "building": 305558,
                "land": 54845,
                "total": 360403
            }
            },
            {
            "year": 2012,
            "tax": 3621,
            "assessment": {
                "building": 299567,
                "land": 53770,
                "total": 353337
            }
            },
            {
            "year": 2010,
            "tax": 3580,
            "assessment": {
                "building": 293694,
                "land": 52716,
                "total": 346410
            }
            },
            {
            "year": 2009,
            "tax": 3643,
            "assessment": {
                "building": 291500,
                "land": 52323,
                "total": 343823
            }
            },
            {
            "year": 2008,
            "tax": 3516,
            "assessment": {
                "building": 286464,
                "land": 51420,
                "total": 337884
            }
            },
            {
            "year": 2007,
            "tax": 3420,
            "assessment": {
                "building": 280848,
                "land": 50412,
                "total": 331260
            }
            }
        ],
        "lot_sqft": 16988,
        "price_per_sqft": 316,
        "latitude": 39.76228,
        "longitude": -121.86976,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/2ad0a82c79f9ebfabac39bd9e06a16f4l-m2074178032od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2942
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1524-Muir-Ave_Chico_CA_95973_M97896-30052",
        "property_id": "9789630052",
        "listing_id": "2977409626",
        "mls": "MRCA",
        "mls_id": "SN25012534",
        "status": "FOR_SALE",
        "text": "If you are looking for a home in the country but close to town, then look no farther! This quaint home, which has updates, such as windows and electrical is located 15 minutes from grocery stores, schools and shopping. Plus, you will own 30 acres of farmland that is currently planted to mature almonds. There is a 60 H.P. electric pump and Ag well with a solid set irrigation system.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "1524 Muir Ave",
        "street": "1524 Muir Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 2,
        "full_baths": 1,
        "half_baths": 0,
        "sqft": 1093,
        "year_built": 1953,
        "days_on_mls": 11,
        "list_price": 850000,
        "list_date": "2025-01-19",
        "assessed_value": 0,
        "estimated_value": 835165,
        "tax": 0,
        "tax_history": 0,
        "lot_sqft": 1306800,
        "price_per_sqft": 778,
        "latitude": 39.739471,
        "longitude": -121.903534,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/cc1fc6dc64a9a9620486951eadf22eb8l-m1353574583od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1499
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/290-E-2nd-Ave_Chico_CA_95926_M28196-14751",
        "property_id": "2819614751",
        "listing_id": "2977372081",
        "mls": "MRCA",
        "mls_id": "SN25011107",
        "status": "PENDING",
        "text": "This charming duplex in the Avenues offers endless possibilities, whether youre looking to live in one unit and rent the other or maximize rental income from both. Situated on a corner lot with a classic picket fence and a beautifully landscaped yard, the property features a 2-bedroom, 1-bath unit and a studio. The 2/1 is adorable and has been tastefully updated with new luxury vinyl plank flooring, cozy carpet in the front bedroom, fresh paint, dual-pane windows (except one), updated bathroom flooring, modern light fixtures, and ceiling fans throughout plus new tile backsplash in the kitchen. It also includes a full-size washer and dryer. The studio unit is equally delightful, featuring a full kitchen with a dining nook, and a stackable washer and dryer in a laundry room off the kitchen. Both units have private front and backyard spaces and separate gas and electric meters for easy management. Additional features include a double car size converted garage thats perfect for a workshop or hobbies, fresh paint on both porches, a new roof on the house and garage in 2019, and front yard sprinklers. Dont miss this fantastic opportunity in one of the most charming neighborhoods around!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "290 E 2nd Ave",
        "street": "290 E 2nd Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1263,
        "year_built": 1913,
        "days_on_mls": 13,
        "list_price": 389500,
        "list_date": "2025-01-17",
        "assessed_value": 169041,
        "estimated_value": 310400,
        "tax": 1891,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1891,
            "assessment": {
                "building": 93912,
                "land": 75129,
                "total": 169041
            }
            },
            {
            "year": 2022,
            "tax": 930,
            "assessment": {
                "building": 92071,
                "land": 73656,
                "total": 165727
            }
            },
            {
            "year": 2021,
            "tax": 1825,
            "assessment": {
                "building": 90266,
                "land": 72212,
                "total": 162478
            }
            },
            {
            "year": 2020,
            "tax": 1820,
            "assessment": {
                "building": 89341,
                "land": 71472,
                "total": 160813
            }
            },
            {
            "year": 2019,
            "tax": 1787,
            "assessment": {
                "building": 87590,
                "land": 70071,
                "total": 157661
            }
            },
            {
            "year": 2018,
            "tax": 1754,
            "assessment": {
                "building": 85873,
                "land": 68698,
                "total": 154571
            }
            },
            {
            "year": 2017,
            "tax": 1718,
            "assessment": {
                "building": 84190,
                "land": 67351,
                "total": 151541
            }
            },
            {
            "year": 2016,
            "tax": 1569,
            "assessment": {
                "building": 82540,
                "land": 66031,
                "total": 148571
            }
            },
            {
            "year": 2015,
            "tax": 1569,
            "assessment": {
                "building": 81301,
                "land": 65040,
                "total": 146341
            }
            },
            {
            "year": 2014,
            "tax": 1531,
            "assessment": {
                "building": 79709,
                "land": 63766,
                "total": 143475
            }
            },
            {
            "year": 2013,
            "tax": 1549,
            "assessment": {
                "building": 79349,
                "land": 63478,
                "total": 142827
            }
            },
            {
            "year": 2012,
            "tax": 1459,
            "assessment": {
                "building": 77794,
                "land": 62234,
                "total": 140028
            }
            },
            {
            "year": 2010,
            "tax": 1369,
            "assessment": {
                "building": 76269,
                "land": 61014,
                "total": 137283
            }
            },
            {
            "year": 2009,
            "tax": 1393,
            "assessment": {
                "building": 75699,
                "land": 60558,
                "total": 136257
            }
            },
            {
            "year": 2008,
            "tax": 1343,
            "assessment": {
                "building": 74392,
                "land": 59512,
                "total": 133904
            }
            },
            {
            "year": 2007,
            "tax": 1306,
            "assessment": {
                "building": 72934,
                "land": 58346,
                "total": 131280
            }
            }
        ],
        "lot_sqft": 4792,
        "price_per_sqft": 308,
        "latitude": 39.740315,
        "longitude": -121.843625,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/c12d9f8dd0227cfb656649d7968a3c9dl-m850129298od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4393
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/894-Liberty-Ln_Chico_CA_95928_M18029-88468",
        "property_id": "1802988468",
        "listing_id": "2977368326",
        "mls": "MRCA",
        "mls_id": "SN25011892",
        "status": "FOR_SALE",
        "text": "Welcome to a truly unique property that offers not just one, but two homes on a sprawling 10-acre lot, providing privacy, tranquility, and endless opportunities. Nestled in a prime location just 5 minutes from Downtown Chico, this property combines the charm of country living with the convenience of City amenities. The two homes are thoughtfully positioned on opposite sides of the property, separated by a picturesque Almond Orchard, ensuring ultimate privacy for both residences. The fertile soil opens the door to countless possibilities - whether you envision expanding the orchard, cultivating a garden, or creating your dream homestead. Everything you need for Almond production is already in place, making this property a turnkey opportunity for agricultural enthusiasts. The main home, 894 Liberty Ln, exudes charm and functionality. A welcoming covered front porch is the perfect spot to enjoy your morning coffee or relax at the end of the day. Inside, you'll find a fantastic layout featuring a primary bedroom suite on the main floor, offering convenience and comfort. Upstairs, 2 additional bedrooms, a guest bathroom, and a spacious open loft with built-in desks create endless possibilities for an office, playroom, or craft space. Outside, a detached 3-car garage with a built-in workshop is ideal for car enthusiasts or those who need space to tinker and create. The second home, 2405 Chico River Rd, is a wonderful home, perfect for generating rental income to offset your mortgage. This charming 2-bedroom, 1-bathroom house features its own detached 2-car garage and a fenced backyard. Its appeal is evident - the 2024 Rental Agreement was rented at $1, 700 per month. Situated off Chico River Rd, this property offers the best of both worlds: a peaceful retreat with all the space and privacy you could want, just minutes from Chico's amenities, schools, and easy freeway access. Whether you're looking for a multigenerational living setup, an income-producing opportunity, or your own slice of paradise, this property has it all. Don't miss the chance to make it yours - schedule your private tour today!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "894 Liberty Ln",
        "street": "894 Liberty Ln",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 5,
        "full_baths": 4,
        "half_baths": 0,
        "sqft": 2896,
        "year_built": 1994,
        "days_on_mls": 13,
        "list_price": 875000,
        "list_date": "2025-01-17",
        "assessed_value": 589481,
        "estimated_value": 859558,
        "tax": 6835,
        "tax_history": [
            {
            "year": 2023,
            "tax": 6835,
            "assessment": {
                "building": 321531,
                "land": 267950,
                "total": 589481
            }
            },
            {
            "year": 2022,
            "tax": 6850,
            "assessment": {
                "building": 455940,
                "land": 408000,
                "total": 863940
            }
            },
            {
            "year": 2021,
            "tax": 6687,
            "assessment": {
                "building": 315226,
                "land": 262696,
                "total": 577922
            }
            },
            {
            "year": 2020,
            "tax": 6683,
            "assessment": {
                "building": 311995,
                "land": 260003,
                "total": 571998
            }
            },
            {
            "year": 2019,
            "tax": 6584,
            "assessment": {
                "building": 305879,
                "land": 254905,
                "total": 560784
            }
            },
            {
            "year": 2018,
            "tax": 6395,
            "assessment": {
                "building": 299883,
                "land": 249907,
                "total": 549790
            }
            },
            {
            "year": 2017,
            "tax": 6301,
            "assessment": {
                "building": 294004,
                "land": 245007,
                "total": 539011
            }
            },
            {
            "year": 2016,
            "tax": 5783,
            "assessment": {
                "building": 288240,
                "land": 240203,
                "total": 528443
            }
            },
            {
            "year": 2015,
            "tax": 5764,
            "assessment": {
                "building": 283912,
                "land": 236595,
                "total": 520507
            }
            },
            {
            "year": 2014,
            "tax": 5680,
            "assessment": {
                "building": 278351,
                "land": 231961,
                "total": 510312
            }
            },
            {
            "year": 2013,
            "tax": 5134,
            "assessment": {
                "building": 250000,
                "land": 200000,
                "total": 450000
            }
            },
            {
            "year": 2012,
            "tax": 4124,
            "assessment": {
                "building": 179000,
                "land": 200000,
                "total": 379000
            }
            },
            {
            "year": 2010,
            "tax": 4986,
            "assessment": {
                "building": 240000,
                "land": 200000,
                "total": 440000
            }
            },
            {
            "year": 2009,
            "tax": 5335,
            "assessment": {
                "building": 244522,
                "land": 220290,
                "total": 484636
            }
            },
            {
            "year": 2008,
            "tax": 5249,
            "assessment": {
                "building": 240298,
                "land": 216485,
                "total": 476266
            }
            },
            {
            "year": 2007,
            "tax": 5013,
            "assessment": {
                "building": 235587,
                "land": 212241,
                "total": 466929
            }
            }
        ],
        "lot_sqft": 435600,
        "price_per_sqft": 302,
        "latitude": 39.711296,
        "longitude": -121.864226,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/bd2e34e1efc95aac3ae8a9f989e7f58bl-m2041287034od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3286
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/141-W-Lassen-Ave-Apt-4_Chico_CA_95973_M12451-50872",
        "property_id": "1245150872",
        "listing_id": "2977313188",
        "mls": "MRCA",
        "mls_id": "SN25004987",
        "status": "FOR_SALE",
        "text": "Discover modern living in this fully remodeled condo, perfectly located with easy access to all that Chico has to offer! Featuring stylish upgrades throughout. This move-in-ready home offers a bright, open layout, contemporary finishes, and a low-maintenance lifestyle. Whether youre exploring nearby parks, dining downtown, or enjoying local shopping, this condo places you at the heart of it all. Don't wait! This one wont last long!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "141 W Lassen Ave Apt 4",
        "street": "141 W Lassen Ave",
        "unit": "Apt 4",
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 2,
        "full_baths": 1,
        "half_baths": 0,
        "sqft": 766,
        "year_built": 1962,
        "days_on_mls": 14,
        "list_price": 199000,
        "list_date": "2025-01-16",
        "assessed_value": 169000,
        "estimated_value": 189000,
        "tax": 1887,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1887,
            "assessment": {
                "building": 109000,
                "land": 60000,
                "total": 169000
            }
            },
            {
            "year": 2022,
            "tax": 906,
            "assessment": {
                "building": 110270,
                "land": 51528,
                "total": 161798
            }
            },
            {
            "year": 2021,
            "tax": 1779,
            "assessment": {
                "building": 108108,
                "land": 50518,
                "total": 158626
            }
            },
            {
            "year": 2020,
            "tax": 1774,
            "assessment": {
                "building": 107000,
                "land": 50000,
                "total": 157000
            }
            },
            {
            "year": 2019,
            "tax": 452,
            "assessment": {
                "building": 29283,
                "land": 17224,
                "total": 46507
            }
            },
            {
            "year": 2018,
            "tax": 521,
            "assessment": {
                "building": 28709,
                "land": 16887,
                "total": 45596
            }
            },
            {
            "year": 2017,
            "tax": 510,
            "assessment": {
                "building": 28147,
                "land": 16556,
                "total": 44703
            }
            },
            {
            "year": 2016,
            "tax": 466,
            "assessment": {
                "building": 27596,
                "land": 16232,
                "total": 43828
            }
            },
            {
            "year": 2015,
            "tax": 466,
            "assessment": {
                "building": 27182,
                "land": 15989,
                "total": 43171
            }
            },
            {
            "year": 2014,
            "tax": 455,
            "assessment": {
                "building": 26650,
                "land": 15676,
                "total": 42326
            }
            },
            {
            "year": 2013,
            "tax": 457,
            "assessment": {
                "building": 26530,
                "land": 15606,
                "total": 42136
            }
            },
            {
            "year": 2012,
            "tax": 430,
            "assessment": {
                "building": 26010,
                "land": 15300,
                "total": 41310
            }
            },
            {
            "year": 2010,
            "tax": 847,
            "assessment": {
                "building": 25500,
                "land": 15000,
                "total": 40500
            }
            },
            {
            "year": 2009,
            "tax": 1182,
            "assessment": {
                "building": 50000,
                "land": 30000,
                "total": 80000
            }
            },
            {
            "year": 2008,
            "tax": 1270,
            "assessment": {
                "building": 98940,
                "land": 66300,
                "total": 165240
            }
            }
        ],
        "lot_sqft": 871,
        "price_per_sqft": 260,
        "latitude": 39.759883,
        "longitude": -121.86709,
        "county": "Butte",
        "hoa_fee": 437,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/1d0f094b87c441f99a07b294e3801b98l-m2052626819od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1364
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/2612-Burnap-Ave_Chico_CA_95973_M11735-66699",
        "property_id": "1173566699",
        "listing_id": "2977291831",
        "mls": "MRCA",
        "mls_id": "SN25010852",
        "status": "FOR_SALE",
        "text": "Great opportunity to build in CHICO on .25 acre lot. CERTIFIED BUILDING plans are INCLUDED! Whether you are looking to build your forever home or invest in a rental potential in this College Town. DO NOT MISS THIS limitless OPPORTUNITY!",
        "style": "LAND",
        "full_street_line": "2612 Burnap Ave",
        "street": "2612 Burnap Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 0,
        "full_baths": 0,
        "half_baths": 0,
        "sqft": 0,
        "year_built": 0,
        "days_on_mls": 14,
        "list_price": 199000,
        "list_date": "2025-01-16",
        "assessed_value": 221318,
        "estimated_value": 195527,
        "tax": 2468,
        "tax_history": [
            {
            "year": 2023,
            "tax": 2468,
            "assessment": {
                "building": 109962,
                "land": 111356,
                "total": 221318
            }
            },
            {
            "year": 2022,
            "tax": 2428,
            "assessment": {
                "building": 107806,
                "land": 109173,
                "total": 216979
            }
            },
            {
            "year": 2021,
            "tax": 2382,
            "assessment": {
                "building": 105693,
                "land": 107033,
                "total": 212726
            }
            },
            {
            "year": 2020,
            "tax": 2376,
            "assessment": {
                "building": 104610,
                "land": 105936,
                "total": 210546
            }
            },
            {
            "year": 2019,
            "tax": 2332,
            "assessment": {
                "building": 102559,
                "land": 103859,
                "total": 206418
            }
            },
            {
            "year": 2018,
            "tax": 2290,
            "assessment": {
                "building": 100549,
                "land": 101823,
                "total": 202372
            }
            },
            {
            "year": 2017,
            "tax": 2243,
            "assessment": {
                "building": 98578,
                "land": 99827,
                "total": 198405
            }
            },
            {
            "year": 2016,
            "tax": 2047,
            "assessment": {
                "building": 96646,
                "land": 97870,
                "total": 194516
            }
            },
            {
            "year": 2015,
            "tax": 2047,
            "assessment": {
                "building": 95195,
                "land": 96400,
                "total": 191595
            }
            },
            {
            "year": 2014,
            "tax": 1980,
            "assessment": {
                "building": 90000,
                "land": 95000,
                "total": 185000
            }
            },
            {
            "year": 2013,
            "tax": 1737,
            "assessment": {
                "building": 89000,
                "land": 70000,
                "total": 159000
            }
            },
            {
            "year": 2012,
            "tax": 1669,
            "assessment": {
                "building": 99000,
                "land": 60000,
                "total": 159000
            }
            },
            {
            "year": 2010,
            "tax": 1902,
            "assessment": {
                "building": 94000,
                "land": 65000,
                "total": 159000
            }
            },
            {
            "year": 2009,
            "tax": 1935,
            "assessment": {
                "building": 88636,
                "land": 89758,
                "total": 178394
            }
            },
            {
            "year": 2008,
            "tax": 1869,
            "assessment": {
                "building": 87105,
                "land": 88208,
                "total": 175313
            }
            },
            {
            "year": 2007,
            "tax": 1818,
            "assessment": {
                "building": 85398,
                "land": 86479,
                "total": 171877
            }
            }
        ],
        "lot_sqft": 10454,
        "price_per_sqft": 0,
        "latitude": 39.768542,
        "longitude": -121.845908,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/d64c41aa1652ef6816d821fd460cd3ael-b2140376944od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2888
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/Yosemite-Dr_Chico_CA_95928_M99277-31001",
        "property_id": "9927731001",
        "listing_id": "2977202929",
        "mls": "MRCA",
        "mls_id": "SN25008134",
        "status": "FOR_SALE",
        "text": "This is a prime 2.34 acre lot in a prime area of commercial development with Native Oak Dr, Yosemite Dr and Humboldt Rd surrounding the property. The parcel has been subdivided with improvements recently completed including road, curb, gutter and utilities in the frontage, the road has also been extended across the creek. This is a site ready for development next to several other completed projects. Neighboring projects include DR Horton's Sparrow community of 86 homes, Oak Valley subdivision, Lava Ridge Apartments, and other multi-unit projects in the final phases of construction. The property has been subdivided to this final acreage with senior housing planned on the adjacent parcel to the West/South West. This parcel is zoned R2 - Medium density with an allowable density to 14 units and focusing on housing for development compatibility with Chico's general plan. Beautiful location with approximately 2.2 miles to services like Target, Winco and more.",
        "style": "LAND",
        "full_street_line": "Yosemite Dr",
        "street": "Yosemite Dr",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 0,
        "full_baths": 0,
        "half_baths": 0,
        "sqft": 0,
        "year_built": 0,
        "days_on_mls": 15,
        "list_price": 950000,
        "list_date": "2025-01-15",
        "assessed_value": 0,
        "estimated_value": 0,
        "tax": 0,
        "tax_history": 0,
        "lot_sqft": 101930,
        "price_per_sqft": 0,
        "latitude": 39.741569,
        "longitude": -121.779207,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/c27671889cd1ef3fef7507bd698a6166l-m2502485306od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1638
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/3050-Hancock-Dr_Chico_CA_95973_M19635-34153",
        "property_id": "1963534153",
        "listing_id": "2977286643",
        "mls": "MRCA",
        "mls_id": "V1-27581",
        "status": "FOR_SALE",
        "text": "This fabulous turnkey home sits in the highly desirable community of Hancock Park. Seller has spent over $70, 000 on recent upgrades including new roof (2024), owned solar, HVAC, finished studio, newer garage door, interior paint and carpet. This corner home sits on a quiet cul-de-sac with no rear neighbors and one block from lovely park and near hiking and biking trails. The oversized yard features a rear block wall, lush landscape, Japanese Maple and finished Artist Studio. The split floor plan and open kitchen/living/dining area with airy vaulted ceilings gives both privacy and options for group entertaining. The main bedroom features an extra large walk in closed and direct access to the rear yard. An indoor laundry with utility sink offers convenience and functionality while the garage boasts loads of cabinets for extra storage. Conveniently located near restaurants and shopping too!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "3050 Hancock Dr",
        "street": "3050 Hancock Dr",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 1,
        "half_baths": 0,
        "sqft": 1679,
        "year_built": 2000,
        "days_on_mls": 14,
        "list_price": 549000,
        "list_date": "2025-01-16",
        "assessed_value": 399178,
        "estimated_value": 563000,
        "tax": 4998,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4998,
            "assessment": {
                "building": 235133,
                "land": 164045,
                "total": 399178
            }
            },
            {
            "year": 2022,
            "tax": 4772,
            "assessment": {
                "building": 230523,
                "land": 160829,
                "total": 391352
            }
            },
            {
            "year": 2021,
            "tax": 4705,
            "assessment": {
                "building": 226003,
                "land": 157676,
                "total": 383679
            }
            },
            {
            "year": 2020,
            "tax": 4560,
            "assessment": {
                "building": 223686,
                "land": 156060,
                "total": 379746
            }
            },
            {
            "year": 2019,
            "tax": 4439,
            "assessment": {
                "building": 219300,
                "land": 153000,
                "total": 372300
            }
            },
            {
            "year": 2018,
            "tax": 4276,
            "assessment": {
                "building": 215000,
                "land": 150000,
                "total": 365000
            }
            },
            {
            "year": 2017,
            "tax": 2689,
            "assessment": {
                "building": 146576,
                "land": 75297,
                "total": 221873
            }
            },
            {
            "year": 2016,
            "tax": 2423,
            "assessment": {
                "building": 143702,
                "land": 73821,
                "total": 217523
            }
            },
            {
            "year": 2015,
            "tax": 2409,
            "assessment": {
                "building": 141544,
                "land": 72713,
                "total": 214257
            }
            },
            {
            "year": 2014,
            "tax": 2384,
            "assessment": {
                "building": 138772,
                "land": 71289,
                "total": 210061
            }
            },
            {
            "year": 2013,
            "tax": 2329,
            "assessment": {
                "building": 138145,
                "land": 70967,
                "total": 209112
            }
            },
            {
            "year": 2012,
            "tax": 2260,
            "assessment": {
                "building": 135437,
                "land": 69576,
                "total": 205013
            }
            },
            {
            "year": 2010,
            "tax": 2190,
            "assessment": {
                "building": 132782,
                "land": 68212,
                "total": 200994
            }
            },
            {
            "year": 2009,
            "tax": 2253,
            "assessment": {
                "building": 131790,
                "land": 67703,
                "total": 199493
            }
            },
            {
            "year": 2008,
            "tax": 2188,
            "assessment": {
                "building": 129514,
                "land": 66534,
                "total": 196048
            }
            },
            {
            "year": 2007,
            "tax": 2193,
            "assessment": {
                "building": 126975,
                "land": 65230,
                "total": 192205
            }
            }
        ],
        "lot_sqft": 8712,
        "price_per_sqft": 327,
        "latitude": 39.770766,
        "longitude": -121.815745,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/7bf068ad094efdad65cbba319a42c522l-m988121670od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3062
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/917-Christi-Ln_Chico_CA_95973_M22269-63096",
        "property_id": "2226963096",
        "listing_id": "2977238842",
        "mls": "MRCA",
        "mls_id": "SN25009818",
        "status": "FOR_SALE",
        "text": "Nestled in a cul-de-sac close to numerous amenities, 917 Christi Ln offers four 2-bedroom, 1-bathroom units, each just under 900 sq. ft. One unit has been fully remodeled, featuring LVP flooring, quartz countertops, modern fixtures and appliances, fresh paint, and many other desirable updates. Ample street parking is available for tenants, along with a private parking lot in the rear. Dont miss your opportunity to invest in this well-maintained, turnkey property!",
        "style": "MULTI_FAMILY",
        "full_street_line": "917 Christi Ln",
        "street": "917 Christi Ln",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 8,
        "full_baths": 4,
        "half_baths": 0,
        "sqft": 3422,
        "year_built": 1986,
        "days_on_mls": 15,
        "list_price": 699000,
        "list_date": "2025-01-15",
        "assessed_value": 292830,
        "estimated_value": 713000,
        "tax": 3302,
        "tax_history": [
            {
            "year": 2023,
            "tax": 3302,
            "assessment": {
                "building": 225850,
                "land": 66980,
                "total": 292830
            }
            },
            {
            "year": 2022,
            "tax": 3247,
            "assessment": {
                "building": 221422,
                "land": 65667,
                "total": 287089
            }
            },
            {
            "year": 2021,
            "tax": 3187,
            "assessment": {
                "building": 217081,
                "land": 64380,
                "total": 281461
            }
            },
            {
            "year": 2020,
            "tax": 3178,
            "assessment": {
                "building": 214856,
                "land": 63720,
                "total": 278576
            }
            },
            {
            "year": 2019,
            "tax": 3121,
            "assessment": {
                "building": 210644,
                "land": 62471,
                "total": 273115
            }
            },
            {
            "year": 2018,
            "tax": 3065,
            "assessment": {
                "building": 206514,
                "land": 61247,
                "total": 267761
            }
            },
            {
            "year": 2017,
            "tax": 3002,
            "assessment": {
                "building": 202465,
                "land": 60047,
                "total": 262512
            }
            },
            {
            "year": 2016,
            "tax": 2741,
            "assessment": {
                "building": 198496,
                "land": 58870,
                "total": 257366
            }
            },
            {
            "year": 2015,
            "tax": 2741,
            "assessment": {
                "building": 195515,
                "land": 57986,
                "total": 253501
            }
            },
            {
            "year": 2014,
            "tax": 2688,
            "assessment": {
                "building": 191686,
                "land": 56851,
                "total": 248537
            }
            },
            {
            "year": 2013,
            "tax": 2717,
            "assessment": {
                "building": 190820,
                "land": 56595,
                "total": 247415
            }
            },
            {
            "year": 2012,
            "tax": 2561,
            "assessment": {
                "building": 187079,
                "land": 55486,
                "total": 242565
            }
            },
            {
            "year": 2010,
            "tax": 2533,
            "assessment": {
                "building": 183411,
                "land": 54399,
                "total": 237810
            }
            },
            {
            "year": 2009,
            "tax": 2578,
            "assessment": {
                "building": 182041,
                "land": 53993,
                "total": 238034
            }
            },
            {
            "year": 2008,
            "tax": 2490,
            "assessment": {
                "building": 178897,
                "land": 53061,
                "total": 233958
            }
            },
            {
            "year": 2007,
            "tax": 2423,
            "assessment": {
                "building": 175390,
                "land": 52021,
                "total": 229411
            }
            }
        ],
        "lot_sqft": 13068,
        "price_per_sqft": 204,
        "latitude": 39.765222,
        "longitude": -121.84243,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/96157b7307059305e2aa5dd7f95258d5l-m885346794od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1729
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/374-Spanish-Garden-Dr_Chico_CA_95928_M28727-27156",
        "property_id": "2872727156",
        "listing_id": "2977204462",
        "mls": "MRCA",
        "mls_id": "SN25007976",
        "status": "FOR_SALE",
        "text": "Nestled in the heart of Butte Creek Canyon, 374 Spanish Garden Drive offers a tranquil retreat surrounded by natural beauty. This expansive property provides spectacular views from nearly every window. This property features an array of fruit treesincluding Santa Rosa plums, peaches, oranges, lemon and olive trees. Whether enjoying the peaceful sounds of nature or gazing at the breathtaking scenery, this home is the perfect escape from the demands of everyday life. This unique, energy efficient home boasts 7 bedrooms and 5 bathrooms, including an expansive upstairs primary suite and an additional upstairs bedroom. Five more bedrooms are located on the main floor, with two featuring en suite bathrooms. A dedicated home office, complete with built-ins, a desk, and a closet, ensures you have a private space to work or study. Freshly painted walls with an imperfect smooth texture complement tile flooring in the common areas and plush new carpet in the downstairs bedrooms and office. Transoms and skylights throughout bring in an abundance of natural light. Home features separate living and family rooms, a spacious formal dining room with built-in cabinetry, a breakfast nook, and a stunning kitchen with a massive island and eating bar. The chefs kitchen is outfitted with double ovens, a Dacor gas (propane) range with six burners, a prep sink, a walk-in pantry, and a built-in pizza oven. Large laundry room offers ample storage, while a finished basement could be your dream wine cellar. The radiant floor heating system is managed by 14 Nest Learning Thermostats. Additionally, there is central air conditioning, and an Earth Cooling system, plus two wood-burning fireplaces (one with a gas option). Home is wired with Ethernet and coax cables for networking and surveillance capabilities, alongside a distributed Wi-Fi system. The property also features an attached 3-car garage, a large circular driveway with ample parking, and thoughtful plans for a future pool, complete with a pool house for storage and equipment. Theres even potential to restore a pond at the rear of the property. This home was meticulously crafted by esteemed local contractor Steve Ferreira using Insulated Concrete Form (ICF) construction for superior insulation and durability. With a tile roof and owned solar system comprising 52 panels, this home is as sustainable as it is stunning. Discover luxury, comfort, and sustainability in this extraordinary Chico residence!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "374 Spanish Garden Dr",
        "street": "374 Spanish Garden Dr",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 7,
        "full_baths": 5,
        "half_baths": 0,
        "sqft": 5643,
        "year_built": 2001,
        "days_on_mls": 16,
        "list_price": 1275000,
        "list_date": "2025-01-14",
        "assessed_value": 987232,
        "estimated_value": 1292000,
        "tax": 10926,
        "tax_history": [
            {
            "year": 2023,
            "tax": 10926,
            "assessment": {
                "building": 708353,
                "land": 278879,
                "total": 987232
            }
            },
            {
            "year": 2022,
            "tax": 10743,
            "assessment": {
                "building": 694464,
                "land": 273411,
                "total": 967875
            }
            },
            {
            "year": 2021,
            "tax": 10539,
            "assessment": {
                "building": 680848,
                "land": 268050,
                "total": 948898
            }
            },
            {
            "year": 2020,
            "tax": 10509,
            "assessment": {
                "building": 673867,
                "land": 265302,
                "total": 939169
            }
            },
            {
            "year": 2019,
            "tax": 10316,
            "assessment": {
                "building": 660654,
                "land": 260100,
                "total": 920754
            }
            },
            {
            "year": 2018,
            "tax": 10126,
            "assessment": {
                "building": 647700,
                "land": 255000,
                "total": 902700
            }
            },
            {
            "year": 2017,
            "tax": 8726,
            "assessment": {
                "building": 534914,
                "land": 244173,
                "total": 779087
            }
            },
            {
            "year": 2016,
            "tax": 7961,
            "assessment": {
                "building": 524426,
                "land": 239386,
                "total": 763812
            }
            },
            {
            "year": 2015,
            "tax": 7960,
            "assessment": {
                "building": 516549,
                "land": 235791,
                "total": 752340
            }
            },
            {
            "year": 2014,
            "tax": 7766,
            "assessment": {
                "building": 506431,
                "land": 231173,
                "total": 737604
            }
            },
            {
            "year": 2013,
            "tax": 7892,
            "assessment": {
                "building": 504143,
                "land": 230129,
                "total": 734272
            }
            },
            {
            "year": 2012,
            "tax": 7433,
            "assessment": {
                "building": 494258,
                "land": 225617,
                "total": 719875
            }
            },
            {
            "year": 2010,
            "tax": 7350,
            "assessment": {
                "building": 484567,
                "land": 221194,
                "total": 705761
            }
            },
            {
            "year": 2009,
            "tax": 7480,
            "assessment": {
                "building": 480946,
                "land": 219541,
                "total": 700487
            }
            },
            {
            "year": 2008,
            "tax": 7220,
            "assessment": {
                "building": 472637,
                "land": 215749,
                "total": 688386
            }
            },
            {
            "year": 2007,
            "tax": 7023,
            "assessment": {
                "building": 463370,
                "land": 211519,
                "total": 674889
            }
            }
        ],
        "lot_sqft": 269636,
        "price_per_sqft": 226,
        "latitude": 39.706374,
        "longitude": -121.747822,
        "county": "Butte",
        "hoa_fee": 44,
        "nearby_schools": "Butte County Office Of Education School District, Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/f4ddcdcc60013dcc12215fa7597b6e5dl-b4058415459od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1771
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/125-Hampshire-Dr_Chico_CA_95926_M28164-41365",
        "property_id": "2816441365",
        "listing_id": "2977119752",
        "mls": "MRCA",
        "mls_id": "OR25006269",
        "status": "CONTINGENT",
        "text": "Welcome to Hollybrook estates, a sought after community where this charming storybook-style home is nestled. Its a vibrant, walkable community with mature landscaping that is located minutes from downtown Chico. The delightful 2-bedroom, 2-bathroom home boasts vaulted ceilings in the living area and updates including a newer roof, HVAC system, and a whole house fan. The HOA takes care of front yard landscaping, street-facing fences, and septic system maintenance, ensuring a low-maintenance lifestyle. Experience the perfect blend of charm and convenience in this truly enchanting home. Come check it out before its gone!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "125 Hampshire Dr",
        "street": "125 Hampshire Dr",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 2,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1034,
        "year_built": 1985,
        "days_on_mls": 19,
        "list_price": 405000,
        "list_date": "2025-01-11",
        "assessed_value": 385000,
        "estimated_value": 402758,
        "tax": 4302,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4302,
            "assessment": {
                "building": 190000,
                "land": 195000,
                "total": 385000
            }
            },
            {
            "year": 2022,
            "tax": 2684,
            "assessment": {
                "building": 171788,
                "land": 72507,
                "total": 244295
            }
            },
            {
            "year": 2021,
            "tax": 2633,
            "assessment": {
                "building": 168420,
                "land": 71086,
                "total": 239506
            }
            },
            {
            "year": 2020,
            "tax": 3292,
            "assessment": {
                "building": 142800,
                "land": 147900,
                "total": 290700
            }
            },
            {
            "year": 2019,
            "tax": 3232,
            "assessment": {
                "building": 140000,
                "land": 145000,
                "total": 285000
            }
            },
            {
            "year": 2018,
            "tax": 2841,
            "assessment": {
                "building": 130000,
                "land": 120000,
                "total": 250000
            }
            },
            {
            "year": 2017,
            "tax": 2565,
            "assessment": {
                "building": 110000,
                "land": 115000,
                "total": 225000
            }
            },
            {
            "year": 2016,
            "tax": 2231,
            "assessment": {
                "building": 105000,
                "land": 105000,
                "total": 210000
            }
            },
            {
            "year": 2015,
            "tax": 2265,
            "assessment": {
                "building": 110000,
                "land": 100000,
                "total": 210000
            }
            },
            {
            "year": 2014,
            "tax": 2161,
            "assessment": {
                "building": 105000,
                "land": 95000,
                "total": 200000
            }
            },
            {
            "year": 2013,
            "tax": 1981,
            "assessment": {
                "building": 95000,
                "land": 85000,
                "total": 180000
            }
            },
            {
            "year": 2012,
            "tax": 1728,
            "assessment": {
                "building": 90000,
                "land": 80000,
                "total": 170000
            }
            },
            {
            "year": 2010,
            "tax": 2285,
            "assessment": {
                "building": 100000,
                "land": 100000,
                "total": 200000
            }
            },
            {
            "year": 2009,
            "tax": 2481,
            "assessment": {
                "building": 110000,
                "land": 125000,
                "total": 235000
            }
            },
            {
            "year": 2008,
            "tax": 2634,
            "assessment": {
                "building": 123000,
                "land": 130000,
                "total": 253000
            }
            },
            {
            "year": 2007,
            "tax": 3193,
            "assessment": {
                "building": 155040,
                "land": 153000,
                "total": 308040
            }
            }
        ],
        "lot_sqft": 6970,
        "price_per_sqft": 392,
        "latitude": 39.729139,
        "longitude": -121.864078,
        "county": "Butte",
        "hoa_fee": 246,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/f02aa886374fe15fc428441b9380e98al-m268172095od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4581
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/9-Hidden-Grove-Ct_Chico_CA_95926_M25062-28716",
        "property_id": "2506228716",
        "listing_id": "2977222684",
        "mls": "MRCA",
        "mls_id": "SN25008067",
        "status": "PENDING",
        "text": "Nestled on a quiet cul-de-sac in the sought-after Estates at Hooker Oak subdivision, 9 Hidden Grove Ct is a home that truly makes a statement. Built by the renowned Chico Lifestyle Builders, this stunning property blends style, comfort, and functionality. From the moment you arrive, the beautifully landscaped front yard and inviting formal entry set the tone for the elegance that awaits inside. The open living room greets you with soaring ceilings, warm LVP flooring, and a striking rock-surround gas fireplace that serves as the centerpiece. Sliding barn doors open to an oversized covered patio, seamlessly blending indoor and outdoor living. The kitchen is a chef's dream, showcasing gorgeous granite countertops, rich cherry cabinetry, and top-of-the-line appliances, including a built-in gas range, microwave, and electric oven. The spacious dining area, with French doors leading to a versatile bonus room, makes entertaining a breeze. This addition is perfect for a second living space, playroom, or game room - options are endless. The split floor plan offers privacy and convenience. One bedroom, a full bathroom, and the laundry room are located near the kitchen, while the primary suite, two additional bedrooms, and another bathroom are on the opposite side of the home. The primary suite is a luxurious retreat featuring a tray ceiling, an en-suite with dual granite-toped vanities, a walk-in shower, a relaxing soaking tub, and a large walk-in closet. Head outside into your private oasis, where relaxation and entertainment come together seamlessly. The oversized covered patio features a fully equipped outdoor kitchen with bar-top seating, making it the ideal spot for hosting game-day gatherings or enjoying a quiet evening outdoors. Take a refreshing dip in the sparkling saltwater pool with a baja shelf, perfect for lounging on sunny days. Find year-round delights throughout the backyard, such as mature fruit trees and patches of Dutchmans pipevine, beckoning Swallowtail butterflies to visit each spring. Other highlights include a charming chicken coop, a high-speed electric car charger in the garage, a whole house fan for added comfort, and the incredible benefit of OWNED solar for energy efficiency and savings. Just blocks from Upper and Lower Bidwell Park, Sierra View Elementary, and Hooker Oak Park. This home is a dream for outdoor enthusiasts! Don't miss your chance to call this remarkable property home - schedule your private showing today!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "9 Hidden Grove Ct",
        "street": "9 Hidden Grove Ct",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 4,
        "full_baths": 3,
        "half_baths": 0,
        "sqft": 2581,
        "year_built": 2015,
        "days_on_mls": 16,
        "list_price": 849000,
        "list_date": "2025-01-14",
        "assessed_value": 628480,
        "estimated_value": 723600,
        "tax": 7120,
        "tax_history": [
            {
            "year": 2023,
            "tax": 7120,
            "assessment": {
                "building": 446430,
                "land": 182050,
                "total": 628480
            }
            },
            {
            "year": 2022,
            "tax": 6264,
            "assessment": {
                "building": 388657,
                "land": 178481,
                "total": 567138
            }
            },
            {
            "year": 2021,
            "tax": 6407,
            "assessment": {
                "building": 381037,
                "land": 174982,
                "total": 556019
            }
            },
            {
            "year": 2020,
            "tax": 6483,
            "assessment": {
                "building": 377130,
                "land": 173188,
                "total": 550318
            }
            },
            {
            "year": 2019,
            "tax": 6347,
            "assessment": {
                "building": 369736,
                "land": 169793,
                "total": 539529
            }
            },
            {
            "year": 2018,
            "tax": 7021,
            "assessment": {
                "building": 362487,
                "land": 166464,
                "total": 528951
            }
            },
            {
            "year": 2017,
            "tax": 5443,
            "assessment": {
                "building": 325380,
                "land": 163200,
                "total": 488580
            }
            },
            {
            "year": 2016,
            "tax": 5607,
            "assessment": {
                "building": 305000,
                "land": 126322,
                "total": 431322
            }
            }
        ],
        "lot_sqft": 10454,
        "price_per_sqft": 329,
        "latitude": 39.757836,
        "longitude": -121.802651,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/282817c7acbc7aa44d8de1a2c3a5ea61l-m1308050129od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3244
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/3065-Sweetwater-Fls_Chico_CA_95973_M28959-85658",
        "property_id": "2895985658",
        "listing_id": "2977204450",
        "mls": "MRCA",
        "mls_id": "SN25008412",
        "status": "PENDING",
        "text": "This wonderful, craftsman style home is not only darling... it's in an absolutely fabulous location! Close proximity to all services as well as Upper and Lower Bidwell Park! Far enough from the main roads to be quiet, but close enough for convenience to most Chico locations. The versatile floorplan features a front room that works as a formal living/dining space, or an office area. Through the archway, the kitchen opens up to a light-filled 'great-room' with a large open family room and views to the rear yard. The kitchen is the ideal blend of form and function with light granite counters, nuetral tile flooring, tall ceilings filled with indirect lighting, TONS of cabinet space, as well and a large island and a pantry. The family room features the same tall ceilings, nook area (perfect for the TV!) and glass door out the great covered patio! The two guest bedrooms are across from the guest bath while the primary suite is tucked in at the end of the hall for a bit of privacy. It has it's own fabulous bath complete with granite counters with double sinks, walk in closet, private toilet, and HUGE walk-in shower. A set of glass doors leads to the outdoor living area and rear yard, which is set up for easy care with concrete patio, pathways, full mow strips, and sprinklers. Plus your own mini orchard with a lemon, plum and apricot tree! Don't miss this 'turn key' home in lovely Sycamore Glen!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "3065 Sweetwater Fls",
        "street": "3065 Sweetwater Fls",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1543,
        "year_built": 2013,
        "days_on_mls": 16,
        "list_price": 499000,
        "list_date": "2025-01-14",
        "assessed_value": 479000,
        "estimated_value": 503466,
        "tax": 3791,
        "tax_history": [
            {
            "year": 2023,
            "tax": 3791,
            "assessment": {
                "building": 309000,
                "land": 170000,
                "total": 479000
            }
            },
            {
            "year": 2022,
            "tax": 3582,
            "assessment": {
                "building": 192158,
                "land": 110234,
                "total": 302392
            }
            },
            {
            "year": 2021,
            "tax": 3421,
            "assessment": {
                "building": 188391,
                "land": 108073,
                "total": 296464
            }
            },
            {
            "year": 2020,
            "tax": 3407,
            "assessment": {
                "building": 186460,
                "land": 106965,
                "total": 293425
            }
            },
            {
            "year": 2019,
            "tax": 3318,
            "assessment": {
                "building": 182804,
                "land": 104868,
                "total": 287672
            }
            },
            {
            "year": 2018,
            "tax": 3222,
            "assessment": {
                "building": 179220,
                "land": 102812,
                "total": 282032
            }
            },
            {
            "year": 2017,
            "tax": 3156,
            "assessment": {
                "building": 175706,
                "land": 100797,
                "total": 276503
            }
            },
            {
            "year": 2016,
            "tax": 3310,
            "assessment": {
                "building": 172261,
                "land": 98821,
                "total": 271082
            }
            },
            {
            "year": 2015,
            "tax": 3050,
            "assessment": {
                "building": 169674,
                "land": 97337,
                "total": 267011
            }
            },
            {
            "year": 2014,
            "tax": 2963,
            "assessment": {
                "building": 166351,
                "land": 95431,
                "total": 261782
            }
            },
            {
            "year": 2013,
            "tax": 1516,
            "assessment": {
                "building": 104000,
                "land": 35867,
                "total": 139867
            }
            }
        ],
        "lot_sqft": 4792,
        "price_per_sqft": 323,
        "latitude": 39.770024,
        "longitude": -121.821554,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/d61d4f7823023df000cbd61a638c964al-m1243409955od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2395
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/955-Aspen-St_Chico_CA_95928_M29429-27755",
        "property_id": "2942927755",
        "listing_id": "2977179779",
        "mls": "BECA",
        "mls_id": "225003276",
        "status": "CONTINGENT",
        "text": "INCOME PRODUCING MULIT-FAMILY for an incredible price! Easy to rent due to its proximity to Chico State campus and Bidwell Park. Completely renovated throughout. Front unit has 2 large bedrooms and office that can be easily converted to a 3rd bedroom. White and bright kitchen with newer appliances. Separate entrances and parking for both units. HUGE BACKYARD that's pet friendly with a wood security fence to keep your fur babies safe. Back unit includes separate bedroom, living space, full bath and white kitchen. It's the perfect investment property for someone looking for another stream of income or can be used as a single-family with a guest house for kids/in-laws. This opportunity will not last long!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "955 Aspen St",
        "street": "955 Aspen St",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1215,
        "year_built": 1942,
        "days_on_mls": 17,
        "list_price": 385000,
        "list_date": "2025-01-13",
        "assessed_value": 358938,
        "estimated_value": 378205,
        "tax": 4023,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4023,
            "assessment": {
                "building": 192474,
                "land": 166464,
                "total": 358938
            }
            },
            {
            "year": 2022,
            "tax": 3958,
            "assessment": {
                "building": 188700,
                "land": 163200,
                "total": 351900
            }
            },
            {
            "year": 2021,
            "tax": 3338,
            "assessment": {
                "building": 157161,
                "land": 139126,
                "total": 296287
            }
            },
            {
            "year": 2020,
            "tax": 3329,
            "assessment": {
                "building": 155550,
                "land": 137700,
                "total": 293250
            }
            },
            {
            "year": 2019,
            "tax": 3270,
            "assessment": {
                "building": 152500,
                "land": 135000,
                "total": 287500
            }
            },
            {
            "year": 2018,
            "tax": 277,
            "assessment": {
                "building": 21703,
                "land": 7486,
                "total": 29189
            }
            },
            {
            "year": 2017,
            "tax": 269,
            "assessment": {
                "building": 21278,
                "land": 7340,
                "total": 28618
            }
            },
            {
            "year": 2016,
            "tax": 247,
            "assessment": {
                "building": 20861,
                "land": 7197,
                "total": 28058
            }
            },
            {
            "year": 2015,
            "tax": 245,
            "assessment": {
                "building": 20548,
                "land": 7089,
                "total": 27637
            }
            },
            {
            "year": 2014,
            "tax": 253,
            "assessment": {
                "building": 20146,
                "land": 6951,
                "total": 27097
            }
            },
            {
            "year": 2013,
            "tax": 237,
            "assessment": {
                "building": 20055,
                "land": 6920,
                "total": 26975
            }
            },
            {
            "year": 2012,
            "tax": 220,
            "assessment": {
                "building": 19662,
                "land": 6785,
                "total": 26447
            }
            },
            {
            "year": 2010,
            "tax": 214,
            "assessment": {
                "building": 19277,
                "land": 6652,
                "total": 25929
            }
            },
            {
            "year": 2009,
            "tax": 218,
            "assessment": {
                "building": 19133,
                "land": 6603,
                "total": 25736
            }
            },
            {
            "year": 2008,
            "tax": 213,
            "assessment": {
                "building": 18803,
                "land": 6490,
                "total": 25293
            }
            },
            {
            "year": 2007,
            "tax": 203,
            "assessment": {
                "building": 18435,
                "land": 6363,
                "total": 24798
            }
            }
        ],
        "lot_sqft": 6098,
        "price_per_sqft": 317,
        "latitude": 39.731169,
        "longitude": -121.82505,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/0037d0825b0ecd2dd2f9c3d6ab98b3a2l-m2683060120od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2134
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/2099-Hartford-Dr-Unit-5_Chico_CA_95928_M15141-97895",
        "property_id": "1514197895",
        "listing_id": "2977204500",
        "mls": "MRCA",
        "mls_id": "SN25008690",
        "status": "PENDING",
        "text": "Welcome to this move in ready 3 bedroom/2 bath townhome near Meriam Park, the Chico Mall and Costco! This centrally located Chico condo boasts lovely laminate floors, window coverings throughout, and indoor laundry for added convenience and privacy! As you step through the front doors, you will appreciate a spacious living room with a sliding glass door that leads to a quaint private patio, perfect for barbecues or patio relaxation! The kitchen is located just off the living area and boasts generous counter space and cabinets. One full bath rests downstairs with the washer and dryer, while the remaining second bathroom and three bedrooms await upstairs. The property is priced to sell and conveniently located with easy access to freeways, Costco, restaurants, gyms, historic Lower Bidwell Park, and walkable to all the new restaurants and night life offered in Meriam Park! Don't let this fantastic townhome pass you by!",
        "style": "TOWNHOMES",
        "full_street_line": "2099 Hartford Dr Unit 5",
        "street": "2099 Hartford Dr",
        "unit": "Unit 5",
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1375,
        "year_built": 2005,
        "days_on_mls": 16,
        "list_price": 259000,
        "list_date": "2025-01-14",
        "assessed_value": 255433,
        "estimated_value": 303000,
        "tax": 2971,
        "tax_history": [
            {
            "year": 2023,
            "tax": 2971,
            "assessment": {
                "building": 187108,
                "land": 68325,
                "total": 255433
            }
            },
            {
            "year": 2022,
            "tax": 2905,
            "assessment": {
                "building": 183440,
                "land": 66986,
                "total": 250426
            }
            },
            {
            "year": 2021,
            "tax": 2838,
            "assessment": {
                "building": 179844,
                "land": 65673,
                "total": 245517
            }
            },
            {
            "year": 2020,
            "tax": 2816,
            "assessment": {
                "building": 178000,
                "land": 65000,
                "total": 243000
            }
            },
            {
            "year": 2019,
            "tax": 2745,
            "assessment": {
                "building": 145000,
                "land": 85000,
                "total": 230000
            }
            },
            {
            "year": 2018,
            "tax": 2352,
            "assessment": {
                "building": 135000,
                "land": 65000,
                "total": 200000
            }
            },
            {
            "year": 2017,
            "tax": 2346,
            "assessment": {
                "building": 115000,
                "land": 80000,
                "total": 195000
            }
            },
            {
            "year": 2016,
            "tax": 2032,
            "assessment": {
                "building": 110000,
                "land": 65000,
                "total": 175000
            }
            },
            {
            "year": 2015,
            "tax": 1886,
            "assessment": {
                "building": 115000,
                "land": 45000,
                "total": 160000
            }
            },
            {
            "year": 2014,
            "tax": 1657,
            "assessment": {
                "building": 105000,
                "land": 30000,
                "total": 135000
            }
            },
            {
            "year": 2013,
            "tax": 1621,
            "assessment": {
                "building": 100000,
                "land": 30000,
                "total": 130000
            }
            },
            {
            "year": 2012,
            "tax": 1591,
            "assessment": {
                "building": 100000,
                "land": 30000,
                "total": 130000
            }
            },
            {
            "year": 2010,
            "tax": 1775,
            "assessment": {
                "building": 100000,
                "land": 30000,
                "total": 130000
            }
            },
            {
            "year": 2009,
            "tax": 1898,
            "assessment": {
                "building": 110000,
                "land": 50000,
                "total": 160000
            }
            },
            {
            "year": 2008,
            "tax": 2637,
            "assessment": {
                "building": 145656,
                "land": 98838,
                "total": 244494
            }
            },
            {
            "year": 2007,
            "tax": 2536,
            "assessment": {
                "building": 142800,
                "land": 96900,
                "total": 239700
            }
            }
        ],
        "lot_sqft": 871,
        "price_per_sqft": 188,
        "latitude": 39.732938,
        "longitude": -121.798455,
        "county": "Butte",
        "hoa_fee": 300,
        "nearby_schools": "Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/7a0ff002137252127d644316eae269f6l-b2308026527od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2060
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/489-E-1st-Ave_Chico_CA_95926_M28784-57674",
        "property_id": "2878457674",
        "listing_id": "2977121774",
        "mls": "MRCA",
        "mls_id": "TR25007218",
        "status": "PENDING",
        "text": "Golden opportunity to own a remodeled and stylish home in the Avenues. One mile from Chico State and Enloe Hospital. Close to restaurants and shops and grocery store. Butte College bus stop is very close to the house. Home is beautifully remodeled, saving original charm including hardwood floors wood, French doors in dining room, gas fireplace, dual pane windows, central H/A. New solid surface countertops, hardware, fixtures and Lighting in kitchen. 3-year-old refrigerator, washer and dryer negotiable. New tile floor, fixtures, mirror, and lighting in bathroom. Newer window coverings, carpet in sunroom, baseboards, interior/ exterior paint, new sewer pipe from house to alley. Newer landscaping with fire pit, chairs, patio with sectional & ping pong table negotiable. Two newer queen mattresses and bed frames and sofa bed in sunroom available. One car garage, two car carport/patio, one gated parking spot, alley access and parking. Prior Airbnb and VRBO short-term rental. History of rental lease stats available on request. Home is completely staged, furnished and stocked to start rental business immediately - all furniture and free-standing appliances available.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "489 E 1st Ave",
        "street": "489 E 1st Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 2,
        "full_baths": 1,
        "half_baths": 0,
        "sqft": 1068,
        "year_built": 1940,
        "days_on_mls": 19,
        "list_price": 379000,
        "list_date": "2025-01-11",
        "assessed_value": 351900,
        "estimated_value": 379090,
        "tax": 3925,
        "tax_history": [
            {
            "year": 2023,
            "tax": 3925,
            "assessment": {
                "building": 188700,
                "land": 163200,
                "total": 351900
            }
            },
            {
            "year": 2022,
            "tax": 3862,
            "assessment": {
                "building": 185000,
                "land": 160000,
                "total": 345000
            }
            },
            {
            "year": 2021,
            "tax": 2757,
            "assessment": {
                "building": 115625,
                "land": 130234,
                "total": 245859
            }
            },
            {
            "year": 2020,
            "tax": 2749,
            "assessment": {
                "building": 114440,
                "land": 128899,
                "total": 243339
            }
            },
            {
            "year": 2019,
            "tax": 2700,
            "assessment": {
                "building": 112197,
                "land": 126372,
                "total": 238569
            }
            },
            {
            "year": 2018,
            "tax": 2650,
            "assessment": {
                "building": 109998,
                "land": 123895,
                "total": 233893
            }
            },
            {
            "year": 2017,
            "tax": 2591,
            "assessment": {
                "building": 107342,
                "land": 121466,
                "total": 228808
            }
            },
            {
            "year": 2016,
            "tax": 2292,
            "assessment": {
                "building": 98375,
                "land": 119085,
                "total": 217460
            }
            },
            {
            "year": 2015,
            "tax": 2292,
            "assessment": {
                "building": 96898,
                "land": 117297,
                "total": 214195
            }
            },
            {
            "year": 2014,
            "tax": 929,
            "assessment": {
                "building": 53081,
                "land": 40590,
                "total": 93671
            }
            },
            {
            "year": 2013,
            "tax": 935,
            "assessment": {
                "building": 52842,
                "land": 40407,
                "total": 93249
            }
            },
            {
            "year": 2012,
            "tax": 879,
            "assessment": {
                "building": 51806,
                "land": 39615,
                "total": 91421
            }
            },
            {
            "year": 2010,
            "tax": 868,
            "assessment": {
                "building": 50791,
                "land": 38839,
                "total": 89630
            }
            },
            {
            "year": 2009,
            "tax": 883,
            "assessment": {
                "building": 50412,
                "land": 38549,
                "total": 88961
            }
            },
            {
            "year": 2008,
            "tax": 851,
            "assessment": {
                "building": 49542,
                "land": 37884,
                "total": 87426
            }
            },
            {
            "year": 2007,
            "tax": 827,
            "assessment": {
                "building": 48571,
                "land": 37142,
                "total": 85713
            }
            }
        ],
        "lot_sqft": 6098,
        "price_per_sqft": 355,
        "latitude": 39.740177,
        "longitude": -121.839585,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/7495fd57079c7bf78ccbbc3d72c37e0fl-m3504311001od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2963
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/2159-Elm-St-Unit-1_Chico_CA_95928_M92739-88176",
        "property_id": "9273988176",
        "listing_id": "2977117637",
        "mls": "MRCA",
        "mls_id": "SN25006638",
        "status": "PENDING",
        "text": "Welcome to 2159 Elm St #1, a delightful townhouse situated within a 10-unit community. Built in 2003, this spacious 4-bedroom, 2-bathroom home perfectly balances comfort, functionality, and thoughtful design. The welcoming covered front porch overlooks the communitys grassy lawn and mature landscaping, creating a charming first impression. Head inside and discover a comfortable living room with upgraded LVP flooring that extends throughout the home, with carpet reserved for the stairs. The kitchen features ample cabinetry, Formica countertops, a layout designed for convenience, and a cozy under-stairs closet that makes an excellent pantry for additional storage. Sliding glass doors lead to a fully fenced, private patioa charming space perfect for a small table and potted plants for those with a green thumb! On the main floor, youll find a bedroom perfect for guests or a home office, located just steps from a full bathroom that also serves as a laundry room. Upstairs, the LVP flooring lines the hallway leading to three additional bedrooms, offering a cohesive and modern look. The upstairs bathroom includes a spacious vanity area and a combined shower/tub and toilet, offering a functional layout perfect for shared living. Additional features include dual-pane windows, central HVAC for year-round comfort, and off-street parking. The homes location is unbeatablejust behind the iconic Sierra Nevada Brewery and minutes from the Chico Community Childrens Center, the Silver Dollar Fairgrounds, and historic Downtown Chico. Whether youre looking for a charming primary residence or an excellent investment opportunity, 2159 Elm St #1 combines charm, low-maintenance living, and location in one exceptional package. Dont miss your chance to see this propertycall your favorite Realtor and make an appointment today!",
        "style": "TOWNHOMES",
        "full_street_line": "2159 Elm St Unit 1",
        "street": "2159 Elm St",
        "unit": "Unit 1",
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 4,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1344,
        "year_built": 2003,
        "days_on_mls": 19,
        "list_price": 225000,
        "list_date": "2025-01-11",
        "assessed_value": 0,
        "estimated_value": 0,
        "tax": 0,
        "tax_history": 0,
        "lot_sqft": 871,
        "price_per_sqft": 167,
        "latitude": 39.721581,
        "longitude": -121.81601,
        "county": "Butte",
        "hoa_fee": 380,
        "nearby_schools": "Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/f1b698046eca6fe8bb13d01f797c8e2cl-m2727736404od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2399
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/2187-Kenrick-Ln-Unit-1_Chico_CA_95928_M91448-23523",
        "property_id": "9144823523",
        "listing_id": "2977096703",
        "mls": "MRCA",
        "mls_id": "SN25006109",
        "status": "FOR_SALE",
        "text": "We are excited to introduce the Stacked Flats, Meriam Park's distinctive duplexes located in the charming Bungalow Commons neighborhood. This rare offering marks the first of its kind to come to market. Nestled within a thriving community, the property is surrounded by exceptional amenities, including renowned restaurants, cozy coffee shops, unique boutiques, fitness facilities, scenic parks, a dog park, pickleball courts, live entertainment, and bustling markets. Offering a lifestyle of modern convenience and sophistication, this duplex features two turnkey units, each showcasing thoughtful upgrades throughout including fresh exterior paint. The first unit is a studio with a spacious private patio, a full kitchen with stainless steel appliances, granite countertops, and soft-close white cabinets. The bathroom includes granite countertops and shower, a walk-in closet, and a full-size washer and dryer are added for convenience. The second unit is a stylish 2-bedroom, 1-bathroom home with an open-concept living space highlighted by vaulted ceilings and large windows that invite natural light. The kitchen stands out with granite countertops, white soft-close cabinets, a kitchen island with bar seating, and stainless steel appliances. This unit also offers a full-size washer and dryer, a two-car garage, and luxury vinyl plank flooring throughout. Dont miss the opportunity to own this exceptional property in one of Chicos most dynamic and desirable communities!",
        "style": "MULTI_FAMILY",
        "full_street_line": "2187 Kenrick Ln",
        "street": "2187 Kenrick Ln",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1375,
        "year_built": 2020,
        "days_on_mls": 20,
        "list_price": 615000,
        "list_date": "2025-01-10",
        "assessed_value": 206002,
        "estimated_value": 397000,
        "tax": 2356,
        "tax_history": [
            {
            "year": 2023,
            "tax": 2356,
            "assessment": {
                "building": 197676,
                "land": 8326,
                "total": 206002
            }
            },
            {
            "year": 2022,
            "tax": 2300,
            "assessment": {
                "building": 193800,
                "land": 8163,
                "total": 201963
            }
            },
            {
            "year": 2021,
            "tax": 2321,
            "assessment": {
                "building": 190000,
                "land": 8003,
                "total": 198003
            }
            },
            {
            "year": 2020,
            "tax": 107,
            "assessment": {
                "building": null,
                "land": 7921,
                "total": 7921
            }
            }
        ],
        "lot_sqft": 2178,
        "price_per_sqft": 447,
        "latitude": 39.731807,
        "longitude": -121.795836,
        "county": "Butte",
        "hoa_fee": 80,
        "nearby_schools": "Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/93d29aa95d1d5167d75358f62ccfa8a7l-m3199258235od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1935
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1029-Citrus-Ave_Chico_CA_95926_M28793-89323",
        "property_id": "2879389323",
        "listing_id": "2977096250",
        "mls": "MRCA",
        "mls_id": "SN24253745",
        "status": "FOR_SALE",
        "text": "Welcome home to this Chico Charmer nestled in the avenues. Walkthrough the picket fence to find this turnkey home with 3 bedrooms, 1.5 bathrooms, indoor laundry, cement flooring and new appliances. There is Hardie Board siding with redwood trim on the exterior, a shed, and new fencing with access for your toys or room to build an ADU or garage. Close to Chico High, Chico State, and Downtown this home is ready and waiting for you!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "1029 Citrus Ave",
        "street": "1029 Citrus Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 3,
        "full_baths": 1,
        "half_baths": 1,
        "sqft": 1042,
        "year_built": 1947,
        "days_on_mls": 20,
        "list_price": 385000,
        "list_date": "2025-01-10",
        "assessed_value": 320000,
        "estimated_value": 338000,
        "tax": 3570,
        "tax_history": [
            {
            "year": 2023,
            "tax": 3570,
            "assessment": {
                "building": 160000,
                "land": 160000,
                "total": 320000
            }
            },
            {
            "year": 2022,
            "tax": 2584,
            "assessment": {
                "building": 121342,
                "land": 109208,
                "total": 230550
            }
            },
            {
            "year": 2021,
            "tax": 2536,
            "assessment": {
                "building": 118963,
                "land": 107067,
                "total": 226030
            }
            },
            {
            "year": 2020,
            "tax": 2529,
            "assessment": {
                "building": 117744,
                "land": 105970,
                "total": 223714
            }
            },
            {
            "year": 2019,
            "tax": 2483,
            "assessment": {
                "building": 115436,
                "land": 103893,
                "total": 219329
            }
            },
            {
            "year": 2018,
            "tax": 2437,
            "assessment": {
                "building": 113173,
                "land": 101856,
                "total": 215029
            }
            },
            {
            "year": 2017,
            "tax": 2388,
            "assessment": {
                "building": 110954,
                "land": 99859,
                "total": 210813
            }
            },
            {
            "year": 2016,
            "tax": 2179,
            "assessment": {
                "building": 108779,
                "land": 97901,
                "total": 206680
            }
            },
            {
            "year": 2015,
            "tax": 2179,
            "assessment": {
                "building": 107146,
                "land": 96431,
                "total": 203577
            }
            },
            {
            "year": 2014,
            "tax": 2127,
            "assessment": {
                "building": 105048,
                "land": 94543,
                "total": 199591
            }
            },
            {
            "year": 2013,
            "tax": 2154,
            "assessment": {
                "building": 104574,
                "land": 94116,
                "total": 198690
            }
            },
            {
            "year": 2012,
            "tax": 1875,
            "assessment": {
                "building": 105000,
                "land": 75000,
                "total": 180000
            }
            },
            {
            "year": 2010,
            "tax": 1933,
            "assessment": {
                "building": 90000,
                "land": 95000,
                "total": 185000
            }
            },
            {
            "year": 2009,
            "tax": 1754,
            "assessment": {
                "building": 99763,
                "land": 89786,
                "total": 189549
            }
            },
            {
            "year": 2008,
            "tax": 1694,
            "assessment": {
                "building": 60000,
                "land": 100000,
                "total": 160000
            }
            },
            {
            "year": 2007,
            "tax": 342,
            "assessment": {
                "building": 25245,
                "land": 7314,
                "total": 32559
            }
            }
        ],
        "lot_sqft": 3049,
        "price_per_sqft": 369,
        "latitude": 39.735081,
        "longitude": -121.850181,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/9a855b907372a3cde3042cd770d84bd5l-m3713260226od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3839
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/337-Southbury-Ln_Chico_CA_95973_M22160-71840",
        "property_id": "2216071840",
        "listing_id": "2977082486",
        "mls": "MRCA",
        "mls_id": "SN25004903",
        "status": "PENDING",
        "text": "Rosewood Estates beauty!!! This very popular place to call home is ready for its new owners - hand scraped walnut porcelain tile floors in the entry, living room, kitchen and hallway. There is a breakfast bar, stainless steel appliances, gas range, and the refrigerator is included !! Vaulted ceilings with walls of windows - this floor plan feels much larger than the square footage states~~ SOLAR - panels that are on a Power Purchase Agreement which is a Pay for Usage plan, not a lease. There is also a whole house fan, dual pane windows, and a fireplace to boot!! Close to shopping, schools and freeway access - this home's location is just prime!!!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "337 Southbury Ln",
        "street": "337 Southbury Ln",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1316,
        "year_built": 2003,
        "days_on_mls": 20,
        "list_price": 429000,
        "list_date": "2025-01-10",
        "assessed_value": 346318,
        "estimated_value": 446100,
        "tax": 4149,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4149,
            "assessment": {
                "building": 190850,
                "land": 155468,
                "total": 346318
            }
            },
            {
            "year": 2022,
            "tax": 4062,
            "assessment": {
                "building": 187108,
                "land": 152420,
                "total": 339528
            }
            },
            {
            "year": 2021,
            "tax": 4001,
            "assessment": {
                "building": 183440,
                "land": 149432,
                "total": 332872
            }
            },
            {
            "year": 2020,
            "tax": 4001,
            "assessment": {
                "building": 181560,
                "land": 147900,
                "total": 329460
            }
            },
            {
            "year": 2019,
            "tax": 3890,
            "assessment": {
                "building": 178000,
                "land": 145000,
                "total": 323000
            }
            },
            {
            "year": 2018,
            "tax": 3184,
            "assessment": {
                "building": 139949,
                "land": 129282,
                "total": 269231
            }
            },
            {
            "year": 2017,
            "tax": 3136,
            "assessment": {
                "building": 137205,
                "land": 126748,
                "total": 263953
            }
            },
            {
            "year": 2016,
            "tax": 2926,
            "assessment": {
                "building": 134515,
                "land": 124263,
                "total": 258778
            }
            },
            {
            "year": 2015,
            "tax": 2953,
            "assessment": {
                "building": 132495,
                "land": 122397,
                "total": 254892
            }
            },
            {
            "year": 2014,
            "tax": 2895,
            "assessment": {
                "building": 140000,
                "land": 110000,
                "total": 250000
            }
            },
            {
            "year": 2013,
            "tax": 2595,
            "assessment": {
                "building": 120000,
                "land": 100000,
                "total": 220000
            }
            },
            {
            "year": 2012,
            "tax": 2393,
            "assessment": {
                "building": 110000,
                "land": 95000,
                "total": 205000
            }
            },
            {
            "year": 2010,
            "tax": 2855,
            "assessment": {
                "building": 125000,
                "land": 120000,
                "total": 245000
            }
            },
            {
            "year": 2009,
            "tax": 2934,
            "assessment": {
                "building": 125000,
                "land": 120000,
                "total": 245000
            }
            },
            {
            "year": 2008,
            "tax": 2561,
            "assessment": {
                "building": 125344,
                "land": 99582,
                "total": 224926
            }
            },
            {
            "year": 2007,
            "tax": 2466,
            "assessment": {
                "building": 122887,
                "land": 97630,
                "total": 220517
            }
            }
        ],
        "lot_sqft": 5227,
        "price_per_sqft": 326,
        "latitude": 39.771272,
        "longitude": -121.880399,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/7af3bd20acfe2c66159e82d423637af5l-b2403009043od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2151
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/3460-Shadowtree-Ln_Chico_CA_95928_M21148-71145",
        "property_id": "2114871145",
        "listing_id": "2977095425",
        "mls": "MRCA",
        "mls_id": "SN25006551",
        "status": "FOR_SALE",
        "text": "BEAUTIFUL 2.13 ACRE LOT in the wonderful community of CANYON OAKS GOLF COURSE! Build your dream home! This stunning property is in a great location surrounded by views, natures beauty and a fabulous lifestyle that living in a golf community can provide. The area provides fun social and golf events, fund raisers, a delicious eating faciality, bar area and more! Be a step ahead of your building desires! INCLUDED with this beautiful lot is a complete full architectural set of building prints for a 2590 Sq. Ft. home plus 3 car garage, topographical drawing of the acreage, engineering and approved landscape drawings by the HOA! Don't miss out of this wonderful opportunity! Call today for details!",
        "style": "LAND",
        "full_street_line": "3460 Shadowtree Ln",
        "street": "3460 Shadowtree Ln",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 0,
        "full_baths": 0,
        "half_baths": 0,
        "sqft": 0,
        "year_built": 0,
        "days_on_mls": 20,
        "list_price": 275000,
        "list_date": "2025-01-10",
        "assessed_value": 153000,
        "estimated_value": 270146,
        "tax": 1707,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1707,
            "assessment": {
                "building": null,
                "land": 153000,
                "total": 153000
            }
            },
            {
            "year": 2022,
            "tax": 2166,
            "assessment": {
                "building": null,
                "land": 193800,
                "total": 193800
            }
            },
            {
            "year": 2021,
            "tax": 2289,
            "assessment": {
                "building": null,
                "land": 204711,
                "total": 204711
            }
            },
            {
            "year": 2020,
            "tax": 2283,
            "assessment": {
                "building": null,
                "land": 202612,
                "total": 202612
            }
            },
            {
            "year": 2019,
            "tax": 2241,
            "assessment": {
                "building": null,
                "land": 198640,
                "total": 198640
            }
            },
            {
            "year": 2018,
            "tax": 2200,
            "assessment": {
                "building": null,
                "land": 194746,
                "total": 194746
            }
            },
            {
            "year": 2017,
            "tax": 1976,
            "assessment": {
                "building": null,
                "land": 175000,
                "total": 175000
            }
            },
            {
            "year": 2016,
            "tax": 1682,
            "assessment": {
                "building": null,
                "land": 160000,
                "total": 160000
            }
            },
            {
            "year": 2015,
            "tax": 1708,
            "assessment": {
                "building": null,
                "land": 160000,
                "total": 160000
            }
            },
            {
            "year": 2014,
            "tax": 1593,
            "assessment": {
                "building": null,
                "land": 90000,
                "total": 90000
            }
            },
            {
            "year": 2013,
            "tax": 650,
            "assessment": {
                "building": null,
                "land": 60000,
                "total": 60000
            }
            },
            {
            "year": 2012,
            "tax": 625,
            "assessment": {
                "building": null,
                "land": 60000,
                "total": 60000
            }
            },
            {
            "year": 2010,
            "tax": 1818,
            "assessment": {
                "building": null,
                "land": 150000,
                "total": 150000
            }
            },
            {
            "year": 2009,
            "tax": 2220,
            "assessment": {
                "building": null,
                "land": 171668,
                "total": 171668
            }
            },
            {
            "year": 2008,
            "tax": 1786,
            "assessment": {
                "building": null,
                "land": 168702,
                "total": 168702
            }
            },
            {
            "year": 2007,
            "tax": 1738,
            "assessment": {
                "building": null,
                "land": 165395,
                "total": 165395
            }
            }
        ],
        "lot_sqft": 92783,
        "price_per_sqft": 0,
        "latitude": 39.765924,
        "longitude": -121.76304,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/3facc047df89de68ef37e40b0efac4e1l-m931328502od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2802
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/2645-Ceanothus-Ave_Chico_CA_95973_M29811-92723",
        "property_id": "2981192723",
        "listing_id": "2977059221",
        "mls": "MRCA",
        "mls_id": "SN25005222",
        "status": "PENDING",
        "text": "Great 3 bedroom/3 bath home that is close to schools, shopping (Safeway & CVS), and great eats!!! This clean as a whistle property is ready to go and includes Washer/dryer and refrigerator. Enjoy visiting with family and friends while you cook on the gas range and they sit at the eating bar sharing your day and making memories. The yard is fenced and easy to manage. Raised planter boxes. There is a 2 car garage to keep your things tucked away and safe. Ceiling fans throughout and carpet in bedrooms only.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "2645 Ceanothus Ave",
        "street": "2645 Ceanothus Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 3,
        "half_baths": 0,
        "sqft": 1571,
        "year_built": 2006,
        "days_on_mls": 20,
        "list_price": 449000,
        "list_date": "2025-01-10",
        "assessed_value": 337741,
        "estimated_value": 451932,
        "tax": 3826,
        "tax_history": [
            {
            "year": 2023,
            "tax": 3826,
            "assessment": {
                "building": 187634,
                "land": 150107,
                "total": 337741
            }
            },
            {
            "year": 2022,
            "tax": 3766,
            "assessment": {
                "building": 183955,
                "land": 147164,
                "total": 331119
            }
            },
            {
            "year": 2021,
            "tax": 3696,
            "assessment": {
                "building": 180349,
                "land": 144279,
                "total": 324628
            }
            },
            {
            "year": 2020,
            "tax": 3686,
            "assessment": {
                "building": 178500,
                "land": 142800,
                "total": 321300
            }
            },
            {
            "year": 2019,
            "tax": 3619,
            "assessment": {
                "building": 175000,
                "land": 140000,
                "total": 315000
            }
            },
            {
            "year": 2018,
            "tax": 3608,
            "assessment": {
                "building": 195000,
                "land": 120000,
                "total": 315000
            }
            },
            {
            "year": 2017,
            "tax": 3438,
            "assessment": {
                "building": 175000,
                "land": 125000,
                "total": 300000
            }
            },
            {
            "year": 2016,
            "tax": 2954,
            "assessment": {
                "building": 160000,
                "land": 115000,
                "total": 275000
            }
            },
            {
            "year": 2015,
            "tax": 2849,
            "assessment": {
                "building": 160000,
                "land": 100000,
                "total": 260000
            }
            },
            {
            "year": 2014,
            "tax": 2768,
            "assessment": {
                "building": 150000,
                "land": 100000,
                "total": 250000
            }
            },
            {
            "year": 2013,
            "tax": 2585,
            "assessment": {
                "building": 145000,
                "land": 85000,
                "total": 230000
            }
            },
            {
            "year": 2012,
            "tax": 2476,
            "assessment": {
                "building": 145000,
                "land": 85000,
                "total": 230000
            }
            },
            {
            "year": 2010,
            "tax": 2704,
            "assessment": {
                "building": 155000,
                "land": 95000,
                "total": 250000
            }
            },
            {
            "year": 2009,
            "tax": 2838,
            "assessment": {
                "building": 155000,
                "land": 95000,
                "total": 250000
            }
            },
            {
            "year": 2008,
            "tax": 3483,
            "assessment": {
                "building": 182070,
                "land": 145656,
                "total": 327726
            }
            },
            {
            "year": 2007,
            "tax": 3416,
            "assessment": {
                "building": 178500,
                "land": 142800,
                "total": 321300
            }
            }
        ],
        "lot_sqft": 3485,
        "price_per_sqft": 286,
        "latitude": 39.76466,
        "longitude": -121.820285,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/cb29af1e7b657a5f57b3bbc594dd11a6l-b1573813725od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2166
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/2776-Ceanothus-Ave_Chico_CA_95973_M29366-51362",
        "property_id": "2936651362",
        "listing_id": "2977081717",
        "mls": "MRCA",
        "mls_id": "SN24218198",
        "status": "PENDING",
        "text": "Welcome to your dream home! Nestled on a spacious corner lot, this meticulously maintained property boasts a sparkling pool with a tranquil water feature, perfect for cold plunges or summer relaxation. The open floor plan invites you into a bright and airy living room, complete with a vaulted ceiling, cozy gas fireplace and an abundance of natural light. The kitchen, a true chef's delight, offers plenty of counter space, an eat-up bar, and updated stainless steel appliances, including a newer cooktop, oven, and dishwasher. Retreat to the large primary bedroom featuring a coffered ceiling, an ensuite bathroom, and a private slider to the backyard oasis. The beautifully landscaped front and backyard provide a serene setting, complete with an extended concrete patio and covered area, ideal for entertaining. With recent updates like fresh interior paint, new carpet, a newer A/C unit, water heater, and pool equipment, this home offers modern comfort and style. Located close to shopping, restaurants, and top-rated schools, this home combines convenience with luxury. Don't miss the opportunity to make this updated move-in ready home your own!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "2776 Ceanothus Ave",
        "street": "2776 Ceanothus Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1696,
        "year_built": 2002,
        "days_on_mls": 20,
        "list_price": 470000,
        "list_date": "2025-01-10",
        "assessed_value": 479270,
        "estimated_value": 525500,
        "tax": 5445,
        "tax_history": [
            {
            "year": 2023,
            "tax": 5445,
            "assessment": {
                "building": 307720,
                "land": 171550,
                "total": 479270
            }
            },
            {
            "year": 2022,
            "tax": 5366,
            "assessment": {
                "building": 301687,
                "land": 168187,
                "total": 469874
            }
            },
            {
            "year": 2021,
            "tax": 5267,
            "assessment": {
                "building": 295772,
                "land": 164890,
                "total": 460662
            }
            },
            {
            "year": 2020,
            "tax": 5286,
            "assessment": {
                "building": 292740,
                "land": 163200,
                "total": 455940
            }
            },
            {
            "year": 2019,
            "tax": 4192,
            "assessment": {
                "building": 255599,
                "land": 110350,
                "total": 365949
            }
            },
            {
            "year": 2018,
            "tax": 4065,
            "assessment": {
                "building": 250588,
                "land": 108187,
                "total": 358775
            }
            },
            {
            "year": 2017,
            "tax": 3986,
            "assessment": {
                "building": 245675,
                "land": 106066,
                "total": 351741
            }
            },
            {
            "year": 2016,
            "tax": 3618,
            "assessment": {
                "building": 240858,
                "land": 103987,
                "total": 344845
            }
            },
            {
            "year": 2015,
            "tax": 3600,
            "assessment": {
                "building": 237241,
                "land": 102426,
                "total": 339667
            }
            },
            {
            "year": 2014,
            "tax": 3605,
            "assessment": {
                "building": 215000,
                "land": 115000,
                "total": 330000
            }
            },
            {
            "year": 2013,
            "tax": 3076,
            "assessment": {
                "building": 185000,
                "land": 90000,
                "total": 275000
            }
            },
            {
            "year": 2012,
            "tax": 2799,
            "assessment": {
                "building": 173000,
                "land": 95000,
                "total": 268000
            }
            },
            {
            "year": 2010,
            "tax": 3130,
            "assessment": {
                "building": 188000,
                "land": 105000,
                "total": 293000
            }
            },
            {
            "year": 2009,
            "tax": 3444,
            "assessment": {
                "building": 188000,
                "land": 105000,
                "total": 293000
            }
            },
            {
            "year": 2008,
            "tax": 3278,
            "assessment": {
                "building": 217073,
                "land": 93721,
                "total": 310794
            }
            },
            {
            "year": 2007,
            "tax": 3158,
            "assessment": {
                "building": 212817,
                "land": 91884,
                "total": 304701
            }
            }
        ],
        "lot_sqft": 6970,
        "price_per_sqft": 277,
        "latitude": 39.765633,
        "longitude": -121.819745,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/29c1c9e6e2bfedb817e9a99eba083508l-m2835994914od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4396
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/3568-Shallow-Springs-Ter_Chico_CA_95928_M23010-15597",
        "property_id": "2301015597",
        "listing_id": "2977055591",
        "mls": "MRCA",
        "mls_id": "SN25006032",
        "status": "FOR_SALE",
        "text": "This stunning vacant lot, located in the Canyon Oaks Country Club gated community, offers an unparalleled opportunity to build your dream home. Spanning nearly half an acre, this prime property is perfectly situated at the end of a quiet cul-de-sac, ensuring ultimate privacy with no through traffic or noise. Nestled alongside the 10th tee, the lot boasts a serene setting surrounded by beautiful mountain bluffs, mature oak trees and views. All utilities are on-site and ready for your custom design. Picture yourself relaxing on your future backyard patio, enjoying the shade on warm summer afternoons, listening to the soothing sounds of birds and a nearby babbling brook, and taking in the breathtaking natural scenery. This is a wonderful opportunity to create your own peaceful retreat in one of Chicos most sought-after communities.",
        "style": "LAND",
        "full_street_line": "3568 Shallow Springs Ter",
        "street": "3568 Shallow Springs Ter",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 0,
        "full_baths": 0,
        "half_baths": 0,
        "sqft": 0,
        "year_built": 0,
        "days_on_mls": 20,
        "list_price": 205000,
        "list_date": "2025-01-10",
        "assessed_value": 153864,
        "estimated_value": 206000,
        "tax": 1714,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1714,
            "assessment": {
                "building": null,
                "land": 153864,
                "total": 153864
            }
            },
            {
            "year": 2022,
            "tax": 843,
            "assessment": {
                "building": null,
                "land": 150848,
                "total": 150848
            }
            },
            {
            "year": 2021,
            "tax": 1655,
            "assessment": {
                "building": null,
                "land": 147891,
                "total": 147891
            }
            },
            {
            "year": 2020,
            "tax": 1650,
            "assessment": {
                "building": null,
                "land": 146375,
                "total": 146375
            }
            },
            {
            "year": 2019,
            "tax": 1620,
            "assessment": {
                "building": null,
                "land": 143505,
                "total": 143505
            }
            },
            {
            "year": 2018,
            "tax": 1590,
            "assessment": {
                "building": null,
                "land": 140692,
                "total": 140692
            }
            },
            {
            "year": 2017,
            "tax": 1558,
            "assessment": {
                "building": null,
                "land": 137934,
                "total": 137934
            }
            },
            {
            "year": 2016,
            "tax": 1422,
            "assessment": {
                "building": null,
                "land": 135230,
                "total": 135230
            }
            },
            {
            "year": 2015,
            "tax": 1422,
            "assessment": {
                "building": null,
                "land": 133199,
                "total": 133199
            }
            },
            {
            "year": 2014,
            "tax": 1387,
            "assessment": {
                "building": null,
                "land": 130590,
                "total": 130590
            }
            },
            {
            "year": 2013,
            "tax": 1466,
            "assessment": {
                "building": null,
                "land": 135252,
                "total": 135252
            }
            },
            {
            "year": 2012,
            "tax": 1381,
            "assessment": {
                "building": null,
                "land": 132600,
                "total": 132600
            }
            },
            {
            "year": 2010,
            "tax": 1323,
            "assessment": {
                "building": null,
                "land": 130000,
                "total": 130000
            }
            },
            {
            "year": 2009,
            "tax": 2040,
            "assessment": {
                "building": null,
                "land": 125000,
                "total": 125000
            }
            },
            {
            "year": 2008,
            "tax": 1980,
            "assessment": {
                "building": null,
                "land": 187000,
                "total": 187000
            }
            }
        ],
        "lot_sqft": 20473,
        "price_per_sqft": 0,
        "latitude": 39.759697,
        "longitude": -121.75539,
        "county": "Butte",
        "hoa_fee": 130,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/9e2c9517ba4031c7ad08e77a9f2a3265l-m2981426132od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3630
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/490-Vilas-Rd_Chico_CA_95973_M27135-44506",
        "property_id": "2713544506",
        "listing_id": "2977081719",
        "mls": "MRCA",
        "mls_id": "SN25006481",
        "status": "FOR_SALE",
        "text": "Home shows like new, complete with updated Minisplit heat and air, Pellet stove, new well in progress, roof on main house is new. Its a move in ready home. Complete with shop building. parcel size 3.21 acres with newly approved boundary line modification. Grounds are manicured. Water Tank complete with gravity fed and pressurized plumbing.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "490 Vilas Rd",
        "street": "490 Vilas Rd",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1968,
        "year_built": 1977,
        "days_on_mls": 20,
        "list_price": 475000,
        "list_date": "2025-01-10",
        "assessed_value": 360000,
        "estimated_value": 395600,
        "tax": 4020,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4020,
            "assessment": {
                "building": 250000,
                "land": 110000,
                "total": 360000
            }
            },
            {
            "year": 2022,
            "tax": 2350,
            "assessment": {
                "building": 174264,
                "land": 41838,
                "total": 216102
            }
            },
            {
            "year": 2021,
            "tax": 2305,
            "assessment": {
                "building": 170848,
                "land": 41018,
                "total": 211866
            }
            },
            {
            "year": 2020,
            "tax": 2297,
            "assessment": {
                "building": 169097,
                "land": 40598,
                "total": 209695
            }
            },
            {
            "year": 2019,
            "tax": 2254,
            "assessment": {
                "building": 165782,
                "land": 39802,
                "total": 205584
            }
            },
            {
            "year": 2018,
            "tax": 2212,
            "assessment": {
                "building": 162532,
                "land": 39022,
                "total": 201554
            }
            },
            {
            "year": 2017,
            "tax": 2165,
            "assessment": {
                "building": 159346,
                "land": 38257,
                "total": 197603
            }
            },
            {
            "year": 2016,
            "tax": 1975,
            "assessment": {
                "building": 156222,
                "land": 37507,
                "total": 193729
            }
            },
            {
            "year": 2015,
            "tax": 1974,
            "assessment": {
                "building": 153876,
                "land": 36944,
                "total": 190820
            }
            },
            {
            "year": 2014,
            "tax": 1925,
            "assessment": {
                "building": 150862,
                "land": 36221,
                "total": 187083
            }
            },
            {
            "year": 2013,
            "tax": 1948,
            "assessment": {
                "building": 150181,
                "land": 36058,
                "total": 186239
            }
            },
            {
            "year": 2012,
            "tax": 1834,
            "assessment": {
                "building": 147237,
                "land": 35351,
                "total": 182588
            }
            },
            {
            "year": 2010,
            "tax": 1812,
            "assessment": {
                "building": 144350,
                "land": 34658,
                "total": 179008
            }
            },
            {
            "year": 2009,
            "tax": 1844,
            "assessment": {
                "building": 143272,
                "land": 34399,
                "total": 177671
            }
            },
            {
            "year": 2008,
            "tax": 1779,
            "assessment": {
                "building": 140798,
                "land": 33805,
                "total": 174603
            }
            },
            {
            "year": 2007,
            "tax": 1730,
            "assessment": {
                "building": 138038,
                "land": 33143,
                "total": 171181
            }
            }
        ],
        "lot_sqft": 233046,
        "price_per_sqft": 241,
        "latitude": 39.91131,
        "longitude": -121.727221,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/a97726bf6a200705eb580a2ab7d9e88dl-m1913865795od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3033
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/701-E-Lassen-Ave-Unit-38_Chico_CA_95973_M91349-60925",
        "property_id": "9134960925",
        "listing_id": "2977007704",
        "mls": "MRCA",
        "mls_id": "SN25005256",
        "status": "FOR_SALE",
        "text": "Well maintained Senior home in Casa De Flores Mobile Home Park. Needs a little TLC.",
        "style": "MOBILE",
        "full_street_line": "701 E Lassen Ave Unit 38",
        "street": "701 E Lassen Ave",
        "unit": "Unit 38",
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 2,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 0,
        "year_built": 1976,
        "days_on_mls": 21,
        "list_price": 80000,
        "list_date": "2025-01-09",
        "assessed_value": 0,
        "estimated_value": 0,
        "tax": 0,
        "tax_history": 0,
        "lot_sqft": 0,
        "price_per_sqft": 0,
        "latitude": 39.767738,
        "longitude": -121.852921,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/38c1a643a795918e0905b4dbc4dac570l-m1769671427od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3114
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/2187-Kenrick-Ln-Unit-1_Chico_CA_95928_M91448-23523",
        "property_id": "9144823523",
        "listing_id": "2977052847",
        "mls": "MRCA",
        "mls_id": "SN25005660",
        "status": "FOR_SALE",
        "text": "We are excited to introduce the Stacked Flats, Meriam Park's distinctive duplexes located in the charming Bungalow Commons neighborhood. This rare offering marks the first of its kind to come to market. Nestled within a thriving community, the property is surrounded by exceptional amenities, including renowned restaurants, cozy coffee shops, unique boutiques, fitness facilities, scenic parks, a dog park, pickleball courts, live entertainment, and bustling markets. Offering a lifestyle of modern convenience and sophistication, this duplex features two turnkey units, each showcasing thoughtful upgrades throughout including fresh exterior paint. The first unit is a studio with a spacious private patio, a full kitchen with stainless steel appliances, granite countertops, and soft-close white cabinets. The bathroom includes granite countertops and shower, a walk-in closet, and a full-size washer and dryer are added for convenience. The second unit is a stylish 2-bedroom, 1-bathroom home with an open-concept living space highlighted by vaulted ceilings and large windows that invite natural light. The kitchen stands out with granite countertops, white soft-close cabinets, a kitchen island with bar seating, and stainless steel appliances. This unit also offers a full-size washer and dryer, a two-car garage, and luxury vinyl plank flooring throughout. Dont miss the opportunity to own this exceptional property in one of Chicos most dynamic and desirable communities!",
        "style": "DUPLEX_TRIPLEX",
        "full_street_line": "2187 Kenrick Ln",
        "street": "2187 Kenrick Ln",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1375,
        "year_built": 2020,
        "days_on_mls": 20,
        "list_price": 615000,
        "list_date": "2025-01-10",
        "assessed_value": 206002,
        "estimated_value": 397000,
        "tax": 2356,
        "tax_history": [
            {
            "year": 2023,
            "tax": 2356,
            "assessment": {
                "building": 197676,
                "land": 8326,
                "total": 206002
            }
            },
            {
            "year": 2022,
            "tax": 2300,
            "assessment": {
                "building": 193800,
                "land": 8163,
                "total": 201963
            }
            },
            {
            "year": 2021,
            "tax": 2321,
            "assessment": {
                "building": 190000,
                "land": 8003,
                "total": 198003
            }
            },
            {
            "year": 2020,
            "tax": 107,
            "assessment": {
                "building": null,
                "land": 7921,
                "total": 7921
            }
            }
        ],
        "lot_sqft": 2178,
        "price_per_sqft": 447,
        "latitude": 39.731807,
        "longitude": -121.795836,
        "county": "Butte",
        "hoa_fee": 80,
        "nearby_schools": "Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/dd49fe110421579aecf05750cc9ee6edl-m693903761od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1187
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1905-Broadway-St_Chico_CA_95928_M10282-66789",
        "property_id": "1028266789",
        "listing_id": "2977022118",
        "mls": "MRCA",
        "mls_id": "SN25004963",
        "status": "PENDING",
        "text": "This Chico bungalow home has been brought back to life! The classic charm with the modern updates creates a feeling of timeless peace when you enter this completely updated home. The open floorplan, beautiful kitchen with an island, coffee/ appliance center, and stainless steal hood vent create a feel of class and style that makes you want to call this house home. A brand new master bedroom and bathroom with walk in closet was added for ideal comfort and livability. Access the backyard and step onto your private redwood deck from the kitchen or your baster bedroom retreat. Located on a large corner lot, this house has tons of off street parking, as well as a driveway and gate that leads to your backyard. The home was originally built in 1910, other than salvaging the charm and enough good siding for the front of the house to keep some of the original character, everything else in the home is new. Complete new electrical, plumbing, HVAC, water heater, roof, and even foundation. This is like buying a new build on a beautiful street with large trees and charming old homes surrounding you. This is a must see!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "1905 Broadway St",
        "street": "1905 Broadway St",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1348,
        "year_built": 1910,
        "days_on_mls": 21,
        "list_price": 475000,
        "list_date": "2025-01-09",
        "assessed_value": 38046,
        "estimated_value": 298000,
        "tax": 459,
        "tax_history": [
            {
            "year": 2023,
            "tax": 459,
            "assessment": {
                "building": 26471,
                "land": 11575,
                "total": 38046
            }
            },
            {
            "year": 2022,
            "tax": 453,
            "assessment": {
                "building": 25952,
                "land": 11349,
                "total": 37301
            }
            },
            {
            "year": 2021,
            "tax": 441,
            "assessment": {
                "building": 25444,
                "land": 11127,
                "total": 36571
            }
            },
            {
            "year": 2020,
            "tax": 442,
            "assessment": {
                "building": 25184,
                "land": 11013,
                "total": 36197
            }
            },
            {
            "year": 2019,
            "tax": 437,
            "assessment": {
                "building": 24691,
                "land": 10798,
                "total": 35489
            }
            },
            {
            "year": 2018,
            "tax": 428,
            "assessment": {
                "building": 24207,
                "land": 10587,
                "total": 34794
            }
            },
            {
            "year": 2017,
            "tax": 416,
            "assessment": {
                "building": 23733,
                "land": 10380,
                "total": 34113
            }
            },
            {
            "year": 2016,
            "tax": 383,
            "assessment": {
                "building": 23268,
                "land": 10177,
                "total": 33445
            }
            },
            {
            "year": 2015,
            "tax": 382,
            "assessment": {
                "building": 22919,
                "land": 10025,
                "total": 32944
            }
            },
            {
            "year": 2014,
            "tax": 378,
            "assessment": {
                "building": 22471,
                "land": 9829,
                "total": 32300
            }
            },
            {
            "year": 2013,
            "tax": 377,
            "assessment": {
                "building": 22370,
                "land": 9785,
                "total": 32155
            }
            },
            {
            "year": 2012,
            "tax": 347,
            "assessment": {
                "building": 21932,
                "land": 9594,
                "total": 31526
            }
            },
            {
            "year": 2010,
            "tax": 338,
            "assessment": {
                "building": 21502,
                "land": 9406,
                "total": 30908
            }
            },
            {
            "year": 2009,
            "tax": 344,
            "assessment": {
                "building": 21342,
                "land": 9336,
                "total": 30678
            }
            },
            {
            "year": 2008,
            "tax": 344,
            "assessment": {
                "building": 20974,
                "land": 9176,
                "total": 30150
            }
            },
            {
            "year": 2007,
            "tax": 321,
            "assessment": {
                "building": 20563,
                "land": 8997,
                "total": 29560
            }
            }
        ],
        "lot_sqft": 6098,
        "price_per_sqft": 352,
        "latitude": 39.718402,
        "longitude": -121.825239,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/d1568602315a7ddaea1af8a6996c556el-m4051199817od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4094
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1675-Manzanita-Ave-Unit-13_Chico_CA_95926_M11141-04071",
        "property_id": "1114104071",
        "listing_id": "2976957180",
        "mls": "MRCA",
        "mls_id": "SN25001237",
        "status": "FOR_SALE",
        "text": "SOLAR power purchase agreement, significantly reducing your energy costs!! The home features a large living space with a formal dining area and an additional dining space off the kitchen. The primary bedroom is a tranquil oasis with hand-painted art, while the second bathroom conveniently connects to the second bedroom and provides access to the laundry area. The home also features newer heating and air conditioning, a newer roof, and all appliances are included. Sellers maintain monthly pest, yard maintance and security on the property and will help switch over to the new buyer! Enjoy the privacy of the paver patio backing up to the park at the Elks Lodge, ensuring no rear neighbors. The park offers an in-ground pool, clubhouse, and an outdoor space for BBQs, perfect for enjoying summer with friends. Numerous scheduled activities cater to seniors, this is a 55+ community. Conveniently located near schools, shopping, and services, this home also offers easy access to the beauty of Wildwood and Upper Bidwell Park. Don't miss this opportunity!",
        "style": "MOBILE",
        "full_street_line": "1675 Manzanita Ave Unit 13",
        "street": "1675 Manzanita Ave",
        "unit": "Unit 13",
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 2,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1512,
        "year_built": 1973,
        "days_on_mls": 23,
        "list_price": 89900,
        "list_date": "2025-01-07",
        "assessed_value": 0,
        "estimated_value": 79000,
        "tax": 623,
        "tax_history": [
            {
            "year": 2023,
            "tax": 623
            },
            {
            "year": 2022,
            "tax": 612
            },
            {
            "year": 2021,
            "tax": 599
            },
            {
            "year": 2020,
            "tax": 597
            },
            {
            "year": 2019,
            "tax": 484
            },
            {
            "year": 2016,
            "tax": 451,
            "assessment": {
                "building": null,
                "land": null,
                "total": 43000
            }
            },
            {
            "year": 2009,
            "tax": 462,
            "assessment": {
                "building": 50000,
                "land": null,
                "total": 50000
            }
            }
        ],
        "lot_sqft": 0,
        "price_per_sqft": 59,
        "latitude": 39.758826,
        "longitude": -121.806822,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/591c5b2ae591046f580dbef232f331c4l-m3334451086od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1645
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/3252-Canyon-Oaks-Ter_Chico_CA_95928_M13808-39993",
        "property_id": "1380839993",
        "listing_id": "2977036166",
        "mls": "MRCA",
        "mls_id": "SN25005360",
        "status": "FOR_SALE",
        "text": "Built with superb craftsmanship, this secluded Mediterranean haven, set amid verdant landscapes with breathtaking views of Canyon Oaks Country Club, spares no expense when it comes to custom detail. This remarkable estate offers an extraordinary blend of elegance and comfort, promising a living experience like no other. Upon entering through the grand double doors, youll be welcomed by an abundance of sunlight pouring in through expansive arched Lowen windows that fill the home with warmth, soaring ceilings, lightly painted walls and an expansive formal seating area that is perfect for entertaining. Take gourmet to the next level in this fully equipped kitchen. It offers beautiful cherry wood custom cabinetry, granite countertops, a top notch 6-burner Wolf cooktop, two Sub-Zero refrigerators, dual Bosch dishwashers, a nicely sized center island with a vegetable sink and a breakfast bar to enjoy a quick snack. The home features four spacious bedrooms and four luxurious bathrooms, providing ample room for family and guests to unwind in style. The primary suite is an oasis of tranquility, offering stunning views and premium amenities. The spa-like en-suite bathroom is a true escape, with a soaking tub and a walk-in shower with multiple shower heads. The upper level includes a versatile sitting area, ideal for gathering or relaxing. Head to the lower level of this villa and unlock endless potential. Whether you dream of creating a personal gym, a private theater, or a deluxe guest suite with its own entrance, this space is designed to suit your needs. Outside, youll find your own private oasis. Dive into the custom-designed pool, glide down the water slide, or relax on the beach entry or in the bubbling hot tub. The expansive backyard is also perfect for outdoor entertaining, surrounded by lush scenery that adds a perfect backdrop to any gathering. If you're looking for some fun, hop on your golf cart for a quick trip to the clubhouse for a meal or a friendly round of golf. Tucked behind lush landscaping is a solar array that adds an eco-friendly touch to the property while also helping save on your energy bills. This Mediterranean villa is more than a residenceit's a lifestyle. Experience ultimate luxury in this serene retreat, where every aspect has been thoughtfully designed for your comfort and pleasure.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "3252 Canyon Oaks Ter",
        "street": "3252 Canyon Oaks Ter",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 4,
        "full_baths": 5,
        "half_baths": 0,
        "sqft": 7073,
        "year_built": 2005,
        "days_on_mls": 21,
        "list_price": 1750000,
        "list_date": "2025-01-09",
        "assessed_value": 1500000,
        "estimated_value": 2157500,
        "tax": 16613,
        "tax_history": [
            {
            "year": 2023,
            "tax": 16613,
            "assessment": {
                "building": 1225000,
                "land": 275000,
                "total": 1500000
            }
            },
            {
            "year": 2022,
            "tax": 15618,
            "assessment": {
                "building": 1130000,
                "land": 275000,
                "total": 1405000
            }
            },
            {
            "year": 2021,
            "tax": 7312,
            "assessment": {
                "building": 1090000,
                "land": 225000,
                "total": 1315000
            }
            },
            {
            "year": 2020,
            "tax": 13552,
            "assessment": {
                "building": 985000,
                "land": 225000,
                "total": 1210000
            }
            },
            {
            "year": 2019,
            "tax": 13459,
            "assessment": {
                "building": 975000,
                "land": 225000,
                "total": 1200000
            }
            },
            {
            "year": 2018,
            "tax": 13476,
            "assessment": {
                "building": 975000,
                "land": 225000,
                "total": 1200000
            }
            },
            {
            "year": 2017,
            "tax": 14033,
            "assessment": {
                "building": 1025000,
                "land": 225000,
                "total": 1250000
            }
            },
            {
            "year": 2016,
            "tax": 12535,
            "assessment": {
                "building": 1000000,
                "land": 200000,
                "total": 1200000
            }
            },
            {
            "year": 2015,
            "tax": 12727,
            "assessment": {
                "building": 1000000,
                "land": 200000,
                "total": 1200000
            }
            },
            {
            "year": 2014,
            "tax": 11181,
            "assessment": {
                "building": 860000,
                "land": 200000,
                "total": 1060000
            }
            },
            {
            "year": 2013,
            "tax": 10411,
            "assessment": {
                "building": 767000,
                "land": 200000,
                "total": 967000
            }
            },
            {
            "year": 2012,
            "tax": 10003,
            "assessment": {
                "building": 767000,
                "land": 200000,
                "total": 967000
            }
            },
            {
            "year": 2010,
            "tax": 11046,
            "assessment": {
                "building": 850000,
                "land": 200000,
                "total": 1050000
            }
            },
            {
            "year": 2009,
            "tax": 12828,
            "assessment": {
                "building": 910000,
                "land": 290000,
                "total": 1200000
            }
            },
            {
            "year": 2008,
            "tax": 16524,
            "assessment": {
                "building": 1481600,
                "land": 85845,
                "total": 1567445
            }
            },
            {
            "year": 2007,
            "tax": 12395,
            "assessment": {
                "building": 1095000,
                "land": 84554,
                "total": 1179554
            }
            }
        ],
        "lot_sqft": 49049,
        "price_per_sqft": 247,
        "latitude": 39.762795,
        "longitude": -121.775612,
        "county": "Butte",
        "hoa_fee": 128,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/7d59509493f27fe491129ed7ef4a9db9l-m3408875051od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4846
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/18-Lobelia-Ct_Chico_CA_95973_M27198-28295",
        "property_id": "2719828295",
        "listing_id": "2976995734",
        "mls": "MRCA",
        "mls_id": "SN25004881",
        "status": "FOR_SALE",
        "text": "Prime Location in North Chico! Nestled in a peaceful cul-de-sac, this charming home is a decorators dream, packed with features that are sure to impress. As you arrive, the private driveway immediately sets this property apart. Step inside and be greeted by soaring vaulted ceilings, light and airy walls, elegant tile flooring, and charming wainscotting that adds a touch of sophistication throughout. The spacious living room invites you to unwind, offering the perfect setting for cozy evenings. The kitchen is a true culinary haven, equipped with granite countertops, stylish wood cabinetry, an eye-catching tile backsplash, modern appliances, and a gas cooktop that makes meal prep effortless. The quaint breakfast bar is ideal for quick bites or morning coffee. The primary bedroom is your personal retreat, complete with private backyard access and a spa-inspired en suite bathroom featuring dual sinks, a walk-in closet, an expansive vanity area, and a tiled walk-in shower. Additional highlights of this home include recessed lighting, ceiling fans throughout, three generously sized guest bedrooms, a convenient indoor laundry room with storage, a dedicated dining area, an attached two-car garage, and energy-saving solar panels. Step outside to find the ultimate backyard oasis, perfect for entertaining. Enjoy barbecues under the covered pergola while the lush lawn provides ample space for pets or play. With its desirable location and an extensive list of amenities, this home offers a rare opportunity you wont want to miss!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "18 Lobelia Ct",
        "street": "18 Lobelia Ct",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 4,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1971,
        "year_built": 2007,
        "days_on_mls": 22,
        "list_price": 525000,
        "list_date": "2025-01-08",
        "assessed_value": 379460,
        "estimated_value": 541300,
        "tax": 4352,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4352,
            "assessment": {
                "building": 242924,
                "land": 136536,
                "total": 379460
            }
            },
            {
            "year": 2022,
            "tax": 4164,
            "assessment": {
                "building": 238161,
                "land": 133859,
                "total": 372020
            }
            },
            {
            "year": 2021,
            "tax": 4305,
            "assessment": {
                "building": 233492,
                "land": 131235,
                "total": 364727
            }
            },
            {
            "year": 2020,
            "tax": 4355,
            "assessment": {
                "building": 231098,
                "land": 129890,
                "total": 360988
            }
            },
            {
            "year": 2019,
            "tax": 4268,
            "assessment": {
                "building": 226567,
                "land": 127344,
                "total": 353911
            }
            },
            {
            "year": 2018,
            "tax": 4083,
            "assessment": {
                "building": 222125,
                "land": 124848,
                "total": 346973
            }
            },
            {
            "year": 2017,
            "tax": 4763,
            "assessment": {
                "building": 217770,
                "land": 122400,
                "total": 340170
            }
            },
            {
            "year": 2016,
            "tax": 3799,
            "assessment": {
                "building": 186000,
                "land": 110000,
                "total": 296000
            }
            },
            {
            "year": 2015,
            "tax": 4187,
            "assessment": {
                "building": 225000,
                "land": 110000,
                "total": 335000
            }
            },
            {
            "year": 2014,
            "tax": 4007,
            "assessment": {
                "building": 210000,
                "land": 110000,
                "total": 320000
            }
            },
            {
            "year": 2013,
            "tax": 3967,
            "assessment": {
                "building": 220000,
                "land": 90000,
                "total": 310000
            }
            },
            {
            "year": 2012,
            "tax": 3431,
            "assessment": {
                "building": 176000,
                "land": 100000,
                "total": 276000
            }
            },
            {
            "year": 2010,
            "tax": 3929,
            "assessment": {
                "building": 217000,
                "land": 110000,
                "total": 327000
            }
            },
            {
            "year": 2009,
            "tax": 4541,
            "assessment": {
                "building": 217000,
                "land": 110000,
                "total": 353640
            }
            },
            {
            "year": 2008,
            "tax": 4995,
            "assessment": {
                "building": 260100,
                "land": 163200,
                "total": 445010
            }
            },
            {
            "year": 2007,
            "tax": 1250,
            "assessment": {
                "building": null,
                "land": 95212,
                "total": 95212
            }
            }
        ],
        "lot_sqft": 8276,
        "price_per_sqft": 266,
        "latitude": 39.765166,
        "longitude": -121.830342,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/b245beb4e0ade8af5401414e88fb28c7l-b1601276096od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3726
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/38-Moraga-Dr_Chico_CA_95926_M22135-47356",
        "property_id": "2213547356",
        "listing_id": "2976956896",
        "mls": "MRCA",
        "mls_id": "SN25002461",
        "status": "PENDING",
        "text": "AWESOME HOME !!!! This huge 3 bd/ 2 bath home has all the bells and whistles. Screened patios, sunroom, quartz countertops, laminate floors, tiled bathrooms. Huge .28 acre lot with trees and magnificent gazebo. Enough room to put in your own pool. Raised beds for gardening. This home is in a great neighborhood just 1.5 miles from Bidwell Park. Take a walk by the Lindo Channel. Home has new paint, laminate floors, dual pane windows and so much more. Its a must see property. Seller is anxious and will look at all offers ! This won't last long",
        "style": "SINGLE_FAMILY",
        "full_street_line": "38 Moraga Dr",
        "street": "38 Moraga Dr",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1810,
        "year_built": 1966,
        "days_on_mls": 23,
        "list_price": 515000,
        "list_date": "2025-01-07",
        "assessed_value": 432094,
        "estimated_value": 454500,
        "tax": 4739,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4739,
            "assessment": {
                "building": 249822,
                "land": 182272,
                "total": 432094
            }
            },
            {
            "year": 2022,
            "tax": 4661,
            "assessment": {
                "building": 244924,
                "land": 178699,
                "total": 423623
            }
            },
            {
            "year": 2021,
            "tax": 4572,
            "assessment": {
                "building": 240122,
                "land": 175196,
                "total": 415318
            }
            },
            {
            "year": 2020,
            "tax": 4559,
            "assessment": {
                "building": 237660,
                "land": 173400,
                "total": 411060
            }
            },
            {
            "year": 2019,
            "tax": 4474,
            "assessment": {
                "building": 233000,
                "land": 170000,
                "total": 403000
            }
            },
            {
            "year": 2018,
            "tax": 3746,
            "assessment": {
                "building": 205970,
                "land": 132032,
                "total": 338002
            }
            },
            {
            "year": 2017,
            "tax": 3669,
            "assessment": {
                "building": 201932,
                "land": 129444,
                "total": 331376
            }
            },
            {
            "year": 2016,
            "tax": 3347,
            "assessment": {
                "building": 197973,
                "land": 126906,
                "total": 324879
            }
            },
            {
            "year": 2015,
            "tax": 2452,
            "assessment": {
                "building": 119391,
                "land": 109797,
                "total": 229188
            }
            },
            {
            "year": 2014,
            "tax": 2406,
            "assessment": {
                "building": 117053,
                "land": 107647,
                "total": 224700
            }
            },
            {
            "year": 2013,
            "tax": 2438,
            "assessment": {
                "building": 116524,
                "land": 107161,
                "total": 223685
            }
            },
            {
            "year": 2012,
            "tax": 2297,
            "assessment": {
                "building": 114240,
                "land": 105060,
                "total": 219300
            }
            },
            {
            "year": 2010,
            "tax": 3391,
            "assessment": {
                "building": 199000,
                "land": 120000,
                "total": 319000
            }
            },
            {
            "year": 2009,
            "tax": 3324,
            "assessment": {
                "building": 199000,
                "land": 120000,
                "total": 319000
            }
            },
            {
            "year": 2008,
            "tax": 3989,
            "assessment": {
                "building": 229500,
                "land": 153000,
                "total": 382500
            }
            },
            {
            "year": 2007,
            "tax": 3884,
            "assessment": {
                "building": 225000,
                "land": 150000,
                "total": 375000
            }
            }
        ],
        "lot_sqft": 12197,
        "price_per_sqft": 285,
        "latitude": 39.754614,
        "longitude": -121.830805,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/0fd1933e25ea614074481a2746f1af66l-m20755253od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4511
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1685-Park-View-Ln_Chico_CA_95926_M21639-46387",
        "property_id": "2163946387",
        "listing_id": "2976984268",
        "mls": "MRCA",
        "mls_id": "SN25001575",
        "status": "PENDING",
        "text": "Nestled in a peaceful and desirable neighborhood, this delightful 3-bedroom, 2-bathroom home offers the perfect blend of comfort and convenience. With 1, 440 square feet of well-designed living space, this home is ideal for modern living and entertaining. Step inside to find a spacious floor plan that seamlessly connects the living, dining, and kitchen areas. The inviting living room features large windows that fill the space with natural light, creating a warm and airy atmosphere. The kitchen is equipped with all the essentials, including appliances that are all included, making this home truly move-in ready. Outside, youll find a peaceful backyard perfect for relaxation and entertaining. Soak away the stress of the day in your own private hot tub, or simply enjoy the serenity of the well-maintained yard. With owned solar panels, youll appreciate the energy savings and eco-friendly benefits of this home. The homes location is truly a standout feature. Youre just a short walk from Sierra View Elementary School and the beauty and outdoor activities of Bidwell Park, making this the perfect spot for those who enjoy hiking, biking, or simply taking in natures beauty. With all appliances included, this home is ready for you to move in and start enjoying the best of Chico living. Dont miss the opportunity to make this beautiful home yours schedule your showing today!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "1685 Park View Ln",
        "street": "1685 Park View Ln",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1440,
        "year_built": 1970,
        "days_on_mls": 22,
        "list_price": 475000,
        "list_date": "2025-01-08",
        "assessed_value": 475983,
        "estimated_value": 474546,
        "tax": 5226,
        "tax_history": [
            {
            "year": 2023,
            "tax": 5226,
            "assessment": {
                "building": 283509,
                "land": 192474,
                "total": 475983
            }
            },
            {
            "year": 2022,
            "tax": 5142,
            "assessment": {
                "building": 277950,
                "land": 188700,
                "total": 466650
            }
            },
            {
            "year": 2021,
            "tax": 3747,
            "assessment": {
                "building": 195936,
                "land": 142756,
                "total": 338692
            }
            },
            {
            "year": 2020,
            "tax": 3741,
            "assessment": {
                "building": 193927,
                "land": 141293,
                "total": 335220
            }
            },
            {
            "year": 2019,
            "tax": 3679,
            "assessment": {
                "building": 190125,
                "land": 138523,
                "total": 328648
            }
            },
            {
            "year": 2018,
            "tax": 3615,
            "assessment": {
                "building": 186398,
                "land": 135807,
                "total": 322205
            }
            },
            {
            "year": 2017,
            "tax": 3546,
            "assessment": {
                "building": 182744,
                "land": 133145,
                "total": 315889
            }
            },
            {
            "year": 2016,
            "tax": 2897,
            "assessment": {
                "building": 150000,
                "land": 125000,
                "total": 275000
            }
            },
            {
            "year": 2015,
            "tax": 2941,
            "assessment": {
                "building": 150000,
                "land": 125000,
                "total": 275000
            }
            },
            {
            "year": 2014,
            "tax": 2853,
            "assessment": {
                "building": 160000,
                "land": 115000,
                "total": 275000
            }
            },
            {
            "year": 2013,
            "tax": 2527,
            "assessment": {
                "building": 140000,
                "land": 100000,
                "total": 240000
            }
            },
            {
            "year": 2012,
            "tax": 2532,
            "assessment": {
                "building": 150000,
                "land": 100000,
                "total": 250000
            }
            },
            {
            "year": 2010,
            "tax": 2732,
            "assessment": {
                "building": 145000,
                "land": 120000,
                "total": 265000
            }
            },
            {
            "year": 2009,
            "tax": 2986,
            "assessment": {
                "building": 164309,
                "land": 119715,
                "total": 284024
            }
            },
            {
            "year": 2008,
            "tax": 3049,
            "assessment": {
                "building": 184119,
                "land": 169793,
                "total": 353912
            }
            },
            {
            "year": 2007,
            "tax": 3572,
            "assessment": {
                "building": 180509,
                "land": 166464,
                "total": 346973
            }
            }
        ],
        "lot_sqft": 6534,
        "price_per_sqft": 330,
        "latitude": 39.750207,
        "longitude": -121.807235,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/75a6157ebd9550593a7b886bc0a9fec7l-m3546962401od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4055
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1095-Woodland-Ave_Chico_CA_95928_M10018-45235",
        "property_id": "1001845235",
        "listing_id": "2976931978",
        "mls": "MRCA",
        "mls_id": "SN24236939",
        "status": "FOR_SALE",
        "text": "Welcome to this Esquisite European Estate. Step inside and experience the elegant design of Old World Charm. High ceilings, magnificent crown molding with special details, custom wood paneling, antique French & Belgium doors, French Chandelier, custom hand carved spindles from Italy showcase the staircase leading up to the 2nd. floor. Flooring throughout is either original hardwood, parque or Carrera marble. All wood work is custom & is European Alder. Custom 12 in baseboards, ceiling medallions, large custom window over looking magnificent Bidwell Park. All outside brick work is custom. The bricks were rescued from the SF earthquake. Herringbone brick detailing. Two tall custom brick spiral chimneys, real cooper gutters & so many more outstanding features that I cannot list. The kitchen features Bosh dishwasher, Viking 48 double oven, gas stove with skillet, Viking refrigerator, Carrera 1 marble counters with custom etched detailng (replicating French Patisserie)& double ogee. Custom double sink, custom cabinetry & two large antique pine free-standing cabinet units. Basement with washer/dryer. Primary Master Suite is 1400 square feet, features a wood burning fireplace with herringbone brick, beautiful copper gas lamps outside master suite balconey tall wood paneled vaulted ceiling, double French Doors open out to a brick floor balcony overlooking beautiful Bidwell Park. Perfect for your morning coffee. There is a 2nd. floor office or a 5th bedroom/Nursery. Amazing master bath with many unique features. Down stares consists of 2 additional bedrooms, 2 baths, a study/bedroom, kitchen, living & sunroom plus a formal dining room. All rooms throughout this home are truly esquite. This amazing home is 3, 824 sq. ft., was originally built in 1924, then in 2007 sellers rebuilt all of the home except the sunroom. Woodland Ave. is an historic neighborhood and is famous to Chico. Rumor has it that back in 1938 when the original Robin Hood was filmed in Bidwell Park that a number of actors stayed in this home. It is directly across the street from famous Bidwell Park. It is in walking distance to beautiful downtown Chico, CSUC and many delightful restaurants and stores in downtown Chico. Don't miss out in this amazing home. Call for a private showing.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "1095 Woodland Ave",
        "street": "1095 Woodland Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 4,
        "full_baths": 2,
        "half_baths": 1,
        "sqft": 3824,
        "year_built": 1925,
        "days_on_mls": 23,
        "list_price": 2100000,
        "list_date": "2025-01-07",
        "assessed_value": 948947,
        "estimated_value": 1111600,
        "tax": 10485,
        "tax_history": [
            {
            "year": 2023,
            "tax": 10485,
            "assessment": {
                "building": 705342,
                "land": 243605,
                "total": 948947
            }
            },
            {
            "year": 2022,
            "tax": 10318,
            "assessment": {
                "building": 691512,
                "land": 238829,
                "total": 930341
            }
            },
            {
            "year": 2021,
            "tax": 10122,
            "assessment": {
                "building": 677953,
                "land": 234147,
                "total": 912100
            }
            },
            {
            "year": 2020,
            "tax": 10093,
            "assessment": {
                "building": 671002,
                "land": 231747,
                "total": 902749
            }
            },
            {
            "year": 2019,
            "tax": 9908,
            "assessment": {
                "building": 657846,
                "land": 227203,
                "total": 885049
            }
            },
            {
            "year": 2018,
            "tax": 9725,
            "assessment": {
                "building": 644948,
                "land": 222749,
                "total": 867697
            }
            },
            {
            "year": 2017,
            "tax": 9528,
            "assessment": {
                "building": 632302,
                "land": 218382,
                "total": 850684
            }
            },
            {
            "year": 2016,
            "tax": 8231,
            "assessment": {
                "building": 465000,
                "land": 325000,
                "total": 790000
            }
            },
            {
            "year": 2015,
            "tax": 8356,
            "assessment": {
                "building": 490000,
                "land": 300000,
                "total": 790000
            }
            },
            {
            "year": 2014,
            "tax": 7892,
            "assessment": {
                "building": 450000,
                "land": 300000,
                "total": 750000
            }
            },
            {
            "year": 2013,
            "tax": 7353,
            "assessment": {
                "building": 415000,
                "land": 270000,
                "total": 685000
            }
            },
            {
            "year": 2012,
            "tax": 6648,
            "assessment": {
                "building": 584244,
                "land": 201786,
                "total": 786030
            }
            },
            {
            "year": 2010,
            "tax": 6623,
            "assessment": {
                "building": 572789,
                "land": 197830,
                "total": 770619
            }
            },
            {
            "year": 2009,
            "tax": 6740,
            "assessment": {
                "building": 436003,
                "land": 196352,
                "total": 632355
            }
            },
            {
            "year": 2008,
            "tax": 6506,
            "assessment": {
                "building": 428470,
                "land": 192960,
                "total": 621430
            }
            },
            {
            "year": 2007,
            "tax": 5453,
            "assessment": {
                "building": 336736,
                "land": 189177,
                "total": 525913
            }
            }
        ],
        "lot_sqft": 8712,
        "price_per_sqft": 549,
        "latitude": 39.73401,
        "longitude": -121.827315,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/61eca4f18998a108a1da54989653497dl-m3123505063od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4084
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/28-Whitewood-Way_Chico_CA_95973_M22894-58081",
        "property_id": "2289458081",
        "listing_id": "2976935753",
        "mls": "MRCA",
        "mls_id": "SN25003327",
        "status": "CONTINGENT",
        "text": "Welcome to your perfect home! This stunning 3-bedroom, 2-bathroom property offers 1, 236 square feet of beautifully updated living space, ready for you to move in and make memories. With brand-new paint throughout and freshly updated bathrooms, this home feels modern, and inviting. The rustic wood shiplap interior siding added throughout the home adds a touch of charm and character. There is luxury vinyl wood flooring in the common areas that create a warm and welcoming atmosphere while cozy Berber carpet in the bedrooms ensures comfort in all the right places. Step outside to an open and landscaped backyard thats perfect for entertaining or relaxing. The covered back patio is the ideal spot for morning coffee or evening gatherings. All appliances are included, making your move-in process seamless and stress-free. The attached 2-car garage adds convenience and ample storage for hobbies, a workshop or all your recreational toys! Situated on a quiet cul-de-sac drive through street, this home is just one block from the NEW Centennial Park, offering endless opportunities for outdoor fun and recreation for everyone. Located close to grocery stores and shopping, with quick access to both Upper and Lower Park, youll love the balance of convenience and serenity this home provides. Whether youre seeking peace and relaxation or proximity to Chicos best amenities, this location has it all. Dont waitthis incredible home wont last long! Schedule a showing with your agent today and see all it has to offer before its gone!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "28 Whitewood Way",
        "street": "28 Whitewood Way",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1236,
        "year_built": 1988,
        "days_on_mls": 23,
        "list_price": 420000,
        "list_date": "2025-01-07",
        "assessed_value": 267994,
        "estimated_value": 405100,
        "tax": 2992,
        "tax_history": [
            {
            "year": 2023,
            "tax": 2992,
            "assessment": {
                "building": 140928,
                "land": 127066,
                "total": 267994
            }
            },
            {
            "year": 2022,
            "tax": 2944,
            "assessment": {
                "building": 138165,
                "land": 124575,
                "total": 262740
            }
            },
            {
            "year": 2021,
            "tax": 2888,
            "assessment": {
                "building": 135456,
                "land": 122133,
                "total": 257589
            }
            },
            {
            "year": 2020,
            "tax": 2880,
            "assessment": {
                "building": 134068,
                "land": 120881,
                "total": 254949
            }
            },
            {
            "year": 2019,
            "tax": 2828,
            "assessment": {
                "building": 131440,
                "land": 118511,
                "total": 249951
            }
            },
            {
            "year": 2018,
            "tax": 2776,
            "assessment": {
                "building": 128863,
                "land": 116188,
                "total": 245051
            }
            },
            {
            "year": 2017,
            "tax": 2720,
            "assessment": {
                "building": 126337,
                "land": 113910,
                "total": 240247
            }
            },
            {
            "year": 2016,
            "tax": 2482,
            "assessment": {
                "building": 123860,
                "land": 111677,
                "total": 235537
            }
            },
            {
            "year": 2015,
            "tax": 2482,
            "assessment": {
                "building": 122000,
                "land": 110000,
                "total": 232000
            }
            },
            {
            "year": 2014,
            "tax": 1513,
            "assessment": {
                "building": 89007,
                "land": 59777,
                "total": 148784
            }
            },
            {
            "year": 2013,
            "tax": 1530,
            "assessment": {
                "building": 88605,
                "land": 59507,
                "total": 148112
            }
            },
            {
            "year": 2012,
            "tax": 1440,
            "assessment": {
                "building": 86868,
                "land": 58341,
                "total": 145209
            }
            },
            {
            "year": 2010,
            "tax": 1422,
            "assessment": {
                "building": 85165,
                "land": 57198,
                "total": 142363
            }
            },
            {
            "year": 2009,
            "tax": 1447,
            "assessment": {
                "building": 84529,
                "land": 56771,
                "total": 141300
            }
            },
            {
            "year": 2008,
            "tax": 1396,
            "assessment": {
                "building": 83069,
                "land": 55791,
                "total": 138860
            }
            },
            {
            "year": 2007,
            "tax": 1357,
            "assessment": {
                "building": 81441,
                "land": 54698,
                "total": 136139
            }
            }
        ],
        "lot_sqft": 6970,
        "price_per_sqft": 340,
        "latitude": 39.767749,
        "longitude": -121.836192,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/5abeb86f6ee98821eb35e9d55fe84e98l-m70959650od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4535
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/9-Camba-Ct_Chico_CA_95928_M25438-75327",
        "property_id": "2543875327",
        "listing_id": "2976935765",
        "mls": "MRCA",
        "mls_id": "SN25003672",
        "status": "FOR_SALE",
        "text": "Desirable single story 3-bedroom 2 full bath house built in 2017 on a CUL-DE-SAC with large 7.624 kW SOLAR array with NEM 2.0 buy back rates producing so much that seller actually gottten PAID by PG&E for the excess power every year since it was install in 2022. Current payments on the solar are only $207 a month and it's assumable at 2.9% interest (on approved credit). Fresh paint and new carpets in the bedrooms and high-end luxury vinyl flooring make this a crisp turn-key home. An entertainer's delight with a large kitchen opening to a sizable dining and living area. Custom shutters throughout open onto a sunny backyard with concrete patios landscaped with productive fruit trees and nice privacy fences. Prime location just moments from the massive and famous Bidwell Park offering outstanding mountain biking, hiking, disk golf and amazing swimming holes. Canyon Oaks Golf course is an easy stroll away, as is Miriam Park with its award-winning walking community, restaurants, music venues and playgrounds. A spacious 2-car garage and covered front porch add to the bucket-list features. Only 30 minutes from Butte Meadows and National Forest campgrounds with year-round adventures, gold-panning, sledding and pristine wild lands. 8 minutes to downtown Chico and the thriving art galleries, shopping and year-round farmer's market one would expect in a university town.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "9 Camba Ct",
        "street": "9 Camba Ct",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1686,
        "year_built": 2017,
        "days_on_mls": 23,
        "list_price": 478000,
        "list_date": "2025-01-07",
        "assessed_value": 371837,
        "estimated_value": 478000,
        "tax": 4146,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4146,
            "assessment": {
                "building": 235133,
                "land": 136704,
                "total": 371837
            }
            },
            {
            "year": 2022,
            "tax": 4080,
            "assessment": {
                "building": 230523,
                "land": 134024,
                "total": 364547
            }
            },
            {
            "year": 2021,
            "tax": 4003,
            "assessment": {
                "building": 226003,
                "land": 131397,
                "total": 357400
            }
            },
            {
            "year": 2020,
            "tax": 3992,
            "assessment": {
                "building": 223686,
                "land": 130050,
                "total": 353736
            }
            },
            {
            "year": 2019,
            "tax": 3920,
            "assessment": {
                "building": 219300,
                "land": 127500,
                "total": 346800
            }
            },
            {
            "year": 2018,
            "tax": 3848,
            "assessment": {
                "building": 215000,
                "land": 125000,
                "total": 340000
            }
            },
            {
            "year": 2017,
            "tax": 714,
            "assessment": {
                "building": null,
                "land": 63132,
                "total": 63132
            }
            },
            {
            "year": 2016,
            "tax": 664,
            "assessment": {
                "building": null,
                "land": 63026,
                "total": 63026
            }
            }
        ],
        "lot_sqft": 4792,
        "price_per_sqft": 284,
        "latitude": 39.74344,
        "longitude": -121.779715,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/f9ef7000850971fb876edf79a51411cdl-m950971955od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3063
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1095-Woodland-Ave_Chico_CA_95928_M10018-45235",
        "property_id": "1001845235",
        "listing_id": "2976932091",
        "mls": "SCCA",
        "mls_id": "224127750",
        "status": "FOR_SALE",
        "text": "Welcome to this Exquisite European Estate. Step inside and experience the elegant design of old world charm. High ceilings, magnificent crown molding with special details, custom wood paneling, antique French & Belgium doors, French Chandelier, custom hand carved spindles from Italy showcase the staircase leading up to the 2nd. floor. Flooring throughout is either original hardwood or Carrera marble. All wood work is custom & is European Alder. Custom 12 in baseboards, ceiling medallions, large custom window over looking magnificent Bidwell Park. All outside brick work is custom. The bricks were rescued from the SF earthquake. Herringbone brick detailing. Two tall custom brick spiral chimneys, real cooper gutters & so many more outstanding features that I cannot list. The kitchen features Bosh dishwasher, Viking 48 double oven, gas stove with skillet, Viking refrigerator, Carrera 1 marble counters with custom etched detailing (replicating French Patisserie)& double ogee. Custom double sink, custom cabinetry & two large antique pine free-standing cabinet units. Basement with washer/dryer. Primary Master Suite is 1400 square feet, features a wood burning fireplace with herringbone brick, beautiful copper gas lamps outside master suite balcony tall wood paneled vaulted ceiling, double French Doors open out to a brick floor balcony overlooking beautiful Bidwell Park. Perfect for your morning coffee. There is a 2nd. floor office or a 5th bedroom/Nursery. Amazing master bath with many unique features. Down stares consists of 2 additional bedrooms, 2 baths, a study/bedroom, kitchen, living & sunroom plus a formal dining room. All rooms throughout this home are truly exsquite. This amazing home is 3, 824 sq. ft., was originally built in 1924, then in 2007 sellers rebuilt all of the home except the sunroom. Woodland Ave. is an historic neighborhood and is famous to Chico. Rumor has it that back in 1938 when the original Robin Hood was filmed in Bidwell Park that a number of actors stayed in this home. It is directly across the street from famous Bidwell Park. It is in walking distance to beautiful downtown Chico, CSUC and many delightful restaurants and stores in downtown Chico. Don't miss out in this amazing home. Call for a private showing.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "1095 N Woodland Ave",
        "street": "1095 N Woodland Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 4,
        "full_baths": 2,
        "half_baths": 1,
        "sqft": 3824,
        "year_built": 1925,
        "days_on_mls": 23,
        "list_price": 2100000,
        "list_date": "2025-01-07",
        "assessed_value": 948947,
        "estimated_value": 1111600,
        "tax": 10485,
        "tax_history": [
            {
            "year": 2023,
            "tax": 10485,
            "assessment": {
                "building": 705342,
                "land": 243605,
                "total": 948947
            }
            },
            {
            "year": 2022,
            "tax": 10318,
            "assessment": {
                "building": 691512,
                "land": 238829,
                "total": 930341
            }
            },
            {
            "year": 2021,
            "tax": 10122,
            "assessment": {
                "building": 677953,
                "land": 234147,
                "total": 912100
            }
            },
            {
            "year": 2020,
            "tax": 10093,
            "assessment": {
                "building": 671002,
                "land": 231747,
                "total": 902749
            }
            },
            {
            "year": 2019,
            "tax": 9908,
            "assessment": {
                "building": 657846,
                "land": 227203,
                "total": 885049
            }
            },
            {
            "year": 2018,
            "tax": 9725,
            "assessment": {
                "building": 644948,
                "land": 222749,
                "total": 867697
            }
            },
            {
            "year": 2017,
            "tax": 9528,
            "assessment": {
                "building": 632302,
                "land": 218382,
                "total": 850684
            }
            },
            {
            "year": 2016,
            "tax": 8231,
            "assessment": {
                "building": 465000,
                "land": 325000,
                "total": 790000
            }
            },
            {
            "year": 2015,
            "tax": 8356,
            "assessment": {
                "building": 490000,
                "land": 300000,
                "total": 790000
            }
            },
            {
            "year": 2014,
            "tax": 7892,
            "assessment": {
                "building": 450000,
                "land": 300000,
                "total": 750000
            }
            },
            {
            "year": 2013,
            "tax": 7353,
            "assessment": {
                "building": 415000,
                "land": 270000,
                "total": 685000
            }
            },
            {
            "year": 2012,
            "tax": 6648,
            "assessment": {
                "building": 584244,
                "land": 201786,
                "total": 786030
            }
            },
            {
            "year": 2010,
            "tax": 6623,
            "assessment": {
                "building": 572789,
                "land": 197830,
                "total": 770619
            }
            },
            {
            "year": 2009,
            "tax": 6740,
            "assessment": {
                "building": 436003,
                "land": 196352,
                "total": 632355
            }
            },
            {
            "year": 2008,
            "tax": 6506,
            "assessment": {
                "building": 428470,
                "land": 192960,
                "total": 621430
            }
            },
            {
            "year": 2007,
            "tax": 5453,
            "assessment": {
                "building": 336736,
                "land": 189177,
                "total": 525913
            }
            }
        ],
        "lot_sqft": 8712,
        "price_per_sqft": 549,
        "latitude": 39.73401,
        "longitude": -121.827315,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/9eb7b455839abd226ea45bb3825aac70l-b3408500127od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4572
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/9-Celtic-Ct_Chico_CA_95926_M96120-25075",
        "property_id": "9612025075",
        "listing_id": "2976875042",
        "mls": "MRCA",
        "mls_id": "SN25001481",
        "status": "FOR_SALE",
        "text": "This stunning 2019-built home is better than brand new with upgrades throughout! Nestled in an adorable cul-de-sac, this property offers both style and convenience, located near Chicos most beloved parks, including Upper Bidwell and Wildwood Park, as well as top-rated schools such as Marigold Elementary and PV High School. The curb appeal is undeniable, featuring a fully landscaped yard adorned with a lovely maple tree and fruit trees, a remote-controlled security gate, and spacious covered patios in both the front and backyardperfect for relaxing or entertaining. Inside, the open-concept design immediately impresses with a spacious great room that seamlessly blends living and dining areas. The dining area boasts elegant tray ceilings, offering ample space for gatherings. The living room connects to the kitchen, which is a showstopper with its quartz countertops, peninsula island with bar seating, white cabinetry, upgraded black stainless steel Whirlpool appliances, and a sleek white tile backsplash. A built-in desk area adds functionality for homework or remote work. The spacious primary suite includes a walk-in closet, a linen closet, and an en-suite bathroom with double quartz-topped sinks and a shower enclosed by upgraded glass sliders. Two guest bedrooms share a beautifully appointed bathroom, also featuring quartz counters, double sinks, and an upgraded tub with glass sliders. Additional features include a whole-house fan, a security system, luxury vinyl plank flooring and plantation shutters throughout, laundry area cabinetry, and gutter guards for easy maintenance. This move-in-ready home is the perfect blend of modern luxury and thoughtful design.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "9 Celtic Ct",
        "street": "9 Celtic Ct",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1704,
        "year_built": 2019,
        "days_on_mls": 26,
        "list_price": 539000,
        "list_date": "2025-01-04",
        "assessed_value": 439284,
        "estimated_value": 548020,
        "tax": 5364,
        "tax_history": [
            {
            "year": 2023,
            "tax": 5364,
            "assessment": {
                "building": 271097,
                "land": 168187,
                "total": 439284
            }
            },
            {
            "year": 2022,
            "tax": 5605,
            "assessment": {
                "building": 265782,
                "land": 164890,
                "total": 430672
            }
            },
            {
            "year": 2021,
            "tax": 5515,
            "assessment": {
                "building": 260571,
                "land": 161657,
                "total": 422228
            }
            },
            {
            "year": 2020,
            "tax": 4636,
            "assessment": {
                "building": 257900,
                "land": 160000,
                "total": 417900
            }
            }
        ],
        "lot_sqft": 5663,
        "price_per_sqft": 316,
        "latitude": 39.761987,
        "longitude": -121.813596,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/0617a6ad43ddca464889dcef360e2f14l-m2209715710od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4818
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/555-Vallombrosa-Ave-Apt-39_Chico_CA_95926_M28454-77315",
        "property_id": "2845477315",
        "listing_id": "2976876553",
        "mls": "MRCA",
        "mls_id": "SN25002080",
        "status": "PENDING",
        "text": "Charming 1 Bedroom, 1 Bathroom, Downstairs End Unit in the WoodOak Condominium Complex. Nestled in the highly desirable WoodOak Condominium community, this well-maintained home offers the perfect blend of comfort, style and convenience. The home is thoughtfully designed with an inviting outdoor courtyard, providing a private place to relax or entertain. The entrance to the condominium is beautifully landscaped, creating a warm and welcoming first impression. The complex itself offers a laid-back lifestyle, located just steps away from the lush greenery of Bidwell Park and within walking distance to downtown Chico. Residents can take full advantage of the fantastic amenities, including a sparkling inground pool, BBQ area, hot tub and a convenient car washing station. Whether you're seeking a tranquil retreat or an active, community-oriented lifestyle, this condominium delivers both. Don't miss your opportunity to call this wonderful home your own!",
        "style": "CONDOS",
        "full_street_line": "555 Vallombrosa Ave Apt 39",
        "street": "555 Vallombrosa Ave",
        "unit": "Apt 39",
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 1,
        "full_baths": 1,
        "half_baths": 0,
        "sqft": 702,
        "year_built": 1973,
        "days_on_mls": 26,
        "list_price": 189000,
        "list_date": "2025-01-04",
        "assessed_value": 176069,
        "estimated_value": 206100,
        "tax": 1965,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1965,
            "assessment": {
                "building": 86721,
                "land": 89348,
                "total": 176069
            }
            },
            {
            "year": 2022,
            "tax": 967,
            "assessment": {
                "building": 85021,
                "land": 87597,
                "total": 172618
            }
            },
            {
            "year": 2021,
            "tax": 1897,
            "assessment": {
                "building": 83354,
                "land": 85880,
                "total": 169234
            }
            },
            {
            "year": 2020,
            "tax": 1892,
            "assessment": {
                "building": 82500,
                "land": 85000,
                "total": 167500
            }
            },
            {
            "year": 2019,
            "tax": 1652,
            "assessment": {
                "building": 76500,
                "land": 76500,
                "total": 153000
            }
            },
            {
            "year": 2018,
            "tax": 1636,
            "assessment": {
                "building": 75000,
                "land": 75000,
                "total": 150000
            }
            },
            {
            "year": 2017,
            "tax": 970,
            "assessment": {
                "building": 57911,
                "land": 27571,
                "total": 85482
            }
            },
            {
            "year": 2016,
            "tax": 886,
            "assessment": {
                "building": 56776,
                "land": 27031,
                "total": 83807
            }
            },
            {
            "year": 2015,
            "tax": 886,
            "assessment": {
                "building": 55924,
                "land": 26625,
                "total": 82549
            }
            },
            {
            "year": 2014,
            "tax": 865,
            "assessment": {
                "building": 54829,
                "land": 26104,
                "total": 80933
            }
            },
            {
            "year": 2013,
            "tax": 873,
            "assessment": {
                "building": 54582,
                "land": 25987,
                "total": 80569
            }
            },
            {
            "year": 2012,
            "tax": 823,
            "assessment": {
                "building": 53512,
                "land": 25478,
                "total": 78990
            }
            },
            {
            "year": 2010,
            "tax": 814,
            "assessment": {
                "building": 52463,
                "land": 24979,
                "total": 77442
            }
            },
            {
            "year": 2009,
            "tax": 828,
            "assessment": {
                "building": 52071,
                "land": 24793,
                "total": 76864
            }
            },
            {
            "year": 2008,
            "tax": 799,
            "assessment": {
                "building": 51172,
                "land": 24365,
                "total": 75537
            }
            },
            {
            "year": 2007,
            "tax": 778,
            "assessment": {
                "building": 50169,
                "land": 23888,
                "total": 74057
            }
            }
        ],
        "lot_sqft": 0,
        "price_per_sqft": 269,
        "latitude": 39.735261,
        "longitude": -121.832151,
        "county": "Butte",
        "hoa_fee": 453,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/f40dca911b8d2823f981fbe941d93f34l-b3785838368od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 2490
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/993-Flying-V-St_Chico_CA_95928_M28168-94337",
        "property_id": "2816894337",
        "listing_id": "2977047193",
        "mls": "MRCA",
        "mls_id": "SN25005824",
        "status": "FOR_SALE",
        "text": "Location, location, location! This move-in-ready three bedroom, two bathroom home is conveniently located near shopping and dining. The open living area with a fireplace is a great feature for both entertaining and cozy nights in. The kitchen offers plenty of counter and cabinet space along with a convenient breakfast bar. The primary bedroom boasts a spacious bathroom designed for efficiency during your morning routine along with sliding glass doors that open to a serene backyard, perfect for evening relaxation. Other notable features include generously sized bedrooms with closet space, indoor laundry facilities, central heat/air and more. The back yard offers a spacious, private, fully fenced yard where you can plant a garden, put out your patio furniture, and have room to bbq and entertain! This is the next place you should call home!",
        "style": "CONDOS",
        "full_street_line": "993 Flying V St",
        "street": "993 Flying V St",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1278,
        "year_built": 1982,
        "days_on_mls": 21,
        "list_price": 305000,
        "list_date": "2025-01-09",
        "assessed_value": 312120,
        "estimated_value": 325100,
        "tax": 3506,
        "tax_history": [
            {
            "year": 2023,
            "tax": 3506,
            "assessment": {
                "building": 234090,
                "land": 78030,
                "total": 312120
            }
            },
            {
            "year": 2022,
            "tax": 3453,
            "assessment": {
                "building": 229500,
                "land": 76500,
                "total": 306000
            }
            },
            {
            "year": 2021,
            "tax": 3384,
            "assessment": {
                "building": 225000,
                "land": 75000,
                "total": 300000
            }
            },
            {
            "year": 2020,
            "tax": 1890,
            "assessment": {
                "building": 109892,
                "land": 54945,
                "total": 164837
            }
            },
            {
            "year": 2019,
            "tax": 1859,
            "assessment": {
                "building": 107738,
                "land": 53868,
                "total": 161606
            }
            },
            {
            "year": 2018,
            "tax": 1824,
            "assessment": {
                "building": 105626,
                "land": 52812,
                "total": 158438
            }
            },
            {
            "year": 2017,
            "tax": 1784,
            "assessment": {
                "building": 103555,
                "land": 51777,
                "total": 155332
            }
            },
            {
            "year": 2016,
            "tax": 1631,
            "assessment": {
                "building": 101525,
                "land": 50762,
                "total": 152287
            }
            },
            {
            "year": 2015,
            "tax": 1630,
            "assessment": {
                "building": 100000,
                "land": 50000,
                "total": 150000
            }
            },
            {
            "year": 2014,
            "tax": 1461,
            "assessment": {
                "building": 94746,
                "land": 39590,
                "total": 134336
            }
            },
            {
            "year": 2013,
            "tax": 1478,
            "assessment": {
                "building": 94318,
                "land": 39412,
                "total": 133730
            }
            },
            {
            "year": 2012,
            "tax": 1385,
            "assessment": {
                "building": 92469,
                "land": 38640,
                "total": 131109
            }
            },
            {
            "year": 2010,
            "tax": 1364,
            "assessment": {
                "building": 90656,
                "land": 37883,
                "total": 128539
            }
            },
            {
            "year": 2009,
            "tax": 1388,
            "assessment": {
                "building": 89979,
                "land": 37600,
                "total": 127579
            }
            },
            {
            "year": 2008,
            "tax": 1352,
            "assessment": {
                "building": 88425,
                "land": 36951,
                "total": 125376
            }
            },
            {
            "year": 2007,
            "tax": 1302,
            "assessment": {
                "building": 86692,
                "land": 36227,
                "total": 122919
            }
            }
        ],
        "lot_sqft": 4356,
        "price_per_sqft": 239,
        "latitude": 39.718863,
        "longitude": -121.798039,
        "county": "Butte",
        "hoa_fee": 207,
        "nearby_schools": "Butte County Office Of Education School District, Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/56c415370c314056ea33c71bab039e47l-b2225722055od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3497
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/8-Joy-Ln_Chico_CA_95926_M21399-09854",
        "property_id": "2139909854",
        "listing_id": "2976918735",
        "mls": "MRCA",
        "mls_id": "SN24252919",
        "status": "CONTINGENT",
        "text": "Located just steps from the iconic Bidwell Park, this inviting home perfectly combines comfort, charm, and a prime Chico location. Conveniently close to Sierra View School, local coffee shops, In Motion Fitness, and freeway access, it offers a lifestyle of ease and accessibility. Inside, two spacious living areas provide versatile options for relaxation and entertainment, anchored by a cozy wood-burning fireplace that sets the stage for warm, memorable evenings. Beautiful hardwood floors flow throughout the freshly painted interior, while energy-efficient dual-pane windows, newer whole house fan and substantial blown-in insulation enhance both style and comfort. The kitchen is a standout feature, offering ample storage, a convenient breakfast bar, and classic built-in cabinetry that blends functionality with timeless appeal. Situated on a corner lot, the property includes an attached two-car garage and plenty of space for gardening or outdoor activities in both the front and backyards. With its unbeatable location near Bidwell Parks scenic trails and recreation, this home offers the perfect balance of indoor comfort and outdoor adventuretruly a standout in the heart of Chico.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "8 Joy Ln",
        "street": "8 Joy Ln",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 1,
        "sqft": 1978,
        "year_built": 1973,
        "days_on_mls": 24,
        "list_price": 499000,
        "list_date": "2025-01-06",
        "assessed_value": 338631,
        "estimated_value": 517400,
        "tax": 3777,
        "tax_history": [
            {
            "year": 2023,
            "tax": 3777,
            "assessment": {
                "building": 198254,
                "land": 140377,
                "total": 338631
            }
            },
            {
            "year": 2022,
            "tax": 3717,
            "assessment": {
                "building": 194367,
                "land": 137625,
                "total": 331992
            }
            },
            {
            "year": 2021,
            "tax": 3647,
            "assessment": {
                "building": 190556,
                "land": 134927,
                "total": 325483
            }
            },
            {
            "year": 2020,
            "tax": 3636,
            "assessment": {
                "building": 188603,
                "land": 133544,
                "total": 322147
            }
            },
            {
            "year": 2019,
            "tax": 3571,
            "assessment": {
                "building": 184905,
                "land": 130926,
                "total": 315831
            }
            },
            {
            "year": 2018,
            "tax": 3505,
            "assessment": {
                "building": 181280,
                "land": 128359,
                "total": 309639
            }
            },
            {
            "year": 2017,
            "tax": 3434,
            "assessment": {
                "building": 177726,
                "land": 125843,
                "total": 303569
            }
            },
            {
            "year": 2016,
            "tax": 3134,
            "assessment": {
                "building": 174242,
                "land": 123376,
                "total": 297618
            }
            },
            {
            "year": 2015,
            "tax": 3134,
            "assessment": {
                "building": 171625,
                "land": 121523,
                "total": 293148
            }
            },
            {
            "year": 2014,
            "tax": 3059,
            "assessment": {
                "building": 168264,
                "land": 119143,
                "total": 287407
            }
            },
            {
            "year": 2013,
            "tax": 3103,
            "assessment": {
                "building": 167504,
                "land": 118605,
                "total": 286109
            }
            },
            {
            "year": 2012,
            "tax": 2922,
            "assessment": {
                "building": 164220,
                "land": 116280,
                "total": 280500
            }
            },
            {
            "year": 2010,
            "tax": 529,
            "assessment": {
                "building": 45913,
                "land": 11473,
                "total": 57386
            }
            },
            {
            "year": 2009,
            "tax": 538,
            "assessment": {
                "building": 45570,
                "land": 11388,
                "total": 56958
            }
            },
            {
            "year": 2008,
            "tax": 518,
            "assessment": {
                "building": 44784,
                "land": 11193,
                "total": 55977
            }
            },
            {
            "year": 2007,
            "tax": 503,
            "assessment": {
                "building": 43906,
                "land": 10974,
                "total": 54880
            }
            }
        ],
        "lot_sqft": 7405,
        "price_per_sqft": 252,
        "latitude": 39.751725,
        "longitude": -121.80663,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/708c7dec148689b98c43e9bb1eb9dc17l-m1893145572od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3214
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/512-Centennial-Ave_Chico_CA_95928_M12112-79832",
        "property_id": "1211279832",
        "listing_id": "2976811570",
        "mls": "MRCA",
        "mls_id": "SN25000391",
        "status": "FOR_SALE",
        "text": "Discover a RARE GEM! 8 sprawling acres right next to Bidwell Park! This extraordinary property is a canvas of possibilities. Imagine crafting your own private estate with nature as your neighbor or exploring the potential for future development in a location that simply doesn't come along often. Opportunities like this are as rare as they are exciting and this one is ready to inspire your next big vision. Don't miss your chance to stake your claim next to one of Chico's most beloved landmarks!",
        "style": "LAND",
        "full_street_line": "512 Centennial Ave",
        "street": "512 Centennial Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 0,
        "full_baths": 0,
        "half_baths": 0,
        "sqft": 0,
        "year_built": 0,
        "days_on_mls": 28,
        "list_price": 1500000,
        "list_date": "2025-01-02",
        "assessed_value": 188458,
        "estimated_value": 542500,
        "tax": 2138,
        "tax_history": [
            {
            "year": 2023,
            "tax": 2138,
            "assessment": {
                "building": 50643,
                "land": 137815,
                "total": 188458
            }
            },
            {
            "year": 2022,
            "tax": 2089,
            "assessment": {
                "building": 49650,
                "land": 135113,
                "total": 184763
            }
            },
            {
            "year": 2021,
            "tax": 2050,
            "assessment": {
                "building": 48677,
                "land": 132464,
                "total": 181141
            }
            },
            {
            "year": 2020,
            "tax": 2044,
            "assessment": {
                "building": 48178,
                "land": 131106,
                "total": 179284
            }
            },
            {
            "year": 2019,
            "tax": 2008,
            "assessment": {
                "building": 47234,
                "land": 128536,
                "total": 175770
            }
            },
            {
            "year": 2018,
            "tax": 1971,
            "assessment": {
                "building": 46308,
                "land": 126016,
                "total": 172324
            }
            },
            {
            "year": 2017,
            "tax": 1930,
            "assessment": {
                "building": 45400,
                "land": 123546,
                "total": 168946
            }
            },
            {
            "year": 2016,
            "tax": 1763,
            "assessment": {
                "building": 44510,
                "land": 121124,
                "total": 165634
            }
            },
            {
            "year": 2015,
            "tax": 1763,
            "assessment": {
                "building": 43842,
                "land": 119305,
                "total": 163147
            }
            },
            {
            "year": 2014,
            "tax": 1734,
            "assessment": {
                "building": 42984,
                "land": 116968,
                "total": 159952
            }
            },
            {
            "year": 2013,
            "tax": 1744,
            "assessment": {
                "building": 42790,
                "land": 116440,
                "total": 159230
            }
            },
            {
            "year": 2012,
            "tax": 1644,
            "assessment": {
                "building": 41951,
                "land": 114157,
                "total": 156108
            }
            },
            {
            "year": 2010,
            "tax": 1626,
            "assessment": {
                "building": 41129,
                "land": 111919,
                "total": 153048
            }
            },
            {
            "year": 2009,
            "tax": 1654,
            "assessment": {
                "building": 40822,
                "land": 111083,
                "total": 151905
            }
            },
            {
            "year": 2008,
            "tax": 1598,
            "assessment": {
                "building": 40117,
                "land": 109164,
                "total": 149281
            }
            },
            {
            "year": 2007,
            "tax": 1555,
            "assessment": {
                "building": 39331,
                "land": 107024,
                "total": 146355
            }
            }
        ],
        "lot_sqft": 351529,
        "price_per_sqft": 0,
        "latitude": 39.764293,
        "longitude": -121.786693,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/38c526c2de1e9db2f7ef879667c05377l-b281915281od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4426
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/3720-Rodgers-Ave_Chico_CA_95928_M18163-66941",
        "property_id": "1816366941",
        "listing_id": "2976785855",
        "mls": "MRCA",
        "mls_id": "SN24247049",
        "status": "PENDING",
        "text": "Are you looking for a peaceful, quiet countryside home with plenty of space to have a pool, shop, large garden, or additional ADU (Accessory Dwelling Unit)??? YOU HAVE FOUND IT! Only a few minutes from the heart of downtown Chico too!! Agricultural interface with zero wildfire potential. Already has many fruit trees like Kumquat, Mandarin, Persimmon & Nectarine on this .67 Acre property! This beautiful 3 bedroom/ 2 bath, 1816 square foot home has been lovingly painted inside & out, you will love the newer flooring and upgraded lighting! You will find that the home has a great layout when you walk into the entryway looking into the kitchen, dining area & huge family room. Family room is warm and cozy with its large wood burning fireplace and has two sliding glass doors that bring the outside in! Family room also has access to a large, covered patio outside that invites many enjoyed hours of outdoor living space! Sparkling kitchen is close by with plenty of counter space, breakfast bar, refrigerator, and ready for new memories of holiday baking!! Separate laundry room is just off the kitchen. Did I mention the large bonus room yet??? Wonderful room that was previously used as a den but could be anything your heart desires. Bonus room has a beautiful, curved brick wood burning fireplace and picture window with a view of the front yard also! The 3 bedrooms are nestled together on the right side of the home. The primary bedroom suite is spacious, and bathroom was upgraded with a walk-in tub. There are gorgeous shade trees on the property and there is an additional outbuilding in the backyard. Plus, on the left side of the home is a gravel driveway with gate that gives privacy, but you can easily drive all the way to the back of the property too! This location has the richest loam soil to help make your garden be exceptional! It's a tranquil drive as you pass many trees & orchards to reach this destination! This type of home does not come on the market often...so give your realtor a call and schedule a showing!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "3720 Rodgers Ave",
        "street": "3720 Rodgers Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 3,
        "full_baths": 1,
        "half_baths": 1,
        "sqft": 1816,
        "year_built": 1974,
        "days_on_mls": 28,
        "list_price": 579500,
        "list_date": "2025-01-02",
        "assessed_value": 253225,
        "estimated_value": 544900,
        "tax": 2849,
        "tax_history": [
            {
            "year": 2023,
            "tax": 2849,
            "assessment": {
                "building": 142757,
                "land": 110468,
                "total": 253225
            }
            },
            {
            "year": 2022,
            "tax": 2803,
            "assessment": {
                "building": 139958,
                "land": 108302,
                "total": 248260
            }
            },
            {
            "year": 2021,
            "tax": 2748,
            "assessment": {
                "building": 137214,
                "land": 106179,
                "total": 243393
            }
            },
            {
            "year": 2020,
            "tax": 2742,
            "assessment": {
                "building": 135808,
                "land": 105091,
                "total": 240899
            }
            },
            {
            "year": 2019,
            "tax": 2693,
            "assessment": {
                "building": 133146,
                "land": 103031,
                "total": 236177
            }
            },
            {
            "year": 2018,
            "tax": 2640,
            "assessment": {
                "building": 130536,
                "land": 101011,
                "total": 231547
            }
            },
            {
            "year": 2017,
            "tax": 2588,
            "assessment": {
                "building": 127977,
                "land": 99031,
                "total": 227008
            }
            },
            {
            "year": 2016,
            "tax": 2365,
            "assessment": {
                "building": 125468,
                "land": 97090,
                "total": 222558
            }
            },
            {
            "year": 2015,
            "tax": 2364,
            "assessment": {
                "building": 123584,
                "land": 95632,
                "total": 219216
            }
            },
            {
            "year": 2014,
            "tax": 2311,
            "assessment": {
                "building": 121164,
                "land": 93759,
                "total": 214923
            }
            },
            {
            "year": 2013,
            "tax": 2342,
            "assessment": {
                "building": 120617,
                "land": 93336,
                "total": 213953
            }
            },
            {
            "year": 2012,
            "tax": 2202,
            "assessment": {
                "building": 118252,
                "land": 91506,
                "total": 209758
            }
            },
            {
            "year": 2010,
            "tax": 2174,
            "assessment": {
                "building": 115934,
                "land": 89712,
                "total": 205646
            }
            },
            {
            "year": 2009,
            "tax": 2212,
            "assessment": {
                "building": 115068,
                "land": 89042,
                "total": 204110
            }
            },
            {
            "year": 2008,
            "tax": 2142,
            "assessment": {
                "building": 113081,
                "land": 87504,
                "total": 200585
            }
            },
            {
            "year": 2007,
            "tax": 2078,
            "assessment": {
                "building": 110864,
                "land": 85789,
                "total": 196653
            }
            }
        ],
        "lot_sqft": 29185,
        "price_per_sqft": 319,
        "latitude": 39.693229,
        "longitude": -121.865448,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/f77dfed4d4dc377a4e95020f4940243al-b3020051652od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1211
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/3549-Cisco-Way_Chico_CA_95973_M90302-16691",
        "property_id": "9030216691",
        "listing_id": "2976763409",
        "mls": "MRCA",
        "mls_id": "SN24254522",
        "status": "FOR_SALE",
        "text": "Beautifully remodeled This charming, manufactured home a peaceful family mobile home community. This home features spacious living areas, a modern kitchen with ample storage, hard surface countertops kitchen, stainless-steel appliances, the carport and new mini splits. Enjoy the convenience of amenities such as pool, club house, shopping, schools, RT, and it is close to both freeways I-5 and CA-99. This home offers comfort and accessibility, making it an ideal choice for a variety of lifestyles.",
        "style": "MOBILE",
        "full_street_line": "3549 Cisco Way",
        "street": "3549 Cisco Way",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 2,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 895,
        "year_built": 1977,
        "days_on_mls": 29,
        "list_price": 85000,
        "list_date": "2025-01-01",
        "assessed_value": 0,
        "estimated_value": 0,
        "tax": 0,
        "tax_history": 0,
        "lot_sqft": 0,
        "price_per_sqft": 95,
        "latitude": 39.778461,
        "longitude": -121.874817,
        "county": "Butte",
        "hoa_fee": 750,
        "nearby_schools": "Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/5a58981ee80e95cf92d1c802c66eacfdl-b927942110od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1161
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/316-W-Sacramento-Ave_Chico_CA_95926_M28701-10103",
        "property_id": "2870110103",
        "listing_id": "2976781795",
        "mls": "MRCA",
        "mls_id": "SN25000256",
        "status": "FOR_SALE",
        "text": "Home is currently under some remodeling! Additional photos to come as updates are made and home is cleaned! Still available to view! Unique, charming, Victorian-style Chico home! Fantastic opportunity to own a piece of some of Chico's original homes or add to your rental portfolio! Across the street from Chico High School and just a short distance from Chico State and downtown Chico as well. Two story house with 3 bedrooms upstairs and 1 bath, master bedroom downstairs with its own bathroom and another 1/2 bath downstairs as well. The home has the original hardwood floors throughout and updated linoleum in the 1/2 bath and kitchen. there is a formal dining room area through the doorway at the base of the staircase entry. The garage unit was converted to a beautiful ADU prior to current owner purchasing the property. There is ample space in the basement for all your storage needs. The back deck was just updated with new redwood and the front door has been replaced! Siding is being replaced this week also to bring a little bit of life back in to this beautiful home. Upstairs bathroom was remodeled within the last 2 years as well! The ADU unit has its own meter for PG & E and is 1 bed, 1 bath with a large living room area and a small kitchen all in about 1100 sq. ft of living space! It has its own alleyway access as well. You don't want to miss out on this fab home!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "316 W Sacramento Ave",
        "street": "316 W Sacramento Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 4,
        "full_baths": 2,
        "half_baths": 1,
        "sqft": 1573,
        "year_built": 1906,
        "days_on_mls": 28,
        "list_price": 600000,
        "list_date": "2025-01-02",
        "assessed_value": 365885,
        "estimated_value": 490000,
        "tax": 4080,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4080,
            "assessment": {
                "building": 220869,
                "land": 145016,
                "total": 365885
            }
            },
            {
            "year": 2022,
            "tax": 4015,
            "assessment": {
                "building": 216539,
                "land": 142173,
                "total": 358712
            }
            },
            {
            "year": 2021,
            "tax": 3939,
            "assessment": {
                "building": 212294,
                "land": 139386,
                "total": 351680
            }
            },
            {
            "year": 2020,
            "tax": 3928,
            "assessment": {
                "building": 210118,
                "land": 137957,
                "total": 348075
            }
            },
            {
            "year": 2019,
            "tax": 3857,
            "assessment": {
                "building": 205999,
                "land": 135252,
                "total": 341251
            }
            },
            {
            "year": 2018,
            "tax": 3787,
            "assessment": {
                "building": 201960,
                "land": 132600,
                "total": 334560
            }
            },
            {
            "year": 2017,
            "tax": 607,
            "assessment": {
                "building": 42991,
                "land": 16967,
                "total": 59958
            }
            },
            {
            "year": 2016,
            "tax": 553,
            "assessment": {
                "building": 42149,
                "land": 16635,
                "total": 58784
            }
            },
            {
            "year": 2015,
            "tax": 552,
            "assessment": {
                "building": 41516,
                "land": 16386,
                "total": 57902
            }
            },
            {
            "year": 2014,
            "tax": 537,
            "assessment": {
                "building": 40703,
                "land": 16066,
                "total": 56769
            }
            },
            {
            "year": 2013,
            "tax": 537,
            "assessment": {
                "building": 40520,
                "land": 15994,
                "total": 56514
            }
            },
            {
            "year": 2012,
            "tax": 504,
            "assessment": {
                "building": 39726,
                "land": 15681,
                "total": 55407
            }
            },
            {
            "year": 2010,
            "tax": 496,
            "assessment": {
                "building": 38948,
                "land": 15374,
                "total": 54322
            }
            },
            {
            "year": 2009,
            "tax": 505,
            "assessment": {
                "building": 38657,
                "land": 15260,
                "total": 53917
            }
            },
            {
            "year": 2008,
            "tax": 487,
            "assessment": {
                "building": 37990,
                "land": 14998,
                "total": 52988
            }
            },
            {
            "year": 2007,
            "tax": 472,
            "assessment": {
                "building": 37246,
                "land": 14704,
                "total": 51950
            }
            }
        ],
        "lot_sqft": 8712,
        "price_per_sqft": 381,
        "latitude": 39.73542,
        "longitude": -121.848824,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/4fef24e9359e46b3cde22f1a17cd60b2l-b291323642od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4384
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/1901-Dayton-Rd-Spc-106_Chico_CA_95928_M23460-22857",
        "property_id": "2346022857",
        "listing_id": "2976742919",
        "mls": "MRCA",
        "mls_id": "SN24232574",
        "status": "FOR_SALE",
        "text": "Truly affordable living! Welcome to the Chico Mobile Country Club community. The property is absolutely loaded with fantastic amenities to ensure comfort and convenience for the occupants. Clubhouse, billiard room, library, pool and hot tub, fitness center, car wash and even a salon!? Conveniently located just minutes from vibrant downtown Chico. This unit enjoys a nice corner lot and covered parking. Call your favorite Realtor today for a private tour!",
        "style": "MOBILE",
        "full_street_line": "1901 Dayton Rd Spc 106",
        "street": "1901 Dayton Rd",
        "unit": "Spc 106",
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 2,
        "full_baths": 1,
        "half_baths": 0,
        "sqft": 800,
        "year_built": 1971,
        "days_on_mls": 30,
        "list_price": 45000,
        "list_date": "2024-12-31",
        "assessed_value": 0,
        "estimated_value": 43630,
        "tax": 314,
        "tax_history": [
            {
            "year": 2023,
            "tax": 314
            },
            {
            "year": 2022,
            "tax": 310
            },
            {
            "year": 2021,
            "tax": 304
            },
            {
            "year": 2020,
            "tax": 303
            },
            {
            "year": 2019,
            "tax": 214
            },
            {
            "year": 2016,
            "tax": 136,
            "assessment": {
                "building": null,
                "land": null,
                "total": 13000
            }
            },
            {
            "year": 2009,
            "tax": 236,
            "assessment": {
                "building": 22000,
                "land": null,
                "total": 22000
            }
            },
            {
            "year": 2008,
            "tax": 232,
            "assessment": {
                "building": 22000,
                "land": null,
                "total": 22000
            }
            },
            {
            "year": 2007,
            "tax": 231,
            "assessment": {
                "building": 22000,
                "land": null,
                "total": 22000
            }
            }
        ],
        "lot_sqft": 0,
        "price_per_sqft": 56,
        "latitude": 39.700922,
        "longitude": -121.847626,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/27721873418b4c99591a3e130b10b0edl-m3187889872od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3990
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/2886-Sweetwater-Fls_Chico_CA_95973_M15245-79225",
        "property_id": "1524579225",
        "listing_id": "2977218569",
        "mls": "MRCA",
        "mls_id": "SN25004373",
        "status": "PENDING",
        "text": "This beautiful home is located in the sought-after Sycamore Creek neighborhood and boasts numerous upgrades, including owned solar panels. The open-concept living and dining areas are highlighted by new luxury vinyl plank flooring, while plush carpeting complements two of the bedrooms. The kitchen features an extra-deep sink and stylish new chandelier in the dining area. Step outside to the low-maintenance yard, featuring fruit trees, raised garden beds, perennial flowers, and ample space for a fire pit, hot tub, or patio seating. The front yard has new lawn. The backyard has raised garden beds and fruit trees. The spacious garage includes custom shelving for optimal storage. Washer/Dryer and Refrigerator remain in the home with the sale. This home offers easy access to Highway 99, schools, East Avenue's commercial corridor, and Upper Bidwell Park. Plus, the charming neighborhood is perfect for celebrating holidays. Call for your tour today!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "2886 Sweetwater Fls",
        "street": "2886 Sweetwater Fls",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95973",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1196,
        "year_built": 2016,
        "days_on_mls": 16,
        "list_price": 449000,
        "list_date": "2025-01-14",
        "assessed_value": 419000,
        "estimated_value": 451687,
        "tax": 4837,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4837,
            "assessment": {
                "building": 229000,
                "land": 190000,
                "total": 419000
            }
            },
            {
            "year": 2022,
            "tax": 3976,
            "assessment": {
                "building": 187635,
                "land": 150107,
                "total": 337742
            }
            },
            {
            "year": 2021,
            "tax": 3808,
            "assessment": {
                "building": 183956,
                "land": 147164,
                "total": 331120
            }
            },
            {
            "year": 2020,
            "tax": 3793,
            "assessment": {
                "building": 182070,
                "land": 145656,
                "total": 327726
            }
            },
            {
            "year": 2019,
            "tax": 3697,
            "assessment": {
                "building": 178500,
                "land": 142800,
                "total": 321300
            }
            },
            {
            "year": 2018,
            "tax": 3214,
            "assessment": {
                "building": 151274,
                "land": 130050,
                "total": 281324
            }
            },
            {
            "year": 2017,
            "tax": 3148,
            "assessment": {
                "building": 148308,
                "land": 127500,
                "total": 275808
            }
            },
            {
            "year": 2016,
            "tax": 1067,
            "assessment": {
                "building": 50000,
                "land": 50762,
                "total": 100762
            }
            },
            {
            "year": 2015,
            "tax": 448,
            "assessment": {
                "building": null,
                "land": 41863,
                "total": 41863
            }
            }
        ],
        "lot_sqft": 4792,
        "price_per_sqft": 375,
        "latitude": 39.770171,
        "longitude": -121.825531,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/0cb084b4a8af0637ed36ce37a47580cbl-m3275162094od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 1784
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/844-Verbena-Ave_Chico_CA_95926_M20783-09251",
        "property_id": "2078309251",
        "listing_id": "2976750486",
        "mls": "MRCA",
        "mls_id": "OR24255687",
        "status": "PENDING",
        "text": "This stunning newer, 2002 built home effortlessly blends contemporary design with the charm of a classic mid-century modern neighborhood. Sunlight streams through extra-tall ceilings, illuminating the open floor plan. Imagine entertaining guests while they marvel at your culinary creations in the spacious kitchen with granite countertops atop the grand bar. Retreat to the luxurious primary suite, where a massive walk-in closet with floor to ceiling built-ins await and a soaking tub invites you to unwind after a long day. Oversize ceramic tile floors grace the main living areas, while warm laminate wood flooring adds a touch of comfort to the bedrooms. Step outside to your own private oasis in the huge backyard. Fruit trees laden with ripe fruit create a picturesque setting. Enjoy the California sunshine in your low-maintenance gardener's paradise. Convenience meets tranquility here! Located in close proximity to In-Motion Fitness and the world-famous Bidwell Park, you'll have easy access to an active lifestyle and endless opportunities for outdoor recreation. Call your agent today for your own private tour.",
        "style": "SINGLE_FAMILY",
        "full_street_line": "844 Verbena Ave",
        "street": "844 Verbena Ave",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95926",
        "beds": 3,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1646,
        "year_built": 2002,
        "days_on_mls": 30,
        "list_price": 499990,
        "list_date": "2024-12-31",
        "assessed_value": 434238,
        "estimated_value": 477000,
        "tax": 4840,
        "tax_history": [
            {
            "year": 2023,
            "tax": 4840,
            "assessment": {
                "building": 273409,
                "land": 160829,
                "total": 434238
            }
            },
            {
            "year": 2022,
            "tax": 4763,
            "assessment": {
                "building": 268049,
                "land": 157676,
                "total": 425725
            }
            },
            {
            "year": 2021,
            "tax": 4673,
            "assessment": {
                "building": 262794,
                "land": 154585,
                "total": 417379
            }
            },
            {
            "year": 2020,
            "tax": 4660,
            "assessment": {
                "building": 260100,
                "land": 153000,
                "total": 413100
            }
            },
            {
            "year": 2019,
            "tax": 4212,
            "assessment": {
                "building": 214887,
                "land": 164844,
                "total": 379731
            }
            },
            {
            "year": 2018,
            "tax": 3600,
            "assessment": {
                "building": 195000,
                "land": 130000,
                "total": 325000
            }
            },
            {
            "year": 2017,
            "tax": 3597,
            "assessment": {
                "building": 200000,
                "land": 125000,
                "total": 325000
            }
            },
            {
            "year": 2016,
            "tax": 3086,
            "assessment": {
                "building": 185000,
                "land": 115000,
                "total": 300000
            }
            },
            {
            "year": 2015,
            "tax": 3133,
            "assessment": {
                "building": 185000,
                "land": 115000,
                "total": 300000
            }
            },
            {
            "year": 2014,
            "tax": 2906,
            "assessment": {
                "building": 165000,
                "land": 115000,
                "total": 280000
            }
            },
            {
            "year": 2013,
            "tax": 2743,
            "assessment": {
                "building": 160000,
                "land": 100000,
                "total": 260000
            }
            },
            {
            "year": 2012,
            "tax": 2740,
            "assessment": {
                "building": 170000,
                "land": 100000,
                "total": 270000
            }
            },
            {
            "year": 2010,
            "tax": 2944,
            "assessment": {
                "building": 175000,
                "land": 110000,
                "total": 285000
            }
            },
            {
            "year": 2009,
            "tax": 3365,
            "assessment": {
                "building": 175000,
                "land": 110000,
                "total": 285000
            }
            },
            {
            "year": 2008,
            "tax": 3510,
            "assessment": {
                "building": 178500,
                "land": 153000,
                "total": 331500
            }
            },
            {
            "year": 2007,
            "tax": 3625,
            "assessment": {
                "building": 205000,
                "land": 140000,
                "total": 345000
            }
            }
        ],
        "lot_sqft": 7841,
        "price_per_sqft": 304,
        "latitude": 39.75163,
        "longitude": -121.818035,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/b2273eb1657d514b81ffc555e9aee2a5l-b2251758658od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 3688
        },
        {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/18-Parkhurst-St_Chico_CA_95928_M27542-87554",
        "property_id": "2754287554",
        "listing_id": "2976817976",
        "mls": "MRCA",
        "mls_id": "SN25001044",
        "status": "PENDING",
        "text": "Your new home awaits at 18 Parkhurst St! This spacious 4-bedroom, 2-bathroom home offers comfortable living spaces and an inviting floor plan. Featuring a 2-car garage, a primary suite, a fireplace, and a spacious front and backyard, this home has the essentials covered. New carpet and interior paint throughout. Conveniently located near the booming Meriam Park community, dog parks, shopping, and dining, this property is a must-see opportunity for both homebuyers and investors alike!",
        "style": "SINGLE_FAMILY",
        "full_street_line": "18 Parkhurst St",
        "street": "18 Parkhurst St",
        "unit": 0,
        "city": "Chico",
        "state": "CA",
        "zip_code": "95928",
        "beds": 4,
        "full_baths": 2,
        "half_baths": 0,
        "sqft": 1670,
        "year_built": 1978,
        "days_on_mls": 27,
        "list_price": 405000,
        "list_date": "2025-01-03",
        "assessed_value": 115433,
        "estimated_value": 406527,
        "tax": 1319,
        "tax_history": [
            {
            "year": 2023,
            "tax": 1319,
            "assessment": {
                "building": 97682,
                "land": 17751,
                "total": 115433
            }
            },
            {
            "year": 2022,
            "tax": 1300,
            "assessment": {
                "building": 95767,
                "land": 17403,
                "total": 113170
            }
            },
            {
            "year": 2021,
            "tax": 1272,
            "assessment": {
                "building": 93890,
                "land": 17062,
                "total": 110952
            }
            },
            {
            "year": 2020,
            "tax": 1271,
            "assessment": {
                "building": 92928,
                "land": 16888,
                "total": 109816
            }
            },
            {
            "year": 2019,
            "tax": 1251,
            "assessment": {
                "building": 91106,
                "land": 16557,
                "total": 107663
            }
            },
            {
            "year": 2018,
            "tax": 1227,
            "assessment": {
                "building": 89320,
                "land": 16233,
                "total": 105553
            }
            },
            {
            "year": 2017,
            "tax": 1199,
            "assessment": {
                "building": 87569,
                "land": 15915,
                "total": 103484
            }
            },
            {
            "year": 2016,
            "tax": 1097,
            "assessment": {
                "building": 85852,
                "land": 15603,
                "total": 101455
            }
            },
            {
            "year": 2015,
            "tax": 1096,
            "assessment": {
                "building": 84563,
                "land": 15369,
                "total": 99932
            }
            },
            {
            "year": 2014,
            "tax": 1075,
            "assessment": {
                "building": 82907,
                "land": 15068,
                "total": 97975
            }
            },
            {
            "year": 2013,
            "tax": 1086,
            "assessment": {
                "building": 82533,
                "land": 15000,
                "total": 97533
            }
            },
            {
            "year": 2012,
            "tax": 1015,
            "assessment": {
                "building": 80915,
                "land": 14706,
                "total": 95621
            }
            },
            {
            "year": 2010,
            "tax": 998,
            "assessment": {
                "building": 79329,
                "land": 14418,
                "total": 93747
            }
            },
            {
            "year": 2009,
            "tax": 1016,
            "assessment": {
                "building": 78737,
                "land": 14311,
                "total": 93048
            }
            },
            {
            "year": 2008,
            "tax": 993,
            "assessment": {
                "building": 77378,
                "land": 14064,
                "total": 91442
            }
            },
            {
            "year": 2007,
            "tax": 953,
            "assessment": {
                "building": 75861,
                "land": 13789,
                "total": 89650
            }
            }
        ],
        "lot_sqft": 7841,
        "price_per_sqft": 243,
        "latitude": 39.726147,
        "longitude": -121.794033,
        "county": "Butte",
        "hoa_fee": 0,
        "nearby_schools": "Butte County Office Of Education School District, Butte County Rop School District, Chico Unified School District",
        "primary_photo": "http://ap.rdcpix.com/c9b53160d87c1a9b4ab6eff602174158l-m2003373554od-w480_h360_x2.webp?w=1080&q=75",
        "rent": 4178
        }
    ]
    }

    '''

    return json.loads(json_text)

