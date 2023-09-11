import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import descriptive.pyeda as dp
import warnings

warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", None)

listings_df = pd.read_csv("listings.csv")
calendar_df = pd.read_csv("calendar.csv")
reviews_df = pd.read_csv("sentimentData.csv")

listings_df = listings_df.rename(columns={"id": "listing_id"})
# print(listings_df.columns)
# print(calendar_df.columns)

merged_data = pd.merge(listings_df, calendar_df, on="listing_id", how="inner")
# print(merged_data.columns)
selected_columns = ['listing_id', 'host_since', 'host_neighbourhood', "review_scores_location", 'host_is_superhost',
                    'neighbourhood_cleansed', 'number_of_reviews', 'review_scores_rating',
                    'room_type', 'amenities', 'property_type', 'date',
                    'available', 'price_y']

merged_data = merged_data[selected_columns]
# listings_df = listings_df.rename(columns={'price_y': "price"})
# print(merged_data.shape)

merged_data = merged_data.dropna(axis=0)
# print(f"Listings null data percentage:\n\n{round(merged_data.isnull().sum() / merged_data.shape[0]*100)}")
# print(merged_data.shape)
# print(reviews_df.columns)

# final_merged_df = pd.merge(merged_data, reviews_df, on="listing_id", how="left")
# print(final_merged_df.shape)

max_sentiment = reviews_df.groupby('listing_id')['compound_sentiment'].max().reset_index()


# Merge the datasets using the common listing ID and maximum average review score
merged_data = pd.merge(merged_data, max_sentiment, on='listing_id', how='left')
# print(merged_data.shape)
# print(f"Listings null data percentage:\n\n{round(merged_data.isnull().sum() / merged_data.shape[0]*100)}")

merged_data = merged_data.rename(columns={'price_y': "price"})
grouped_property_type = {"Entire home": "House", "Entire rental unit": "Apartment",
                         "Private room in home": "Guest suite", "Entire condo": "Apartment",
                         "Entire guesthouse": "House", "Private room in rental unit":  "Guest suite",
                         "Entire townhouse": "TownHouse", "Entire guest suite": "Guest suite",
                         "Entire bungalow": "Bungalow", "Entire serviced apartment": "Apartment",
                         "Tiny home": "House", "Camper/RV": "Camping", "Entire loft": "House",
                         "Private room in condo": "Apartment", "Entire villa": "Villa",
                         "Private room in townhouse": "Guest suite", "Private room in resort": "Guest suite",
                         "Entire cottage": "Cottage", "Room in hotel": "Guest suite",
                         "Shared room in rental unit": "House", "Entire cabin": "Camping",
                         "Private room in guest suite": "Guest suite", "Entire vacation home": "House",
                         "Room in boutique hotel": "Guest suite", "Shared room in home": "House",
                         "Private room in guesthouse": "Guest suite", "Entire place": "House",
                         " Private room in bed and breakfast": "House", "Private room in bungalow": "Guest suite",
                         "Entire home/apt": "Apartment", "Campsite": "Camping", "Private room": "Guest suite",
                         "Room in aparthotel": "House", "Treehouse": "Others", "Boat": "Others", "Bus": "Others",
                         "Farm stay": "TownHouse", "Shared room in cabin": "Others", "Private room in loft": "House",
                         "Shipping container": "Others", "Private room in camper/rv": "Camping",
                         "Shared room in condo": "Apartment", "Private room in tiny home": "House",
                         "Tower": "Others", "Private room in cabin": "Others", "Yurt": "Others",
                         "Room in resort": "Others", "Private room in villa": "Villa", "Houseboat": "Others",
                         "Private room in tent": "Camping", "Private room in serviced apartment": "Apartment",
                         "Shared room": "Others", "Earthen home": "TownHouse", "Shared room in loft": "House",
                         "Shared room in hostel": "Others", "Private room in hostel": "Others", "Tent": "Camping",
                         "Casa particular": "Others", "Barn": "Others", "Ranch": "Others",
                         "Private room in cottage": "House",
                         "Room in bed and breakfast": "Others", "Private room in earthen home": "TownHouse",
                         "Tipi": "Others", "Dome": "Others", "Shared room in guest suite": "Guest suite",
                         "Entire chalet": "TownHouse", "Shared room in camper/rv": "Camping",
                         "Shared room in townhouse": "TownHouse"}

merged_data["property_type"] = merged_data["property_type"].map(grouped_property_type).fillna("Others")
grouped_zip_code = {78701: "Downtown", 78704: "South Central", 78703: "Central Austin", 78705: "Central Austin",
                    78751: "Central Austin", 78756: "Central Austin", 78757: "Central Austin",
                    78702: 'East Austin', 78722: 'East Austin', 78741: "Southeast", 78744: "Southeast",
                    78747: "Southeast", 78745: "South Austin", 78748: "South Austin", 78735: "Southwest Austin",
                    78736: "Southwest Austin", 78738: "Southwest Austin", 78739: "Southwest Austin",
                    78733: "West lake Hills", 78746: "West lake Hills", 78731: "Northwest Austin",
                    78727: "Northwest Austin", 78750: "Northwest Austin", 78759: "Northwest Austin",
                    78721: "Northeast Austin", 78723: "Northeast Austin", 78724: "Northeast Austin",
                    78758: "North Austin", 78734: "North Lake Village", 78752: "St. Johns", 78753: "North Lamar",
                    78737: "Hays County", 78749: "West Austin", 78732: "West Austin", 78728: "Travis County",
                    78754: "Travis County", 78730: "Riverplace", 78717: "Williamson County", 78719: "Southeast",
                    78726: "Travis County", 78742: "Travis County"}

merged_data["neighbourhood_cleansed"] = merged_data["neighbourhood_cleansed"].map(grouped_zip_code).fillna("Suburban")
# print(merged_data.head())
# print(merged_data.shape)
# print(f"Listings null data percentage:\n\n{round(merged_data.isnull().sum() / merged_data.shape[0]*100)}")

#  Extracting top 5 amenities

select_column = ["listing_id", "amenities"]
amenities_df = merged_data[select_column]
amenities_df = pd.DataFrame(amenities_df)
amenities_df['amenities'] = amenities_df['amenities'].str.split(', ')
amenities_df = amenities_df.explode('amenities')
amenity_counts = amenities_df['amenities'].value_counts()
top_5_amenities = amenity_counts.head(5)
top_5_amenities_dict = top_5_amenities.to_dict()

# Merge the top 5 amenities back into the main DataFrame based on 'ListingID'
merged_data = pd.merge(merged_data, amenities_df.groupby('listing_id')['amenities'].apply(list).reset_index(),
                       on='listing_id', how='left')

# Add columns for the top 5 amenities and their counts
for amenity, count in top_5_amenities_dict.items():
    merged_data[amenity] = merged_data['amenities_x'].apply(lambda x: x.count(amenity) if isinstance(x, list) else 0)
#
#

# print(merged_data.shape)
# print(merged_data.head())
columns_to_drop = ["amenities_y"]
merged_data.drop(columns=columns_to_drop, axis=1, inplace=True)
merged_data.rename(columns=lambda x: x.replace('"', ''), inplace=True)

merged_data["price"] = merged_data["price"].str.strip("$")
merged_data["price"] = merged_data["price"].str.replace(",", "")
merged_data["price"] = merged_data["price"].astype("float")

merged_data["listing_id"] = merged_data["listing_id"].astype("int32")

merged_data["host_neighbourhood"] = merged_data["host_neighbourhood"].replace("Downtown Austin", "Downtown")
merged_data["host_neighbourhood"] = merged_data["host_neighbourhood"].replace("MLK & 183", "MLK")
merged_data["host_neighbourhood"] = merged_data["host_neighbourhood"].replace("MLK-183", "MLK")
merged_data["host_neighbourhood"] = merged_data["host_neighbourhood"].replace("Allendale", "Allandale")

bins = [0, 50, 100, 150, 200, 250, 300, 10000]
labels =["0 - 50", "51 - 100", "101 - 150", "151 - 200", "201 - 250", "251 - 300", "300+"]

merged_data["price_range"] = pd.cut(merged_data["price"], bins=bins, labels=labels)


# print(merged_data.info())
dp.save_data_to_csv_file(merged_data, "final_austin_airbnb_dataset.csv")
