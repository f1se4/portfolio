# INITIAL ANALYSIS OF FILES AND PREPARATION OF THE CASE

We will use actual data provided by AirBnB on this page: [Airbnb Insider](http://insideairbnb.com/get-the-data.html)


## SETUP


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

#Automcompletar rápido
%config IPCompleter.greedy=True
```

## UNDERSTAND THE FILES

On the AirBnB website we can see the description of the tables:


    
![jpeg](/static/notebooks/airbnbds4/02_Analisis%20de%20ficheros%20y%20preparacion%20del%20caso_files/02_Analisis%20de%20ficheros%20y%20preparacion%20del%20caso_6_0.jpg)
    



We are going to load one by one, understand them and make a decision whether to use it or not.

### We load and understand aggregated listings


```python
listings = pd.read_csv('../Datos/listings.csv')
```


```python
listings.head()
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
      <th>id</th>
      <th>name</th>
      <th>host_id</th>
      <th>host_name</th>
<td>...</td>
      <th>license</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6369</td>
      <td>Rooftop terrace room ,  ensuite bathroom</td>
      <td>13660</td>
      <td>Simon</td>
<td>...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21853</td>
      <td>Bright and airy room</td>
      <td>83531</td>
      <td>Abdel</td>
<td>...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23001</td>
      <td>Apartmento Arganzuela- Madrid Rio</td>
      <td>82175</td>
      <td>Jesus</td>
<td>...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24805</td>
      <td>Gran Via Studio Madrid</td>
      <td>346366726</td>
      <td>A</td>
<td>...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26825</td>
      <td>Single Room whith private Bathroom</td>
      <td>114340</td>
      <td>Agustina</td>
<td>...</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
listings.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 18909 entries, 0 to 18908
    Data columns (total 18 columns):
     #   Column                          Non-Null Count  Dtype  
    ---  ------                          --------------  -----  
     0   id                              18909 non-null  int64  
     1   name                            18906 non-null  object 
     2   host_id                         18909 non-null  int64  
     3   host_name                       18883 non-null  object 
     4   neighbourhood_group             18909 non-null  object 
     5   neighbourhood                   18909 non-null  object 
     6   latitude                        18909 non-null  float64
     7   longitude                       18909 non-null  float64
     8   room_type                       18909 non-null  object 
     9   price                           18909 non-null  int64  
     10  minimum_nights                  18909 non-null  int64  
     11  number_of_reviews               18909 non-null  int64  
     12  last_review                     13877 non-null  object 
     13  reviews_per_month               13877 non-null  float64
     14  calculated_host_listings_count  18909 non-null  int64  
     15  availability_365                18909 non-null  int64  
     16  number_of_reviews_ltm           18909 non-null  int64  
     17  license                         2828 non-null   object 
    dtypes: float64(3), int64(8), object(7)
    memory usage: 2.6+ MB


### We upload and understand detailed listings


```python
listings_det = pd.read_csv('../Datos/listings.csv.gz',compression='gzip')
```


```python
listings_det.head()
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
      <th>id</th>
      <th>listing_url</th>
      <th>scrape_id</th>
      <th>last_scraped</th>
      <th>name</th>
      <th>description</th>
      <th>...</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6369</td>
      <td>https://www.airbnb.com/rooms/6369</td>
      <td>20210910193531</td>
      <td>2021-09-11</td>
      <td>Rooftop terrace room ,  ensuite bathroom</td>
      <td>Excellent connection with the AIRPORT and EXHI...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21853</td>
      <td>https://www.airbnb.com/rooms/21853</td>
      <td>20210910193531</td>
      <td>2021-09-11</td>
      <td>Bright and airy room</td>
      <td>We have a quiet and sunny room with a good vie...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23001</td>
      <td>https://www.airbnb.com/rooms/23001</td>
      <td>20210910193531</td>
      <td>2021-09-11</td>
      <td>Apartmento Arganzuela- Madrid Rio</td>
      <td>Apartamento de tres dormitorios dobles, gran s...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24805</td>
      <td>https://www.airbnb.com/rooms/24805</td>
      <td>20210910193531</td>
      <td>2021-09-11</td>
      <td>Gran Via Studio Madrid</td>
      <td>Studio located 50 meters from Gran Via, next t...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26825</td>
      <td>https://www.airbnb.com/rooms/26825</td>
      <td>20210910193531</td>
      <td>2021-09-11</td>
      <td>Single Room whith private Bathroom</td>
      <td>Nice and cozy roon for one person with a priva...</td>
      <td>...</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 74 columns</p>
</div>




```python
listings_det.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 18909 entries, 0 to 18908
    Data columns (total 74 columns):
     #   Column                                        Non-Null Count  Dtype  
    ---  ------                                        --------------  -----  
     0   id                                            18909 non-null  int64  
     1   listing_url                                   18909 non-null  object 
     2   scrape_id                                     18909 non-null  int64  
     3   last_scraped                                  18909 non-null  object 
     4   name                                          18906 non-null  object 
     5   description                                   17854 non-null  object 
     6   neighborhood_overview                         10997 non-null  object 
     7   picture_url                                   18908 non-null  object 
     8   host_id                                       18909 non-null  int64  
     9   host_url                                      18909 non-null  object 
     10  host_name                                     18883 non-null  object 
     11  host_since                                    18883 non-null  object 
     12  host_location                                 18841 non-null  object 
     13  host_about                                    9427 non-null   object 
     14  host_response_time                            11972 non-null  object 
     15  host_response_rate                            11972 non-null  object 
     16  host_acceptance_rate                          11531 non-null  object 
     17  host_is_superhost                             18883 non-null  object 
     18  host_thumbnail_url                            18883 non-null  object 
     19  host_picture_url                              18883 non-null  object 
     20  host_neighbourhood                            12034 non-null  object 
     21  host_listings_count                           18883 non-null  float64
     22  host_total_listings_count                     18883 non-null  float64
     23  host_verifications                            18909 non-null  object 
     24  host_has_profile_pic                          18883 non-null  object 
     25  host_identity_verified                        18883 non-null  object 
     26  neighbourhood                                 10997 non-null  object 
     27  neighbourhood_cleansed                        18909 non-null  object 
     28  neighbourhood_group_cleansed                  18909 non-null  object 
     29  latitude                                      18909 non-null  float64
     30  longitude                                     18909 non-null  float64
     31  property_type                                 18909 non-null  object 
     32  room_type                                     18909 non-null  object 
     33  accommodates                                  18909 non-null  int64  
     34  bathrooms                                     0 non-null      float64
     35  bathrooms_text                                18884 non-null  object 
     36  bedrooms                                      17475 non-null  float64
     37  beds                                          18568 non-null  float64
     38  amenities                                     18909 non-null  object 
     39  price                                         18909 non-null  object 
     40  minimum_nights                                18909 non-null  int64  
     41  maximum_nights                                18909 non-null  int64  
     42  minimum_minimum_nights                        18908 non-null  float64
     43  maximum_minimum_nights                        18908 non-null  float64
     44  minimum_maximum_nights                        18908 non-null  float64
     45  maximum_maximum_nights                        18908 non-null  float64
     46  minimum_nights_avg_ntm                        18908 non-null  float64
     47  maximum_nights_avg_ntm                        18908 non-null  float64
     48  calendar_updated                              0 non-null      float64
     49  has_availability                              18909 non-null  object 
     50  availability_30                               18909 non-null  int64  
     51  availability_60                               18909 non-null  int64  
     52  availability_90                               18909 non-null  int64  
     53  availability_365                              18909 non-null  int64  
     54  calendar_last_scraped                         18909 non-null  object 
     55  number_of_reviews                             18909 non-null  int64  
     56  number_of_reviews_ltm                         18909 non-null  int64  
     57  number_of_reviews_l30d                        18909 non-null  int64  
     58  first_review                                  13877 non-null  object 
     59  last_review                                   13877 non-null  object 
     60  review_scores_rating                          13877 non-null  float64
     61  review_scores_accuracy                        13638 non-null  float64
     62  review_scores_cleanliness                     13640 non-null  float64
     63  review_scores_checkin                         13640 non-null  float64
     64  review_scores_communication                   13640 non-null  float64
     65  review_scores_location                        13637 non-null  float64
     66  review_scores_value                           13636 non-null  float64
     67  license                                       2828 non-null   object 
     68  instant_bookable                              18909 non-null  object 
     69  calculated_host_listings_count                18909 non-null  int64  
     70  calculated_host_listings_count_entire_homes   18909 non-null  int64  
     71  calculated_host_listings_count_private_rooms  18909 non-null  int64  
     72  calculated_host_listings_count_shared_rooms   18909 non-null  int64  
     73  reviews_per_month                             13877 non-null  float64
    dtypes: float64(22), int64(17), object(35)
    memory usage: 10.7+ MB


Conclusions:

* They are the same records but the detail file has more columns.
* We could join them through the id field

### We load and understand reviews added


```python
reviews = pd.read_csv('../Datos/reviews.csv')
```


```python
reviews.head()
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
      <th>listing_id</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6369</td>
      <td>2010-03-14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6369</td>
      <td>2010-03-23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6369</td>
      <td>2010-04-10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6369</td>
      <td>2010-04-21</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6369</td>
      <td>2010-04-26</td>
    </tr>
  </tbody>
</table>
</div>




```python
reviews.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 618440 entries, 0 to 618439
    Data columns (total 2 columns):
     #   Column      Non-Null Count   Dtype 
    ---  ------      --------------   ----- 
     0   listing_id  618440 non-null  int64 
     1   date        618440 non-null  object
    dtypes: int64(1), object(1)
    memory usage: 9.4+ MB


### We upload and understand detailed reviews


```python
reviews_det = pd.read_csv('../Datos/reviews.csv.gz',compression = 'gzip')
```


```python
reviews_det.head()
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
      <th>listing_id</th>
      <th>id</th>
      <th>date</th>
      <th>reviewer_id</th>
      <th>reviewer_name</th>
      <th>comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6369</td>
      <td>29428</td>
      <td>2010-03-14</td>
      <td>84790</td>
      <td>Nancy</td>
      <td>Simon and Arturo have the ultimate location in...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6369</td>
      <td>31018</td>
      <td>2010-03-23</td>
      <td>84338</td>
      <td>David</td>
      <td>Myself and Kristy originally planned on stayin...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6369</td>
      <td>34694</td>
      <td>2010-04-10</td>
      <td>98655</td>
      <td>Marion</td>
      <td>We had a great time at Arturo and Simon's ! A ...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6369</td>
      <td>37146</td>
      <td>2010-04-21</td>
      <td>109871</td>
      <td>Kurt</td>
      <td>I very much enjoyed the stay.  \r&lt;br/&gt;It's a w...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6369</td>
      <td>38168</td>
      <td>2010-04-26</td>
      <td>98901</td>
      <td>Dennis</td>
      <td>Arturo and Simon are polite and friendly hosts...</td>
    </tr>
  </tbody>
</table>
</div>




```python
reviews_det.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 618440 entries, 0 to 618439
    Data columns (total 6 columns):
     #   Column         Non-Null Count   Dtype 
    ---  ------         --------------   ----- 
     0   listing_id     618440 non-null  int64 
     1   id             618440 non-null  int64 
     2   date           618440 non-null  object
     3   reviewer_id    618440 non-null  int64 
     4   reviewer_name  618439 non-null  object
     5   comments       618054 non-null  object
    dtypes: int64(3), object(3)
    memory usage: 28.3+ MB


Conclusions:

* They are the same records but the detail file has more columns.
* Really this information from the reviews does not contribute anything to our objective, so we will not use these tables

### We load and understand calendar


```python
calendar = pd.read_csv('../Datos/calendar.csv.gz',compression = 'gzip')
```


```python
calendar.head(30)
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
      <th>listing_id</th>
      <th>date</th>
      <th>available</th>
      <th>price</th>
      <th>adjusted_price</th>
      <th>minimum_nights</th>
      <th>maximum_nights</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6369</td>
      <td>2021-09-11</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6369</td>
      <td>2021-09-12</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6369</td>
      <td>2021-09-13</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6369</td>
      <td>2021-09-14</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6369</td>
      <td>2021-09-15</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6369</td>
      <td>2021-09-16</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6369</td>
      <td>2021-09-17</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>6369</td>
      <td>2021-09-18</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>6369</td>
      <td>2021-09-19</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>6369</td>
      <td>2021-09-20</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>6369</td>
      <td>2021-09-21</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>6369</td>
      <td>2021-09-22</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>6369</td>
      <td>2021-09-23</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>6369</td>
      <td>2021-09-24</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>6369</td>
      <td>2021-09-25</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>6369</td>
      <td>2021-09-26</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>6369</td>
      <td>2021-09-27</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>6369</td>
      <td>2021-09-28</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>6369</td>
      <td>2021-09-29</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>6369</td>
      <td>2021-09-30</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>6369</td>
      <td>2021-10-01</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>6369</td>
      <td>2021-10-02</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>6369</td>
      <td>2021-10-03</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>6369</td>
      <td>2021-10-04</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>6369</td>
      <td>2021-10-05</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>6369</td>
      <td>2021-10-06</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>6369</td>
      <td>2021-10-07</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>6369</td>
      <td>2021-10-08</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>6369</td>
      <td>2021-10-09</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>6369</td>
      <td>2021-10-10</td>
      <td>t</td>
      <td>$60.00</td>
      <td>$60.00</td>
      <td>1.0</td>
      <td>1125.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
calendar.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 6901414 entries, 0 to 6901413
    Data columns (total 7 columns):
     #   Column          Dtype  
    ---  ------          -----  
     0   listing_id      int64  
     1   date            object 
     2   available       object 
     3   price           object 
     4   adjusted_price  object 
     5   minimum_nights  float64
     6   maximum_nights  float64
    dtypes: float64(2), int64(1), object(4)
    memory usage: 368.6+ MB


Conclusions:

* This table is projected into the future, and appears to contain reserve availability
* It is not information that serves our purposes and therefore we will not use it

### We load and understand neighborhoods.csv


```python
neigh = pd.read_csv('../Datos/neighbourhoods.csv')
```


```python
neigh.head(5)
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
      <th>neighbourhood_group</th>
      <th>neighbourhood</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Arganzuela</td>
      <td>Acacias</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arganzuela</td>
      <td>Atocha</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arganzuela</td>
      <td>Chopera</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arganzuela</td>
      <td>Delicias</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arganzuela</td>
      <td>Imperial</td>
    </tr>
  </tbody>
</table>
</div>



Conclusions:

* It is simply a neighborhood teacher and neighborhood group
* At first we will not use it, since both the neighborhood and its group are already incorporated into other tables

### Load and understand neighborhoods.geojson


```python
neigh_geo = pd.read_json('../Datos/neighbourhoods.geojson')
```


```python
neigh_geo.head(5)
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
      <th>type</th>
      <th>features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>FeatureCollection</td>
      <td>{'type': 'Feature', 'geometry': {'type': 'Mult...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>FeatureCollection</td>
      <td>{'type': 'Feature', 'geometry': {'type': 'Mult...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>FeatureCollection</td>
      <td>{'type': 'Feature', 'geometry': {'type': 'Mult...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>FeatureCollection</td>
      <td>{'type': 'Feature', 'geometry': {'type': 'Mult...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>FeatureCollection</td>
      <td>{'type': 'Feature', 'geometry': {'type': 'Mult...</td>
    </tr>
  </tbody>
</table>
</div>




```python
neigh_geo.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 128 entries, 0 to 127
    Data columns (total 2 columns):
     #   Column    Non-Null Count  Dtype 
    ---  ------    --------------  ----- 
     0   type      128 non-null    object
     1   features  128 non-null    object
    dtypes: object(2)
    memory usage: 2.1+ KB


Conclusions:

* Looks like geometry info for maps
* Making maps with geometries is out of the scope of this program, we will see another much easier option, so we will not use it

### Conclusions of the file analysis

* Main tables we will use:
     * listings.csv
     * listings.csv.gz

## CREATION OF A DATABASE

We are going to put the selected tables in an internal database.

We will use what is possibly the simplest database: sqlite, since it is self-contained, serverless and configuration-free, so it is usually the format of choice for storing "own" projects.

We create the connection:


```python
import sqlalchemy as sa

con = sa.create_engine('sqlite:///../Datos/airbnb.db')
```

We create the tables and load the data


```python
listings.to_sql('listings', con = con, if_exists = 'replace')
listings_det.to_sql('listings_det', con = con, if_exists = 'replace')
```
