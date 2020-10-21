# Barcelona Airbnb DS analysis (1st part)
## Source of data
[Inside Airbnb](http://insideairbnb.com/get-the-data.html) --> **Barcelona**

Date from the Data: *12/09/2020* 
```
\
|--Airbnb_Barcelona.ipynb
|--data
    |-calendarBarcelona.csv
    |-listingsBarcelona.csv
    |->> output.csv --> result file from part 1.
```

## Libraries and Importing Raw Data

```python
#Datamining library
import pandas as pd
import seaborn as sns
import numpy as np

from plotnine import *
```

```python
#Reading Raw Data
raw_data = pd.read_csv("./data/listingsBarcelona.csv")
airbnb_pub = raw_data.copy()
```

## General Exploration and Data Adjustment

Take a look at first in how much data and how is that data.

```python
print("Shape: ",airbnb_pub.shape)
print("Column Information:",airbnb_pub.info())
```

    Shape:  (20337, 74)
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 20337 entries, 0 to 20336
    Data columns (total 74 columns):
     #   Column                                        Non-Null Count  Dtype  
    ---  ------                                        --------------  -----  
     0   id                                            20337 non-null  int64  
     1   listing_url                                   20337 non-null  object 
     2   scrape_id                                     20337 non-null  int64  
     3   last_scraped                                  20337 non-null  object 
     4   name                                          20324 non-null  object 
     5   description                                   20185 non-null  object 
     6   neighborhood_overview                         12447 non-null  object 
     7   picture_url                                   20337 non-null  object 
     8   host_id                                       20337 non-null  int64  
     9   host_url                                      20337 non-null  object 
     10  host_name                                     20330 non-null  object 
     11  host_since                                    20330 non-null  object 
     12  host_location                                 20305 non-null  object 
     13  host_about                                    12573 non-null  object 
     14  host_response_time                            13233 non-null  object 
     15  host_response_rate                            13233 non-null  object 
     16  host_acceptance_rate                          16752 non-null  object 
     17  host_is_superhost                             20330 non-null  object 
     18  host_thumbnail_url                            20330 non-null  object 
     19  host_picture_url                              20330 non-null  object 
     20  host_neighbourhood                            14891 non-null  object 
     21  host_listings_count                           20330 non-null  float64
     22  host_total_listings_count                     20330 non-null  float64
     23  host_verifications                            20337 non-null  object 
     24  host_has_profile_pic                          20330 non-null  object 
     25  host_identity_verified                        20330 non-null  object 
     26  neighbourhood                                 12447 non-null  object 
     27  neighbourhood_cleansed                        20337 non-null  object 
     28  neighbourhood_group_cleansed                  20337 non-null  object 
     29  latitude                                      20337 non-null  float64
     30  longitude                                     20337 non-null  float64
     31  property_type                                 20337 non-null  object 
     32  room_type                                     20337 non-null  object 
     33  accommodates                                  20337 non-null  int64  
     34  bathrooms                                     0 non-null      float64
     35  bathrooms_text                                20326 non-null  object 
     36  bedrooms                                      19630 non-null  float64
     37  beds                                          19923 non-null  float64
     38  amenities                                     20337 non-null  object 
     39  price                                         20337 non-null  object 
     40  minimum_nights                                20337 non-null  int64  
     41  maximum_nights                                20337 non-null  int64  
     42  minimum_minimum_nights                        20337 non-null  int64  
     43  maximum_minimum_nights                        20337 non-null  int64  
     44  minimum_maximum_nights                        20337 non-null  int64  
     45  maximum_maximum_nights                        20337 non-null  int64  
     46  minimum_nights_avg_ntm                        20337 non-null  float64
     47  maximum_nights_avg_ntm                        20337 non-null  float64
     48  calendar_updated                              0 non-null      float64
     49  has_availability                              20337 non-null  object 
     50  availability_30                               20337 non-null  int64  
     51  availability_60                               20337 non-null  int64  
     52  availability_90                               20337 non-null  int64  
     53  availability_365                              20337 non-null  int64  
     54  calendar_last_scraped                         20337 non-null  object 
     55  number_of_reviews                             20337 non-null  int64  
     56  number_of_reviews_ltm                         20337 non-null  int64  
     57  number_of_reviews_l30d                        20337 non-null  int64  
     58  first_review                                  14526 non-null  object 
     59  last_review                                   14526 non-null  object 
     60  review_scores_rating                          14278 non-null  float64
     61  review_scores_accuracy                        14267 non-null  float64
     62  review_scores_cleanliness                     14269 non-null  float64
     63  review_scores_checkin                         14263 non-null  float64
     64  review_scores_communication                   14270 non-null  float64
     65  review_scores_location                        14264 non-null  float64
     66  review_scores_value                           14263 non-null  float64
     67  license                                       12854 non-null  object 
     68  instant_bookable                              20337 non-null  object 
     69  calculated_host_listings_count                20337 non-null  int64  
     70  calculated_host_listings_count_entire_homes   20337 non-null  int64  
     71  calculated_host_listings_count_private_rooms  20337 non-null  int64  
     72  calculated_host_listings_count_shared_rooms   20337 non-null  int64  
     73  reviews_per_month                             14526 non-null  float64
    dtypes: float64(18), int64(21), object(35)
    memory usage: 11.5+ MB
    Column Information: None
    

The dataset has 20337 lines with 74 different columns and types.

Here it's going to be detected/reviewed/changed:

- Aggregated columns, could be images, hashtags, datasets inside principal dataset, etc...
- *Types* that for our interest should be changed.
    - False/True Values to boolean ones
    - String types that are numeric
    - Manage Nan Values
    - Resize using analytical and functional logic   

### Currency detected as string (object) in spite of numbers (float)

If we look at our column information we will see that **price** is an 'object' type:
```
39  price                                         20337 non-null  object 
```
Let's take a look to the column


```python
airbnb_pub['price'].head(2)
```

    0     $80.00
    1    $200.00
    Name: price, dtype: object



It has been selected to string because it has *$* symbol. So we will need to modify by clearing this symbol and changing to *float*.


```python
airbnb_pub['price'] = airbnb_pub['price'].str.replace("$","").str.replace(",","").astype(float)
```
Now as this is going to be the variable that we would like to predict and study, let's take a look to the distribution of the data, as we want to have it cleaned, without strange values or nonsense values, and from statistical point of view, relevant data so we could predict the usual cases of the dataset.

```python
airbnb_pub.price.describe()
```
    count    20337.00000
    mean        84.79339
    std        210.66629
    min          0.00000
    25%         35.00000
    50%         55.00000
    75%         93.00000
    max      10000.00000
    Name: price, dtype: float64



Looking at percentiles we could see that more or less all values are in a range near 100, and then it seems that we have some outliers, we will try to 'catch' the normal behaivour so we want to use and truncate data with most usual values.

If we 'graph' them it will become more obvious.


```python
(
    ggplot(airbnb_pub,aes(x='id',y='price')) +
    geom_boxplot(fill=orange,color='red') +
    orange_dark_theme
).draw(); #raw
```
    
![png](/static/notebooks/airbnb/images/output_14_0.png)
 

Now the price filter is going to be changed till we have some values that belongs to the 'normal' expected price, to try to avoid in our future model any inconsistence because outliers. Here you have the last result, I have let some outliers to let the future model to detect some trend or non obvious behaivour.


```python
airbnb_pub = airbnb_pub.loc[(airbnb_pub.price <=150) & (airbnb_pub.price>0)]
(
    ggplot(airbnb_pub,aes(x='id',y='price')) +
    geom_boxplot(fill=orange,color='red') +
    orange_dark_theme
).draw();
print(airbnb_pub.price.describe())
```

    count    18466.000000
    mean        58.502799
    std         33.610651
    min          8.000000
    25%         32.000000
    50%         50.000000
    75%         80.000000
    max        150.000000
    Name: price, dtype: float64
    
   
![png](/static/notebooks/airbnb/images/output_16_1.png)

After that we have now smaller data collection without outliers, so we could think that we are going to take the usual behaivor of the dataset in 95% of confidence.

### Extracting additional data from 'complex' fields
There are some data that is composed by different other data, we want to use them, so we need to transform these information in new columns.


```python
airbnb_pub.amenities.head(3)
```
    0    ["Carbon monoxide alarm", "Fire extinguisher",...
    3    ["Stove", "Microwave", "Refrigerator", "Oven",...
    4    ["Refrigerator", "Microwave", "Carbon monoxide...
    Name: amenities, dtype: object


```python
#Text to column tool -> Vectorizer
from sklearn.feature_extraction.text import CountVectorizer
count_vectorizer = CountVectorizer(tokenizer=lambda x: x.split(','))
amenities = count_vectorizer.fit_transform(airbnb_pub.amenities)
```


```python
#We are going to clean column names
columns=count_vectorizer.get_feature_names()
for index, item in enumerate(columns):
    replaced = item.replace('"','').replace('[','').replace(']','').strip()
    columns[index] = replaced
```


```python
# dataframe with new columns
df_amenities = pd.DataFrame(amenities.toarray(),columns=columns)
df_amenities.head(2)
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>air conditioning</th>
      <th>air conditioning</th>
      <th>baby bath</th>
      <th>...</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
    </tr>
  </tbody>
</table>
<p>2 rows x 206 columns</p>
</div>

### Boolean literals to binary literals

In the visual exploration (most different possibilities excel/csviewer/spyder/vscode....) we have seen that some columns have 'T' for True and 'F' for false, we need to transform them in a way that we could use in future model.


```python
# I'm going to 'catch' all possible columns to be transformed.
boolean_list = []
for col in airbnb_pub.columns:
    if airbnb_pub[col].unique().size == 3:
        column_array_values = np.delete(airbnb_pub[col].unique(),2,0)
        if set(column_array_values)==set(['t','f']):
            boolean_list.append(col)
    if airbnb_pub[col].unique().size == 2:
        if set(column_array_values)==set(['t','f']):
            boolean_list.append(col)
boolean_list
```

    ['host_is_superhost',
     'host_has_profile_pic',
     'host_identity_verified',
     'has_availability',
     'instant_bookable']




```python
# Transform to binary
for col in boolean_list:
    airbnb_pub[col] = airbnb_pub[col].replace('f',0)
    airbnb_pub[col] = airbnb_pub[col].replace('t',1)
```

### Looking for nan values in number columns
We have seen that we have different types in our dataset, in this case we want to look for numerical ones, we have only 2 types in our dataset that are numericals *float64* and *int64*.
We want to know if they are completed or have *Nan* values, if *Nan* then we want to change with the mean of the serie (column).

```Notice that false true changed to boolean could be also affected```


```python
for c in airbnb_pub:
    if ((airbnb_pub[c].dtype=='float64') | (airbnb_pub[c].dtype=='int64')):
        if airbnb_pub[c].isnull().any():
            airbnb_pub[c] = airbnb_pub[c].fillna(airbnb_pub[c].median())
```

### Creating our final output dataset to start with analytics
**Summary**
- We have detected some pricing data that initially was selected as string and we have changed it to numeric format.
- Resize our dataset by clearing all negative prizes and outliers prizes.
- All string boolean values have been changed to numeric ones.
- All Nan numeric dataset values have been treated to avoid any numerical issue
- Some data items are dataset itself, we have catch it, split and transform in an individual dataset

We have to take some decission about which data will be relevant for our model, which columns, thinking that our objective is to have a model that predicts or help us which values are most relevant in price determination.

We will also add our amenities dataset as we found them relevant for price determination, and we want to have them in our model.


```python
#Small script to let me select in the next step the columns in an easy way using notebook :P
#I have cleared the output because readability reasons.
for c in airbnb_pub.columns:
    print('"',c,'",',sep="")
```

    "id",
    "listing_url",
    "scrape_id",
    ...
    ...    


```python
airbnb_pub = airbnb_pub[[
"host_is_superhost",
"host_identity_verified",
"host_has_profile_pic",
"instant_bookable",
"bedrooms",
"room_type",
"bathrooms",
"beds",
"property_type",
"number_of_reviews",
"host_listings_count",
"host_total_listings_count",
"minimum_nights",
"review_scores_rating",
"price"
]]
```


```python
airbnb_data = pd.concat([airbnb_pub,df_amenities],axis=1,join='inner')
airbnb_data.to_csv("./data/output.csv")
print("Final output dataset Shape: ",airbnb_data.shape)
```

    Final output dataset Shape:  (16732, 221)
    

And that's all, airbnb data cleaning has been done and we are ready for analyze the data that we 'feel' that is relevant for pricing, of course, using the same pipeline we could test/check and recatch all the steps that we have done to review or try or remove some data with the results we have when modelizing or analyzing the data.
