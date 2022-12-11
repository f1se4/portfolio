# DATA PREPARATION

In this phase we are going to create new variables or transform the existing ones in order to give a better response to our objective.

We are going to give examples of both how to use internal variables and how to enrich with external variables.

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

## DATA UPLOAD


```python
con = sa.create_engine('sqlite:///../Datos/airbnb.db')

df = pd.read_sql('df', con = con)

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
      <th>index</th>
      <th>id</th>
      <th>name</th>
      <th>host_id</th>
      <th>neighbourhood_group</th>
      <th>neighbourhood</th>
      <th>latitude</th>
      <th>...</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>6369</td>
      <td>Rooftop terrace room ,  ensuite bathroom</td>
      <td>13660</td>
      <td>Chamartín</td>
      <td>Hispanoamérica</td>
      <td>40.45724</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>21853</td>
      <td>Bright and airy room</td>
      <td>83531</td>
      <td>Latina</td>
      <td>Cármenes</td>
      <td>40.40381</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>23001</td>
      <td>Apartmento Arganzuela- Madrid Rio</td>
      <td>82175</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.38840</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>24805</td>
      <td>Gran Via Studio Madrid</td>
      <td>346366726</td>
      <td>Centro</td>
      <td>Universidad</td>
      <td>40.42183</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>26825</td>
      <td>Single Room whith private Bathroom</td>
      <td>114340</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.38975</td>
      <td>...</td>
    </tr>
  </tbody>
</table>
</div>



## PREPARATION OF VARIABLES

### Creation of lever kpis

First we are going to create the analysis variables, that is, those that we had identified as the Kpis that we will use in the levers that influence the business.

We had said that there were 3:

* price per night: we already have this directly in the price variable, but we are going to review it to see that we understand it correctly
* occupation: we have availability_365 but it must be transformed
* price of the property: we will have to create this with external variables so we leave it for later

**We start with the price.**

The documentation does not clarify whether the price is for the entire property, or if a room is rented, it is per room.

It is a key piece of information to be able to make an assessment of the potential income of a property.

We are going to try to understand it by analyzing the average price by type of rental.

It is important to filter by only one district so as not to include the "zone" effect.

So first we choose a district that has a lot of data.


```python
df.distrito.value_counts()
```




    Centro                   8127
    Salamanca                1218
    Chamberí                 1089
    Arganzuela               1005
    Tetuán                    762
    Retiro                    618
    Carabanchel               581
    Chamartín                 538
    Ciudad Lineal             532
    Moncloa - Aravaca         493
    Puente de Vallecas        465
    San Blas - Canillejas     463
    Latina                    455
    Hortaleza                 354
    Fuencarral - El Pardo     265
    Usera                     233
    Barajas                   142
    Villaverde                129
    Moratalaz                  94
    Villa de Vallecas          90
    Vicálvaro                  57
    Name: distrito, dtype: int64




```python
df.loc[df.distrito == 'Centro',:].groupby('room_type').price.mean()
```




    room_type
    Entire home/apt    148.859980
    Private room        67.131643
    Shared room         60.464286
    Name: price, dtype: float64



Conclusion:
    
* renting the apartment has an average price of €148
* renting a room has an average price of €60 or €67 depending on whether it is shared or private
* Therefore, to calculate the "income" of a property, we must multiply the price by the number of rooms when it is of the Private room or Shared room types

However, multiplying the price by the total number of rooms can artificially bias upward the income-generating capacity of a property.

Since if it is rented by rooms, it is not likely that it will always be 100%

Therefore we should weight it by the average percentage of rented rooms.

We do not have that data, but suppose we have spoken with the business manager and he has told us that it is 70%.

We can create the total price variable by applying apply on a custom function.


```python
def crear_precio_total(registro):
    if (registro.beds > 1) & ((registro.room_type == 'Private room') | (registro.room_type == 'Shared room')):
        salida = registro.price * registro.beds * 0.7
    else:
        salida = registro.price
    return(salida)

df['precio_total'] = df.apply(crear_precio_total, axis = 1)
```

Comprobamos


```python
df[['room_type','price','beds','precio_total']].head(30)
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
      <th>room_type</th>
      <th>price</th>
      <th>beds</th>
      <th>precio_total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Private room</td>
      <td>60</td>
      <td>1.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Private room</td>
      <td>31</td>
      <td>1.0</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Entire home/apt</td>
      <td>50</td>
      <td>5.0</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Entire home/apt</td>
      <td>92</td>
      <td>1.0</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Private room</td>
      <td>26</td>
      <td>1.0</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Entire home/apt</td>
      <td>85</td>
      <td>3.0</td>
      <td>85.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Entire home/apt</td>
      <td>65</td>
      <td>2.0</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Entire home/apt</td>
      <td>54</td>
      <td>1.0</td>
      <td>54.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Entire home/apt</td>
      <td>1400</td>
      <td>3.0</td>
      <td>1400.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Entire home/apt</td>
      <td>81</td>
      <td>2.0</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Entire home/apt</td>
      <td>90</td>
      <td>3.0</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Entire home/apt</td>
      <td>82</td>
      <td>2.0</td>
      <td>82.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Private room</td>
      <td>40</td>
      <td>1.0</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Private room</td>
      <td>36</td>
      <td>2.0</td>
      <td>50.4</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Entire home/apt</td>
      <td>51</td>
      <td>1.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Entire home/apt</td>
      <td>76</td>
      <td>2.0</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Entire home/apt</td>
      <td>54</td>
      <td>3.0</td>
      <td>54.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Entire home/apt</td>
      <td>60</td>
      <td>3.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Entire home/apt</td>
      <td>55</td>
      <td>2.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Entire home/apt</td>
      <td>121</td>
      <td>6.0</td>
      <td>121.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Entire home/apt</td>
      <td>80</td>
      <td>2.0</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Entire home/apt</td>
      <td>63</td>
      <td>2.0</td>
      <td>63.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Entire home/apt</td>
      <td>63</td>
      <td>1.0</td>
      <td>63.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Entire home/apt</td>
      <td>46</td>
      <td>1.0</td>
      <td>46.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Entire home/apt</td>
      <td>171</td>
      <td>3.0</td>
      <td>171.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Private room</td>
      <td>55</td>
      <td>1.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Private room</td>
      <td>26</td>
      <td>2.0</td>
      <td>36.4</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Private room</td>
      <td>31</td>
      <td>2.0</td>
      <td>43.4</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Entire home/apt</td>
      <td>60</td>
      <td>1.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Entire home/apt</td>
      <td>149</td>
      <td>2.0</td>
      <td>149.0</td>
    </tr>
  </tbody>
</table>
</div>



**Now we go with the occupation**

The variable we have that allows us to measure this is availability_365.

This variable tells us the number of days in a year that the property is NOT occupied.

Therefore, we would be interested in transforming it into a more direct measure of occupancy, for example, the % of the year that it IS occupied.

We can do it with a direct transformation.


```python
df['ocupacion'] = ((365 - df.availability_365) / 365 * 100).astype('int')
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
      <th>index</th>
      <th>id</th>
      <th>name</th>
      <th>...</th>
      <th>precio_m2</th>
      <th>distrito</th>
      <th>precio_total</th>
      <th>ocupacion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>6369</td>
      <td>Rooftop terrace room ,  ensuite bathroom</td>
      <td>...</td>
      <td>5098</td>
      <td>Chamartín</td>
      <td>60.0</td>
      <td>50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>21853</td>
      <td>Bright and airy room</td>
      <td>...</td>
      <td>2267</td>
      <td>Latina</td>
      <td>31.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>23001</td>
      <td>Apartmento Arganzuela- Madrid Rio</td>
      <td>...</td>
      <td>4085</td>
      <td>Arganzuela</td>
      <td>50.0</td>
      <td>39</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>24805</td>
      <td>Gran Via Studio Madrid</td>
      <td>...</td>
      <td>4827</td>
      <td>Centro</td>
      <td>92.0</td>
      <td>68</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>26825</td>
      <td>Single Room whith private Bathroom</td>
      <td>...</td>
      <td>4085</td>
      <td>Arganzuela</td>
      <td>26.0</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### Transformation of analysis variables

Some of the seed questions are aimed at checking how the price or occupancy behaves according to other variables such as the number of rooms, the average rating, etc.

Normally we can do these analyzes better if we discretize the analysis variable.

In our case, the candidates for this analysis are: accommodates, bedrooms, beds and number_of_reviews.

In bedrooms, a more personalized discretization makes sense. In the others we can make it automatic.

**Discretize bedrooms**

We begin by evaluating the distribution of the data.


```python
df.bedrooms.value_counts().plot.bar();
```


    
![png](static/notebooks/airbnbds4/04_Preparacion%20de%20datos_files/04_Preparacion%20de%20datos_22_0.png)
    


We are going to discretize for 1,2,3 and more than 3.

We can use np.select


```python
condiciones = [df.bedrooms == 1,
               df.bedrooms == 2,
               df.bedrooms == 3,
               df.bedrooms > 3]

resultados = ['01_Una','02_Dos','03_Tres','04_Cuatro o mas']

df['bedrooms_disc'] = np.select(condiciones, resultados, default = -999)
```

Review


```python
df.bedrooms_disc.value_counts().plot.bar();
```


    
![png](static/notebooks/airbnbds4/04_Preparacion%20de%20datos_files/04_Preparacion%20de%20datos_26_0.png)
    


**Discretize accommodates, beds and number_of_reviews**

We are going to use qcut to discriminate with percentiles 0.5, 0.8, 1


```python
df['accommodates_disc'] = pd.qcut(df.accommodates,[0, 0.5, 0.8, 1],
                                 labels = ['0-2','3','4-16'])

df['accommodates_disc'].value_counts().sort_index(ascending = False).plot.barh();
```


    
![png](static/notebooks/airbnbds4/04_Preparacion%20de%20datos_files/04_Preparacion%20de%20datos_28_0.png)
    



```python
df['beds_disc'] = pd.qcut(df.beds,[0, 0.5, 0.8, 1],
                         labels = ['1','2','3-24'])

df['beds_disc'].value_counts().sort_index(ascending = False).plot.barh();
```


    
![png](static/notebooks/airbnbds4/04_Preparacion%20de%20datos_files/04_Preparacion%20de%20datos_29_0.png)
    



```python
df['number_of_reviews_disc'] = pd.qcut(df.number_of_reviews,[0, 0.5, 0.8, 1],
                                      labels = ['1-4','5-48','48-744'])

df['number_of_reviews_disc'].value_counts().sort_index(ascending = False).plot.barh();
```


    
![png](static/notebooks/airbnbds4/04_Preparacion%20de%20datos_files/04_Preparacion%20de%20datos_30_0.png)
    


### Creating variables with external data

In this particular case, many things could be done with external data.

The first thing, which we have already partially incorporated, is the property price lever.

We said that we could estimate it by multiplying the square meters of the property by the price per m2.

We have already obtained the price_m2, but we do not have the size of the property in the data.

What we can do is establish criteria based on the number of rooms.

It's not perfect, but it will serve as an approximation.

**Estimate of the square meters of the property**

Let's use the following algorithm:

* a room: m2 = 50
* two rooms: m2 = 70
* three rooms: m2 = 90
* four rooms: m2 = 120
* five or more rooms: m2 = 150


```python
condiciones = [df.bedrooms == 1,
               df.bedrooms == 2,
               df.bedrooms == 3,
               df.bedrooms == 4,
               df.bedrooms > 4]

resultados = [50,70,90,120,150]

df['m2'] = np.select(condiciones, resultados, default = -999)
```

Comprobamos


```python
df['m2'].value_counts()
```




    50     12422
    70      3617
    90      1228
    120      296
    150      147
    Name: m2, dtype: int64



Now we can estimate the purchase price of the property.

We remember that we took 30% from the price we got for bargaining power.


```python
df['precio_compra'] = df.m2 * df.precio_m2 * 0.7
```

Comprobamos


```python
df[['bedrooms','m2','distrito','precio_m2','precio_compra']].head(20)
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
      <th>bedrooms</th>
      <th>m2</th>
      <th>distrito</th>
      <th>precio_m2</th>
      <th>precio_compra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>50</td>
      <td>Chamartín</td>
      <td>5098</td>
      <td>178430.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>50</td>
      <td>Latina</td>
      <td>2267</td>
      <td>79345.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>90</td>
      <td>Arganzuela</td>
      <td>4085</td>
      <td>257355.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>4827</td>
      <td>168945.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.0</td>
      <td>50</td>
      <td>Arganzuela</td>
      <td>4085</td>
      <td>142975.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3.0</td>
      <td>90</td>
      <td>Arganzuela</td>
      <td>4085</td>
      <td>257355.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>4827</td>
      <td>168945.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>4827</td>
      <td>168945.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2.0</td>
      <td>70</td>
      <td>Centro</td>
      <td>4827</td>
      <td>236523.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>4827</td>
      <td>168945.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>4827</td>
      <td>168945.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2.0</td>
      <td>70</td>
      <td>Salamanca</td>
      <td>6114</td>
      <td>299586.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>4827</td>
      <td>168945.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>4827</td>
      <td>168945.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>4827</td>
      <td>168945.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>4827</td>
      <td>168945.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>4827</td>
      <td>168945.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2.0</td>
      <td>70</td>
      <td>Centro</td>
      <td>4827</td>
      <td>236523.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2.0</td>
      <td>70</td>
      <td>Centro</td>
      <td>4827</td>
      <td>236523.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>3.0</td>
      <td>90</td>
      <td>Centro</td>
      <td>4827</td>
      <td>304101.0</td>
    </tr>
  </tbody>
</table>
</div>



Now we are going to give an example of what other types of variables we can build.

In this case we could do a lot with the x,y coordinates.

Since in tourism the location is very important.

For example, we could calculate the distances to different points of interest such as monuments, entertainment venues, sports venues, etc.

Simply as an example we are going to calculate the distance from each property to Puerta del Sol.

To do this, we Google its longitude and latitude: https://www.123coordenadas.com/coordinates/81497-puerta-del-sol-madrid

Latitude: 40.4167278
Longitude: -3.7033387

**Calculation of the distance of each property to Puerta del Sol**

Given the curvature of the earth, the distance between two points based on their latitude and longitude is calculated using a formula called the Haversine distance.

A Google search gives us a built-in function to calculate it that we can adapt: [Haversine](https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points)


```python
from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):

      R = 6372.8 #En km, si usas millas tienes que cambiarlo por 3959.87433

      dLat = radians(lat2 - lat1)
      dLon = radians(lon2 - lon1)
      lat1 = radians(lat1)
      lat2 = radians(lat2)

      a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
      c = 2*asin(sqrt(a))

      return R * c
```

We create the variable


```python
#Las coordenadas de la Puerta del Sol serán lat1 y lon1
lat1 = 40.4167278
lon1 = -3.7033387

df['pdi_sol'] = df.apply(lambda registro: haversine(lat1,lon1,registro.latitude,registro.longitude),axis = 1)
```

We check by reviewing the average distance by districts.


```python
df.groupby('distrito').pdi_sol.mean().sort_values()
```




    distrito
    Centro                    0.730611
    Arganzuela                1.939114
    Chamberí                  2.133167
    Retiro                    2.450593
    Salamanca                 2.715975
    Moncloa - Aravaca         3.294526
    Usera                     3.928874
    Latina                    3.942634
    Carabanchel               3.970238
    Chamartín                 4.432842
    Puente de Vallecas        4.481127
    Tetuán                    4.624605
    Moratalaz                 5.073901
    Ciudad Lineal             5.231293
    Villaverde                7.664192
    Fuencarral - El Pardo     8.062301
    Hortaleza                 8.074184
    San Blas - Canillejas     8.199011
    Vicálvaro                 8.599559
    Villa de Vallecas         9.176618
    Barajas                  11.439064
    Name: pdi_sol, dtype: float64



## WE SAVE IN THE DATAMART

We are going to save this version as df_preparado


```python
df.to_sql('df_preparado', con = con, if_exists = 'replace')
```
