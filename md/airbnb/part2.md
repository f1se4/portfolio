# Barcelona Airbnb DS analysis (2nd part) 
We are going now to try to understand our data a bit more.

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

# Viewing/Understanding the data

We will start trying to find correlations/aggrupations in a visual way, for that we have an excelent tool from seaborn (location will be analyzed at the end):


```python
sns.pairplot(airbnb_data[[
"bedrooms",
"room_type",
"beds",
"property_type",
"number_of_reviews",
"host_listings_count",
"host_total_listings_count",
"minimum_nights",
"review_scores_rating",
"price"
]],hue='property_type');
```

    
![png](/static/notebooks/airbnb/images/output_8_1.png)
    

```python
(
    ggplot(airbnb_data, aes(x='review_scores_rating')) +
    geom_density(aes(y='stat(count)'), fill=orange,color='red',alpha=0.3) +
    geom_bar(aes(y='stat(count)'),fill=yellow_orange,alpha=0.2) +
    orange_dark_theme
).draw();
```

   
![png](/static/notebooks/airbnb/images/output_9_0.png)
    


```python
sorted_by_price = airbnb_data.groupby(by='property_type')['price'].median().sort_values(ascending=False).index
```

```python
(
    ggplot(airbnb_data,aes(x='property_type',y='price',fill='property_type',group='property_type')) +
    scale_x_discrete(limits=sorted_by_price) +
    geom_boxplot(color=light_orange,show_legend=False) +
    labs(x='',y='Price $') +
    orange_dark_theme +
    theme(
        axis_text_x=element_text(angle=90, color =light_white, size=8),
        )
).draw(); #raw
```
    
![png](/static/notebooks/airbnb/images/output_11_0.png)
    

```python
sorted_by_price_top10 = airbnb_data.groupby(by='property_type')['price'].count().sort_values(ascending=False).head(10).index
(
    ggplot(airbnb_data,aes(x='property_type',y='price',fill='property_type',group='property_type')) +
    scale_x_discrete(limits=sorted_by_price_top10) +
    scale_fill_brewer(palette = "Oranges") +
    geom_bar(aes(y='stat(count)'),color=light_orange,show_legend=False) +
    labs(x='',y='Number of Publications') +
    orange_dark_theme +
    theme(
        axis_text_x=element_text(angle=45, ha='right',color =light_white, size=12),
        )
).draw(); #raw
```
    
![png](/static/notebooks/airbnb/images/output_12_0.png)
    

```python
df_corr = airbnb_data.corr()
df_corr = df_corr[(df_corr>0.8) | (df_corr<-0.8)]
```

```python
sns.heatmap(df_corr,cmap='magma');
```
    
![png](/static/notebooks/airbnb/images/output_14_0_b.png)
    
### Location analysis

```python
(
    ggplot(airbnb_data, aes(x='price',y='location1d',colors='review_scores_rating')) +
    geom_point() +
    facet_wrap('property_type', ncol = 3) +
    orange_dark_theme +
    theme(
        figure_size=(20,70)
    )
    + labs(x='Price $', y='Location (Lat+Long)')
).draw();
```

    
![png](/static/notebooks/airbnb/images/output_16_0.png)
    

Looking at 'Private room in apartment' and 'entire apartment' we found some correlation between locations and prices, we could see triangle (clear in 'Private room in apartment') where some locations have expensive distribution (you have lots of points to the right) compared with other locations. Same figure in 'entire apartment' where prices are more distributed but for the same locations you have several expensive points.

Is possible that other types follow the same behavior 'Private room in house' for example, but I think that we don't have enough data to arrive to some conclusion.

In fact, the impact over the price it's going to be very little because the big density of the other prices which are more or less distributed randomly so it makes us think that other variables will be much relevant for price determination.

#### We will focus on the most usual publication and take a more detailed view


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
### Link to the [Barcelona Airbnb Map](/mapairbnb)

![png](/static/notebooks/airbnb/images/general.png)

![png](/static/notebooks/airbnb/images/detalles.png)
