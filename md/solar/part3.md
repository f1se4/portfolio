# DATA TRANSFORMATION

## SET UP


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

import fiser_tools as fs
fs.misc.dark_theme()


#Automcompletar rápido
%config IPCompleter.greedy=True

#Formato de display
pd.options.display.float_format = '{:15.2f}'.format
```

## DATA UPLOAD


```python
df = pd.read_pickle('df.pickle')
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




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    DatetimeIndex: 136472 entries, 2020-05-15 00:00:00 to 2020-06-17 23:45:00
    Data columns (total 10 columns):
     #   Column       Non-Null Count   Dtype  
    ---  ------       --------------   -----  
     0   planta       136472 non-null  object 
     1   inverter_id  136472 non-null  object 
     2   kw_dc        136472 non-null  float64
     3   kw_ac        136472 non-null  float64
     4   kw_dia       136472 non-null  float64
     5   kw_total     136472 non-null  float64
     6   sensor_id    136472 non-null  object 
     7   t_ambiente   136472 non-null  float64
     8   t_modulo     136472 non-null  float64
     9   irradiacion  136472 non-null  float64
    dtypes: float64(7), object(3)
    memory usage: 11.5+ MB
    

## CREATION OF VARIABLES

We start by extracting the date components and adding them as new variables.


```python
def componentes_fecha(dataframe):
    mes = dataframe.index.month
    dia = dataframe.index.day
    hora = dataframe.index.hour
    minuto = dataframe.index.minute
    
    
    return(pd.DataFrame({'mes':mes, 'dia':dia, 'hora':hora, 'minuto':minuto}))
```


```python
df = pd.concat([df.reset_index(),componentes_fecha(df)], axis = 1).set_index('fecha')
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
      <th>mes</th>
      <th>dia</th>
      <th>hora</th>
      <th>minuto</th>
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
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
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
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
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
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
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
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
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
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
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
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
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
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
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
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
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
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
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
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
    </tr>
  </tbody>
</table>
<p>136472 rows × 14 columns</p>
</div>


We are going to create the inverter efficiency variable, which consists of the percentage of DC that successfully transforms to AC.

But we are presented with a very common difficulty in ratios, that the denominator can be zero.

If that were the case, when doing the ratio it would return a null.

In our case the denominator is DC, so if the DC generation were zero, the AC generation should also be zero.

We can correct that simply by imputing the nulls that come out with zeros.


```python
def eficiencia_inverter(AC,DC):
    temp = AC / DC * 100
    return(temp.fillna(0))
```


```python
df['eficiencia'] = eficiencia_inverter(df.kw_ac, df.kw_dc)
```

We check that it has not generated nulls.


```python
df.eficiencia.isna().sum()
```




    0



We visualize efficiency globally.


```python
df.eficiencia.plot.kde();
```


    
![png](static/notebooks/solar/03_Transformacion_files/03_Transformacion_16_0.png)
    


Here is something important.

There are two clearly differentiated groups and one of them is clearly inefficient.

But for now we'll leave it written down and later we'll review which entity is having problems: plant, inverter, etc.

## DATAFRAME REORDERING

In this case it is very important not to start analyzing by analyzing, but to follow the plan defined in the project design, since there is a very clear order in the process: environmental factors --> kw_dc --> kw ac.

So let's rearrange the columns of the df to help us interpret in this order.


```python
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
      <th>mes</th>
      <th>dia</th>
      <th>hora</th>
      <th>minuto</th>
      <th>eficiencia</th>
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
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
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
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
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
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
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
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
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
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
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
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
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
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
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
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
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
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
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
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>136472 rows × 15 columns</p>
</div>




```python
orden = ['planta','mes','dia','hora','minuto','sensor_id','irradiacion','t_ambiente','t_modulo','inverter_id','kw_dc','kw_ac','eficiencia','kw_dia','kw_total']
```


```python
df = df[orden]
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
      <th>mes</th>
      <th>dia</th>
      <th>hora</th>
      <th>minuto</th>
      <th>sensor_id</th>
      <th>irradiacion</th>
      <th>t_ambiente</th>
      <th>t_modulo</th>
      <th>inverter_id</th>
      <th>kw_dc</th>
      <th>kw_ac</th>
      <th>eficiencia</th>
      <th>kw_dia</th>
      <th>kw_total</th>
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
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6259559.00</td>
    </tr>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6183645.00</td>
    </tr>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6987759.00</td>
    </tr>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7602960.00</td>
    </tr>
    <tr>
      <th>2020-05-15 00:00:00</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.00</td>
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
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.00</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>q49J1IKaHRwDQnt</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4157.00</td>
      <td>520758.00</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p2</td>
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.00</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>rrq4fwE8jgrTyWY</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3931.00</td>
      <td>121131356.00</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p2</td>
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.00</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>vOuJvMaM2sgwLmb</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4322.00</td>
      <td>2427691.00</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p2</td>
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.00</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>xMbIugepa2P7lBB</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4218.00</td>
      <td>106896394.00</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p2</td>
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>45</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.00</td>
      <td>23.20</td>
      <td>22.54</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4316.00</td>
      <td>209335741.00</td>
    </tr>
  </tbody>
</table>
<p>136472 rows × 15 columns</p>
</div>



## DAILY DATAFRAME

The level of analysis at which we have the data is every 15 minutes, which may be too disaggregated for certain analyses.

We are going to build a version of the dataframe added to the day level.

For this we use resample to do downgrading.

We must add by plant and inverter, which are the key fields of our dataset.

Since we have variables to which different aggregation functions apply we can use the dictionary format of agg()

```python
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
      <th>planta</th>
      <th>mes</th>
      <th>dia</th>
      <th>hora</th>
      <th>minuto</th>
      <th>sensor_id</th>
      <th>irradiacion</th>
      <th>t_ambiente</th>
      <th>t_modulo</th>
      <th>inverter_id</th>
      <th>kw_dc</th>
      <th>kw_ac</th>
      <th>eficiencia</th>
      <th>kw_dia</th>
      <th>kw_total</th>
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
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-05-15</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6259559.00</td>
    </tr>
    <tr>
      <th>2020-05-15</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6183645.00</td>
    </tr>
    <tr>
      <th>2020-05-15</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6987759.00</td>
    </tr>
    <tr>
      <th>2020-05-15</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7602960.00</td>
    </tr>
    <tr>
      <th>2020-05-15</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>25.18</td>
      <td>22.86</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7158964.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_dia = df.groupby(['planta', 'inverter_id']).resample('D') \
    .agg({'irradiacion': [min,np.mean,max],
          't_ambiente': [min,np.mean,max],
          't_modulo': [min,np.mean,max],
          'kw_dc': [min,np.mean,max,sum],
          'kw_ac': [min,np.mean,max,sum],
          'eficiencia': [min,np.mean,max],
          'kw_dia': max,
          'kw_total': max})

df_dia
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th colspan="3" halign="left">irradiacion</th>
      <th colspan="3" halign="left">t_ambiente</th>
      <th colspan="3" halign="left">t_modulo</th>
      <th colspan="4" halign="left">kw_dc</th>
      <th colspan="4" halign="left">kw_ac</th>
      <th colspan="3" halign="left">eficiencia</th>
      <th>kw_dia</th>
      <th>kw_total</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>min</th>
      <th>mean</th>
      <th>max</th>
      <th>min</th>
      <th>mean</th>
      <th>max</th>
      <th>min</th>
      <th>mean</th>
      <th>max</th>
      <th>min</th>
      <th>mean</th>
      <th>max</th>
      <th>sum</th>
      <th>min</th>
      <th>mean</th>
      <th>max</th>
      <th>sum</th>
      <th>min</th>
      <th>mean</th>
      <th>max</th>
      <th>max</th>
      <th>max</th>
    </tr>
    <tr>
      <th>planta</th>
      <th>inverter_id</th>
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
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">p1</th>
      <th rowspan="5" valign="top">1BY6WEcLGh8j5v7</th>
      <th>2020-05-15</th>
      <td>0.00</td>
      <td>0.20</td>
      <td>0.89</td>
      <td>22.04</td>
      <td>27.43</td>
      <td>34.43</td>
      <td>20.29</td>
      <td>32.58</td>
      <td>55.03</td>
      <td>0.00</td>
      <td>2530.55</td>
      <td>10642.75</td>
      <td>235340.70</td>
      <td>0.00</td>
      <td>247.81</td>
      <td>1039.35</td>
      <td>23046.55</td>
      <td>0.00</td>
      <td>5.26</td>
      <td>9.82</td>
      <td>5754.00</td>
      <td>6265313.00</td>
    </tr>
    <tr>
      <th>2020-05-16</th>
      <td>0.00</td>
      <td>0.21</td>
      <td>0.81</td>
      <td>21.50</td>
      <td>26.78</td>
      <td>32.52</td>
      <td>19.59</td>
      <td>31.86</td>
      <td>54.23</td>
      <td>0.00</td>
      <td>2916.25</td>
      <td>11209.00</td>
      <td>256629.88</td>
      <td>0.00</td>
      <td>285.51</td>
      <td>1095.29</td>
      <td>25124.49</td>
      <td>0.00</td>
      <td>5.56</td>
      <td>9.83</td>
      <td>6292.00</td>
      <td>6271605.00</td>
    </tr>
    <tr>
      <th>2020-05-17</th>
      <td>0.00</td>
      <td>0.24</td>
      <td>1.00</td>
      <td>21.21</td>
      <td>26.69</td>
      <td>35.25</td>
      <td>20.38</td>
      <td>32.74</td>
      <td>63.15</td>
      <td>0.00</td>
      <td>3000.41</td>
      <td>11416.43</td>
      <td>288039.82</td>
      <td>0.00</td>
      <td>293.47</td>
      <td>1114.81</td>
      <td>28172.85</td>
      <td>0.00</td>
      <td>4.99</td>
      <td>9.82</td>
      <td>7045.00</td>
      <td>6278650.00</td>
    </tr>
    <tr>
      <th>2020-05-18</th>
      <td>0.00</td>
      <td>0.16</td>
      <td>0.97</td>
      <td>20.96</td>
      <td>23.85</td>
      <td>28.37</td>
      <td>19.48</td>
      <td>27.81</td>
      <td>53.94</td>
      <td>0.00</td>
      <td>2125.32</td>
      <td>12238.86</td>
      <td>204030.30</td>
      <td>0.00</td>
      <td>208.03</td>
      <td>1193.63</td>
      <td>19970.51</td>
      <td>0.00</td>
      <td>4.99</td>
      <td>9.83</td>
      <td>4998.00</td>
      <td>6283648.00</td>
    </tr>
    <tr>
      <th>2020-05-19</th>
      <td>0.00</td>
      <td>0.19</td>
      <td>0.84</td>
      <td>22.39</td>
      <td>25.34</td>
      <td>30.37</td>
      <td>20.06</td>
      <td>29.73</td>
      <td>51.85</td>
      <td>0.00</td>
      <td>2497.61</td>
      <td>10854.50</td>
      <td>232277.27</td>
      <td>0.00</td>
      <td>244.53</td>
      <td>1059.80</td>
      <td>22741.18</td>
      <td>0.00</td>
      <td>4.63</td>
      <td>9.83</td>
      <td>6449.00</td>
      <td>6290097.00</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
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
      <th rowspan="5" valign="top">p2</th>
      <th rowspan="5" valign="top">xoJJ8DcxJEcupym</th>
      <th>2020-06-13</th>
      <td>0.00</td>
      <td>0.22</td>
      <td>0.93</td>
      <td>22.20</td>
      <td>26.12</td>
      <td>31.91</td>
      <td>20.88</td>
      <td>30.39</td>
      <td>51.01</td>
      <td>0.00</td>
      <td>285.87</td>
      <td>1271.15</td>
      <td>27443.74</td>
      <td>0.00</td>
      <td>279.59</td>
      <td>1239.95</td>
      <td>26840.58</td>
      <td>0.00</td>
      <td>51.91</td>
      <td>98.29</td>
      <td>6632.00</td>
      <td>209312200.00</td>
    </tr>
    <tr>
      <th>2020-06-14</th>
      <td>0.00</td>
      <td>0.23</td>
      <td>0.92</td>
      <td>23.65</td>
      <td>27.02</td>
      <td>32.96</td>
      <td>22.12</td>
      <td>31.59</td>
      <td>52.99</td>
      <td>0.00</td>
      <td>320.51</td>
      <td>1362.06</td>
      <td>30768.78</td>
      <td>0.00</td>
      <td>313.43</td>
      <td>1328.21</td>
      <td>30088.97</td>
      <td>0.00</td>
      <td>51.94</td>
      <td>99.92</td>
      <td>7268.00</td>
      <td>209319687.00</td>
    </tr>
    <tr>
      <th>2020-06-15</th>
      <td>0.00</td>
      <td>0.19</td>
      <td>0.83</td>
      <td>24.00</td>
      <td>26.56</td>
      <td>31.61</td>
      <td>23.00</td>
      <td>30.00</td>
      <td>48.46</td>
      <td>0.00</td>
      <td>266.64</td>
      <td>1288.28</td>
      <td>25597.24</td>
      <td>0.00</td>
      <td>260.93</td>
      <td>1256.67</td>
      <td>25049.49</td>
      <td>0.00</td>
      <td>52.94</td>
      <td>98.27</td>
      <td>7412.67</td>
      <td>209325949.00</td>
    </tr>
    <tr>
      <th>2020-06-16</th>
      <td>0.00</td>
      <td>0.17</td>
      <td>0.77</td>
      <td>23.63</td>
      <td>26.37</td>
      <td>30.83</td>
      <td>22.56</td>
      <td>29.59</td>
      <td>46.36</td>
      <td>0.00</td>
      <td>232.66</td>
      <td>1124.97</td>
      <td>22335.69</td>
      <td>0.00</td>
      <td>227.82</td>
      <td>1098.21</td>
      <td>21870.63</td>
      <td>0.00</td>
      <td>50.90</td>
      <td>98.29</td>
      <td>6203.20</td>
      <td>209331425.00</td>
    </tr>
    <tr>
      <th>2020-06-17</th>
      <td>0.00</td>
      <td>0.12</td>
      <td>0.58</td>
      <td>22.55</td>
      <td>24.85</td>
      <td>29.04</td>
      <td>21.91</td>
      <td>26.67</td>
      <td>42.33</td>
      <td>0.00</td>
      <td>183.75</td>
      <td>828.77</td>
      <td>17640.42</td>
      <td>0.00</td>
      <td>179.98</td>
      <td>810.77</td>
      <td>17278.51</td>
      <td>0.00</td>
      <td>52.90</td>
      <td>98.32</td>
      <td>5327.00</td>
      <td>209335741.00</td>
    </tr>
  </tbody>
</table>
<p>1496 rows × 22 columns</p>
</div>



It has been generated for us with a multi-index, both in rows and in columns.

To remove the from the columns we can flatten the names with .to_flat_index().

This returns the levels in tuples, which we can then join with a list comprehension.

Let's review how to_flat_index() returns the column names


```python
tuplas = df_dia.columns.to_flat_index()
tuplas
```




    Index([ ('irradiacion', 'min'), ('irradiacion', 'mean'),
            ('irradiacion', 'max'),   ('t_ambiente', 'min'),
            ('t_ambiente', 'mean'),   ('t_ambiente', 'max'),
               ('t_modulo', 'min'),    ('t_modulo', 'mean'),
               ('t_modulo', 'max'),        ('kw_dc', 'min'),
                 ('kw_dc', 'mean'),        ('kw_dc', 'max'),
                  ('kw_dc', 'sum'),        ('kw_ac', 'min'),
                 ('kw_ac', 'mean'),        ('kw_ac', 'max'),
                  ('kw_ac', 'sum'),   ('eficiencia', 'min'),
            ('eficiencia', 'mean'),   ('eficiencia', 'max'),
                 ('kw_dia', 'max'),     ('kw_total', 'max')],
          dtype='object')



And we join both parts of the pair with an underscore using .join


```python
df_dia.columns = ["_".join(par) for par in tuplas]
df_dia
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
      <th></th>
      <th>irradiacion_min</th>
      <th>irradiacion_mean</th>
      <th>irradiacion_max</th>
      <th>t_ambiente_min</th>
      <th>t_ambiente_mean</th>
      <th>t_ambiente_max</th>
      <th>t_modulo_min</th>
      <th>t_modulo_mean</th>
      <th>t_modulo_max</th>
      <th>kw_dc_min</th>
      <th>kw_dc_mean</th>
      <th>kw_dc_max</th>
      <th>kw_dc_sum</th>
      <th>kw_ac_min</th>
      <th>kw_ac_mean</th>
      <th>kw_ac_max</th>
      <th>kw_ac_sum</th>
      <th>eficiencia_min</th>
      <th>eficiencia_mean</th>
      <th>eficiencia_max</th>
      <th>kw_dia_max</th>
      <th>kw_total_max</th>
    </tr>
    <tr>
      <th>planta</th>
      <th>inverter_id</th>
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
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">p1</th>
      <th rowspan="5" valign="top">1BY6WEcLGh8j5v7</th>
      <th>2020-05-15</th>
      <td>0.00</td>
      <td>0.20</td>
      <td>0.89</td>
      <td>22.04</td>
      <td>27.43</td>
      <td>34.43</td>
      <td>20.29</td>
      <td>32.58</td>
      <td>55.03</td>
      <td>0.00</td>
      <td>2530.55</td>
      <td>10642.75</td>
      <td>235340.70</td>
      <td>0.00</td>
      <td>247.81</td>
      <td>1039.35</td>
      <td>23046.55</td>
      <td>0.00</td>
      <td>5.26</td>
      <td>9.82</td>
      <td>5754.00</td>
      <td>6265313.00</td>
    </tr>
    <tr>
      <th>2020-05-16</th>
      <td>0.00</td>
      <td>0.21</td>
      <td>0.81</td>
      <td>21.50</td>
      <td>26.78</td>
      <td>32.52</td>
      <td>19.59</td>
      <td>31.86</td>
      <td>54.23</td>
      <td>0.00</td>
      <td>2916.25</td>
      <td>11209.00</td>
      <td>256629.88</td>
      <td>0.00</td>
      <td>285.51</td>
      <td>1095.29</td>
      <td>25124.49</td>
      <td>0.00</td>
      <td>5.56</td>
      <td>9.83</td>
      <td>6292.00</td>
      <td>6271605.00</td>
    </tr>
    <tr>
      <th>2020-05-17</th>
      <td>0.00</td>
      <td>0.24</td>
      <td>1.00</td>
      <td>21.21</td>
      <td>26.69</td>
      <td>35.25</td>
      <td>20.38</td>
      <td>32.74</td>
      <td>63.15</td>
      <td>0.00</td>
      <td>3000.41</td>
      <td>11416.43</td>
      <td>288039.82</td>
      <td>0.00</td>
      <td>293.47</td>
      <td>1114.81</td>
      <td>28172.85</td>
      <td>0.00</td>
      <td>4.99</td>
      <td>9.82</td>
      <td>7045.00</td>
      <td>6278650.00</td>
    </tr>
    <tr>
      <th>2020-05-18</th>
      <td>0.00</td>
      <td>0.16</td>
      <td>0.97</td>
      <td>20.96</td>
      <td>23.85</td>
      <td>28.37</td>
      <td>19.48</td>
      <td>27.81</td>
      <td>53.94</td>
      <td>0.00</td>
      <td>2125.32</td>
      <td>12238.86</td>
      <td>204030.30</td>
      <td>0.00</td>
      <td>208.03</td>
      <td>1193.63</td>
      <td>19970.51</td>
      <td>0.00</td>
      <td>4.99</td>
      <td>9.83</td>
      <td>4998.00</td>
      <td>6283648.00</td>
    </tr>
    <tr>
      <th>2020-05-19</th>
      <td>0.00</td>
      <td>0.19</td>
      <td>0.84</td>
      <td>22.39</td>
      <td>25.34</td>
      <td>30.37</td>
      <td>20.06</td>
      <td>29.73</td>
      <td>51.85</td>
      <td>0.00</td>
      <td>2497.61</td>
      <td>10854.50</td>
      <td>232277.27</td>
      <td>0.00</td>
      <td>244.53</td>
      <td>1059.80</td>
      <td>22741.18</td>
      <td>0.00</td>
      <td>4.63</td>
      <td>9.83</td>
      <td>6449.00</td>
      <td>6290097.00</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
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
      <th rowspan="5" valign="top">p2</th>
      <th rowspan="5" valign="top">xoJJ8DcxJEcupym</th>
      <th>2020-06-13</th>
      <td>0.00</td>
      <td>0.22</td>
      <td>0.93</td>
      <td>22.20</td>
      <td>26.12</td>
      <td>31.91</td>
      <td>20.88</td>
      <td>30.39</td>
      <td>51.01</td>
      <td>0.00</td>
      <td>285.87</td>
      <td>1271.15</td>
      <td>27443.74</td>
      <td>0.00</td>
      <td>279.59</td>
      <td>1239.95</td>
      <td>26840.58</td>
      <td>0.00</td>
      <td>51.91</td>
      <td>98.29</td>
      <td>6632.00</td>
      <td>209312200.00</td>
    </tr>
    <tr>
      <th>2020-06-14</th>
      <td>0.00</td>
      <td>0.23</td>
      <td>0.92</td>
      <td>23.65</td>
      <td>27.02</td>
      <td>32.96</td>
      <td>22.12</td>
      <td>31.59</td>
      <td>52.99</td>
      <td>0.00</td>
      <td>320.51</td>
      <td>1362.06</td>
      <td>30768.78</td>
      <td>0.00</td>
      <td>313.43</td>
      <td>1328.21</td>
      <td>30088.97</td>
      <td>0.00</td>
      <td>51.94</td>
      <td>99.92</td>
      <td>7268.00</td>
      <td>209319687.00</td>
    </tr>
    <tr>
      <th>2020-06-15</th>
      <td>0.00</td>
      <td>0.19</td>
      <td>0.83</td>
      <td>24.00</td>
      <td>26.56</td>
      <td>31.61</td>
      <td>23.00</td>
      <td>30.00</td>
      <td>48.46</td>
      <td>0.00</td>
      <td>266.64</td>
      <td>1288.28</td>
      <td>25597.24</td>
      <td>0.00</td>
      <td>260.93</td>
      <td>1256.67</td>
      <td>25049.49</td>
      <td>0.00</td>
      <td>52.94</td>
      <td>98.27</td>
      <td>7412.67</td>
      <td>209325949.00</td>
    </tr>
    <tr>
      <th>2020-06-16</th>
      <td>0.00</td>
      <td>0.17</td>
      <td>0.77</td>
      <td>23.63</td>
      <td>26.37</td>
      <td>30.83</td>
      <td>22.56</td>
      <td>29.59</td>
      <td>46.36</td>
      <td>0.00</td>
      <td>232.66</td>
      <td>1124.97</td>
      <td>22335.69</td>
      <td>0.00</td>
      <td>227.82</td>
      <td>1098.21</td>
      <td>21870.63</td>
      <td>0.00</td>
      <td>50.90</td>
      <td>98.29</td>
      <td>6203.20</td>
      <td>209331425.00</td>
    </tr>
    <tr>
      <th>2020-06-17</th>
      <td>0.00</td>
      <td>0.12</td>
      <td>0.58</td>
      <td>22.55</td>
      <td>24.85</td>
      <td>29.04</td>
      <td>21.91</td>
      <td>26.67</td>
      <td>42.33</td>
      <td>0.00</td>
      <td>183.75</td>
      <td>828.77</td>
      <td>17640.42</td>
      <td>0.00</td>
      <td>179.98</td>
      <td>810.77</td>
      <td>17278.51</td>
      <td>0.00</td>
      <td>52.90</td>
      <td>98.32</td>
      <td>5327.00</td>
      <td>209335741.00</td>
    </tr>
  </tbody>
</table>
<p>1496 rows × 22 columns</p>
</div>



Now we need to pass plant and inverter_id to columns, and leave the date as the index.


```python
df_dia = df_dia.reset_index().set_index('fecha')
df_dia
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
      <th>irradiacion_min</th>
      <th>irradiacion_mean</th>
      <th>irradiacion_max</th>
      <th>t_ambiente_min</th>
      <th>t_ambiente_mean</th>
      <th>t_ambiente_max</th>
      <th>t_modulo_min</th>
      <th>t_modulo_mean</th>
      <th>t_modulo_max</th>
      <th>kw_dc_min</th>
      <th>kw_dc_mean</th>
      <th>kw_dc_max</th>
      <th>kw_dc_sum</th>
      <th>kw_ac_min</th>
      <th>kw_ac_mean</th>
      <th>kw_ac_max</th>
      <th>kw_ac_sum</th>
      <th>eficiencia_min</th>
      <th>eficiencia_mean</th>
      <th>eficiencia_max</th>
      <th>kw_dia_max</th>
      <th>kw_total_max</th>
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
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-05-15</th>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.20</td>
      <td>0.89</td>
      <td>22.04</td>
      <td>27.43</td>
      <td>34.43</td>
      <td>20.29</td>
      <td>32.58</td>
      <td>55.03</td>
      <td>0.00</td>
      <td>2530.55</td>
      <td>10642.75</td>
      <td>235340.70</td>
      <td>0.00</td>
      <td>247.81</td>
      <td>1039.35</td>
      <td>23046.55</td>
      <td>0.00</td>
      <td>5.26</td>
      <td>9.82</td>
      <td>5754.00</td>
      <td>6265313.00</td>
    </tr>
    <tr>
      <th>2020-05-16</th>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.21</td>
      <td>0.81</td>
      <td>21.50</td>
      <td>26.78</td>
      <td>32.52</td>
      <td>19.59</td>
      <td>31.86</td>
      <td>54.23</td>
      <td>0.00</td>
      <td>2916.25</td>
      <td>11209.00</td>
      <td>256629.88</td>
      <td>0.00</td>
      <td>285.51</td>
      <td>1095.29</td>
      <td>25124.49</td>
      <td>0.00</td>
      <td>5.56</td>
      <td>9.83</td>
      <td>6292.00</td>
      <td>6271605.00</td>
    </tr>
    <tr>
      <th>2020-05-17</th>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.24</td>
      <td>1.00</td>
      <td>21.21</td>
      <td>26.69</td>
      <td>35.25</td>
      <td>20.38</td>
      <td>32.74</td>
      <td>63.15</td>
      <td>0.00</td>
      <td>3000.41</td>
      <td>11416.43</td>
      <td>288039.82</td>
      <td>0.00</td>
      <td>293.47</td>
      <td>1114.81</td>
      <td>28172.85</td>
      <td>0.00</td>
      <td>4.99</td>
      <td>9.82</td>
      <td>7045.00</td>
      <td>6278650.00</td>
    </tr>
    <tr>
      <th>2020-05-18</th>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.16</td>
      <td>0.97</td>
      <td>20.96</td>
      <td>23.85</td>
      <td>28.37</td>
      <td>19.48</td>
      <td>27.81</td>
      <td>53.94</td>
      <td>0.00</td>
      <td>2125.32</td>
      <td>12238.86</td>
      <td>204030.30</td>
      <td>0.00</td>
      <td>208.03</td>
      <td>1193.63</td>
      <td>19970.51</td>
      <td>0.00</td>
      <td>4.99</td>
      <td>9.83</td>
      <td>4998.00</td>
      <td>6283648.00</td>
    </tr>
    <tr>
      <th>2020-05-19</th>
      <td>p1</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>0.00</td>
      <td>0.19</td>
      <td>0.84</td>
      <td>22.39</td>
      <td>25.34</td>
      <td>30.37</td>
      <td>20.06</td>
      <td>29.73</td>
      <td>51.85</td>
      <td>0.00</td>
      <td>2497.61</td>
      <td>10854.50</td>
      <td>232277.27</td>
      <td>0.00</td>
      <td>244.53</td>
      <td>1059.80</td>
      <td>22741.18</td>
      <td>0.00</td>
      <td>4.63</td>
      <td>9.83</td>
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
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2020-06-13</th>
      <td>p2</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.22</td>
      <td>0.93</td>
      <td>22.20</td>
      <td>26.12</td>
      <td>31.91</td>
      <td>20.88</td>
      <td>30.39</td>
      <td>51.01</td>
      <td>0.00</td>
      <td>285.87</td>
      <td>1271.15</td>
      <td>27443.74</td>
      <td>0.00</td>
      <td>279.59</td>
      <td>1239.95</td>
      <td>26840.58</td>
      <td>0.00</td>
      <td>51.91</td>
      <td>98.29</td>
      <td>6632.00</td>
      <td>209312200.00</td>
    </tr>
    <tr>
      <th>2020-06-14</th>
      <td>p2</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.23</td>
      <td>0.92</td>
      <td>23.65</td>
      <td>27.02</td>
      <td>32.96</td>
      <td>22.12</td>
      <td>31.59</td>
      <td>52.99</td>
      <td>0.00</td>
      <td>320.51</td>
      <td>1362.06</td>
      <td>30768.78</td>
      <td>0.00</td>
      <td>313.43</td>
      <td>1328.21</td>
      <td>30088.97</td>
      <td>0.00</td>
      <td>51.94</td>
      <td>99.92</td>
      <td>7268.00</td>
      <td>209319687.00</td>
    </tr>
    <tr>
      <th>2020-06-15</th>
      <td>p2</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.19</td>
      <td>0.83</td>
      <td>24.00</td>
      <td>26.56</td>
      <td>31.61</td>
      <td>23.00</td>
      <td>30.00</td>
      <td>48.46</td>
      <td>0.00</td>
      <td>266.64</td>
      <td>1288.28</td>
      <td>25597.24</td>
      <td>0.00</td>
      <td>260.93</td>
      <td>1256.67</td>
      <td>25049.49</td>
      <td>0.00</td>
      <td>52.94</td>
      <td>98.27</td>
      <td>7412.67</td>
      <td>209325949.00</td>
    </tr>
    <tr>
      <th>2020-06-16</th>
      <td>p2</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.17</td>
      <td>0.77</td>
      <td>23.63</td>
      <td>26.37</td>
      <td>30.83</td>
      <td>22.56</td>
      <td>29.59</td>
      <td>46.36</td>
      <td>0.00</td>
      <td>232.66</td>
      <td>1124.97</td>
      <td>22335.69</td>
      <td>0.00</td>
      <td>227.82</td>
      <td>1098.21</td>
      <td>21870.63</td>
      <td>0.00</td>
      <td>50.90</td>
      <td>98.29</td>
      <td>6203.20</td>
      <td>209331425.00</td>
    </tr>
    <tr>
      <th>2020-06-17</th>
      <td>p2</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.12</td>
      <td>0.58</td>
      <td>22.55</td>
      <td>24.85</td>
      <td>29.04</td>
      <td>21.91</td>
      <td>26.67</td>
      <td>42.33</td>
      <td>0.00</td>
      <td>183.75</td>
      <td>828.77</td>
      <td>17640.42</td>
      <td>0.00</td>
      <td>179.98</td>
      <td>810.77</td>
      <td>17278.51</td>
      <td>0.00</td>
      <td>52.90</td>
      <td>98.32</td>
      <td>5327.00</td>
      <td>209335741.00</td>
    </tr>
  </tbody>
</table>
<p>1496 rows × 24 columns</p>
</div>



We already have our hourly and daily datasets ready.

We keep them.


```python
df.to_pickle('df.pickle')
df_dia.to_pickle('df_dia.pickle')
```
