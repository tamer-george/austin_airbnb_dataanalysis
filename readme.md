![cover_project](images/header.png)

---

### Following are the roadmap that we aim to answer through our analysis:

1. Background What is Austin

         a. Who are the people who travel to Austin? why?
         b. What people are looking for in Austin?
         c. Outliers - Special cases of why people come to Austin


2. How do the ratings of listings vary by:

         a. Property type
            i. Ratio of property_type to count_of_review per room+property type
         b. Find areas with high number reviews relative to number of properties with sentiment
            i.  Find what amenities are required
            ii. What property types are relevant to these areas



        
3. Find what populations rent in each area and what type of property they rent
      
         a. If clear division in target population when grouping by location and property:
            i.   What amenities do these populations require/want
                 count _of_amenities/count_of_properties_in_group
            ii.  What is important for them in the Reviews (positive and negative)
            iii. occupants/capacity (use as a hint to target population: 2 =
                 students/business, >4 = families, 12+ families or friends)
            iv.  What do they mention in reviews? 

4. Trends of people entering Airbnb market and leaving Airbnb market in areas of interest
found in previous steps

         a. Using first and last reviews as an instrument for entering and exiting
         i. By area and property type
         ii. Look at what factors exiting properties have in common
         iii. Look at what factors entering properties have in common

5. Availability and price, seasonality of property, term of rental

_______
  
### A quick glance at the data shows that there are:

* 10150 number of listing in Austin with positive score > 0.05. The first rental in Texas was up in 
March 2008 in McKinney. 

* Over 545633 reviews have been written by guests. 
* The average price for listing ranges from $10 per night to $10000 per night. Listing with 
$10000 price tag are in Windsor Park, Northeast Austin.

### Analysis of Data Quality 
1. Price : The price column contained data in string format with the currency 
symbol "$" and comma separator attached to it.
2. Date: We transformed the host_since and date columns to datetime format.
3. Dealing with missing values : The data also had null values to preserve all the information, 
we imputed or dropped the rows containing null values. 
4. Imputed : we fixed some wrong entry in the host_neighbourhood column,
   moreover, we segment the property type, the zipcode and the price columns. 

         

____


# Exploratory Data Analysis 

We will detail our analysis to answer the questions of interest through exploratory data analysis
and visualization. we will use :
  * Hypothesis Testing 
  * Sentiment Analysis
  * Spatial Data Analysis
  * Demand and price analysis
  * Textual data mining
  * Other interesting insights
  
____

# Hypothesis Testing 

      Test one: 
      If there is a significant difference in the avg nightly price between 
      properties located in downtown and those in East Austin? 
      
      Our Case:
            H0 : avg nightly price DT =(Significant) avg nightly price ET 
        
            Ha : avg nightly price DT !=(Not Significant) avg nightly price ET 
      
                  
      we performed the T-test and the result of the p-value: 
      P-Value = 8.85715622564
      α = 0.05
      
      Test:
      if p-value <= a ---> reject H0
      if p-value > a  ---> dont reject H0
      
      result of the test: 
      p-value is greater than alpha(0.05) we fail to reject the null hypothesis,  suggesting there is
      significant difference in avergae nightly price between DT and ET. 

---

      Test Two:      
      Is there a relationship between special amenities and property types in an Airbnb dataset?
            
            Our Case:
            H0 : property type  =(Significant) aminities 
        
            Ha : property type !=(No Significant) aminities
      
            
      Test:
      if p-value <= a ---> reject H0
      if p-value > a  ---> dont reject H0
      
      We Perform the Chi-Squared Test
      P-Value = 0.0
      α = 0.05

      result of the test: 
      p-value is less than alpha(0.05) we dont reject the null hypothesis,
      suggesting there is significant difference.

_______


## Spatial Data Analysis

This section will explore various variables from our dataset to answer questions relating 
to prices property types and  locations in Austin, in addition to prove 
our hypothesis test.

![number_of_listing](images/how_many_listing.png)

--------------
![number_of_listing](images/Best_area.png)


--------------

![Best_area](images/new_expensive_area.png)


      The graph follows our previous location ratings by neighbourhood. Now its obvious that the highly rated location
      would also tend to be costly. 
      
-------------
![number_of_listing](images/property_type_by_area.png)

-------------

![Best_area](images/property_expensive.png)

      
------------


# Demand and Price Analysis 
         

------------
![price](images/monthly_trend.png)

------------

![price](images/trend_booking.png)

-----------
![price](images/boxplot.png)
![price](images/boxplot_house.png)


      As we can see , Friday and Saturday are more expensive compared to 
      the other days of the week,
      perhaps due to higher demand for lodging.
______

# Textual Data Mining 
______
![price](images/top_10_ameinities.png)
______
![price](images/top_10_ameinities_housing.png)
______

## Top 10 most frequent words 
![price](images/postive_words.png)
![price](images/top_10_words.png)
![price](images/negative_words.png)

______

## Other interesting insights

![price](images/linear_regression.png)

______

## Executive Summary: Airbnb Data Analysis

Key Findings:*

1. *High Demand Periods*: Our analysis revealed that the months of Feb to April experienced the highest demand, 
    with a noticeable peak in March. 

2. *Pricing Trends*: We observed that pricing varies significantly by neighborhood,
with East Austin listings commanding the highest nightly rates. 
Seasonal patterns also influence pricing, with rates inclement during peak tourist seasons.

3. *Guest Preferences*: Guests predominantly book entire homes or apartments, 
and the most frequently cited reasons for travel were vacations and leisure trips.
This suggests an opportunity to tailor listings and amenities to these preferences.


*Amenities and Reviews:*
4. *Amenities Analysis*: Amenities such as Kitchen, smoked alarm, essentials, hairdryer and Wi-Fi were highly prevalent. 
listings offering unique features like fire extinguisher and hangers 
stood out and often commanded higher prices.

5. *Review Sentiments*: Sentiment analysis of guest reviews indicated that location, comfortable, and neighborhood 
were critical factors influencing overall guest satisfaction. 
Listings with consistently positive reviews tended to perform well.

*Recommendations:*

6. *Pricing Strategy*: Hosts should consider dynamic pricing strategies to 
maximize revenue during peak demand periods while remaining competitive during off-peak times.

7. *Amenity Enhancements*: Hosts can invest in standout amenities that align with guest preferences
to increase listing desirability.

8. *Superhost Status*: Aspiring hosts should aim to meet the criteria for
Superhost status, as it positively impacts bookings and reputation.


 [Austin Airbnb DashBoard](https:www.google.com)
