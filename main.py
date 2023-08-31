import numpy as np
import pandas as pd
import pyvis as eda
import seaborn as sns
import matplotlib.pyplot as plt
import descriptive.pyeda as dp
import warnings


warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", None)

# Reading Data Sets

listings_df = pd.read_csv("listings.csv")
calendar_df = pd.read_csv("calendar.csv")
reviews_df = pd.read_csv("reviews.csv")
# print(calendar_df.shape)
# print(listings_df.shape)
# print(reviews_df.shape)

# print(listings_df.columns)

#                       Listings DataSet

select_column = ["id", 'host_since', "host_neighbourhood", "review_scores_location", 'latitude', 'longitude',
                 "number_of_reviews",'amenities', 'host_is_superhost', 'property_type', 'room_type',
                 "price"]

lsting_df = listings_df[select_column]
lsting_df = lsting_df.rename(columns={"id": "listing_id"})

#                       Calendar Data Set

select_calender_column = ["listing_id", 'date', "price"]

calenders_df = calendar_df[select_calender_column]
# print(calenders_df.shape)
df = lsting_df.merge(calenders_df, how="left")
# print(df.shape)
# print(f"Listings null data percentage:\n\n{round(df.isnull().sum() / df.shape[0]*100)}")

#                         Data Cleaning


df = df.dropna(axis=0)
# print(df["listing_id"].duplicated().count())
# print(f"Listings null data percentage:\n\n{round(df.isnull().sum() / df.shape[0]*100)}")

df["price"] = df["price"].str.strip("$")
df["price"] = df["price"].str.replace(",", "")
df["price"] = df["price"].astype("float")


df["host_since"] = pd.to_datetime(df["host_since"], infer_datetime_format=True)
df["date"] = pd.to_datetime(df["date"], infer_datetime_format=True)
df["listing_id"] = df["listing_id"].astype("int32")


# nh_group = df.groupby("host_neighbourhood")["listing_id"].count().sort_values(ascending=False)
# print(nh_group.nlargest(50))

#           Subset Data Where price less than 300 and choosing the largest listing neighbourhood

df = df.loc[(df["price"] <= 300)]
# dp.visualize_distribution_of_numeric_col(df, "price", 6)
nh_group = df.groupby("host_neighbourhood")["listing_id"].count().sort_values(ascending=False)
largest_listings = nh_group.to_dict()
largest_listing_neighbourhood = [i for i, k in largest_listings.items() if k >= 5000]

df = df.loc[df["host_neighbourhood"].isin(largest_listing_neighbourhood)]
# print(df.shape)

#                    Property Type Segment

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

df["property_type"] = df["property_type"].map(grouped_property_type)

#           Price segment

bins = [0, 50, 100, 150, 200, 250, 300]
labels =["0 - 50", "51 - 100", "101 - 150", "151 - 200", "201 - 250", "251 - 300"]

df["PriceRange"] = pd.cut(df["price"], bins=bins, labels=labels)

# Imputed host_neighbourhood

df["host_neighbourhood"] = df["host_neighbourhood"].replace("Downtown Austin", "Downtown")
df["host_neighbourhood"] = df["host_neighbourhood"].replace("MLK & 183", "MLK")
df["host_neighbourhood"] = df["host_neighbourhood"].replace("MLK-183", "MLK")
# print(df["host_neighbourhood"].unique())



# print(df["listing_id"].nunique())
# df = df.drop_duplicates(subset="listing_id")
# print(df.shape)
# print(df.describe(include="all"))
# print(f"Listings null data percentage:\n\n{round(df.isnull().sum() / df.shape[0]*100)}")
# print(df.info())
# print(df.shape)
# print(df["price"].min())


#               Saving subset data set

# dp.save_data_to_csv_file(df, "austin_airbnb_data.csv")

#                EDA

# dp.visualize_distribution_of_categorical_col(df, "property_type")

# f_title = "Which area is the best?"
# f_subtitle = "Showing Average Location Score by Neighbourhood"
# eda.vis_top_highest_average(df, ["host_neighbourhood"], "review_scores_location",
#                             [4.99, 4.96, 4.95], f_title, f_subtitle)

# s_title = "Which area is expensive?"
# s_subtitle = "Showing Average price by neighbourhood"
#
# eda.vis_top_highest_average(df, ["host_neighbourhood"], "price",
#                             [245.19, 225.73, 208.25], s_title, s_subtitle)

# f_title = "Which types of properties are there in Austin?"
# f_subtitle = "Showing count of property Type by neighbourhood"
# eda.visualize_countplot(df, "host_neighbourhood", "property_type", title=f_title,
#                         subtitle=f_subtitle)
df2 = df.drop_duplicates(subset="listing_id")

# print(df2.shape)

# eda.visualize_time_relationship(df2, "host_since", "number_of_reviews", "year")

