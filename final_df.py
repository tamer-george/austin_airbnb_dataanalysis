import numpy as np
import pandas as pd
import pyvis as eda
import calendar
import seaborn as sns
import matplotlib.pyplot as plt
import descriptive.pyeda as dp

import warnings

warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", None)

# Reading Data Sets

df = pd.read_csv("final_austin_airbnb_dataset.csv")

# Cleaning Data

df.drop(['Smoke alarm', 'Kitchen', 'Wifi', 'Hangers', 'Hair dryer'], axis=1, inplace=True)

df["host_since"] = pd.to_datetime(df["host_since"], infer_datetime_format=True)


# Apply the function to the 'amenities' column and create a new column 'num_amenities'
df['num_amenities'] = df['amenities_x'].apply(eda.count_amenities)
# print(df.shape)
# print(df.columns)


# month = 5
year_to_filter = 2023
property_types_austin = ["House", "Apartment"]
neighbourhood = ["East Austin", "South Central", "Downtown", "Central Austin"]
price = 500
num_amenities = 20
property_type = ["House"]


austin_positive_score_df = df.loc[
                                  (df["compound_sentiment"] > 0.05) &
                                  # (df["host_since"].dt.month == month) &
                                  # (df["host_since"].dt.year != year_to_filter)
                                  (df["neighbourhood_cleansed"].isin(neighbourhood)) &
                                  (df["property_type"].isin(property_types_austin)) &
                                  # (df["num_amenities"] <= num_amenities) &
                                  # (df["property_type"].isin(property_type)) &
                                  (df["price"] < price)
                                  ]

# print(austin_positive_score_df.head())

# print(austin_positive_score_df.listing_id.nunique())
#  Oversight

# print(df.listing_id.nunique())
# oversight_one = df.groupby(["neighbourhood_cleansed", 'host_neighbourhood'])['host_since'].min().sort_values(ascending=True)
# oversight_two = austin_positive_score_df.groupby(['host_neighbourhood', "neighbourhood_cleansed",
#                                                   "host_since"])['price'].mean().sort_values(ascending=False)
# print(oversight_one)
# print(oversight_two)


# nbr_of_reviews = austin_df.groupby("neighbourhood_cleansed")["number_of_reviews"].mean().sort_values(ascending=False)
#
# print(f"nbr_of_reviews")



# s_title = "Which area is the most expensive in Austin?"
# s_subtitle = "Showing price range by area"
# eda.visualize_countplot(austin_positive_score_df, "neighbourhood_cleansed",
#                             'price_range', title=s_title, subtitle=s_subtitle)


# northwest = austin_positive_score_df.groupby("neighbourhood_cleansed")["price"].mean().sort_values(ascending=False)
# print(northwest)

# t_title = "Which types of properties are there in Austin?"
# t_subtitle = "Showing count of property Type by area"
# eda.visualize_countplot(austin_positive_score_df, "neighbourhood_cleansed",
#                         "property_type", t_title, t_subtitle)

# t_title = " Which property is the most expensive in Austin?"
# t_subtitle = "Showing average nightly price by property type"
# eda.vis_top_highest_average(austin_positive_score_df, "property_type",
#                             "price", [1046.42, 431.50, 398.28],
#                             "property_expensive.png",
#                              title =t_title,
#                              subtitle =t_subtitle)


#           Demand and Price Analysis

# Group data by month and count new listings and hosts

# l_title = "Seasonality in avg nightly price by House / Apartment"
# l_subtitle = ""
# eda.visualize_time_relationship(austin_positive_score_df, "host_since", "price",
#                                 filter_by="month",
#                                 image_name="monthly_trend.png",
#                                 title=l_title, subtitle=l_subtitle)



# b_title = "is it more expensive to travel on weekends?"
# b_subtitle = "Showing avg. nightly price for all types of property type"
# eda.visualize_boxplot(austin_positive_score_df,
#                       "boxplot.png",
#                       b_title, b_subtitle)


# b_title = "Is it expensive to book a house on weekends?"
# b_subtitle = "Showing avg. nightly price vs House property"
# eda.visualize_boxplot(austin_positive_score_df, "boxplot_house.png", b_title, b_subtitle)


#   Textual Data Mining

# a_title = "Top 10 unique ameinities by House/ Apartment?"
# a_subtitle = " showing top 10 ameinities with average price"
# eda.plt_top_10_rated_amenities(austin_positive_score_df,
#                                image_name="top_10_ameinities.png",
#                                title=a_title, subtitle=a_subtitle)

# a_title = "what are the top 10 unique ameinities with price > 1000$?"
# a_subtitle = " showing top 10 ameinities with higher price"
# eda.plt_top_10_rated_amenities(austin_positive_score_df,
#                                image_name="top_10_ameinities_housing.png",
#                                title=a_title, subtitle=a_subtitle)



# s_title = "Which area is the most expensive in Austin?"
# s_subtitle = "Showing price range by neighbourhood area"
# eda.visualize_advanced_bar_plot(austin_positive_score_df, "neighbourhood_cleansed", "price",
#                             'price_range',
#                             image_name="expensive_area.png",
#                             title=s_title, subtitle=s_subtitle)




# select_columns = ["price", "num_amenities"]
# austin_positive_score_df = austin_positive_score_df[select_columns]
# eda.vis_heatmap(austin_positive_score_df, "heat_map.png")


# s_title = "       Which area is the best in Austin?"
# s_subtitle = "Showing best neighbourhood by the highest average review scores location"
# eda.vis_top_highest_average(austin_positive_score_df, "neighbourhood_cleansed",
#                             "review_scores_location",
#                             [4.90],
#                             image_name="Best_area.png",
#                             title=s_title, subtitle=s_subtitle)


# Pie Chart Group data by 'Property_Type' and 'Neighborhood'

# grouped = austin_positive_score_df.groupby(['property_type',
#                                             'neighbourhood_cleansed']).size().reset_index(name="Total")
# grand_total = grouped["Total"].sum()
# print(grand_total)



#  PIE CHART

# eda.vis_pie_chart(austin_positive_score_df)


# NUMBER OF LISTINGS

# eda.yearly_listing(austin_positive_score_df, image_name="unique_listing.png")
