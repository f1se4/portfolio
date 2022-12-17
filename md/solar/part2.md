# CALIDAD DE DATOS Y CREACION DATAMART ANALITICO

## SET UP


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

#Automcompletar rápido
%config IPCompleter.greedy=True

import fiser_tools as fs
fs.misc.dark_theme()
```

## CARGA DE DATOS

Este caso se compone de 4 ficheros:

* Planta 1, datos de generación
* Planta 1, datos de sensor ambiental
* Planta 2, datos de generación
* Planta 2, datos de sensor ambiental

### Carga de datos planta 1 - datos de generación


```python
p1g = pd.read_csv('Plant_1_Generation_Data.csv')
p1g
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
      <th>DATE_TIME</th>
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>DC_POWER</th>
      <th>AC_POWER</th>
      <th>DAILY_YIELD</th>
      <th>TOTAL_YIELD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15-05-2020 00:00</td>
      <td>4135001</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>6259559.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15-05-2020 00:00</td>
      <td>4135001</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>6183645.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>15-05-2020 00:00</td>
      <td>4135001</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>6987759.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15-05-2020 00:00</td>
      <td>4135001</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>7602960.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15-05-2020 00:00</td>
      <td>4135001</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>7158964.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>68773</th>
      <td>17-06-2020 23:45</td>
      <td>4135001</td>
      <td>uHbuxQJl8lW7ozc</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5967.000</td>
      <td>7287002.0</td>
    </tr>
    <tr>
      <th>68774</th>
      <td>17-06-2020 23:45</td>
      <td>4135001</td>
      <td>wCURE6d3bPkepu2</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5147.625</td>
      <td>7028601.0</td>
    </tr>
    <tr>
      <th>68775</th>
      <td>17-06-2020 23:45</td>
      <td>4135001</td>
      <td>z9Y9gH1T5YWrNuG</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5819.000</td>
      <td>7251204.0</td>
    </tr>
    <tr>
      <th>68776</th>
      <td>17-06-2020 23:45</td>
      <td>4135001</td>
      <td>zBIq5rxdHJRwDNY</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5817.000</td>
      <td>6583369.0</td>
    </tr>
    <tr>
      <th>68777</th>
      <td>17-06-2020 23:45</td>
      <td>4135001</td>
      <td>zVJPv84UY57bAof</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5910.000</td>
      <td>7363272.0</td>
    </tr>
  </tbody>
</table>
<p>68778 rows × 7 columns</p>
</div>



### Carga de datos planta 1 - datos de sensor ambiental


```python
p1w = pd.read_csv('Plant_1_Weather_Sensor_Data.csv')
p1w
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
      <th>DATE_TIME</th>
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>AMBIENT_TEMPERATURE</th>
      <th>MODULE_TEMPERATURE</th>
      <th>IRRADIATION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.184316</td>
      <td>22.857507</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:15:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.084589</td>
      <td>22.761668</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:30:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.935753</td>
      <td>22.592306</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:45:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.846130</td>
      <td>22.360852</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 01:00:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.621525</td>
      <td>22.165423</td>
      <td>0.0</td>
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
      <th>3177</th>
      <td>2020-06-17 22:45:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>22.150570</td>
      <td>21.480377</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3178</th>
      <td>2020-06-17 23:00:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>22.129816</td>
      <td>21.389024</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3179</th>
      <td>2020-06-17 23:15:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>22.008275</td>
      <td>20.709211</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3180</th>
      <td>2020-06-17 23:30:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>21.969495</td>
      <td>20.734963</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3181</th>
      <td>2020-06-17 23:45:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>21.909288</td>
      <td>20.427972</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>3182 rows × 6 columns</p>
</div>



### Carga de datos planta 2 - datos de generación


```python
p2g = pd.read_csv('Plant_2_Generation_Data.csv')
p2g
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
      <th>DATE_TIME</th>
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>DC_POWER</th>
      <th>AC_POWER</th>
      <th>DAILY_YIELD</th>
      <th>TOTAL_YIELD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>4136001</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>9425.000000</td>
      <td>2.429011e+06</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:00:00</td>
      <td>4136001</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>1.215279e+09</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:00:00</td>
      <td>4136001</td>
      <td>9kRcWv60rDACzjR</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3075.333333</td>
      <td>2.247720e+09</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:00:00</td>
      <td>4136001</td>
      <td>Et9kgGMDl729KT4</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>269.933333</td>
      <td>1.704250e+06</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 00:00:00</td>
      <td>4136001</td>
      <td>IQ2d7wF4YD8zU1Q</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3177.000000</td>
      <td>1.994153e+07</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>67693</th>
      <td>2020-06-17 23:45:00</td>
      <td>4136001</td>
      <td>q49J1IKaHRwDQnt</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4157.000000</td>
      <td>5.207580e+05</td>
    </tr>
    <tr>
      <th>67694</th>
      <td>2020-06-17 23:45:00</td>
      <td>4136001</td>
      <td>rrq4fwE8jgrTyWY</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3931.000000</td>
      <td>1.211314e+08</td>
    </tr>
    <tr>
      <th>67695</th>
      <td>2020-06-17 23:45:00</td>
      <td>4136001</td>
      <td>vOuJvMaM2sgwLmb</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4322.000000</td>
      <td>2.427691e+06</td>
    </tr>
    <tr>
      <th>67696</th>
      <td>2020-06-17 23:45:00</td>
      <td>4136001</td>
      <td>xMbIugepa2P7lBB</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4218.000000</td>
      <td>1.068964e+08</td>
    </tr>
    <tr>
      <th>67697</th>
      <td>2020-06-17 23:45:00</td>
      <td>4136001</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4316.000000</td>
      <td>2.093357e+08</td>
    </tr>
  </tbody>
</table>
<p>67698 rows × 7 columns</p>
</div>



### Carga de datos planta 2 - datos de sensor ambiental


```python
p2w = pd.read_csv('Plant_2_Weather_Sensor_Data.csv')
p2w
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
      <th>DATE_TIME</th>
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>AMBIENT_TEMPERATURE</th>
      <th>MODULE_TEMPERATURE</th>
      <th>IRRADIATION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>27.004764</td>
      <td>25.060789</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:15:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>26.880811</td>
      <td>24.421869</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:30:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>26.682055</td>
      <td>24.427290</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:45:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>26.500589</td>
      <td>24.420678</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 01:00:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>26.596148</td>
      <td>25.088210</td>
      <td>0.0</td>
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
      <th>3254</th>
      <td>2020-06-17 22:45:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.511703</td>
      <td>22.856201</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3255</th>
      <td>2020-06-17 23:00:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.482282</td>
      <td>22.744190</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3256</th>
      <td>2020-06-17 23:15:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.354743</td>
      <td>22.492245</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3257</th>
      <td>2020-06-17 23:30:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.291048</td>
      <td>22.373909</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3258</th>
      <td>2020-06-17 23:45:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.202871</td>
      <td>22.535908</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>3259 rows × 6 columns</p>
</div>



## CALIDAD DE DATOS

### Calidad de planta 1 - datos de generación

Empezamos con la visión general.


```python
p1g.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 68778 entries, 0 to 68777
    Data columns (total 7 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   DATE_TIME    68778 non-null  object 
     1   PLANT_ID     68778 non-null  int64  
     2   SOURCE_KEY   68778 non-null  object 
     3   DC_POWER     68778 non-null  float64
     4   AC_POWER     68778 non-null  float64
     5   DAILY_YIELD  68778 non-null  float64
     6   TOTAL_YIELD  68778 non-null  float64
    dtypes: float64(4), int64(1), object(2)
    memory usage: 3.7+ MB
    

Vemos que no hay nulos.

Vemos que DATE_TIME está como object.

Convertimos DATE_TIME a tipo datetime.


```python
p1g['DATE_TIME'] = pd.to_datetime(p1g.DATE_TIME,dayfirst=True)
```

Revisamos una muestra de datos.


```python
p1g.head()
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
      <th>DATE_TIME</th>
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>DC_POWER</th>
      <th>AC_POWER</th>
      <th>DAILY_YIELD</th>
      <th>TOTAL_YIELD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15</td>
      <td>4135001</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6259559.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15</td>
      <td>4135001</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6183645.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15</td>
      <td>4135001</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6987759.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15</td>
      <td>4135001</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7602960.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15</td>
      <td>4135001</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7158964.0</td>
    </tr>
  </tbody>
</table>
</div>



Comprobamos que el identificador de planta sea único.


```python
p1g.PLANT_ID.unique()
```




    array([4135001], dtype=int64)



Vamos a reemplazarlo por un literal más legible.


```python
p1g['PLANT_ID'] = p1g.PLANT_ID.replace(4135001, 'p1')
```

Revisamos los descriptivos.


```python
p1g.describe().T
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>DC_POWER</th>
      <td>68778.0</td>
      <td>3.147426e+03</td>
      <td>4036.457169</td>
      <td>0.0</td>
      <td>0.000000e+00</td>
      <td>4.290000e+02</td>
      <td>6.366964e+03</td>
      <td>14471.125</td>
    </tr>
    <tr>
      <th>AC_POWER</th>
      <td>68778.0</td>
      <td>3.078028e+02</td>
      <td>394.396439</td>
      <td>0.0</td>
      <td>0.000000e+00</td>
      <td>4.149375e+01</td>
      <td>6.236187e+02</td>
      <td>1410.950</td>
    </tr>
    <tr>
      <th>DAILY_YIELD</th>
      <td>68778.0</td>
      <td>3.295969e+03</td>
      <td>3145.178309</td>
      <td>0.0</td>
      <td>0.000000e+00</td>
      <td>2.658714e+03</td>
      <td>6.274000e+03</td>
      <td>9163.000</td>
    </tr>
    <tr>
      <th>TOTAL_YIELD</th>
      <td>68778.0</td>
      <td>6.978712e+06</td>
      <td>416271.982856</td>
      <td>6183645.0</td>
      <td>6.512003e+06</td>
      <td>7.146685e+06</td>
      <td>7.268706e+06</td>
      <td>7846821.000</td>
    </tr>
  </tbody>
</table>
</div>



Vamos a quitar la visualización de notación científica.


```python
pd.options.display.float_format = '{:15.2f}'.format
```


```python
p1g.describe().T
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>DC_POWER</th>
      <td>68778.00</td>
      <td>3147.43</td>
      <td>4036.46</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>429.00</td>
      <td>6366.96</td>
      <td>14471.12</td>
    </tr>
    <tr>
      <th>AC_POWER</th>
      <td>68778.00</td>
      <td>307.80</td>
      <td>394.40</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>41.49</td>
      <td>623.62</td>
      <td>1410.95</td>
    </tr>
    <tr>
      <th>DAILY_YIELD</th>
      <td>68778.00</td>
      <td>3295.97</td>
      <td>3145.18</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2658.71</td>
      <td>6274.00</td>
      <td>9163.00</td>
    </tr>
    <tr>
      <th>TOTAL_YIELD</th>
      <td>68778.00</td>
      <td>6978711.76</td>
      <td>416271.98</td>
      <td>6183645.00</td>
      <td>6512002.54</td>
      <td>7146685.00</td>
      <td>7268705.91</td>
      <td>7846821.00</td>
    </tr>
  </tbody>
</table>
</div>



Resulta extraño la diferencia de medias entre DC y AC.

Vamos a visualizarlo.


```python
p1g[['DC_POWER','AC_POWER']].plot(figsize = (16,12));
```


    
![png](static/notebooks/solar/static/notebooks/solar/02_Calidad_de_datos_files/02_Calidad_de_datos_31_0.png)
    


La diferencia es muy grande.

Primero vamos a comprobar si van en la misma dirección aunque sea a disinta escala (con una correlación), y después vamos a comprobar cual es el ratio medio entre ambas medidas.


```python
p1g.DC_POWER.corr(p1g.AC_POWER)
```




    0.9999962553331414




```python
(p1g.DC_POWER / p1g.AC_POWER).describe()
```




    count          36827.00
    mean              10.23
    std                0.05
    min                9.38
    25%               10.20
    50%               10.22
    75%               10.25
    max               10.47
    dtype: float64



Parece que los Inverters están transformando solo el 10% de DC a AC, lo cual a priori es muy bajo.

De todas formas desde la calidad llegamos hasta aquí y seguiremos explorando esto en la parte de análisis y comparándolo con la Planta 2 a ver si pasa lo mismo.

Analizamos la variable categórica, que es el identificador de los inverters.


```python
p1g.SOURCE_KEY.nunique()
```




    22




```python
p1g.SOURCE_KEY.value_counts()
```




    bvBOhCH3iADSZry    3155
    1BY6WEcLGh8j5v7    3154
    7JYdWkrLSPkdwr4    3133
    VHMLBKoKgIrUVDU    3133
    ZnxXDlPa8U1GXgE    3130
    ih0vzX44oOqAx2f    3130
    z9Y9gH1T5YWrNuG    3126
    wCURE6d3bPkepu2    3126
    uHbuxQJl8lW7ozc    3125
    pkci93gMrogZuBj    3125
    iCRJl6heRkivqQ3    3125
    rGa61gmuvPhdLxV    3124
    sjndEbLyjtCKgGv    3124
    McdE0feGgRqW7Ca    3124
    zVJPv84UY57bAof    3124
    ZoEaEvLYb1n2sOq    3123
    1IF53ai7Xc0U56Y    3119
    adLQvlD726eNBSB    3119
    zBIq5rxdHJRwDNY    3119
    WRmjgnKYAwPKWDb    3118
    3PZuoBAID5Wc2HD    3118
    YxYtjZvoooNbGkE    3104
    Name: SOURCE_KEY, dtype: int64



Conclusiones:

    * La planta 1 tiene 22 inverters
    * Todos tienen un número similar de medidas aunque no exactamente igual
    * Podrían ser paradas por mantenimientos, o simples pérdidas de datos pero lo apuntamos para la fase de análisis

Vamos a analizar las variables DAILY_YIELD, ya que los metadatos nos dicen que la variable TOTAL_YIELD es el total acumulado **por inverter**, pero en DAILY_YIELD no lo especifica, por lo que no sabemos si es un acumulado por inverter o por planta.

La hipótesis es la siguiente: si es por planta no debería haber diferencias entre el dato de los diferentes inverters en el mismo momento puntual.

Y por consiguiente si vemos que sí hay diferencias entonces es que el dato es por inverter.

Para comprobarlo nos sirve con coger una muestra de inverters.


```python
seleccion = list(p1g.SOURCE_KEY.unique()[:5])
```


```python
temp = p1g[p1g.SOURCE_KEY.isin(seleccion)].set_index('DATE_TIME')
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
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>DC_POWER</th>
      <th>AC_POWER</th>
      <th>DAILY_YIELD</th>
      <th>TOTAL_YIELD</th>
    </tr>
    <tr>
      <th>DATE_TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6259559.00</td>
    </tr>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6183645.00</td>
    </tr>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6987759.00</td>
    </tr>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7602960.00</td>
    </tr>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7158964.00</td>
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
      <th>2020-06-17 23:45:00</th>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>5521.00</td>
      <td>6485319.00</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p1</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6034.00</td>
      <td>6433566.00</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p1</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6052.00</td>
      <td>7237425.00</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p1</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>5856.00</td>
      <td>7846821.00</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p1</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>5992.00</td>
      <td>7408587.00</td>
    </tr>
  </tbody>
</table>
<p>15648 rows × 6 columns</p>
</div>



En los datos ya vemos que es diferente, pero vamos a comprobar sobre más datos para que no sea un efecto de esos registros en concreto.

Vamos a verlo gráficamente, y por simplificar vamos a coger solo una muestra de días.

Como tenemos la fecha como index recordamos que podemos usar indexación parcial y slice.


```python
temp = temp.loc['2020-06-01':'2020-06-05']
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
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>DC_POWER</th>
      <th>AC_POWER</th>
      <th>DAILY_YIELD</th>
      <th>TOTAL_YIELD</th>
    </tr>
    <tr>
      <th>DATE_TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-06-01 00:00:00</th>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>829.00</td>
      <td>6377931.00</td>
    </tr>
    <tr>
      <th>2020-06-01 00:00:00</th>
      <td>p1</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6311432.00</td>
    </tr>
    <tr>
      <th>2020-06-01 00:00:00</th>
      <td>p1</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7115304.00</td>
    </tr>
    <tr>
      <th>2020-06-01 00:00:00</th>
      <td>p1</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>730.38</td>
      <td>7727821.00</td>
    </tr>
    <tr>
      <th>2020-06-01 00:00:00</th>
      <td>p1</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7286760.00</td>
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
      <th>2020-06-05 23:45:00</th>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7162.00</td>
      <td>6412542.00</td>
    </tr>
    <tr>
      <th>2020-06-05 23:45:00</th>
      <td>p1</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6348557.00</td>
    </tr>
    <tr>
      <th>2020-06-05 23:45:00</th>
      <td>p1</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7152486.00</td>
    </tr>
    <tr>
      <th>2020-06-05 23:45:00</th>
      <td>p1</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7764140.00</td>
    </tr>
    <tr>
      <th>2020-06-05 23:45:00</th>
      <td>p1</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4950.00</td>
      <td>7324681.00</td>
    </tr>
  </tbody>
</table>
<p>2370 rows × 6 columns</p>
</div>




```python
plt.figure(figsize = (16,12))
sns.lineplot(data = temp.reset_index(), x = temp.reset_index().DATE_TIME, y = 'DAILY_YIELD', hue = 'SOURCE_KEY');
```


    
![png](static/notebooks/solar/02_Calidad_de_datos_files/02_Calidad_de_datos_45_0.png)
    


Definitivamente diferentes inverters tienen diferentes datos en el mismo momento temporal, por lo que concluímos que esa variable es **por inverter**

Por último vamos a analizar el período en el que tenemos datos y si el número de mediciones diarias es constante.


```python
p1g.DATE_TIME.dt.date.value_counts().sort_index().plot.bar(figsize = (12,8));
```


    
![png](static/notebooks/solar/02_Calidad_de_datos_files/02_Calidad_de_datos_48_0.png)
    


Conclusiones:

    * El período de datos es entre el 15 de Mayo del 2020 y el 17 de Junio de 2020
    * Tenemos datos para todos los días, no falta ninguno intermedio
    * Pero algunos días como el 21/05 o el 29/05 tienen menos mediciones
    * Por lo que no parece 100% regular

### Calidad de datos planta 1 - datos de sensor ambiental


```python
p1w.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3182 entries, 0 to 3181
    Data columns (total 6 columns):
     #   Column               Non-Null Count  Dtype  
    ---  ------               --------------  -----  
     0   DATE_TIME            3182 non-null   object 
     1   PLANT_ID             3182 non-null   int64  
     2   SOURCE_KEY           3182 non-null   object 
     3   AMBIENT_TEMPERATURE  3182 non-null   float64
     4   MODULE_TEMPERATURE   3182 non-null   float64
     5   IRRADIATION          3182 non-null   float64
    dtypes: float64(3), int64(1), object(2)
    memory usage: 149.3+ KB
    

Corregimos el tipo de DATE_TIME


```python
p1w.DATE_TIME = pd.to_datetime(p1w.DATE_TIME)
p1w.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3182 entries, 0 to 3181
    Data columns (total 6 columns):
     #   Column               Non-Null Count  Dtype         
    ---  ------               --------------  -----         
     0   DATE_TIME            3182 non-null   datetime64[ns]
     1   PLANT_ID             3182 non-null   int64         
     2   SOURCE_KEY           3182 non-null   object        
     3   AMBIENT_TEMPERATURE  3182 non-null   float64       
     4   MODULE_TEMPERATURE   3182 non-null   float64       
     5   IRRADIATION          3182 non-null   float64       
    dtypes: datetime64[ns](1), float64(3), int64(1), object(1)
    memory usage: 149.3+ KB
    


```python
p1w.head()
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
      <th>DATE_TIME</th>
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>AMBIENT_TEMPERATURE</th>
      <th>MODULE_TEMPERATURE</th>
      <th>IRRADIATION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:15:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.08</td>
      <td>22.76</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:30:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.94</td>
      <td>22.59</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:45:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.85</td>
      <td>22.36</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 01:00:00</td>
      <td>4135001</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.62</td>
      <td>22.17</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>



Reemplazamos el nombre de la planta.


```python
p1w['PLANT_ID'] = p1w.PLANT_ID.replace(4135001,'p1')
p1w
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
      <th>DATE_TIME</th>
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>AMBIENT_TEMPERATURE</th>
      <th>MODULE_TEMPERATURE</th>
      <th>IRRADIATION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:15:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.08</td>
      <td>22.76</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:30:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.94</td>
      <td>22.59</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:45:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.85</td>
      <td>22.36</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 01:00:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.62</td>
      <td>22.17</td>
      <td>0.00</td>
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
      <th>3177</th>
      <td>2020-06-17 22:45:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>22.15</td>
      <td>21.48</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3178</th>
      <td>2020-06-17 23:00:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>22.13</td>
      <td>21.39</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3179</th>
      <td>2020-06-17 23:15:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>22.01</td>
      <td>20.71</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3180</th>
      <td>2020-06-17 23:30:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>21.97</td>
      <td>20.73</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3181</th>
      <td>2020-06-17 23:45:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>21.91</td>
      <td>20.43</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>3182 rows × 6 columns</p>
</div>



Revisamos los estadísticos.


```python
p1w.describe().T
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AMBIENT_TEMPERATURE</th>
      <td>3182.00</td>
      <td>25.53</td>
      <td>3.35</td>
      <td>20.40</td>
      <td>22.71</td>
      <td>24.61</td>
      <td>27.92</td>
      <td>35.25</td>
    </tr>
    <tr>
      <th>MODULE_TEMPERATURE</th>
      <td>3182.00</td>
      <td>31.09</td>
      <td>12.26</td>
      <td>18.14</td>
      <td>21.09</td>
      <td>24.62</td>
      <td>41.31</td>
      <td>65.55</td>
    </tr>
    <tr>
      <th>IRRADIATION</th>
      <td>3182.00</td>
      <td>0.23</td>
      <td>0.30</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>0.45</td>
      <td>1.22</td>
    </tr>
  </tbody>
</table>
</div>



Revisamos la variable categórica, que es el identificador del sensor.


```python
p1w.SOURCE_KEY.nunique()
```




    1



Solo hay un sensor de variables ambientales en la planta.

Revisamos la fecha.


```python
p1w.DATE_TIME.dt.date.value_counts().sort_index().plot.bar(figsize = (12,8));
```


    
![png](static/notebooks/solar/02_Calidad_de_datos_files/02_Calidad_de_datos_63_0.png)
    


Conclusiones:

    * El período de datos es entre el 15 de Mayo del 2020 y el 17 de Junio de 2020
    * Tenemos datos para todos los días, no falta ninguno intermedio
    * Pero algunos días como el 21/05 o el 29/05 tienen menos mediciones
    * Por lo que no parece 100% regular

### Calidad de planta 2 - datos de generación


```python
p2g.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 67698 entries, 0 to 67697
    Data columns (total 7 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   DATE_TIME    67698 non-null  object 
     1   PLANT_ID     67698 non-null  int64  
     2   SOURCE_KEY   67698 non-null  object 
     3   DC_POWER     67698 non-null  float64
     4   AC_POWER     67698 non-null  float64
     5   DAILY_YIELD  67698 non-null  float64
     6   TOTAL_YIELD  67698 non-null  float64
    dtypes: float64(4), int64(1), object(2)
    memory usage: 3.6+ MB
    


```python
p2g['DATE_TIME'] = pd.to_datetime(p2g.DATE_TIME)
```


```python
p2g['PLANT_ID'] = p2g.PLANT_ID.replace(4136001, 'p2')
```


```python
p2g.head()
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
      <th>DATE_TIME</th>
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>DC_POWER</th>
      <th>AC_POWER</th>
      <th>DAILY_YIELD</th>
      <th>TOTAL_YIELD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15</td>
      <td>p2</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>9425.00</td>
      <td>2429011.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15</td>
      <td>p2</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1215278736.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15</td>
      <td>p2</td>
      <td>9kRcWv60rDACzjR</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3075.33</td>
      <td>2247719577.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15</td>
      <td>p2</td>
      <td>Et9kgGMDl729KT4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>269.93</td>
      <td>1704250.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15</td>
      <td>p2</td>
      <td>IQ2d7wF4YD8zU1Q</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3177.00</td>
      <td>19941526.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
p2g.describe().T
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>DC_POWER</th>
      <td>67698.00</td>
      <td>246.70</td>
      <td>370.57</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>446.59</td>
      <td>1420.93</td>
    </tr>
    <tr>
      <th>AC_POWER</th>
      <td>67698.00</td>
      <td>241.28</td>
      <td>362.11</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>438.22</td>
      <td>1385.42</td>
    </tr>
    <tr>
      <th>DAILY_YIELD</th>
      <td>67698.00</td>
      <td>3294.89</td>
      <td>2919.45</td>
      <td>0.00</td>
      <td>272.75</td>
      <td>2911.00</td>
      <td>5534.00</td>
      <td>9873.00</td>
    </tr>
    <tr>
      <th>TOTAL_YIELD</th>
      <td>67698.00</td>
      <td>658944788.42</td>
      <td>729667771.07</td>
      <td>0.00</td>
      <td>19964944.87</td>
      <td>282627587.00</td>
      <td>1348495113.00</td>
      <td>2247916295.00</td>
    </tr>
  </tbody>
</table>
</div>



En este caso los valores de DC y AC están mucho más cercanos entre sí.

Vamos a calcular el ratio.


```python
(p2g.DC_POWER / p2g.AC_POWER).describe()
```




    count          32036.00
    mean               1.02
    std                0.01
    min                0.99
    25%                1.02
    50%                1.02
    75%                1.03
    max                1.10
    dtype: float64



Ahora los valores del ratio sí están muy próximos a uno.

Analizamos la variable categórica, que es el identificador de los inverters.


```python
p2g.SOURCE_KEY.nunique()
```




    22




```python
p2g.SOURCE_KEY.value_counts()
```




    xoJJ8DcxJEcupym    3259
    WcxssY2VbP4hApt    3259
    9kRcWv60rDACzjR    3259
    vOuJvMaM2sgwLmb    3259
    rrq4fwE8jgrTyWY    3259
    LYwnQax7tkwH5Cb    3259
    LlT2YUhhzqhg5Sw    3259
    q49J1IKaHRwDQnt    3259
    oZZkBaNadn6DNKz    3259
    PeE6FRyGXUgsRhN    3259
    81aHJ1q11NBPMrL    3259
    V94E5Ben1TlhnDV    3259
    oZ35aAeoifZaQzV    3195
    4UPUqMRk7TRMgml    3195
    Qf4GUc1pJu5T6c6    3195
    Mx2yZCDsyf6DPfv    3195
    Et9kgGMDl729KT4    3195
    Quc1TzYxW2pYoWX    3195
    mqwcsP2rE7J0TFp    2355
    NgDl19wMapZy17u    2355
    IQ2d7wF4YD8zU1Q    2355
    xMbIugepa2P7lBB    2355
    Name: SOURCE_KEY, dtype: int64



Conclusiones:

    * La planta 2 tiene 22 inverters
    * Todos tienen un número similar de medidas aunque no exactamente igual
    * A excepción de 4 que tienen unas 800 medidas menos
    * Lo apuntamos para la fase de análisis

Por último vamos a analizar la fecha.


```python
p2g.DATE_TIME.dt.date.value_counts().sort_index().plot.bar(figsize = (12,8));
```


    
![png](static/notebooks/solar/02_Calidad_de_datos_files/02_Calidad_de_datos_79_0.png)
    


Conclusiones:

    * El período de datos es entre el 15 de Mayo del 2020 y el 17 de Junio de 2020
    * Tenemos datos para todos los días, no falta ninguno intermedio
    * Pero algunos días como el 20/05 y varios más tienen menos mediciones
    * Por lo que no parece 100% regular

### Calidad de datos planta 2 - datos de sensor ambiental


```python
p2w.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3259 entries, 0 to 3258
    Data columns (total 6 columns):
     #   Column               Non-Null Count  Dtype  
    ---  ------               --------------  -----  
     0   DATE_TIME            3259 non-null   object 
     1   PLANT_ID             3259 non-null   int64  
     2   SOURCE_KEY           3259 non-null   object 
     3   AMBIENT_TEMPERATURE  3259 non-null   float64
     4   MODULE_TEMPERATURE   3259 non-null   float64
     5   IRRADIATION          3259 non-null   float64
    dtypes: float64(3), int64(1), object(2)
    memory usage: 152.9+ KB
    

Corregimos el tipo de DATE_TIME


```python
p2w.DATE_TIME = pd.to_datetime(p2w.DATE_TIME)
p2w.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3259 entries, 0 to 3258
    Data columns (total 6 columns):
     #   Column               Non-Null Count  Dtype         
    ---  ------               --------------  -----         
     0   DATE_TIME            3259 non-null   datetime64[ns]
     1   PLANT_ID             3259 non-null   int64         
     2   SOURCE_KEY           3259 non-null   object        
     3   AMBIENT_TEMPERATURE  3259 non-null   float64       
     4   MODULE_TEMPERATURE   3259 non-null   float64       
     5   IRRADIATION          3259 non-null   float64       
    dtypes: datetime64[ns](1), float64(3), int64(1), object(1)
    memory usage: 152.9+ KB
    


```python
p2w.head()
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
      <th>DATE_TIME</th>
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>AMBIENT_TEMPERATURE</th>
      <th>MODULE_TEMPERATURE</th>
      <th>IRRADIATION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>27.00</td>
      <td>25.06</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:15:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>26.88</td>
      <td>24.42</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:30:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>26.68</td>
      <td>24.43</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:45:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>26.50</td>
      <td>24.42</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 01:00:00</td>
      <td>4136001</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>26.60</td>
      <td>25.09</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>



Reemplazamos el nombre de la planta.


```python
p2w['PLANT_ID'] = p2w.PLANT_ID.replace(4136001,'p2')
p2w
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
      <th>DATE_TIME</th>
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>AMBIENT_TEMPERATURE</th>
      <th>MODULE_TEMPERATURE</th>
      <th>IRRADIATION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>27.00</td>
      <td>25.06</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:15:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>26.88</td>
      <td>24.42</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:30:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>26.68</td>
      <td>24.43</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:45:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>26.50</td>
      <td>24.42</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 01:00:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>26.60</td>
      <td>25.09</td>
      <td>0.00</td>
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
      <th>3254</th>
      <td>2020-06-17 22:45:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.51</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3255</th>
      <td>2020-06-17 23:00:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.48</td>
      <td>22.74</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3256</th>
      <td>2020-06-17 23:15:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.35</td>
      <td>22.49</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3257</th>
      <td>2020-06-17 23:30:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.29</td>
      <td>22.37</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3258</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>3259 rows × 6 columns</p>
</div>



Revisamos los estadísticos.


```python
p2w.describe().T
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AMBIENT_TEMPERATURE</th>
      <td>3259.00</td>
      <td>28.07</td>
      <td>4.06</td>
      <td>20.94</td>
      <td>24.60</td>
      <td>26.98</td>
      <td>31.06</td>
      <td>39.18</td>
    </tr>
    <tr>
      <th>MODULE_TEMPERATURE</th>
      <td>3259.00</td>
      <td>32.77</td>
      <td>11.34</td>
      <td>20.27</td>
      <td>23.72</td>
      <td>27.53</td>
      <td>40.48</td>
      <td>66.64</td>
    </tr>
    <tr>
      <th>IRRADIATION</th>
      <td>3259.00</td>
      <td>0.23</td>
      <td>0.31</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>0.44</td>
      <td>1.10</td>
    </tr>
  </tbody>
</table>
</div>



Analizamos la variable categórica, que es el identificador del sensor.


```python
p2w.SOURCE_KEY.nunique()
```




    1



Solo hay un sensor de variables ambientales en la planta.

Revisamos la fecha.


```python
p2w.DATE_TIME.dt.date.value_counts().sort_index().plot.bar(figsize = (12,8));
```


    
![png](static/notebooks/solar/02_Calidad_de_datos_files/02_Calidad_de_datos_94_0.png)
    


Conclusiones:

    * El período de datos es entre el 15 de Mayo del 2020 y el 17 de Junio de 2020
    * Tenemos datos para todos los días, no falta ninguno intermedio
    * Pero algunos días como el 15/05 u otros tienen menos mediciones, aunque faltan mucho menos que en los otros datasets
    * Pero no parece 100% regular

### Temas pendientes de la calidad de datos para analizar posteriormente

* En la planta 1 parece que los Inverters están transformando solo el 10% de DC a AC, lo cual a priori es muy bajo.
* En la planta 2 el ratio es mucho más cercano a 1.
* Los intervalos de medida no son 100% regulares. Hay días con menos medidas, y hay también diferencias por inverters.


## CREACIÓN DEL DATAMART ANALITICO

Vamos a hacer una unión por partes.

Primero los dos datasets de generación. Que será una apilación de registros ya que los campos son iguales.

Después los dos de medidas ambientales. Que será una apilación de registros ya que los campos son iguales.

Y por último cruzaremos ambos parciales mediante la integración por campos clave.

### Unión de los datasets de generación


```python
gener = pd.concat([p1g,p2g],axis = 'index')
gener
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
      <th>DATE_TIME</th>
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>DC_POWER</th>
      <th>AC_POWER</th>
      <th>DAILY_YIELD</th>
      <th>TOTAL_YIELD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6259559.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6183645.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6987759.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7602960.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7158964.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>67693</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>q49J1IKaHRwDQnt</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4157.00</td>
      <td>520758.00</td>
    </tr>
    <tr>
      <th>67694</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>rrq4fwE8jgrTyWY</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3931.00</td>
      <td>121131356.00</td>
    </tr>
    <tr>
      <th>67695</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>vOuJvMaM2sgwLmb</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4322.00</td>
      <td>2427691.00</td>
    </tr>
    <tr>
      <th>67696</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>xMbIugepa2P7lBB</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4218.00</td>
      <td>106896394.00</td>
    </tr>
    <tr>
      <th>67697</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4316.00</td>
      <td>209335741.00</td>
    </tr>
  </tbody>
</table>
<p>136476 rows × 7 columns</p>
</div>



Vamos a renombrar ya las variables para hacerlas más descriptivas y usables.


```python
gener.columns = ['fecha','planta','inverter_id','kw_dc','kw_ac','kw_dia','kw_total']
gener
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
      <th>fecha</th>
      <th>planta</th>
      <th>inverter_id</th>
      <th>kw_dc</th>
      <th>kw_ac</th>
      <th>kw_dia</th>
      <th>kw_total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6259559.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6183645.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6987759.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7602960.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7158964.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>67693</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>q49J1IKaHRwDQnt</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4157.00</td>
      <td>520758.00</td>
    </tr>
    <tr>
      <th>67694</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>rrq4fwE8jgrTyWY</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3931.00</td>
      <td>121131356.00</td>
    </tr>
    <tr>
      <th>67695</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>vOuJvMaM2sgwLmb</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4322.00</td>
      <td>2427691.00</td>
    </tr>
    <tr>
      <th>67696</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>xMbIugepa2P7lBB</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4218.00</td>
      <td>106896394.00</td>
    </tr>
    <tr>
      <th>67697</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4316.00</td>
      <td>209335741.00</td>
    </tr>
  </tbody>
</table>
<p>136476 rows × 7 columns</p>
</div>



Ahora que tenemos las 2 plantas unidas vamos a hacer lo que se llama un análisis de coherencia, dado que según la documentación kw_dia y kw_total están directamente relacionados con kw_dc y kw_ac.

Vamos a intentar replicar los datos de kw_dia y kw_total.


```python
gener2 = gener.copy()
```

Creamos una variable date para poder agregar por ella.


```python
gener2['date'] = gener2.fecha.dt.date
gener2
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
      <th>fecha</th>
      <th>planta</th>
      <th>inverter_id</th>
      <th>kw_dc</th>
      <th>kw_ac</th>
      <th>kw_dia</th>
      <th>kw_total</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6259559.00</td>
      <td>2020-05-15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6183645.00</td>
      <td>2020-05-15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6987759.00</td>
      <td>2020-05-15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7602960.00</td>
      <td>2020-05-15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7158964.00</td>
      <td>2020-05-15</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>67693</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>q49J1IKaHRwDQnt</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4157.00</td>
      <td>520758.00</td>
      <td>2020-06-17</td>
    </tr>
    <tr>
      <th>67694</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>rrq4fwE8jgrTyWY</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3931.00</td>
      <td>121131356.00</td>
      <td>2020-06-17</td>
    </tr>
    <tr>
      <th>67695</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>vOuJvMaM2sgwLmb</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4322.00</td>
      <td>2427691.00</td>
      <td>2020-06-17</td>
    </tr>
    <tr>
      <th>67696</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>xMbIugepa2P7lBB</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4218.00</td>
      <td>106896394.00</td>
      <td>2020-06-17</td>
    </tr>
    <tr>
      <th>67697</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4316.00</td>
      <td>209335741.00</td>
      <td>2020-06-17</td>
    </tr>
  </tbody>
</table>
<p>136476 rows × 8 columns</p>
</div>



La suma por planta, date e inverter de kw_dc o de kw_ac debería coincidir con el máximo de kw_dia.


```python
gener2 = gener2.groupby(['planta','date','inverter_id']).agg({'kw_dc':sum,
                                                              'kw_ac':sum,
                                                              'kw_dia':max,
                                                              'kw_total':max}).reset_index()
gener2
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
      <th>planta</th>
      <th>date</th>
      <th>inverter_id</th>
      <th>kw_dc</th>
      <th>kw_ac</th>
      <th>kw_dia</th>
      <th>kw_total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>p1</td>
      <td>2020-05-15</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>235340.70</td>
      <td>23046.55</td>
      <td>5754.00</td>
      <td>6265313.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>p1</td>
      <td>2020-05-15</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>258911.11</td>
      <td>25343.29</td>
      <td>6357.00</td>
      <td>6190002.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>p1</td>
      <td>2020-05-15</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>254766.05</td>
      <td>24937.70</td>
      <td>6274.00</td>
      <td>6994033.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>p1</td>
      <td>2020-05-15</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>250608.34</td>
      <td>24533.91</td>
      <td>6116.00</td>
      <td>7609076.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>p1</td>
      <td>2020-05-15</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>264030.98</td>
      <td>25840.63</td>
      <td>6471.00</td>
      <td>7165435.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>p2</td>
      <td>2020-06-17</td>
      <td>q49J1IKaHRwDQnt</td>
      <td>17001.51</td>
      <td>16655.15</td>
      <td>4157.00</td>
      <td>520758.00</td>
    </tr>
    <tr>
      <th>1460</th>
      <td>p2</td>
      <td>2020-06-17</td>
      <td>rrq4fwE8jgrTyWY</td>
      <td>16073.93</td>
      <td>15748.92</td>
      <td>3931.00</td>
      <td>121131356.00</td>
    </tr>
    <tr>
      <th>1461</th>
      <td>p2</td>
      <td>2020-06-17</td>
      <td>vOuJvMaM2sgwLmb</td>
      <td>17710.00</td>
      <td>17345.44</td>
      <td>4322.00</td>
      <td>2427691.00</td>
    </tr>
    <tr>
      <th>1462</th>
      <td>p2</td>
      <td>2020-06-17</td>
      <td>xMbIugepa2P7lBB</td>
      <td>17211.23</td>
      <td>16860.38</td>
      <td>5502.00</td>
      <td>106896394.00</td>
    </tr>
    <tr>
      <th>1463</th>
      <td>p2</td>
      <td>2020-06-17</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>17640.42</td>
      <td>17278.51</td>
      <td>5327.00</td>
      <td>209335741.00</td>
    </tr>
  </tbody>
</table>
<p>1464 rows × 7 columns</p>
</div>



Ordenamos para poder analizar.


```python
gener2 = gener2.sort_values(['planta','inverter_id','date'])
gener2
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
      <th>planta</th>
      <th>date</th>
      <th>inverter_id</th>
      <th>kw_dc</th>
      <th>kw_ac</th>
      <th>kw_dia</th>
      <th>kw_total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>p1</td>
      <td>2020-05-15</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>235340.70</td>
      <td>23046.55</td>
      <td>5754.00</td>
      <td>6265313.00</td>
    </tr>
    <tr>
      <th>22</th>
      <td>p1</td>
      <td>2020-05-16</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>256629.88</td>
      <td>25124.49</td>
      <td>6292.00</td>
      <td>6271605.00</td>
    </tr>
    <tr>
      <th>44</th>
      <td>p1</td>
      <td>2020-05-17</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>288039.82</td>
      <td>28172.85</td>
      <td>7045.00</td>
      <td>6278650.00</td>
    </tr>
    <tr>
      <th>66</th>
      <td>p1</td>
      <td>2020-05-18</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>204030.30</td>
      <td>19970.51</td>
      <td>4998.00</td>
      <td>6283648.00</td>
    </tr>
    <tr>
      <th>88</th>
      <td>p1</td>
      <td>2020-05-19</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>232277.27</td>
      <td>22741.18</td>
      <td>6449.00</td>
      <td>6290097.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1375</th>
      <td>p2</td>
      <td>2020-06-13</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>27443.74</td>
      <td>26840.58</td>
      <td>6632.00</td>
      <td>209312200.00</td>
    </tr>
    <tr>
      <th>1397</th>
      <td>p2</td>
      <td>2020-06-14</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>30768.78</td>
      <td>30088.97</td>
      <td>7268.00</td>
      <td>209319687.00</td>
    </tr>
    <tr>
      <th>1419</th>
      <td>p2</td>
      <td>2020-06-15</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>25597.24</td>
      <td>25049.49</td>
      <td>7412.67</td>
      <td>209325949.00</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>p2</td>
      <td>2020-06-16</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>22335.69</td>
      <td>21870.63</td>
      <td>6203.20</td>
      <td>209331425.00</td>
    </tr>
    <tr>
      <th>1463</th>
      <td>p2</td>
      <td>2020-06-17</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>17640.42</td>
      <td>17278.51</td>
      <td>5327.00</td>
      <td>209335741.00</td>
    </tr>
  </tbody>
</table>
<p>1464 rows × 7 columns</p>
</div>



Kw_dia no concuerda para nada ni con kw_dc ni con kw_ac.

Vamos a ver si concuerda con kw_total, para ello calculamos el incremento diario de kw_total que debería coincidir con el máximo de kw_dia del día anterior.


```python
gener2['lag1'] = gener2.groupby(['planta','inverter_id']).kw_total.shift(1)
gener2['incremento'] = gener2.kw_total - gener2.lag1
gener2
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
      <th>planta</th>
      <th>date</th>
      <th>inverter_id</th>
      <th>kw_dc</th>
      <th>kw_ac</th>
      <th>kw_dia</th>
      <th>kw_total</th>
      <th>lag1</th>
      <th>incremento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>p1</td>
      <td>2020-05-15</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>235340.70</td>
      <td>23046.55</td>
      <td>5754.00</td>
      <td>6265313.00</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>p1</td>
      <td>2020-05-16</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>256629.88</td>
      <td>25124.49</td>
      <td>6292.00</td>
      <td>6271605.00</td>
      <td>6265313.00</td>
      <td>6292.00</td>
    </tr>
    <tr>
      <th>44</th>
      <td>p1</td>
      <td>2020-05-17</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>288039.82</td>
      <td>28172.85</td>
      <td>7045.00</td>
      <td>6278650.00</td>
      <td>6271605.00</td>
      <td>7045.00</td>
    </tr>
    <tr>
      <th>66</th>
      <td>p1</td>
      <td>2020-05-18</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>204030.30</td>
      <td>19970.51</td>
      <td>4998.00</td>
      <td>6283648.00</td>
      <td>6278650.00</td>
      <td>4998.00</td>
    </tr>
    <tr>
      <th>88</th>
      <td>p1</td>
      <td>2020-05-19</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>232277.27</td>
      <td>22741.18</td>
      <td>6449.00</td>
      <td>6290097.00</td>
      <td>6283648.00</td>
      <td>6449.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1375</th>
      <td>p2</td>
      <td>2020-06-13</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>27443.74</td>
      <td>26840.58</td>
      <td>6632.00</td>
      <td>209312200.00</td>
      <td>209305520.00</td>
      <td>6680.00</td>
    </tr>
    <tr>
      <th>1397</th>
      <td>p2</td>
      <td>2020-06-14</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>30768.78</td>
      <td>30088.97</td>
      <td>7268.00</td>
      <td>209319687.00</td>
      <td>209312200.00</td>
      <td>7487.00</td>
    </tr>
    <tr>
      <th>1419</th>
      <td>p2</td>
      <td>2020-06-15</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>25597.24</td>
      <td>25049.49</td>
      <td>7412.67</td>
      <td>209325949.00</td>
      <td>209319687.00</td>
      <td>6262.00</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>p2</td>
      <td>2020-06-16</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>22335.69</td>
      <td>21870.63</td>
      <td>6203.20</td>
      <td>209331425.00</td>
      <td>209325949.00</td>
      <td>5476.00</td>
    </tr>
    <tr>
      <th>1463</th>
      <td>p2</td>
      <td>2020-06-17</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>17640.42</td>
      <td>17278.51</td>
      <td>5327.00</td>
      <td>209335741.00</td>
      <td>209331425.00</td>
      <td>4316.00</td>
    </tr>
  </tbody>
</table>
<p>1464 rows × 9 columns</p>
</div>



Comprobamos en la planta 1.


```python
gener2[gener2.planta == 'p1'].head(50)
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
      <th>planta</th>
      <th>date</th>
      <th>inverter_id</th>
      <th>kw_dc</th>
      <th>kw_ac</th>
      <th>kw_dia</th>
      <th>kw_total</th>
      <th>lag1</th>
      <th>incremento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>p1</td>
      <td>2020-05-15</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>235340.70</td>
      <td>23046.55</td>
      <td>5754.00</td>
      <td>6265313.00</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>p1</td>
      <td>2020-05-16</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>256629.88</td>
      <td>25124.49</td>
      <td>6292.00</td>
      <td>6271605.00</td>
      <td>6265313.00</td>
      <td>6292.00</td>
    </tr>
    <tr>
      <th>44</th>
      <td>p1</td>
      <td>2020-05-17</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>288039.82</td>
      <td>28172.85</td>
      <td>7045.00</td>
      <td>6278650.00</td>
      <td>6271605.00</td>
      <td>7045.00</td>
    </tr>
    <tr>
      <th>66</th>
      <td>p1</td>
      <td>2020-05-18</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>204030.30</td>
      <td>19970.51</td>
      <td>4998.00</td>
      <td>6283648.00</td>
      <td>6278650.00</td>
      <td>4998.00</td>
    </tr>
    <tr>
      <th>88</th>
      <td>p1</td>
      <td>2020-05-19</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>232277.27</td>
      <td>22741.18</td>
      <td>6449.00</td>
      <td>6290097.00</td>
      <td>6283648.00</td>
      <td>6449.00</td>
    </tr>
    <tr>
      <th>110</th>
      <td>p1</td>
      <td>2020-05-20</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>230412.62</td>
      <td>22516.26</td>
      <td>8249.00</td>
      <td>6298346.00</td>
      <td>6290097.00</td>
      <td>8249.00</td>
    </tr>
    <tr>
      <th>132</th>
      <td>p1</td>
      <td>2020-05-21</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>288676.60</td>
      <td>28223.13</td>
      <td>7243.00</td>
      <td>6305589.00</td>
      <td>6298346.00</td>
      <td>7243.00</td>
    </tr>
    <tr>
      <th>154</th>
      <td>p1</td>
      <td>2020-05-22</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>280809.07</td>
      <td>27456.63</td>
      <td>6848.00</td>
      <td>6312437.00</td>
      <td>6305589.00</td>
      <td>6848.00</td>
    </tr>
    <tr>
      <th>176</th>
      <td>p1</td>
      <td>2020-05-23</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>326468.27</td>
      <td>31922.93</td>
      <td>7966.00</td>
      <td>6320403.00</td>
      <td>6312437.00</td>
      <td>7966.00</td>
    </tr>
    <tr>
      <th>198</th>
      <td>p1</td>
      <td>2020-05-24</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>309111.73</td>
      <td>30220.37</td>
      <td>7537.00</td>
      <td>6327940.00</td>
      <td>6320403.00</td>
      <td>7537.00</td>
    </tr>
    <tr>
      <th>220</th>
      <td>p1</td>
      <td>2020-05-25</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>339109.95</td>
      <td>33144.65</td>
      <td>8268.00</td>
      <td>6336208.00</td>
      <td>6327940.00</td>
      <td>8268.00</td>
    </tr>
    <tr>
      <th>242</th>
      <td>p1</td>
      <td>2020-05-26</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>305515.95</td>
      <td>29873.74</td>
      <td>7456.43</td>
      <td>6343669.00</td>
      <td>6336208.00</td>
      <td>7461.00</td>
    </tr>
    <tr>
      <th>264</th>
      <td>p1</td>
      <td>2020-05-27</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>251250.52</td>
      <td>24595.61</td>
      <td>6164.00</td>
      <td>6349833.00</td>
      <td>6343669.00</td>
      <td>6164.00</td>
    </tr>
    <tr>
      <th>286</th>
      <td>p1</td>
      <td>2020-05-28</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>326520.42</td>
      <td>31917.63</td>
      <td>7977.00</td>
      <td>6357810.00</td>
      <td>6349833.00</td>
      <td>7977.00</td>
    </tr>
    <tr>
      <th>308</th>
      <td>p1</td>
      <td>2020-05-29</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>310776.57</td>
      <td>30387.48</td>
      <td>7564.00</td>
      <td>6365374.00</td>
      <td>6357810.00</td>
      <td>7564.00</td>
    </tr>
    <tr>
      <th>330</th>
      <td>p1</td>
      <td>2020-05-30</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>276466.89</td>
      <td>27054.69</td>
      <td>6754.00</td>
      <td>6372128.00</td>
      <td>6365374.00</td>
      <td>6754.00</td>
    </tr>
    <tr>
      <th>352</th>
      <td>p1</td>
      <td>2020-05-31</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>234509.23</td>
      <td>22928.22</td>
      <td>5803.00</td>
      <td>6377931.00</td>
      <td>6372128.00</td>
      <td>5803.00</td>
    </tr>
    <tr>
      <th>374</th>
      <td>p1</td>
      <td>2020-06-01</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>225219.77</td>
      <td>22033.25</td>
      <td>5508.00</td>
      <td>6383439.00</td>
      <td>6377931.00</td>
      <td>5508.00</td>
    </tr>
    <tr>
      <th>396</th>
      <td>p1</td>
      <td>2020-06-02</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>286633.75</td>
      <td>28043.89</td>
      <td>7029.00</td>
      <td>6390468.00</td>
      <td>6383439.00</td>
      <td>7029.00</td>
    </tr>
    <tr>
      <th>418</th>
      <td>p1</td>
      <td>2020-06-03</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>287069.37</td>
      <td>28085.88</td>
      <td>7341.00</td>
      <td>6397809.00</td>
      <td>6390468.00</td>
      <td>7341.00</td>
    </tr>
    <tr>
      <th>440</th>
      <td>p1</td>
      <td>2020-06-04</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>309653.82</td>
      <td>30287.02</td>
      <td>7571.00</td>
      <td>6405380.00</td>
      <td>6397809.00</td>
      <td>7571.00</td>
    </tr>
    <tr>
      <th>462</th>
      <td>p1</td>
      <td>2020-06-05</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>293353.25</td>
      <td>28693.91</td>
      <td>7162.00</td>
      <td>6412542.00</td>
      <td>6405380.00</td>
      <td>7162.00</td>
    </tr>
    <tr>
      <th>484</th>
      <td>p1</td>
      <td>2020-06-06</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>243297.18</td>
      <td>23793.42</td>
      <td>5940.00</td>
      <td>6418482.00</td>
      <td>6412542.00</td>
      <td>5940.00</td>
    </tr>
    <tr>
      <th>506</th>
      <td>p1</td>
      <td>2020-06-07</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>217217.71</td>
      <td>21247.58</td>
      <td>5268.00</td>
      <td>6423750.00</td>
      <td>6418482.00</td>
      <td>5268.00</td>
    </tr>
    <tr>
      <th>528</th>
      <td>p1</td>
      <td>2020-06-08</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>316710.85</td>
      <td>30969.72</td>
      <td>7864.00</td>
      <td>6431614.00</td>
      <td>6423750.00</td>
      <td>7864.00</td>
    </tr>
    <tr>
      <th>550</th>
      <td>p1</td>
      <td>2020-06-09</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>301395.46</td>
      <td>29476.87</td>
      <td>7456.00</td>
      <td>6439070.00</td>
      <td>6431614.00</td>
      <td>7456.00</td>
    </tr>
    <tr>
      <th>572</th>
      <td>p1</td>
      <td>2020-06-10</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>242187.71</td>
      <td>23707.68</td>
      <td>5911.00</td>
      <td>6444981.00</td>
      <td>6439070.00</td>
      <td>5911.00</td>
    </tr>
    <tr>
      <th>594</th>
      <td>p1</td>
      <td>2020-06-11</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>214404.59</td>
      <td>21003.57</td>
      <td>5257.00</td>
      <td>6450238.00</td>
      <td>6444981.00</td>
      <td>5257.00</td>
    </tr>
    <tr>
      <th>616</th>
      <td>p1</td>
      <td>2020-06-12</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>222758.55</td>
      <td>21813.00</td>
      <td>5441.00</td>
      <td>6455679.00</td>
      <td>6450238.00</td>
      <td>5441.00</td>
    </tr>
    <tr>
      <th>638</th>
      <td>p1</td>
      <td>2020-06-13</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>326297.09</td>
      <td>31895.25</td>
      <td>7984.00</td>
      <td>6463663.00</td>
      <td>6455679.00</td>
      <td>7984.00</td>
    </tr>
    <tr>
      <th>660</th>
      <td>p1</td>
      <td>2020-06-14</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>164127.30</td>
      <td>16085.33</td>
      <td>4012.00</td>
      <td>6467675.00</td>
      <td>6463663.00</td>
      <td>4012.00</td>
    </tr>
    <tr>
      <th>682</th>
      <td>p1</td>
      <td>2020-06-15</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>255298.41</td>
      <td>24986.86</td>
      <td>6275.00</td>
      <td>6473950.00</td>
      <td>6467675.00</td>
      <td>6275.00</td>
    </tr>
    <tr>
      <th>704</th>
      <td>p1</td>
      <td>2020-06-16</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>237829.61</td>
      <td>23288.02</td>
      <td>5848.00</td>
      <td>6479798.00</td>
      <td>6473950.00</td>
      <td>5848.00</td>
    </tr>
    <tr>
      <th>726</th>
      <td>p1</td>
      <td>2020-06-17</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>224315.74</td>
      <td>21957.17</td>
      <td>5521.00</td>
      <td>6485319.00</td>
      <td>6479798.00</td>
      <td>5521.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>p1</td>
      <td>2020-05-15</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>258911.11</td>
      <td>25343.29</td>
      <td>6357.00</td>
      <td>6190002.00</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>p1</td>
      <td>2020-05-16</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>269678.23</td>
      <td>26396.93</td>
      <td>6592.00</td>
      <td>6196594.00</td>
      <td>6190002.00</td>
      <td>6592.00</td>
    </tr>
    <tr>
      <th>45</th>
      <td>p1</td>
      <td>2020-05-17</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>316701.61</td>
      <td>30962.51</td>
      <td>7759.00</td>
      <td>6204353.00</td>
      <td>6196594.00</td>
      <td>7759.00</td>
    </tr>
    <tr>
      <th>67</th>
      <td>p1</td>
      <td>2020-05-18</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>221984.75</td>
      <td>21723.95</td>
      <td>5453.00</td>
      <td>6209806.00</td>
      <td>6204353.00</td>
      <td>5453.00</td>
    </tr>
    <tr>
      <th>89</th>
      <td>p1</td>
      <td>2020-05-19</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>237092.43</td>
      <td>23202.78</td>
      <td>6568.75</td>
      <td>6216430.00</td>
      <td>6209806.00</td>
      <td>6624.00</td>
    </tr>
    <tr>
      <th>111</th>
      <td>p1</td>
      <td>2020-05-20</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>251521.07</td>
      <td>24564.96</td>
      <td>8997.00</td>
      <td>6225427.00</td>
      <td>6216430.00</td>
      <td>8997.00</td>
    </tr>
    <tr>
      <th>133</th>
      <td>p1</td>
      <td>2020-05-21</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>310547.48</td>
      <td>30352.05</td>
      <td>7816.50</td>
      <td>6233247.00</td>
      <td>6225427.00</td>
      <td>7820.00</td>
    </tr>
    <tr>
      <th>155</th>
      <td>p1</td>
      <td>2020-05-22</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>296998.09</td>
      <td>29011.33</td>
      <td>7287.00</td>
      <td>6240534.00</td>
      <td>6233247.00</td>
      <td>7287.00</td>
    </tr>
    <tr>
      <th>177</th>
      <td>p1</td>
      <td>2020-05-23</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>355283.96</td>
      <td>34726.34</td>
      <td>8673.00</td>
      <td>6249207.00</td>
      <td>6240534.00</td>
      <td>8673.00</td>
    </tr>
    <tr>
      <th>199</th>
      <td>p1</td>
      <td>2020-05-24</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>339436.82</td>
      <td>33170.41</td>
      <td>8273.00</td>
      <td>6257480.00</td>
      <td>6249207.00</td>
      <td>8273.00</td>
    </tr>
    <tr>
      <th>221</th>
      <td>p1</td>
      <td>2020-05-25</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>371166.75</td>
      <td>36249.54</td>
      <td>9048.00</td>
      <td>6266528.00</td>
      <td>6257480.00</td>
      <td>9048.00</td>
    </tr>
    <tr>
      <th>243</th>
      <td>p1</td>
      <td>2020-05-26</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>332953.20</td>
      <td>32544.54</td>
      <td>8109.50</td>
      <td>6274638.00</td>
      <td>6266528.00</td>
      <td>8110.00</td>
    </tr>
    <tr>
      <th>265</th>
      <td>p1</td>
      <td>2020-05-27</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>279934.18</td>
      <td>27390.71</td>
      <td>6824.00</td>
      <td>6281462.00</td>
      <td>6274638.00</td>
      <td>6824.00</td>
    </tr>
    <tr>
      <th>287</th>
      <td>p1</td>
      <td>2020-05-28</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>348916.90</td>
      <td>34097.52</td>
      <td>8496.00</td>
      <td>6289958.00</td>
      <td>6281462.00</td>
      <td>8496.00</td>
    </tr>
    <tr>
      <th>309</th>
      <td>p1</td>
      <td>2020-05-29</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>338805.39</td>
      <td>33116.10</td>
      <td>8253.00</td>
      <td>6298211.00</td>
      <td>6289958.00</td>
      <td>8253.00</td>
    </tr>
    <tr>
      <th>331</th>
      <td>p1</td>
      <td>2020-05-30</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>300749.29</td>
      <td>29414.52</td>
      <td>7332.00</td>
      <td>6305543.00</td>
      <td>6298211.00</td>
      <td>7332.00</td>
    </tr>
  </tbody>
</table>
</div>



Comprobamos en la planta 2.


```python
gener2[gener2.planta == 'p2'].head(50)
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
      <th>planta</th>
      <th>date</th>
      <th>inverter_id</th>
      <th>kw_dc</th>
      <th>kw_ac</th>
      <th>kw_dia</th>
      <th>kw_total</th>
      <th>lag1</th>
      <th>incremento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>748</th>
      <td>p2</td>
      <td>2020-05-15</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>17112.65</td>
      <td>16744.08</td>
      <td>9425.00</td>
      <td>2433212.00</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>770</th>
      <td>p2</td>
      <td>2020-05-16</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>23305.45</td>
      <td>22791.22</td>
      <td>5677.00</td>
      <td>2438889.00</td>
      <td>2433212.00</td>
      <td>5677.00</td>
    </tr>
    <tr>
      <th>792</th>
      <td>p2</td>
      <td>2020-05-17</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>25985.95</td>
      <td>25430.42</td>
      <td>6342.00</td>
      <td>2445231.00</td>
      <td>2438889.00</td>
      <td>6342.00</td>
    </tr>
    <tr>
      <th>814</th>
      <td>p2</td>
      <td>2020-05-18</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>31218.58</td>
      <td>30516.03</td>
      <td>7641.00</td>
      <td>2452872.00</td>
      <td>2445231.00</td>
      <td>7641.00</td>
    </tr>
    <tr>
      <th>836</th>
      <td>p2</td>
      <td>2020-05-19</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>8040.00</td>
      <td>7878.39</td>
      <td>7641.00</td>
      <td>2454841.00</td>
      <td>2452872.00</td>
      <td>1969.00</td>
    </tr>
    <tr>
      <th>858</th>
      <td>p2</td>
      <td>2020-05-20</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>9852.13</td>
      <td>9641.35</td>
      <td>9423.00</td>
      <td>2464264.00</td>
      <td>2454841.00</td>
      <td>9423.00</td>
    </tr>
    <tr>
      <th>880</th>
      <td>p2</td>
      <td>2020-05-21</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>37403.77</td>
      <td>36540.63</td>
      <td>9423.00</td>
      <td>2473415.00</td>
      <td>2464264.00</td>
      <td>9151.00</td>
    </tr>
    <tr>
      <th>898</th>
      <td>p2</td>
      <td>2020-05-22</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>40414.35</td>
      <td>39472.14</td>
      <td>9863.00</td>
      <td>2483278.00</td>
      <td>2473415.00</td>
      <td>9863.00</td>
    </tr>
    <tr>
      <th>916</th>
      <td>p2</td>
      <td>2020-05-23</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>39690.66</td>
      <td>38769.69</td>
      <td>9863.00</td>
      <td>2492966.00</td>
      <td>2483278.00</td>
      <td>9688.00</td>
    </tr>
    <tr>
      <th>934</th>
      <td>p2</td>
      <td>2020-05-24</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>18963.72</td>
      <td>18558.18</td>
      <td>9688.00</td>
      <td>2497601.00</td>
      <td>2492966.00</td>
      <td>4635.00</td>
    </tr>
    <tr>
      <th>952</th>
      <td>p2</td>
      <td>2020-05-25</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>37659.21</td>
      <td>36789.31</td>
      <td>9224.00</td>
      <td>2506825.00</td>
      <td>2497601.00</td>
      <td>9224.00</td>
    </tr>
    <tr>
      <th>970</th>
      <td>p2</td>
      <td>2020-05-26</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>38900.22</td>
      <td>37995.67</td>
      <td>9501.00</td>
      <td>2516326.00</td>
      <td>2506825.00</td>
      <td>9501.00</td>
    </tr>
    <tr>
      <th>988</th>
      <td>p2</td>
      <td>2020-05-27</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>38919.76</td>
      <td>38017.83</td>
      <td>9501.00</td>
      <td>2525827.00</td>
      <td>2516326.00</td>
      <td>9501.00</td>
    </tr>
    <tr>
      <th>1006</th>
      <td>p2</td>
      <td>2020-05-28</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>15261.36</td>
      <td>14937.97</td>
      <td>9501.00</td>
      <td>2529556.00</td>
      <td>2525827.00</td>
      <td>3729.00</td>
    </tr>
    <tr>
      <th>1024</th>
      <td>p2</td>
      <td>2020-05-29</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>32521.41</td>
      <td>31811.48</td>
      <td>8126.00</td>
      <td>2537682.00</td>
      <td>2529556.00</td>
      <td>8126.00</td>
    </tr>
    <tr>
      <th>1046</th>
      <td>p2</td>
      <td>2020-05-30</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>33420.25</td>
      <td>32663.54</td>
      <td>8185.00</td>
      <td>2545867.00</td>
      <td>2537682.00</td>
      <td>8185.00</td>
    </tr>
    <tr>
      <th>1068</th>
      <td>p2</td>
      <td>2020-05-31</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>27317.90</td>
      <td>26701.78</td>
      <td>8185.00</td>
      <td>2552559.00</td>
      <td>2545867.00</td>
      <td>6692.00</td>
    </tr>
    <tr>
      <th>1090</th>
      <td>p2</td>
      <td>2020-06-01</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>17867.74</td>
      <td>17462.72</td>
      <td>6692.00</td>
      <td>2556897.00</td>
      <td>2552559.00</td>
      <td>4338.00</td>
    </tr>
    <tr>
      <th>1112</th>
      <td>p2</td>
      <td>2020-06-02</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>30176.94</td>
      <td>29508.22</td>
      <td>7404.00</td>
      <td>2564301.00</td>
      <td>2556897.00</td>
      <td>7404.00</td>
    </tr>
    <tr>
      <th>1134</th>
      <td>p2</td>
      <td>2020-06-03</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>23834.47</td>
      <td>23319.73</td>
      <td>7404.00</td>
      <td>2570414.00</td>
      <td>2564301.00</td>
      <td>6113.00</td>
    </tr>
    <tr>
      <th>1156</th>
      <td>p2</td>
      <td>2020-06-04</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>28736.11</td>
      <td>28109.01</td>
      <td>6990.00</td>
      <td>2577404.00</td>
      <td>2570414.00</td>
      <td>6990.00</td>
    </tr>
    <tr>
      <th>1178</th>
      <td>p2</td>
      <td>2020-06-05</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>31594.37</td>
      <td>30884.49</td>
      <td>7756.00</td>
      <td>2585160.00</td>
      <td>2577404.00</td>
      <td>7756.00</td>
    </tr>
    <tr>
      <th>1200</th>
      <td>p2</td>
      <td>2020-06-06</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>34226.22</td>
      <td>33435.09</td>
      <td>8376.00</td>
      <td>2593536.00</td>
      <td>2585160.00</td>
      <td>8376.00</td>
    </tr>
    <tr>
      <th>1222</th>
      <td>p2</td>
      <td>2020-06-07</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>32026.91</td>
      <td>31285.99</td>
      <td>8376.00</td>
      <td>2601362.00</td>
      <td>2593536.00</td>
      <td>7826.00</td>
    </tr>
    <tr>
      <th>1244</th>
      <td>p2</td>
      <td>2020-06-08</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>37814.61</td>
      <td>36940.31</td>
      <td>9210.00</td>
      <td>2610588.00</td>
      <td>2601362.00</td>
      <td>9226.00</td>
    </tr>
    <tr>
      <th>1266</th>
      <td>p2</td>
      <td>2020-06-09</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>33205.47</td>
      <td>32465.97</td>
      <td>9217.93</td>
      <td>2618699.00</td>
      <td>2610588.00</td>
      <td>8111.00</td>
    </tr>
    <tr>
      <th>1288</th>
      <td>p2</td>
      <td>2020-06-10</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>22793.26</td>
      <td>22291.98</td>
      <td>8098.00</td>
      <td>2624287.00</td>
      <td>2618699.00</td>
      <td>5588.00</td>
    </tr>
    <tr>
      <th>1310</th>
      <td>p2</td>
      <td>2020-06-11</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>16069.58</td>
      <td>15745.07</td>
      <td>5588.00</td>
      <td>2628220.00</td>
      <td>2624287.00</td>
      <td>3933.00</td>
    </tr>
    <tr>
      <th>1332</th>
      <td>p2</td>
      <td>2020-06-12</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>18684.47</td>
      <td>18306.11</td>
      <td>4548.00</td>
      <td>2632794.00</td>
      <td>2628220.00</td>
      <td>4574.00</td>
    </tr>
    <tr>
      <th>1354</th>
      <td>p2</td>
      <td>2020-06-13</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>25901.76</td>
      <td>25335.74</td>
      <td>6289.00</td>
      <td>2639150.00</td>
      <td>2632794.00</td>
      <td>6356.00</td>
    </tr>
    <tr>
      <th>1376</th>
      <td>p2</td>
      <td>2020-06-14</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>8863.51</td>
      <td>8699.19</td>
      <td>6462.80</td>
      <td>2641320.00</td>
      <td>2639150.00</td>
      <td>2170.00</td>
    </tr>
    <tr>
      <th>1398</th>
      <td>p2</td>
      <td>2020-06-15</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>10205.79</td>
      <td>9999.45</td>
      <td>2304.00</td>
      <td>2643840.00</td>
      <td>2641320.00</td>
      <td>2520.00</td>
    </tr>
    <tr>
      <th>1420</th>
      <td>p2</td>
      <td>2020-06-16</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>21302.43</td>
      <td>20858.99</td>
      <td>5004.00</td>
      <td>2649049.00</td>
      <td>2643840.00</td>
      <td>5209.00</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>p2</td>
      <td>2020-06-17</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>18153.88</td>
      <td>17780.37</td>
      <td>5004.00</td>
      <td>2653495.00</td>
      <td>2649049.00</td>
      <td>4446.00</td>
    </tr>
    <tr>
      <th>749</th>
      <td>p2</td>
      <td>2020-05-15</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>13169.45</td>
      <td>12896.82</td>
      <td>3214.00</td>
      <td>1215281950.00</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>771</th>
      <td>p2</td>
      <td>2020-05-16</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>19238.71</td>
      <td>18812.08</td>
      <td>4857.00</td>
      <td>1215286807.00</td>
      <td>1215281950.00</td>
      <td>4857.00</td>
    </tr>
    <tr>
      <th>793</th>
      <td>p2</td>
      <td>2020-05-17</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>23577.93</td>
      <td>23078.49</td>
      <td>5758.00</td>
      <td>1215292565.00</td>
      <td>1215286807.00</td>
      <td>5758.00</td>
    </tr>
    <tr>
      <th>815</th>
      <td>p2</td>
      <td>2020-05-18</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>14117.46</td>
      <td>13820.30</td>
      <td>3485.00</td>
      <td>1215296050.00</td>
      <td>1215292565.00</td>
      <td>3485.00</td>
    </tr>
    <tr>
      <th>837</th>
      <td>p2</td>
      <td>2020-05-19</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>27893.17</td>
      <td>27253.87</td>
      <td>6771.00</td>
      <td>1215302821.00</td>
      <td>1215296050.00</td>
      <td>6771.00</td>
    </tr>
    <tr>
      <th>859</th>
      <td>p2</td>
      <td>2020-05-20</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>14040.81</td>
      <td>13748.34</td>
      <td>3439.00</td>
      <td>1215306260.00</td>
      <td>1215302821.00</td>
      <td>3439.00</td>
    </tr>
    <tr>
      <th>881</th>
      <td>p2</td>
      <td>2020-05-21</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>29804.31</td>
      <td>29105.05</td>
      <td>8570.00</td>
      <td>1215314830.00</td>
      <td>1215306260.00</td>
      <td>8570.00</td>
    </tr>
    <tr>
      <th>899</th>
      <td>p2</td>
      <td>2020-05-22</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>13268.32</td>
      <td>12992.02</td>
      <td>3269.00</td>
      <td>1215318099.00</td>
      <td>1215314830.00</td>
      <td>3269.00</td>
    </tr>
    <tr>
      <th>917</th>
      <td>p2</td>
      <td>2020-05-23</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>27742.32</td>
      <td>27098.60</td>
      <td>9333.00</td>
      <td>1215327432.00</td>
      <td>1215318099.00</td>
      <td>9333.00</td>
    </tr>
    <tr>
      <th>935</th>
      <td>p2</td>
      <td>2020-05-24</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>15849.25</td>
      <td>15512.54</td>
      <td>9100.00</td>
      <td>1215336532.00</td>
      <td>1215327432.00</td>
      <td>9100.00</td>
    </tr>
    <tr>
      <th>953</th>
      <td>p2</td>
      <td>2020-05-25</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>35834.31</td>
      <td>35018.35</td>
      <td>8860.00</td>
      <td>1215345392.00</td>
      <td>1215336532.00</td>
      <td>8860.00</td>
    </tr>
    <tr>
      <th>971</th>
      <td>p2</td>
      <td>2020-05-26</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>14655.46</td>
      <td>14326.96</td>
      <td>3212.67</td>
      <td>1215348540.93</td>
      <td>1215345392.00</td>
      <td>3148.93</td>
    </tr>
    <tr>
      <th>989</th>
      <td>p2</td>
      <td>2020-05-27</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>5380.56</td>
      <td>5270.20</td>
      <td>9138.00</td>
      <td>1215363661.00</td>
      <td>1215348540.93</td>
      <td>15120.07</td>
    </tr>
    <tr>
      <th>1007</th>
      <td>p2</td>
      <td>2020-05-28</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>36201.81</td>
      <td>35369.55</td>
      <td>8947.00</td>
      <td>1215372608.00</td>
      <td>1215363661.00</td>
      <td>8947.00</td>
    </tr>
    <tr>
      <th>1025</th>
      <td>p2</td>
      <td>2020-05-29</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>18928.49</td>
      <td>18527.04</td>
      <td>4812.00</td>
      <td>1215377420.00</td>
      <td>1215372608.00</td>
      <td>4812.00</td>
    </tr>
    <tr>
      <th>1047</th>
      <td>p2</td>
      <td>2020-05-30</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>29388.91</td>
      <td>28733.23</td>
      <td>7156.00</td>
      <td>1215384576.00</td>
      <td>1215377420.00</td>
      <td>7156.00</td>
    </tr>
  </tbody>
</table>
</div>



Conclusiones:
* kw_dia tiene coherencia con kw_total
* pero éstas no tienen coherencia con kw_dc ni con kw_ac
* es como si estuvieran en diferentes unidades o hubiera algún cálculo del que no somos conscientes
* por tanto tendremos 2 bloques a poder usar: o bien kw_dc con kw_ac, o bien kw_dia con kw_total, pero no podemos mezclarlas entre sí

### Unión de los datasets de mediciones ambientales


```python
temper = pd.concat([p1w,p2w], axis = 'index')
temper
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
      <th>DATE_TIME</th>
      <th>PLANT_ID</th>
      <th>SOURCE_KEY</th>
      <th>AMBIENT_TEMPERATURE</th>
      <th>MODULE_TEMPERATURE</th>
      <th>IRRADIATION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:15:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.08</td>
      <td>22.76</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:30:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.94</td>
      <td>22.59</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:45:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.85</td>
      <td>22.36</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 01:00:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.62</td>
      <td>22.17</td>
      <td>0.00</td>
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
      <th>3254</th>
      <td>2020-06-17 22:45:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.51</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3255</th>
      <td>2020-06-17 23:00:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.48</td>
      <td>22.74</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3256</th>
      <td>2020-06-17 23:15:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.35</td>
      <td>22.49</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3257</th>
      <td>2020-06-17 23:30:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.29</td>
      <td>22.37</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3258</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>6441 rows × 6 columns</p>
</div>



Vamos a renombrar ya las variables para hacerlas más descriptivas y usables.


```python
temper.columns = ['fecha','planta','sensor_id','t_ambiente','t_modulo','irradiacion']
temper
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
      <th>fecha</th>
      <th>planta</th>
      <th>sensor_id</th>
      <th>t_ambiente</th>
      <th>t_modulo</th>
      <th>irradiacion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:15:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.08</td>
      <td>22.76</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:30:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.94</td>
      <td>22.59</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:45:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.85</td>
      <td>22.36</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 01:00:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>24.62</td>
      <td>22.17</td>
      <td>0.00</td>
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
      <th>3254</th>
      <td>2020-06-17 22:45:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.51</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3255</th>
      <td>2020-06-17 23:00:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.48</td>
      <td>22.74</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3256</th>
      <td>2020-06-17 23:15:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.35</td>
      <td>22.49</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3257</th>
      <td>2020-06-17 23:30:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.29</td>
      <td>22.37</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3258</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>6441 rows × 6 columns</p>
</div>



### Creación del datamart analitico

En este caso el campo clave es compuesto de fecha y planta y manda el dataset de generación, ya que el de temperatura solo nos aporta variables adicionales.


```python
df = pd.merge(left = gener, right = temper, how = 'left', on = ['fecha','planta'])
df
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
      <th>fecha</th>
      <th>planta</th>
      <th>inverter_id</th>
      <th>kw_dc</th>
      <th>kw_ac</th>
      <th>kw_dia</th>
      <th>kw_total</th>
      <th>sensor_id</th>
      <th>t_ambiente</th>
      <th>t_modulo</th>
      <th>irradiacion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6259559.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6183645.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6987759.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7602960.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7158964.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>136471</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>q49J1IKaHRwDQnt</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4157.00</td>
      <td>520758.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>136472</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>rrq4fwE8jgrTyWY</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3931.00</td>
      <td>121131356.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>136473</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>vOuJvMaM2sgwLmb</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4322.00</td>
      <td>2427691.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>136474</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>xMbIugepa2P7lBB</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4218.00</td>
      <td>106896394.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>136475</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4316.00</td>
      <td>209335741.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>136476 rows × 11 columns</p>
</div>



Tras una integración siempre es conveniente comprobar si se han generado nulos.


```python
df.isna().sum()
```




    fecha          0
    planta         0
    inverter_id    0
    kw_dc          0
    kw_ac          0
    kw_dia         0
    kw_total       0
    sensor_id      4
    t_ambiente     4
    t_modulo       4
    irradiacion    4
    dtype: int64



Buscamos si los nulos cumplen algún patrón.


```python
nulos = df[df.sensor_id.isna()]
nulos
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
      <th>fecha</th>
      <th>planta</th>
      <th>inverter_id</th>
      <th>kw_dc</th>
      <th>kw_ac</th>
      <th>kw_dia</th>
      <th>kw_total</th>
      <th>sensor_id</th>
      <th>t_ambiente</th>
      <th>t_modulo</th>
      <th>irradiacion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>38544</th>
      <td>2020-06-03 14:00:00</td>
      <td>p1</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>7003.00</td>
      <td>685.80</td>
      <td>5601.00</td>
      <td>6330385.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>38545</th>
      <td>2020-06-03 14:00:00</td>
      <td>p1</td>
      <td>adLQvlD726eNBSB</td>
      <td>7204.00</td>
      <td>705.40</td>
      <td>5685.00</td>
      <td>6419961.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>38546</th>
      <td>2020-06-03 14:00:00</td>
      <td>p1</td>
      <td>wCURE6d3bPkepu2</td>
      <td>7545.00</td>
      <td>738.70</td>
      <td>5579.00</td>
      <td>6928448.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>38547</th>
      <td>2020-06-03 14:00:00</td>
      <td>p1</td>
      <td>z9Y9gH1T5YWrNuG</td>
      <td>7946.00</td>
      <td>777.80</td>
      <td>5541.00</td>
      <td>7152815.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



Se trata del día 3 de Junio a las 14:00, que por algún motivo no tiene datos de temperatura pero solo para 4 inverters de la planta 1.

Vamos a buscar en el dataset de temperatura si existe ese datetime.


```python
temper[temper.fecha.between('2020-06-03 13:30:00', '2020-06-03 14:30:00')]
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
      <th>fecha</th>
      <th>planta</th>
      <th>sensor_id</th>
      <th>t_ambiente</th>
      <th>t_modulo</th>
      <th>irradiacion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1797</th>
      <td>2020-06-03 13:30:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>28.56</td>
      <td>48.78</td>
      <td>0.75</td>
    </tr>
    <tr>
      <th>1798</th>
      <td>2020-06-03 13:45:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>27.86</td>
      <td>46.63</td>
      <td>0.62</td>
    </tr>
    <tr>
      <th>1799</th>
      <td>2020-06-03 14:15:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>28.36</td>
      <td>50.63</td>
      <td>0.72</td>
    </tr>
    <tr>
      <th>1800</th>
      <td>2020-06-03 14:30:00</td>
      <td>p1</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>28.31</td>
      <td>47.38</td>
      <td>0.67</td>
    </tr>
    <tr>
      <th>1874</th>
      <td>2020-06-03 13:30:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>28.60</td>
      <td>37.68</td>
      <td>0.41</td>
    </tr>
    <tr>
      <th>1875</th>
      <td>2020-06-03 13:45:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>28.75</td>
      <td>36.35</td>
      <td>0.35</td>
    </tr>
    <tr>
      <th>1876</th>
      <td>2020-06-03 14:15:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>30.45</td>
      <td>45.63</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>1877</th>
      <td>2020-06-03 14:30:00</td>
      <td>p2</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>29.64</td>
      <td>40.40</td>
      <td>0.44</td>
    </tr>
  </tbody>
</table>
</div>



Efectivamente vemos que falta ese tramo en ambas plantas. Pero sin embargo solo hay mediciones en esa hora en la planta 1, y solo en 4 inverters.

Por tanto habría dos soluciones:

* imputar esos datos para esos invertes
* eliminar esos 4 registros

Dado que parece una franja de medición propia solo de 4 inverters de la planta 1 vamos a optar por eliminarlos.


```python
df.dropna(inplace = True)
df
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
      <th>fecha</th>
      <th>planta</th>
      <th>inverter_id</th>
      <th>kw_dc</th>
      <th>kw_ac</th>
      <th>kw_dia</th>
      <th>kw_total</th>
      <th>sensor_id</th>
      <th>t_ambiente</th>
      <th>t_modulo</th>
      <th>irradiacion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6259559.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6183645.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6987759.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7602960.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-05-15 00:00:00</td>
      <td>p1</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7158964.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>136471</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>q49J1IKaHRwDQnt</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4157.00</td>
      <td>520758.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>136472</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>rrq4fwE8jgrTyWY</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3931.00</td>
      <td>121131356.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>136473</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>vOuJvMaM2sgwLmb</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4322.00</td>
      <td>2427691.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>136474</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>xMbIugepa2P7lBB</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4218.00</td>
      <td>106896394.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>136475</th>
      <td>2020-06-17 23:45:00</td>
      <td>p2</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4316.00</td>
      <td>209335741.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>136472 rows × 11 columns</p>
</div>



Por último vamos a pasar la fecha al index para poder usar toda la potencia de Pandas.


```python
df.set_index('fecha', inplace = True)
df
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
      <th>planta</th>
      <th>inverter_id</th>
      <th>kw_dc</th>
      <th>kw_ac</th>
      <th>kw_dia</th>
      <th>kw_total</th>
      <th>sensor_id</th>
      <th>t_ambiente</th>
      <th>t_modulo</th>
      <th>irradiacion</th>
    </tr>
    <tr>
      <th>fecha</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6259559.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6183645.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6987759.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7602960.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7158964.00</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p2</td>
      <td>q49J1IKaHRwDQnt</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4157.00</td>
      <td>520758.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p2</td>
      <td>rrq4fwE8jgrTyWY</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3931.00</td>
      <td>121131356.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p2</td>
      <td>vOuJvMaM2sgwLmb</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4322.00</td>
      <td>2427691.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p2</td>
      <td>xMbIugepa2P7lBB</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4218.00</td>
      <td>106896394.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p2</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4316.00</td>
      <td>209335741.00</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>136472 rows × 10 columns</p>
</div>



## GUARDAMOS EL DATAMART

Hasta ahora habíamos usado csv y bases de datos para guardar los datos.

Son formatos muy útiles y sobre todo portables.

Pero tienen el problema de son externos a Python, y por tanto no son capaces de almacenar metadatos propios de Python como algunos tipos de variables (ej datetime).

Por eso se creó un formato propio de Python: el pickle.

Con este formato podemos almacenar cualquier objeto de Python, desde un dataset hasta un modelo de machine learning.

Y tiene la ventaja de que cuando lo recuperas tiene exactamente todas las propiedades del momento en el que lo guardaste.

Además de que está bastante optimizado en cuanto al tamaño en disco.

El inconveniente es que no es tan portable. No puedes abrirlo desde Excel por ejemplo.

Puedes ponerle la extensión que quieras al archivo, aunque se suele usar la convencion .pickle

Para guardar en pickle desde Pandas usamos df.to_pickle('ruta_en_disco')

Y para cargar un pickle usamos pd.read_pickle('ruta_en_disco')


```python
df.to_pickle('df.pickle')
```
