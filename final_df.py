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

df = pd.read_csv("final_austin_airbnb_dataset.csv")
df.drop(['Smoke alarm', 'Kitchen', 'Wifi', 'Hangers', 'Hair dryer'], axis=1, inplace=True)

df["host_since"] = pd.to_datetime(df["host_since"], infer_datetime_format=True)


# Convert the date columns to datetime objects
df['first_review'] = pd.to_datetime(df['first_review'])
df['last_review'] = pd.to_datetime(df['last_review'])

# Calculate the duration between the first and last review for each listing
df['booking_duration'] = (df['last_review'] - df['first_review']).dt.days




# Apply the function to the 'amenities' column and create a new column 'num_amenities'
df['num_amenities'] = df['amenities_x'].apply(eda.count_amenities)




"""
print(df.columns)
[['listing_id', 'host_since', 'host_neighbourhood',
       'host_total_listings_count', 'neighbourhood_cleansed', 'first_review',
       'last_review', 'reviews_per_month', 'number_of_reviews',
       'review_scores_rating', 'availability_365', 'room_type', 'amenities_x',
       'property_type', 'date', 'available', 'price', 'compound_sentiment',
       'price_range', 'booking_duration', 'num_amenities'],
       
"""

# month = 5
year_to_filter = 2023
property_types_austin = ["House", "Apartment", "Guest suite", "Bungalow", "TownHouse"]
neighbourhood = ["East Austin", "South Central", "Downtown", "Central Austin"]
price = 610
num_amenities = 20
property_type = ["House"]


austin_positive_score_df = df.loc[(df["compound_sentiment"] >= 0.05) &
                                  # (df["host_since"].dt.month == month) &
                                  (df["host_since"].dt.year != year_to_filter) &
                                  (df["neighbourhood_cleansed"].isin(neighbourhood)) &
                                  (df["property_type"].isin(property_types_austin)) &
                                  # (df["num_amenities"] <= num_amenities) &
                                  # (df["property_type"].isin(property_type)) &
                                  (df["price"] > price)
                                  ]
# print(austin_positive_score_df.listing_id.nunique())
#  Oversight

# print(df.listing_id.nunique())
oversight_one = df.groupby(["neighbourhood_cleansed", 'host_neighbourhood'])['host_since'].min().sort_values(ascending=True)
oversight_two = austin_positive_score_df.groupby(['host_neighbourhood', "neighbourhood_cleansed",
                                                  "host_since"])['price'].mean().sort_values(ascending=False)
# print(oversight_one)
# print(oversight_two)


# nbr_of_reviews = austin_df.groupby("neighbourhood_cleansed")["number_of_reviews"].mean().sort_values(ascending=False)
#
# print(f"nbr_of_reviews")


# f_title = "How many airbnb hosts are there in Austin?"
# f_subtitle = "Showing number of unique listing per top 5 zipcode boundary from 2018 - 2022"
#
# eda.vis_top_ten_values(austin_positive_score_df,"neighbourhood_cleansed", "listing_id",
#                        [1704, 1616, 1544], title=f_title, subtitle=f_subtitle)
# print(nbr_of_listing)

# price_range = pd.crosstab(index=austin_positive_score_df["neighbourhood_cleansed"],
#                           columns=austin_positive_score_df['price_range'])
# top_5 = price_range.stack().reset_index(name="Count").nlargest(20, "Count")
# print(top_5)


# s_title = "Which area is expensive in Austin?"
# s_subtitle = "Showing price range by area"
# eda.visualize_countplot(austin_positive_score_df, "neighbourhood_cleansed",
#                             'price_range', title=s_title, subtitle=s_subtitle)


# northwest = austin_positive_score_df.groupby("neighbourhood_cleansed")["price"].mean().sort_values(ascending=False)
# print(northwest)

# t_title = "Which types of properties are there in Austin?"
# t_subtitle = "Showing count of property Type by area"
# eda.visualize_countplot(austin_positive_score_df, "neighbourhood_cleansed",
#                         "property_type", t_title, t_subtitle)

# t_title = "Which property is expensive?"
# t_subtitle = "Showing average price by property type"
# eda.vis_top_highest_average(austin_positive_score_df, "property_type",
#                             "price", [403.08, 219.25, 111.31], title=t_title,
#                             subtitle=t_subtitle)



# dp.visualize_distribution_of_numeric_col(austin_positive_score_df, "booking_duration", bins=8)
# l_title = "Seasonality in price"
# l_subtitle = "Average Listing price across Months (2018)"
# eda.visualize_time_relationship(best_location, "host_since", "price",
#                                 "month", title=l_title, subtitle=l_subtitle)


#         Best Location Down Town
# year_to_filter = 2022
# month = 5
# best_location = austin_positive_score_df.loc[(austin_positive_score_df["neighbourhood_cleansed"] == "Downtown")
#                                              & (austin_positive_score_df["price"] <= 350) &
#                                                # (austin_positive_score_df["property_type"] == "Apartment") &
#                                              (austin_positive_score_df["host_since"].dt.month == month)&
#                                              (austin_positive_score_df["host_since"].dt.year == year_to_filter)]

# nbr_of_avg_listing = best_location.groupby("neighbourhood_cleansed")["listing_id"].nunique().sort_values(ascending=False)
# print(nbr_of_avg_listing)
# dp.visualize_distribution_of_numeric_col(best_location, "price", bins=5)


#           Demand and Price Analysis

# Group data by month and count new listings and hosts

# l_title = "When there is typically high demand for airbnb listings in Austin?"
# l_subtitle = " showing Average price per listing across Months"
# eda.visualize_time_relationship(austin_positive_score_df, "host_since", "price",
#                                 "month", title=l_title, subtitle=l_subtitle)


# l_title = "what are the booking trends for Airbnb listings in Austin"
# l_subtitle = "Showing the time gap between the first and last review per day"
# eda.visualize_time_relationship(austin_positive_score_df, "host_since", "booking_duration",
#                                 "day", title=l_title, subtitle=l_subtitle)


# l_title = "Seasonality in demand"
# l_subtitle = "Number of reviews across months in 2017"
# eda.visualize_time_relationship(best_location, "host_since", "number_of_reviews",
#                                 "month", title=l_title, subtitle=l_subtitle)



# b_title = "is it expensive to travel on weekends?"
# b_subtitle = "Showing Avg price vs. house property type"
# eda.visualize_boxplot(austin_positive_score_df, b_title, b_subtitle)

a_title = "what are the top 10 unique ameinities with higher price?"
a_subtitle = " showing top 10 ameinities with higher price"
eda.plt_top_10_expensive_amenities(austin_positive_score_df, title=a_title, subtitle=a_subtitle)

# a_title = "what are the top 10 rated ameinities in Austin?"
# a_subtitle = "  showing top 10 ameinities vs. house property type"
# eda.plt_top_10_expensive_amenities(austin_positive_score_df, title=a_title, subtitle=a_subtitle)

# a_title = "       What property types are there in Austin ?"
# a_subtitle = "showing number of rented property types per neighbourhood for the years 2008 - 2022 "
#
# dp.visualize_advanced_bar_plot(austin_positive_score_df, "property_type", "property_count",
#                                "neighbourhood_cleansed", title=a_title, subtitle=a_subtitle)

# s_title = "        Which area is expensive in Austin?"
# s_subtitle = "Showing price range by area"
# dp.visualize_advanced_bar_plot(austin_positive_score_df, "neighbourhood_cleansed", "price",
#                             'price_range', title=s_title, subtitle=s_subtitle)

# s_title = "        Which area is expensive in Austin?"
# s_subtitle = "Showing price range by area"
# dp.visualize_advanced_bar_plot(austin_positive_score_df, "neighbourhood_cleansed", "review_scores_rating",
#                             'price_range', title=s_title, subtitle=s_subtitle)

# s_title = "         Which area is the best?"
# s_subtitle = "Showing Average location score by area"
# dp.vis_top_highest_average(austin_positive_score_df, "neighbourhood_cleansed",
#                            "review_scores_rating",[4.87, 4.84, 4.83],
#                            title=s_title, subtitle=s_subtitle)


# s_title = "Which property is the most expensive in austin?"
# s_subtitle = "Showing property type by average price"
# dp.visualize_basic_bar_plot(austin_positive_score_df, "price", "property_type", title=s_title,
#                             subtitle=s_subtitle)

# s_title = "Is there a correlation between specific amenities and the nightly price?"
# s_subtitle = "Showing number of amenities vs price"
# dp.visualize_linear_regression(austin_positive_score_df, 'price', 'num_amenities',
#                                title=s_title, subtitle=s_subtitle)