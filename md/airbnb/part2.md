# Barcelona Airbnb DS analysis (2nd part) 
We are going now to try to understand our data a bit more.
```
\
|--Airbnb_Barcelona.ipynb
|--data
|   |-output.csv
```

## Importing Libraries


```python
#Data
import pandas as pd 

#Graphics libraries
from plotnine import *
import seaborn as sns
import matplotlib.pyplot as plt
```

## Reading the data
At the end of *part1* we finished with cleaned data set **output.csv**, we will continue using this data set, se we will read it, adjust a little bit dropping some garbage columns, and go on.


```python
airbnb_data = pd.read_csv("./data/output.csv")
airbnb_data.drop(['Unnamed: 0','Unnamed: 225'],axis=1,inplace=True)
```

## Data Visualization

We will start trying to find correlations/aggrupations in a visual way, for that we have an excelent tool from seaborn:


```python
sns.pairplot(airbnb_data[[
"bedrooms",
"beds",
"host_is_superhost",
"instant_bookable",
"property_type",
"number_of_reviews",
"host_listings_count",
"minimum_nights",
"review_scores_rating",
"price"
]],hue='property_type')
# Title 
plt.suptitle("Fig 1 - Correlation between principal variables",  y=1.06, size = 24);
```


    
![png](/static/notebooks/airbnb/part2/output_8_0.png)
    


In this type of graphs, we are trying to find some logic that helps us understand how our data is distributed, if there is some correlation, and also if it's obvoius some aggrupation. To follow the discussion, I encourage to see this graphic in a separate window and maximized. <a href="/static/notebooks/airbnb/part2/output_8_0.png" target="_blank">Pairplot Image</a>

We have 2 types of graphics:
- Crossed characteristics: plot graphic with the relation with the 2 variables.
- Diagonal characteristics: As we have the same 2 characteristics, here we found distribution plot of our characteristics.

All of them are colored by property type, as it's clear that is an important aggregation characteristic which I will try to highlight in any graphic so we could analyze all data with this dimension disaggregated.

Some conclusions, from visual interpretation:

- You will have best reviews if you are superhost $^(1)$
- The properties which have more reviews usually have also best scores.
- Score rating doesn't seem clear that impacts over the price, as we have lots of different prices distributed the same way in all the score range.
- We have several 1 bedroom with 1 bed publication.
- It seems in general that people review and rate similar way...

*$(1)$ The "superhost" designation on Airbnb is a sign that an Airbnb host has gotten consistently good reviews over at least a year of hosting. Airbnb checks the status of hosts four times a year to ensure that a superhost badge is still relevant for each host.*

### Review Scores Rating

Let's see one particular distribution, scores rating, you will see in *Fig 2* that we have more or less always 80-100 rating with really few scores under that. It could mean that people that doesn't like some property it's not giving any comment, and who has enjoyed the property usually scores it.

It's not clear how could affect to our predicted price and if there are some other categories most relevant. The relation with score and price exists, because you find more expensive properties when looking for best scores, but there are also inexpensive ones. *Fig 3*


```python
(
    ggplot(airbnb_data, aes(x='review_scores_rating')) +
    geom_density(aes(y='stat(count)'), fill=orange,color='red',alpha=0.3) +
    geom_bar(aes(y='stat(count)'),fill=yellow_orange,alpha=0.2) +
    orange_dark_theme +
    labs(x='Score 0 - 100',y='Number of Publications',title='Fig 2 - Score Review Distribution')
).draw();
```


    
![png](/static/notebooks/airbnb/part2/output_10_0.png)
    



```python
(
    ggplot(airbnb_data[airbnb_data['property_type']=='Private room in apartment'], 
           aes(x='review_scores_rating',y='price')) +
    geom_point(aes(color='price')) +
    scale_color_distiller(palette= 'Oranges') +    
    orange_dark_theme +
    labs(x='Score 0 - 100',y='Price $',title='Fig 3 - Price/Score Distribution')
).draw();
```


    
![png](/static/notebooks/airbnb/part2/output_11_0.png)
    


### Property Type

We are working all the time disaggregating by property_type, this is because from an intuitive point of view, it's clear that room it's not the same as house, so this variable is clear that will be relevant in price determination. We can see which is the price distribution for each property type, to confirm our intuitive interpretation.


```python
sorted_by_price = airbnb_data.groupby(by='property_type')['price'].median().sort_values(ascending=False).index
```


```python
(
    ggplot(airbnb_data,aes(x='property_type',y='price',fill='property_type',group='property_type')) +
    scale_x_discrete(limits=sorted_by_price) +
    geom_boxplot(color=light_orange,show_legend=False) +
    labs(x='',y='Price $',title='Fig 4 - Price distribution aggregated by Property Type') +
    orange_dark_theme +
    theme(
        axis_text_x=element_text(angle=90, color =light_white, size=8),
        )
).draw(); #raw
```


    
![png](/static/notebooks/airbnb/part2/output_14_0.png)
    


And we could check also which is the top 10 types of our dataset.


```python
sorted_by_price_top10 = airbnb_data.groupby(by='property_type')['price'].count().sort_values(ascending=False).head(10).index
(
    ggplot(airbnb_data,aes(x='property_type',y='price',fill='property_type',group='property_type')) +
    scale_x_discrete(limits=sorted_by_price_top10) +
    scale_fill_brewer(palette = "Oranges") +
    geom_bar(aes(y='stat(count)'),color=light_orange,show_legend=False) +
    labs(x='',y='Number of Publications',title='Fig 5 - Top 10 Property Type Publications') +
    orange_dark_theme +
    theme(
        axis_text_x=element_text(angle=45, ha='right',color =light_white, size=12),
        )
).draw(); #raw
```


    
![png](/static/notebooks/airbnb/part2/output_16_0.png)
    


### Correlations
Now we are going to check all the correlations from our dataset, so we could avoid using the correlated ones, as they could be described one from the other and when modeling we need only independent variables.


```python
df_corr = airbnb_data.corr()
df_corr = df_corr[(df_corr>0.8) | (df_corr<-0.8)] #I want only most relevant correlations.
# For visualization I don't want all nan values expect diagonal = 1
# So I will clear all not relevant ones.
df_corr = df_corr.abs()
df_corr['Corr'] = df_corr.sum()
df_corr = df_corr[df_corr['Corr'] > 1]
df_corr.drop('Corr',axis=1,inplace=True) #calculation column
df_corr.dropna(1,how='all',inplace=True) #All full nan columns
```


```python
sns.heatmap(df_corr,cmap='magma');
plt.suptitle("Fig 6 - Correlation Dependencies between principal variables", size = 24);
```


    
![png](/static/notebooks/airbnb/part2/output_19_0.png)
    


```We have cleaned >0.8 values, but we could drop till 0.95, but if some of them are 'logic' we could drop also <0.95 value```

Conclusions:

- We have that if we have soap we have bath essentials so we could drop one of them.
- As we see before 'host_listings_count' and 'host_total_listings_count' are highly related.
- If we have some comfort characteristic it seems that is shared with other comfort characteristics (bedroom, with kitchen, but we will let them.
- Of course, location1d and latitude are related as one has been done with the other.


### Location analysis

```Remember, we have created variable called 'location1d' which is the sumatory of latitude and longitude that will help us to determinate 1 point```

We need to see which is the behavior for location, so we will wrap our graphics with the property type, and its relation with location. Let's take a look:


```python
(
    ggplot(airbnb_data, aes(x='price',y='location1d')) +
    geom_point(aes(color='price')) + #it's not necessary color by price but help visualization
    facet_wrap('property_type', ncol = 3) + 
    orange_dark_theme +
    theme(
        figure_size=(20,70)
    )
    + labs(x='Price $', 
           y='Location (Lat+Long)',
           title='Fig 7 - Location vs Price aggregated by Property Type')
).draw();
```


    
![png](/static/notebooks/airbnb/part2/output_22_0.png)
    


Looking at 'Private room in apartment' and 'entire apartment' we found some correlation between locations and prices, we could see triangle (clear in 'Private room in apartment') where some locations have expensive distribution (you have lots of points to the right) compared with other locations. Same figure in 'entire apartment' where prices are more distributed but for the same locations you have several expensive points.

Is possible that other types follow the same behavior 'Private room in house' for example, but I think that we don't have enough data to arrive to some conclusion.

In fact, the impact over the price it's going to be very little because the big density of the other prices which are more or less distributed randomly so it makes us think that other variables will be much relevant for price determination.

#### (BONUS) We will focus on the most usual publication and take a more detailed view


```python
airbnb_private = airbnb_data[['latitude','longitude','price']][airbnb_data.property_type == 'Private room in apartment']
airbnb_private.price = airbnb_private.price.astype(float)
```


```python
#Centering the map
init_lat = airbnb_private.latitude.mean()
init_long = airbnb_private.longitude.mean()
```

We are going to represent in a map:

- **Heatmap**: Which represents 'heat' points for density publication.
- **Clustering**: Publications density.
- **Color Markers**: Represent different prices.


```python
import folium
from folium.plugins import MarkerCluster, HeatMap
m = folium.Map(
    tiles='CartoDB Dark_Matter',
    location=[init_lat, init_long],
    zoom_start=13,
    max_bounds=True
    )
marker_cluster = MarkerCluster().add_to(m)
for index, row in airbnb_data.iterrows():
    lat_air = row.latitude
    long_air = row.longitude
    price = row.price
    if (price > 0 ) & (price < 30):
        folium.Marker([lat_air, long_air],
                      tooltip=price,
                      icon=folium.Icon(color='green'),
                      clustered_marker = True
                         ).add_to(marker_cluster)
    elif (price < 50) & (price >= 30):
        folium.Marker([lat_air, long_air],
                    clustered_marker = True,
                    tooltip=price,
                    icon=folium.Icon(color='orange')
                 ).add_to(marker_cluster)
    elif (price < 90) & (price >= 50):
        folium.Marker([lat_air, long_air],
                    clustered_marker = True,
                    tooltip=price,
                    icon=folium.Icon(color='lightred')
                 ).add_to(marker_cluster)    
    else:
        folium.Marker([lat_air, long_air],
                    clustered_marker = True,
                    tooltip=price,
                    icon=folium.Icon(color='red')
                 ).add_to(marker_cluster)      

# convert to (n, 2) nd-array format for heatmap
privateArr = airbnb_data[['latitude', 'longitude']].values

# plot heatmap
m.add_children(HeatMap(privateArr, radius=12))
```

### Link to the <a href="/mapairbnb" target="_blank">Airbnb Map</a>

![png](/static/notebooks/airbnb/part2/general.png)

![png](/static/notebooks/airbnb/part2/detalles.png)
