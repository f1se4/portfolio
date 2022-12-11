# ANALYSIS AND INSIGHTS

We come to the most important part, where we are going to try to obtain relevant conclusions for the objective using all the preparation work we have done, the Business Analytics techniques that we already know and also we are going to learn how to create a map visualization.

To do this, we will begin by answering the seed questions and it is likely that in the process interesting findings will emerge that lead us to new questions or the application of certain techniques.

## SET UP


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import sqlalchemy as sa

#Automcompletar rápido
%config IPCompleter.greedy=True

pd.options.display.max_columns = None
```


```python
import fiser_tools as fs
fs.misc.dark_theme()
```

## DATA UPLOAD


```python
con = sa.create_engine('sqlite:///../DatosCaso1/airbnb.db')

df = pd.read_sql('df_preparado', con = con)

df.head()
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
      <th>level_0</th>
      <th>index</th>
      <th>id</th>
      <th>name</th>
      <th>host_id</th>
      <th>neighbourhood_group</th>
      <th>neighbourhood</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>room_type</th>
      <th>price</th>
      <th>minimum_nights</th>
      <th>calculated_host_listings_count</th>
      <th>availability_365</th>
      <th>description</th>
      <th>host_is_superhost</th>
      <th>accommodates</th>
      <th>bedrooms</th>
      <th>beds</th>
      <th>number_of_reviews</th>
      <th>review_scores_rating</th>
      <th>review_scores_communication</th>
      <th>review_scores_location</th>
      <th>precio_m2</th>
      <th>distrito</th>
      <th>precio_total</th>
      <th>ocupacion</th>
      <th>bedrooms_disc</th>
      <th>accommodates_disc</th>
      <th>beds_disc</th>
      <th>number_of_reviews_disc</th>
      <th>m2</th>
      <th>precio_compra</th>
      <th>pdi_sol</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>6369</td>
      <td>Rooftop terrace room ,  ensuite bathroom</td>
      <td>13660</td>
      <td>Chamartín</td>
      <td>Hispanoamérica</td>
      <td>40.45724</td>
      <td>-3.67688</td>
      <td>Private room</td>
      <td>60</td>
      <td>1</td>
      <td>2</td>
      <td>180</td>
      <td>Excellent connection with the AIRPORT and EXHI...</td>
      <td>t</td>
      <td>2</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>80</td>
      <td>4.87</td>
      <td>4.89</td>
      <td>4.77</td>
      <td>164</td>
      <td>Chamartín</td>
      <td>60.0</td>
      <td>50</td>
      <td>01_Una</td>
      <td>0-2</td>
      <td>1</td>
      <td>48-744</td>
      <td>50</td>
      <td>5740.0</td>
      <td>5.032039</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>21853</td>
      <td>Bright and airy room</td>
      <td>83531</td>
      <td>Latina</td>
      <td>Cármenes</td>
      <td>40.40381</td>
      <td>-3.74130</td>
      <td>Private room</td>
      <td>31</td>
      <td>4</td>
      <td>2</td>
      <td>364</td>
      <td>We have a quiet and sunny room with a good vie...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>33</td>
      <td>4.58</td>
      <td>4.82</td>
      <td>4.21</td>
      <td>125</td>
      <td>Latina</td>
      <td>31.0</td>
      <td>0</td>
      <td>01_Una</td>
      <td>0-2</td>
      <td>1</td>
      <td>5-48</td>
      <td>50</td>
      <td>4375.0</td>
      <td>3.521406</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2</td>
      <td>23001</td>
      <td>Apartmento Arganzuela- Madrid Rio</td>
      <td>82175</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.38840</td>
      <td>-3.69511</td>
      <td>Entire home/apt</td>
      <td>50</td>
      <td>15</td>
      <td>5</td>
      <td>222</td>
      <td>Apartamento de tres dormitorios dobles, gran s...</td>
      <td>f</td>
      <td>6</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>155</td>
      <td>Arganzuela</td>
      <td>50.0</td>
      <td>39</td>
      <td>03_Tres</td>
      <td>4-16</td>
      <td>3-24</td>
      <td>1-4</td>
      <td>90</td>
      <td>9765.0</td>
      <td>3.226963</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>3</td>
      <td>24805</td>
      <td>Gran Via Studio Madrid</td>
      <td>346366726</td>
      <td>Centro</td>
      <td>Universidad</td>
      <td>40.42183</td>
      <td>-3.70529</td>
      <td>Entire home/apt</td>
      <td>92</td>
      <td>5</td>
      <td>1</td>
      <td>115</td>
      <td>Studio located 50 meters from Gran Via, next t...</td>
      <td>f</td>
      <td>3</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>12</td>
      <td>4.92</td>
      <td>5.00</td>
      <td>5.00</td>
      <td>186</td>
      <td>Centro</td>
      <td>92.0</td>
      <td>68</td>
      <td>01_Una</td>
      <td>0-2</td>
      <td>1</td>
      <td>5-48</td>
      <td>50</td>
      <td>6510.0</td>
      <td>0.591065</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>4</td>
      <td>26825</td>
      <td>Single Room whith private Bathroom</td>
      <td>114340</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.38975</td>
      <td>-3.69018</td>
      <td>Private room</td>
      <td>26</td>
      <td>2</td>
      <td>1</td>
      <td>349</td>
      <td>Nice and cozy roon for one person with a priva...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>149</td>
      <td>4.68</td>
      <td>4.71</td>
      <td>4.70</td>
      <td>155</td>
      <td>Arganzuela</td>
      <td>26.0</td>
      <td>4</td>
      <td>01_Una</td>
      <td>0-2</td>
      <td>1</td>
      <td>48-744</td>
      <td>50</td>
      <td>5425.0</td>
      <td>3.200942</td>
    </tr>
  </tbody>
</table>
</div>



## ANALYSIS

### Price analysis

**What is the average price? And the price range? And by districts? And by neighborhoods?**

**What is the ranking of districts and neighborhoods by average rental price?**


```python
df.precio_total.describe()
```




    count    17710.000000
    mean       149.027770
    std        523.211567
    min         20.000000
    25%         43.000000
    50%         70.000000
    75%        112.000000
    max      22400.000000
    Name: precio_total, dtype: float64



We see that there is at least one outlier on the upper part that skews the mean, so we are going to use the median as a more reliable measure of centralization.


```python
df.precio_total.median()
```




    70.0




```python
df.groupby('distrito').precio_total.median().sort_values(ascending = False)
```




    distrito
    San Blas - Canillejas    90.0
    Salamanca                88.0
    Centro                   76.0
    Chamartín                74.0
    Chamberí                 70.0
    Hortaleza                69.0
    Retiro                   68.0
    Tetuán                   66.0
    Moncloa - Aravaca        61.0
    Fuencarral - El Pardo    60.0
    Arganzuela               58.0
    Vicálvaro                53.0
    Ciudad Lineal            50.0
    Barajas                  49.5
    Carabanchel              48.0
    Villa de Vallecas        47.5
    Latina                   47.0
    Usera                    42.0
    Villaverde               42.0
    Moratalaz                40.0
    Puente de Vallecas       40.0
    Name: precio_total, dtype: float64



The data from San Blas catches our attention, we are going to look at it in more detail to see what is happening.


```python
df.loc[df.distrito == 'San Blas - Canillejas'].sort_values('precio_total',ascending = False).head(10)
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
      <th>level_0</th>
      <th>index</th>
      <th>id</th>
      <th>name</th>
      <th>host_id</th>
      <th>neighbourhood_group</th>
      <th>neighbourhood</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>room_type</th>
      <th>price</th>
      <th>minimum_nights</th>
      <th>calculated_host_listings_count</th>
      <th>availability_365</th>
      <th>description</th>
      <th>host_is_superhost</th>
      <th>accommodates</th>
      <th>bedrooms</th>
      <th>beds</th>
      <th>number_of_reviews</th>
      <th>review_scores_rating</th>
      <th>review_scores_communication</th>
      <th>review_scores_location</th>
      <th>precio_m2</th>
      <th>distrito</th>
      <th>precio_total</th>
      <th>ocupacion</th>
      <th>bedrooms_disc</th>
      <th>accommodates_disc</th>
      <th>beds_disc</th>
      <th>number_of_reviews_disc</th>
      <th>m2</th>
      <th>precio_compra</th>
      <th>pdi_sol</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>9290</th>
      <td>9290</td>
      <td>9290</td>
      <td>34600594</td>
      <td>3 rooms near Wanda</td>
      <td>38951538</td>
      <td>San Blas - Canillejas</td>
      <td>Arcos</td>
      <td>40.42105</td>
      <td>-3.61457</td>
      <td>Private room</td>
      <td>2800</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>3 rooms 15´walking from Wanda.</td>
      <td>f</td>
      <td>6</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>120</td>
      <td>San Blas - Canillejas</td>
      <td>9800.0</td>
      <td>100</td>
      <td>03_Tres</td>
      <td>4-16</td>
      <td>3-24</td>
      <td>1-4</td>
      <td>90</td>
      <td>7560.0</td>
      <td>7.532233</td>
    </tr>
    <tr>
      <th>9662</th>
      <td>9662</td>
      <td>9662</td>
      <td>34826962</td>
      <td>Pozos rooms</td>
      <td>222068421</td>
      <td>San Blas - Canillejas</td>
      <td>Arcos</td>
      <td>40.41927</td>
      <td>-3.61555</td>
      <td>Private room</td>
      <td>3000</td>
      <td>1</td>
      <td>1</td>
      <td>88</td>
      <td>Cerca nos podemos encontrar un centro comercia...</td>
      <td>f</td>
      <td>4</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>120</td>
      <td>San Blas - Canillejas</td>
      <td>6300.0</td>
      <td>75</td>
      <td>02_Dos</td>
      <td>3</td>
      <td>2</td>
      <td>1-4</td>
      <td>70</td>
      <td>5880.0</td>
      <td>7.439364</td>
    </tr>
    <tr>
      <th>10189</th>
      <td>10189</td>
      <td>10189</td>
      <td>35149419</td>
      <td>CHALET FOR THE FINAL CHAMPIONS LEAGUE MADRID</td>
      <td>143732655</td>
      <td>San Blas - Canillejas</td>
      <td>Canillejas</td>
      <td>40.44937</td>
      <td>-3.61633</td>
      <td>Entire home/apt</td>
      <td>6000</td>
      <td>1</td>
      <td>1</td>
      <td>365</td>
      <td>We are talking about one of the last villas fo...</td>
      <td>f</td>
      <td>6</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>120</td>
      <td>San Blas - Canillejas</td>
      <td>6000.0</td>
      <td>0</td>
      <td>04_Cuatro o mas</td>
      <td>4-16</td>
      <td>3-24</td>
      <td>1-4</td>
      <td>120</td>
      <td>10080.0</td>
      <td>8.212429</td>
    </tr>
    <tr>
      <th>9668</th>
      <td>9668</td>
      <td>9668</td>
      <td>34833756</td>
      <td>Wanda Champions Final</td>
      <td>29628177</td>
      <td>San Blas - Canillejas</td>
      <td>Rosas</td>
      <td>40.42622</td>
      <td>-3.60502</td>
      <td>Private room</td>
      <td>2700</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>Somos una pareja joven educados y muy sociable...</td>
      <td>f</td>
      <td>5</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>120</td>
      <td>San Blas - Canillejas</td>
      <td>5670.0</td>
      <td>100</td>
      <td>02_Dos</td>
      <td>4-16</td>
      <td>2</td>
      <td>1-4</td>
      <td>70</td>
      <td>5880.0</td>
      <td>8.391922</td>
    </tr>
    <tr>
      <th>9878</th>
      <td>9878</td>
      <td>9878</td>
      <td>34970236</td>
      <td>Habitaciones cerca Wanda Metropolitano (Champi...</td>
      <td>263474389</td>
      <td>San Blas - Canillejas</td>
      <td>Arcos</td>
      <td>40.41920</td>
      <td>-3.61229</td>
      <td>Private room</td>
      <td>800</td>
      <td>1</td>
      <td>1</td>
      <td>88</td>
      <td>Se alquilan 5 habitaciones, cada una para 2 hu...</td>
      <td>f</td>
      <td>10</td>
      <td>5.0</td>
      <td>8.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>120</td>
      <td>San Blas - Canillejas</td>
      <td>4480.0</td>
      <td>75</td>
      <td>04_Cuatro o mas</td>
      <td>4-16</td>
      <td>3-24</td>
      <td>1-4</td>
      <td>150</td>
      <td>12600.0</td>
      <td>7.714952</td>
    </tr>
    <tr>
      <th>9748</th>
      <td>9748</td>
      <td>9748</td>
      <td>34882596</td>
      <td>2 rooms near wanda</td>
      <td>38951538</td>
      <td>San Blas - Canillejas</td>
      <td>Arcos</td>
      <td>40.41948</td>
      <td>-3.61427</td>
      <td>Private room</td>
      <td>1500</td>
      <td>1</td>
      <td>2</td>
      <td>363</td>
      <td>2 rooms near Wanda stadium (20' walking) with ...</td>
      <td>f</td>
      <td>4</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>120</td>
      <td>San Blas - Canillejas</td>
      <td>4200.0</td>
      <td>0</td>
      <td>02_Dos</td>
      <td>3</td>
      <td>3-24</td>
      <td>1-4</td>
      <td>70</td>
      <td>5880.0</td>
      <td>7.548577</td>
    </tr>
    <tr>
      <th>9173</th>
      <td>9173</td>
      <td>9173</td>
      <td>34522997</td>
      <td>Beautiful Penthouse next to Wanda Metropolitano</td>
      <td>260551569</td>
      <td>San Blas - Canillejas</td>
      <td>Canillejas</td>
      <td>40.43686</td>
      <td>-3.61093</td>
      <td>Private room</td>
      <td>2000</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>Wonderful penthouse in a lovely duplex next to...</td>
      <td>f</td>
      <td>4</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>120</td>
      <td>San Blas - Canillejas</td>
      <td>4200.0</td>
      <td>100</td>
      <td>01_Una</td>
      <td>3</td>
      <td>2</td>
      <td>1-4</td>
      <td>50</td>
      <td>4200.0</td>
      <td>8.138310</td>
    </tr>
    <tr>
      <th>9831</th>
      <td>9831</td>
      <td>9831</td>
      <td>34933116</td>
      <td>FINAL CHAMPIONS LEAGUE MADRID</td>
      <td>263232278</td>
      <td>San Blas - Canillejas</td>
      <td>Simancas</td>
      <td>40.43968</td>
      <td>-3.61933</td>
      <td>Private room</td>
      <td>2000</td>
      <td>2</td>
      <td>1</td>
      <td>365</td>
      <td>Near (15 minutes walking) to WANDA STADIUM.&lt;br...</td>
      <td>f</td>
      <td>5</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>120</td>
      <td>San Blas - Canillejas</td>
      <td>4200.0</td>
      <td>0</td>
      <td>03_Tres</td>
      <td>4-16</td>
      <td>2</td>
      <td>1-4</td>
      <td>90</td>
      <td>7560.0</td>
      <td>7.557076</td>
    </tr>
    <tr>
      <th>10092</th>
      <td>10092</td>
      <td>10092</td>
      <td>35091283</td>
      <td>FINAL CHAMPIONS LEAGUE</td>
      <td>264225539</td>
      <td>San Blas - Canillejas</td>
      <td>Rejas</td>
      <td>40.44592</td>
      <td>-3.58746</td>
      <td>Private room</td>
      <td>1000</td>
      <td>1</td>
      <td>1</td>
      <td>180</td>
      <td>Desayuno, comida y cena incluida. Traslados al...</td>
      <td>f</td>
      <td>6</td>
      <td>2.0</td>
      <td>6.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>120</td>
      <td>San Blas - Canillejas</td>
      <td>4200.0</td>
      <td>50</td>
      <td>02_Dos</td>
      <td>4-16</td>
      <td>3-24</td>
      <td>1-4</td>
      <td>70</td>
      <td>5880.0</td>
      <td>10.334061</td>
    </tr>
    <tr>
      <th>10404</th>
      <td>10404</td>
      <td>10404</td>
      <td>35251141</td>
      <td>Se alquila para final de la champion league</td>
      <td>265376740</td>
      <td>San Blas - Canillejas</td>
      <td>Canillejas</td>
      <td>40.44292</td>
      <td>-3.60764</td>
      <td>Entire home/apt</td>
      <td>3000</td>
      <td>1</td>
      <td>1</td>
      <td>365</td>
      <td>None</td>
      <td>f</td>
      <td>1</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>120</td>
      <td>San Blas - Canillejas</td>
      <td>3000.0</td>
      <td>0</td>
      <td>02_Dos</td>
      <td>0-2</td>
      <td>3-24</td>
      <td>1-4</td>
      <td>70</td>
      <td>5880.0</td>
      <td>8.610212</td>
    </tr>
  </tbody>
</table>
</div>



We see that they are prices in the environment of 3,000 - 5,000 euros!

When reading the description we realize that all these prices are defined by the Champions League final.

Which is an interesting insight:

**Insight 1: there may be properties with a regular residual value but with high value at specific times due to sporting events or shows**

Would it make sense to generate a rental product that consists of renting in a "normal" way at a price below the market with the condition that the tenant leaves the apartment free to rent it "touristically" on designated dates?

In the rest there are no surprises, with districts like Salamanca, Centro or Chanmartín in the lead.

But for example we see that the average price difference between Retiro and Tetuán is very low.

This leads us to compare the average price per district with the average purchase price also per district.


```python
temp = df.groupby('distrito')[['precio_total','precio_compra']].median()
temp
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
      <th>precio_total</th>
      <th>precio_compra</th>
    </tr>
    <tr>
      <th>distrito</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Arganzuela</th>
      <td>58.0</td>
      <td>5425.0</td>
    </tr>
    <tr>
      <th>Barajas</th>
      <td>49.5</td>
      <td>4235.0</td>
    </tr>
    <tr>
      <th>Carabanchel</th>
      <td>48.0</td>
      <td>4305.0</td>
    </tr>
    <tr>
      <th>Centro</th>
      <td>76.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>Chamartín</th>
      <td>74.0</td>
      <td>5740.0</td>
    </tr>
    <tr>
      <th>Chamberí</th>
      <td>70.0</td>
      <td>6300.0</td>
    </tr>
    <tr>
      <th>Ciudad Lineal</th>
      <td>50.0</td>
      <td>4760.0</td>
    </tr>
    <tr>
      <th>Fuencarral - El Pardo</th>
      <td>60.0</td>
      <td>4480.0</td>
    </tr>
    <tr>
      <th>Hortaleza</th>
      <td>69.0</td>
      <td>4515.0</td>
    </tr>
    <tr>
      <th>Latina</th>
      <td>47.0</td>
      <td>4375.0</td>
    </tr>
    <tr>
      <th>Moncloa - Aravaca</th>
      <td>61.0</td>
      <td>5390.0</td>
    </tr>
    <tr>
      <th>Moratalaz</th>
      <td>40.0</td>
      <td>3955.0</td>
    </tr>
    <tr>
      <th>Puente de Vallecas</th>
      <td>40.0</td>
      <td>4305.0</td>
    </tr>
    <tr>
      <th>Retiro</th>
      <td>68.0</td>
      <td>5670.0</td>
    </tr>
    <tr>
      <th>Salamanca</th>
      <td>88.0</td>
      <td>6685.0</td>
    </tr>
    <tr>
      <th>San Blas - Canillejas</th>
      <td>90.0</td>
      <td>4200.0</td>
    </tr>
    <tr>
      <th>Tetuán</th>
      <td>66.0</td>
      <td>5600.0</td>
    </tr>
    <tr>
      <th>Usera</th>
      <td>42.0</td>
      <td>4585.0</td>
    </tr>
    <tr>
      <th>Vicálvaro</th>
      <td>53.0</td>
      <td>3850.0</td>
    </tr>
    <tr>
      <th>Villa de Vallecas</th>
      <td>47.5</td>
      <td>4130.0</td>
    </tr>
    <tr>
      <th>Villaverde</th>
      <td>42.0</td>
      <td>3920.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize = (16,8))
sns.scatterplot(data = temp, x = 'precio_compra', y = 'precio_total')
#Ponemos las etiquetas
for cada in range(0,temp.shape[0]):
    plt.text(temp.precio_compra[cada], temp.precio_total[cada], temp.index[cada])
```


    
![png](/static/notebooks/airbnbds4/05_Analisis%20e%20insights_files/05_Analisis%20e%20insights_19_0.png)
    


There is a clear correlation between the purchase price in each district and the price we will be able to charge.

Three clusters of low-low, medium-medium and high-high are clearly perceived.

And the exception of San Blas that we already know why it is.

Therefore, as expected, there is no clear "bargain" at this level a priori.

We are going to repeat the analysis at the neighborhood level to see if we identify anything.


```python
temp = df.groupby('neighbourhood')[['precio_total','precio_compra']].median()
temp
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
      <th>precio_total</th>
      <th>precio_compra</th>
    </tr>
    <tr>
      <th>neighbourhood</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Abrantes</th>
      <td>35.5</td>
      <td>4305.0</td>
    </tr>
    <tr>
      <th>Acacias</th>
      <td>53.8</td>
      <td>5425.0</td>
    </tr>
    <tr>
      <th>Adelfas</th>
      <td>54.0</td>
      <td>7938.0</td>
    </tr>
    <tr>
      <th>Aeropuerto</th>
      <td>41.3</td>
      <td>4235.0</td>
    </tr>
    <tr>
      <th>Aguilas</th>
      <td>47.0</td>
      <td>4375.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Valverde</th>
      <td>62.5</td>
      <td>4480.0</td>
    </tr>
    <tr>
      <th>Ventas</th>
      <td>42.0</td>
      <td>4760.0</td>
    </tr>
    <tr>
      <th>Vinateros</th>
      <td>50.0</td>
      <td>3955.0</td>
    </tr>
    <tr>
      <th>Vista Alegre</th>
      <td>50.0</td>
      <td>4305.0</td>
    </tr>
    <tr>
      <th>Zofío</th>
      <td>36.4</td>
      <td>4585.0</td>
    </tr>
  </tbody>
</table>
<p>128 rows × 2 columns</p>
</div>




```python
plt.figure(figsize = (16,20))
sns.scatterplot(data = temp, x = 'precio_compra', y = 'precio_total')
#Ponemos las etiquetas
for cada in range(0,temp.shape[0]):
    plt.text(temp.precio_compra[cada], temp.precio_total[cada], temp.index[cada])
```


    
![png](/static/notebooks/airbnbds4/05_Analisis%20e%20insights_files/05_Analisis%20e%20insights_22_0.png)
    


At this level we already see more things:

* 3 neighborhoods that stand out, possibly all 3 are from San Blas
* Within each low-medium-high group, we can begin to separate
     * Bass: Simancas, Ambroz, Marroquina, San Juan Bautista
     * Medium: El Plantio, Valdemarín, Valdefuentes
     * Medium-high: Jerónimos, Fuentela Reina
     * High: Recoletos
    
**Insight 2: There are certain neighborhoods that a priori can maximize the cost-income ratio and we can also segment it by the type of quality of the property in which we are interested in investing**


```python
df.loc[df.neighbourhood.isin(['Rosas','Canillejas','Hellin']),'distrito'].unique()
```




    array(['San Blas - Canillejas'], dtype=object)



**What factors (apart from location determine the rental price?**

To answer this question we can build a minicube, since we have discretized our analysis variables.


```python
#Paso 1: Seleccionar qué variables serán la métricas y cuales las dimensiones
metricas = ['precio_total','precio_compra']
dimensiones = ['bedrooms_disc','accommodates_disc','beds_disc','number_of_reviews_disc']

minicubo_precio = df[dimensiones + metricas]
minicubo_precio
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
      <th>bedrooms_disc</th>
      <th>accommodates_disc</th>
      <th>beds_disc</th>
      <th>number_of_reviews_disc</th>
      <th>precio_total</th>
      <th>precio_compra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01_Una</td>
      <td>0-2</td>
      <td>1</td>
      <td>48-744</td>
      <td>60.0</td>
      <td>5740.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>01_Una</td>
      <td>0-2</td>
      <td>1</td>
      <td>5-48</td>
      <td>31.0</td>
      <td>4375.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>03_Tres</td>
      <td>4-16</td>
      <td>3-24</td>
      <td>1-4</td>
      <td>50.0</td>
      <td>9765.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>01_Una</td>
      <td>0-2</td>
      <td>1</td>
      <td>5-48</td>
      <td>92.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>01_Una</td>
      <td>0-2</td>
      <td>1</td>
      <td>48-744</td>
      <td>26.0</td>
      <td>5425.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>17705</th>
      <td>01_Una</td>
      <td>0-2</td>
      <td>1</td>
      <td>1-4</td>
      <td>29.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>17706</th>
      <td>01_Una</td>
      <td>0-2</td>
      <td>1</td>
      <td>1-4</td>
      <td>29.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>17707</th>
      <td>01_Una</td>
      <td>0-2</td>
      <td>1</td>
      <td>1-4</td>
      <td>29.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>17708</th>
      <td>01_Una</td>
      <td>0-2</td>
      <td>1</td>
      <td>1-4</td>
      <td>29.0</td>
      <td>6685.0</td>
    </tr>
    <tr>
      <th>17709</th>
      <td>01_Una</td>
      <td>0-2</td>
      <td>1</td>
      <td>1-4</td>
      <td>33.0</td>
      <td>6510.0</td>
    </tr>
  </tbody>
</table>
<p>17710 rows × 6 columns</p>
</div>




```python
#Paso 2: pasar a transaccional las dimensiones
minicubo_precio = minicubo_precio.melt(id_vars=['precio_total','precio_compra'])
minicubo_precio
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
      <th>precio_total</th>
      <th>precio_compra</th>
      <th>variable</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>60.0</td>
      <td>5740.0</td>
      <td>bedrooms_disc</td>
      <td>01_Una</td>
    </tr>
    <tr>
      <th>1</th>
      <td>31.0</td>
      <td>4375.0</td>
      <td>bedrooms_disc</td>
      <td>01_Una</td>
    </tr>
    <tr>
      <th>2</th>
      <td>50.0</td>
      <td>9765.0</td>
      <td>bedrooms_disc</td>
      <td>03_Tres</td>
    </tr>
    <tr>
      <th>3</th>
      <td>92.0</td>
      <td>6510.0</td>
      <td>bedrooms_disc</td>
      <td>01_Una</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26.0</td>
      <td>5425.0</td>
      <td>bedrooms_disc</td>
      <td>01_Una</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>70835</th>
      <td>29.0</td>
      <td>6510.0</td>
      <td>number_of_reviews_disc</td>
      <td>1-4</td>
    </tr>
    <tr>
      <th>70836</th>
      <td>29.0</td>
      <td>6510.0</td>
      <td>number_of_reviews_disc</td>
      <td>1-4</td>
    </tr>
    <tr>
      <th>70837</th>
      <td>29.0</td>
      <td>6510.0</td>
      <td>number_of_reviews_disc</td>
      <td>1-4</td>
    </tr>
    <tr>
      <th>70838</th>
      <td>29.0</td>
      <td>6685.0</td>
      <td>number_of_reviews_disc</td>
      <td>1-4</td>
    </tr>
    <tr>
      <th>70839</th>
      <td>33.0</td>
      <td>6510.0</td>
      <td>number_of_reviews_disc</td>
      <td>1-4</td>
    </tr>
  </tbody>
</table>
<p>70840 rows × 4 columns</p>
</div>




```python
#Paso 3: Agregar las métricas por "variable" y "valor" con las funciones deseadas
minicubo_precio = minicubo_precio.groupby(['variable','value'])[['precio_total','precio_compra']].agg('median')
minicubo_precio
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
      <th></th>
      <th>precio_total</th>
      <th>precio_compra</th>
    </tr>
    <tr>
      <th>variable</th>
      <th>value</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">accommodates_disc</th>
      <th>0-2</th>
      <td>50.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>86.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>4-16</th>
      <td>126.0</td>
      <td>9114.0</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">bedrooms_disc</th>
      <th>01_Una</th>
      <td>56.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>02_Dos</th>
      <td>100.0</td>
      <td>9114.0</td>
    </tr>
    <tr>
      <th>03_Tres</th>
      <td>140.0</td>
      <td>11718.0</td>
    </tr>
    <tr>
      <th>04_Cuatro o mas</th>
      <td>204.0</td>
      <td>15624.0</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">beds_disc</th>
      <th>1</th>
      <td>59.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100.0</td>
      <td>9114.0</td>
    </tr>
    <tr>
      <th>3-24</th>
      <td>139.0</td>
      <td>9359.0</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">number_of_reviews_disc</th>
      <th>1-4</th>
      <td>70.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>48-744</th>
      <td>68.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>5-48</th>
      <td>69.0</td>
      <td>6510.0</td>
    </tr>
  </tbody>
</table>
</div>



On the minicube we are analyzing each variable.


```python
minicubo_precio.loc['bedrooms_disc']
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
      <th>precio_total</th>
      <th>precio_compra</th>
    </tr>
    <tr>
      <th>value</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>01_Una</th>
      <td>56.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>02_Dos</th>
      <td>100.0</td>
      <td>9114.0</td>
    </tr>
    <tr>
      <th>03_Tres</th>
      <td>140.0</td>
      <td>11718.0</td>
    </tr>
    <tr>
      <th>04_Cuatro o mas</th>
      <td>204.0</td>
      <td>15624.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
f, ax = plt.subplots()
ax.plot(minicubo_precio.loc['bedrooms_disc'].precio_total)
ax2 = ax.twinx()
ax2.plot(minicubo_precio.loc['bedrooms_disc'].precio_compra,color = 'green');
```


    
![png](/static/notebooks/airbnbds4/05_Analisis%20e%20insights_files/05_Analisis%20e%20insights_32_0.png)
    


Regarding the number of rooms, there is nothing to highlight.

There is an almost perfect relationship between the purchase price and the total price that can be charged.

Part of this effect may be artificial, since we use the number of rooms to calculate the total price as the purchase price.


```python
minicubo_precio.loc['beds_disc']
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
      <th>precio_total</th>
      <th>precio_compra</th>
    </tr>
    <tr>
      <th>value</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>59.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100.0</td>
      <td>9114.0</td>
    </tr>
    <tr>
      <th>3-24</th>
      <td>139.0</td>
      <td>9359.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
f, ax = plt.subplots()
ax.plot(minicubo_precio.loc['beds_disc'].precio_total)
ax2 = ax.twinx()
ax2.plot(minicubo_precio.loc['beds_disc'].precio_compra,color = 'green');
```


    
![png](/static/notebooks/airbnbds4/05_Analisis%20e%20insights_files/05_Analisis%20e%20insights_35_0.png)
    


Regarding the number of beds, there is a conclusion:

**Insight 3: the number of beds to avoid is 2**. Either we put a bed or we try to fit as many as possible.

Since there was no effect on the number of rooms, could it be that the owners are trying to cram in a lot more beds than rooms to maximize revenue?

Let's see it for example with the floors of a room:


```python
df[df.bedrooms == 1].groupby('beds').precio_total.median().plot();
```


    
![png](/static/notebooks/airbnbds4/05_Analisis%20e%20insights_files/05_Analisis%20e%20insights_37_0.png)
    


Indeed there is something here, since it appears that for one-room apartments there are people who are putting up to dozens of beds!

It would be a topic to explore in more detail and discuss with someone who knows the business.

Let's see some examples:


```python
df.loc[(df.bedrooms == 1)& (df.beds > 8)]
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
      <th>level_0</th>
      <th>index</th>
      <th>id</th>
      <th>name</th>
      <th>host_id</th>
      <th>neighbourhood_group</th>
      <th>neighbourhood</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>room_type</th>
      <th>price</th>
      <th>minimum_nights</th>
      <th>calculated_host_listings_count</th>
      <th>availability_365</th>
      <th>description</th>
      <th>host_is_superhost</th>
      <th>accommodates</th>
      <th>bedrooms</th>
      <th>beds</th>
      <th>number_of_reviews</th>
      <th>review_scores_rating</th>
      <th>review_scores_communication</th>
      <th>review_scores_location</th>
      <th>precio_m2</th>
      <th>distrito</th>
      <th>precio_total</th>
      <th>ocupacion</th>
      <th>bedrooms_disc</th>
      <th>accommodates_disc</th>
      <th>beds_disc</th>
      <th>number_of_reviews_disc</th>
      <th>m2</th>
      <th>precio_compra</th>
      <th>pdi_sol</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>357</th>
      <td>357</td>
      <td>357</td>
      <td>1044902</td>
      <td>Masía el Ferrajón</td>
      <td>5751753</td>
      <td>Moncloa - Aravaca</td>
      <td>Ciudad Universitaria</td>
      <td>40.46549</td>
      <td>-3.75115</td>
      <td>Private room</td>
      <td>112</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>&lt;b&gt;The space&lt;/b&gt;&lt;br /&gt;Masía el Ferrajón featur...</td>
      <td>f</td>
      <td>16</td>
      <td>1.0</td>
      <td>14.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>154</td>
      <td>Moncloa - Aravaca</td>
      <td>1097.6</td>
      <td>100</td>
      <td>01_Una</td>
      <td>4-16</td>
      <td>3-24</td>
      <td>1-4</td>
      <td>50</td>
      <td>5390.0</td>
      <td>6.767308</td>
    </tr>
    <tr>
      <th>605</th>
      <td>605</td>
      <td>605</td>
      <td>2143824</td>
      <td>The Hat Madrid - 10 people shared</td>
      <td>10940437</td>
      <td>Centro</td>
      <td>Sol</td>
      <td>40.41511</td>
      <td>-3.70804</td>
      <td>Shared room</td>
      <td>24</td>
      <td>1</td>
      <td>6</td>
      <td>364</td>
      <td>10 people shared room with shared bathroom. &lt;b...</td>
      <td>t</td>
      <td>10</td>
      <td>1.0</td>
      <td>10.0</td>
      <td>91</td>
      <td>4.57</td>
      <td>4.69</td>
      <td>4.84</td>
      <td>186</td>
      <td>Centro</td>
      <td>168.0</td>
      <td>0</td>
      <td>01_Una</td>
      <td>4-16</td>
      <td>3-24</td>
      <td>48-744</td>
      <td>50</td>
      <td>6510.0</td>
      <td>0.436897</td>
    </tr>
    <tr>
      <th>710</th>
      <td>710</td>
      <td>710</td>
      <td>3011110</td>
      <td>The Hat Madrid-Compartida 10 pers 2</td>
      <td>10940437</td>
      <td>Centro</td>
      <td>Embajadores</td>
      <td>40.41311</td>
      <td>-3.70621</td>
      <td>Shared room</td>
      <td>24</td>
      <td>1</td>
      <td>6</td>
      <td>364</td>
      <td>The Hat Madrid es el primer Boutique Hostel de...</td>
      <td>t</td>
      <td>10</td>
      <td>1.0</td>
      <td>10.0</td>
      <td>28</td>
      <td>4.56</td>
      <td>4.81</td>
      <td>4.93</td>
      <td>186</td>
      <td>Centro</td>
      <td>168.0</td>
      <td>0</td>
      <td>01_Una</td>
      <td>4-16</td>
      <td>3-24</td>
      <td>5-48</td>
      <td>50</td>
      <td>6510.0</td>
      <td>0.470155</td>
    </tr>
    <tr>
      <th>11848</th>
      <td>11848</td>
      <td>11848</td>
      <td>39600798</td>
      <td>Bed in a 10-Bed Dormitory In the Centre of Madrid</td>
      <td>304035848</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.42710</td>
      <td>-3.69912</td>
      <td>Shared room</td>
      <td>20</td>
      <td>1</td>
      <td>13</td>
      <td>351</td>
      <td>Low-key, hostel-style setup on a tree-lined st...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>10.0</td>
      <td>2</td>
      <td>5.00</td>
      <td>5.00</td>
      <td>5.00</td>
      <td>186</td>
      <td>Centro</td>
      <td>140.0</td>
      <td>3</td>
      <td>01_Una</td>
      <td>0-2</td>
      <td>3-24</td>
      <td>1-4</td>
      <td>50</td>
      <td>6510.0</td>
      <td>1.207701</td>
    </tr>
    <tr>
      <th>13340</th>
      <td>13340</td>
      <td>13340</td>
      <td>42492960</td>
      <td>Apartamento dúplex 10camas en literas</td>
      <td>338384437</td>
      <td>Tetuán</td>
      <td>Cuatro Caminos</td>
      <td>40.44959</td>
      <td>-3.70138</td>
      <td>Private room</td>
      <td>298</td>
      <td>1</td>
      <td>1</td>
      <td>364</td>
      <td>Vivienda en planta baja con 10 plazas distribu...</td>
      <td>f</td>
      <td>10</td>
      <td>1.0</td>
      <td>10.0</td>
      <td>1</td>
      <td>5.00</td>
      <td>4.00</td>
      <td>5.00</td>
      <td>160</td>
      <td>Tetuán</td>
      <td>2086.0</td>
      <td>0</td>
      <td>01_Una</td>
      <td>4-16</td>
      <td>3-24</td>
      <td>1-4</td>
      <td>50</td>
      <td>5600.0</td>
      <td>3.658902</td>
    </tr>
    <tr>
      <th>15722</th>
      <td>15722</td>
      <td>15722</td>
      <td>48855617</td>
      <td>habitaciones en una casa tranquila, en el centro</td>
      <td>194738186</td>
      <td>Salamanca</td>
      <td>Fuente del Berro</td>
      <td>40.42604</td>
      <td>-3.66373</td>
      <td>Private room</td>
      <td>36</td>
      <td>2</td>
      <td>1</td>
      <td>359</td>
      <td>Es una casa que tiene dos habitaciones que se ...</td>
      <td>f</td>
      <td>5</td>
      <td>1.0</td>
      <td>9.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>191</td>
      <td>Salamanca</td>
      <td>226.8</td>
      <td>1</td>
      <td>01_Una</td>
      <td>4-16</td>
      <td>3-24</td>
      <td>1-4</td>
      <td>50</td>
      <td>6685.0</td>
      <td>3.510206</td>
    </tr>
  </tbody>
</table>
</div>



Vamos a analizar ahora por el número de huéspedes que aceptan


```python
minicubo_precio.loc['accommodates_disc']
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
      <th>precio_total</th>
      <th>precio_compra</th>
    </tr>
    <tr>
      <th>value</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0-2</th>
      <td>50.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>86.0</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>4-16</th>
      <td>126.0</td>
      <td>9114.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
f, ax = plt.subplots()
ax.plot(minicubo_precio.loc['accommodates_disc'].precio_total)
ax2 = ax.twinx()
ax2.plot(minicubo_precio.loc['accommodates_disc'].precio_compra,color = 'green');
```


    
![png](/static/notebooks/airbnbds4/05_Analisis%20e%20insights_files/05_Analisis%20e%20insights_42_0.png)
    


**Insight 4: the optimal number of guests is 3, since the price of the properties to accommodate 3 is the same as to accommodate 1 or 2. From 4 the floor needs to be larger and the purchase price increases a lot **

Finally we are going to analyze the variable that we have built of proximity to a point of interest to see if it has an effect on the price of the rooms.

In a real situation we would have built many of this type, and repeated the analysis with all of them.

In this case, as we have built the distance to Puerta del Sol, we are going to evaluate only the districts for which this may be relevant, that is, the most central ones.

To do this, we will first calculate the average distance per district and choose a cut-off point.


```python
df.groupby('distrito').pdi_sol.median().sort_values()
```




    distrito
    Centro                    0.728581
    Arganzuela                1.817840
    Chamberí                  2.078790
    Moncloa - Aravaca         2.130135
    Retiro                    2.415432
    Salamanca                 2.705209
    Latina                    3.496952
    Carabanchel               3.647956
    Usera                     3.661376
    Chamartín                 4.233216
    Puente de Vallecas        4.233631
    Tetuán                    4.572866
    Ciudad Lineal             5.170226
    Moratalaz                 5.242395
    Villaverde                7.579665
    Fuencarral - El Pardo     7.738933
    San Blas - Canillejas     7.962141
    Hortaleza                 8.132864
    Vicálvaro                 8.396723
    Villa de Vallecas         8.822907
    Barajas                  11.593340
    Name: pdi_sol, dtype: float64



Let's cut in Latina included.

And on that selection we are going to visualize with a scatter.


```python
df.groupby('distrito').pdi_sol.median().sort_values()[0:7].index.to_list()
```




    ['Centro',
     'Arganzuela',
     'Chamberí',
     'Moncloa - Aravaca',
     'Retiro',
     'Salamanca',
     'Latina']




```python
seleccion = df.groupby('distrito').pdi_sol.median().sort_values()[0:7].index.to_list()

plt.figure(figsize = (16,12))
sns.scatterplot(data = df.loc[df.distrito.isin(seleccion)], x = 'pdi_sol', y = 'precio_total');
```


    
![png](/static/notebooks/airbnbds4/05_Analisis%20e%20insights_files/05_Analisis%20e%20insights_48_0.png)
    


There does not seem to be as direct a relationship as would be expected between the distance to Puerta del Sol and the rental price.

**Insight 5: being within the district it seems that the proximity to points of interest does not have as much impact as would be expected. This opens the door to looking for properties that, being in a central district, are not right next to the PoI and therefore hopefully have a lower purchase price**

### Analysis of occupation

At this point, we could repeat exactly the same analysis as with the price, but changing the price variable for the occupancy variable that we had built.

Since it would be the same, we are not going to develop it and I will leave it as a homework for you to practice and try to get your first insights.

Instead I prefer the time to show you how we can include analysis on a map, since in this case it would be something very relevant and it is a type of analysis that is always very popular.

### Geographic analysis on a map

```python
import folium
```

We are going to use the coordinates of the Puerta del Sol that we already had as the center point of the map.

For example, we are going to visually analyze the insight on the San Blas district.

```python
datos = df[df.distrito == 'San Blas - Canillejas'].copy()
```

To represent the markers of all the floors we have to create a loop to add them to the map.

We are going also to add some color legend to see which is the price range.
```python
datos['precio_total_disc'] = pd.qcut(datos['precio_total'], q = [0, .25, .5, .75, 1.], 
                              labels=['yellow', 'orange', 'blue', 'red'])
```


```python
mapa = folium.Map(location=[40.4167278, -3.7033387],zoom_start=12)

for piso in range(0,len(datos)):
   folium.CircleMarker(
      location = [datos.iloc[piso]['latitude'], datos.iloc[piso]['longitude']],
      popup = datos.iloc[piso]['precio_total'],
      fill=True,
      color = datos.iloc[piso]['precio_total_disc'],
      fill_opacity=1,
      radius = 5
   ).add_to(mapa)

mapa
```

<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;head&gt;    
    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_a8516ba71be4178f04e6dd1586315ef3 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;    

            &lt;div class=&quot;folium-map&quot; id=&quot;map_a8516ba71be4178f04e6dd1586315ef3&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;    

            var map_a8516ba71be4178f04e6dd1586315ef3 = L.map(
                &quot;map_a8516ba71be4178f04e6dd1586315ef3&quot;,
                {
                    center: [40.4167278, -3.7033387],
                    crs: L.CRS.EPSG3857,
                    zoom: 12,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_8092c898f5636e15d0957ce13ddb18f6 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


            var circle_marker_b57f53c5992b5cf10bc2ccfb00d67fc9 = L.circleMarker(
                [40.43202, -3.60353],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_456540b4cb562891cadaf31dd7a4ea20 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_98e64e34d9da9be24775d6233b044f88 = $(`&lt;div id=&quot;html_98e64e34d9da9be24775d6233b044f88&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;36.0&lt;/div&gt;`)[0];
            popup_456540b4cb562891cadaf31dd7a4ea20.setContent(html_98e64e34d9da9be24775d6233b044f88);


        circle_marker_b57f53c5992b5cf10bc2ccfb00d67fc9.bindPopup(popup_456540b4cb562891cadaf31dd7a4ea20)
        ;




            var circle_marker_74df851bec3f059f76c147015fb516f6 = L.circleMarker(
                [40.42756, -3.61577],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_481119b5c470f5df5f2794fa0811dd26 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_cc416224170e983e91ecea7d1cf2909c = $(`&lt;div id=&quot;html_cc416224170e983e91ecea7d1cf2909c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;29.4&lt;/div&gt;`)[0];
            popup_481119b5c470f5df5f2794fa0811dd26.setContent(html_cc416224170e983e91ecea7d1cf2909c);


        circle_marker_74df851bec3f059f76c147015fb516f6.bindPopup(popup_481119b5c470f5df5f2794fa0811dd26)
        ;




            var circle_marker_2847e3300fa47d6b4ffbce566c728e95 = L.circleMarker(
                [40.42761, -3.6158],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_575b61b6a213bfa0fe474e5535de1b93 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_89b4e8ebfa130b78e124d75b0f2aedd2 = $(`&lt;div id=&quot;html_89b4e8ebfa130b78e124d75b0f2aedd2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;29.4&lt;/div&gt;`)[0];
            popup_575b61b6a213bfa0fe474e5535de1b93.setContent(html_89b4e8ebfa130b78e124d75b0f2aedd2);


        circle_marker_2847e3300fa47d6b4ffbce566c728e95.bindPopup(popup_575b61b6a213bfa0fe474e5535de1b93)
        ;




            var circle_marker_704f4a1faaa73143796094749ec82b39 = L.circleMarker(
                [40.4267, -3.61631],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4e07382259b3095f43a76c4b5e900659 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0767683e879aefce652c9a53fa9b194f = $(`&lt;div id=&quot;html_0767683e879aefce652c9a53fa9b194f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;21.0&lt;/div&gt;`)[0];
            popup_4e07382259b3095f43a76c4b5e900659.setContent(html_0767683e879aefce652c9a53fa9b194f);


        circle_marker_704f4a1faaa73143796094749ec82b39.bindPopup(popup_4e07382259b3095f43a76c4b5e900659)
        ;




            var circle_marker_ed6e186240977016ef8930b517cb2d1f = L.circleMarker(
                [40.44791, -3.57918],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8d668091c718c9a0cfba4c4302dc0412 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ad9df672ab5216e53cf2d5cafc08b720 = $(`&lt;div id=&quot;html_ad9df672ab5216e53cf2d5cafc08b720&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;85.0&lt;/div&gt;`)[0];
            popup_8d668091c718c9a0cfba4c4302dc0412.setContent(html_ad9df672ab5216e53cf2d5cafc08b720);


        circle_marker_ed6e186240977016ef8930b517cb2d1f.bindPopup(popup_8d668091c718c9a0cfba4c4302dc0412)
        ;




            var circle_marker_adefe0a077b1a5b13bbfc2d3395b3d71 = L.circleMarker(
                [40.44655, -3.58128],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_44979e6ebe1cadd9e6af7a10e9285a9a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_415f4eb51d1b34b6380e6d324df58953 = $(`&lt;div id=&quot;html_415f4eb51d1b34b6380e6d324df58953&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;57.0&lt;/div&gt;`)[0];
            popup_44979e6ebe1cadd9e6af7a10e9285a9a.setContent(html_415f4eb51d1b34b6380e6d324df58953);


        circle_marker_adefe0a077b1a5b13bbfc2d3395b3d71.bindPopup(popup_44979e6ebe1cadd9e6af7a10e9285a9a)
        ;




            var circle_marker_44ec65046df767b35b36ae67d2574ac1 = L.circleMarker(
                [40.43602, -3.63506],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f3c149c6b4d76736bd42a29c917b14d8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a244d63276df0c5d6f7b0d9cfe1e729b = $(`&lt;div id=&quot;html_a244d63276df0c5d6f7b0d9cfe1e729b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;51.0&lt;/div&gt;`)[0];
            popup_f3c149c6b4d76736bd42a29c917b14d8.setContent(html_a244d63276df0c5d6f7b0d9cfe1e729b);


        circle_marker_44ec65046df767b35b36ae67d2574ac1.bindPopup(popup_f3c149c6b4d76736bd42a29c917b14d8)
        ;




            var circle_marker_450d5377a28b7bf4bb98bd88518a1208 = L.circleMarker(
                [40.4403, -3.63464],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ee461ea11f0b71ac3c207233149fffde = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a6ae273fd349b8f7351a15fa72ee23f5 = $(`&lt;div id=&quot;html_a6ae273fd349b8f7351a15fa72ee23f5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.0&lt;/div&gt;`)[0];
            popup_ee461ea11f0b71ac3c207233149fffde.setContent(html_a6ae273fd349b8f7351a15fa72ee23f5);


        circle_marker_450d5377a28b7bf4bb98bd88518a1208.bindPopup(popup_ee461ea11f0b71ac3c207233149fffde)
        ;




            var circle_marker_9f64c43e87c98d22c72570e543fa2766 = L.circleMarker(
                [40.44214, -3.63756],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_2f34d30bd46dbee3fbc39c313fb1cff1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_3ac7790fd5427109f5c994df92e02edc = $(`&lt;div id=&quot;html_3ac7790fd5427109f5c994df92e02edc&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;32.0&lt;/div&gt;`)[0];
            popup_2f34d30bd46dbee3fbc39c313fb1cff1.setContent(html_3ac7790fd5427109f5c994df92e02edc);


        circle_marker_9f64c43e87c98d22c72570e543fa2766.bindPopup(popup_2f34d30bd46dbee3fbc39c313fb1cff1)
        ;




            var circle_marker_bc955bd18dc8f93155978d83b9651ed3 = L.circleMarker(
                [40.4449, -3.63508],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3ed51b7d6548f3649a2603cc88f934ab = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1cd42588f852312d21f5cd395bfed324 = $(`&lt;div id=&quot;html_1cd42588f852312d21f5cd395bfed324&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;42.0&lt;/div&gt;`)[0];
            popup_3ed51b7d6548f3649a2603cc88f934ab.setContent(html_1cd42588f852312d21f5cd395bfed324);


        circle_marker_bc955bd18dc8f93155978d83b9651ed3.bindPopup(popup_3ed51b7d6548f3649a2603cc88f934ab)
        ;




            var circle_marker_042788ab874480738461e7af08f33d02 = L.circleMarker(
                [40.41909, -3.61418],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9d756a5b3245c565e332242ffa0adb8d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_adbfeae1ab9148c7ae4c400a77302839 = $(`&lt;div id=&quot;html_adbfeae1ab9148c7ae4c400a77302839&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;60.0&lt;/div&gt;`)[0];
            popup_9d756a5b3245c565e332242ffa0adb8d.setContent(html_adbfeae1ab9148c7ae4c400a77302839);


        circle_marker_042788ab874480738461e7af08f33d02.bindPopup(popup_9d756a5b3245c565e332242ffa0adb8d)
        ;




            var circle_marker_702bd39c8ab6c55f166234af91103d25 = L.circleMarker(
                [40.44544, -3.5861],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_56988413742658b1c4c2514206e49fe5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_cff756876f9ff03c7ee0bb7e34fe98d8 = $(`&lt;div id=&quot;html_cff756876f9ff03c7ee0bb7e34fe98d8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_56988413742658b1c4c2514206e49fe5.setContent(html_cff756876f9ff03c7ee0bb7e34fe98d8);


        circle_marker_702bd39c8ab6c55f166234af91103d25.bindPopup(popup_56988413742658b1c4c2514206e49fe5)
        ;




            var circle_marker_5eb8dd0d81116caaa23cdf707fc94ed7 = L.circleMarker(
                [40.44033, -3.61872],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9f12b0d6dc1987d45a9d758878d07f37 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a4d75e803311e75862d08f96c75cd302 = $(`&lt;div id=&quot;html_a4d75e803311e75862d08f96c75cd302&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;85.0&lt;/div&gt;`)[0];
            popup_9f12b0d6dc1987d45a9d758878d07f37.setContent(html_a4d75e803311e75862d08f96c75cd302);


        circle_marker_5eb8dd0d81116caaa23cdf707fc94ed7.bindPopup(popup_9f12b0d6dc1987d45a9d758878d07f37)
        ;




            var circle_marker_87c83a9a7435984cb532a9d56d01c550 = L.circleMarker(
                [40.42781, -3.61522],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_6b548f6b463fff718e35180bed9171f1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_28badd92cb614147ab9b80ea0c4f94d1 = $(`&lt;div id=&quot;html_28badd92cb614147ab9b80ea0c4f94d1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;29.4&lt;/div&gt;`)[0];
            popup_6b548f6b463fff718e35180bed9171f1.setContent(html_28badd92cb614147ab9b80ea0c4f94d1);


        circle_marker_87c83a9a7435984cb532a9d56d01c550.bindPopup(popup_6b548f6b463fff718e35180bed9171f1)
        ;




            var circle_marker_a4a7bac8313896c52c32b265a6a14ce0 = L.circleMarker(
                [40.43857, -3.61918],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_37c180d3b098847958acfb2d4804f11c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ba55a14da1812ba3845c024286eec093 = $(`&lt;div id=&quot;html_ba55a14da1812ba3845c024286eec093&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;36.0&lt;/div&gt;`)[0];
            popup_37c180d3b098847958acfb2d4804f11c.setContent(html_ba55a14da1812ba3845c024286eec093);


        circle_marker_a4a7bac8313896c52c32b265a6a14ce0.bindPopup(popup_37c180d3b098847958acfb2d4804f11c)
        ;




            var circle_marker_3365b4142584e043d48465a5e7097427 = L.circleMarker(
                [40.44597, -3.63157],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e04f05ca855d4d2bbc9989f7046157df = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_58ac99fb58fd5581f57abc3cd1dd5096 = $(`&lt;div id=&quot;html_58ac99fb58fd5581f57abc3cd1dd5096&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;55.0&lt;/div&gt;`)[0];
            popup_e04f05ca855d4d2bbc9989f7046157df.setContent(html_58ac99fb58fd5581f57abc3cd1dd5096);


        circle_marker_3365b4142584e043d48465a5e7097427.bindPopup(popup_e04f05ca855d4d2bbc9989f7046157df)
        ;




            var circle_marker_f30182297df38de85a4c180c08ce460c = L.circleMarker(
                [40.44805, -3.60888],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d79d9b703ab0d11c6cc06e322a30e0e2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_686f1a5a060c858283f49844acf6508a = $(`&lt;div id=&quot;html_686f1a5a060c858283f49844acf6508a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;38.0&lt;/div&gt;`)[0];
            popup_d79d9b703ab0d11c6cc06e322a30e0e2.setContent(html_686f1a5a060c858283f49844acf6508a);


        circle_marker_f30182297df38de85a4c180c08ce460c.bindPopup(popup_d79d9b703ab0d11c6cc06e322a30e0e2)
        ;




            var circle_marker_ffd9d9730685d288e54ac26d3e3978cf = L.circleMarker(
                [40.43715, -3.63231],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_6115ee46ac2394fd95f9ffa986b8928c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9c122e997b92639fc7ade14dc8a441f0 = $(`&lt;div id=&quot;html_9c122e997b92639fc7ade14dc8a441f0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;76.0&lt;/div&gt;`)[0];
            popup_6115ee46ac2394fd95f9ffa986b8928c.setContent(html_9c122e997b92639fc7ade14dc8a441f0);


        circle_marker_ffd9d9730685d288e54ac26d3e3978cf.bindPopup(popup_6115ee46ac2394fd95f9ffa986b8928c)
        ;




            var circle_marker_1fbdd7251c3a1e611e4b9f11a6a2c486 = L.circleMarker(
                [40.43997, -3.61707],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_36fe652b1d764dcde103cd824731d974 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_13a3418e0cd5ebdd247f1a8fc9005562 = $(`&lt;div id=&quot;html_13a3418e0cd5ebdd247f1a8fc9005562&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;80.0&lt;/div&gt;`)[0];
            popup_36fe652b1d764dcde103cd824731d974.setContent(html_13a3418e0cd5ebdd247f1a8fc9005562);


        circle_marker_1fbdd7251c3a1e611e4b9f11a6a2c486.bindPopup(popup_36fe652b1d764dcde103cd824731d974)
        ;




            var circle_marker_8eb8fd4dff52d4a6edae19c9739ff484 = L.circleMarker(
                [40.44121, -3.63667],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a3678317cc0bf79a2ee4b390e0657854 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b19be9529abc1183f239e9e80e3d962e = $(`&lt;div id=&quot;html_b19be9529abc1183f239e9e80e3d962e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;67.0&lt;/div&gt;`)[0];
            popup_a3678317cc0bf79a2ee4b390e0657854.setContent(html_b19be9529abc1183f239e9e80e3d962e);


        circle_marker_8eb8fd4dff52d4a6edae19c9739ff484.bindPopup(popup_a3678317cc0bf79a2ee4b390e0657854)
        ;




            var circle_marker_62311c7358ea98b4840ed9b51d80450b = L.circleMarker(
                [40.42609, -3.60935],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ccee145dd87e81a797ed6b7b8f2b1680 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7249ca29fd7472ae030d74439545ccfe = $(`&lt;div id=&quot;html_7249ca29fd7472ae030d74439545ccfe&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;25.0&lt;/div&gt;`)[0];
            popup_ccee145dd87e81a797ed6b7b8f2b1680.setContent(html_7249ca29fd7472ae030d74439545ccfe);


        circle_marker_62311c7358ea98b4840ed9b51d80450b.bindPopup(popup_ccee145dd87e81a797ed6b7b8f2b1680)
        ;




            var circle_marker_83a78f4f4c5ae2af1a59fb615adb624e = L.circleMarker(
                [40.43869, -3.624],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a0be59aa21d97785e33c1c429a46597b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2a98927181fd9e09172cfac0db13fdc5 = $(`&lt;div id=&quot;html_2a98927181fd9e09172cfac0db13fdc5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;55.0&lt;/div&gt;`)[0];
            popup_a0be59aa21d97785e33c1c429a46597b.setContent(html_2a98927181fd9e09172cfac0db13fdc5);


        circle_marker_83a78f4f4c5ae2af1a59fb615adb624e.bindPopup(popup_a0be59aa21d97785e33c1c429a46597b)
        ;




            var circle_marker_61aa3ae69fa073b113665600401c7ff2 = L.circleMarker(
                [40.44468, -3.58021],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a8f95db3113cf0713969a361b914ffbf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_53227a13dae65af758bb93df3a7efc52 = $(`&lt;div id=&quot;html_53227a13dae65af758bb93df3a7efc52&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;82.0&lt;/div&gt;`)[0];
            popup_a8f95db3113cf0713969a361b914ffbf.setContent(html_53227a13dae65af758bb93df3a7efc52);


        circle_marker_61aa3ae69fa073b113665600401c7ff2.bindPopup(popup_a8f95db3113cf0713969a361b914ffbf)
        ;




            var circle_marker_5cf7d50a19870c51000312ba2448bc9c = L.circleMarker(
                [40.4197, -3.61808],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4d7d03a338f201e7afb7f4663f1a355f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_bd7fc5e6ed72a806ef469b260e3fba03 = $(`&lt;div id=&quot;html_bd7fc5e6ed72a806ef469b260e3fba03&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;163.0&lt;/div&gt;`)[0];
            popup_4d7d03a338f201e7afb7f4663f1a355f.setContent(html_bd7fc5e6ed72a806ef469b260e3fba03);


        circle_marker_5cf7d50a19870c51000312ba2448bc9c.bindPopup(popup_4d7d03a338f201e7afb7f4663f1a355f)
        ;




            var circle_marker_df538da6e1e4712383def28db356466a = L.circleMarker(
                [40.44293, -3.57959],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e3fc6341f43c32bf52dbb311e38f2402 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_04a21f0f72acf724278d3e364b619d5d = $(`&lt;div id=&quot;html_04a21f0f72acf724278d3e364b619d5d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;63.0&lt;/div&gt;`)[0];
            popup_e3fc6341f43c32bf52dbb311e38f2402.setContent(html_04a21f0f72acf724278d3e364b619d5d);


        circle_marker_df538da6e1e4712383def28db356466a.bindPopup(popup_e3fc6341f43c32bf52dbb311e38f2402)
        ;




            var circle_marker_214e830e2f3be03dbcaed4c9e289d2a1 = L.circleMarker(
                [40.44037, -3.6251],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_65e14acd30764fec70ca7c25b8aee607 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_829d8e158f42d7336735ca59463dfe60 = $(`&lt;div id=&quot;html_829d8e158f42d7336735ca59463dfe60&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;55.0&lt;/div&gt;`)[0];
            popup_65e14acd30764fec70ca7c25b8aee607.setContent(html_829d8e158f42d7336735ca59463dfe60);


        circle_marker_214e830e2f3be03dbcaed4c9e289d2a1.bindPopup(popup_65e14acd30764fec70ca7c25b8aee607)
        ;




            var circle_marker_f949dc9d61b0b7d45354c7f1d9e0aacc = L.circleMarker(
                [40.43731, -3.62278],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_40f1c8503c2be9f64f00b73c4924ee3b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b433af0a710611be4257b8904bd6dba7 = $(`&lt;div id=&quot;html_b433af0a710611be4257b8904bd6dba7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;60.0&lt;/div&gt;`)[0];
            popup_40f1c8503c2be9f64f00b73c4924ee3b.setContent(html_b433af0a710611be4257b8904bd6dba7);


        circle_marker_f949dc9d61b0b7d45354c7f1d9e0aacc.bindPopup(popup_40f1c8503c2be9f64f00b73c4924ee3b)
        ;




            var circle_marker_128e3892ee63c2c576747705b38e10ee = L.circleMarker(
                [40.43972, -3.62306],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_553b385bc47a89152248076c08126c6b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2b4a2e0f7d5270aeaa2594d08d4d6c69 = $(`&lt;div id=&quot;html_2b4a2e0f7d5270aeaa2594d08d4d6c69&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_553b385bc47a89152248076c08126c6b.setContent(html_2b4a2e0f7d5270aeaa2594d08d4d6c69);


        circle_marker_128e3892ee63c2c576747705b38e10ee.bindPopup(popup_553b385bc47a89152248076c08126c6b)
        ;




            var circle_marker_ee9ee9923c02c9c3b1a6dc3283d8bef4 = L.circleMarker(
                [40.4443, -3.58335],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b047a1891bf4dea0526b9f57661a1d91 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6df6cded48101b6fbf62bab11b2c9972 = $(`&lt;div id=&quot;html_6df6cded48101b6fbf62bab11b2c9972&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;32.0&lt;/div&gt;`)[0];
            popup_b047a1891bf4dea0526b9f57661a1d91.setContent(html_6df6cded48101b6fbf62bab11b2c9972);


        circle_marker_ee9ee9923c02c9c3b1a6dc3283d8bef4.bindPopup(popup_b047a1891bf4dea0526b9f57661a1d91)
        ;




            var circle_marker_f424a6ec60c9f632c29714ffa0a3e63e = L.circleMarker(
                [40.43263, -3.60358],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b96509398db67eda8820691177206dfb = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9626ab5b878a2e5e5dc47ddd78a48764 = $(`&lt;div id=&quot;html_9626ab5b878a2e5e5dc47ddd78a48764&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;25.0&lt;/div&gt;`)[0];
            popup_b96509398db67eda8820691177206dfb.setContent(html_9626ab5b878a2e5e5dc47ddd78a48764);


        circle_marker_f424a6ec60c9f632c29714ffa0a3e63e.bindPopup(popup_b96509398db67eda8820691177206dfb)
        ;




            var circle_marker_8dce799aaf3fd26202707e9c9dc3cec7 = L.circleMarker(
                [40.44614, -3.5872],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ff929e82d1f43c5548d6af58089a04f8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_61c30982fd04653a6589c440e5b59506 = $(`&lt;div id=&quot;html_61c30982fd04653a6589c440e5b59506&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;56.0&lt;/div&gt;`)[0];
            popup_ff929e82d1f43c5548d6af58089a04f8.setContent(html_61c30982fd04653a6589c440e5b59506);


        circle_marker_8dce799aaf3fd26202707e9c9dc3cec7.bindPopup(popup_ff929e82d1f43c5548d6af58089a04f8)
        ;




            var circle_marker_3e78f88b32ef003f63cafa8d3609cdf3 = L.circleMarker(
                [40.43225, -3.62502],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_1078099c3880596a105b22b908ee39a2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_698f619e5ae5cba5d4d7149ed1ec2fa2 = $(`&lt;div id=&quot;html_698f619e5ae5cba5d4d7149ed1ec2fa2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;65.0&lt;/div&gt;`)[0];
            popup_1078099c3880596a105b22b908ee39a2.setContent(html_698f619e5ae5cba5d4d7149ed1ec2fa2);


        circle_marker_3e78f88b32ef003f63cafa8d3609cdf3.bindPopup(popup_1078099c3880596a105b22b908ee39a2)
        ;




            var circle_marker_7c26bc7a69592bd77baa3a84923e04a3 = L.circleMarker(
                [40.43184, -3.62333],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_7f6f1d21b7312870c35a6327570abfaf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_774ccb200661037a746e0c63e4ae327b = $(`&lt;div id=&quot;html_774ccb200661037a746e0c63e4ae327b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;46.0&lt;/div&gt;`)[0];
            popup_7f6f1d21b7312870c35a6327570abfaf.setContent(html_774ccb200661037a746e0c63e4ae327b);


        circle_marker_7c26bc7a69592bd77baa3a84923e04a3.bindPopup(popup_7f6f1d21b7312870c35a6327570abfaf)
        ;




            var circle_marker_45c0554e55909a2f95c6cc8910c5441c = L.circleMarker(
                [40.44626, -3.5853],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5c5ecec53bbef5a7df9a469492572f67 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_386600b5b9797f87e7b108b9730f6e19 = $(`&lt;div id=&quot;html_386600b5b9797f87e7b108b9730f6e19&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;40.0&lt;/div&gt;`)[0];
            popup_5c5ecec53bbef5a7df9a469492572f67.setContent(html_386600b5b9797f87e7b108b9730f6e19);


        circle_marker_45c0554e55909a2f95c6cc8910c5441c.bindPopup(popup_5c5ecec53bbef5a7df9a469492572f67)
        ;




            var circle_marker_b754f835b668112f26890180b7ccc97f = L.circleMarker(
                [40.44472, -3.58884],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b1ae6255a1145dac3326cea9221eb1d3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_c79d76c6b069ad74f7506973dd90aa4b = $(`&lt;div id=&quot;html_c79d76c6b069ad74f7506973dd90aa4b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;83.0&lt;/div&gt;`)[0];
            popup_b1ae6255a1145dac3326cea9221eb1d3.setContent(html_c79d76c6b069ad74f7506973dd90aa4b);


        circle_marker_b754f835b668112f26890180b7ccc97f.bindPopup(popup_b1ae6255a1145dac3326cea9221eb1d3)
        ;




            var circle_marker_79929a21893e82b592a487ee5ed0cb98 = L.circleMarker(
                [40.43765, -3.62672],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_61fb914315dda0dd64f2c5d3ba62ffe7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_23819a5522409b67e84f56a47bef7522 = $(`&lt;div id=&quot;html_23819a5522409b67e84f56a47bef7522&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_61fb914315dda0dd64f2c5d3ba62ffe7.setContent(html_23819a5522409b67e84f56a47bef7522);


        circle_marker_79929a21893e82b592a487ee5ed0cb98.bindPopup(popup_61fb914315dda0dd64f2c5d3ba62ffe7)
        ;




            var circle_marker_3f222ea8afdecc92e8c97f8371ef0c77 = L.circleMarker(
                [40.43112, -3.62941],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_42fe6df0b7bdbba20722048097b6e2b5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0804db10ce03e55abee36d3d779c30bb = $(`&lt;div id=&quot;html_0804db10ce03e55abee36d3d779c30bb&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;23.0&lt;/div&gt;`)[0];
            popup_42fe6df0b7bdbba20722048097b6e2b5.setContent(html_0804db10ce03e55abee36d3d779c30bb);


        circle_marker_3f222ea8afdecc92e8c97f8371ef0c77.bindPopup(popup_42fe6df0b7bdbba20722048097b6e2b5)
        ;




            var circle_marker_dcb52f3997f502b8de078ceda05a652e = L.circleMarker(
                [40.4352, -3.61977],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_491644ad63687c3bc3a5f463ee1409fd = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_867c7abcd05d9cf74b0d91f7cc146e10 = $(`&lt;div id=&quot;html_867c7abcd05d9cf74b0d91f7cc146e10&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;420.0&lt;/div&gt;`)[0];
            popup_491644ad63687c3bc3a5f463ee1409fd.setContent(html_867c7abcd05d9cf74b0d91f7cc146e10);


        circle_marker_dcb52f3997f502b8de078ceda05a652e.bindPopup(popup_491644ad63687c3bc3a5f463ee1409fd)
        ;




            var circle_marker_1c9d5ed1c9705552ac7ea313ac8fb6b8 = L.circleMarker(
                [40.43795, -3.63676],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5dc137902f67a88a5ccd596e47c4d076 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_545e1da9e979d3ad6b9b3ac013b01da6 = $(`&lt;div id=&quot;html_545e1da9e979d3ad6b9b3ac013b01da6&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;97.0&lt;/div&gt;`)[0];
            popup_5dc137902f67a88a5ccd596e47c4d076.setContent(html_545e1da9e979d3ad6b9b3ac013b01da6);


        circle_marker_1c9d5ed1c9705552ac7ea313ac8fb6b8.bindPopup(popup_5dc137902f67a88a5ccd596e47c4d076)
        ;




            var circle_marker_1ead43a3280ab7a152528f3212ad5188 = L.circleMarker(
                [40.41974, -3.61898],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_6c8c83a83a732c0db567ef5392693dd4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_67b4d71d9d12588ec83b3c3375baea65 = $(`&lt;div id=&quot;html_67b4d71d9d12588ec83b3c3375baea65&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;29.0&lt;/div&gt;`)[0];
            popup_6c8c83a83a732c0db567ef5392693dd4.setContent(html_67b4d71d9d12588ec83b3c3375baea65);


        circle_marker_1ead43a3280ab7a152528f3212ad5188.bindPopup(popup_6c8c83a83a732c0db567ef5392693dd4)
        ;




            var circle_marker_37f84d0ca2791e3a0c2d9e958e63874e = L.circleMarker(
                [40.44336, -3.5754],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b4d0bf78ce0c976655622bb36ceabb23 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d37ea30d2aa07f79afdef39b8b64d3fc = $(`&lt;div id=&quot;html_d37ea30d2aa07f79afdef39b8b64d3fc&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;69.0&lt;/div&gt;`)[0];
            popup_b4d0bf78ce0c976655622bb36ceabb23.setContent(html_d37ea30d2aa07f79afdef39b8b64d3fc);


        circle_marker_37f84d0ca2791e3a0c2d9e958e63874e.bindPopup(popup_b4d0bf78ce0c976655622bb36ceabb23)
        ;




            var circle_marker_1fb8bfab0e2752ee98c9200a82dc5275 = L.circleMarker(
                [40.44148, -3.60867],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f12a7de0ef3c4d0b9c14706f009d2f96 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_721b20cc6872b3725ed19595d15d0a9e = $(`&lt;div id=&quot;html_721b20cc6872b3725ed19595d15d0a9e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;137.2&lt;/div&gt;`)[0];
            popup_f12a7de0ef3c4d0b9c14706f009d2f96.setContent(html_721b20cc6872b3725ed19595d15d0a9e);


        circle_marker_1fb8bfab0e2752ee98c9200a82dc5275.bindPopup(popup_f12a7de0ef3c4d0b9c14706f009d2f96)
        ;




            var circle_marker_ae7c0f57bb162173d186d256404ab0b4 = L.circleMarker(
                [40.43491, -3.61782],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_883a63e4b65ca0c7ef29cc6795ee0395 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ad92084bf25ad517cea1a4206efbbc18 = $(`&lt;div id=&quot;html_ad92084bf25ad517cea1a4206efbbc18&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;25.0&lt;/div&gt;`)[0];
            popup_883a63e4b65ca0c7ef29cc6795ee0395.setContent(html_ad92084bf25ad517cea1a4206efbbc18);


        circle_marker_ae7c0f57bb162173d186d256404ab0b4.bindPopup(popup_883a63e4b65ca0c7ef29cc6795ee0395)
        ;




            var circle_marker_3f4d6e911597b1699b3e42554a6b0da4 = L.circleMarker(
                [40.44917, -3.61064],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_93114db2c40b88be9bb2d6e878081efc = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1d14e6129b89c8a674d5bbd09c1e63b4 = $(`&lt;div id=&quot;html_1d14e6129b89c8a674d5bbd09c1e63b4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;140.0&lt;/div&gt;`)[0];
            popup_93114db2c40b88be9bb2d6e878081efc.setContent(html_1d14e6129b89c8a674d5bbd09c1e63b4);


        circle_marker_3f4d6e911597b1699b3e42554a6b0da4.bindPopup(popup_93114db2c40b88be9bb2d6e878081efc)
        ;




            var circle_marker_2f39def28953c6585f0831d9e3def136 = L.circleMarker(
                [40.44366, -3.63272],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a3eaa4e9b959a7d0aea4ebe4988f052b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0c8715c5d16654aa7c4565f30006c3ec = $(`&lt;div id=&quot;html_0c8715c5d16654aa7c4565f30006c3ec&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;28.0&lt;/div&gt;`)[0];
            popup_a3eaa4e9b959a7d0aea4ebe4988f052b.setContent(html_0c8715c5d16654aa7c4565f30006c3ec);


        circle_marker_2f39def28953c6585f0831d9e3def136.bindPopup(popup_a3eaa4e9b959a7d0aea4ebe4988f052b)
        ;




            var circle_marker_71bb6111c5dc65818918f119208124f8 = L.circleMarker(
                [40.43985, -3.62632],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_fa3e02e895e48151a2dd3a35844792a4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_bc257ccba50d2043c433a5aa1055c736 = $(`&lt;div id=&quot;html_bc257ccba50d2043c433a5aa1055c736&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;46.0&lt;/div&gt;`)[0];
            popup_fa3e02e895e48151a2dd3a35844792a4.setContent(html_bc257ccba50d2043c433a5aa1055c736);


        circle_marker_71bb6111c5dc65818918f119208124f8.bindPopup(popup_fa3e02e895e48151a2dd3a35844792a4)
        ;




            var circle_marker_f1e89018925f4eb6770f437affd179f2 = L.circleMarker(
                [40.43623, -3.62453],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_56b36c1c9fde88c5824b3db2e6673a18 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6f531f8a126cad13e583030e48fad28f = $(`&lt;div id=&quot;html_6f531f8a126cad13e583030e48fad28f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;150.0&lt;/div&gt;`)[0];
            popup_56b36c1c9fde88c5824b3db2e6673a18.setContent(html_6f531f8a126cad13e583030e48fad28f);


        circle_marker_f1e89018925f4eb6770f437affd179f2.bindPopup(popup_56b36c1c9fde88c5824b3db2e6673a18)
        ;




            var circle_marker_a0d7fa0279ae51b53584f632d8e05704 = L.circleMarker(
                [40.4296, -3.62345],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_56777b2877001e58783bd3d51b0b0bad = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_411289a6bb5e6871d9e4f0825b99cfb9 = $(`&lt;div id=&quot;html_411289a6bb5e6871d9e4f0825b99cfb9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;20.0&lt;/div&gt;`)[0];
            popup_56777b2877001e58783bd3d51b0b0bad.setContent(html_411289a6bb5e6871d9e4f0825b99cfb9);


        circle_marker_a0d7fa0279ae51b53584f632d8e05704.bindPopup(popup_56777b2877001e58783bd3d51b0b0bad)
        ;




            var circle_marker_abd31282ff5c9318c432a3c438c96bef = L.circleMarker(
                [40.44688, -3.61423],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_525bb96c880c9eb72069bedb0f41e9a9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_deda0232e54f42b9b1bb7e2cfb312c6d = $(`&lt;div id=&quot;html_deda0232e54f42b9b1bb7e2cfb312c6d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;44.0&lt;/div&gt;`)[0];
            popup_525bb96c880c9eb72069bedb0f41e9a9.setContent(html_deda0232e54f42b9b1bb7e2cfb312c6d);


        circle_marker_abd31282ff5c9318c432a3c438c96bef.bindPopup(popup_525bb96c880c9eb72069bedb0f41e9a9)
        ;




            var circle_marker_376d44da0de524340e0563884312c7b7 = L.circleMarker(
                [40.44381, -3.6103],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_49de34bb9e22ede8400199c825bcd267 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7366fcf9219fcc4a2f418d14543560b2 = $(`&lt;div id=&quot;html_7366fcf9219fcc4a2f418d14543560b2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;70.0&lt;/div&gt;`)[0];
            popup_49de34bb9e22ede8400199c825bcd267.setContent(html_7366fcf9219fcc4a2f418d14543560b2);


        circle_marker_376d44da0de524340e0563884312c7b7.bindPopup(popup_49de34bb9e22ede8400199c825bcd267)
        ;




            var circle_marker_7ca3a25aff68cef7ac424c6dc6a8f332 = L.circleMarker(
                [40.43062, -3.61323],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8a50a36c77af2e5e153d63288b8e726b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0b15762686f40b15e4a56bc94288fcb3 = $(`&lt;div id=&quot;html_0b15762686f40b15e4a56bc94288fcb3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;52.0&lt;/div&gt;`)[0];
            popup_8a50a36c77af2e5e153d63288b8e726b.setContent(html_0b15762686f40b15e4a56bc94288fcb3);


        circle_marker_7ca3a25aff68cef7ac424c6dc6a8f332.bindPopup(popup_8a50a36c77af2e5e153d63288b8e726b)
        ;




            var circle_marker_043f6165421ff5f150714cf64921b9ae = L.circleMarker(
                [40.42565, -3.61811],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3f7cd860632a1a3d0cfec005f2250770 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_70f6791c443f8d3a892f41d6eacdf065 = $(`&lt;div id=&quot;html_70f6791c443f8d3a892f41d6eacdf065&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;36.0&lt;/div&gt;`)[0];
            popup_3f7cd860632a1a3d0cfec005f2250770.setContent(html_70f6791c443f8d3a892f41d6eacdf065);


        circle_marker_043f6165421ff5f150714cf64921b9ae.bindPopup(popup_3f7cd860632a1a3d0cfec005f2250770)
        ;




            var circle_marker_2acc287382b282187f5f918253695edf = L.circleMarker(
                [40.4315, -3.62729],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8cdab22c196b2957413cc4d7877f72e3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_992ce2c1ba186cc4f332973e45c12982 = $(`&lt;div id=&quot;html_992ce2c1ba186cc4f332973e45c12982&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;29.0&lt;/div&gt;`)[0];
            popup_8cdab22c196b2957413cc4d7877f72e3.setContent(html_992ce2c1ba186cc4f332973e45c12982);


        circle_marker_2acc287382b282187f5f918253695edf.bindPopup(popup_8cdab22c196b2957413cc4d7877f72e3)
        ;




            var circle_marker_56e011d52e854786611c39d68d277579 = L.circleMarker(
                [40.42564, -3.62215],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3183567caa280780e1436cab71353a7a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_001ddd306765486d38ed1adb1b0388dd = $(`&lt;div id=&quot;html_001ddd306765486d38ed1adb1b0388dd&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1000.0&lt;/div&gt;`)[0];
            popup_3183567caa280780e1436cab71353a7a.setContent(html_001ddd306765486d38ed1adb1b0388dd);


        circle_marker_56e011d52e854786611c39d68d277579.bindPopup(popup_3183567caa280780e1436cab71353a7a)
        ;




            var circle_marker_2fc9e1d006df3d7d8f57a4164627854b = L.circleMarker(
                [40.4367, -3.63438],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_93d77f1e670ca78f4995732a1284ca5a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_feba10816c3381c533e3327e37092811 = $(`&lt;div id=&quot;html_feba10816c3381c533e3327e37092811&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;57.0&lt;/div&gt;`)[0];
            popup_93d77f1e670ca78f4995732a1284ca5a.setContent(html_feba10816c3381c533e3327e37092811);


        circle_marker_2fc9e1d006df3d7d8f57a4164627854b.bindPopup(popup_93d77f1e670ca78f4995732a1284ca5a)
        ;




            var circle_marker_cdc7e08d528ae45da776c042772debc8 = L.circleMarker(
                [40.43039, -3.61631],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_78eedcad7ed761e8b2aac2202e52845a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_cead2a60fd6e463b692264ba67bce178 = $(`&lt;div id=&quot;html_cead2a60fd6e463b692264ba67bce178&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;47.0&lt;/div&gt;`)[0];
            popup_78eedcad7ed761e8b2aac2202e52845a.setContent(html_cead2a60fd6e463b692264ba67bce178);


        circle_marker_cdc7e08d528ae45da776c042772debc8.bindPopup(popup_78eedcad7ed761e8b2aac2202e52845a)
        ;




            var circle_marker_cd222711dca9e02edfdf822b8b45f295 = L.circleMarker(
                [40.43956, -3.61889],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_51bdd5e93d31af0fcf70c0a542b93611 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_03a7a77b81f028793cb83ccffa3149bb = $(`&lt;div id=&quot;html_03a7a77b81f028793cb83ccffa3149bb&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;60.0&lt;/div&gt;`)[0];
            popup_51bdd5e93d31af0fcf70c0a542b93611.setContent(html_03a7a77b81f028793cb83ccffa3149bb);


        circle_marker_cd222711dca9e02edfdf822b8b45f295.bindPopup(popup_51bdd5e93d31af0fcf70c0a542b93611)
        ;




            var circle_marker_015da2d0c65313222b2144a513822e02 = L.circleMarker(
                [40.44318, -3.63236],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f324b80c76fef11c6f88b58d1f32b7c3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_15583535f570693abeca24f74fc98e11 = $(`&lt;div id=&quot;html_15583535f570693abeca24f74fc98e11&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;44.099999999999994&lt;/div&gt;`)[0];
            popup_f324b80c76fef11c6f88b58d1f32b7c3.setContent(html_15583535f570693abeca24f74fc98e11);


        circle_marker_015da2d0c65313222b2144a513822e02.bindPopup(popup_f324b80c76fef11c6f88b58d1f32b7c3)
        ;




            var circle_marker_84ff94cf2c22f403b21dad8cabf3c9c3 = L.circleMarker(
                [40.42185, -3.61892],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_977f76a48e8289a02a5ad8c90df0609a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1f771cc955a662d0d5a533e981bb8d78 = $(`&lt;div id=&quot;html_1f771cc955a662d0d5a533e981bb8d78&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;35.0&lt;/div&gt;`)[0];
            popup_977f76a48e8289a02a5ad8c90df0609a.setContent(html_1f771cc955a662d0d5a533e981bb8d78);


        circle_marker_84ff94cf2c22f403b21dad8cabf3c9c3.bindPopup(popup_977f76a48e8289a02a5ad8c90df0609a)
        ;




            var circle_marker_9a26a0049e69ce1d5d8c0a66539ebd05 = L.circleMarker(
                [40.43638, -3.60933],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_cb736d75630139972a5d8fd997d78cc3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6b6cf2d04842f38ef420fdccf984b313 = $(`&lt;div id=&quot;html_6b6cf2d04842f38ef420fdccf984b313&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;420.0&lt;/div&gt;`)[0];
            popup_cb736d75630139972a5d8fd997d78cc3.setContent(html_6b6cf2d04842f38ef420fdccf984b313);


        circle_marker_9a26a0049e69ce1d5d8c0a66539ebd05.bindPopup(popup_cb736d75630139972a5d8fd997d78cc3)
        ;




            var circle_marker_e69712ba8ffc56c9d3d057db6ad5d11c = L.circleMarker(
                [40.44503748964719, -3.5816784435547797],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_6bb6bb8aeab3fdab870b73ece1c833b4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_85cc6d63b1e969cebddeb4ff8126045e = $(`&lt;div id=&quot;html_85cc6d63b1e969cebddeb4ff8126045e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;75.0&lt;/div&gt;`)[0];
            popup_6bb6bb8aeab3fdab870b73ece1c833b4.setContent(html_85cc6d63b1e969cebddeb4ff8126045e);


        circle_marker_e69712ba8ffc56c9d3d057db6ad5d11c.bindPopup(popup_6bb6bb8aeab3fdab870b73ece1c833b4)
        ;




            var circle_marker_1581b40a4baa85c01d455524936afda0 = L.circleMarker(
                [40.43294, -3.63283],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8769bed4a6fecaa0cf3f69cdbebc2ad3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_68eb45b8f35edd3aea6f319ebf7a500b = $(`&lt;div id=&quot;html_68eb45b8f35edd3aea6f319ebf7a500b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;22.0&lt;/div&gt;`)[0];
            popup_8769bed4a6fecaa0cf3f69cdbebc2ad3.setContent(html_68eb45b8f35edd3aea6f319ebf7a500b);


        circle_marker_1581b40a4baa85c01d455524936afda0.bindPopup(popup_8769bed4a6fecaa0cf3f69cdbebc2ad3)
        ;




            var circle_marker_6a6523223421f03f3c1a80f375c14990 = L.circleMarker(
                [40.4485, -3.60755],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_2f744f26bdae41b76edd3134430192b7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_53c9ea84b2cdb6a9a3ea76bb9c286ce9 = $(`&lt;div id=&quot;html_53c9ea84b2cdb6a9a3ea76bb9c286ce9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;31.0&lt;/div&gt;`)[0];
            popup_2f744f26bdae41b76edd3134430192b7.setContent(html_53c9ea84b2cdb6a9a3ea76bb9c286ce9);


        circle_marker_6a6523223421f03f3c1a80f375c14990.bindPopup(popup_2f744f26bdae41b76edd3134430192b7)
        ;




            var circle_marker_cfa15da2a238aac6d43036c317db093d = L.circleMarker(
                [40.44256, -3.58315],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_7c00b1f9406f5a5a1ed440560c718560 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a8e6fcd2d7df1ec329307e8dca372077 = $(`&lt;div id=&quot;html_a8e6fcd2d7df1ec329307e8dca372077&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;44.0&lt;/div&gt;`)[0];
            popup_7c00b1f9406f5a5a1ed440560c718560.setContent(html_a8e6fcd2d7df1ec329307e8dca372077);


        circle_marker_cfa15da2a238aac6d43036c317db093d.bindPopup(popup_7c00b1f9406f5a5a1ed440560c718560)
        ;




            var circle_marker_f7ecdff6e753be53043b02ad53d24db3 = L.circleMarker(
                [40.44349, -3.58355],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_99971fee475d7acd46c015df0f1c13a0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a6bcad11564ffe4d8154e29d5611b367 = $(`&lt;div id=&quot;html_a6bcad11564ffe4d8154e29d5611b367&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;39.0&lt;/div&gt;`)[0];
            popup_99971fee475d7acd46c015df0f1c13a0.setContent(html_a6bcad11564ffe4d8154e29d5611b367);


        circle_marker_f7ecdff6e753be53043b02ad53d24db3.bindPopup(popup_99971fee475d7acd46c015df0f1c13a0)
        ;




            var circle_marker_5194bab2594715cda355154a0f89913e = L.circleMarker(
                [40.43425, -3.63169],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_965069803ec29638ae7e8dc95d841c51 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_fab75ec43115381be7b3e205c00ac95c = $(`&lt;div id=&quot;html_fab75ec43115381be7b3e205c00ac95c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;169.0&lt;/div&gt;`)[0];
            popup_965069803ec29638ae7e8dc95d841c51.setContent(html_fab75ec43115381be7b3e205c00ac95c);


        circle_marker_5194bab2594715cda355154a0f89913e.bindPopup(popup_965069803ec29638ae7e8dc95d841c51)
        ;




            var circle_marker_477926e62c62e793717fe0e29feeb487 = L.circleMarker(
                [40.43036, -3.62729],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_61f35154dfdeb0e3bdac8194c624dd0c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_debf421efc5b8c8f63691bc0703fd2c4 = $(`&lt;div id=&quot;html_debf421efc5b8c8f63691bc0703fd2c4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.0&lt;/div&gt;`)[0];
            popup_61f35154dfdeb0e3bdac8194c624dd0c.setContent(html_debf421efc5b8c8f63691bc0703fd2c4);


        circle_marker_477926e62c62e793717fe0e29feeb487.bindPopup(popup_61f35154dfdeb0e3bdac8194c624dd0c)
        ;




            var circle_marker_b3f3425847b25f0d1f6ae264fc961f30 = L.circleMarker(
                [40.43701, -3.62442],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4efd62b1de3e92e8233472858434da51 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_dd965d8a4d664e6947d1146df2c6c4e2 = $(`&lt;div id=&quot;html_dd965d8a4d664e6947d1146df2c6c4e2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;93.0&lt;/div&gt;`)[0];
            popup_4efd62b1de3e92e8233472858434da51.setContent(html_dd965d8a4d664e6947d1146df2c6c4e2);


        circle_marker_b3f3425847b25f0d1f6ae264fc961f30.bindPopup(popup_4efd62b1de3e92e8233472858434da51)
        ;




            var circle_marker_c169c8e7adfec5d11b85f98f9c38b8d9 = L.circleMarker(
                [40.44494, -3.58664],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b9a5f618a199348dbabc8c7590b64cea = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7fc5339c8bff68cf29ba8b2639f66a60 = $(`&lt;div id=&quot;html_7fc5339c8bff68cf29ba8b2639f66a60&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;61.0&lt;/div&gt;`)[0];
            popup_b9a5f618a199348dbabc8c7590b64cea.setContent(html_7fc5339c8bff68cf29ba8b2639f66a60);


        circle_marker_c169c8e7adfec5d11b85f98f9c38b8d9.bindPopup(popup_b9a5f618a199348dbabc8c7590b64cea)
        ;




            var circle_marker_4cc90794ef647a9e15a98c00197606fc = L.circleMarker(
                [40.42377, -3.6133],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3625a0b19bb34efbb15d3375702d5d22 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e33286b3eda51f815bd1344d9765ffda = $(`&lt;div id=&quot;html_e33286b3eda51f815bd1344d9765ffda&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;25.0&lt;/div&gt;`)[0];
            popup_3625a0b19bb34efbb15d3375702d5d22.setContent(html_e33286b3eda51f815bd1344d9765ffda);


        circle_marker_4cc90794ef647a9e15a98c00197606fc.bindPopup(popup_3625a0b19bb34efbb15d3375702d5d22)
        ;




            var circle_marker_84dd35d6aed79e53a8ebffc992262b64 = L.circleMarker(
                [40.43078, -3.62508],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_13adf2ea7a934602414528eda37076ce = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_14871b6fdd20174d1fb44482ffca01ef = $(`&lt;div id=&quot;html_14871b6fdd20174d1fb44482ffca01ef&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;22.0&lt;/div&gt;`)[0];
            popup_13adf2ea7a934602414528eda37076ce.setContent(html_14871b6fdd20174d1fb44482ffca01ef);


        circle_marker_84dd35d6aed79e53a8ebffc992262b64.bindPopup(popup_13adf2ea7a934602414528eda37076ce)
        ;




            var circle_marker_4cff4038c0943bed6c321f980ae0f0e3 = L.circleMarker(
                [40.42589, -3.60997],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_125bebd3495a57492792fb9c6490b13e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2556004ab5192d08e59973ce9cd4bdc8 = $(`&lt;div id=&quot;html_2556004ab5192d08e59973ce9cd4bdc8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;89.0&lt;/div&gt;`)[0];
            popup_125bebd3495a57492792fb9c6490b13e.setContent(html_2556004ab5192d08e59973ce9cd4bdc8);


        circle_marker_4cff4038c0943bed6c321f980ae0f0e3.bindPopup(popup_125bebd3495a57492792fb9c6490b13e)
        ;




            var circle_marker_9226d16c231ce688a346c75a0721e4be = L.circleMarker(
                [40.43003, -3.59975],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8054f7b6fa518a15bf1621ada3058ffe = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4f62524028880c3a217b8a75605fdd1f = $(`&lt;div id=&quot;html_4f62524028880c3a217b8a75605fdd1f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1470.0&lt;/div&gt;`)[0];
            popup_8054f7b6fa518a15bf1621ada3058ffe.setContent(html_4f62524028880c3a217b8a75605fdd1f);


        circle_marker_9226d16c231ce688a346c75a0721e4be.bindPopup(popup_8054f7b6fa518a15bf1621ada3058ffe)
        ;




            var circle_marker_0b37cec8419685d726feea9120d7c028 = L.circleMarker(
                [40.44604, -3.61323],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f0cbedd40a42ed4d8a4c65dc247156c3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_3ee215513086aadd68ee2a925ac92a0c = $(`&lt;div id=&quot;html_3ee215513086aadd68ee2a925ac92a0c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;250.0&lt;/div&gt;`)[0];
            popup_f0cbedd40a42ed4d8a4c65dc247156c3.setContent(html_3ee215513086aadd68ee2a925ac92a0c);


        circle_marker_0b37cec8419685d726feea9120d7c028.bindPopup(popup_f0cbedd40a42ed4d8a4c65dc247156c3)
        ;




            var circle_marker_4d5acd0e205db942ff568ce2c906545f = L.circleMarker(
                [40.43889, -3.63051],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_62d881000efbc3c5a6bf9c1ed3d82d13 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_41af44720b9795ddea15c1d2445842b5 = $(`&lt;div id=&quot;html_41af44720b9795ddea15c1d2445842b5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;85.0&lt;/div&gt;`)[0];
            popup_62d881000efbc3c5a6bf9c1ed3d82d13.setContent(html_41af44720b9795ddea15c1d2445842b5);


        circle_marker_4d5acd0e205db942ff568ce2c906545f.bindPopup(popup_62d881000efbc3c5a6bf9c1ed3d82d13)
        ;




            var circle_marker_07466e66293d84747db6bc781ca01214 = L.circleMarker(
                [40.43882, -3.62378],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_1d5135eee16587b09f387c0e72fa77d4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d8f116a1dd9740872bad2c19e25ed3c9 = $(`&lt;div id=&quot;html_d8f116a1dd9740872bad2c19e25ed3c9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;22.0&lt;/div&gt;`)[0];
            popup_1d5135eee16587b09f387c0e72fa77d4.setContent(html_d8f116a1dd9740872bad2c19e25ed3c9);


        circle_marker_07466e66293d84747db6bc781ca01214.bindPopup(popup_1d5135eee16587b09f387c0e72fa77d4)
        ;




            var circle_marker_f652c9d2407d83c3e33c40a4a57058df = L.circleMarker(
                [40.44923, -3.58724],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9e5362c245d83f5f33ed998bfb6cda4d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_40fcccbc9465699ff616ec41a9852a7a = $(`&lt;div id=&quot;html_40fcccbc9465699ff616ec41a9852a7a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;75.0&lt;/div&gt;`)[0];
            popup_9e5362c245d83f5f33ed998bfb6cda4d.setContent(html_40fcccbc9465699ff616ec41a9852a7a);


        circle_marker_f652c9d2407d83c3e33c40a4a57058df.bindPopup(popup_9e5362c245d83f5f33ed998bfb6cda4d)
        ;




            var circle_marker_2e57c1fd04be348fc3c51bc196b2f653 = L.circleMarker(
                [40.43285, -3.60691],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d3b0657224392676e23a64aeedf70d46 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1b7e99d0ef3deebcab287a5397ac5bcf = $(`&lt;div id=&quot;html_1b7e99d0ef3deebcab287a5397ac5bcf&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;45.0&lt;/div&gt;`)[0];
            popup_d3b0657224392676e23a64aeedf70d46.setContent(html_1b7e99d0ef3deebcab287a5397ac5bcf);


        circle_marker_2e57c1fd04be348fc3c51bc196b2f653.bindPopup(popup_d3b0657224392676e23a64aeedf70d46)
        ;




            var circle_marker_f5bb98e11cd990a3ab6a76008b7804ee = L.circleMarker(
                [40.43303, -3.63345],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_55d3693c9687cb31ee3452364046b069 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_57c811e0157e73b29358ec6b8f61f86a = $(`&lt;div id=&quot;html_57c811e0157e73b29358ec6b8f61f86a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;23.0&lt;/div&gt;`)[0];
            popup_55d3693c9687cb31ee3452364046b069.setContent(html_57c811e0157e73b29358ec6b8f61f86a);


        circle_marker_f5bb98e11cd990a3ab6a76008b7804ee.bindPopup(popup_55d3693c9687cb31ee3452364046b069)
        ;




            var circle_marker_a5e80051c189ad1170fbf17551ec4cad = L.circleMarker(
                [40.42847, -3.62638],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_661f1afa97506574d6b91123206f0f26 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_43e814f76db3da1c0d2f57ebdab23c5c = $(`&lt;div id=&quot;html_43e814f76db3da1c0d2f57ebdab23c5c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;38.0&lt;/div&gt;`)[0];
            popup_661f1afa97506574d6b91123206f0f26.setContent(html_43e814f76db3da1c0d2f57ebdab23c5c);


        circle_marker_a5e80051c189ad1170fbf17551ec4cad.bindPopup(popup_661f1afa97506574d6b91123206f0f26)
        ;




            var circle_marker_a399366e69fc0d310cd18427f2fb1067 = L.circleMarker(
                [40.43786, -3.6357],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_46166590b0e88e501deffb9f8fc5db15 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_586f2d93825e0e93d743478d8a33fe4f = $(`&lt;div id=&quot;html_586f2d93825e0e93d743478d8a33fe4f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1000.0&lt;/div&gt;`)[0];
            popup_46166590b0e88e501deffb9f8fc5db15.setContent(html_586f2d93825e0e93d743478d8a33fe4f);


        circle_marker_a399366e69fc0d310cd18427f2fb1067.bindPopup(popup_46166590b0e88e501deffb9f8fc5db15)
        ;




            var circle_marker_48761ce19d5cfe28e3e5eaf48adbbc3c = L.circleMarker(
                [40.43963, -3.61865],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ff3c9687cf8ac3110d4e10d19c3d10d8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_82d219e92a88d82d6b86a64d62aeeb74 = $(`&lt;div id=&quot;html_82d219e92a88d82d6b86a64d62aeeb74&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_ff3c9687cf8ac3110d4e10d19c3d10d8.setContent(html_82d219e92a88d82d6b86a64d62aeeb74);


        circle_marker_48761ce19d5cfe28e3e5eaf48adbbc3c.bindPopup(popup_ff3c9687cf8ac3110d4e10d19c3d10d8)
        ;




            var circle_marker_788d3abac097aee8b7d0f39872a43598 = L.circleMarker(
                [40.43182, -3.6236],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c5126087286575d6367aefaaba8dca6e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_5453f6d5c1bb3c6b909489ab72ef3d18 = $(`&lt;div id=&quot;html_5453f6d5c1bb3c6b909489ab72ef3d18&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;47.0&lt;/div&gt;`)[0];
            popup_c5126087286575d6367aefaaba8dca6e.setContent(html_5453f6d5c1bb3c6b909489ab72ef3d18);


        circle_marker_788d3abac097aee8b7d0f39872a43598.bindPopup(popup_c5126087286575d6367aefaaba8dca6e)
        ;




            var circle_marker_edcf0d70954f0fcf81bd0cbe7984aa09 = L.circleMarker(
                [40.44412, -3.584],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_90a92aff3b1c5121775382130ba03c5d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_3247b8e60dcbb7910841fbb415a47ff2 = $(`&lt;div id=&quot;html_3247b8e60dcbb7910841fbb415a47ff2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;55.0&lt;/div&gt;`)[0];
            popup_90a92aff3b1c5121775382130ba03c5d.setContent(html_3247b8e60dcbb7910841fbb415a47ff2);


        circle_marker_edcf0d70954f0fcf81bd0cbe7984aa09.bindPopup(popup_90a92aff3b1c5121775382130ba03c5d)
        ;




            var circle_marker_7d201874ad21b7b2020c8ddfba241db9 = L.circleMarker(
                [40.44407, -3.58457],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_caef8b99f14146291634c4ae97cf9c85 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_c2925deba7f4a7f01f719a59f0ff1c54 = $(`&lt;div id=&quot;html_c2925deba7f4a7f01f719a59f0ff1c54&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;60.0&lt;/div&gt;`)[0];
            popup_caef8b99f14146291634c4ae97cf9c85.setContent(html_c2925deba7f4a7f01f719a59f0ff1c54);


        circle_marker_7d201874ad21b7b2020c8ddfba241db9.bindPopup(popup_caef8b99f14146291634c4ae97cf9c85)
        ;




            var circle_marker_3386871305a001048ace321a7e0650fb = L.circleMarker(
                [40.4346, -3.60708],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5cb2478901ae7a134b5b9c8628fcc34f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_06228a3ed6f3b4c8caf4c40f2f273989 = $(`&lt;div id=&quot;html_06228a3ed6f3b4c8caf4c40f2f273989&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.0&lt;/div&gt;`)[0];
            popup_5cb2478901ae7a134b5b9c8628fcc34f.setContent(html_06228a3ed6f3b4c8caf4c40f2f273989);


        circle_marker_3386871305a001048ace321a7e0650fb.bindPopup(popup_5cb2478901ae7a134b5b9c8628fcc34f)
        ;




            var circle_marker_3f852c529f321e0315b889d08376264f = L.circleMarker(
                [40.4436, -3.58343],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_de76205188630b14b63db162e5aa216d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2ec437ea1b50f4fb02189606f6d954b0 = $(`&lt;div id=&quot;html_2ec437ea1b50f4fb02189606f6d954b0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;59.0&lt;/div&gt;`)[0];
            popup_de76205188630b14b63db162e5aa216d.setContent(html_2ec437ea1b50f4fb02189606f6d954b0);


        circle_marker_3f852c529f321e0315b889d08376264f.bindPopup(popup_de76205188630b14b63db162e5aa216d)
        ;




            var circle_marker_a766c4a3a11237d665d4ef29d07c1545 = L.circleMarker(
                [40.44701, -3.64362],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_718545992a18fb026837692325e34d61 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e984f2cd8f51d940dd80aa31605bf58b = $(`&lt;div id=&quot;html_e984f2cd8f51d940dd80aa31605bf58b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;70.0&lt;/div&gt;`)[0];
            popup_718545992a18fb026837692325e34d61.setContent(html_e984f2cd8f51d940dd80aa31605bf58b);


        circle_marker_a766c4a3a11237d665d4ef29d07c1545.bindPopup(popup_718545992a18fb026837692325e34d61)
        ;




            var circle_marker_adc858393b66ad768f746a53147b4073 = L.circleMarker(
                [40.4468, -3.57502],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_28e8b8f0be12421e3fda3591f2c7899d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1c659c8ef26f6764d124c1a2befc0e47 = $(`&lt;div id=&quot;html_1c659c8ef26f6764d124c1a2befc0e47&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;200.0&lt;/div&gt;`)[0];
            popup_28e8b8f0be12421e3fda3591f2c7899d.setContent(html_1c659c8ef26f6764d124c1a2befc0e47);


        circle_marker_adc858393b66ad768f746a53147b4073.bindPopup(popup_28e8b8f0be12421e3fda3591f2c7899d)
        ;




            var circle_marker_e18e944f6f1a4e05dcd2053033a1ec60 = L.circleMarker(
                [40.44349, -3.58368],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_1d0ce938a86b0e918e86aab3ffa4fcf9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_18b5f9ed989905da263acb4263fd08a0 = $(`&lt;div id=&quot;html_18b5f9ed989905da263acb4263fd08a0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;150.0&lt;/div&gt;`)[0];
            popup_1d0ce938a86b0e918e86aab3ffa4fcf9.setContent(html_18b5f9ed989905da263acb4263fd08a0);


        circle_marker_e18e944f6f1a4e05dcd2053033a1ec60.bindPopup(popup_1d0ce938a86b0e918e86aab3ffa4fcf9)
        ;




            var circle_marker_a27b6bccffc0289ffe43a175f517ddbd = L.circleMarker(
                [40.44391, -3.58362],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ec366297d4fcf3b03f75456e38d552a4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0895f2206d6bcaad87be0ac7852ac4a5 = $(`&lt;div id=&quot;html_0895f2206d6bcaad87be0ac7852ac4a5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;79.0&lt;/div&gt;`)[0];
            popup_ec366297d4fcf3b03f75456e38d552a4.setContent(html_0895f2206d6bcaad87be0ac7852ac4a5);


        circle_marker_a27b6bccffc0289ffe43a175f517ddbd.bindPopup(popup_ec366297d4fcf3b03f75456e38d552a4)
        ;




            var circle_marker_c0ec727683753c2334037c8e33c3bd7a = L.circleMarker(
                [40.42365, -3.62196],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_2416e230d2c6785f6bd525e32f20fb25 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_3719b1d254b017ef8ad0ab17df7277d6 = $(`&lt;div id=&quot;html_3719b1d254b017ef8ad0ab17df7277d6&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;489.99999999999994&lt;/div&gt;`)[0];
            popup_2416e230d2c6785f6bd525e32f20fb25.setContent(html_3719b1d254b017ef8ad0ab17df7277d6);


        circle_marker_c0ec727683753c2334037c8e33c3bd7a.bindPopup(popup_2416e230d2c6785f6bd525e32f20fb25)
        ;




            var circle_marker_96ce80440a6352efb11336465513c915 = L.circleMarker(
                [40.44324, -3.58412],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_11c8369f8f19750bf944641181a216f5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_8a931a50865694994cf0b4707d4a0893 = $(`&lt;div id=&quot;html_8a931a50865694994cf0b4707d4a0893&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;69.0&lt;/div&gt;`)[0];
            popup_11c8369f8f19750bf944641181a216f5.setContent(html_8a931a50865694994cf0b4707d4a0893);


        circle_marker_96ce80440a6352efb11336465513c915.bindPopup(popup_11c8369f8f19750bf944641181a216f5)
        ;




            var circle_marker_8847ca4d07832961cfc862b05ff15a33 = L.circleMarker(
                [40.43847, -3.62865],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_078c7f4ac279900dd43f32b9fa9bc753 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_777f2f1af6e2abb29e191e96d29e2c43 = $(`&lt;div id=&quot;html_777f2f1af6e2abb29e191e96d29e2c43&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;82.0&lt;/div&gt;`)[0];
            popup_078c7f4ac279900dd43f32b9fa9bc753.setContent(html_777f2f1af6e2abb29e191e96d29e2c43);


        circle_marker_8847ca4d07832961cfc862b05ff15a33.bindPopup(popup_078c7f4ac279900dd43f32b9fa9bc753)
        ;




            var circle_marker_a76434ba7ed844542677546526254575 = L.circleMarker(
                [40.42662, -3.60745],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_624366b50e93c30d222a4b72c83d27c0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ce5cf66592949e29c34d52918ea3cdb9 = $(`&lt;div id=&quot;html_ce5cf66592949e29c34d52918ea3cdb9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;27.0&lt;/div&gt;`)[0];
            popup_624366b50e93c30d222a4b72c83d27c0.setContent(html_ce5cf66592949e29c34d52918ea3cdb9);


        circle_marker_a76434ba7ed844542677546526254575.bindPopup(popup_624366b50e93c30d222a4b72c83d27c0)
        ;




            var circle_marker_dbf07f8a0bf219185ccc0cb82daa5eb3 = L.circleMarker(
                [40.44377, -3.58241],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c13a3506864de3e220b9505ef1a1f25c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_c1fbdf872d3c642d03c1bcfd8061a24c = $(`&lt;div id=&quot;html_c1fbdf872d3c642d03c1bcfd8061a24c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;60.0&lt;/div&gt;`)[0];
            popup_c13a3506864de3e220b9505ef1a1f25c.setContent(html_c1fbdf872d3c642d03c1bcfd8061a24c);


        circle_marker_dbf07f8a0bf219185ccc0cb82daa5eb3.bindPopup(popup_c13a3506864de3e220b9505ef1a1f25c)
        ;




            var circle_marker_0d69e281be3078ebedb7cb48c2d199dd = L.circleMarker(
                [40.44578, -3.58879],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_30371483c9e4ca8797f73fac6fee3cf3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_488d0f56e79c6972d661df205681b7ca = $(`&lt;div id=&quot;html_488d0f56e79c6972d661df205681b7ca&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;65.0&lt;/div&gt;`)[0];
            popup_30371483c9e4ca8797f73fac6fee3cf3.setContent(html_488d0f56e79c6972d661df205681b7ca);


        circle_marker_0d69e281be3078ebedb7cb48c2d199dd.bindPopup(popup_30371483c9e4ca8797f73fac6fee3cf3)
        ;




            var circle_marker_c8a62d61a30d0cdc535a36f508087e19 = L.circleMarker(
                [40.44482, -3.5838],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4934184946277c1e75c5c985005a6c22 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_f944141ab92ca785da8486d0ecae262b = $(`&lt;div id=&quot;html_f944141ab92ca785da8486d0ecae262b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;65.0&lt;/div&gt;`)[0];
            popup_4934184946277c1e75c5c985005a6c22.setContent(html_f944141ab92ca785da8486d0ecae262b);


        circle_marker_c8a62d61a30d0cdc535a36f508087e19.bindPopup(popup_4934184946277c1e75c5c985005a6c22)
        ;




            var circle_marker_4600bfb6c6d82a5a21415600098bc0ce = L.circleMarker(
                [40.4278, -3.606],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a99169e9f3c594dbfb2fa2c419845b89 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_efa3eee8ed8bbb01a350a54848252ff6 = $(`&lt;div id=&quot;html_efa3eee8ed8bbb01a350a54848252ff6&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;90.0&lt;/div&gt;`)[0];
            popup_a99169e9f3c594dbfb2fa2c419845b89.setContent(html_efa3eee8ed8bbb01a350a54848252ff6);


        circle_marker_4600bfb6c6d82a5a21415600098bc0ce.bindPopup(popup_a99169e9f3c594dbfb2fa2c419845b89)
        ;




            var circle_marker_b7299e789747e64cc7314aa563c21db9 = L.circleMarker(
                [40.43416, -3.61036],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_bceb8cde64f3931d03b787ee221a6bae = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_935894830c6c8501922720b28fd79ccd = $(`&lt;div id=&quot;html_935894830c6c8501922720b28fd79ccd&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;154.0&lt;/div&gt;`)[0];
            popup_bceb8cde64f3931d03b787ee221a6bae.setContent(html_935894830c6c8501922720b28fd79ccd);


        circle_marker_b7299e789747e64cc7314aa563c21db9.bindPopup(popup_bceb8cde64f3931d03b787ee221a6bae)
        ;




            var circle_marker_3b75d7cd7a5ab9d9b6cb62fd610c79ea = L.circleMarker(
                [40.44332, -3.5771],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_fc36bd960adf2decae49be39bf5e6c4b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6672a55d5203cea34488dc29a05e3095 = $(`&lt;div id=&quot;html_6672a55d5203cea34488dc29a05e3095&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;26.0&lt;/div&gt;`)[0];
            popup_fc36bd960adf2decae49be39bf5e6c4b.setContent(html_6672a55d5203cea34488dc29a05e3095);


        circle_marker_3b75d7cd7a5ab9d9b6cb62fd610c79ea.bindPopup(popup_fc36bd960adf2decae49be39bf5e6c4b)
        ;




            var circle_marker_957e77575f1b35dc03ad589119cf3e52 = L.circleMarker(
                [40.44356, -3.57674],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_218dadbfdc886b0de73f4a360cc88959 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_5f3bd517e656006861086ee60caeba70 = $(`&lt;div id=&quot;html_5f3bd517e656006861086ee60caeba70&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;49.0&lt;/div&gt;`)[0];
            popup_218dadbfdc886b0de73f4a360cc88959.setContent(html_5f3bd517e656006861086ee60caeba70);


        circle_marker_957e77575f1b35dc03ad589119cf3e52.bindPopup(popup_218dadbfdc886b0de73f4a360cc88959)
        ;




            var circle_marker_f5056912fd6f4729e699d42e80efdff6 = L.circleMarker(
                [40.42104, -3.61483],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ed36d98136a55e529ab491364185fc08 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_8a7164746c464a537f438419e9817d83 = $(`&lt;div id=&quot;html_8a7164746c464a537f438419e9817d83&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1499.3999999999999&lt;/div&gt;`)[0];
            popup_ed36d98136a55e529ab491364185fc08.setContent(html_8a7164746c464a537f438419e9817d83);


        circle_marker_f5056912fd6f4729e699d42e80efdff6.bindPopup(popup_ed36d98136a55e529ab491364185fc08)
        ;




            var circle_marker_1d0a0b2fc98d4f9f8271d93e9d3cee92 = L.circleMarker(
                [40.43665, -3.63535],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_021f980b7cb6688eb8a08263eb240244 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_fa386d7ea68836702fdefcb6c86825cc = $(`&lt;div id=&quot;html_fa386d7ea68836702fdefcb6c86825cc&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;64.0&lt;/div&gt;`)[0];
            popup_021f980b7cb6688eb8a08263eb240244.setContent(html_fa386d7ea68836702fdefcb6c86825cc);


        circle_marker_1d0a0b2fc98d4f9f8271d93e9d3cee92.bindPopup(popup_021f980b7cb6688eb8a08263eb240244)
        ;




            var circle_marker_4ae19069889bc4e25f20b749d39c6e1c = L.circleMarker(
                [40.43865, -3.62314],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_478c4a7aaf441666e63f642a6e7ee017 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d8a252cdb81c2d8e06faaefdaa159e0d = $(`&lt;div id=&quot;html_d8a252cdb81c2d8e06faaefdaa159e0d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;49.0&lt;/div&gt;`)[0];
            popup_478c4a7aaf441666e63f642a6e7ee017.setContent(html_d8a252cdb81c2d8e06faaefdaa159e0d);


        circle_marker_4ae19069889bc4e25f20b749d39c6e1c.bindPopup(popup_478c4a7aaf441666e63f642a6e7ee017)
        ;




            var circle_marker_5213db57a837f50df814379fce43cc05 = L.circleMarker(
                [40.43796, -3.60738],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3169eab2ee09a5ba26f9544dc75377a6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9ea57ef30ac4c63e9a365c016c74cd9f = $(`&lt;div id=&quot;html_9ea57ef30ac4c63e9a365c016c74cd9f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;33.0&lt;/div&gt;`)[0];
            popup_3169eab2ee09a5ba26f9544dc75377a6.setContent(html_9ea57ef30ac4c63e9a365c016c74cd9f);


        circle_marker_5213db57a837f50df814379fce43cc05.bindPopup(popup_3169eab2ee09a5ba26f9544dc75377a6)
        ;




            var circle_marker_5c9ce0c864bb5dc57e6b7b890a5724c1 = L.circleMarker(
                [40.44504, -3.5959],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c6a1c5ea2016e1f73f38c8f420ec2429 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_895f6520f8626b87841095e64127de72 = $(`&lt;div id=&quot;html_895f6520f8626b87841095e64127de72&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;27.0&lt;/div&gt;`)[0];
            popup_c6a1c5ea2016e1f73f38c8f420ec2429.setContent(html_895f6520f8626b87841095e64127de72);


        circle_marker_5c9ce0c864bb5dc57e6b7b890a5724c1.bindPopup(popup_c6a1c5ea2016e1f73f38c8f420ec2429)
        ;




            var circle_marker_2d9406d9d9d72e063128f8f008fa2555 = L.circleMarker(
                [40.43674, -3.61056],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_1efee7de623a67ed4186cb7efd03f4ad = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_fe38faf58a41a9e4f949a7d5958c70bf = $(`&lt;div id=&quot;html_fe38faf58a41a9e4f949a7d5958c70bf&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;70.0&lt;/div&gt;`)[0];
            popup_1efee7de623a67ed4186cb7efd03f4ad.setContent(html_fe38faf58a41a9e4f949a7d5958c70bf);


        circle_marker_2d9406d9d9d72e063128f8f008fa2555.bindPopup(popup_1efee7de623a67ed4186cb7efd03f4ad)
        ;




            var circle_marker_80bdc7d548431256fe023d5b2224f53a = L.circleMarker(
                [40.44697, -3.60856],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_46d01e9ea977ede8be714682461083e9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_bfb398827321bc23157473b966805a26 = $(`&lt;div id=&quot;html_bfb398827321bc23157473b966805a26&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;25.0&lt;/div&gt;`)[0];
            popup_46d01e9ea977ede8be714682461083e9.setContent(html_bfb398827321bc23157473b966805a26);


        circle_marker_80bdc7d548431256fe023d5b2224f53a.bindPopup(popup_46d01e9ea977ede8be714682461083e9)
        ;




            var circle_marker_c593ee004fa8c0e5356a33077ab014e2 = L.circleMarker(
                [40.44674, -3.64423],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_59cffce7012350703872b584826bd6a4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a578b9ff8c7304b3685e6ea144682987 = $(`&lt;div id=&quot;html_a578b9ff8c7304b3685e6ea144682987&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;39.0&lt;/div&gt;`)[0];
            popup_59cffce7012350703872b584826bd6a4.setContent(html_a578b9ff8c7304b3685e6ea144682987);


        circle_marker_c593ee004fa8c0e5356a33077ab014e2.bindPopup(popup_59cffce7012350703872b584826bd6a4)
        ;




            var circle_marker_1a6b8167916356c22e5e0edf83d48593 = L.circleMarker(
                [40.42777, -3.62006],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e0d93a8475c96604e0a2fbe0df052515 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e1e70da32fb8e7a9c130559ebd0b99a5 = $(`&lt;div id=&quot;html_e1e70da32fb8e7a9c130559ebd0b99a5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;32.0&lt;/div&gt;`)[0];
            popup_e0d93a8475c96604e0a2fbe0df052515.setContent(html_e1e70da32fb8e7a9c130559ebd0b99a5);


        circle_marker_1a6b8167916356c22e5e0edf83d48593.bindPopup(popup_e0d93a8475c96604e0a2fbe0df052515)
        ;




            var circle_marker_1cd0c171adb86647ee3df521dc90525c = L.circleMarker(
                [40.41883, -3.61888],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ab1f90c51ef474f93c463c53fddf43c1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2db689f0f5dadde4270d13d2d87fc6d7 = $(`&lt;div id=&quot;html_2db689f0f5dadde4270d13d2d87fc6d7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;300.0&lt;/div&gt;`)[0];
            popup_ab1f90c51ef474f93c463c53fddf43c1.setContent(html_2db689f0f5dadde4270d13d2d87fc6d7);


        circle_marker_1cd0c171adb86647ee3df521dc90525c.bindPopup(popup_ab1f90c51ef474f93c463c53fddf43c1)
        ;




            var circle_marker_7126eb244baf7514768c28db1dfb8d56 = L.circleMarker(
                [40.43991, -3.62013],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_7afd3b78cd1f13d2254a5e855024db5a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a3bfe7d05707d243b535424ad57efdd4 = $(`&lt;div id=&quot;html_a3bfe7d05707d243b535424ad57efdd4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;35.0&lt;/div&gt;`)[0];
            popup_7afd3b78cd1f13d2254a5e855024db5a.setContent(html_a3bfe7d05707d243b535424ad57efdd4);


        circle_marker_7126eb244baf7514768c28db1dfb8d56.bindPopup(popup_7afd3b78cd1f13d2254a5e855024db5a)
        ;




            var circle_marker_346333b3b3efeec59450553a4b70de65 = L.circleMarker(
                [40.44742, -3.59655],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8b212c60d7704eea8b960f429738cbca = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_279ed680feb5d7e54d361506d0e7a721 = $(`&lt;div id=&quot;html_279ed680feb5d7e54d361506d0e7a721&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;42.0&lt;/div&gt;`)[0];
            popup_8b212c60d7704eea8b960f429738cbca.setContent(html_279ed680feb5d7e54d361506d0e7a721);


        circle_marker_346333b3b3efeec59450553a4b70de65.bindPopup(popup_8b212c60d7704eea8b960f429738cbca)
        ;




            var circle_marker_e17b42d544266872d3b8b833935d64aa = L.circleMarker(
                [40.42409, -3.60761],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c3c708bf4a43c2cc7cc858b3e7ef4a6a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2199ca64ec94410662373e6a6537de64 = $(`&lt;div id=&quot;html_2199ca64ec94410662373e6a6537de64&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_c3c708bf4a43c2cc7cc858b3e7ef4a6a.setContent(html_2199ca64ec94410662373e6a6537de64);


        circle_marker_e17b42d544266872d3b8b833935d64aa.bindPopup(popup_c3c708bf4a43c2cc7cc858b3e7ef4a6a)
        ;




            var circle_marker_646319144b46d77a68e908cfbb23d9b2 = L.circleMarker(
                [40.4343, -3.61773],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_763e79a894ebe895b3f547f64649d0a9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_92ec40d614cd62b31e6c98e2fbc677b6 = $(`&lt;div id=&quot;html_92ec40d614cd62b31e6c98e2fbc677b6&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_763e79a894ebe895b3f547f64649d0a9.setContent(html_92ec40d614cd62b31e6c98e2fbc677b6);


        circle_marker_646319144b46d77a68e908cfbb23d9b2.bindPopup(popup_763e79a894ebe895b3f547f64649d0a9)
        ;




            var circle_marker_d0278b0e9d9c0e3e881187779549cd78 = L.circleMarker(
                [40.42227, -3.60449],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_db94be9c27556bfc83722d9283107146 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d641915c1bc2632257fe155728c7d89b = $(`&lt;div id=&quot;html_d641915c1bc2632257fe155728c7d89b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;40.0&lt;/div&gt;`)[0];
            popup_db94be9c27556bfc83722d9283107146.setContent(html_d641915c1bc2632257fe155728c7d89b);


        circle_marker_d0278b0e9d9c0e3e881187779549cd78.bindPopup(popup_db94be9c27556bfc83722d9283107146)
        ;




            var circle_marker_18d295c63e4acef273108945c4472053 = L.circleMarker(
                [40.43215, -3.62403],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_687a45ae6f890a0e114eda2205c76e68 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_570a19eaa1f1a197870bf01084fa5eb7 = $(`&lt;div id=&quot;html_570a19eaa1f1a197870bf01084fa5eb7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;635.0&lt;/div&gt;`)[0];
            popup_687a45ae6f890a0e114eda2205c76e68.setContent(html_570a19eaa1f1a197870bf01084fa5eb7);


        circle_marker_18d295c63e4acef273108945c4472053.bindPopup(popup_687a45ae6f890a0e114eda2205c76e68)
        ;




            var circle_marker_bb8e7158128ec6ba0e1bea0c5ba43277 = L.circleMarker(
                [40.43888, -3.62321],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_0a10d6c9fc54605fc2443b9a5af42b89 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_68f2918eb10ffa183bea5117e4a7dccd = $(`&lt;div id=&quot;html_68f2918eb10ffa183bea5117e4a7dccd&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_0a10d6c9fc54605fc2443b9a5af42b89.setContent(html_68f2918eb10ffa183bea5117e4a7dccd);


        circle_marker_bb8e7158128ec6ba0e1bea0c5ba43277.bindPopup(popup_0a10d6c9fc54605fc2443b9a5af42b89)
        ;




            var circle_marker_dcb7dc58ff6e35438f6286a5e94923a9 = L.circleMarker(
                [40.43926, -3.61988],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_6a4481b0421702799ce4931ef417d09a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_501612138391fbb19f9ffa1602516428 = $(`&lt;div id=&quot;html_501612138391fbb19f9ffa1602516428&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;100.0&lt;/div&gt;`)[0];
            popup_6a4481b0421702799ce4931ef417d09a.setContent(html_501612138391fbb19f9ffa1602516428);


        circle_marker_dcb7dc58ff6e35438f6286a5e94923a9.bindPopup(popup_6a4481b0421702799ce4931ef417d09a)
        ;




            var circle_marker_0049ecf0a9dcad1612b6e7facf36ebe1 = L.circleMarker(
                [40.42422, -3.60528],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_1a17e3a6598c4278f9c5c43ceea43b19 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e2076d230a043ef1bf04ad5377d6d0b3 = $(`&lt;div id=&quot;html_e2076d230a043ef1bf04ad5377d6d0b3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;79.0&lt;/div&gt;`)[0];
            popup_1a17e3a6598c4278f9c5c43ceea43b19.setContent(html_e2076d230a043ef1bf04ad5377d6d0b3);


        circle_marker_0049ecf0a9dcad1612b6e7facf36ebe1.bindPopup(popup_1a17e3a6598c4278f9c5c43ceea43b19)
        ;




            var circle_marker_b4f12f84c749a370e4fda40964a6d2c1 = L.circleMarker(
                [40.43128, -3.62661],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3e0acb6d8cb1437940ccd9603104cc24 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_88bbe2b0fbccb1887061aeaff514f2a0 = $(`&lt;div id=&quot;html_88bbe2b0fbccb1887061aeaff514f2a0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;21.0&lt;/div&gt;`)[0];
            popup_3e0acb6d8cb1437940ccd9603104cc24.setContent(html_88bbe2b0fbccb1887061aeaff514f2a0);


        circle_marker_b4f12f84c749a370e4fda40964a6d2c1.bindPopup(popup_3e0acb6d8cb1437940ccd9603104cc24)
        ;




            var circle_marker_b5e7d938b10cccf1325d315356e91d5a = L.circleMarker(
                [40.43867, -3.61125],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_cf14a1dfe64644517ed63dc12bb9f72f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_06590699a35d62a36e67feb980e0c621 = $(`&lt;div id=&quot;html_06590699a35d62a36e67feb980e0c621&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;657.0&lt;/div&gt;`)[0];
            popup_cf14a1dfe64644517ed63dc12bb9f72f.setContent(html_06590699a35d62a36e67feb980e0c621);


        circle_marker_b5e7d938b10cccf1325d315356e91d5a.bindPopup(popup_cf14a1dfe64644517ed63dc12bb9f72f)
        ;




            var circle_marker_1d92f5e5c699e76530149e82577d43b4 = L.circleMarker(
                [40.42389, -3.62255],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f37ee9c495e36afbabe737c96eff363e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0fef421181d5812036d1885a7eb48a53 = $(`&lt;div id=&quot;html_0fef421181d5812036d1885a7eb48a53&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;26.0&lt;/div&gt;`)[0];
            popup_f37ee9c495e36afbabe737c96eff363e.setContent(html_0fef421181d5812036d1885a7eb48a53);


        circle_marker_1d92f5e5c699e76530149e82577d43b4.bindPopup(popup_f37ee9c495e36afbabe737c96eff363e)
        ;




            var circle_marker_7178bf7c3a26d20995b0390949f6e7f8 = L.circleMarker(
                [40.43442, -3.60787],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_1456bd6a3f75683e8c140f8a08957ce4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_dd0ec2574044ce0a1adc5958a87ae57f = $(`&lt;div id=&quot;html_dd0ec2574044ce0a1adc5958a87ae57f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;84.0&lt;/div&gt;`)[0];
            popup_1456bd6a3f75683e8c140f8a08957ce4.setContent(html_dd0ec2574044ce0a1adc5958a87ae57f);


        circle_marker_7178bf7c3a26d20995b0390949f6e7f8.bindPopup(popup_1456bd6a3f75683e8c140f8a08957ce4)
        ;




            var circle_marker_d63042254b73ac108ba39c193c3d2d15 = L.circleMarker(
                [40.44443, -3.58635],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_20f9ca9e6d814bfd11ab976d8171b1ee = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_054b8bb521e02b76fc4261d6d9c24cd2 = $(`&lt;div id=&quot;html_054b8bb521e02b76fc4261d6d9c24cd2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;85.0&lt;/div&gt;`)[0];
            popup_20f9ca9e6d814bfd11ab976d8171b1ee.setContent(html_054b8bb521e02b76fc4261d6d9c24cd2);


        circle_marker_d63042254b73ac108ba39c193c3d2d15.bindPopup(popup_20f9ca9e6d814bfd11ab976d8171b1ee)
        ;




            var circle_marker_cd0ee7e97cfbd15faca2201a64614732 = L.circleMarker(
                [40.44512, -3.58262],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_2123abddd1c96821eb65ecb1adee848c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9eced2e3ecb5f016af87d6d5ba244b55 = $(`&lt;div id=&quot;html_9eced2e3ecb5f016af87d6d5ba244b55&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_2123abddd1c96821eb65ecb1adee848c.setContent(html_9eced2e3ecb5f016af87d6d5ba244b55);


        circle_marker_cd0ee7e97cfbd15faca2201a64614732.bindPopup(popup_2123abddd1c96821eb65ecb1adee848c)
        ;




            var circle_marker_d0f8d7b85ace4fca80a4a0e90fc5b454 = L.circleMarker(
                [40.44799, -3.61047],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a36aadbbaad049804d7fdc0af9686e7d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_fbd4435c58fdcfde550d4e409b680cea = $(`&lt;div id=&quot;html_fbd4435c58fdcfde550d4e409b680cea&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;56.0&lt;/div&gt;`)[0];
            popup_a36aadbbaad049804d7fdc0af9686e7d.setContent(html_fbd4435c58fdcfde550d4e409b680cea);


        circle_marker_d0f8d7b85ace4fca80a4a0e90fc5b454.bindPopup(popup_a36aadbbaad049804d7fdc0af9686e7d)
        ;




            var circle_marker_286e3379ff8aa55e9f3ad5135fd3d35c = L.circleMarker(
                [40.44556, -3.61267],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_52fd2f7ff9e207b5f98efcccd82ab586 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_34c0ac61a06fed6ef8f509675beb8697 = $(`&lt;div id=&quot;html_34c0ac61a06fed6ef8f509675beb8697&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;200.0&lt;/div&gt;`)[0];
            popup_52fd2f7ff9e207b5f98efcccd82ab586.setContent(html_34c0ac61a06fed6ef8f509675beb8697);


        circle_marker_286e3379ff8aa55e9f3ad5135fd3d35c.bindPopup(popup_52fd2f7ff9e207b5f98efcccd82ab586)
        ;




            var circle_marker_adf7003095136764154aed92c9fb2436 = L.circleMarker(
                [40.44083, -3.6102],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f00b233cd66280b494f8bbd0ce725baf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_038ab8dba958a336bbb0096783cca04c = $(`&lt;div id=&quot;html_038ab8dba958a336bbb0096783cca04c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;35.0&lt;/div&gt;`)[0];
            popup_f00b233cd66280b494f8bbd0ce725baf.setContent(html_038ab8dba958a336bbb0096783cca04c);


        circle_marker_adf7003095136764154aed92c9fb2436.bindPopup(popup_f00b233cd66280b494f8bbd0ce725baf)
        ;




            var circle_marker_4b947ecba2fd13ef858ae8af301e69bc = L.circleMarker(
                [40.42923, -3.61234],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f147cf725710e3202950905839c7d9b1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1c4295fa310c2510b8e26f9d9b57ca77 = $(`&lt;div id=&quot;html_1c4295fa310c2510b8e26f9d9b57ca77&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;200.0&lt;/div&gt;`)[0];
            popup_f147cf725710e3202950905839c7d9b1.setContent(html_1c4295fa310c2510b8e26f9d9b57ca77);


        circle_marker_4b947ecba2fd13ef858ae8af301e69bc.bindPopup(popup_f147cf725710e3202950905839c7d9b1)
        ;




            var circle_marker_16f57f9e70f39cf12bfb849b28e442ad = L.circleMarker(
                [40.42191, -3.61333],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d622ef7a2bf3260fe068740e7b70e06a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e8d3e129af2f15f54a2781851876a78f = $(`&lt;div id=&quot;html_e8d3e129af2f15f54a2781851876a78f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;100.0&lt;/div&gt;`)[0];
            popup_d622ef7a2bf3260fe068740e7b70e06a.setContent(html_e8d3e129af2f15f54a2781851876a78f);


        circle_marker_16f57f9e70f39cf12bfb849b28e442ad.bindPopup(popup_d622ef7a2bf3260fe068740e7b70e06a)
        ;




            var circle_marker_aac5dc1fe8941c06cbe77e5c001a2865 = L.circleMarker(
                [40.43686, -3.61093],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a955ab8ced3114214b48fb66f46fdd0b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e37c1cf54047906ce5e870be175520f2 = $(`&lt;div id=&quot;html_e37c1cf54047906ce5e870be175520f2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;4200.0&lt;/div&gt;`)[0];
            popup_a955ab8ced3114214b48fb66f46fdd0b.setContent(html_e37c1cf54047906ce5e870be175520f2);


        circle_marker_aac5dc1fe8941c06cbe77e5c001a2865.bindPopup(popup_a955ab8ced3114214b48fb66f46fdd0b)
        ;




            var circle_marker_de871f12d7a9fc46dcd3f9d751d530d3 = L.circleMarker(
                [40.42363, -3.60378],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_fc5f1dcabb5a900935ce07dd0eb0a916 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e1b3d0f5ccd70eeccae86a56e615f3ed = $(`&lt;div id=&quot;html_e1b3d0f5ccd70eeccae86a56e615f3ed&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;150.0&lt;/div&gt;`)[0];
            popup_fc5f1dcabb5a900935ce07dd0eb0a916.setContent(html_e1b3d0f5ccd70eeccae86a56e615f3ed);


        circle_marker_de871f12d7a9fc46dcd3f9d751d530d3.bindPopup(popup_fc5f1dcabb5a900935ce07dd0eb0a916)
        ;




            var circle_marker_2c967ffa886842dd8b477a1e12e78516 = L.circleMarker(
                [40.43182, -3.60349],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_731f0c17a5253276027fa5515697f823 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_715eee2f7f573a55693f0265c24da8ff = $(`&lt;div id=&quot;html_715eee2f7f573a55693f0265c24da8ff&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;800.0&lt;/div&gt;`)[0];
            popup_731f0c17a5253276027fa5515697f823.setContent(html_715eee2f7f573a55693f0265c24da8ff);


        circle_marker_2c967ffa886842dd8b477a1e12e78516.bindPopup(popup_731f0c17a5253276027fa5515697f823)
        ;




            var circle_marker_0a5a4c24fb3aec3b46a5ad74e7e0c11f = L.circleMarker(
                [40.43331, -3.61724],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_84b4492ec98ced17978159a6e74e3130 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2f6b692ae39d9722aab9aa7cb8eab37a = $(`&lt;div id=&quot;html_2f6b692ae39d9722aab9aa7cb8eab37a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;315.0&lt;/div&gt;`)[0];
            popup_84b4492ec98ced17978159a6e74e3130.setContent(html_2f6b692ae39d9722aab9aa7cb8eab37a);


        circle_marker_0a5a4c24fb3aec3b46a5ad74e7e0c11f.bindPopup(popup_84b4492ec98ced17978159a6e74e3130)
        ;




            var circle_marker_a06006cab27915b11ba1f35fab71af9c = L.circleMarker(
                [40.44589, -3.61518],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f77754197aee77216ef701d618416b99 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_de04b1f9c5ea06ca67ab6bb1d9a70b75 = $(`&lt;div id=&quot;html_de04b1f9c5ea06ca67ab6bb1d9a70b75&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;70.0&lt;/div&gt;`)[0];
            popup_f77754197aee77216ef701d618416b99.setContent(html_de04b1f9c5ea06ca67ab6bb1d9a70b75);


        circle_marker_a06006cab27915b11ba1f35fab71af9c.bindPopup(popup_f77754197aee77216ef701d618416b99)
        ;




            var circle_marker_2da7bf3de8d229707f1b0a8039cc72e7 = L.circleMarker(
                [40.43761, -3.6311],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_19f1478790d09c4a2ce05ec7007efd24 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7240c4552e916a975076343b2aa7e3e0 = $(`&lt;div id=&quot;html_7240c4552e916a975076343b2aa7e3e0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;250.0&lt;/div&gt;`)[0];
            popup_19f1478790d09c4a2ce05ec7007efd24.setContent(html_7240c4552e916a975076343b2aa7e3e0);


        circle_marker_2da7bf3de8d229707f1b0a8039cc72e7.bindPopup(popup_19f1478790d09c4a2ce05ec7007efd24)
        ;




            var circle_marker_827e264f25e6dfa4ae5d3a978d4edf48 = L.circleMarker(
                [40.44863, -3.60335],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_70bdd37446cee4b913f64faa0040a217 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9a7adb54407e5ff2485dee9989b734e7 = $(`&lt;div id=&quot;html_9a7adb54407e5ff2485dee9989b734e7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1450.0&lt;/div&gt;`)[0];
            popup_70bdd37446cee4b913f64faa0040a217.setContent(html_9a7adb54407e5ff2485dee9989b734e7);


        circle_marker_827e264f25e6dfa4ae5d3a978d4edf48.bindPopup(popup_70bdd37446cee4b913f64faa0040a217)
        ;




            var circle_marker_7742c17ba41a0ea895895fc88e4ba949 = L.circleMarker(
                [40.43502, -3.62565],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3d40a0b67c7bbfcabd62e11fff4527df = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7107a5f6495db4e135fd77b78c3b9081 = $(`&lt;div id=&quot;html_7107a5f6495db4e135fd77b78c3b9081&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;2600.0&lt;/div&gt;`)[0];
            popup_3d40a0b67c7bbfcabd62e11fff4527df.setContent(html_7107a5f6495db4e135fd77b78c3b9081);


        circle_marker_7742c17ba41a0ea895895fc88e4ba949.bindPopup(popup_3d40a0b67c7bbfcabd62e11fff4527df)
        ;




            var circle_marker_f614d8ce25e25edd402d7752c4469441 = L.circleMarker(
                [40.4352, -3.61265],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ffc0c64c390bc96627d54553c1e45d34 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d924d1a8a5f526dfdcb1b7c3eee5ea01 = $(`&lt;div id=&quot;html_d924d1a8a5f526dfdcb1b7c3eee5ea01&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;600.0&lt;/div&gt;`)[0];
            popup_ffc0c64c390bc96627d54553c1e45d34.setContent(html_d924d1a8a5f526dfdcb1b7c3eee5ea01);


        circle_marker_f614d8ce25e25edd402d7752c4469441.bindPopup(popup_ffc0c64c390bc96627d54553c1e45d34)
        ;




            var circle_marker_526fa3c9ed0c15e9892672449a89bee6 = L.circleMarker(
                [40.43, -3.60694],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9c078283d10e81668250236c4b1c93f7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_89db8ee817d9477c93b68ef06d1f0fcf = $(`&lt;div id=&quot;html_89db8ee817d9477c93b68ef06d1f0fcf&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1330.0&lt;/div&gt;`)[0];
            popup_9c078283d10e81668250236c4b1c93f7.setContent(html_89db8ee817d9477c93b68ef06d1f0fcf);


        circle_marker_526fa3c9ed0c15e9892672449a89bee6.bindPopup(popup_9c078283d10e81668250236c4b1c93f7)
        ;




            var circle_marker_ee882c185c982749c5e85890ca459072 = L.circleMarker(
                [40.44383, -3.62319],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_0d4f52559060cd4da83c21f80afc1a9e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4e2c3270ea1c82c4181f04325a0e8983 = $(`&lt;div id=&quot;html_4e2c3270ea1c82c4181f04325a0e8983&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;294.0&lt;/div&gt;`)[0];
            popup_0d4f52559060cd4da83c21f80afc1a9e.setContent(html_4e2c3270ea1c82c4181f04325a0e8983);


        circle_marker_ee882c185c982749c5e85890ca459072.bindPopup(popup_0d4f52559060cd4da83c21f80afc1a9e)
        ;




            var circle_marker_581af660c9d29472d7727b0f6745cef1 = L.circleMarker(
                [40.44853, -3.60137],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_225d20937bf26dfc59b4675c43b6dd1a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6fdab4d5a60a40e03817e6e9ccc9cbef = $(`&lt;div id=&quot;html_6fdab4d5a60a40e03817e6e9ccc9cbef&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1700.0&lt;/div&gt;`)[0];
            popup_225d20937bf26dfc59b4675c43b6dd1a.setContent(html_6fdab4d5a60a40e03817e6e9ccc9cbef);


        circle_marker_581af660c9d29472d7727b0f6745cef1.bindPopup(popup_225d20937bf26dfc59b4675c43b6dd1a)
        ;




            var circle_marker_547976599dafb777787e0e532869fc57 = L.circleMarker(
                [40.42986, -3.60531],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_977edc6f612b17aa709b04f428ac3d19 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_8311ffa8c5433edf20a3d95753e611b0 = $(`&lt;div id=&quot;html_8311ffa8c5433edf20a3d95753e611b0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;266.0&lt;/div&gt;`)[0];
            popup_977edc6f612b17aa709b04f428ac3d19.setContent(html_8311ffa8c5433edf20a3d95753e611b0);


        circle_marker_547976599dafb777787e0e532869fc57.bindPopup(popup_977edc6f612b17aa709b04f428ac3d19)
        ;




            var circle_marker_6879e49b845def125bd392a0876b0896 = L.circleMarker(
                [40.43598, -3.60904],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a2d258368b4ed5fd5de5054c9b4e00c9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_28a96f588b47b768617616f0b22e3200 = $(`&lt;div id=&quot;html_28a96f588b47b768617616f0b22e3200&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;850.0&lt;/div&gt;`)[0];
            popup_a2d258368b4ed5fd5de5054c9b4e00c9.setContent(html_28a96f588b47b768617616f0b22e3200);


        circle_marker_6879e49b845def125bd392a0876b0896.bindPopup(popup_a2d258368b4ed5fd5de5054c9b4e00c9)
        ;




            var circle_marker_6cb443064bc3ff718115c844ccd75f45 = L.circleMarker(
                [40.43715, -3.61812],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_88cc4f929a76ff4d2d8353e98e5b9ab8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9ce20c7d63c576cf1c6a71f584e0cd9e = $(`&lt;div id=&quot;html_9ce20c7d63c576cf1c6a71f584e0cd9e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;2100.0&lt;/div&gt;`)[0];
            popup_88cc4f929a76ff4d2d8353e98e5b9ab8.setContent(html_9ce20c7d63c576cf1c6a71f584e0cd9e);


        circle_marker_6cb443064bc3ff718115c844ccd75f45.bindPopup(popup_88cc4f929a76ff4d2d8353e98e5b9ab8)
        ;




            var circle_marker_d6133b3ca24217aa77bbb7b702d97316 = L.circleMarker(
                [40.43743, -3.60758],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e7c516aaaed41314e4f0710571cf2303 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d951563a89d91f4e6cdefee0c458957d = $(`&lt;div id=&quot;html_d951563a89d91f4e6cdefee0c458957d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.0&lt;/div&gt;`)[0];
            popup_e7c516aaaed41314e4f0710571cf2303.setContent(html_d951563a89d91f4e6cdefee0c458957d);


        circle_marker_d6133b3ca24217aa77bbb7b702d97316.bindPopup(popup_e7c516aaaed41314e4f0710571cf2303)
        ;




            var circle_marker_b3f6fa81884ca70aa70790cb7dc86a08 = L.circleMarker(
                [40.43409, -3.60753],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5b1750f047bab421ae03968448252892 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_09b50a35818ab0531ca84d0324d813c9 = $(`&lt;div id=&quot;html_09b50a35818ab0531ca84d0324d813c9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1994.9999999999998&lt;/div&gt;`)[0];
            popup_5b1750f047bab421ae03968448252892.setContent(html_09b50a35818ab0531ca84d0324d813c9);


        circle_marker_b3f6fa81884ca70aa70790cb7dc86a08.bindPopup(popup_5b1750f047bab421ae03968448252892)
        ;




            var circle_marker_429741995e1479e624858aec0583783d = L.circleMarker(
                [40.42105, -3.61457],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_78f73aa9fc8bc86eaec944e9d2f30c4c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_f876bd8eebb46833f5f6535ac526a2e8 = $(`&lt;div id=&quot;html_f876bd8eebb46833f5f6535ac526a2e8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;9800.0&lt;/div&gt;`)[0];
            popup_78f73aa9fc8bc86eaec944e9d2f30c4c.setContent(html_f876bd8eebb46833f5f6535ac526a2e8);


        circle_marker_429741995e1479e624858aec0583783d.bindPopup(popup_78f73aa9fc8bc86eaec944e9d2f30c4c)
        ;




            var circle_marker_4cae6d3e3091262e5e00eb7adfe90966 = L.circleMarker(
                [40.43045, -3.61315],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_683b04c7cfd5c693664bc8d114ff21e9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_34774a154c69a4e8f979ce662bfa2edf = $(`&lt;div id=&quot;html_34774a154c69a4e8f979ce662bfa2edf&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;40.0&lt;/div&gt;`)[0];
            popup_683b04c7cfd5c693664bc8d114ff21e9.setContent(html_34774a154c69a4e8f979ce662bfa2edf);


        circle_marker_4cae6d3e3091262e5e00eb7adfe90966.bindPopup(popup_683b04c7cfd5c693664bc8d114ff21e9)
        ;




            var circle_marker_c40a35de58b7a00178b470dca0c6bd03 = L.circleMarker(
                [40.44437, -3.61309],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c8a32a4823f76db03c25a56ccf3ddff9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d632bcaec5772085cf4b91d4537152ed = $(`&lt;div id=&quot;html_d632bcaec5772085cf4b91d4537152ed&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;800.0&lt;/div&gt;`)[0];
            popup_c8a32a4823f76db03c25a56ccf3ddff9.setContent(html_d632bcaec5772085cf4b91d4537152ed);


        circle_marker_c40a35de58b7a00178b470dca0c6bd03.bindPopup(popup_c8a32a4823f76db03c25a56ccf3ddff9)
        ;




            var circle_marker_c37a4dcf4b5db651a118f5120650e95b = L.circleMarker(
                [40.41995, -3.6176],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_6242b1b965664f8636a9ec04b882c60f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b4286b9acea63027ed5e6120e970f313 = $(`&lt;div id=&quot;html_b4286b9acea63027ed5e6120e970f313&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1400.0&lt;/div&gt;`)[0];
            popup_6242b1b965664f8636a9ec04b882c60f.setContent(html_b4286b9acea63027ed5e6120e970f313);


        circle_marker_c37a4dcf4b5db651a118f5120650e95b.bindPopup(popup_6242b1b965664f8636a9ec04b882c60f)
        ;




            var circle_marker_d7f006ab0bbbb36d80967e1683c1157b = L.circleMarker(
                [40.43082, -3.60461],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_36a628b17a8f96519a94308d06d0d246 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e1ba3e258bc9630f12d1d405541c4c71 = $(`&lt;div id=&quot;html_e1ba3e258bc9630f12d1d405541c4c71&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1260.0&lt;/div&gt;`)[0];
            popup_36a628b17a8f96519a94308d06d0d246.setContent(html_e1ba3e258bc9630f12d1d405541c4c71);


        circle_marker_d7f006ab0bbbb36d80967e1683c1157b.bindPopup(popup_36a628b17a8f96519a94308d06d0d246)
        ;




            var circle_marker_b8ffd985080f52ad19d5659b527c8536 = L.circleMarker(
                [40.42805, -3.61584],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_118acff95f1e3fca6620b95f3deb8b93 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a3eb17410c0ab02ae6d64e17f7842c33 = $(`&lt;div id=&quot;html_a3eb17410c0ab02ae6d64e17f7842c33&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;400.0&lt;/div&gt;`)[0];
            popup_118acff95f1e3fca6620b95f3deb8b93.setContent(html_a3eb17410c0ab02ae6d64e17f7842c33);


        circle_marker_b8ffd985080f52ad19d5659b527c8536.bindPopup(popup_118acff95f1e3fca6620b95f3deb8b93)
        ;




            var circle_marker_8ca40eb9b48df137723640f34de929a9 = L.circleMarker(
                [40.44567, -3.6097],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_126ffc4a713cad3acff4b4226a66f1e3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_cc0569716d7c1cffc19fe8d4350f829f = $(`&lt;div id=&quot;html_cc0569716d7c1cffc19fe8d4350f829f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;2000.0&lt;/div&gt;`)[0];
            popup_126ffc4a713cad3acff4b4226a66f1e3.setContent(html_cc0569716d7c1cffc19fe8d4350f829f);


        circle_marker_8ca40eb9b48df137723640f34de929a9.bindPopup(popup_126ffc4a713cad3acff4b4226a66f1e3)
        ;




            var circle_marker_057565e5bf6ddf33b3a9ab31afb3e02e = L.circleMarker(
                [40.43418, -3.62518],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b2283349ef1b38c7bd70f48ff3f02e8e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_8091f5d972a338f65c464348421ea5f3 = $(`&lt;div id=&quot;html_8091f5d972a338f65c464348421ea5f3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1470.0&lt;/div&gt;`)[0];
            popup_b2283349ef1b38c7bd70f48ff3f02e8e.setContent(html_8091f5d972a338f65c464348421ea5f3);


        circle_marker_057565e5bf6ddf33b3a9ab31afb3e02e.bindPopup(popup_b2283349ef1b38c7bd70f48ff3f02e8e)
        ;




            var circle_marker_fdbb121e4defd201cc557791bbcebe9a = L.circleMarker(
                [40.42053, -3.62031],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3c760ca9e69258cca3cffd7a88ae29f6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ce74640bddc33458bb0d27f2944f9253 = $(`&lt;div id=&quot;html_ce74640bddc33458bb0d27f2944f9253&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;75.0&lt;/div&gt;`)[0];
            popup_3c760ca9e69258cca3cffd7a88ae29f6.setContent(html_ce74640bddc33458bb0d27f2944f9253);


        circle_marker_fdbb121e4defd201cc557791bbcebe9a.bindPopup(popup_3c760ca9e69258cca3cffd7a88ae29f6)
        ;




            var circle_marker_d166f4a105623a3b01029b9d32af209c = L.circleMarker(
                [40.43697, -3.608],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3cc67c820a4da901e6d18319814848d6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0fabe04aefa3774d65226da1683f51a3 = $(`&lt;div id=&quot;html_0fabe04aefa3774d65226da1683f51a3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_3cc67c820a4da901e6d18319814848d6.setContent(html_0fabe04aefa3774d65226da1683f51a3);


        circle_marker_d166f4a105623a3b01029b9d32af209c.bindPopup(popup_3cc67c820a4da901e6d18319814848d6)
        ;




            var circle_marker_e4b1d0fcabefaf6e9964479d54fff724 = L.circleMarker(
                [40.43538, -3.60719],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_555edb5ff52bb34315556ce22fc898c6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_daf5fc1143fc22b80f4715c754c733ae = $(`&lt;div id=&quot;html_daf5fc1143fc22b80f4715c754c733ae&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;480.0&lt;/div&gt;`)[0];
            popup_555edb5ff52bb34315556ce22fc898c6.setContent(html_daf5fc1143fc22b80f4715c754c733ae);


        circle_marker_e4b1d0fcabefaf6e9964479d54fff724.bindPopup(popup_555edb5ff52bb34315556ce22fc898c6)
        ;




            var circle_marker_03c8f6f09db9e80230a19eb7deb7c784 = L.circleMarker(
                [40.42705, -3.62679],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_bb68ff439c9039180dee04e15ccbe97b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4a0e740e894a39b82e59276896de1699 = $(`&lt;div id=&quot;html_4a0e740e894a39b82e59276896de1699&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;250.0&lt;/div&gt;`)[0];
            popup_bb68ff439c9039180dee04e15ccbe97b.setContent(html_4a0e740e894a39b82e59276896de1699);


        circle_marker_03c8f6f09db9e80230a19eb7deb7c784.bindPopup(popup_bb68ff439c9039180dee04e15ccbe97b)
        ;




            var circle_marker_2abba8578f9c1c89ad8009350a7a2fb6 = L.circleMarker(
                [40.44435, -3.58328],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_755f2acf9ad0042ef3e01652c85266cf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d80a063c2feee398935639691a4c5564 = $(`&lt;div id=&quot;html_d80a063c2feee398935639691a4c5564&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1200.0&lt;/div&gt;`)[0];
            popup_755f2acf9ad0042ef3e01652c85266cf.setContent(html_d80a063c2feee398935639691a4c5564);


        circle_marker_2abba8578f9c1c89ad8009350a7a2fb6.bindPopup(popup_755f2acf9ad0042ef3e01652c85266cf)
        ;




            var circle_marker_4f2dd985bb5ece337bc6c99c7428842e = L.circleMarker(
                [40.44738, -3.60776],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_96b9919d46c201c62a00188898cf8f8f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_702f2eb1885c95be976778cab394ac8d = $(`&lt;div id=&quot;html_702f2eb1885c95be976778cab394ac8d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1050.0&lt;/div&gt;`)[0];
            popup_96b9919d46c201c62a00188898cf8f8f.setContent(html_702f2eb1885c95be976778cab394ac8d);


        circle_marker_4f2dd985bb5ece337bc6c99c7428842e.bindPopup(popup_96b9919d46c201c62a00188898cf8f8f)
        ;




            var circle_marker_344975b33434d3cf0e5e43cf4c2066a8 = L.circleMarker(
                [40.42447, -3.60233],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a5212d2609d0d393225d7efd3fefe388 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_dd107ef90bcd8c5e43b22f3db09e4f02 = $(`&lt;div id=&quot;html_dd107ef90bcd8c5e43b22f3db09e4f02&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;450.0&lt;/div&gt;`)[0];
            popup_a5212d2609d0d393225d7efd3fefe388.setContent(html_dd107ef90bcd8c5e43b22f3db09e4f02);


        circle_marker_344975b33434d3cf0e5e43cf4c2066a8.bindPopup(popup_a5212d2609d0d393225d7efd3fefe388)
        ;




            var circle_marker_6562bb29d601dbc7c92138da7ad5da4c = L.circleMarker(
                [40.44276, -3.61222],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_776a18ef0f6bc5852ef66be0403ec82b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a095092d55725691e31512df6a3135d8 = $(`&lt;div id=&quot;html_a095092d55725691e31512df6a3135d8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;2200.0&lt;/div&gt;`)[0];
            popup_776a18ef0f6bc5852ef66be0403ec82b.setContent(html_a095092d55725691e31512df6a3135d8);


        circle_marker_6562bb29d601dbc7c92138da7ad5da4c.bindPopup(popup_776a18ef0f6bc5852ef66be0403ec82b)
        ;




            var circle_marker_f012cc2853df3309cf832a8e33cd4108 = L.circleMarker(
                [40.44857, -3.6136],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e6650b7cb1d9e35ddb2b4366c3e9236d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_60b8892fc8db51d963617d1ec9531a1c = $(`&lt;div id=&quot;html_60b8892fc8db51d963617d1ec9531a1c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;2300.0&lt;/div&gt;`)[0];
            popup_e6650b7cb1d9e35ddb2b4366c3e9236d.setContent(html_60b8892fc8db51d963617d1ec9531a1c);


        circle_marker_f012cc2853df3309cf832a8e33cd4108.bindPopup(popup_e6650b7cb1d9e35ddb2b4366c3e9236d)
        ;




            var circle_marker_2e5212eab83385e70b31bb288e3cc8fd = L.circleMarker(
                [40.42997, -3.60505],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_64fa4d2cb80795716792037527fcc40d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_61e87598fe8e9679ebc2b04c6e1145d9 = $(`&lt;div id=&quot;html_61e87598fe8e9679ebc2b04c6e1145d9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1500.0&lt;/div&gt;`)[0];
            popup_64fa4d2cb80795716792037527fcc40d.setContent(html_61e87598fe8e9679ebc2b04c6e1145d9);


        circle_marker_2e5212eab83385e70b31bb288e3cc8fd.bindPopup(popup_64fa4d2cb80795716792037527fcc40d)
        ;




            var circle_marker_ab60dfb286cca6e9df17b51626c5ebdd = L.circleMarker(
                [40.42133, -3.61068],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_515d71b3fe14a2f3e84463133cbf5228 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_23a656831ad5ee892c06aeae4c871b3b = $(`&lt;div id=&quot;html_23a656831ad5ee892c06aeae4c871b3b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_515d71b3fe14a2f3e84463133cbf5228.setContent(html_23a656831ad5ee892c06aeae4c871b3b);


        circle_marker_ab60dfb286cca6e9df17b51626c5ebdd.bindPopup(popup_515d71b3fe14a2f3e84463133cbf5228)
        ;




            var circle_marker_20fa8bfc05b6af43530aec5d05bf5568 = L.circleMarker(
                [40.44331, -3.6155],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_40506716711112f231975f32d14b2a50 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d9777a6cf27f093627e85a6a5e54fe5d = $(`&lt;div id=&quot;html_d9777a6cf27f093627e85a6a5e54fe5d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;300.0&lt;/div&gt;`)[0];
            popup_40506716711112f231975f32d14b2a50.setContent(html_d9777a6cf27f093627e85a6a5e54fe5d);


        circle_marker_20fa8bfc05b6af43530aec5d05bf5568.bindPopup(popup_40506716711112f231975f32d14b2a50)
        ;




            var circle_marker_756814951e7dc7cba7be4ac587895122 = L.circleMarker(
                [40.42759, -3.6039],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a76986ce7046c201384eae0cdc2edcdb = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_5efcdb1063f1826e7eb155d3aa06e071 = $(`&lt;div id=&quot;html_5efcdb1063f1826e7eb155d3aa06e071&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;800.0&lt;/div&gt;`)[0];
            popup_a76986ce7046c201384eae0cdc2edcdb.setContent(html_5efcdb1063f1826e7eb155d3aa06e071);


        circle_marker_756814951e7dc7cba7be4ac587895122.bindPopup(popup_a76986ce7046c201384eae0cdc2edcdb)
        ;




            var circle_marker_d5aa168b1317a6ba0315c4f111df7666 = L.circleMarker(
                [40.44596, -3.59433],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_86402cf24114e5f728e77dee64ba04c6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a5014da3a8bb2c1e237332c587c17938 = $(`&lt;div id=&quot;html_a5014da3a8bb2c1e237332c587c17938&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_86402cf24114e5f728e77dee64ba04c6.setContent(html_a5014da3a8bb2c1e237332c587c17938);


        circle_marker_d5aa168b1317a6ba0315c4f111df7666.bindPopup(popup_86402cf24114e5f728e77dee64ba04c6)
        ;




            var circle_marker_34144098a3cd6df904946c51c7e14fdd = L.circleMarker(
                [40.44555, -3.58619],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8118e66b78ceba316766adb8f32bce5c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_80d48c0ff9e72bb792ae4bf684052b76 = $(`&lt;div id=&quot;html_80d48c0ff9e72bb792ae4bf684052b76&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;800.0&lt;/div&gt;`)[0];
            popup_8118e66b78ceba316766adb8f32bce5c.setContent(html_80d48c0ff9e72bb792ae4bf684052b76);


        circle_marker_34144098a3cd6df904946c51c7e14fdd.bindPopup(popup_8118e66b78ceba316766adb8f32bce5c)
        ;




            var circle_marker_c1bf6087e296caf396aa06a955e12c43 = L.circleMarker(
                [40.42482, -3.61998],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_23f5088947a37aab8ecc4b88a688b1d2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_f4b3a25c10a24645e0f842cc35f3606f = $(`&lt;div id=&quot;html_f4b3a25c10a24645e0f842cc35f3606f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1200.0&lt;/div&gt;`)[0];
            popup_23f5088947a37aab8ecc4b88a688b1d2.setContent(html_f4b3a25c10a24645e0f842cc35f3606f);


        circle_marker_c1bf6087e296caf396aa06a955e12c43.bindPopup(popup_23f5088947a37aab8ecc4b88a688b1d2)
        ;




            var circle_marker_8c664679e272d6f731d3ec57c5d6bb74 = L.circleMarker(
                [40.43011, -3.60361],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a684492d5c5e9e0d84c79b28b8a3cd06 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e2b18f8f734b1872e97d453b217b5360 = $(`&lt;div id=&quot;html_e2b18f8f734b1872e97d453b217b5360&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;700.0&lt;/div&gt;`)[0];
            popup_a684492d5c5e9e0d84c79b28b8a3cd06.setContent(html_e2b18f8f734b1872e97d453b217b5360);


        circle_marker_8c664679e272d6f731d3ec57c5d6bb74.bindPopup(popup_a684492d5c5e9e0d84c79b28b8a3cd06)
        ;




            var circle_marker_307ba722cb32346dbb852c4ef6dfb8d3 = L.circleMarker(
                [40.44288, -3.58168],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d722122006149e439c5903bdc86c8d94 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a5e6ff03325ad3f7504520e97f7379f5 = $(`&lt;div id=&quot;html_a5e6ff03325ad3f7504520e97f7379f5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;55.0&lt;/div&gt;`)[0];
            popup_d722122006149e439c5903bdc86c8d94.setContent(html_a5e6ff03325ad3f7504520e97f7379f5);


        circle_marker_307ba722cb32346dbb852c4ef6dfb8d3.bindPopup(popup_d722122006149e439c5903bdc86c8d94)
        ;




            var circle_marker_a573c5f86343943f4fd54595207655c1 = L.circleMarker(
                [40.44528, -3.62616],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ffbd725f8c77bb8fd5ce154b639894d9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_69df48e6d07522411ffb600ba80f54da = $(`&lt;div id=&quot;html_69df48e6d07522411ffb600ba80f54da&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;400.0&lt;/div&gt;`)[0];
            popup_ffbd725f8c77bb8fd5ce154b639894d9.setContent(html_69df48e6d07522411ffb600ba80f54da);


        circle_marker_a573c5f86343943f4fd54595207655c1.bindPopup(popup_ffbd725f8c77bb8fd5ce154b639894d9)
        ;




            var circle_marker_3673a017801295d9ed79aa0167129a6c = L.circleMarker(
                [40.42779, -3.61478],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_463e4c6ee630406a9d783d9c64c1bba4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_36abc4ca44868cc94084c634325a9b0a = $(`&lt;div id=&quot;html_36abc4ca44868cc94084c634325a9b0a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1659.0&lt;/div&gt;`)[0];
            popup_463e4c6ee630406a9d783d9c64c1bba4.setContent(html_36abc4ca44868cc94084c634325a9b0a);


        circle_marker_3673a017801295d9ed79aa0167129a6c.bindPopup(popup_463e4c6ee630406a9d783d9c64c1bba4)
        ;




            var circle_marker_ab6bc0721d6860b59b03691113f4e02e = L.circleMarker(
                [40.43521, -3.59904],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_978c8e150a26718e00c3da397841ab22 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2cdda1b76fb28325cc0b65974cf0aedd = $(`&lt;div id=&quot;html_2cdda1b76fb28325cc0b65974cf0aedd&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1100.0&lt;/div&gt;`)[0];
            popup_978c8e150a26718e00c3da397841ab22.setContent(html_2cdda1b76fb28325cc0b65974cf0aedd);


        circle_marker_ab6bc0721d6860b59b03691113f4e02e.bindPopup(popup_978c8e150a26718e00c3da397841ab22)
        ;




            var circle_marker_5f149648d89593a9e0511fd118a8ebb1 = L.circleMarker(
                [40.44496, -3.58995],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9b24451ffcae98ca60e9949f162b0988 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_33bf5ff58124676b2767935be3660912 = $(`&lt;div id=&quot;html_33bf5ff58124676b2767935be3660912&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;350.0&lt;/div&gt;`)[0];
            popup_9b24451ffcae98ca60e9949f162b0988.setContent(html_33bf5ff58124676b2767935be3660912);


        circle_marker_5f149648d89593a9e0511fd118a8ebb1.bindPopup(popup_9b24451ffcae98ca60e9949f162b0988)
        ;




            var circle_marker_31b2fd0316cece60b8905ad1f31c8e42 = L.circleMarker(
                [40.42562, -3.6049],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_41acee9c9ca7b5cde3f1eccb9c8b3cf3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0489916d6793f66d9339183b864a28b5 = $(`&lt;div id=&quot;html_0489916d6793f66d9339183b864a28b5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;979.9999999999999&lt;/div&gt;`)[0];
            popup_41acee9c9ca7b5cde3f1eccb9c8b3cf3.setContent(html_0489916d6793f66d9339183b864a28b5);


        circle_marker_31b2fd0316cece60b8905ad1f31c8e42.bindPopup(popup_41acee9c9ca7b5cde3f1eccb9c8b3cf3)
        ;




            var circle_marker_b57c1482279a231336d8255d5ad378b9 = L.circleMarker(
                [40.42794, -3.6044],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_db715bb9eee531f9db70d78e452f2185 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_cf797df41ebf7417fadce1ef08c34e52 = $(`&lt;div id=&quot;html_cf797df41ebf7417fadce1ef08c34e52&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;560.0&lt;/div&gt;`)[0];
            popup_db715bb9eee531f9db70d78e452f2185.setContent(html_cf797df41ebf7417fadce1ef08c34e52);


        circle_marker_b57c1482279a231336d8255d5ad378b9.bindPopup(popup_db715bb9eee531f9db70d78e452f2185)
        ;




            var circle_marker_0866e76de253c4a0fa9a8846e510a6a2 = L.circleMarker(
                [40.44483, -3.60616],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_62bcf1e91d410eee9f338bc546b4c737 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_33d7e1378eb633674291a7f9780ee73b = $(`&lt;div id=&quot;html_33d7e1378eb633674291a7f9780ee73b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1120.0&lt;/div&gt;`)[0];
            popup_62bcf1e91d410eee9f338bc546b4c737.setContent(html_33d7e1378eb633674291a7f9780ee73b);


        circle_marker_0866e76de253c4a0fa9a8846e510a6a2.bindPopup(popup_62bcf1e91d410eee9f338bc546b4c737)
        ;




            var circle_marker_75304b5ea11eb0daf60c62f7fddd3943 = L.circleMarker(
                [40.43317, -3.625],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3ff66a9d1835cac0f22fe5782edbeab4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_8e266585536578a97d68ae132e4e0608 = $(`&lt;div id=&quot;html_8e266585536578a97d68ae132e4e0608&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;2000.0&lt;/div&gt;`)[0];
            popup_3ff66a9d1835cac0f22fe5782edbeab4.setContent(html_8e266585536578a97d68ae132e4e0608);


        circle_marker_75304b5ea11eb0daf60c62f7fddd3943.bindPopup(popup_3ff66a9d1835cac0f22fe5782edbeab4)
        ;




            var circle_marker_bda67460ed512d7c59284e56e0b51f93 = L.circleMarker(
                [40.44727, -3.59494],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_6bb9a3bc7f81ec4e0e660679894f8ac7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_5ee89c91bb31a566c14e4bdc2352b1b2 = $(`&lt;div id=&quot;html_5ee89c91bb31a566c14e4bdc2352b1b2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;840.0&lt;/div&gt;`)[0];
            popup_6bb9a3bc7f81ec4e0e660679894f8ac7.setContent(html_5ee89c91bb31a566c14e4bdc2352b1b2);


        circle_marker_bda67460ed512d7c59284e56e0b51f93.bindPopup(popup_6bb9a3bc7f81ec4e0e660679894f8ac7)
        ;




            var circle_marker_d3d6d1000d02313062678a066e09f5a9 = L.circleMarker(
                [40.4395, -3.63327],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_bb4b341afef0523ab27ba7a742990ae5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_dc30135452aaa9a923e4ba7d35ac3e95 = $(`&lt;div id=&quot;html_dc30135452aaa9a923e4ba7d35ac3e95&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;2100.0&lt;/div&gt;`)[0];
            popup_bb4b341afef0523ab27ba7a742990ae5.setContent(html_dc30135452aaa9a923e4ba7d35ac3e95);


        circle_marker_d3d6d1000d02313062678a066e09f5a9.bindPopup(popup_bb4b341afef0523ab27ba7a742990ae5)
        ;




            var circle_marker_63b249d4865113169007e7a13fb8b56a = L.circleMarker(
                [40.42957, -3.61912],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a4a9c3008e0324ef69a52591b4a852ba = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_681daf7b2e6d905a11b45df558bea7a0 = $(`&lt;div id=&quot;html_681daf7b2e6d905a11b45df558bea7a0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_a4a9c3008e0324ef69a52591b4a852ba.setContent(html_681daf7b2e6d905a11b45df558bea7a0);


        circle_marker_63b249d4865113169007e7a13fb8b56a.bindPopup(popup_a4a9c3008e0324ef69a52591b4a852ba)
        ;




            var circle_marker_40e13a1c2263760d7bf149e105cc2036 = L.circleMarker(
                [40.43024, -3.60062],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c8ed637de3a7fd62a3d90efbcd247843 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1aa4df9727d2a5d1b84c725aee46d2e4 = $(`&lt;div id=&quot;html_1aa4df9727d2a5d1b84c725aee46d2e4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_c8ed637de3a7fd62a3d90efbcd247843.setContent(html_1aa4df9727d2a5d1b84c725aee46d2e4);


        circle_marker_40e13a1c2263760d7bf149e105cc2036.bindPopup(popup_c8ed637de3a7fd62a3d90efbcd247843)
        ;




            var circle_marker_72caa618606951ce83bcf810b59cd772 = L.circleMarker(
                [40.43728, -3.61764],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5829c959364026a2fcbc80cc910e674f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_dec14525d7319f6b12f81a40d3506a70 = $(`&lt;div id=&quot;html_dec14525d7319f6b12f81a40d3506a70&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1200.0&lt;/div&gt;`)[0];
            popup_5829c959364026a2fcbc80cc910e674f.setContent(html_dec14525d7319f6b12f81a40d3506a70);


        circle_marker_72caa618606951ce83bcf810b59cd772.bindPopup(popup_5829c959364026a2fcbc80cc910e674f)
        ;




            var circle_marker_1565cb39f652ba11e91632546f4d5502 = L.circleMarker(
                [40.44071, -3.62519],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b76ef9c7f41a7e3f9f67ea7251d85131 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_91e7cf83536a15974088f1137207e75d = $(`&lt;div id=&quot;html_91e7cf83536a15974088f1137207e75d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;91.0&lt;/div&gt;`)[0];
            popup_b76ef9c7f41a7e3f9f67ea7251d85131.setContent(html_91e7cf83536a15974088f1137207e75d);


        circle_marker_1565cb39f652ba11e91632546f4d5502.bindPopup(popup_b76ef9c7f41a7e3f9f67ea7251d85131)
        ;




            var circle_marker_2819ddde3c5dde1cf1e85870cee23ed7 = L.circleMarker(
                [40.41927, -3.61555],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9c153eb20271d7fdf6fc2a606fa5633d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6c17962e5ec01d4bb4bf86d7bc919ab4 = $(`&lt;div id=&quot;html_6c17962e5ec01d4bb4bf86d7bc919ab4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;6300.0&lt;/div&gt;`)[0];
            popup_9c153eb20271d7fdf6fc2a606fa5633d.setContent(html_6c17962e5ec01d4bb4bf86d7bc919ab4);


        circle_marker_2819ddde3c5dde1cf1e85870cee23ed7.bindPopup(popup_9c153eb20271d7fdf6fc2a606fa5633d)
        ;




            var circle_marker_06ac1408605eeea85423194db8c29499 = L.circleMarker(
                [40.42622, -3.60502],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_502c26fbd7ae45139d91f14a7fe3b524 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a0d6c052c9036c64495884464e6af445 = $(`&lt;div id=&quot;html_a0d6c052c9036c64495884464e6af445&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;5670.0&lt;/div&gt;`)[0];
            popup_502c26fbd7ae45139d91f14a7fe3b524.setContent(html_a0d6c052c9036c64495884464e6af445);


        circle_marker_06ac1408605eeea85423194db8c29499.bindPopup(popup_502c26fbd7ae45139d91f14a7fe3b524)
        ;




            var circle_marker_4d84bdd87028a2dc26aeab77ef3bb223 = L.circleMarker(
                [40.43879, -3.61425],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_075f8527911946d37b4c3bde59c3fda3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9cdbf45b171051edba9040ddb42ae55b = $(`&lt;div id=&quot;html_9cdbf45b171051edba9040ddb42ae55b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;3000.0&lt;/div&gt;`)[0];
            popup_075f8527911946d37b4c3bde59c3fda3.setContent(html_9cdbf45b171051edba9040ddb42ae55b);


        circle_marker_4d84bdd87028a2dc26aeab77ef3bb223.bindPopup(popup_075f8527911946d37b4c3bde59c3fda3)
        ;




            var circle_marker_bf804ffd4d650d8c583d058a188aefb2 = L.circleMarker(
                [40.43613, -3.61768],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d7235d44487c72c98a47c01c8f571131 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_5ed5f240f7825ac01bd91aafc49731a8 = $(`&lt;div id=&quot;html_5ed5f240f7825ac01bd91aafc49731a8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_d7235d44487c72c98a47c01c8f571131.setContent(html_5ed5f240f7825ac01bd91aafc49731a8);


        circle_marker_bf804ffd4d650d8c583d058a188aefb2.bindPopup(popup_d7235d44487c72c98a47c01c8f571131)
        ;




            var circle_marker_dc330eadadbc1a3081f67f2163b4ca69 = L.circleMarker(
                [40.42836, -3.61353],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_56a98149859f9f0864981daa36e9c4bf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_82134f83178f996f52f6a935c202f359 = $(`&lt;div id=&quot;html_82134f83178f996f52f6a935c202f359&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;195.0&lt;/div&gt;`)[0];
            popup_56a98149859f9f0864981daa36e9c4bf.setContent(html_82134f83178f996f52f6a935c202f359);


        circle_marker_dc330eadadbc1a3081f67f2163b4ca69.bindPopup(popup_56a98149859f9f0864981daa36e9c4bf)
        ;




            var circle_marker_92d0bec242d878f839e624f3380c3410 = L.circleMarker(
                [40.4465, -3.6165],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b56506fc1c37b02258cfa61f76a0193e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_839ea7f44f81e55e76b7ff4357932123 = $(`&lt;div id=&quot;html_839ea7f44f81e55e76b7ff4357932123&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;450.0&lt;/div&gt;`)[0];
            popup_b56506fc1c37b02258cfa61f76a0193e.setContent(html_839ea7f44f81e55e76b7ff4357932123);


        circle_marker_92d0bec242d878f839e624f3380c3410.bindPopup(popup_b56506fc1c37b02258cfa61f76a0193e)
        ;




            var circle_marker_607549c5d69781f4c6d892014b296885 = L.circleMarker(
                [40.42855, -3.60914],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_513d610353d888a6b60f3b136689fc51 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_016273463a487476a307292e217f8a02 = $(`&lt;div id=&quot;html_016273463a487476a307292e217f8a02&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;400.0&lt;/div&gt;`)[0];
            popup_513d610353d888a6b60f3b136689fc51.setContent(html_016273463a487476a307292e217f8a02);


        circle_marker_607549c5d69781f4c6d892014b296885.bindPopup(popup_513d610353d888a6b60f3b136689fc51)
        ;




            var circle_marker_f42020f899885f36255f3e57ece71089 = L.circleMarker(
                [40.42431, -3.59922],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f737d6d959d99e6901a5cc0486eaa1f4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2450952104a8bc590d69a7a5ee4a1697 = $(`&lt;div id=&quot;html_2450952104a8bc590d69a7a5ee4a1697&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1680.0&lt;/div&gt;`)[0];
            popup_f737d6d959d99e6901a5cc0486eaa1f4.setContent(html_2450952104a8bc590d69a7a5ee4a1697);


        circle_marker_f42020f899885f36255f3e57ece71089.bindPopup(popup_f737d6d959d99e6901a5cc0486eaa1f4)
        ;




            var circle_marker_975bf358c952c970900390de45f8b984 = L.circleMarker(
                [40.42851, -3.60142],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e6685f9309a31afd6c7583296898a4d0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_57bb2b5de9ae6d12ccd93e7452d0e469 = $(`&lt;div id=&quot;html_57bb2b5de9ae6d12ccd93e7452d0e469&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1050.0&lt;/div&gt;`)[0];
            popup_e6685f9309a31afd6c7583296898a4d0.setContent(html_57bb2b5de9ae6d12ccd93e7452d0e469);


        circle_marker_975bf358c952c970900390de45f8b984.bindPopup(popup_e6685f9309a31afd6c7583296898a4d0)
        ;




            var circle_marker_8e208279c498f9e25470f536427fcb90 = L.circleMarker(
                [40.41948, -3.61427],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5b4db3ac5008cd4e73de0aa588668771 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_478e4fe11dc7794071125ea017b0ead3 = $(`&lt;div id=&quot;html_478e4fe11dc7794071125ea017b0ead3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;4200.0&lt;/div&gt;`)[0];
            popup_5b4db3ac5008cd4e73de0aa588668771.setContent(html_478e4fe11dc7794071125ea017b0ead3);


        circle_marker_8e208279c498f9e25470f536427fcb90.bindPopup(popup_5b4db3ac5008cd4e73de0aa588668771)
        ;




            var circle_marker_3055ae28b9b4abe16040bfc90e97b7b7 = L.circleMarker(
                [40.43994, -3.60981],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8b7b0318b1086f68d024dfc32b0d83af = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2d10028726f944968c771345b4a516e8 = $(`&lt;div id=&quot;html_2d10028726f944968c771345b4a516e8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;600.0&lt;/div&gt;`)[0];
            popup_8b7b0318b1086f68d024dfc32b0d83af.setContent(html_2d10028726f944968c771345b4a516e8);


        circle_marker_3055ae28b9b4abe16040bfc90e97b7b7.bindPopup(popup_8b7b0318b1086f68d024dfc32b0d83af)
        ;




            var circle_marker_38fdbc1e4a64d6b3bb961f4d81d71373 = L.circleMarker(
                [40.43867, -3.63424],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_66805dabc090e09a1c57a2761dad546f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b099ecd051ba09af793d9c7a167b70d3 = $(`&lt;div id=&quot;html_b099ecd051ba09af793d9c7a167b70d3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1400.0&lt;/div&gt;`)[0];
            popup_66805dabc090e09a1c57a2761dad546f.setContent(html_b099ecd051ba09af793d9c7a167b70d3);


        circle_marker_38fdbc1e4a64d6b3bb961f4d81d71373.bindPopup(popup_66805dabc090e09a1c57a2761dad546f)
        ;




            var circle_marker_7736e8dc4b2cdfa0919b9faee13967ef = L.circleMarker(
                [40.42725, -3.60481],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3bb8d0a4c8bb1f69ae5ec423eab431bb = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4137d357a39ee7886c3c3f960751e632 = $(`&lt;div id=&quot;html_4137d357a39ee7886c3c3f960751e632&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;420.0&lt;/div&gt;`)[0];
            popup_3bb8d0a4c8bb1f69ae5ec423eab431bb.setContent(html_4137d357a39ee7886c3c3f960751e632);


        circle_marker_7736e8dc4b2cdfa0919b9faee13967ef.bindPopup(popup_3bb8d0a4c8bb1f69ae5ec423eab431bb)
        ;




            var circle_marker_2934fdeca5730b91afde5473c6334ca0 = L.circleMarker(
                [40.42704, -3.61564],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d74f4de338fad92f349b5b1416ad78c5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_af10d5f276b6b5fbf0903c8b08b22d0b = $(`&lt;div id=&quot;html_af10d5f276b6b5fbf0903c8b08b22d0b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1000.0&lt;/div&gt;`)[0];
            popup_d74f4de338fad92f349b5b1416ad78c5.setContent(html_af10d5f276b6b5fbf0903c8b08b22d0b);


        circle_marker_2934fdeca5730b91afde5473c6334ca0.bindPopup(popup_d74f4de338fad92f349b5b1416ad78c5)
        ;




            var circle_marker_be522fee3a36a233636a9183dca88428 = L.circleMarker(
                [40.43857, -3.62069],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_71938ca8a4d485a8ad9882cea29728f0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4a30ec6fdb6c39ff2ecc7afff836d5a0 = $(`&lt;div id=&quot;html_4a30ec6fdb6c39ff2ecc7afff836d5a0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;300.0&lt;/div&gt;`)[0];
            popup_71938ca8a4d485a8ad9882cea29728f0.setContent(html_4a30ec6fdb6c39ff2ecc7afff836d5a0);


        circle_marker_be522fee3a36a233636a9183dca88428.bindPopup(popup_71938ca8a4d485a8ad9882cea29728f0)
        ;




            var circle_marker_f5cc8358aadaf9c82d901bf3202c0578 = L.circleMarker(
                [40.43216, -3.63019],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_6cb03e5cf7caba08d5e9ba87a77ef18a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_fb9ac3dd2930646fdfc582189134fa4d = $(`&lt;div id=&quot;html_fb9ac3dd2930646fdfc582189134fa4d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1500.0&lt;/div&gt;`)[0];
            popup_6cb03e5cf7caba08d5e9ba87a77ef18a.setContent(html_fb9ac3dd2930646fdfc582189134fa4d);


        circle_marker_f5cc8358aadaf9c82d901bf3202c0578.bindPopup(popup_6cb03e5cf7caba08d5e9ba87a77ef18a)
        ;




            var circle_marker_81d526b482d3cc6b04251a74765f3ee7 = L.circleMarker(
                [40.42383, -3.62498],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d703dff1b2c2dd2be45bfc53cfd69164 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b71c9f6ed3c7f5302a69c6b1a4aeb5b9 = $(`&lt;div id=&quot;html_b71c9f6ed3c7f5302a69c6b1a4aeb5b9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;700.0&lt;/div&gt;`)[0];
            popup_d703dff1b2c2dd2be45bfc53cfd69164.setContent(html_b71c9f6ed3c7f5302a69c6b1a4aeb5b9);


        circle_marker_81d526b482d3cc6b04251a74765f3ee7.bindPopup(popup_d703dff1b2c2dd2be45bfc53cfd69164)
        ;




            var circle_marker_af6487267599f014fa788f7823a9c9b1 = L.circleMarker(
                [40.42966, -3.6247],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9bb9284f9f1b2ad9ec63f13bdd687afb = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4741067019a7ff719f2ae2f87bdabcfa = $(`&lt;div id=&quot;html_4741067019a7ff719f2ae2f87bdabcfa&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;280.0&lt;/div&gt;`)[0];
            popup_9bb9284f9f1b2ad9ec63f13bdd687afb.setContent(html_4741067019a7ff719f2ae2f87bdabcfa);


        circle_marker_af6487267599f014fa788f7823a9c9b1.bindPopup(popup_9bb9284f9f1b2ad9ec63f13bdd687afb)
        ;




            var circle_marker_27ad0a088fade333154d3af48daa5b31 = L.circleMarker(
                [40.43729, -3.61814],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e094251bbccfe62252bb6d3d133b80d4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_3867e627c5873b58d4a6b67c296526c9 = $(`&lt;div id=&quot;html_3867e627c5873b58d4a6b67c296526c9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;420.0&lt;/div&gt;`)[0];
            popup_e094251bbccfe62252bb6d3d133b80d4.setContent(html_3867e627c5873b58d4a6b67c296526c9);


        circle_marker_27ad0a088fade333154d3af48daa5b31.bindPopup(popup_e094251bbccfe62252bb6d3d133b80d4)
        ;




            var circle_marker_7276f2384a456c3d8802787e3680c68f = L.circleMarker(
                [40.44456, -3.57863],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_cb54ede47aa59644ecf4371f371f953d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_c29254330aad94e943ef64ae202188a6 = $(`&lt;div id=&quot;html_c29254330aad94e943ef64ae202188a6&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;55.0&lt;/div&gt;`)[0];
            popup_cb54ede47aa59644ecf4371f371f953d.setContent(html_c29254330aad94e943ef64ae202188a6);


        circle_marker_7276f2384a456c3d8802787e3680c68f.bindPopup(popup_cb54ede47aa59644ecf4371f371f953d)
        ;




            var circle_marker_88701bb5d11878c8ba9df7255b9da4cb = L.circleMarker(
                [40.43968, -3.61933],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_38fffe7d387dc81f511dcdc3f1f07688 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_3349cf2de8f9fb2a235f47169f47df8e = $(`&lt;div id=&quot;html_3349cf2de8f9fb2a235f47169f47df8e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;4200.0&lt;/div&gt;`)[0];
            popup_38fffe7d387dc81f511dcdc3f1f07688.setContent(html_3349cf2de8f9fb2a235f47169f47df8e);


        circle_marker_88701bb5d11878c8ba9df7255b9da4cb.bindPopup(popup_38fffe7d387dc81f511dcdc3f1f07688)
        ;




            var circle_marker_e48f1f747616946d2c0ac07eb5280a8d = L.circleMarker(
                [40.44275, -3.58518],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d8ae1b26bc0e2a73bce0c98e628867f8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_726d2d3ca493d36a124f5163ed9347a3 = $(`&lt;div id=&quot;html_726d2d3ca493d36a124f5163ed9347a3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;700.0&lt;/div&gt;`)[0];
            popup_d8ae1b26bc0e2a73bce0c98e628867f8.setContent(html_726d2d3ca493d36a124f5163ed9347a3);


        circle_marker_e48f1f747616946d2c0ac07eb5280a8d.bindPopup(popup_d8ae1b26bc0e2a73bce0c98e628867f8)
        ;




            var circle_marker_2a0bc682b05c825c0507ed54a920cba1 = L.circleMarker(
                [40.42521, -3.60677],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_61a1eb87125106ca4f154a78698f4c35 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d159f4ede42f9c8c0a65be0d3511e053 = $(`&lt;div id=&quot;html_d159f4ede42f9c8c0a65be0d3511e053&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;400.0&lt;/div&gt;`)[0];
            popup_61a1eb87125106ca4f154a78698f4c35.setContent(html_d159f4ede42f9c8c0a65be0d3511e053);


        circle_marker_2a0bc682b05c825c0507ed54a920cba1.bindPopup(popup_61a1eb87125106ca4f154a78698f4c35)
        ;




            var circle_marker_fb5794913c8616b15d65884db2c5f844 = L.circleMarker(
                [40.43616, -3.61925],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ebf8d5e446a94274616430c09fe5dc8b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0089729cb91c08fd9c72417f04542bd5 = $(`&lt;div id=&quot;html_0089729cb91c08fd9c72417f04542bd5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1120.0&lt;/div&gt;`)[0];
            popup_ebf8d5e446a94274616430c09fe5dc8b.setContent(html_0089729cb91c08fd9c72417f04542bd5);


        circle_marker_fb5794913c8616b15d65884db2c5f844.bindPopup(popup_ebf8d5e446a94274616430c09fe5dc8b)
        ;




            var circle_marker_7c3eb0164a1a735ed9e722509400bd37 = L.circleMarker(
                [40.43977, -3.61025],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5a5830250cd3cff86688e3563518d52c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0fcf1f1567ac8efd17501f4c232041f5 = $(`&lt;div id=&quot;html_0fcf1f1567ac8efd17501f4c232041f5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;700.0&lt;/div&gt;`)[0];
            popup_5a5830250cd3cff86688e3563518d52c.setContent(html_0fcf1f1567ac8efd17501f4c232041f5);


        circle_marker_7c3eb0164a1a735ed9e722509400bd37.bindPopup(popup_5a5830250cd3cff86688e3563518d52c)
        ;




            var circle_marker_f03717ee97dcd7b4d0fe39a60b255d9d = L.circleMarker(
                [40.42185, -3.62188],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_24d4fcae386e28eee2c0b02ffe379617 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_24d336e32acc4bb2baca89faa5252f09 = $(`&lt;div id=&quot;html_24d336e32acc4bb2baca89faa5252f09&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;250.0&lt;/div&gt;`)[0];
            popup_24d4fcae386e28eee2c0b02ffe379617.setContent(html_24d336e32acc4bb2baca89faa5252f09);


        circle_marker_f03717ee97dcd7b4d0fe39a60b255d9d.bindPopup(popup_24d4fcae386e28eee2c0b02ffe379617)
        ;




            var circle_marker_a99fe1f8eb8cc5bbfcaa58d5505ec730 = L.circleMarker(
                [40.438, -3.61893],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_93b3f987eb0d5e055023a02eda7a191f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_466a0cb104c01a2d36633d6b8dceba09 = $(`&lt;div id=&quot;html_466a0cb104c01a2d36633d6b8dceba09&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;420.0&lt;/div&gt;`)[0];
            popup_93b3f987eb0d5e055023a02eda7a191f.setContent(html_466a0cb104c01a2d36633d6b8dceba09);


        circle_marker_a99fe1f8eb8cc5bbfcaa58d5505ec730.bindPopup(popup_93b3f987eb0d5e055023a02eda7a191f)
        ;




            var circle_marker_7d8d93a47c2238f944132342fe9d50d4 = L.circleMarker(
                [40.43242, -3.61716],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_7ed3105b5424a4537113aa4b22eb4dc0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1821e6f552a6d74581140b7d1bacad24 = $(`&lt;div id=&quot;html_1821e6f552a6d74581140b7d1bacad24&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;420.0&lt;/div&gt;`)[0];
            popup_7ed3105b5424a4537113aa4b22eb4dc0.setContent(html_1821e6f552a6d74581140b7d1bacad24);


        circle_marker_7d8d93a47c2238f944132342fe9d50d4.bindPopup(popup_7ed3105b5424a4537113aa4b22eb4dc0)
        ;




            var circle_marker_a66e421a82129c9a9ad165dbeb026c0d = L.circleMarker(
                [40.43572, -3.6191],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4c6a981bee10e2920e0c75d61c6e130e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9da5cafdf1c1de7b971c621886f29f01 = $(`&lt;div id=&quot;html_9da5cafdf1c1de7b971c621886f29f01&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;400.0&lt;/div&gt;`)[0];
            popup_4c6a981bee10e2920e0c75d61c6e130e.setContent(html_9da5cafdf1c1de7b971c621886f29f01);


        circle_marker_a66e421a82129c9a9ad165dbeb026c0d.bindPopup(popup_4c6a981bee10e2920e0c75d61c6e130e)
        ;




            var circle_marker_f26814b6d832e0f9394df7a2e846789d = L.circleMarker(
                [40.43639, -3.61809],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_49fac548e00207e373ce0a86d1a0ea2b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_66b5e52118fa2f72931217dafecb2e70 = $(`&lt;div id=&quot;html_66b5e52118fa2f72931217dafecb2e70&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;400.0&lt;/div&gt;`)[0];
            popup_49fac548e00207e373ce0a86d1a0ea2b.setContent(html_66b5e52118fa2f72931217dafecb2e70);


        circle_marker_f26814b6d832e0f9394df7a2e846789d.bindPopup(popup_49fac548e00207e373ce0a86d1a0ea2b)
        ;




            var circle_marker_13049e629a76b4c98b3e43ebc3604ce8 = L.circleMarker(
                [40.42543, -3.60688],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3552307f6e00292ef1de4abe1b7bc902 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2d7065d7fa69408a9a85cf1d83614796 = $(`&lt;div id=&quot;html_2d7065d7fa69408a9a85cf1d83614796&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;750.0&lt;/div&gt;`)[0];
            popup_3552307f6e00292ef1de4abe1b7bc902.setContent(html_2d7065d7fa69408a9a85cf1d83614796);


        circle_marker_13049e629a76b4c98b3e43ebc3604ce8.bindPopup(popup_3552307f6e00292ef1de4abe1b7bc902)
        ;




            var circle_marker_77b43892beed6580e18a12a226d98f75 = L.circleMarker(
                [40.4192, -3.61229],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_08fb443771dfbb787f7fd764cd6f9506 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1fe6ee064e3e02c444776ee02b9ba049 = $(`&lt;div id=&quot;html_1fe6ee064e3e02c444776ee02b9ba049&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;4480.0&lt;/div&gt;`)[0];
            popup_08fb443771dfbb787f7fd764cd6f9506.setContent(html_1fe6ee064e3e02c444776ee02b9ba049);


        circle_marker_77b43892beed6580e18a12a226d98f75.bindPopup(popup_08fb443771dfbb787f7fd764cd6f9506)
        ;




            var circle_marker_e1bac19fc67fe896a69e8fbc65be00fe = L.circleMarker(
                [40.43832, -3.63514],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_aab0fbafd18a36984130d9efe2e84274 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9bc62e9922bba614c6c11702eecbd22a = $(`&lt;div id=&quot;html_9bc62e9922bba614c6c11702eecbd22a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;250.0&lt;/div&gt;`)[0];
            popup_aab0fbafd18a36984130d9efe2e84274.setContent(html_9bc62e9922bba614c6c11702eecbd22a);


        circle_marker_e1bac19fc67fe896a69e8fbc65be00fe.bindPopup(popup_aab0fbafd18a36984130d9efe2e84274)
        ;




            var circle_marker_89839a15ef9844cef82c3c84baf9ec2c = L.circleMarker(
                [40.4279, -3.61039],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f793ffcdb50d078c791a1b9a33521065 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1406e625d281cfbd2b930844b1e835e5 = $(`&lt;div id=&quot;html_1406e625d281cfbd2b930844b1e835e5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;700.0&lt;/div&gt;`)[0];
            popup_f793ffcdb50d078c791a1b9a33521065.setContent(html_1406e625d281cfbd2b930844b1e835e5);


        circle_marker_89839a15ef9844cef82c3c84baf9ec2c.bindPopup(popup_f793ffcdb50d078c791a1b9a33521065)
        ;




            var circle_marker_983a963f52994883e7926d47074d45b4 = L.circleMarker(
                [40.41862, -3.61938],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_defbef095f9688e0250fae85ebcc6847 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b28be478144bc0486fe29d818100296e = $(`&lt;div id=&quot;html_b28be478144bc0486fe29d818100296e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;66.0&lt;/div&gt;`)[0];
            popup_defbef095f9688e0250fae85ebcc6847.setContent(html_b28be478144bc0486fe29d818100296e);


        circle_marker_983a963f52994883e7926d47074d45b4.bindPopup(popup_defbef095f9688e0250fae85ebcc6847)
        ;




            var circle_marker_5d3f0493b8def5d1a13b28aac0ec70e7 = L.circleMarker(
                [40.4493, -3.60987],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9ad32f67807e2ed50f388bee6508b224 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e5a9fc22711341dcb6a5c19caa832f92 = $(`&lt;div id=&quot;html_e5a9fc22711341dcb6a5c19caa832f92&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;250.0&lt;/div&gt;`)[0];
            popup_9ad32f67807e2ed50f388bee6508b224.setContent(html_e5a9fc22711341dcb6a5c19caa832f92);


        circle_marker_5d3f0493b8def5d1a13b28aac0ec70e7.bindPopup(popup_9ad32f67807e2ed50f388bee6508b224)
        ;




            var circle_marker_f79a7c9aa85d266df38ed21eb6d1f849 = L.circleMarker(
                [40.43764, -3.61036],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_48b75c46866ca2a0b65523666f0ae00a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_053617c7b0b39b2bf438b54c1d7d8598 = $(`&lt;div id=&quot;html_053617c7b0b39b2bf438b54c1d7d8598&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1400.0&lt;/div&gt;`)[0];
            popup_48b75c46866ca2a0b65523666f0ae00a.setContent(html_053617c7b0b39b2bf438b54c1d7d8598);


        circle_marker_f79a7c9aa85d266df38ed21eb6d1f849.bindPopup(popup_48b75c46866ca2a0b65523666f0ae00a)
        ;




            var circle_marker_8bb473e2f29ec60326c09247a1adda52 = L.circleMarker(
                [40.43051, -3.6229],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5788c5e3199bbfacbd9017b44536252b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7b4d0da9709f3c12409e4b300cb6f8ee = $(`&lt;div id=&quot;html_7b4d0da9709f3c12409e4b300cb6f8ee&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;735.0&lt;/div&gt;`)[0];
            popup_5788c5e3199bbfacbd9017b44536252b.setContent(html_7b4d0da9709f3c12409e4b300cb6f8ee);


        circle_marker_8bb473e2f29ec60326c09247a1adda52.bindPopup(popup_5788c5e3199bbfacbd9017b44536252b)
        ;




            var circle_marker_4e19e2a8fecc2158e90a35ffe010df5f = L.circleMarker(
                [40.44413, -3.60768],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_34b58e13026358ce88dd03abb4624254 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_89251daa31b28f64f2dd2d17e1fabd17 = $(`&lt;div id=&quot;html_89251daa31b28f64f2dd2d17e1fabd17&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;503.99999999999994&lt;/div&gt;`)[0];
            popup_34b58e13026358ce88dd03abb4624254.setContent(html_89251daa31b28f64f2dd2d17e1fabd17);


        circle_marker_4e19e2a8fecc2158e90a35ffe010df5f.bindPopup(popup_34b58e13026358ce88dd03abb4624254)
        ;




            var circle_marker_934dbc337fcd5cce42b44bad2b7fac6a = L.circleMarker(
                [40.42943, -3.62857],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c7c6a59e064f09ca6dc1f14e36d0df73 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0a088f7f49925fe0b976ce715c9de80c = $(`&lt;div id=&quot;html_0a088f7f49925fe0b976ce715c9de80c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;322.0&lt;/div&gt;`)[0];
            popup_c7c6a59e064f09ca6dc1f14e36d0df73.setContent(html_0a088f7f49925fe0b976ce715c9de80c);


        circle_marker_934dbc337fcd5cce42b44bad2b7fac6a.bindPopup(popup_c7c6a59e064f09ca6dc1f14e36d0df73)
        ;




            var circle_marker_cf9deb6e4fe687c2c918345662e7fe0a = L.circleMarker(
                [40.4325, -3.60373],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_408ccba67a96f801e453d57cf27e79f8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_5945a2791b4dfddb5f7efa0586ffe125 = $(`&lt;div id=&quot;html_5945a2791b4dfddb5f7efa0586ffe125&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;280.0&lt;/div&gt;`)[0];
            popup_408ccba67a96f801e453d57cf27e79f8.setContent(html_5945a2791b4dfddb5f7efa0586ffe125);


        circle_marker_cf9deb6e4fe687c2c918345662e7fe0a.bindPopup(popup_408ccba67a96f801e453d57cf27e79f8)
        ;




            var circle_marker_6bd54f20cd1ab2672face071f5f2cf7f = L.circleMarker(
                [40.44041, -3.61048],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_acae79944560049e109f54006a480dc5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_44f452c88fa22dc85e587e57b2a9c53f = $(`&lt;div id=&quot;html_44f452c88fa22dc85e587e57b2a9c53f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;2000.0&lt;/div&gt;`)[0];
            popup_acae79944560049e109f54006a480dc5.setContent(html_44f452c88fa22dc85e587e57b2a9c53f);


        circle_marker_6bd54f20cd1ab2672face071f5f2cf7f.bindPopup(popup_acae79944560049e109f54006a480dc5)
        ;




            var circle_marker_553241aa176a79e4642b91ad45324d43 = L.circleMarker(
                [40.42442, -3.60478],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ae4cc0266ce37dcc669254be80d8e37f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a74dbd972d1507fe6a762308eaf9813c = $(`&lt;div id=&quot;html_a74dbd972d1507fe6a762308eaf9813c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_ae4cc0266ce37dcc669254be80d8e37f.setContent(html_a74dbd972d1507fe6a762308eaf9813c);


        circle_marker_553241aa176a79e4642b91ad45324d43.bindPopup(popup_ae4cc0266ce37dcc669254be80d8e37f)
        ;




            var circle_marker_fc157fa938725f48210b259ca451ae33 = L.circleMarker(
                [40.42211, -3.61311],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5cb594cb914658fec951f519c6011eec = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b5e4b4df2c6bb62174f6fbf3b8995ec8 = $(`&lt;div id=&quot;html_b5e4b4df2c6bb62174f6fbf3b8995ec8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;400.0&lt;/div&gt;`)[0];
            popup_5cb594cb914658fec951f519c6011eec.setContent(html_b5e4b4df2c6bb62174f6fbf3b8995ec8);


        circle_marker_fc157fa938725f48210b259ca451ae33.bindPopup(popup_5cb594cb914658fec951f519c6011eec)
        ;




            var circle_marker_e089ba5ddb91485328082fdc51366bfa = L.circleMarker(
                [40.43493, -3.62433],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_12ced2f50a201e077059caab0adcf6f0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_05c821cf3f9ce89983baafb49a2651cb = $(`&lt;div id=&quot;html_05c821cf3f9ce89983baafb49a2651cb&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;800.0&lt;/div&gt;`)[0];
            popup_12ced2f50a201e077059caab0adcf6f0.setContent(html_05c821cf3f9ce89983baafb49a2651cb);


        circle_marker_e089ba5ddb91485328082fdc51366bfa.bindPopup(popup_12ced2f50a201e077059caab0adcf6f0)
        ;




            var circle_marker_29f21060f6173e3df556ed8f14f5a96f = L.circleMarker(
                [40.42716, -3.60073],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8fc816b5cf592c114814c9d47090707d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_080f5ac825481cae00d33676d6bf71df = $(`&lt;div id=&quot;html_080f5ac825481cae00d33676d6bf71df&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;250.0&lt;/div&gt;`)[0];
            popup_8fc816b5cf592c114814c9d47090707d.setContent(html_080f5ac825481cae00d33676d6bf71df);


        circle_marker_29f21060f6173e3df556ed8f14f5a96f.bindPopup(popup_8fc816b5cf592c114814c9d47090707d)
        ;




            var circle_marker_dd5d54316e04c9586f8dd52c88890b0f = L.circleMarker(
                [40.42575, -3.60548],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_2094c2fd74e2990b80289c3fe96943e4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_3861f2d21b6e179b4a4195014538f9c3 = $(`&lt;div id=&quot;html_3861f2d21b6e179b4a4195014538f9c3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1092.0&lt;/div&gt;`)[0];
            popup_2094c2fd74e2990b80289c3fe96943e4.setContent(html_3861f2d21b6e179b4a4195014538f9c3);


        circle_marker_dd5d54316e04c9586f8dd52c88890b0f.bindPopup(popup_2094c2fd74e2990b80289c3fe96943e4)
        ;




            var circle_marker_99cba585505af091cb824d707b85542c = L.circleMarker(
                [40.43882, -3.63511],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_70924ba7c5eca0ba52ea8a2d951c6d63 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1f5c111df61a2ccf270b14eb236b47b5 = $(`&lt;div id=&quot;html_1f5c111df61a2ccf270b14eb236b47b5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;800.0&lt;/div&gt;`)[0];
            popup_70924ba7c5eca0ba52ea8a2d951c6d63.setContent(html_1f5c111df61a2ccf270b14eb236b47b5);


        circle_marker_99cba585505af091cb824d707b85542c.bindPopup(popup_70924ba7c5eca0ba52ea8a2d951c6d63)
        ;




            var circle_marker_92ab2fdf59c904d48fa781a2eb513a8a = L.circleMarker(
                [40.42632, -3.60444],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_52c97d906186c16d586f0dd1bac9f6d7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7a4c0b722e65bec885f40109bcaddc81 = $(`&lt;div id=&quot;html_7a4c0b722e65bec885f40109bcaddc81&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1499.0&lt;/div&gt;`)[0];
            popup_52c97d906186c16d586f0dd1bac9f6d7.setContent(html_7a4c0b722e65bec885f40109bcaddc81);


        circle_marker_92ab2fdf59c904d48fa781a2eb513a8a.bindPopup(popup_52c97d906186c16d586f0dd1bac9f6d7)
        ;




            var circle_marker_242664b2ee55503b84fe62085a058786 = L.circleMarker(
                [40.43294, -3.6182],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_19ad6284a9fb1138133d363a218a29b1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a885aecdb37cb685c4120049c1ac57b8 = $(`&lt;div id=&quot;html_a885aecdb37cb685c4120049c1ac57b8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;800.0&lt;/div&gt;`)[0];
            popup_19ad6284a9fb1138133d363a218a29b1.setContent(html_a885aecdb37cb685c4120049c1ac57b8);


        circle_marker_242664b2ee55503b84fe62085a058786.bindPopup(popup_19ad6284a9fb1138133d363a218a29b1)
        ;




            var circle_marker_c9528db515e3988711f65235df4878c3 = L.circleMarker(
                [40.43167, -3.61665],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_dceb7d605481147888351f43446f98da = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_38e3f3cb9b5464a828239515dec9ca47 = $(`&lt;div id=&quot;html_38e3f3cb9b5464a828239515dec9ca47&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1100.0&lt;/div&gt;`)[0];
            popup_dceb7d605481147888351f43446f98da.setContent(html_38e3f3cb9b5464a828239515dec9ca47);


        circle_marker_c9528db515e3988711f65235df4878c3.bindPopup(popup_dceb7d605481147888351f43446f98da)
        ;




            var circle_marker_b9c591b3dd9d41211def55108cf72d15 = L.circleMarker(
                [40.44865, -3.60688],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d8c683137b5a0398d80b57291483274d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_800ce43974ba3a005cd7771cc763dd2c = $(`&lt;div id=&quot;html_800ce43974ba3a005cd7771cc763dd2c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;25.0&lt;/div&gt;`)[0];
            popup_d8c683137b5a0398d80b57291483274d.setContent(html_800ce43974ba3a005cd7771cc763dd2c);


        circle_marker_b9c591b3dd9d41211def55108cf72d15.bindPopup(popup_d8c683137b5a0398d80b57291483274d)
        ;




            var circle_marker_e43f385cedb02a4dd7cce990879cd265 = L.circleMarker(
                [40.44401, -3.61288],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b766a3254d425229d87c77f6e5ccb085 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_05b2e8e9af6a6495604964416bdca2c1 = $(`&lt;div id=&quot;html_05b2e8e9af6a6495604964416bdca2c1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;400.0&lt;/div&gt;`)[0];
            popup_b766a3254d425229d87c77f6e5ccb085.setContent(html_05b2e8e9af6a6495604964416bdca2c1);


        circle_marker_e43f385cedb02a4dd7cce990879cd265.bindPopup(popup_b766a3254d425229d87c77f6e5ccb085)
        ;




            var circle_marker_a4f8b6e5d1e850ba51ff3fa6a567a6e8 = L.circleMarker(
                [40.4447, -3.5833],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_eda088902f3e91305e48b3c20b971241 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6a4ecd2dd3c48144247cbcfab7066329 = $(`&lt;div id=&quot;html_6a4ecd2dd3c48144247cbcfab7066329&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;800.0&lt;/div&gt;`)[0];
            popup_eda088902f3e91305e48b3c20b971241.setContent(html_6a4ecd2dd3c48144247cbcfab7066329);


        circle_marker_a4f8b6e5d1e850ba51ff3fa6a567a6e8.bindPopup(popup_eda088902f3e91305e48b3c20b971241)
        ;




            var circle_marker_6ce509baf1dd127fac71e0d72e793135 = L.circleMarker(
                [40.44706, -3.61107],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_68c0c655cdb7a992684a627562322c61 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_38fd3593efe4db8621576228558df3a1 = $(`&lt;div id=&quot;html_38fd3593efe4db8621576228558df3a1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;81.0&lt;/div&gt;`)[0];
            popup_68c0c655cdb7a992684a627562322c61.setContent(html_38fd3593efe4db8621576228558df3a1);


        circle_marker_6ce509baf1dd127fac71e0d72e793135.bindPopup(popup_68c0c655cdb7a992684a627562322c61)
        ;




            var circle_marker_2a9b69487dc8935d7d255da1a5ed5b2c = L.circleMarker(
                [40.42697, -3.62934],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f6d4d738c86438d09a4686d5d6ff4cc3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7fe446736db2b6607bead9938f47764f = $(`&lt;div id=&quot;html_7fe446736db2b6607bead9938f47764f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;600.0&lt;/div&gt;`)[0];
            popup_f6d4d738c86438d09a4686d5d6ff4cc3.setContent(html_7fe446736db2b6607bead9938f47764f);


        circle_marker_2a9b69487dc8935d7d255da1a5ed5b2c.bindPopup(popup_f6d4d738c86438d09a4686d5d6ff4cc3)
        ;




            var circle_marker_6d6bdfcc708166291b373fe214b094b4 = L.circleMarker(
                [40.4357, -3.61656],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5af77b9fb51252154167844e015695b1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_f7171b1652fe6b189afd0492699d4748 = $(`&lt;div id=&quot;html_f7171b1652fe6b189afd0492699d4748&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;80.0&lt;/div&gt;`)[0];
            popup_5af77b9fb51252154167844e015695b1.setContent(html_f7171b1652fe6b189afd0492699d4748);


        circle_marker_6d6bdfcc708166291b373fe214b094b4.bindPopup(popup_5af77b9fb51252154167844e015695b1)
        ;




            var circle_marker_9359598d2414918f9bddb19d82b533a3 = L.circleMarker(
                [40.4184, -3.61572],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4e0fddce83d63bb1ce84beeb2d28494f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7d2fadb859caa546978f981328e3e99f = $(`&lt;div id=&quot;html_7d2fadb859caa546978f981328e3e99f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;525.0&lt;/div&gt;`)[0];
            popup_4e0fddce83d63bb1ce84beeb2d28494f.setContent(html_7d2fadb859caa546978f981328e3e99f);


        circle_marker_9359598d2414918f9bddb19d82b533a3.bindPopup(popup_4e0fddce83d63bb1ce84beeb2d28494f)
        ;




            var circle_marker_59db4ae37824560713e41ff5bdc64c3b = L.circleMarker(
                [40.44901, -3.60807],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b294fd8a11e64c5443dc314d537b4ace = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_71e59b34ef80e00014b1052f41bcc644 = $(`&lt;div id=&quot;html_71e59b34ef80e00014b1052f41bcc644&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;20.0&lt;/div&gt;`)[0];
            popup_b294fd8a11e64c5443dc314d537b4ace.setContent(html_71e59b34ef80e00014b1052f41bcc644);


        circle_marker_59db4ae37824560713e41ff5bdc64c3b.bindPopup(popup_b294fd8a11e64c5443dc314d537b4ace)
        ;




            var circle_marker_26de77e79d6ce4d91dea08136e5d5a8f = L.circleMarker(
                [40.44764, -3.60751],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e91d01079788ac7b4d5eab4637557fd5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a13a67698c51627dfef6961f9930d4c2 = $(`&lt;div id=&quot;html_a13a67698c51627dfef6961f9930d4c2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1120.0&lt;/div&gt;`)[0];
            popup_e91d01079788ac7b4d5eab4637557fd5.setContent(html_a13a67698c51627dfef6961f9930d4c2);


        circle_marker_26de77e79d6ce4d91dea08136e5d5a8f.bindPopup(popup_e91d01079788ac7b4d5eab4637557fd5)
        ;




            var circle_marker_5dfee908724e8c3f41548a27ce3d06dd = L.circleMarker(
                [40.43029, -3.60298],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_263e35b5652c1363e38692cd15e26f18 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a2c9673799d884541d4b52e214cdd3bf = $(`&lt;div id=&quot;html_a2c9673799d884541d4b52e214cdd3bf&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1190.0&lt;/div&gt;`)[0];
            popup_263e35b5652c1363e38692cd15e26f18.setContent(html_a2c9673799d884541d4b52e214cdd3bf);


        circle_marker_5dfee908724e8c3f41548a27ce3d06dd.bindPopup(popup_263e35b5652c1363e38692cd15e26f18)
        ;




            var circle_marker_3382ebdbddc6169df27f7c29fc453619 = L.circleMarker(
                [40.43848, -3.61177],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_cbcff75514dfc355fa34974cd802b455 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_17f2c8909be0faa3acd81d05776a5e96 = $(`&lt;div id=&quot;html_17f2c8909be0faa3acd81d05776a5e96&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;300.0&lt;/div&gt;`)[0];
            popup_cbcff75514dfc355fa34974cd802b455.setContent(html_17f2c8909be0faa3acd81d05776a5e96);


        circle_marker_3382ebdbddc6169df27f7c29fc453619.bindPopup(popup_cbcff75514dfc355fa34974cd802b455)
        ;




            var circle_marker_d648825f94448d9ac5c06b61012e31f4 = L.circleMarker(
                [40.42475, -3.61202],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_535a8494efb5b5fbca7f30c08f9d0310 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_97fe413a48d3e4a9373fc9eeadb3fbf2 = $(`&lt;div id=&quot;html_97fe413a48d3e4a9373fc9eeadb3fbf2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;700.0&lt;/div&gt;`)[0];
            popup_535a8494efb5b5fbca7f30c08f9d0310.setContent(html_97fe413a48d3e4a9373fc9eeadb3fbf2);


        circle_marker_d648825f94448d9ac5c06b61012e31f4.bindPopup(popup_535a8494efb5b5fbca7f30c08f9d0310)
        ;




            var circle_marker_d2e5ff48b801a8941f17148bb88f9877 = L.circleMarker(
                [40.43725, -3.61922],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_555e3a954f03ea8bd8416ad7de76eadc = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6e925e51dfdc4b3e76b928d900d1a66d = $(`&lt;div id=&quot;html_6e925e51dfdc4b3e76b928d900d1a66d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1200.0&lt;/div&gt;`)[0];
            popup_555e3a954f03ea8bd8416ad7de76eadc.setContent(html_6e925e51dfdc4b3e76b928d900d1a66d);


        circle_marker_d2e5ff48b801a8941f17148bb88f9877.bindPopup(popup_555e3a954f03ea8bd8416ad7de76eadc)
        ;




            var circle_marker_df652196e969998a1039316b5b871903 = L.circleMarker(
                [40.44104, -3.58593],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_bbe1bb3ec4369f917de9c7594d1ed120 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_62508b7895c144d5fdc032feb9a5fa78 = $(`&lt;div id=&quot;html_62508b7895c144d5fdc032feb9a5fa78&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;350.0&lt;/div&gt;`)[0];
            popup_bbe1bb3ec4369f917de9c7594d1ed120.setContent(html_62508b7895c144d5fdc032feb9a5fa78);


        circle_marker_df652196e969998a1039316b5b871903.bindPopup(popup_bbe1bb3ec4369f917de9c7594d1ed120)
        ;




            var circle_marker_3150ce11ea235188c53f2abf7516b3a8 = L.circleMarker(
                [40.42828, -3.61992],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c9a2cd0f036e91067b5f2c4e9fa1c9e2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4f444bc079d987fb953259b4329c3efb = $(`&lt;div id=&quot;html_4f444bc079d987fb953259b4329c3efb&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;300.0&lt;/div&gt;`)[0];
            popup_c9a2cd0f036e91067b5f2c4e9fa1c9e2.setContent(html_4f444bc079d987fb953259b4329c3efb);


        circle_marker_3150ce11ea235188c53f2abf7516b3a8.bindPopup(popup_c9a2cd0f036e91067b5f2c4e9fa1c9e2)
        ;




            var circle_marker_24b793af8c5476b2b66ac8b8e389e022 = L.circleMarker(
                [40.42229, -3.60595],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_755cbf33204a6b305d152da3faca8058 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6b62d7952892882df243801fdcf2cd0a = $(`&lt;div id=&quot;html_6b62d7952892882df243801fdcf2cd0a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;150.0&lt;/div&gt;`)[0];
            popup_755cbf33204a6b305d152da3faca8058.setContent(html_6b62d7952892882df243801fdcf2cd0a);


        circle_marker_24b793af8c5476b2b66ac8b8e389e022.bindPopup(popup_755cbf33204a6b305d152da3faca8058)
        ;




            var circle_marker_9498e37797bd420ee85c012a0a7cebff = L.circleMarker(
                [40.42832, -3.62926],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4f77219a4de01e6f7e3a752f669b7316 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_78618d9365a3934a284740ef6b2da0c2 = $(`&lt;div id=&quot;html_78618d9365a3934a284740ef6b2da0c2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;420.0&lt;/div&gt;`)[0];
            popup_4f77219a4de01e6f7e3a752f669b7316.setContent(html_78618d9365a3934a284740ef6b2da0c2);


        circle_marker_9498e37797bd420ee85c012a0a7cebff.bindPopup(popup_4f77219a4de01e6f7e3a752f669b7316)
        ;




            var circle_marker_48a3398ef1a720c86f792cb0999bf84d = L.circleMarker(
                [40.43614, -3.60969],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ff1a92c5dc9016b831a645ad405b7020 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d8d453ec8a2b6f70a6feab6ad0ab1bab = $(`&lt;div id=&quot;html_d8d453ec8a2b6f70a6feab6ad0ab1bab&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;338.79999999999995&lt;/div&gt;`)[0];
            popup_ff1a92c5dc9016b831a645ad405b7020.setContent(html_d8d453ec8a2b6f70a6feab6ad0ab1bab);


        circle_marker_48a3398ef1a720c86f792cb0999bf84d.bindPopup(popup_ff1a92c5dc9016b831a645ad405b7020)
        ;




            var circle_marker_f0169eb865d90da7eb6dd3a995e47cd1 = L.circleMarker(
                [40.44276, -3.58933],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5a176a1753bac9739d573621f008f3d5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ae0c2da0cd271f865552999c889fd991 = $(`&lt;div id=&quot;html_ae0c2da0cd271f865552999c889fd991&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;100.0&lt;/div&gt;`)[0];
            popup_5a176a1753bac9739d573621f008f3d5.setContent(html_ae0c2da0cd271f865552999c889fd991);


        circle_marker_f0169eb865d90da7eb6dd3a995e47cd1.bindPopup(popup_5a176a1753bac9739d573621f008f3d5)
        ;




            var circle_marker_29069504f45bd0ae34d92fe9328212b8 = L.circleMarker(
                [40.42906, -3.61137],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_50ad96a438f2d5663d86b4718f582599 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6a4761002101e9bf93865ff00ef012f1 = $(`&lt;div id=&quot;html_6a4761002101e9bf93865ff00ef012f1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_50ad96a438f2d5663d86b4718f582599.setContent(html_6a4761002101e9bf93865ff00ef012f1);


        circle_marker_29069504f45bd0ae34d92fe9328212b8.bindPopup(popup_50ad96a438f2d5663d86b4718f582599)
        ;




            var circle_marker_8e75c3305d3b779fdb0e52bdc6d8c73a = L.circleMarker(
                [40.4375, -3.62381],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_184706784e08e6ba64a05a8f1b5be090 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_38c84daef3a631fb84ca58df1fa6757a = $(`&lt;div id=&quot;html_38c84daef3a631fb84ca58df1fa6757a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;800.0&lt;/div&gt;`)[0];
            popup_184706784e08e6ba64a05a8f1b5be090.setContent(html_38c84daef3a631fb84ca58df1fa6757a);


        circle_marker_8e75c3305d3b779fdb0e52bdc6d8c73a.bindPopup(popup_184706784e08e6ba64a05a8f1b5be090)
        ;




            var circle_marker_25236260c2dbfe65b718e80a0b17a427 = L.circleMarker(
                [40.42301, -3.60735],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_68413bb1da79ab1b8872118744742c69 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_617d90a22c5634a663f287e24863d23f = $(`&lt;div id=&quot;html_617d90a22c5634a663f287e24863d23f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;2800.0&lt;/div&gt;`)[0];
            popup_68413bb1da79ab1b8872118744742c69.setContent(html_617d90a22c5634a663f287e24863d23f);


        circle_marker_25236260c2dbfe65b718e80a0b17a427.bindPopup(popup_68413bb1da79ab1b8872118744742c69)
        ;




            var circle_marker_f22d0c5879022e2b01887a0562bd7b09 = L.circleMarker(
                [40.44107, -3.61044],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_32ba260ab2d422884e53a28cb10baa71 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_06c64e76fbe23e855ce3e5953b371025 = $(`&lt;div id=&quot;html_06c64e76fbe23e855ce3e5953b371025&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_32ba260ab2d422884e53a28cb10baa71.setContent(html_06c64e76fbe23e855ce3e5953b371025);


        circle_marker_f22d0c5879022e2b01887a0562bd7b09.bindPopup(popup_32ba260ab2d422884e53a28cb10baa71)
        ;




            var circle_marker_97a2a86f0a4678e10f9286133805379b = L.circleMarker(
                [40.44517, -3.58333],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d467e27fd10554abcdf210f2200f784b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_98df9aaa63779ad089c3a0684c8c526c = $(`&lt;div id=&quot;html_98df9aaa63779ad089c3a0684c8c526c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;60.0&lt;/div&gt;`)[0];
            popup_d467e27fd10554abcdf210f2200f784b.setContent(html_98df9aaa63779ad089c3a0684c8c526c);


        circle_marker_97a2a86f0a4678e10f9286133805379b.bindPopup(popup_d467e27fd10554abcdf210f2200f784b)
        ;




            var circle_marker_10f08d8e69d45c652f151da0ba4b6316 = L.circleMarker(
                [40.44592, -3.58746],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e3caac758106b2ff7149113fdda8d6b3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_463ea75f9f1eccafbf6e274ad608b875 = $(`&lt;div id=&quot;html_463ea75f9f1eccafbf6e274ad608b875&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;4200.0&lt;/div&gt;`)[0];
            popup_e3caac758106b2ff7149113fdda8d6b3.setContent(html_463ea75f9f1eccafbf6e274ad608b875);


        circle_marker_10f08d8e69d45c652f151da0ba4b6316.bindPopup(popup_e3caac758106b2ff7149113fdda8d6b3)
        ;




            var circle_marker_22b79c6faee2d661e4ba9cf6a39ea310 = L.circleMarker(
                [40.43069, -3.62837],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_cb3db44bd9ff97f670733adde9de6722 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_c3108948956ddc4968d0ac06db60186c = $(`&lt;div id=&quot;html_c3108948956ddc4968d0ac06db60186c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;882.0&lt;/div&gt;`)[0];
            popup_cb3db44bd9ff97f670733adde9de6722.setContent(html_c3108948956ddc4968d0ac06db60186c);


        circle_marker_22b79c6faee2d661e4ba9cf6a39ea310.bindPopup(popup_cb3db44bd9ff97f670733adde9de6722)
        ;




            var circle_marker_a96bdc8a306c05d001d80e7376aea42b = L.circleMarker(
                [40.43819, -3.60716],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5a94814353b3a3014a3d5f9a873e7f83 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_f3313a35ec15896b2b1dd3702377905c = $(`&lt;div id=&quot;html_f3313a35ec15896b2b1dd3702377905c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;2000.0&lt;/div&gt;`)[0];
            popup_5a94814353b3a3014a3d5f9a873e7f83.setContent(html_f3313a35ec15896b2b1dd3702377905c);


        circle_marker_a96bdc8a306c05d001d80e7376aea42b.bindPopup(popup_5a94814353b3a3014a3d5f9a873e7f83)
        ;




            var circle_marker_0d772416870a479e048182b16d3b907e = L.circleMarker(
                [40.44048, -3.61089],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_686aa389cbc7f0ec589525ac59b906e9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_8ba9a2f66ee4abbeb08197cc3466d167 = $(`&lt;div id=&quot;html_8ba9a2f66ee4abbeb08197cc3466d167&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;812.0&lt;/div&gt;`)[0];
            popup_686aa389cbc7f0ec589525ac59b906e9.setContent(html_8ba9a2f66ee4abbeb08197cc3466d167);


        circle_marker_0d772416870a479e048182b16d3b907e.bindPopup(popup_686aa389cbc7f0ec589525ac59b906e9)
        ;




            var circle_marker_edf1fc9f0b7535fdab7b0fe17496bbd1 = L.circleMarker(
                [40.42795, -3.60439],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d504924241d715c894c9eb5743057691 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b585525e3b85e203cb35e452e2495abd = $(`&lt;div id=&quot;html_b585525e3b85e203cb35e452e2495abd&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1190.0&lt;/div&gt;`)[0];
            popup_d504924241d715c894c9eb5743057691.setContent(html_b585525e3b85e203cb35e452e2495abd);


        circle_marker_edf1fc9f0b7535fdab7b0fe17496bbd1.bindPopup(popup_d504924241d715c894c9eb5743057691)
        ;




            var circle_marker_3b766acc22879f0d5ba459c01485041f = L.circleMarker(
                [40.43178, -3.61584],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_da7215b23aab4cba3e14fbb135a0b615 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_13a9eebbfd257d46aebb40b05103d91c = $(`&lt;div id=&quot;html_13a9eebbfd257d46aebb40b05103d91c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;400.0&lt;/div&gt;`)[0];
            popup_da7215b23aab4cba3e14fbb135a0b615.setContent(html_13a9eebbfd257d46aebb40b05103d91c);


        circle_marker_3b766acc22879f0d5ba459c01485041f.bindPopup(popup_da7215b23aab4cba3e14fbb135a0b615)
        ;




            var circle_marker_a701c09f3a4b3458fde168875325bd90 = L.circleMarker(
                [40.42969, -3.61082],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_650642320a9dfc2ce01c93b0ac6f4c79 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d5ba4220daa9582d6d81ea2a052b07f0 = $(`&lt;div id=&quot;html_d5ba4220daa9582d6d81ea2a052b07f0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1000.0&lt;/div&gt;`)[0];
            popup_650642320a9dfc2ce01c93b0ac6f4c79.setContent(html_d5ba4220daa9582d6d81ea2a052b07f0);


        circle_marker_a701c09f3a4b3458fde168875325bd90.bindPopup(popup_650642320a9dfc2ce01c93b0ac6f4c79)
        ;




            var circle_marker_9b3e2c43934281feff7c7b5bea4e9085 = L.circleMarker(
                [40.43441, -3.60877],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3d999b091fc0c452d3c7fc45cdf8424b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_bb43c370818f2b0413763465ad0702fc = $(`&lt;div id=&quot;html_bb43c370818f2b0413763465ad0702fc&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;25.0&lt;/div&gt;`)[0];
            popup_3d999b091fc0c452d3c7fc45cdf8424b.setContent(html_bb43c370818f2b0413763465ad0702fc);


        circle_marker_9b3e2c43934281feff7c7b5bea4e9085.bindPopup(popup_3d999b091fc0c452d3c7fc45cdf8424b)
        ;




            var circle_marker_93c59abf9d3f5b3893cf3a823ae3d256 = L.circleMarker(
                [40.43078, -3.60412],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_80877604f74c5bd87bf144f254c9b1d6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7e2515f31421e06a1fae1d91d6dbbc2b = $(`&lt;div id=&quot;html_7e2515f31421e06a1fae1d91d6dbbc2b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;840.0&lt;/div&gt;`)[0];
            popup_80877604f74c5bd87bf144f254c9b1d6.setContent(html_7e2515f31421e06a1fae1d91d6dbbc2b);


        circle_marker_93c59abf9d3f5b3893cf3a823ae3d256.bindPopup(popup_80877604f74c5bd87bf144f254c9b1d6)
        ;




            var circle_marker_64d6b395766c8778cb4d27adba1f7bef = L.circleMarker(
                [40.43924, -3.62995],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c459902068e0227ebf57423099455601 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_22e2c16480e51921bf1e6479267ed341 = $(`&lt;div id=&quot;html_22e2c16480e51921bf1e6479267ed341&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;46.0&lt;/div&gt;`)[0];
            popup_c459902068e0227ebf57423099455601.setContent(html_22e2c16480e51921bf1e6479267ed341);


        circle_marker_64d6b395766c8778cb4d27adba1f7bef.bindPopup(popup_c459902068e0227ebf57423099455601)
        ;




            var circle_marker_be4a09924b552fa631d1626db36846f9 = L.circleMarker(
                [40.42939, -3.61535],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_406593215daf994198543532e4e63e31 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d37e3cb60916a739a30b01bf2411303a = $(`&lt;div id=&quot;html_d37e3cb60916a739a30b01bf2411303a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;300.0&lt;/div&gt;`)[0];
            popup_406593215daf994198543532e4e63e31.setContent(html_d37e3cb60916a739a30b01bf2411303a);


        circle_marker_be4a09924b552fa631d1626db36846f9.bindPopup(popup_406593215daf994198543532e4e63e31)
        ;




            var circle_marker_1a24ca0d9f638dd7313e02f8d57b46af = L.circleMarker(
                [40.433, -3.61638],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_48dd418b9ba04dc6d41ba88545627ec8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_84ac403e61fdda1250e5c572668728a6 = $(`&lt;div id=&quot;html_84ac403e61fdda1250e5c572668728a6&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;2000.0&lt;/div&gt;`)[0];
            popup_48dd418b9ba04dc6d41ba88545627ec8.setContent(html_84ac403e61fdda1250e5c572668728a6);


        circle_marker_1a24ca0d9f638dd7313e02f8d57b46af.bindPopup(popup_48dd418b9ba04dc6d41ba88545627ec8)
        ;




            var circle_marker_8d921ce623798b5c30f82dbb78b318a6 = L.circleMarker(
                [40.42658, -3.61196],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ac06ba9007e62d07d7d6e691882a1c87 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_93662bb0f3d529269c560a798a6a435b = $(`&lt;div id=&quot;html_93662bb0f3d529269c560a798a6a435b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1050.0&lt;/div&gt;`)[0];
            popup_ac06ba9007e62d07d7d6e691882a1c87.setContent(html_93662bb0f3d529269c560a798a6a435b);


        circle_marker_8d921ce623798b5c30f82dbb78b318a6.bindPopup(popup_ac06ba9007e62d07d7d6e691882a1c87)
        ;




            var circle_marker_05a1da5245931bd339bc7b1eaa2bed52 = L.circleMarker(
                [40.44439, -3.61021],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_38338fc61ed96d49ee26aa70b1128a01 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_f109bbb08f1a083e2b12001c189ec7d2 = $(`&lt;div id=&quot;html_f109bbb08f1a083e2b12001c189ec7d2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;600.0&lt;/div&gt;`)[0];
            popup_38338fc61ed96d49ee26aa70b1128a01.setContent(html_f109bbb08f1a083e2b12001c189ec7d2);


        circle_marker_05a1da5245931bd339bc7b1eaa2bed52.bindPopup(popup_38338fc61ed96d49ee26aa70b1128a01)
        ;




            var circle_marker_0e54eb63d03852600921addf5dd44405 = L.circleMarker(
                [40.43448, -3.61723],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_cd95c9773070882891554738560038ba = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7cc09ddaa0b438b6d5737936f36b0fee = $(`&lt;div id=&quot;html_7cc09ddaa0b438b6d5737936f36b0fee&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_cd95c9773070882891554738560038ba.setContent(html_7cc09ddaa0b438b6d5737936f36b0fee);


        circle_marker_0e54eb63d03852600921addf5dd44405.bindPopup(popup_cd95c9773070882891554738560038ba)
        ;




            var circle_marker_4c274ad1c2ef496e75ecf8f691983129 = L.circleMarker(
                [40.42272, -3.6193],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9f0648ba1ab948ab659aced79a890380 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_5db1e610d10f9b70e6d27412b927a1b5 = $(`&lt;div id=&quot;html_5db1e610d10f9b70e6d27412b927a1b5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1260.0&lt;/div&gt;`)[0];
            popup_9f0648ba1ab948ab659aced79a890380.setContent(html_5db1e610d10f9b70e6d27412b927a1b5);


        circle_marker_4c274ad1c2ef496e75ecf8f691983129.bindPopup(popup_9f0648ba1ab948ab659aced79a890380)
        ;




            var circle_marker_9f90a4ab6d65651cc1bc2e7794d5671e = L.circleMarker(
                [40.42916, -3.60887],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_fa8fbafd1119cf9c46a080799f7d66db = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_5bd2cf1f8119146e6b1edbe2c21739d2 = $(`&lt;div id=&quot;html_5bd2cf1f8119146e6b1edbe2c21739d2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1650.0&lt;/div&gt;`)[0];
            popup_fa8fbafd1119cf9c46a080799f7d66db.setContent(html_5bd2cf1f8119146e6b1edbe2c21739d2);


        circle_marker_9f90a4ab6d65651cc1bc2e7794d5671e.bindPopup(popup_fa8fbafd1119cf9c46a080799f7d66db)
        ;




            var circle_marker_310fad6de5bfd6a5ed317840dd15ced3 = L.circleMarker(
                [40.44796, -3.60974],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_cd818aff4b8504944b7cdeec2723bf78 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2f58e866f79a39788dca1008351a6ce5 = $(`&lt;div id=&quot;html_2f58e866f79a39788dca1008351a6ce5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1540.0&lt;/div&gt;`)[0];
            popup_cd818aff4b8504944b7cdeec2723bf78.setContent(html_2f58e866f79a39788dca1008351a6ce5);


        circle_marker_310fad6de5bfd6a5ed317840dd15ced3.bindPopup(popup_cd818aff4b8504944b7cdeec2723bf78)
        ;




            var circle_marker_113f8abea92269de3c980202ba44265d = L.circleMarker(
                [40.43668, -3.61959],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ac15e20c348931023048625096177bd1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ca27f6c5a2f2470f908e809ca4be054f = $(`&lt;div id=&quot;html_ca27f6c5a2f2470f908e809ca4be054f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;400.0&lt;/div&gt;`)[0];
            popup_ac15e20c348931023048625096177bd1.setContent(html_ca27f6c5a2f2470f908e809ca4be054f);


        circle_marker_113f8abea92269de3c980202ba44265d.bindPopup(popup_ac15e20c348931023048625096177bd1)
        ;




            var circle_marker_711e3e538ecef5132ec7d341a9626414 = L.circleMarker(
                [40.44937, -3.61633],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a032c5fc95fed98ea3dada1edb80ceba = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_f480e1bb621d46d900fd6448d06cfe8f = $(`&lt;div id=&quot;html_f480e1bb621d46d900fd6448d06cfe8f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;6000.0&lt;/div&gt;`)[0];
            popup_a032c5fc95fed98ea3dada1edb80ceba.setContent(html_f480e1bb621d46d900fd6448d06cfe8f);


        circle_marker_711e3e538ecef5132ec7d341a9626414.bindPopup(popup_a032c5fc95fed98ea3dada1edb80ceba)
        ;




            var circle_marker_1f6130203d7afc294c50444e05a9b5ee = L.circleMarker(
                [40.4307, -3.6174],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f40b3ef444c63227645d4dd12727ef53 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_f99b32480df74639f207b2a1e3269df5 = $(`&lt;div id=&quot;html_f99b32480df74639f207b2a1e3269df5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;920.0&lt;/div&gt;`)[0];
            popup_f40b3ef444c63227645d4dd12727ef53.setContent(html_f99b32480df74639f207b2a1e3269df5);


        circle_marker_1f6130203d7afc294c50444e05a9b5ee.bindPopup(popup_f40b3ef444c63227645d4dd12727ef53)
        ;




            var circle_marker_713a1840a3313ccee7c631d069b18391 = L.circleMarker(
                [40.42861, -3.60124],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_951d7eef90870d0593322a5ae56ff561 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_51abb0e36a164941421395f8fe360461 = $(`&lt;div id=&quot;html_51abb0e36a164941421395f8fe360461&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;300.0&lt;/div&gt;`)[0];
            popup_951d7eef90870d0593322a5ae56ff561.setContent(html_51abb0e36a164941421395f8fe360461);


        circle_marker_713a1840a3313ccee7c631d069b18391.bindPopup(popup_951d7eef90870d0593322a5ae56ff561)
        ;




            var circle_marker_66546c3fbae39fa415fa2d322e5f1e3c = L.circleMarker(
                [40.43127, -3.61234],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_7d194dd46613fc27221a55dda437b348 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_815f6dac8c4f56172b0a829c8890469f = $(`&lt;div id=&quot;html_815f6dac8c4f56172b0a829c8890469f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1470.0&lt;/div&gt;`)[0];
            popup_7d194dd46613fc27221a55dda437b348.setContent(html_815f6dac8c4f56172b0a829c8890469f);


        circle_marker_66546c3fbae39fa415fa2d322e5f1e3c.bindPopup(popup_7d194dd46613fc27221a55dda437b348)
        ;




            var circle_marker_94a62c8eb47d3f57f38afbf82d9fff6f = L.circleMarker(
                [40.42225, -3.61375],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_0743079c25dc72cee7b21ac99de3ed00 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_f4d210bb40406cf1521d344900f43be3 = $(`&lt;div id=&quot;html_f4d210bb40406cf1521d344900f43be3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;420.0&lt;/div&gt;`)[0];
            popup_0743079c25dc72cee7b21ac99de3ed00.setContent(html_f4d210bb40406cf1521d344900f43be3);


        circle_marker_94a62c8eb47d3f57f38afbf82d9fff6f.bindPopup(popup_0743079c25dc72cee7b21ac99de3ed00)
        ;




            var circle_marker_0eade1c21d080759b0c11bda56a3678d = L.circleMarker(
                [40.42895, -3.60146],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8ab4cf37f3cc9783c66beecec22c246a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0e1c268f2ce755e252fc83ebdb46cc5c = $(`&lt;div id=&quot;html_0e1c268f2ce755e252fc83ebdb46cc5c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;700.0&lt;/div&gt;`)[0];
            popup_8ab4cf37f3cc9783c66beecec22c246a.setContent(html_0e1c268f2ce755e252fc83ebdb46cc5c);


        circle_marker_0eade1c21d080759b0c11bda56a3678d.bindPopup(popup_8ab4cf37f3cc9783c66beecec22c246a)
        ;




            var circle_marker_fe454b437c7a4b245c7e18e0aa6966a7 = L.circleMarker(
                [40.44129, -3.62892],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_32e04c366a665c1c6a1bec509a448e3d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1da629f675d2a63a007a55bb739c62eb = $(`&lt;div id=&quot;html_1da629f675d2a63a007a55bb739c62eb&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;200.0&lt;/div&gt;`)[0];
            popup_32e04c366a665c1c6a1bec509a448e3d.setContent(html_1da629f675d2a63a007a55bb739c62eb);


        circle_marker_fe454b437c7a4b245c7e18e0aa6966a7.bindPopup(popup_32e04c366a665c1c6a1bec509a448e3d)
        ;




            var circle_marker_d226ec89b44d297ae6dd120dfea00486 = L.circleMarker(
                [40.43037, -3.60158],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3cb034abf7b76b95706cbc02d7fb6d99 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e3903433002277333aae23da766999ad = $(`&lt;div id=&quot;html_e3903433002277333aae23da766999ad&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;180.0&lt;/div&gt;`)[0];
            popup_3cb034abf7b76b95706cbc02d7fb6d99.setContent(html_e3903433002277333aae23da766999ad);


        circle_marker_d226ec89b44d297ae6dd120dfea00486.bindPopup(popup_3cb034abf7b76b95706cbc02d7fb6d99)
        ;




            var circle_marker_3261b4f609c50e915905ed172eaaee3f = L.circleMarker(
                [40.43983, -3.60951],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d4b277d12f64fbcc6201681890d199e6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_bc8c4c9bcf3ee465e207ac6e0c6ca738 = $(`&lt;div id=&quot;html_bc8c4c9bcf3ee465e207ac6e0c6ca738&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;840.0&lt;/div&gt;`)[0];
            popup_d4b277d12f64fbcc6201681890d199e6.setContent(html_bc8c4c9bcf3ee465e207ac6e0c6ca738);


        circle_marker_3261b4f609c50e915905ed172eaaee3f.bindPopup(popup_d4b277d12f64fbcc6201681890d199e6)
        ;




            var circle_marker_a3b73f346f3db3c201502773c180ba58 = L.circleMarker(
                [40.44677, -3.5787],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_decdcce0fa64bd1160033debf98d79d7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9c697cd6c10475c68776efff7f0e3286 = $(`&lt;div id=&quot;html_9c697cd6c10475c68776efff7f0e3286&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1000.0&lt;/div&gt;`)[0];
            popup_decdcce0fa64bd1160033debf98d79d7.setContent(html_9c697cd6c10475c68776efff7f0e3286);


        circle_marker_a3b73f346f3db3c201502773c180ba58.bindPopup(popup_decdcce0fa64bd1160033debf98d79d7)
        ;




            var circle_marker_9044ff568be6f1f7b2ba6aa1b69ba254 = L.circleMarker(
                [40.44465, -3.58397],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f923a4131a78d5336365357dfe7853f0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_8a70ed82076e806c8887fef8ad28e921 = $(`&lt;div id=&quot;html_8a70ed82076e806c8887fef8ad28e921&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;650.0&lt;/div&gt;`)[0];
            popup_f923a4131a78d5336365357dfe7853f0.setContent(html_8a70ed82076e806c8887fef8ad28e921);


        circle_marker_9044ff568be6f1f7b2ba6aa1b69ba254.bindPopup(popup_f923a4131a78d5336365357dfe7853f0)
        ;




            var circle_marker_17486d1f44751e4406b746e37b0a5b48 = L.circleMarker(
                [40.42196, -3.62591],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8ea3aa6df1aa1b6d686366250e163192 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_c84f6a69360d2ea1ffdf2cf15b49b905 = $(`&lt;div id=&quot;html_c84f6a69360d2ea1ffdf2cf15b49b905&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;630.0&lt;/div&gt;`)[0];
            popup_8ea3aa6df1aa1b6d686366250e163192.setContent(html_c84f6a69360d2ea1ffdf2cf15b49b905);


        circle_marker_17486d1f44751e4406b746e37b0a5b48.bindPopup(popup_8ea3aa6df1aa1b6d686366250e163192)
        ;




            var circle_marker_57030b0e7eded2d188fd1d435f1b2470 = L.circleMarker(
                [40.43472, -3.60832],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_01132a4e2e53e2603d8b25f438d0c69c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ce0cea1bfbad9293a28c24727a929007 = $(`&lt;div id=&quot;html_ce0cea1bfbad9293a28c24727a929007&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;800.0&lt;/div&gt;`)[0];
            popup_01132a4e2e53e2603d8b25f438d0c69c.setContent(html_ce0cea1bfbad9293a28c24727a929007);


        circle_marker_57030b0e7eded2d188fd1d435f1b2470.bindPopup(popup_01132a4e2e53e2603d8b25f438d0c69c)
        ;




            var circle_marker_28fa1bd55b07dd9414774f09510b0e50 = L.circleMarker(
                [40.43211, -3.62524],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_449d92d72b354ce41299cc426620c3e6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d03396e255d31167cb2a8ae6037bbc3f = $(`&lt;div id=&quot;html_d03396e255d31167cb2a8ae6037bbc3f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;350.0&lt;/div&gt;`)[0];
            popup_449d92d72b354ce41299cc426620c3e6.setContent(html_d03396e255d31167cb2a8ae6037bbc3f);


        circle_marker_28fa1bd55b07dd9414774f09510b0e50.bindPopup(popup_449d92d72b354ce41299cc426620c3e6)
        ;




            var circle_marker_3d945a20b1f3cd343baf8ccd3c43b82f = L.circleMarker(
                [40.42898, -3.6133],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_0ced573dde948a9529fcca9e4bd36005 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6557141cfc88bcbeefcef7e2c9b29bdf = $(`&lt;div id=&quot;html_6557141cfc88bcbeefcef7e2c9b29bdf&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;600.0&lt;/div&gt;`)[0];
            popup_0ced573dde948a9529fcca9e4bd36005.setContent(html_6557141cfc88bcbeefcef7e2c9b29bdf);


        circle_marker_3d945a20b1f3cd343baf8ccd3c43b82f.bindPopup(popup_0ced573dde948a9529fcca9e4bd36005)
        ;




            var circle_marker_a3bb76a56779007423954b857704fe2f = L.circleMarker(
                [40.42452, -3.61933],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9c5be1de7deae89176f2797e25960d31 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_90f05cc8eab34f1f8a96fa8c6917e4f6 = $(`&lt;div id=&quot;html_90f05cc8eab34f1f8a96fa8c6917e4f6&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;950.0&lt;/div&gt;`)[0];
            popup_9c5be1de7deae89176f2797e25960d31.setContent(html_90f05cc8eab34f1f8a96fa8c6917e4f6);


        circle_marker_a3bb76a56779007423954b857704fe2f.bindPopup(popup_9c5be1de7deae89176f2797e25960d31)
        ;




            var circle_marker_67cfc5a4163ccda3fa1d7f88b916411b = L.circleMarker(
                [40.44743, -3.60449],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ee520d37b1372ae6c8fd696bb9a37646 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2613c44e931d8f5092f8a06d5292d38b = $(`&lt;div id=&quot;html_2613c44e931d8f5092f8a06d5292d38b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_ee520d37b1372ae6c8fd696bb9a37646.setContent(html_2613c44e931d8f5092f8a06d5292d38b);


        circle_marker_67cfc5a4163ccda3fa1d7f88b916411b.bindPopup(popup_ee520d37b1372ae6c8fd696bb9a37646)
        ;




            var circle_marker_6cc791fd8b7cecb3630347f678f80887 = L.circleMarker(
                [40.44304, -3.58532],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_27c7bc921eacdbc2a969108ede29d400 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6973eb856603ad233dffeab3984a295e = $(`&lt;div id=&quot;html_6973eb856603ad233dffeab3984a295e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;650.0&lt;/div&gt;`)[0];
            popup_27c7bc921eacdbc2a969108ede29d400.setContent(html_6973eb856603ad233dffeab3984a295e);


        circle_marker_6cc791fd8b7cecb3630347f678f80887.bindPopup(popup_27c7bc921eacdbc2a969108ede29d400)
        ;




            var circle_marker_8972eff1fd2cfa03494831147ba7ce45 = L.circleMarker(
                [40.44315, -3.61253],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_6de4ee130701e145a90f6586cc6c2378 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_3b1db1eea28c82822d0a1f6d884c4a90 = $(`&lt;div id=&quot;html_3b1db1eea28c82822d0a1f6d884c4a90&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_6de4ee130701e145a90f6586cc6c2378.setContent(html_3b1db1eea28c82822d0a1f6d884c4a90);


        circle_marker_8972eff1fd2cfa03494831147ba7ce45.bindPopup(popup_6de4ee130701e145a90f6586cc6c2378)
        ;




            var circle_marker_360c746c637d5923ae94872c32abb7a7 = L.circleMarker(
                [40.44506, -3.6099],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_87800e76da8a9401e821da861a2aad86 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_79d2bed2575992fd8f50ba8b88ed9934 = $(`&lt;div id=&quot;html_79d2bed2575992fd8f50ba8b88ed9934&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1000.0&lt;/div&gt;`)[0];
            popup_87800e76da8a9401e821da861a2aad86.setContent(html_79d2bed2575992fd8f50ba8b88ed9934);


        circle_marker_360c746c637d5923ae94872c32abb7a7.bindPopup(popup_87800e76da8a9401e821da861a2aad86)
        ;




            var circle_marker_2ff5d8f68a8c569a8fc0ee8896c3e8cd = L.circleMarker(
                [40.4461, -3.58302],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_585be01d150e8ab52a1c3b27f33f5153 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e8ec539a04e19678dc652daa8892c9da = $(`&lt;div id=&quot;html_e8ec539a04e19678dc652daa8892c9da&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;69.0&lt;/div&gt;`)[0];
            popup_585be01d150e8ab52a1c3b27f33f5153.setContent(html_e8ec539a04e19678dc652daa8892c9da);


        circle_marker_2ff5d8f68a8c569a8fc0ee8896c3e8cd.bindPopup(popup_585be01d150e8ab52a1c3b27f33f5153)
        ;




            var circle_marker_51d2a34e418d8af0497ebdc07afcb2d4 = L.circleMarker(
                [40.43964, -3.62306],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_85c4f2f8af36d7f8ab94da4636323963 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_c4c4e5576fe32661eb1498534109005f = $(`&lt;div id=&quot;html_c4c4e5576fe32661eb1498534109005f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;900.0&lt;/div&gt;`)[0];
            popup_85c4f2f8af36d7f8ab94da4636323963.setContent(html_c4c4e5576fe32661eb1498534109005f);


        circle_marker_51d2a34e418d8af0497ebdc07afcb2d4.bindPopup(popup_85c4f2f8af36d7f8ab94da4636323963)
        ;




            var circle_marker_9dd2678e2b6ed9e308937b598f76e049 = L.circleMarker(
                [40.43559, -3.61088],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_1813a1d5c70a0ab9dc282a7da2c021a2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7bdd19cb5da28b82748ff8ec9caf4243 = $(`&lt;div id=&quot;html_7bdd19cb5da28b82748ff8ec9caf4243&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;300.0&lt;/div&gt;`)[0];
            popup_1813a1d5c70a0ab9dc282a7da2c021a2.setContent(html_7bdd19cb5da28b82748ff8ec9caf4243);


        circle_marker_9dd2678e2b6ed9e308937b598f76e049.bindPopup(popup_1813a1d5c70a0ab9dc282a7da2c021a2)
        ;




            var circle_marker_60f76ea7e77428df042ed3ce770f103c = L.circleMarker(
                [40.43162, -3.61689],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c18a2d86df7a6433b706a47d73556eb1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7d2593febab5aa9dd0c3eb2b469a0d3c = $(`&lt;div id=&quot;html_7d2593febab5aa9dd0c3eb2b469a0d3c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1000.0&lt;/div&gt;`)[0];
            popup_c18a2d86df7a6433b706a47d73556eb1.setContent(html_7d2593febab5aa9dd0c3eb2b469a0d3c);


        circle_marker_60f76ea7e77428df042ed3ce770f103c.bindPopup(popup_c18a2d86df7a6433b706a47d73556eb1)
        ;




            var circle_marker_7d9967282e8caee37968f2942cd173f7 = L.circleMarker(
                [40.43777, -3.60938],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_db8dad047c44fa843307d41d6701f7a5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7f19f0bbed0a0b63fa69e23cab3302de = $(`&lt;div id=&quot;html_7f19f0bbed0a0b63fa69e23cab3302de&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;315.0&lt;/div&gt;`)[0];
            popup_db8dad047c44fa843307d41d6701f7a5.setContent(html_7f19f0bbed0a0b63fa69e23cab3302de);


        circle_marker_7d9967282e8caee37968f2942cd173f7.bindPopup(popup_db8dad047c44fa843307d41d6701f7a5)
        ;




            var circle_marker_20feebdc40bed4f19a55fbea4773b07b = L.circleMarker(
                [40.435, -3.61656],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f40168455ec4c6106c5070cb1dec2cb1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b082ca33418b5130aba68fe47814806b = $(`&lt;div id=&quot;html_b082ca33418b5130aba68fe47814806b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;182.0&lt;/div&gt;`)[0];
            popup_f40168455ec4c6106c5070cb1dec2cb1.setContent(html_b082ca33418b5130aba68fe47814806b);


        circle_marker_20feebdc40bed4f19a55fbea4773b07b.bindPopup(popup_f40168455ec4c6106c5070cb1dec2cb1)
        ;




            var circle_marker_4ed365f9e4ec96f9425486e31f0c350a = L.circleMarker(
                [40.444, -3.59137],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d2087a4ce340213c8b0bc922a5f9b138 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_26dd1a7613b7d65a48a00ea8b8e4d38d = $(`&lt;div id=&quot;html_26dd1a7613b7d65a48a00ea8b8e4d38d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;85.0&lt;/div&gt;`)[0];
            popup_d2087a4ce340213c8b0bc922a5f9b138.setContent(html_26dd1a7613b7d65a48a00ea8b8e4d38d);


        circle_marker_4ed365f9e4ec96f9425486e31f0c350a.bindPopup(popup_d2087a4ce340213c8b0bc922a5f9b138)
        ;




            var circle_marker_9cda1234861ab904b32085dd787ad282 = L.circleMarker(
                [40.43025, -3.61878],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_cf8c4daebd48816e5853e8c0ea03a514 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7d345f240a507e6b6ff20bc4c287ca8b = $(`&lt;div id=&quot;html_7d345f240a507e6b6ff20bc4c287ca8b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;900.0&lt;/div&gt;`)[0];
            popup_cf8c4daebd48816e5853e8c0ea03a514.setContent(html_7d345f240a507e6b6ff20bc4c287ca8b);


        circle_marker_9cda1234861ab904b32085dd787ad282.bindPopup(popup_cf8c4daebd48816e5853e8c0ea03a514)
        ;




            var circle_marker_eaba89f198613682e03873f2ae19b91b = L.circleMarker(
                [40.44341, -3.6093],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3171ae0b71876599b5372be972ad746e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_8e1bb366c3b48c8a722bc0d4f62485ca = $(`&lt;div id=&quot;html_8e1bb366c3b48c8a722bc0d4f62485ca&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;250.0&lt;/div&gt;`)[0];
            popup_3171ae0b71876599b5372be972ad746e.setContent(html_8e1bb366c3b48c8a722bc0d4f62485ca);


        circle_marker_eaba89f198613682e03873f2ae19b91b.bindPopup(popup_3171ae0b71876599b5372be972ad746e)
        ;




            var circle_marker_4ac8f561100ec22012d1f3464f98c31e = L.circleMarker(
                [40.44373, -3.58723],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_0e17a36b55c87e6d4cc4825f0254726f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b331a4c3733b40511972f26f3b07ee37 = $(`&lt;div id=&quot;html_b331a4c3733b40511972f26f3b07ee37&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1260.0&lt;/div&gt;`)[0];
            popup_0e17a36b55c87e6d4cc4825f0254726f.setContent(html_b331a4c3733b40511972f26f3b07ee37);


        circle_marker_4ac8f561100ec22012d1f3464f98c31e.bindPopup(popup_0e17a36b55c87e6d4cc4825f0254726f)
        ;




            var circle_marker_271f7aed3b6d0bc405fbbbcb0ac4a7e1 = L.circleMarker(
                [40.43532, -3.61878],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_09cfbc27e1d4cb2a37f34f734b8123f5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d6bbb7f1ee6c157f14eb4614f66db7bc = $(`&lt;div id=&quot;html_d6bbb7f1ee6c157f14eb4614f66db7bc&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1500.0&lt;/div&gt;`)[0];
            popup_09cfbc27e1d4cb2a37f34f734b8123f5.setContent(html_d6bbb7f1ee6c157f14eb4614f66db7bc);


        circle_marker_271f7aed3b6d0bc405fbbbcb0ac4a7e1.bindPopup(popup_09cfbc27e1d4cb2a37f34f734b8123f5)
        ;




            var circle_marker_9ad8fd775e830f56da579d280b61f5cd = L.circleMarker(
                [40.43709, -3.62448],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4eb7b7a23767c21f25f3d3f3177a3328 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_f8dacc8a48bdfb1a89a3b9f9f3ee1f2e = $(`&lt;div id=&quot;html_f8dacc8a48bdfb1a89a3b9f9f3ee1f2e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;200.0&lt;/div&gt;`)[0];
            popup_4eb7b7a23767c21f25f3d3f3177a3328.setContent(html_f8dacc8a48bdfb1a89a3b9f9f3ee1f2e);


        circle_marker_9ad8fd775e830f56da579d280b61f5cd.bindPopup(popup_4eb7b7a23767c21f25f3d3f3177a3328)
        ;




            var circle_marker_bb87d350c586785728ce470a139c84dc = L.circleMarker(
                [40.43682, -3.63117],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_51c3d41b4106788dfedd64144c0e3652 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a1fb1ab2297641158af4ff2b146c1b8d = $(`&lt;div id=&quot;html_a1fb1ab2297641158af4ff2b146c1b8d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;250.0&lt;/div&gt;`)[0];
            popup_51c3d41b4106788dfedd64144c0e3652.setContent(html_a1fb1ab2297641158af4ff2b146c1b8d);


        circle_marker_bb87d350c586785728ce470a139c84dc.bindPopup(popup_51c3d41b4106788dfedd64144c0e3652)
        ;




            var circle_marker_da3de18d39eb0f08f5008af2ba6fe2ca = L.circleMarker(
                [40.42411, -3.6009],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f6b29ae651acc22b80a3a1c001b2c280 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_8eb8f86ea57b8a4d49676082c6b85253 = $(`&lt;div id=&quot;html_8eb8f86ea57b8a4d49676082c6b85253&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1200.0&lt;/div&gt;`)[0];
            popup_f6b29ae651acc22b80a3a1c001b2c280.setContent(html_8eb8f86ea57b8a4d49676082c6b85253);


        circle_marker_da3de18d39eb0f08f5008af2ba6fe2ca.bindPopup(popup_f6b29ae651acc22b80a3a1c001b2c280)
        ;




            var circle_marker_26313cdc1e7b18f39c4e8a81e60e5a64 = L.circleMarker(
                [40.4325, -3.61792],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_fc88ac788e325c3bb89dd0c581d36d08 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_838eb8f7af76feba7ff1876068b4e173 = $(`&lt;div id=&quot;html_838eb8f7af76feba7ff1876068b4e173&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1000.0&lt;/div&gt;`)[0];
            popup_fc88ac788e325c3bb89dd0c581d36d08.setContent(html_838eb8f7af76feba7ff1876068b4e173);


        circle_marker_26313cdc1e7b18f39c4e8a81e60e5a64.bindPopup(popup_fc88ac788e325c3bb89dd0c581d36d08)
        ;




            var circle_marker_f36c0902fa4959eeea8f72d19a870913 = L.circleMarker(
                [40.43803, -3.60775],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b57dc1abd0f9ba4f0e40287b840093e9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7e7ad2a525965d18cddcab7437676ce3 = $(`&lt;div id=&quot;html_7e7ad2a525965d18cddcab7437676ce3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;2450.0&lt;/div&gt;`)[0];
            popup_b57dc1abd0f9ba4f0e40287b840093e9.setContent(html_7e7ad2a525965d18cddcab7437676ce3);


        circle_marker_f36c0902fa4959eeea8f72d19a870913.bindPopup(popup_b57dc1abd0f9ba4f0e40287b840093e9)
        ;




            var circle_marker_9c9429ba152feb4741ff257969e5cf25 = L.circleMarker(
                [40.43247, -3.61189],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c695dc1c43e0820a5ac7361d2eff1910 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a4e33ef254d997b6af26809a843e90a0 = $(`&lt;div id=&quot;html_a4e33ef254d997b6af26809a843e90a0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;210.0&lt;/div&gt;`)[0];
            popup_c695dc1c43e0820a5ac7361d2eff1910.setContent(html_a4e33ef254d997b6af26809a843e90a0);


        circle_marker_9c9429ba152feb4741ff257969e5cf25.bindPopup(popup_c695dc1c43e0820a5ac7361d2eff1910)
        ;




            var circle_marker_b628901ab63684dce88b043111a20387 = L.circleMarker(
                [40.43701, -3.61917],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_334767c56f261f02a14f11b8cd6b4d91 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_8a2d6faabf738d45ebad861f84b1cba4 = $(`&lt;div id=&quot;html_8a2d6faabf738d45ebad861f84b1cba4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;250.0&lt;/div&gt;`)[0];
            popup_334767c56f261f02a14f11b8cd6b4d91.setContent(html_8a2d6faabf738d45ebad861f84b1cba4);


        circle_marker_b628901ab63684dce88b043111a20387.bindPopup(popup_334767c56f261f02a14f11b8cd6b4d91)
        ;




            var circle_marker_47fb59ee94d496e6adb9d48d976255bd = L.circleMarker(
                [40.41629, -3.61807],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_cc56bffb98453f6f89272a606ea8cd09 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e8217430a092e1bab8446dec814d4e3d = $(`&lt;div id=&quot;html_e8217430a092e1bab8446dec814d4e3d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;147.0&lt;/div&gt;`)[0];
            popup_cc56bffb98453f6f89272a606ea8cd09.setContent(html_e8217430a092e1bab8446dec814d4e3d);


        circle_marker_47fb59ee94d496e6adb9d48d976255bd.bindPopup(popup_cc56bffb98453f6f89272a606ea8cd09)
        ;




            var circle_marker_a07780da1ba56fa2445776c088286658 = L.circleMarker(
                [40.43982, -3.62385],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e02e7327f7d22de746d2d8e4db8a25dc = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_969890a0f6792b57fa6003080519ea73 = $(`&lt;div id=&quot;html_969890a0f6792b57fa6003080519ea73&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_e02e7327f7d22de746d2d8e4db8a25dc.setContent(html_969890a0f6792b57fa6003080519ea73);


        circle_marker_a07780da1ba56fa2445776c088286658.bindPopup(popup_e02e7327f7d22de746d2d8e4db8a25dc)
        ;




            var circle_marker_21f54b149133e54055344ba5d40e7180 = L.circleMarker(
                [40.4264, -3.62066],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_082b928146d8059902ad5efdda8cdfaa = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_87ee2f184c65cc552e63743a021acc4c = $(`&lt;div id=&quot;html_87ee2f184c65cc552e63743a021acc4c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;800.0&lt;/div&gt;`)[0];
            popup_082b928146d8059902ad5efdda8cdfaa.setContent(html_87ee2f184c65cc552e63743a021acc4c);


        circle_marker_21f54b149133e54055344ba5d40e7180.bindPopup(popup_082b928146d8059902ad5efdda8cdfaa)
        ;




            var circle_marker_376f2f6a47d6e961278b5a3a63836cce = L.circleMarker(
                [40.44292, -3.60764],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a91b5bcb4953bfd4076b2d6a2f412f86 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4278689c6a3d679854f2af49664c54a5 = $(`&lt;div id=&quot;html_4278689c6a3d679854f2af49664c54a5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;3000.0&lt;/div&gt;`)[0];
            popup_a91b5bcb4953bfd4076b2d6a2f412f86.setContent(html_4278689c6a3d679854f2af49664c54a5);


        circle_marker_376f2f6a47d6e961278b5a3a63836cce.bindPopup(popup_a91b5bcb4953bfd4076b2d6a2f412f86)
        ;




            var circle_marker_a31c39e06f30e155acad891a60c67f72 = L.circleMarker(
                [40.44238, -3.57244],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_2d6022c8d93e892a91ad85d471e797f5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ce947410a33dae3e1ae1c4c374fbbe9c = $(`&lt;div id=&quot;html_ce947410a33dae3e1ae1c4c374fbbe9c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;40.0&lt;/div&gt;`)[0];
            popup_2d6022c8d93e892a91ad85d471e797f5.setContent(html_ce947410a33dae3e1ae1c4c374fbbe9c);


        circle_marker_a31c39e06f30e155acad891a60c67f72.bindPopup(popup_2d6022c8d93e892a91ad85d471e797f5)
        ;




            var circle_marker_ba62c259f3ccf4a629ada625fa7ec58e = L.circleMarker(
                [40.42003, -3.61274],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4909eb41f7019f8b62cfc6235b3c6601 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_65e757dc26efc2b6a4663815da5a3d84 = $(`&lt;div id=&quot;html_65e757dc26efc2b6a4663815da5a3d84&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;1900.0&lt;/div&gt;`)[0];
            popup_4909eb41f7019f8b62cfc6235b3c6601.setContent(html_65e757dc26efc2b6a4663815da5a3d84);


        circle_marker_ba62c259f3ccf4a629ada625fa7ec58e.bindPopup(popup_4909eb41f7019f8b62cfc6235b3c6601)
        ;




            var circle_marker_477414f0e5798a60e62ee2e838394f1c = L.circleMarker(
                [40.42144, -3.61298],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e7f8b2105dde59afad9984434549aacc = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_48177c2164664fd6e78be2f64728a0f4 = $(`&lt;div id=&quot;html_48177c2164664fd6e78be2f64728a0f4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;800.0&lt;/div&gt;`)[0];
            popup_e7f8b2105dde59afad9984434549aacc.setContent(html_48177c2164664fd6e78be2f64728a0f4);


        circle_marker_477414f0e5798a60e62ee2e838394f1c.bindPopup(popup_e7f8b2105dde59afad9984434549aacc)
        ;




            var circle_marker_73f1afb988d9274a0ca931be3846c195 = L.circleMarker(
                [40.43492, -3.60853],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9badc87575ece52f14d75375682f5685 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2bb6f84fa868ce93ddf685e03a5ba110 = $(`&lt;div id=&quot;html_2bb6f84fa868ce93ddf685e03a5ba110&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;420.0&lt;/div&gt;`)[0];
            popup_9badc87575ece52f14d75375682f5685.setContent(html_2bb6f84fa868ce93ddf685e03a5ba110);


        circle_marker_73f1afb988d9274a0ca931be3846c195.bindPopup(popup_9badc87575ece52f14d75375682f5685)
        ;




            var circle_marker_641ab1556af96ba6e07fb20c683b4f5e = L.circleMarker(
                [40.43699, -3.60813],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_2db0a44d3a01123860634aee14575c8a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_54bb3fe89ac5dc440df9bee43c981861 = $(`&lt;div id=&quot;html_54bb3fe89ac5dc440df9bee43c981861&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;420.0&lt;/div&gt;`)[0];
            popup_2db0a44d3a01123860634aee14575c8a.setContent(html_54bb3fe89ac5dc440df9bee43c981861);


        circle_marker_641ab1556af96ba6e07fb20c683b4f5e.bindPopup(popup_2db0a44d3a01123860634aee14575c8a)
        ;




            var circle_marker_c3fc7fc0209e419b7aa1a5c110a5df3f = L.circleMarker(
                [40.43409, -3.62502],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9afbe8ef0271608722802005c310ecdf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_69d78287bc8eaf97882ed6b56d97177e = $(`&lt;div id=&quot;html_69d78287bc8eaf97882ed6b56d97177e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;45.0&lt;/div&gt;`)[0];
            popup_9afbe8ef0271608722802005c310ecdf.setContent(html_69d78287bc8eaf97882ed6b56d97177e);


        circle_marker_c3fc7fc0209e419b7aa1a5c110a5df3f.bindPopup(popup_9afbe8ef0271608722802005c310ecdf)
        ;




            var circle_marker_2fa884a951e6c40d6fd5f771c03a6c04 = L.circleMarker(
                [40.43679, -3.61506],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a986e1c158cedc071a53bff025ebbad7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_805392e682504cf3250a5a219873baec = $(`&lt;div id=&quot;html_805392e682504cf3250a5a219873baec&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;28.0&lt;/div&gt;`)[0];
            popup_a986e1c158cedc071a53bff025ebbad7.setContent(html_805392e682504cf3250a5a219873baec);


        circle_marker_2fa884a951e6c40d6fd5f771c03a6c04.bindPopup(popup_a986e1c158cedc071a53bff025ebbad7)
        ;




            var circle_marker_cdb1ebf209152afddf9ffcd2290a5b6f = L.circleMarker(
                [40.43207, -3.62518],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3e7163424e9d78a5e959574397cf4375 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_99696bea056b995f2131a66bb9a50ad4 = $(`&lt;div id=&quot;html_99696bea056b995f2131a66bb9a50ad4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;45.0&lt;/div&gt;`)[0];
            popup_3e7163424e9d78a5e959574397cf4375.setContent(html_99696bea056b995f2131a66bb9a50ad4);


        circle_marker_cdb1ebf209152afddf9ffcd2290a5b6f.bindPopup(popup_3e7163424e9d78a5e959574397cf4375)
        ;




            var circle_marker_ea9d89e8ba50e9160423e2c8ae310874 = L.circleMarker(
                [40.4271, -3.60073],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_10d6382200060f973801a0b813286957 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4aceb6bd48a008d10752795a01e5e260 = $(`&lt;div id=&quot;html_4aceb6bd48a008d10752795a01e5e260&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;160.0&lt;/div&gt;`)[0];
            popup_10d6382200060f973801a0b813286957.setContent(html_4aceb6bd48a008d10752795a01e5e260);


        circle_marker_ea9d89e8ba50e9160423e2c8ae310874.bindPopup(popup_10d6382200060f973801a0b813286957)
        ;




            var circle_marker_26b73e39804250a2dd1e0820ff4fb7ff = L.circleMarker(
                [40.44406, -3.63545],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_7206bac643eb128d3b19f025e8b10dfb = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6d3b49c576b6fe2d8eb64bd59b9e48d2 = $(`&lt;div id=&quot;html_6d3b49c576b6fe2d8eb64bd59b9e48d2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;89.0&lt;/div&gt;`)[0];
            popup_7206bac643eb128d3b19f025e8b10dfb.setContent(html_6d3b49c576b6fe2d8eb64bd59b9e48d2);


        circle_marker_26b73e39804250a2dd1e0820ff4fb7ff.bindPopup(popup_7206bac643eb128d3b19f025e8b10dfb)
        ;




            var circle_marker_088ca93e54a73444fd9d0b1759ec443c = L.circleMarker(
                [40.42463, -3.60616],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f6aea18572c5223428eaa9d6c0b60fd2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_5f79744f40b1e43f915bcb4fd5d6fc41 = $(`&lt;div id=&quot;html_5f79744f40b1e43f915bcb4fd5d6fc41&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;140.0&lt;/div&gt;`)[0];
            popup_f6aea18572c5223428eaa9d6c0b60fd2.setContent(html_5f79744f40b1e43f915bcb4fd5d6fc41);


        circle_marker_088ca93e54a73444fd9d0b1759ec443c.bindPopup(popup_f6aea18572c5223428eaa9d6c0b60fd2)
        ;




            var circle_marker_e510366b786c3437cb71adfa45083cb2 = L.circleMarker(
                [40.43453, -3.60631],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9e82a1b3723ba31775969e5164192675 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4693ed2ae0bb8cc29c641772e4b36aa9 = $(`&lt;div id=&quot;html_4693ed2ae0bb8cc29c641772e4b36aa9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;367.5&lt;/div&gt;`)[0];
            popup_9e82a1b3723ba31775969e5164192675.setContent(html_4693ed2ae0bb8cc29c641772e4b36aa9);


        circle_marker_e510366b786c3437cb71adfa45083cb2.bindPopup(popup_9e82a1b3723ba31775969e5164192675)
        ;




            var circle_marker_4c361ac6e76f37dc06047b45b918aee0 = L.circleMarker(
                [40.42445, -3.62002],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4ad6b768224f91e04a9a82ced268f032 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d57ee742b57dc1cf3475f7ddbe230e92 = $(`&lt;div id=&quot;html_d57ee742b57dc1cf3475f7ddbe230e92&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;113.0&lt;/div&gt;`)[0];
            popup_4ad6b768224f91e04a9a82ced268f032.setContent(html_d57ee742b57dc1cf3475f7ddbe230e92);


        circle_marker_4c361ac6e76f37dc06047b45b918aee0.bindPopup(popup_4ad6b768224f91e04a9a82ced268f032)
        ;




            var circle_marker_fa4267ad722631355208fe5d5e5dc3fb = L.circleMarker(
                [40.4483, -3.60695],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a064a3d7adfb61fcf029ccb3e17cce84 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_bb2ee16a88aa32c20570ea7e81162b92 = $(`&lt;div id=&quot;html_bb2ee16a88aa32c20570ea7e81162b92&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;22.0&lt;/div&gt;`)[0];
            popup_a064a3d7adfb61fcf029ccb3e17cce84.setContent(html_bb2ee16a88aa32c20570ea7e81162b92);


        circle_marker_fa4267ad722631355208fe5d5e5dc3fb.bindPopup(popup_a064a3d7adfb61fcf029ccb3e17cce84)
        ;




            var circle_marker_348b720c012a4283cc8714a408899ec8 = L.circleMarker(
                [40.43542, -3.60796],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4de46cc61149dbddf30b60a6e0a52211 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0de5408519f32d2c1b01a3f0ad118386 = $(`&lt;div id=&quot;html_0de5408519f32d2c1b01a3f0ad118386&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;105.0&lt;/div&gt;`)[0];
            popup_4de46cc61149dbddf30b60a6e0a52211.setContent(html_0de5408519f32d2c1b01a3f0ad118386);


        circle_marker_348b720c012a4283cc8714a408899ec8.bindPopup(popup_4de46cc61149dbddf30b60a6e0a52211)
        ;




            var circle_marker_3bcfa1ba868b83207b5c0a18b33559ee = L.circleMarker(
                [40.44752, -3.61102],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d50d8076badb2061fd9520e551f42bd3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_fe28677d26e758d12865d52b5fca5903 = $(`&lt;div id=&quot;html_fe28677d26e758d12865d52b5fca5903&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;20.0&lt;/div&gt;`)[0];
            popup_d50d8076badb2061fd9520e551f42bd3.setContent(html_fe28677d26e758d12865d52b5fca5903);


        circle_marker_3bcfa1ba868b83207b5c0a18b33559ee.bindPopup(popup_d50d8076badb2061fd9520e551f42bd3)
        ;




            var circle_marker_ec04a31b54505394664547c9c7eb4174 = L.circleMarker(
                [40.43132, -3.6155],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;red&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;red&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4313e38b190875535b3f61fa8b848a45 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b95f0c4d11fa5327d91636e5b4f6a4d4 = $(`&lt;div id=&quot;html_b95f0c4d11fa5327d91636e5b4f6a4d4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;800.0&lt;/div&gt;`)[0];
            popup_4313e38b190875535b3f61fa8b848a45.setContent(html_b95f0c4d11fa5327d91636e5b4f6a4d4);


        circle_marker_ec04a31b54505394664547c9c7eb4174.bindPopup(popup_4313e38b190875535b3f61fa8b848a45)
        ;




            var circle_marker_942d4c90cabf93d206c6e1a51c5bed29 = L.circleMarker(
                [40.44355, -3.58184],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a4a13a5a2e3737f90f647507123c2e58 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7e232f05d48ddfdce9c39fc687b5b337 = $(`&lt;div id=&quot;html_7e232f05d48ddfdce9c39fc687b5b337&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;70.0&lt;/div&gt;`)[0];
            popup_a4a13a5a2e3737f90f647507123c2e58.setContent(html_7e232f05d48ddfdce9c39fc687b5b337);


        circle_marker_942d4c90cabf93d206c6e1a51c5bed29.bindPopup(popup_a4a13a5a2e3737f90f647507123c2e58)
        ;




            var circle_marker_f7d33db46c1ce462c659def6bf5a58db = L.circleMarker(
                [40.42661, -3.61733],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_0d04a145546845ce9d9a1576ce15af23 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_f55287ff7bb5b0fbf35aae51ddc36d54 = $(`&lt;div id=&quot;html_f55287ff7bb5b0fbf35aae51ddc36d54&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;49.0&lt;/div&gt;`)[0];
            popup_0d04a145546845ce9d9a1576ce15af23.setContent(html_f55287ff7bb5b0fbf35aae51ddc36d54);


        circle_marker_f7d33db46c1ce462c659def6bf5a58db.bindPopup(popup_0d04a145546845ce9d9a1576ce15af23)
        ;




            var circle_marker_5a7e95a8c82aec2a32bd056d52df17be = L.circleMarker(
                [40.43976, -3.6104],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_cbcbed36015e17bc9616aff4ca18c50d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a41fcb97bbe5b7fc939e36014ad9c3e1 = $(`&lt;div id=&quot;html_a41fcb97bbe5b7fc939e36014ad9c3e1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;22.0&lt;/div&gt;`)[0];
            popup_cbcbed36015e17bc9616aff4ca18c50d.setContent(html_a41fcb97bbe5b7fc939e36014ad9c3e1);


        circle_marker_5a7e95a8c82aec2a32bd056d52df17be.bindPopup(popup_cbcbed36015e17bc9616aff4ca18c50d)
        ;




            var circle_marker_fd7ac883521c76f95e2b983557292ef5 = L.circleMarker(
                [40.44609, -3.58831],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_da6d1655d3ad06744edf68960ff46b11 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0407f09de55186b0e0d38b38585abb89 = $(`&lt;div id=&quot;html_0407f09de55186b0e0d38b38585abb89&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;85.0&lt;/div&gt;`)[0];
            popup_da6d1655d3ad06744edf68960ff46b11.setContent(html_0407f09de55186b0e0d38b38585abb89);


        circle_marker_fd7ac883521c76f95e2b983557292ef5.bindPopup(popup_da6d1655d3ad06744edf68960ff46b11)
        ;




            var circle_marker_d5c79057332dd11670c949e7760842c8 = L.circleMarker(
                [40.42621, -3.60971],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_89aef82ef4a70ddebf1aa40d224ee3cd = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1eeeec2ceb74e9494f85848a73a2e4dc = $(`&lt;div id=&quot;html_1eeeec2ceb74e9494f85848a73a2e4dc&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;40.0&lt;/div&gt;`)[0];
            popup_89aef82ef4a70ddebf1aa40d224ee3cd.setContent(html_1eeeec2ceb74e9494f85848a73a2e4dc);


        circle_marker_d5c79057332dd11670c949e7760842c8.bindPopup(popup_89aef82ef4a70ddebf1aa40d224ee3cd)
        ;




            var circle_marker_cbc9774378cf10be0ee828da22b5e345 = L.circleMarker(
                [40.42779, -3.60949],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f2fe7a330319e794cb42a9750e4c3153 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_15e1ea390882a0f29756d4b2c5521d5f = $(`&lt;div id=&quot;html_15e1ea390882a0f29756d4b2c5521d5f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;28.0&lt;/div&gt;`)[0];
            popup_f2fe7a330319e794cb42a9750e4c3153.setContent(html_15e1ea390882a0f29756d4b2c5521d5f);


        circle_marker_cbc9774378cf10be0ee828da22b5e345.bindPopup(popup_f2fe7a330319e794cb42a9750e4c3153)
        ;




            var circle_marker_374cd685bd667880824cd6014ac76b2e = L.circleMarker(
                [40.43826, -3.60656],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_071c1f4f7549eef42e4c36d98e78258e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_79cfd9ddd1bfc4417d7e2b1dce1d89d2 = $(`&lt;div id=&quot;html_79cfd9ddd1bfc4417d7e2b1dce1d89d2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;35.0&lt;/div&gt;`)[0];
            popup_071c1f4f7549eef42e4c36d98e78258e.setContent(html_79cfd9ddd1bfc4417d7e2b1dce1d89d2);


        circle_marker_374cd685bd667880824cd6014ac76b2e.bindPopup(popup_071c1f4f7549eef42e4c36d98e78258e)
        ;




            var circle_marker_fc48f2c02b5dcfbb86e57126c4a961dc = L.circleMarker(
                [40.42393, -3.61109],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_634346773860f312bc818ed501e01e9e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_065ec0ddbc32b6e65334a34dc60a6134 = $(`&lt;div id=&quot;html_065ec0ddbc32b6e65334a34dc60a6134&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;29.0&lt;/div&gt;`)[0];
            popup_634346773860f312bc818ed501e01e9e.setContent(html_065ec0ddbc32b6e65334a34dc60a6134);


        circle_marker_fc48f2c02b5dcfbb86e57126c4a961dc.bindPopup(popup_634346773860f312bc818ed501e01e9e)
        ;




            var circle_marker_2d67b27e98b812b72eb19c02f6374c84 = L.circleMarker(
                [40.43227, -3.62511],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b23d223a4ebe12deea0b23b9dd49f896 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4571979ac17bd9bc3fb57f69d6a5ba03 = $(`&lt;div id=&quot;html_4571979ac17bd9bc3fb57f69d6a5ba03&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.0&lt;/div&gt;`)[0];
            popup_b23d223a4ebe12deea0b23b9dd49f896.setContent(html_4571979ac17bd9bc3fb57f69d6a5ba03);


        circle_marker_2d67b27e98b812b72eb19c02f6374c84.bindPopup(popup_b23d223a4ebe12deea0b23b9dd49f896)
        ;




            var circle_marker_9371b4f44871adcea376d1bfc4a1cad5 = L.circleMarker(
                [40.44606, -3.59655],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_7fa19fead1ed0303bb3de433be9f91ef = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_84fa25c180f67aa21c05a696a45aac2c = $(`&lt;div id=&quot;html_84fa25c180f67aa21c05a696a45aac2c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;21.0&lt;/div&gt;`)[0];
            popup_7fa19fead1ed0303bb3de433be9f91ef.setContent(html_84fa25c180f67aa21c05a696a45aac2c);


        circle_marker_9371b4f44871adcea376d1bfc4a1cad5.bindPopup(popup_7fa19fead1ed0303bb3de433be9f91ef)
        ;




            var circle_marker_8d5bdf7d452f7924bc9132ad6b72c647 = L.circleMarker(
                [40.44265, -3.57248],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_cb18f88e8df7250d212bdef8e801646e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d827d64b256b73a0b5bfff0f505c7c2c = $(`&lt;div id=&quot;html_d827d64b256b73a0b5bfff0f505c7c2c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;55.0&lt;/div&gt;`)[0];
            popup_cb18f88e8df7250d212bdef8e801646e.setContent(html_d827d64b256b73a0b5bfff0f505c7c2c);


        circle_marker_8d5bdf7d452f7924bc9132ad6b72c647.bindPopup(popup_cb18f88e8df7250d212bdef8e801646e)
        ;




            var circle_marker_a84929d80a77fa57aefc46db0103d35d = L.circleMarker(
                [40.4268, -3.62007],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_039cc70b84bad228a7504050938a2263 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0ce4a2885af43cc882599ed0fa5dd497 = $(`&lt;div id=&quot;html_0ce4a2885af43cc882599ed0fa5dd497&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;35.0&lt;/div&gt;`)[0];
            popup_039cc70b84bad228a7504050938a2263.setContent(html_0ce4a2885af43cc882599ed0fa5dd497);


        circle_marker_a84929d80a77fa57aefc46db0103d35d.bindPopup(popup_039cc70b84bad228a7504050938a2263)
        ;




            var circle_marker_f873a717f4395b27c924ce4746bf2040 = L.circleMarker(
                [40.44309, -3.58528],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_49cad0be8dff8da26b687f4e3f7d799e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_8ba00df3698cb25ce3f852e600c948a1 = $(`&lt;div id=&quot;html_8ba00df3698cb25ce3f852e600c948a1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;59.0&lt;/div&gt;`)[0];
            popup_49cad0be8dff8da26b687f4e3f7d799e.setContent(html_8ba00df3698cb25ce3f852e600c948a1);


        circle_marker_f873a717f4395b27c924ce4746bf2040.bindPopup(popup_49cad0be8dff8da26b687f4e3f7d799e)
        ;




            var circle_marker_f20c942c5bd933124012ade08e6516dd = L.circleMarker(
                [40.44664, -3.61175],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_0bf4bda80306cfeb6f8ae76513fb4cf1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b106894d8a34b296cfbd2ff2c9c3e466 = $(`&lt;div id=&quot;html_b106894d8a34b296cfbd2ff2c9c3e466&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;67.0&lt;/div&gt;`)[0];
            popup_0bf4bda80306cfeb6f8ae76513fb4cf1.setContent(html_b106894d8a34b296cfbd2ff2c9c3e466);


        circle_marker_f20c942c5bd933124012ade08e6516dd.bindPopup(popup_0bf4bda80306cfeb6f8ae76513fb4cf1)
        ;




            var circle_marker_07f1d6350ac7dc55589071637a51681c = L.circleMarker(
                [40.43105, -3.61652],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_1e0933b2df92bef2ebdc2e4911c15163 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e126da32d34c7151391478c04d3bffc5 = $(`&lt;div id=&quot;html_e126da32d34c7151391478c04d3bffc5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_1e0933b2df92bef2ebdc2e4911c15163.setContent(html_e126da32d34c7151391478c04d3bffc5);


        circle_marker_07f1d6350ac7dc55589071637a51681c.bindPopup(popup_1e0933b2df92bef2ebdc2e4911c15163)
        ;




            var circle_marker_185af6004066d9ed06e8d7388fbceef9 = L.circleMarker(
                [40.44955, -3.5694],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4c1002625cc7cbaafaf0b50978db1290 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_55bfa6e322ae6bd58a66d50f8b98ba18 = $(`&lt;div id=&quot;html_55bfa6e322ae6bd58a66d50f8b98ba18&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;136.5&lt;/div&gt;`)[0];
            popup_4c1002625cc7cbaafaf0b50978db1290.setContent(html_55bfa6e322ae6bd58a66d50f8b98ba18);


        circle_marker_185af6004066d9ed06e8d7388fbceef9.bindPopup(popup_4c1002625cc7cbaafaf0b50978db1290)
        ;




            var circle_marker_ced62e6aded6ee243ed2d027cc76d523 = L.circleMarker(
                [40.44734, -3.56924],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8c6876fbb4b0bcfa522677da69bd0efa = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_8dc4880ca5fc3cc714ac354aa2ca28e4 = $(`&lt;div id=&quot;html_8dc4880ca5fc3cc714ac354aa2ca28e4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;55.0&lt;/div&gt;`)[0];
            popup_8c6876fbb4b0bcfa522677da69bd0efa.setContent(html_8dc4880ca5fc3cc714ac354aa2ca28e4);


        circle_marker_ced62e6aded6ee243ed2d027cc76d523.bindPopup(popup_8c6876fbb4b0bcfa522677da69bd0efa)
        ;




            var circle_marker_6cffca2663f1b21e45ea78feb581427c = L.circleMarker(
                [40.43712, -3.63236],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e8e50963677732f43c727feda10bd7a7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7278b4bfdc996986736bb742febe4630 = $(`&lt;div id=&quot;html_7278b4bfdc996986736bb742febe4630&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;56.0&lt;/div&gt;`)[0];
            popup_e8e50963677732f43c727feda10bd7a7.setContent(html_7278b4bfdc996986736bb742febe4630);


        circle_marker_6cffca2663f1b21e45ea78feb581427c.bindPopup(popup_e8e50963677732f43c727feda10bd7a7)
        ;




            var circle_marker_262779427b272dd4318fc380e03b76a5 = L.circleMarker(
                [40.42548, -3.60921],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a5ef1fb76e8062284ed29d168669f836 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6886ca5a10f447274229a81258b81150 = $(`&lt;div id=&quot;html_6886ca5a10f447274229a81258b81150&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_a5ef1fb76e8062284ed29d168669f836.setContent(html_6886ca5a10f447274229a81258b81150);


        circle_marker_262779427b272dd4318fc380e03b76a5.bindPopup(popup_a5ef1fb76e8062284ed29d168669f836)
        ;




            var circle_marker_e3ebc24677d68ed31828c70548c133ff = L.circleMarker(
                [40.42649, -3.60856],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_2183bf7658530cc0ae24077aaf8643b3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_fb08ea9f87fdf1d7abc371f5f0ca7b38 = $(`&lt;div id=&quot;html_fb08ea9f87fdf1d7abc371f5f0ca7b38&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;22.0&lt;/div&gt;`)[0];
            popup_2183bf7658530cc0ae24077aaf8643b3.setContent(html_fb08ea9f87fdf1d7abc371f5f0ca7b38);


        circle_marker_e3ebc24677d68ed31828c70548c133ff.bindPopup(popup_2183bf7658530cc0ae24077aaf8643b3)
        ;




            var circle_marker_8d9910ba8c5c888103d09fdd5805382c = L.circleMarker(
                [40.42819, -3.61052],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f413f10a5f5968f2e210561b23d3aed6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_3b64654f144d1d887794d00478f98009 = $(`&lt;div id=&quot;html_3b64654f144d1d887794d00478f98009&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;22.0&lt;/div&gt;`)[0];
            popup_f413f10a5f5968f2e210561b23d3aed6.setContent(html_3b64654f144d1d887794d00478f98009);


        circle_marker_8d9910ba8c5c888103d09fdd5805382c.bindPopup(popup_f413f10a5f5968f2e210561b23d3aed6)
        ;




            var circle_marker_4c2c1057acb688069503276e1e8309b3 = L.circleMarker(
                [40.4262, -3.60966],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c052ea20148a6c900fa4059e3588ca51 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9c8bbb2fabc58c4ac859f3f9128805ee = $(`&lt;div id=&quot;html_9c8bbb2fabc58c4ac859f3f9128805ee&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;22.0&lt;/div&gt;`)[0];
            popup_c052ea20148a6c900fa4059e3588ca51.setContent(html_9c8bbb2fabc58c4ac859f3f9128805ee);


        circle_marker_4c2c1057acb688069503276e1e8309b3.bindPopup(popup_c052ea20148a6c900fa4059e3588ca51)
        ;




            var circle_marker_95c8e8ab08a79671b31e4dde50247bd1 = L.circleMarker(
                [40.42773, -3.6103],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_91eaeee93541db6bed0ebe20fd3f36f9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_33225d42ff400e371f0d9127c7848e8e = $(`&lt;div id=&quot;html_33225d42ff400e371f0d9127c7848e8e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;22.0&lt;/div&gt;`)[0];
            popup_91eaeee93541db6bed0ebe20fd3f36f9.setContent(html_33225d42ff400e371f0d9127c7848e8e);


        circle_marker_95c8e8ab08a79671b31e4dde50247bd1.bindPopup(popup_91eaeee93541db6bed0ebe20fd3f36f9)
        ;




            var circle_marker_1735dcc2ec45a96f9f59ab541e9b7619 = L.circleMarker(
                [40.42638, -3.60822],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b7d29fc6b6bfa166c82cc10b2b775f66 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ede7ebdc0bb8ea406fcbe1f58954d4dc = $(`&lt;div id=&quot;html_ede7ebdc0bb8ea406fcbe1f58954d4dc&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.799999999999997&lt;/div&gt;`)[0];
            popup_b7d29fc6b6bfa166c82cc10b2b775f66.setContent(html_ede7ebdc0bb8ea406fcbe1f58954d4dc);


        circle_marker_1735dcc2ec45a96f9f59ab541e9b7619.bindPopup(popup_b7d29fc6b6bfa166c82cc10b2b775f66)
        ;




            var circle_marker_fdd7215514f0e1c873196bb5276fd6b9 = L.circleMarker(
                [40.44127, -3.56764],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5e2f9aa53568d2446d86cfd3b29ad1d5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_30928080c45f913ff0f982f780ca4a33 = $(`&lt;div id=&quot;html_30928080c45f913ff0f982f780ca4a33&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;55.0&lt;/div&gt;`)[0];
            popup_5e2f9aa53568d2446d86cfd3b29ad1d5.setContent(html_30928080c45f913ff0f982f780ca4a33);


        circle_marker_fdd7215514f0e1c873196bb5276fd6b9.bindPopup(popup_5e2f9aa53568d2446d86cfd3b29ad1d5)
        ;




            var circle_marker_0f1560ce1811743e8865c3db59fc741d = L.circleMarker(
                [40.43012, -3.61753],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_7fd865f10ad4a9bf5a967367dd731cff = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7f97fbcf18bf1a4af7b9514ffd706f12 = $(`&lt;div id=&quot;html_7f97fbcf18bf1a4af7b9514ffd706f12&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.0&lt;/div&gt;`)[0];
            popup_7fd865f10ad4a9bf5a967367dd731cff.setContent(html_7f97fbcf18bf1a4af7b9514ffd706f12);


        circle_marker_0f1560ce1811743e8865c3db59fc741d.bindPopup(popup_7fd865f10ad4a9bf5a967367dd731cff)
        ;




            var circle_marker_b7783e5b2d9b03d7c3c204540ca43134 = L.circleMarker(
                [40.43827, -3.63029],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e95589565d916b31b6d677f9f3f48dac = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_233142cd937e8af35011b23c20f4a285 = $(`&lt;div id=&quot;html_233142cd937e8af35011b23c20f4a285&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_e95589565d916b31b6d677f9f3f48dac.setContent(html_233142cd937e8af35011b23c20f4a285);


        circle_marker_b7783e5b2d9b03d7c3c204540ca43134.bindPopup(popup_e95589565d916b31b6d677f9f3f48dac)
        ;




            var circle_marker_164b985153dce9e081a2ad7878388755 = L.circleMarker(
                [40.4296, -3.62755],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_6b5c5d3f341ca7e23aa2a2b5f68384b7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_c7b3ab3502b595af120e167da2cf6cbf = $(`&lt;div id=&quot;html_c7b3ab3502b595af120e167da2cf6cbf&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;75.0&lt;/div&gt;`)[0];
            popup_6b5c5d3f341ca7e23aa2a2b5f68384b7.setContent(html_c7b3ab3502b595af120e167da2cf6cbf);


        circle_marker_164b985153dce9e081a2ad7878388755.bindPopup(popup_6b5c5d3f341ca7e23aa2a2b5f68384b7)
        ;




            var circle_marker_3523362023d9735b17d8b67e8883c88b = L.circleMarker(
                [40.43385, -3.6252],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_47a97aa796827cf10a37dc19001bce7d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4afd3b942608fbdc20935c7c52949519 = $(`&lt;div id=&quot;html_4afd3b942608fbdc20935c7c52949519&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;36.0&lt;/div&gt;`)[0];
            popup_47a97aa796827cf10a37dc19001bce7d.setContent(html_4afd3b942608fbdc20935c7c52949519);


        circle_marker_3523362023d9735b17d8b67e8883c88b.bindPopup(popup_47a97aa796827cf10a37dc19001bce7d)
        ;




            var circle_marker_9f6a23317d53aed2ebbf5138c22f2617 = L.circleMarker(
                [40.4327, -3.60665],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_73793f4dcb5c17b55e859564db669fe4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_01610366a9972e7890965059f52abec4 = $(`&lt;div id=&quot;html_01610366a9972e7890965059f52abec4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;20.0&lt;/div&gt;`)[0];
            popup_73793f4dcb5c17b55e859564db669fe4.setContent(html_01610366a9972e7890965059f52abec4);


        circle_marker_9f6a23317d53aed2ebbf5138c22f2617.bindPopup(popup_73793f4dcb5c17b55e859564db669fe4)
        ;




            var circle_marker_518d5913b79ddb41b9c5fd308732e252 = L.circleMarker(
                [40.44564, -3.57232],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_96b9e98b111d061b40072861585e411b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_db28f0c9411c588de2d0627b6449646d = $(`&lt;div id=&quot;html_db28f0c9411c588de2d0627b6449646d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;48.0&lt;/div&gt;`)[0];
            popup_96b9e98b111d061b40072861585e411b.setContent(html_db28f0c9411c588de2d0627b6449646d);


        circle_marker_518d5913b79ddb41b9c5fd308732e252.bindPopup(popup_96b9e98b111d061b40072861585e411b)
        ;




            var circle_marker_1a5bb3e7d99b582256767ef90de12a98 = L.circleMarker(
                [40.44545, -3.57239],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_2a23a62e9aa3de730e25fe6108f6f4be = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_610748a76dcb17384911b31354346e97 = $(`&lt;div id=&quot;html_610748a76dcb17384911b31354346e97&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;39.0&lt;/div&gt;`)[0];
            popup_2a23a62e9aa3de730e25fe6108f6f4be.setContent(html_610748a76dcb17384911b31354346e97);


        circle_marker_1a5bb3e7d99b582256767ef90de12a98.bindPopup(popup_2a23a62e9aa3de730e25fe6108f6f4be)
        ;




            var circle_marker_808105ec8070c52e1ba324740694c6d3 = L.circleMarker(
                [40.43788, -3.62792],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a27e4857ad4213dd2122ac3bc75cb0d6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_870cc61759c938cd3ce1e84d8605a348 = $(`&lt;div id=&quot;html_870cc61759c938cd3ce1e84d8605a348&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;114.0&lt;/div&gt;`)[0];
            popup_a27e4857ad4213dd2122ac3bc75cb0d6.setContent(html_870cc61759c938cd3ce1e84d8605a348);


        circle_marker_808105ec8070c52e1ba324740694c6d3.bindPopup(popup_a27e4857ad4213dd2122ac3bc75cb0d6)
        ;




            var circle_marker_5389b43a5555e8f65055093fe743a115 = L.circleMarker(
                [40.44744, -3.57105],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8d8fe67628595ae0495f804c378a16ba = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_036d4fcabf1cef868737425a11ae8066 = $(`&lt;div id=&quot;html_036d4fcabf1cef868737425a11ae8066&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;40.0&lt;/div&gt;`)[0];
            popup_8d8fe67628595ae0495f804c378a16ba.setContent(html_036d4fcabf1cef868737425a11ae8066);


        circle_marker_5389b43a5555e8f65055093fe743a115.bindPopup(popup_8d8fe67628595ae0495f804c378a16ba)
        ;




            var circle_marker_bad2d70c4813e39f349e41efc2f07442 = L.circleMarker(
                [40.43568, -3.60931],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_adda24c82d2225172d1d48b4170c7607 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6bd2112a4ec8786851fce863d2dd2bcd = $(`&lt;div id=&quot;html_6bd2112a4ec8786851fce863d2dd2bcd&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;64.0&lt;/div&gt;`)[0];
            popup_adda24c82d2225172d1d48b4170c7607.setContent(html_6bd2112a4ec8786851fce863d2dd2bcd);


        circle_marker_bad2d70c4813e39f349e41efc2f07442.bindPopup(popup_adda24c82d2225172d1d48b4170c7607)
        ;




            var circle_marker_15f432efeb7133cb64cf8594a58ed3d8 = L.circleMarker(
                [40.44458, -3.5815],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d24e2a6956fec8ebee0d0c309c8315d6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_80cfe74dccd1491d207cbf824f9dffdf = $(`&lt;div id=&quot;html_80cfe74dccd1491d207cbf824f9dffdf&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;85.0&lt;/div&gt;`)[0];
            popup_d24e2a6956fec8ebee0d0c309c8315d6.setContent(html_80cfe74dccd1491d207cbf824f9dffdf);


        circle_marker_15f432efeb7133cb64cf8594a58ed3d8.bindPopup(popup_d24e2a6956fec8ebee0d0c309c8315d6)
        ;




            var circle_marker_1fde05306f9485f25eca02d2ee40558e = L.circleMarker(
                [40.43919, -3.61766],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3eab210558ace83428114519fd465261 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_730e6cea62111352ba21a4ba855141b3 = $(`&lt;div id=&quot;html_730e6cea62111352ba21a4ba855141b3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;55.0&lt;/div&gt;`)[0];
            popup_3eab210558ace83428114519fd465261.setContent(html_730e6cea62111352ba21a4ba855141b3);


        circle_marker_1fde05306f9485f25eca02d2ee40558e.bindPopup(popup_3eab210558ace83428114519fd465261)
        ;




            var circle_marker_723647281adb7a497b43eb7808e34fcd = L.circleMarker(
                [40.41993, -3.61799],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5b4e5c05373fe60650b9190d80bb8dcd = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6ad376c8c339a1e3edf6e419d8eba986 = $(`&lt;div id=&quot;html_6ad376c8c339a1e3edf6e419d8eba986&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;24.0&lt;/div&gt;`)[0];
            popup_5b4e5c05373fe60650b9190d80bb8dcd.setContent(html_6ad376c8c339a1e3edf6e419d8eba986);


        circle_marker_723647281adb7a497b43eb7808e34fcd.bindPopup(popup_5b4e5c05373fe60650b9190d80bb8dcd)
        ;




            var circle_marker_e1fa428fec44a4294fe1a40e51c92f92 = L.circleMarker(
                [40.44836, -3.56681],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_7acc3904bc49a19459df0b5202916fc8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_67f1731f2b6adf1cc464e1426dc23def = $(`&lt;div id=&quot;html_67f1731f2b6adf1cc464e1426dc23def&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;105.0&lt;/div&gt;`)[0];
            popup_7acc3904bc49a19459df0b5202916fc8.setContent(html_67f1731f2b6adf1cc464e1426dc23def);


        circle_marker_e1fa428fec44a4294fe1a40e51c92f92.bindPopup(popup_7acc3904bc49a19459df0b5202916fc8)
        ;




            var circle_marker_603e2ca2e8cd73a05665ab4c91b32d6e = L.circleMarker(
                [40.44849, -3.56706],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_005b6a5fae0aa91e63d767a22f847ae7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_eed703a7a46869118a167526abd1715c = $(`&lt;div id=&quot;html_eed703a7a46869118a167526abd1715c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;46.199999999999996&lt;/div&gt;`)[0];
            popup_005b6a5fae0aa91e63d767a22f847ae7.setContent(html_eed703a7a46869118a167526abd1715c);


        circle_marker_603e2ca2e8cd73a05665ab4c91b32d6e.bindPopup(popup_005b6a5fae0aa91e63d767a22f847ae7)
        ;




            var circle_marker_038f6ec76576e5528efa4c311d41a28a = L.circleMarker(
                [40.43265, -3.61723],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_98a05185bcece937f8f6ada0abbceb9e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b26e6233762962b06b84b53fe2c99d0d = $(`&lt;div id=&quot;html_b26e6233762962b06b84b53fe2c99d0d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;45.0&lt;/div&gt;`)[0];
            popup_98a05185bcece937f8f6ada0abbceb9e.setContent(html_b26e6233762962b06b84b53fe2c99d0d);


        circle_marker_038f6ec76576e5528efa4c311d41a28a.bindPopup(popup_98a05185bcece937f8f6ada0abbceb9e)
        ;




            var circle_marker_e509ca76f72488cb394c35964d868593 = L.circleMarker(
                [40.44813, -3.56796],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_777a32dd8d72af50b2594837db6ca100 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_fc0dfbb2ea4923b7e8abf76653365c40 = $(`&lt;div id=&quot;html_fc0dfbb2ea4923b7e8abf76653365c40&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;133.0&lt;/div&gt;`)[0];
            popup_777a32dd8d72af50b2594837db6ca100.setContent(html_fc0dfbb2ea4923b7e8abf76653365c40);


        circle_marker_e509ca76f72488cb394c35964d868593.bindPopup(popup_777a32dd8d72af50b2594837db6ca100)
        ;




            var circle_marker_1a923182cb2d9047844de43e72d79f44 = L.circleMarker(
                [40.4412, -3.63173],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_0b13152f812048f322d224bb2f862682 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_c04536eacf92a21f16e564a286b14b2d = $(`&lt;div id=&quot;html_c04536eacf92a21f16e564a286b14b2d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;38.0&lt;/div&gt;`)[0];
            popup_0b13152f812048f322d224bb2f862682.setContent(html_c04536eacf92a21f16e564a286b14b2d);


        circle_marker_1a923182cb2d9047844de43e72d79f44.bindPopup(popup_0b13152f812048f322d224bb2f862682)
        ;




            var circle_marker_e5ce7a26f074a767b7c732c07b29cfc0 = L.circleMarker(
                [40.43629, -3.60937],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_2f7746306b9f267739917c7c28a920f8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_52531cc5d7bb784454025fbdb9b3fbaf = $(`&lt;div id=&quot;html_52531cc5d7bb784454025fbdb9b3fbaf&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;64.0&lt;/div&gt;`)[0];
            popup_2f7746306b9f267739917c7c28a920f8.setContent(html_52531cc5d7bb784454025fbdb9b3fbaf);


        circle_marker_e5ce7a26f074a767b7c732c07b29cfc0.bindPopup(popup_2f7746306b9f267739917c7c28a920f8)
        ;




            var circle_marker_cdd3a7bbb676f600aa8b5ef18c2a7e15 = L.circleMarker(
                [40.44702, -3.57558],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b47266ceeca82e4cf9215394d9023ad7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ef7459e2f03b4834fb93a5a93bb9cf23 = $(`&lt;div id=&quot;html_ef7459e2f03b4834fb93a5a93bb9cf23&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;58.0&lt;/div&gt;`)[0];
            popup_b47266ceeca82e4cf9215394d9023ad7.setContent(html_ef7459e2f03b4834fb93a5a93bb9cf23);


        circle_marker_cdd3a7bbb676f600aa8b5ef18c2a7e15.bindPopup(popup_b47266ceeca82e4cf9215394d9023ad7)
        ;




            var circle_marker_134631c86256279d935311e72a36ef2e = L.circleMarker(
                [40.42981, -3.62567],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_0b8b89999859c325c21051ea013e162c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ffaf702dee7fb91efa074814f7d61b4f = $(`&lt;div id=&quot;html_ffaf702dee7fb91efa074814f7d61b4f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;25.0&lt;/div&gt;`)[0];
            popup_0b8b89999859c325c21051ea013e162c.setContent(html_ffaf702dee7fb91efa074814f7d61b4f);


        circle_marker_134631c86256279d935311e72a36ef2e.bindPopup(popup_0b8b89999859c325c21051ea013e162c)
        ;




            var circle_marker_511f152a169cbe1b2b3ef7a2aa148529 = L.circleMarker(
                [40.42685, -3.62946],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_74a69dd289350007b24dc59e032bae6e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1d9d88a6834c75b6133c5cd285393591 = $(`&lt;div id=&quot;html_1d9d88a6834c75b6133c5cd285393591&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;500.0&lt;/div&gt;`)[0];
            popup_74a69dd289350007b24dc59e032bae6e.setContent(html_1d9d88a6834c75b6133c5cd285393591);


        circle_marker_511f152a169cbe1b2b3ef7a2aa148529.bindPopup(popup_74a69dd289350007b24dc59e032bae6e)
        ;




            var circle_marker_e65b0e1670ffc6b0864e49c1e9f01251 = L.circleMarker(
                [40.43643, -3.6095],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_2a709af3730016164cb2f50486093e66 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a41aed91a4399658ea931f7dc5ed0548 = $(`&lt;div id=&quot;html_a41aed91a4399658ea931f7dc5ed0548&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;25.0&lt;/div&gt;`)[0];
            popup_2a709af3730016164cb2f50486093e66.setContent(html_a41aed91a4399658ea931f7dc5ed0548);


        circle_marker_e65b0e1670ffc6b0864e49c1e9f01251.bindPopup(popup_2a709af3730016164cb2f50486093e66)
        ;




            var circle_marker_38b57311389fe645ac3b295a1cb636f6 = L.circleMarker(
                [40.44439, -3.57794],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5ef63accd4e055e8dabdefd903fc1571 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_55e55125db6fa18415b8d7f77d56360f = $(`&lt;div id=&quot;html_55e55125db6fa18415b8d7f77d56360f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;35.0&lt;/div&gt;`)[0];
            popup_5ef63accd4e055e8dabdefd903fc1571.setContent(html_55e55125db6fa18415b8d7f77d56360f);


        circle_marker_38b57311389fe645ac3b295a1cb636f6.bindPopup(popup_5ef63accd4e055e8dabdefd903fc1571)
        ;




            var circle_marker_d2fe23ef9b0c8d192154ec8df59eb09b = L.circleMarker(
                [40.43731, -3.62305],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_62d0beda8f63aee07ab8bec951231089 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_38e914fb864748c1671b69f7609990e3 = $(`&lt;div id=&quot;html_38e914fb864748c1671b69f7609990e3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;90.0&lt;/div&gt;`)[0];
            popup_62d0beda8f63aee07ab8bec951231089.setContent(html_38e914fb864748c1671b69f7609990e3);


        circle_marker_d2fe23ef9b0c8d192154ec8df59eb09b.bindPopup(popup_62d0beda8f63aee07ab8bec951231089)
        ;




            var circle_marker_382c285e4e70ddf00e5b7506192ed082 = L.circleMarker(
                [40.4491, -3.57707],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ff324cbd3bf371b58a0d1a5794c96c80 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_8ab8bd7a160ba15575d633d21c4d4e18 = $(`&lt;div id=&quot;html_8ab8bd7a160ba15575d633d21c4d4e18&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;60.0&lt;/div&gt;`)[0];
            popup_ff324cbd3bf371b58a0d1a5794c96c80.setContent(html_8ab8bd7a160ba15575d633d21c4d4e18);


        circle_marker_382c285e4e70ddf00e5b7506192ed082.bindPopup(popup_ff324cbd3bf371b58a0d1a5794c96c80)
        ;




            var circle_marker_9cd66d331a44964ed44f646d216b9fd6 = L.circleMarker(
                [40.434, -3.61289],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a6d650a5e52bd9d861e7a76c661fa483 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_bba80b630ec028ac551805dfc8bdb2a1 = $(`&lt;div id=&quot;html_bba80b630ec028ac551805dfc8bdb2a1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;52.0&lt;/div&gt;`)[0];
            popup_a6d650a5e52bd9d861e7a76c661fa483.setContent(html_bba80b630ec028ac551805dfc8bdb2a1);


        circle_marker_9cd66d331a44964ed44f646d216b9fd6.bindPopup(popup_a6d650a5e52bd9d861e7a76c661fa483)
        ;




            var circle_marker_ddce60bcc2eb6262b810651f8aa80fe5 = L.circleMarker(
                [40.44249, -3.57557],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9838d77b6cf9f3ed1d273600923354e5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d049519e86e0fac6e501f88540c0a632 = $(`&lt;div id=&quot;html_d049519e86e0fac6e501f88540c0a632&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;23.0&lt;/div&gt;`)[0];
            popup_9838d77b6cf9f3ed1d273600923354e5.setContent(html_d049519e86e0fac6e501f88540c0a632);


        circle_marker_ddce60bcc2eb6262b810651f8aa80fe5.bindPopup(popup_9838d77b6cf9f3ed1d273600923354e5)
        ;




            var circle_marker_feff7482886c9415c334e35e66da6021 = L.circleMarker(
                [40.44294, -3.63248],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d0a50b8f8c1dca51cdcbef249dd19ba7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7591ee9f146ef905b635dd3366f5d4c7 = $(`&lt;div id=&quot;html_7591ee9f146ef905b635dd3366f5d4c7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;49.0&lt;/div&gt;`)[0];
            popup_d0a50b8f8c1dca51cdcbef249dd19ba7.setContent(html_7591ee9f146ef905b635dd3366f5d4c7);


        circle_marker_feff7482886c9415c334e35e66da6021.bindPopup(popup_d0a50b8f8c1dca51cdcbef249dd19ba7)
        ;




            var circle_marker_df5e2c99da57b5212a4dc1aa69f2c03a = L.circleMarker(
                [40.43723, -3.6112],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8c6dd279f5e005d932c6b8b1e769e8c4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4e6f0675bc152fb40c7188f0e271d754 = $(`&lt;div id=&quot;html_4e6f0675bc152fb40c7188f0e271d754&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;25.0&lt;/div&gt;`)[0];
            popup_8c6dd279f5e005d932c6b8b1e769e8c4.setContent(html_4e6f0675bc152fb40c7188f0e271d754);


        circle_marker_df5e2c99da57b5212a4dc1aa69f2c03a.bindPopup(popup_8c6dd279f5e005d932c6b8b1e769e8c4)
        ;




            var circle_marker_38805559f0ca51c467be1e0f1fb3cde1 = L.circleMarker(
                [40.4318, -3.6154],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c041b2a7242a614f4dea77dc91dd126e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4b1601bfd615ea311e9057f493a9915b = $(`&lt;div id=&quot;html_4b1601bfd615ea311e9057f493a9915b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;24.0&lt;/div&gt;`)[0];
            popup_c041b2a7242a614f4dea77dc91dd126e.setContent(html_4b1601bfd615ea311e9057f493a9915b);


        circle_marker_38805559f0ca51c467be1e0f1fb3cde1.bindPopup(popup_c041b2a7242a614f4dea77dc91dd126e)
        ;




            var circle_marker_110d75f6dad6eeac9d82aa232e4c2dd1 = L.circleMarker(
                [40.43115, -3.61849],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3415db7ff2a70ac4a0ae7bb9fb78eb16 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b1e8826a02b867e707cd4462d4bea0fd = $(`&lt;div id=&quot;html_b1e8826a02b867e707cd4462d4bea0fd&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;104.0&lt;/div&gt;`)[0];
            popup_3415db7ff2a70ac4a0ae7bb9fb78eb16.setContent(html_b1e8826a02b867e707cd4462d4bea0fd);


        circle_marker_110d75f6dad6eeac9d82aa232e4c2dd1.bindPopup(popup_3415db7ff2a70ac4a0ae7bb9fb78eb16)
        ;




            var circle_marker_4beae388492468ac26a43d7cdb3ed392 = L.circleMarker(
                [40.42558, -3.62087],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_0c71b98dbe8ffce81cfa12ebbd89188e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_dac34b8ce07dfc90385162ba4a9f3a83 = $(`&lt;div id=&quot;html_dac34b8ce07dfc90385162ba4a9f3a83&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;35.0&lt;/div&gt;`)[0];
            popup_0c71b98dbe8ffce81cfa12ebbd89188e.setContent(html_dac34b8ce07dfc90385162ba4a9f3a83);


        circle_marker_4beae388492468ac26a43d7cdb3ed392.bindPopup(popup_0c71b98dbe8ffce81cfa12ebbd89188e)
        ;




            var circle_marker_ee5c2567e0f36473136ed0ecbafeb320 = L.circleMarker(
                [40.43955, -3.63394],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_70d117f7ea1de6bcee347846992dcc24 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_34849df1579ae74735b61353027fc496 = $(`&lt;div id=&quot;html_34849df1579ae74735b61353027fc496&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;54.599999999999994&lt;/div&gt;`)[0];
            popup_70d117f7ea1de6bcee347846992dcc24.setContent(html_34849df1579ae74735b61353027fc496);


        circle_marker_ee5c2567e0f36473136ed0ecbafeb320.bindPopup(popup_70d117f7ea1de6bcee347846992dcc24)
        ;




            var circle_marker_0b36d5900907d8c37bc0b3cc4816ccda = L.circleMarker(
                [40.42681, -3.61727],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_1910e1abea9373bb5132346d0b6abdf5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_822d937999957473865cffdaf5b0d859 = $(`&lt;div id=&quot;html_822d937999957473865cffdaf5b0d859&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;52.0&lt;/div&gt;`)[0];
            popup_1910e1abea9373bb5132346d0b6abdf5.setContent(html_822d937999957473865cffdaf5b0d859);


        circle_marker_0b36d5900907d8c37bc0b3cc4816ccda.bindPopup(popup_1910e1abea9373bb5132346d0b6abdf5)
        ;




            var circle_marker_07d213719944af461aa6ee6462c0100d = L.circleMarker(
                [40.44404, -3.56658],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5bb781d24aee283277f598850ca2ddbe = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_cf8eb1fa549723cf89dbb148918a5c6a = $(`&lt;div id=&quot;html_cf8eb1fa549723cf89dbb148918a5c6a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;251.99999999999997&lt;/div&gt;`)[0];
            popup_5bb781d24aee283277f598850ca2ddbe.setContent(html_cf8eb1fa549723cf89dbb148918a5c6a);


        circle_marker_07d213719944af461aa6ee6462c0100d.bindPopup(popup_5bb781d24aee283277f598850ca2ddbe)
        ;




            var circle_marker_1c40fc205483f43b4f75d1108458ceee = L.circleMarker(
                [40.44395, -3.56649],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_94a6951e9f317db2eb9a3f7805ee4914 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e6b9171b106eae16bf2ddbd21b70f597 = $(`&lt;div id=&quot;html_e6b9171b106eae16bf2ddbd21b70f597&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;57.0&lt;/div&gt;`)[0];
            popup_94a6951e9f317db2eb9a3f7805ee4914.setContent(html_e6b9171b106eae16bf2ddbd21b70f597);


        circle_marker_1c40fc205483f43b4f75d1108458ceee.bindPopup(popup_94a6951e9f317db2eb9a3f7805ee4914)
        ;




            var circle_marker_5862c8c4c950244feaeb1710680eece1 = L.circleMarker(
                [40.44625, -3.57381],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a9c3b50b4a895e5afb1e93be06313126 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_327d524f7c11fbb122a23bf40ea2703c = $(`&lt;div id=&quot;html_327d524f7c11fbb122a23bf40ea2703c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_a9c3b50b4a895e5afb1e93be06313126.setContent(html_327d524f7c11fbb122a23bf40ea2703c);


        circle_marker_5862c8c4c950244feaeb1710680eece1.bindPopup(popup_a9c3b50b4a895e5afb1e93be06313126)
        ;




            var circle_marker_493200d725f0170c4556982b8f72984c = L.circleMarker(
                [40.44408, -3.57436],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_03096ced5962f23e92a8b8a578899931 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_41b5da04b33fe8a3774bace00de3a532 = $(`&lt;div id=&quot;html_41b5da04b33fe8a3774bace00de3a532&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_03096ced5962f23e92a8b8a578899931.setContent(html_41b5da04b33fe8a3774bace00de3a532);


        circle_marker_493200d725f0170c4556982b8f72984c.bindPopup(popup_03096ced5962f23e92a8b8a578899931)
        ;




            var circle_marker_74c686f937b771d10053602ecd1ba1e5 = L.circleMarker(
                [40.44586, -3.57696],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e4080b2bd8255cf965615ea5278b5e70 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6d754615d18ecdbdc61c2f6e9034e1d5 = $(`&lt;div id=&quot;html_6d754615d18ecdbdc61c2f6e9034e1d5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;63.0&lt;/div&gt;`)[0];
            popup_e4080b2bd8255cf965615ea5278b5e70.setContent(html_6d754615d18ecdbdc61c2f6e9034e1d5);


        circle_marker_74c686f937b771d10053602ecd1ba1e5.bindPopup(popup_e4080b2bd8255cf965615ea5278b5e70)
        ;




            var circle_marker_0bf415b040bd12200e5aa4944ebfd6e3 = L.circleMarker(
                [40.44442, -3.60887],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_64b4178c6e65796a984b2392eca6ab05 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b9dc064e7d0c9a8ca6bb6ca66ac52fb5 = $(`&lt;div id=&quot;html_b9dc064e7d0c9a8ca6bb6ca66ac52fb5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;53.0&lt;/div&gt;`)[0];
            popup_64b4178c6e65796a984b2392eca6ab05.setContent(html_b9dc064e7d0c9a8ca6bb6ca66ac52fb5);


        circle_marker_0bf415b040bd12200e5aa4944ebfd6e3.bindPopup(popup_64b4178c6e65796a984b2392eca6ab05)
        ;




            var circle_marker_8a61374a9f8fa5f94183a4982e017855 = L.circleMarker(
                [40.42306, -3.61692],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_bb1e31a39f21c61975924f5d4bc5ecad = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b561800b09c8b1a3f64d00420c66c7d0 = $(`&lt;div id=&quot;html_b561800b09c8b1a3f64d00420c66c7d0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;105.0&lt;/div&gt;`)[0];
            popup_bb1e31a39f21c61975924f5d4bc5ecad.setContent(html_b561800b09c8b1a3f64d00420c66c7d0);


        circle_marker_8a61374a9f8fa5f94183a4982e017855.bindPopup(popup_bb1e31a39f21c61975924f5d4bc5ecad)
        ;




            var circle_marker_cb740707abe625993b07f9e98e39865a = L.circleMarker(
                [40.42666, -3.62949],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_a2f357e5dbd9f3421a8ca8eb70441610 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9447d36b644a67f28dd8c1211511731b = $(`&lt;div id=&quot;html_9447d36b644a67f28dd8c1211511731b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;105.0&lt;/div&gt;`)[0];
            popup_a2f357e5dbd9f3421a8ca8eb70441610.setContent(html_9447d36b644a67f28dd8c1211511731b);


        circle_marker_cb740707abe625993b07f9e98e39865a.bindPopup(popup_a2f357e5dbd9f3421a8ca8eb70441610)
        ;




            var circle_marker_67bc9f102efed5b321d62979d8ba6edd = L.circleMarker(
                [40.44355, -3.63643],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_19b2b633d0bc929a2a91bc9c47a378f8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_cf28360dfb0295edab5c7d21be978634 = $(`&lt;div id=&quot;html_cf28360dfb0295edab5c7d21be978634&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.0&lt;/div&gt;`)[0];
            popup_19b2b633d0bc929a2a91bc9c47a378f8.setContent(html_cf28360dfb0295edab5c7d21be978634);


        circle_marker_67bc9f102efed5b321d62979d8ba6edd.bindPopup(popup_19b2b633d0bc929a2a91bc9c47a378f8)
        ;




            var circle_marker_d938ceba603fbbefea41cacfb712be9b = L.circleMarker(
                [40.43058, -3.62372],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e4ed596e2eb064a870f46c09047a370b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_4c80d7f242459c1f9f8da5f82288911f = $(`&lt;div id=&quot;html_4c80d7f242459c1f9f8da5f82288911f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;390.0&lt;/div&gt;`)[0];
            popup_e4ed596e2eb064a870f46c09047a370b.setContent(html_4c80d7f242459c1f9f8da5f82288911f);


        circle_marker_d938ceba603fbbefea41cacfb712be9b.bindPopup(popup_e4ed596e2eb064a870f46c09047a370b)
        ;




            var circle_marker_12fe970d88f1360576b4a54e0692827b = L.circleMarker(
                [40.43583, -3.6348],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_54ae0dd4d740a2a47e33179c334bb3cb = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_887a43f084a8a7eac364c2ec68c01453 = $(`&lt;div id=&quot;html_887a43f084a8a7eac364c2ec68c01453&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;72.0&lt;/div&gt;`)[0];
            popup_54ae0dd4d740a2a47e33179c334bb3cb.setContent(html_887a43f084a8a7eac364c2ec68c01453);


        circle_marker_12fe970d88f1360576b4a54e0692827b.bindPopup(popup_54ae0dd4d740a2a47e33179c334bb3cb)
        ;




            var circle_marker_7ba0606eb679a53a25c134d8e769aacc = L.circleMarker(
                [40.44681, -3.61425],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_068bf2b9c0657095f4d0cc69b265e04b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_fc1471815a57175ecbb90fe1d0c3cc18 = $(`&lt;div id=&quot;html_fc1471815a57175ecbb90fe1d0c3cc18&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;49.0&lt;/div&gt;`)[0];
            popup_068bf2b9c0657095f4d0cc69b265e04b.setContent(html_fc1471815a57175ecbb90fe1d0c3cc18);


        circle_marker_7ba0606eb679a53a25c134d8e769aacc.bindPopup(popup_068bf2b9c0657095f4d0cc69b265e04b)
        ;




            var circle_marker_7e97cd444f1f87c4cbd1f55b590c5db4 = L.circleMarker(
                [40.44402, -3.61643],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f42b164d004f41149787690018897307 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_16aedf2dc62405e91740dfe63b4b37f2 = $(`&lt;div id=&quot;html_16aedf2dc62405e91740dfe63b4b37f2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;73.0&lt;/div&gt;`)[0];
            popup_f42b164d004f41149787690018897307.setContent(html_16aedf2dc62405e91740dfe63b4b37f2);


        circle_marker_7e97cd444f1f87c4cbd1f55b590c5db4.bindPopup(popup_f42b164d004f41149787690018897307)
        ;




            var circle_marker_c4bb940bd18cbaaefccebc7e441af52d = L.circleMarker(
                [40.43492, -3.6233],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_6fa8985558c4453c6d8528c12d30b274 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_7848ec53bccc496129126920196baed3 = $(`&lt;div id=&quot;html_7848ec53bccc496129126920196baed3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;65.0&lt;/div&gt;`)[0];
            popup_6fa8985558c4453c6d8528c12d30b274.setContent(html_7848ec53bccc496129126920196baed3);


        circle_marker_c4bb940bd18cbaaefccebc7e441af52d.bindPopup(popup_6fa8985558c4453c6d8528c12d30b274)
        ;




            var circle_marker_8bd102c0ab3562c5e8a4f2288e741d5e = L.circleMarker(
                [40.42952, -3.62531],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ed3027127b487cfa72add2509e11f2de = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_205e803bc239f394adc315fa55c74f0c = $(`&lt;div id=&quot;html_205e803bc239f394adc315fa55c74f0c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;102.0&lt;/div&gt;`)[0];
            popup_ed3027127b487cfa72add2509e11f2de.setContent(html_205e803bc239f394adc315fa55c74f0c);


        circle_marker_8bd102c0ab3562c5e8a4f2288e741d5e.bindPopup(popup_ed3027127b487cfa72add2509e11f2de)
        ;




            var circle_marker_c2a6babd2457dfd7c5e00a809d07256d = L.circleMarker(
                [40.44653, -3.60689],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_c9c23ff632d48ff04743bf5eb5baeb72 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b240e470eac55eb799b09228269515e3 = $(`&lt;div id=&quot;html_b240e470eac55eb799b09228269515e3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;50.0&lt;/div&gt;`)[0];
            popup_c9c23ff632d48ff04743bf5eb5baeb72.setContent(html_b240e470eac55eb799b09228269515e3);


        circle_marker_c2a6babd2457dfd7c5e00a809d07256d.bindPopup(popup_c9c23ff632d48ff04743bf5eb5baeb72)
        ;




            var circle_marker_83696f937a390382ea10df6a269724b9 = L.circleMarker(
                [40.44661, -3.61599],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_31e386eb40892b65fff5a1ba25180595 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e94c1d321c02764a91f6f7a45441b515 = $(`&lt;div id=&quot;html_e94c1d321c02764a91f6f7a45441b515&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;133.0&lt;/div&gt;`)[0];
            popup_31e386eb40892b65fff5a1ba25180595.setContent(html_e94c1d321c02764a91f6f7a45441b515);


        circle_marker_83696f937a390382ea10df6a269724b9.bindPopup(popup_31e386eb40892b65fff5a1ba25180595)
        ;




            var circle_marker_1b56a8acb1dcb11a48dbb9f7a0db9912 = L.circleMarker(
                [40.44675, -3.61502],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_97a47c11084aef9efcc2bf75df66b2b1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_be632eebdc4b905ed5dc78d08909dabe = $(`&lt;div id=&quot;html_be632eebdc4b905ed5dc78d08909dabe&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;103.6&lt;/div&gt;`)[0];
            popup_97a47c11084aef9efcc2bf75df66b2b1.setContent(html_be632eebdc4b905ed5dc78d08909dabe);


        circle_marker_1b56a8acb1dcb11a48dbb9f7a0db9912.bindPopup(popup_97a47c11084aef9efcc2bf75df66b2b1)
        ;




            var circle_marker_2ed7e4ee9651a321bda945adb34657d0 = L.circleMarker(
                [40.44659, -3.61437],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_91cc7b80cf727fa97cef1864ce4d2b2d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9ec6401b148bf3b0ec2753a19469356f = $(`&lt;div id=&quot;html_9ec6401b148bf3b0ec2753a19469356f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;75.0&lt;/div&gt;`)[0];
            popup_91cc7b80cf727fa97cef1864ce4d2b2d.setContent(html_9ec6401b148bf3b0ec2753a19469356f);


        circle_marker_2ed7e4ee9651a321bda945adb34657d0.bindPopup(popup_91cc7b80cf727fa97cef1864ce4d2b2d)
        ;




            var circle_marker_bd7eaef0613e556e84ccbd750af0efc5 = L.circleMarker(
                [40.43697, -3.62398],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_cacd53c6206e7a399d13466228099f08 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_c7a167c5fe1303a423cc12948627dad5 = $(`&lt;div id=&quot;html_c7a167c5fe1303a423cc12948627dad5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;42.0&lt;/div&gt;`)[0];
            popup_cacd53c6206e7a399d13466228099f08.setContent(html_c7a167c5fe1303a423cc12948627dad5);


        circle_marker_bd7eaef0613e556e84ccbd750af0efc5.bindPopup(popup_cacd53c6206e7a399d13466228099f08)
        ;




            var circle_marker_88750439a19b4a0c8eaf653dcd5e76cc = L.circleMarker(
                [40.41683, -3.61825],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_7d5a006427e1f823fbe8f4e712a0fc61 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_07909b54ac89ce71eec2465730df1e33 = $(`&lt;div id=&quot;html_07909b54ac89ce71eec2465730df1e33&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;26.0&lt;/div&gt;`)[0];
            popup_7d5a006427e1f823fbe8f4e712a0fc61.setContent(html_07909b54ac89ce71eec2465730df1e33);


        circle_marker_88750439a19b4a0c8eaf653dcd5e76cc.bindPopup(popup_7d5a006427e1f823fbe8f4e712a0fc61)
        ;




            var circle_marker_a24f62f71aae2c38287daab30566e111 = L.circleMarker(
                [40.44156, -3.63253],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_7d5575df330aff9e0adebc4c08e449bc = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_abb2ed2d317f26b89544cabde2a8c2c7 = $(`&lt;div id=&quot;html_abb2ed2d317f26b89544cabde2a8c2c7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;37.0&lt;/div&gt;`)[0];
            popup_7d5575df330aff9e0adebc4c08e449bc.setContent(html_abb2ed2d317f26b89544cabde2a8c2c7);


        circle_marker_a24f62f71aae2c38287daab30566e111.bindPopup(popup_7d5575df330aff9e0adebc4c08e449bc)
        ;




            var circle_marker_54391b042833836b131453f3e79f77fe = L.circleMarker(
                [40.44761, -3.64223],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_62a017f6881bff43e256f3612119bd27 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_986e440f9c1540c362255bd98b4d721c = $(`&lt;div id=&quot;html_986e440f9c1540c362255bd98b4d721c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;28.0&lt;/div&gt;`)[0];
            popup_62a017f6881bff43e256f3612119bd27.setContent(html_986e440f9c1540c362255bd98b4d721c);


        circle_marker_54391b042833836b131453f3e79f77fe.bindPopup(popup_62a017f6881bff43e256f3612119bd27)
        ;




            var circle_marker_705e08542b2f0ec5991234d6e7317889 = L.circleMarker(
                [40.44159, -3.63069],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f26d33fde55a862d6d4a9aee116a670a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_fd2fa006b239fc84889ba3331e3061d7 = $(`&lt;div id=&quot;html_fd2fa006b239fc84889ba3331e3061d7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;53.0&lt;/div&gt;`)[0];
            popup_f26d33fde55a862d6d4a9aee116a670a.setContent(html_fd2fa006b239fc84889ba3331e3061d7);


        circle_marker_705e08542b2f0ec5991234d6e7317889.bindPopup(popup_f26d33fde55a862d6d4a9aee116a670a)
        ;




            var circle_marker_c28b9e04549348889393b4a23119889c = L.circleMarker(
                [40.43753, -3.61127],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_3965939a89c1f52afed0ec68e4c84542 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_e072f817c0c90d9fdb5b1e72c4bafda8 = $(`&lt;div id=&quot;html_e072f817c0c90d9fdb5b1e72c4bafda8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.0&lt;/div&gt;`)[0];
            popup_3965939a89c1f52afed0ec68e4c84542.setContent(html_e072f817c0c90d9fdb5b1e72c4bafda8);


        circle_marker_c28b9e04549348889393b4a23119889c.bindPopup(popup_3965939a89c1f52afed0ec68e4c84542)
        ;




            var circle_marker_44ff8677b801edb2fd0226134747d5ab = L.circleMarker(
                [40.42371, -3.62334],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_20f747326d3786d7bd8eadf5e9587cf7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_17e5a419ea5528616e987f0fbc11fdfa = $(`&lt;div id=&quot;html_17e5a419ea5528616e987f0fbc11fdfa&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;39.0&lt;/div&gt;`)[0];
            popup_20f747326d3786d7bd8eadf5e9587cf7.setContent(html_17e5a419ea5528616e987f0fbc11fdfa);


        circle_marker_44ff8677b801edb2fd0226134747d5ab.bindPopup(popup_20f747326d3786d7bd8eadf5e9587cf7)
        ;




            var circle_marker_ae03c797da17bfa999ef25e560dbdab8 = L.circleMarker(
                [40.43922, -3.62195],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_0946f2989cdfe0808e5d2f5a8b1c24cb = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d10a61c709987f011c1a87626d605f96 = $(`&lt;div id=&quot;html_d10a61c709987f011c1a87626d605f96&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;63.0&lt;/div&gt;`)[0];
            popup_0946f2989cdfe0808e5d2f5a8b1c24cb.setContent(html_d10a61c709987f011c1a87626d605f96);


        circle_marker_ae03c797da17bfa999ef25e560dbdab8.bindPopup(popup_0946f2989cdfe0808e5d2f5a8b1c24cb)
        ;




            var circle_marker_c363ea9afa50529255ef7470a1f36379 = L.circleMarker(
                [40.42592, -3.62118],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_fd061ffaffcdd38c6873036365efae8e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2575192471ec837519862ea1356a0c8f = $(`&lt;div id=&quot;html_2575192471ec837519862ea1356a0c8f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;102.0&lt;/div&gt;`)[0];
            popup_fd061ffaffcdd38c6873036365efae8e.setContent(html_2575192471ec837519862ea1356a0c8f);


        circle_marker_c363ea9afa50529255ef7470a1f36379.bindPopup(popup_fd061ffaffcdd38c6873036365efae8e)
        ;




            var circle_marker_ce1a9d21b2585df910cf3a2590d81f80 = L.circleMarker(
                [40.42499, -3.62308],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_4d5857b9009b6f9e33042c7e07fb539f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6fbae1659334be6bfa5f33804e4945f1 = $(`&lt;div id=&quot;html_6fbae1659334be6bfa5f33804e4945f1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;20.0&lt;/div&gt;`)[0];
            popup_4d5857b9009b6f9e33042c7e07fb539f.setContent(html_6fbae1659334be6bfa5f33804e4945f1);


        circle_marker_ce1a9d21b2585df910cf3a2590d81f80.bindPopup(popup_4d5857b9009b6f9e33042c7e07fb539f)
        ;




            var circle_marker_289366c760b691ef84cce15629c3435e = L.circleMarker(
                [40.42303, -3.61124],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_21b6760dfd6aa5db12702a44331d11f2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a9e60332f4cb90a0291907bdce414de7 = $(`&lt;div id=&quot;html_a9e60332f4cb90a0291907bdce414de7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;105.0&lt;/div&gt;`)[0];
            popup_21b6760dfd6aa5db12702a44331d11f2.setContent(html_a9e60332f4cb90a0291907bdce414de7);


        circle_marker_289366c760b691ef84cce15629c3435e.bindPopup(popup_21b6760dfd6aa5db12702a44331d11f2)
        ;




            var circle_marker_3a27561ccf676240497160baf665d4bc = L.circleMarker(
                [40.446, -3.56585],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_95355f53fd0179e4c74f24d6597db4ff = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9cff7f0d1a72d6621a64e7c12aa3c8b4 = $(`&lt;div id=&quot;html_9cff7f0d1a72d6621a64e7c12aa3c8b4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;98.69999999999999&lt;/div&gt;`)[0];
            popup_95355f53fd0179e4c74f24d6597db4ff.setContent(html_9cff7f0d1a72d6621a64e7c12aa3c8b4);


        circle_marker_3a27561ccf676240497160baf665d4bc.bindPopup(popup_95355f53fd0179e4c74f24d6597db4ff)
        ;




            var circle_marker_cf4ac2282c5c97f45da81b753f693b15 = L.circleMarker(
                [40.43934, -3.63085],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_9e18f620804dcb8f58829d2b18e0b882 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9a367100654fc9f110cd773830602328 = $(`&lt;div id=&quot;html_9a367100654fc9f110cd773830602328&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.0&lt;/div&gt;`)[0];
            popup_9e18f620804dcb8f58829d2b18e0b882.setContent(html_9a367100654fc9f110cd773830602328);


        circle_marker_cf4ac2282c5c97f45da81b753f693b15.bindPopup(popup_9e18f620804dcb8f58829d2b18e0b882)
        ;




            var circle_marker_dbc7c51a88d2041e5a7ffe56f2b25c66 = L.circleMarker(
                [40.43514, -3.61917],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5bcf11c276dbe359a3b0494a8ccae57b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_5fd5d374f5592f09706d56922f508786 = $(`&lt;div id=&quot;html_5fd5d374f5592f09706d56922f508786&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;86.0&lt;/div&gt;`)[0];
            popup_5bcf11c276dbe359a3b0494a8ccae57b.setContent(html_5fd5d374f5592f09706d56922f508786);


        circle_marker_dbc7c51a88d2041e5a7ffe56f2b25c66.bindPopup(popup_5bcf11c276dbe359a3b0494a8ccae57b)
        ;




            var circle_marker_1aa083152430eeec866cd9bc43756900 = L.circleMarker(
                [40.43316, -3.61962],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_8e1f8ff9f5b4bf48a6189cd81b319292 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1fe1a6f682bd130c450e2845b6c82e92 = $(`&lt;div id=&quot;html_1fe1a6f682bd130c450e2845b6c82e92&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;63.0&lt;/div&gt;`)[0];
            popup_8e1f8ff9f5b4bf48a6189cd81b319292.setContent(html_1fe1a6f682bd130c450e2845b6c82e92);


        circle_marker_1aa083152430eeec866cd9bc43756900.bindPopup(popup_8e1f8ff9f5b4bf48a6189cd81b319292)
        ;




            var circle_marker_82ec094d7dbc129fd0c3a577b8beb1b1 = L.circleMarker(
                [40.4443, -3.56595],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_932b053f5e7f6ab51c3ff5bbc859d336 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ee3f375e0607a79ae875db3f5ac4c461 = $(`&lt;div id=&quot;html_ee3f375e0607a79ae875db3f5ac4c461&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;46.0&lt;/div&gt;`)[0];
            popup_932b053f5e7f6ab51c3ff5bbc859d336.setContent(html_ee3f375e0607a79ae875db3f5ac4c461);


        circle_marker_82ec094d7dbc129fd0c3a577b8beb1b1.bindPopup(popup_932b053f5e7f6ab51c3ff5bbc859d336)
        ;




            var circle_marker_18432cf8e6ef3acbd2c290af69d8b509 = L.circleMarker(
                [40.44611, -3.56659],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5f459d9891d6c3db466499cbe9afe1ad = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_68fa1c107265344f98162677b745d4ac = $(`&lt;div id=&quot;html_68fa1c107265344f98162677b745d4ac&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;33.0&lt;/div&gt;`)[0];
            popup_5f459d9891d6c3db466499cbe9afe1ad.setContent(html_68fa1c107265344f98162677b745d4ac);


        circle_marker_18432cf8e6ef3acbd2c290af69d8b509.bindPopup(popup_5f459d9891d6c3db466499cbe9afe1ad)
        ;




            var circle_marker_2d3225d4e2cc89e7f0bb120435e4f5c5 = L.circleMarker(
                [40.42811, -3.6274],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d5a5f3702e84bcf218266696fb6e1361 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_c32ce4973a5388cd4d7c563d6b917723 = $(`&lt;div id=&quot;html_c32ce4973a5388cd4d7c563d6b917723&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;20.0&lt;/div&gt;`)[0];
            popup_d5a5f3702e84bcf218266696fb6e1361.setContent(html_c32ce4973a5388cd4d7c563d6b917723);


        circle_marker_2d3225d4e2cc89e7f0bb120435e4f5c5.bindPopup(popup_d5a5f3702e84bcf218266696fb6e1361)
        ;




            var circle_marker_8a763b64ab6a7f2b779e374afe7fe1f5 = L.circleMarker(
                [40.43299, -3.62069],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5f29bb118a668f5b2957fcc9d0874b1b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_ba42835e4a8478a1a37097b0906d2d34 = $(`&lt;div id=&quot;html_ba42835e4a8478a1a37097b0906d2d34&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;154.0&lt;/div&gt;`)[0];
            popup_5f29bb118a668f5b2957fcc9d0874b1b.setContent(html_ba42835e4a8478a1a37097b0906d2d34);


        circle_marker_8a763b64ab6a7f2b779e374afe7fe1f5.bindPopup(popup_5f29bb118a668f5b2957fcc9d0874b1b)
        ;




            var circle_marker_5ff9883ee2450c64ce0a5f785d5f7600 = L.circleMarker(
                [40.44098, -3.57049],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;blue&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_622197133db4b7e2412e6feb3e9a2d37 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_cd7bfd3010a9d10313bcfef1ec1e76d1 = $(`&lt;div id=&quot;html_cd7bfd3010a9d10313bcfef1ec1e76d1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;160.0&lt;/div&gt;`)[0];
            popup_622197133db4b7e2412e6feb3e9a2d37.setContent(html_cd7bfd3010a9d10313bcfef1ec1e76d1);


        circle_marker_5ff9883ee2450c64ce0a5f785d5f7600.bindPopup(popup_622197133db4b7e2412e6feb3e9a2d37)
        ;




            var circle_marker_c03416a425d306cabf14be1e66081572 = L.circleMarker(
                [40.44612, -3.58057],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_e74817bd9587ee8cd9fc0d02f2684c84 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0c5fa863ab20a0c13c10e26861c7f42a = $(`&lt;div id=&quot;html_0c5fa863ab20a0c13c10e26861c7f42a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;57.0&lt;/div&gt;`)[0];
            popup_e74817bd9587ee8cd9fc0d02f2684c84.setContent(html_0c5fa863ab20a0c13c10e26861c7f42a);


        circle_marker_c03416a425d306cabf14be1e66081572.bindPopup(popup_e74817bd9587ee8cd9fc0d02f2684c84)
        ;




            var circle_marker_ef216c8243dd7466dfd1a860e17a1617 = L.circleMarker(
                [40.42359, -3.61705],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_85d84c0ab50f20e86befd921811627cf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6b52f40f72df759290746438da78cf9f = $(`&lt;div id=&quot;html_6b52f40f72df759290746438da78cf9f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.0&lt;/div&gt;`)[0];
            popup_85d84c0ab50f20e86befd921811627cf.setContent(html_6b52f40f72df759290746438da78cf9f);


        circle_marker_ef216c8243dd7466dfd1a860e17a1617.bindPopup(popup_85d84c0ab50f20e86befd921811627cf)
        ;




            var circle_marker_fd82dd81faab9f9a6aab5f1fdfcf8411 = L.circleMarker(
                [40.43977, -3.62476],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_55ca7adf50101543c4126143f4eb9f31 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_fc10687ffaecda822722c933c01783f0 = $(`&lt;div id=&quot;html_fc10687ffaecda822722c933c01783f0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;51.0&lt;/div&gt;`)[0];
            popup_55ca7adf50101543c4126143f4eb9f31.setContent(html_fc10687ffaecda822722c933c01783f0);


        circle_marker_fd82dd81faab9f9a6aab5f1fdfcf8411.bindPopup(popup_55ca7adf50101543c4126143f4eb9f31)
        ;




            var circle_marker_febe206db568a9ebfff376a164cf9315 = L.circleMarker(
                [40.43082, -3.61166],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_39e23934de37082931647bdea55e9544 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_47690ac17b8301c53e4da98aadfdb4b9 = $(`&lt;div id=&quot;html_47690ac17b8301c53e4da98aadfdb4b9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.0&lt;/div&gt;`)[0];
            popup_39e23934de37082931647bdea55e9544.setContent(html_47690ac17b8301c53e4da98aadfdb4b9);


        circle_marker_febe206db568a9ebfff376a164cf9315.bindPopup(popup_39e23934de37082931647bdea55e9544)
        ;




            var circle_marker_e6474e07b9f14736bbc2625a70ebf4ef = L.circleMarker(
                [40.43246, -3.61765],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_fe9cf1b0c2411b034af4424aa85cb4e0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_465fb9f7ee195be87f1ed956e13bc762 = $(`&lt;div id=&quot;html_465fb9f7ee195be87f1ed956e13bc762&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;45.0&lt;/div&gt;`)[0];
            popup_fe9cf1b0c2411b034af4424aa85cb4e0.setContent(html_465fb9f7ee195be87f1ed956e13bc762);


        circle_marker_e6474e07b9f14736bbc2625a70ebf4ef.bindPopup(popup_fe9cf1b0c2411b034af4424aa85cb4e0)
        ;




            var circle_marker_0504ad3be20bf8b8f22cb8ae14c31c28 = L.circleMarker(
                [40.43576, -3.61633],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d9bd02369c444afd40dd93a2426bc911 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1711c3dd7576a03072bf0efb2f9fc7f4 = $(`&lt;div id=&quot;html_1711c3dd7576a03072bf0efb2f9fc7f4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;21.0&lt;/div&gt;`)[0];
            popup_d9bd02369c444afd40dd93a2426bc911.setContent(html_1711c3dd7576a03072bf0efb2f9fc7f4);


        circle_marker_0504ad3be20bf8b8f22cb8ae14c31c28.bindPopup(popup_d9bd02369c444afd40dd93a2426bc911)
        ;




            var circle_marker_e422004abb2e0c66bbe070f36cd579da = L.circleMarker(
                [40.42341, -3.60125],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_984e81bed53dd18b41cd27d60443aaa5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_9d6284b09d58596f0273c3df4d88e15f = $(`&lt;div id=&quot;html_9d6284b09d58596f0273c3df4d88e15f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;29.0&lt;/div&gt;`)[0];
            popup_984e81bed53dd18b41cd27d60443aaa5.setContent(html_9d6284b09d58596f0273c3df4d88e15f);


        circle_marker_e422004abb2e0c66bbe070f36cd579da.bindPopup(popup_984e81bed53dd18b41cd27d60443aaa5)
        ;




            var circle_marker_63f5ec8dc379d7f2ca7551ff6713261d = L.circleMarker(
                [40.42642, -3.62488],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_dc1adbc98ca235855559f6f92b2d5ec8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a451c71b9dd16eb2628eeff7bec5ee0f = $(`&lt;div id=&quot;html_a451c71b9dd16eb2628eeff7bec5ee0f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;35.0&lt;/div&gt;`)[0];
            popup_dc1adbc98ca235855559f6f92b2d5ec8.setContent(html_a451c71b9dd16eb2628eeff7bec5ee0f);


        circle_marker_63f5ec8dc379d7f2ca7551ff6713261d.bindPopup(popup_dc1adbc98ca235855559f6f92b2d5ec8)
        ;




            var circle_marker_2d9b38002a8a01248dacf5f685613eb1 = L.circleMarker(
                [40.4398, -3.6335],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_866d000d0d9fbbcdf6951086c071aa89 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_389aa7ef467d73989a76d6262f4a283e = $(`&lt;div id=&quot;html_389aa7ef467d73989a76d6262f4a283e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;78.0&lt;/div&gt;`)[0];
            popup_866d000d0d9fbbcdf6951086c071aa89.setContent(html_389aa7ef467d73989a76d6262f4a283e);


        circle_marker_2d9b38002a8a01248dacf5f685613eb1.bindPopup(popup_866d000d0d9fbbcdf6951086c071aa89)
        ;




            var circle_marker_c65c8240cd063584a68be7bea7c76398 = L.circleMarker(
                [40.4274, -3.62239],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_b3db24b8590020f4d1716738f4f8c430 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_98dfbadef5fee0b52af53cdbd58a091a = $(`&lt;div id=&quot;html_98dfbadef5fee0b52af53cdbd58a091a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;40.0&lt;/div&gt;`)[0];
            popup_b3db24b8590020f4d1716738f4f8c430.setContent(html_98dfbadef5fee0b52af53cdbd58a091a);


        circle_marker_c65c8240cd063584a68be7bea7c76398.bindPopup(popup_b3db24b8590020f4d1716738f4f8c430)
        ;




            var circle_marker_2c454c2b4cf636a1d4ea40e357cdc82f = L.circleMarker(
                [40.43074, -3.61735],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_914192047b0ed8738062bdd4c058ebdf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_b0911c0f7b040eaf0dd345eee96ee0f1 = $(`&lt;div id=&quot;html_b0911c0f7b040eaf0dd345eee96ee0f1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;35.0&lt;/div&gt;`)[0];
            popup_914192047b0ed8738062bdd4c058ebdf.setContent(html_b0911c0f7b040eaf0dd345eee96ee0f1);


        circle_marker_2c454c2b4cf636a1d4ea40e357cdc82f.bindPopup(popup_914192047b0ed8738062bdd4c058ebdf)
        ;




            var circle_marker_15d6005ebbec39e6bacf048d256b2dde = L.circleMarker(
                [40.43354, -3.6239],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_d9e57dac929cf62bd9cd06ef7ffc27df = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_c5975358fa43442b3ec42998e519cb21 = $(`&lt;div id=&quot;html_c5975358fa43442b3ec42998e519cb21&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;20.0&lt;/div&gt;`)[0];
            popup_d9e57dac929cf62bd9cd06ef7ffc27df.setContent(html_c5975358fa43442b3ec42998e519cb21);


        circle_marker_15d6005ebbec39e6bacf048d256b2dde.bindPopup(popup_d9e57dac929cf62bd9cd06ef7ffc27df)
        ;




            var circle_marker_a225c23930c7dfc40afb8d92e97fb3d4 = L.circleMarker(
                [40.44396, -3.58344],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_22af21d30ca1f75cbf5e845eff986574 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_af27b98b9f3722302adf1c6f1e627091 = $(`&lt;div id=&quot;html_af27b98b9f3722302adf1c6f1e627091&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;65.0&lt;/div&gt;`)[0];
            popup_22af21d30ca1f75cbf5e845eff986574.setContent(html_af27b98b9f3722302adf1c6f1e627091);


        circle_marker_a225c23930c7dfc40afb8d92e97fb3d4.bindPopup(popup_22af21d30ca1f75cbf5e845eff986574)
        ;




            var circle_marker_ad0ba232002664860657eff78f970495 = L.circleMarker(
                [40.4444, -3.61712],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_38705e99218d971f5276ab2478031963 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1f4127e868388d3132f7771d967653b3 = $(`&lt;div id=&quot;html_1f4127e868388d3132f7771d967653b3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.0&lt;/div&gt;`)[0];
            popup_38705e99218d971f5276ab2478031963.setContent(html_1f4127e868388d3132f7771d967653b3);


        circle_marker_ad0ba232002664860657eff78f970495.bindPopup(popup_38705e99218d971f5276ab2478031963)
        ;




            var circle_marker_1f9b2c80ded79e13971c48199bc6e41e = L.circleMarker(
                [40.44496, -3.58471],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_1dd928c8cba606bdbe899bd42c0d59b8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_a9d3176c4630f093bb3b889c52d6aa9c = $(`&lt;div id=&quot;html_a9d3176c4630f093bb3b889c52d6aa9c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;60.0&lt;/div&gt;`)[0];
            popup_1dd928c8cba606bdbe899bd42c0d59b8.setContent(html_a9d3176c4630f093bb3b889c52d6aa9c);


        circle_marker_1f9b2c80ded79e13971c48199bc6e41e.bindPopup(popup_1dd928c8cba606bdbe899bd42c0d59b8)
        ;




            var circle_marker_845a9974e5ed445679a9115a5e9eb81e = L.circleMarker(
                [40.44608, -3.59755],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;orange&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;orange&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_ec19526f30f95e72af2a152f780d58d0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_2321c2d2ff55453aa44837c054198c6d = $(`&lt;div id=&quot;html_2321c2d2ff55453aa44837c054198c6d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;69.0&lt;/div&gt;`)[0];
            popup_ec19526f30f95e72af2a152f780d58d0.setContent(html_2321c2d2ff55453aa44837c054198c6d);


        circle_marker_845a9974e5ed445679a9115a5e9eb81e.bindPopup(popup_ec19526f30f95e72af2a152f780d58d0)
        ;




            var circle_marker_8f46a107fc6ac6ef1fa785497668b132 = L.circleMarker(
                [40.42951603256381, -3.6269474581492234],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_798b94dbbc7f8c52e67235572953cf21 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_30b8b87f8b8802e1c6234db2f6cd62af = $(`&lt;div id=&quot;html_30b8b87f8b8802e1c6234db2f6cd62af&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;20.0&lt;/div&gt;`)[0];
            popup_798b94dbbc7f8c52e67235572953cf21.setContent(html_30b8b87f8b8802e1c6234db2f6cd62af);


        circle_marker_8f46a107fc6ac6ef1fa785497668b132.bindPopup(popup_798b94dbbc7f8c52e67235572953cf21)
        ;




            var circle_marker_93677de1a7cdd6e2881ca0652b548981 = L.circleMarker(
                [40.43688590023851, -3.6085659417302174],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_1cc3800d55fbb04d0cf096ed7c8d18d8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_d65f432c12676ded3c60ac0975cc89ac = $(`&lt;div id=&quot;html_d65f432c12676ded3c60ac0975cc89ac&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;32.0&lt;/div&gt;`)[0];
            popup_1cc3800d55fbb04d0cf096ed7c8d18d8.setContent(html_d65f432c12676ded3c60ac0975cc89ac);


        circle_marker_93677de1a7cdd6e2881ca0652b548981.bindPopup(popup_1cc3800d55fbb04d0cf096ed7c8d18d8)
        ;




            var circle_marker_c5e8e8fcc48b706d7477bb530fd49397 = L.circleMarker(
                [40.43486658745417, -3.6332088003836223],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_f17acb3459d5ed4631b40f38508be5a3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_0d7389ce88e8ebcc5ecc02da667e6045 = $(`&lt;div id=&quot;html_0d7389ce88e8ebcc5ecc02da667e6045&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;45.0&lt;/div&gt;`)[0];
            popup_f17acb3459d5ed4631b40f38508be5a3.setContent(html_0d7389ce88e8ebcc5ecc02da667e6045);


        circle_marker_c5e8e8fcc48b706d7477bb530fd49397.bindPopup(popup_f17acb3459d5ed4631b40f38508be5a3)
        ;




            var circle_marker_65595d37ec459e689cbc67fb1e908621 = L.circleMarker(
                [40.43689945496136, -3.611809718339415],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_5e0ae96f95af121345ba2badb594ff3f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_3d0cbeb7d3cdabd62748dc5de3a8eaf4 = $(`&lt;div id=&quot;html_3d0cbeb7d3cdabd62748dc5de3a8eaf4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;29.0&lt;/div&gt;`)[0];
            popup_5e0ae96f95af121345ba2badb594ff3f.setContent(html_3d0cbeb7d3cdabd62748dc5de3a8eaf4);


        circle_marker_65595d37ec459e689cbc67fb1e908621.bindPopup(popup_5e0ae96f95af121345ba2badb594ff3f)
        ;




            var circle_marker_c7e04701416ab103f4e57f13c1b8e57e = L.circleMarker(
                [40.4263, -3.60922],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_382b746b3c538a45eb0bef0bf3c59e25 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_92be0ac6637ccfddac8dd93318dcb1eb = $(`&lt;div id=&quot;html_92be0ac6637ccfddac8dd93318dcb1eb&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;23.0&lt;/div&gt;`)[0];
            popup_382b746b3c538a45eb0bef0bf3c59e25.setContent(html_92be0ac6637ccfddac8dd93318dcb1eb);


        circle_marker_c7e04701416ab103f4e57f13c1b8e57e.bindPopup(popup_382b746b3c538a45eb0bef0bf3c59e25)
        ;




            var circle_marker_2d1ea0402a04867c149b83a2f2e79fa9 = L.circleMarker(
                [40.43530204812947, -3.6110466103562953],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;yellow&quot;, &quot;fillOpacity&quot;: 1, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_a8516ba71be4178f04e6dd1586315ef3);


        var popup_fcdba62a6b5dfba66b91ca8e9a3feb0a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_6fe41db5f2b05a1b9b741c1f9714f66e = $(`&lt;div id=&quot;html_6fe41db5f2b05a1b9b741c1f9714f66e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;30.0&lt;/div&gt;`)[0];
            popup_fcdba62a6b5dfba66b91ca8e9a3feb0a.setContent(html_6fe41db5f2b05a1b9b741c1f9714f66e);


        circle_marker_2d1ea0402a04867c149b83a2f2e79fa9.bindPopup(popup_fcdba62a6b5dfba66b91ca8e9a3feb0a)
        ;



&lt;/script&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



**Insight 1b: There are still many yellow and orange dots, which may indicate that there is still potential to further exploit the factor of sporting events**
