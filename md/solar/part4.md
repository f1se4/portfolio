# ANALYSIS AND INSIGHTS

## SET UP


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns


#Automcompletar rápido
%config IPCompleter.greedy=True

#Formato de display
pd.options.display.float_format = '{:15.2f}'.format

#Formato de graficos
import fiser_tools as fs 
fs.misc.dark_theme()
```

## CARGA DE DATOS


```python
df = pd.read_pickle('df.pickle')
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
df_dia = pd.read_pickle('df_dia.pickle')
df_dia.head()
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
      <th>...</th>
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
      <td>...</td>
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
      <td>...</td>
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
      <td>...</td>
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
      <td>...</td>
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
      <td>...</td>
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
  </tbody>
</table>
<p>5 rows × 24 columns</p>
</div>



## ANALYSIS AND INSIGHTS

The first lever is the reception of solar energy.

We have 3 kpis with which to measure this lever: incoming irradiation, ambient temperature, and module temperature.

These kpis are measured with a single sensor per plant, so the data is the same for all inverters.

We need to understand how these variables work with each other before moving on to see how they interact with the next level.

Since the inverter does not matter and we only need those 3 variables, we are going to create a smaller dataset with only one inverter from each plant to work on.

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




```python
recepcion = df.loc[(df.inverter_id == '1BY6WEcLGh8j5v7') | (df.inverter_id == 'q49J1IKaHRwDQnt'), 'planta':'t_modulo']
recepcion
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
    </tr>
    <tr>
      <th>2020-05-15 00:15:00</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>15</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>25.08</td>
      <td>22.76</td>
    </tr>
    <tr>
      <th>2020-05-15 00:30:00</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>30</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>24.94</td>
      <td>22.59</td>
    </tr>
    <tr>
      <th>2020-05-15 00:45:00</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>0</td>
      <td>45</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>24.85</td>
      <td>22.36</td>
    </tr>
    <tr>
      <th>2020-05-15 01:00:00</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>1</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.00</td>
      <td>24.62</td>
      <td>22.17</td>
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
      <th>2020-06-17 22:45:00</th>
      <td>p2</td>
      <td>6</td>
      <td>17</td>
      <td>22</td>
      <td>45</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.00</td>
      <td>23.51</td>
      <td>22.86</td>
    </tr>
    <tr>
      <th>2020-06-17 23:00:00</th>
      <td>p2</td>
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>0</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.00</td>
      <td>23.48</td>
      <td>22.74</td>
    </tr>
    <tr>
      <th>2020-06-17 23:15:00</th>
      <td>p2</td>
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>15</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.00</td>
      <td>23.35</td>
      <td>22.49</td>
    </tr>
    <tr>
      <th>2020-06-17 23:30:00</th>
      <td>p2</td>
      <td>6</td>
      <td>17</td>
      <td>23</td>
      <td>30</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.00</td>
      <td>23.29</td>
      <td>22.37</td>
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
    </tr>
  </tbody>
</table>
<p>6413 rows × 9 columns</p>
</div>



### Do the two plants receive the same amount of solar energy?


```python
temp = recepcion.groupby('planta').agg({'irradiacion':sum,'t_ambiente':np.mean,'t_modulo':np.mean})
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
      <th>irradiacion</th>
      <th>t_ambiente</th>
      <th>t_modulo</th>
    </tr>
    <tr>
      <th>planta</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>p1</th>
      <td>726.40</td>
      <td>25.56</td>
      <td>31.18</td>
    </tr>
    <tr>
      <th>p2</th>
      <td>758.49</td>
      <td>28.07</td>
      <td>32.77</td>
    </tr>
  </tbody>
</table>
</div>




```python
f, ax = plt.subplots(nrows=1, ncols=3, figsize = (18,5))

ax[0].bar(temp.index, temp.irradiacion, color = ['red','blue'], alpha = 0.3)
ax[1].bar(temp.index, temp.t_ambiente, color = ['red','blue'], alpha = 0.3)
ax[2].bar(temp.index, temp.t_modulo, color = ['red','blue'], alpha = 0.3)
ax[0].set_title('Irradiación por planta')
ax[1].set_title('Temperatura ambiente por planta')
ax[2].set_title('Temperatura módulo por planta');
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_12_0.png)
    


Conclusions:

* In general, plant 2 receives more solar energy than plant 1
* But this difference cannot imply the performance problem that supposedly exists

### How are these three variables related?


```python
temp = recepcion.loc[:,['planta','irradiacion','t_ambiente','t_modulo']]
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
      <th>planta</th>
      <th>irradiacion</th>
      <th>t_ambiente</th>
      <th>t_modulo</th>
    </tr>
    <tr>
      <th>fecha</th>
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
      <td>0.00</td>
      <td>25.18</td>
      <td>22.86</td>
    </tr>
    <tr>
      <th>2020-05-15 00:15:00</th>
      <td>p1</td>
      <td>0.00</td>
      <td>25.08</td>
      <td>22.76</td>
    </tr>
    <tr>
      <th>2020-05-15 00:30:00</th>
      <td>p1</td>
      <td>0.00</td>
      <td>24.94</td>
      <td>22.59</td>
    </tr>
    <tr>
      <th>2020-05-15 00:45:00</th>
      <td>p1</td>
      <td>0.00</td>
      <td>24.85</td>
      <td>22.36</td>
    </tr>
    <tr>
      <th>2020-05-15 01:00:00</th>
      <td>p1</td>
      <td>0.00</td>
      <td>24.62</td>
      <td>22.17</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2020-06-17 22:45:00</th>
      <td>p2</td>
      <td>0.00</td>
      <td>23.51</td>
      <td>22.86</td>
    </tr>
    <tr>
      <th>2020-06-17 23:00:00</th>
      <td>p2</td>
      <td>0.00</td>
      <td>23.48</td>
      <td>22.74</td>
    </tr>
    <tr>
      <th>2020-06-17 23:15:00</th>
      <td>p2</td>
      <td>0.00</td>
      <td>23.35</td>
      <td>22.49</td>
    </tr>
    <tr>
      <th>2020-06-17 23:30:00</th>
      <td>p2</td>
      <td>0.00</td>
      <td>23.29</td>
      <td>22.37</td>
    </tr>
    <tr>
      <th>2020-06-17 23:45:00</th>
      <td>p2</td>
      <td>0.00</td>
      <td>23.20</td>
      <td>22.54</td>
    </tr>
  </tbody>
</table>
<p>6413 rows × 4 columns</p>
</div>




```python
sns.heatmap(temp.corr(), annot=True);
```


    
![png](static/notebooks/solar/static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_16_0.png)
    



```python
sns.pairplot(temp.reset_index(), hue = 'planta', height=3, plot_kws={'alpha': 0.1});
```


    
![png](static/notebooks/solar/static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_17_0.png)
    


Conclusions:

* Irradiance highly correlates with module temperature
* But not so much with room temperature
* Therefore, a first way to identify defective or dirty modules is to locate those that produce little when the irradiation is high

### How is the irradiation and temperature distributed throughout the day?


```python
temp = pd.crosstab(recepcion.hora,recepcion.planta,values = recepcion.irradiacion,aggfunc='mean')
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
      <th>planta</th>
      <th>p1</th>
      <th>p2</th>
    </tr>
    <tr>
      <th>hora</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.04</td>
      <td>0.04</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.19</td>
      <td>0.19</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.37</td>
      <td>0.39</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.53</td>
      <td>0.57</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.64</td>
      <td>0.69</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.73</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.74</td>
      <td>0.79</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.69</td>
      <td>0.69</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.58</td>
      <td>0.60</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.46</td>
      <td>0.44</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.29</td>
      <td>0.28</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0.13</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.02</td>
      <td>0.02</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize=(10,10))
sns.heatmap(temp, annot=True, fmt=".2f");
```


    
![png](static/notebooks/solar/static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_21_0.png)
    



```python
temp = pd.crosstab(recepcion.hora,recepcion.planta,values = recepcion.t_ambiente,aggfunc='mean')
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
      <th>planta</th>
      <th>p1</th>
      <th>p2</th>
    </tr>
    <tr>
      <th>hora</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>22.80</td>
      <td>25.20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>22.63</td>
      <td>24.82</td>
    </tr>
    <tr>
      <th>2</th>
      <td>22.46</td>
      <td>24.48</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22.32</td>
      <td>24.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22.17</td>
      <td>24.07</td>
    </tr>
    <tr>
      <th>5</th>
      <td>22.06</td>
      <td>23.91</td>
    </tr>
    <tr>
      <th>6</th>
      <td>22.20</td>
      <td>24.19</td>
    </tr>
    <tr>
      <th>7</th>
      <td>23.34</td>
      <td>25.48</td>
    </tr>
    <tr>
      <th>8</th>
      <td>24.92</td>
      <td>27.05</td>
    </tr>
    <tr>
      <th>9</th>
      <td>26.48</td>
      <td>28.61</td>
    </tr>
    <tr>
      <th>10</th>
      <td>27.65</td>
      <td>30.17</td>
    </tr>
    <tr>
      <th>11</th>
      <td>28.80</td>
      <td>31.43</td>
    </tr>
    <tr>
      <th>12</th>
      <td>29.62</td>
      <td>32.55</td>
    </tr>
    <tr>
      <th>13</th>
      <td>30.10</td>
      <td>33.01</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.29</td>
      <td>33.16</td>
    </tr>
    <tr>
      <th>15</th>
      <td>29.99</td>
      <td>32.81</td>
    </tr>
    <tr>
      <th>16</th>
      <td>29.38</td>
      <td>32.44</td>
    </tr>
    <tr>
      <th>17</th>
      <td>28.29</td>
      <td>31.59</td>
    </tr>
    <tr>
      <th>18</th>
      <td>26.66</td>
      <td>30.00</td>
    </tr>
    <tr>
      <th>19</th>
      <td>25.36</td>
      <td>28.61</td>
    </tr>
    <tr>
      <th>20</th>
      <td>24.50</td>
      <td>27.63</td>
    </tr>
    <tr>
      <th>21</th>
      <td>23.87</td>
      <td>26.75</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23.26</td>
      <td>26.06</td>
    </tr>
    <tr>
      <th>23</th>
      <td>22.92</td>
      <td>25.46</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize=(10,10))
sns.heatmap(temp, annot=True, fmt=".1f");
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_23_0.png)
    


Conclusions:

* Both plants have similar patterns. We might think that they are in geographical areas not far away
* There is irradiation (and therefore a priori the plants should produce) between 7 a.m. and 5 p.m.
* The maximum irradiation occurs between 11 and 12
* The maximum room temperature occurs between 14 and 16

### Are both plants equally capable of generating DC from irradiation?


```python
plt.figure(figsize = (12,8))
sns.scatterplot(data = df, x = df.irradiacion, y = df.kw_dc);
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_26_0.png)
    


There are 2 clearly different patterns. Could it be the plants?


```python
plt.figure(figsize = (12,8))
sns.scatterplot(data = df, x = df.irradiacion, y = df.kw_dc, hue = 'planta');
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_28_0.png)
    


Plant number 2 produces much less kW at the same irradiation levels.

But before we had seen that the relationship between dc and ac in plant 1 was strange.

And also that the data for dc and ac did not match those of kw_dia.

There is something strange in the data.

Let's see the relationship between irradiation and kw_dia to see if it gives us light.


```python
plt.figure(figsize = (12,10))
sns.scatterplot(data = df, x = df.irradiacion, y = df.kw_dia, hue = 'planta');
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_30_0.png)
    


It's very strange. It seems that the relationship is that the more irradiation, the less kW generated. Which doesn't make sense.

It even seems that the kw maximums occur in hours of zero irradiation.

Can you imagine what could be happening?

BEWARE: the variable kw_dia is a CUMULATIVE. That means that it should reach its maximum when the last hour of the day arrives, for example 23:45, where obviously the irradiation is zero.

And not have data until after 7, which is when we see that there is irradiation.

Let's check it out.


```python
df.groupby('hora')[['kw_dia']].mean().plot.bar();
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_33_0.png)
    


Again something doesn't add up. There is generation between 00 and 06.

And also after 6:00 p.m. it begins to decline, which should not happen if it is accumulated.

Conclusion:

We don't trust these cumulative variables like kw_day and kw_total.

But the truth is that we don't trust the others much either.

In a real situation I would stop the project until I was able to see what happens with the data.

But in order to continue we are going to assume that the dc and ac data are correct.

And under this assumption we will obtain our conclusions.

**INSIGHT #1**

Plant 2 generates much lower levels of DC even at similar levels of irradiation

### Is the generation constant throughout the days?

We can use the df_dia to plot the global vision of DC generation during the analysis period.


```python
plt.figure(figsize = (10,8))
sns.lineplot(data = df_dia.reset_index(), x = df_dia.reset_index().fecha, y = 'kw_dc_sum', hue = 'planta');
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_38_0.png)
    


We see that plant 1 has much more variability while plant 2 is much more constant.

But above all we are surprised by the low levels of DC generation on plant 2 compared to 1.

Let's examine the generation of each day to see if we see something strange.

We generate a date variable to be able to add by it.


```python
df['date'] = df.index.date
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
      <th>date</th>
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
      <td>2020-05-15</td>
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
      <td>2020-05-15</td>
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
      <td>2020-05-15</td>
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
      <td>2020-05-15</td>
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
      <td>2020-06-17</td>
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
      <td>2020-06-17</td>
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
      <td>2020-06-17</td>
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
      <td>2020-06-17</td>
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
      <td>2020-06-17</td>
    </tr>
  </tbody>
</table>
<p>136472 rows × 16 columns</p>
</div>


We create a temporal dataframe to analyze the hourly DC generation on each day at plant 1.

```python
dc_constante_p1 = df[df.planta == 'p1'].groupby(['planta','date','hora']).kw_dc.sum()
dc_constante_p1
```




    planta  date        hora
    p1      2020-05-15  0                 0.00
                        1                 0.00
                        2                 0.00
                        3                 0.00
                        4                 0.00
                                     ...      
            2020-06-17  19                0.00
                        20                0.00
                        21                0.00
                        22                0.00
                        23                0.00
    Name: kw_dc, Length: 796, dtype: float64



We create a temporal dataframe to analyze the hourly DC generation on each day at plant 1.

```python
dc_constante_p1.unstack(level = 1).plot(subplots = True, layout = (17,2), sharex=True, figsize=(20,30));
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_45_0.png)
    


Conclusions:

* On floor 1, similar patterns are maintained every day
* Except for a break on May 20 and a strange crash on June 5
* But none appear to be structural
* Therefore, although each day may have different production totals, the intraday patterns are similar and seem correct.

We repeated the analysis on plant 2


```python
dc_constante_p2 = df[df.planta == 'p2'].groupby(['planta','date','hora']).kw_dc.sum()
dc_constante_p2
```




    planta  date        hora
    p2      2020-05-15  0                 0.00
                        1                 0.00
                        2                 0.00
                        3                 0.00
                        4                 0.00
                                     ...      
            2020-06-17  19                0.00
                        20                0.00
                        21                0.00
                        22                0.00
                        23                0.00
    Name: kw_dc, Length: 816, dtype: float64


We are going to pass date to columns, to be able to represent each column (which are the dates) as a variable and therefore as an independent graph.

```python
dc_constante_p2.unstack(level = 1).plot(subplots = True, layout = (17,2), sharex=True, figsize=(20,30));
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_50_0.png)
    


Conclusions:

* Again on May 20 he appears with a strange behavior
* Production levels are constant over the days, but always about 10 times below plant 1 levels

**INSIGHT #2:** The low levels of plant 2 are constant and have daily curves that seem normal.

### Is the DC to AC conversion generated correctly?


```python
sns.scatterplot(data = df, x = df.kw_dc, y = df.kw_ac, hue = df.planta);
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_53_0.png)
    


Again the patterns are very clear: plant 2 transforms the current much more efficiently.

We are going to expand by analyzing the efficiency variable that we had created.


```python
temp = df.groupby(['planta','hora'],as_index = False).eficiencia.mean()
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
      <th>planta</th>
      <th>hora</th>
      <th>eficiencia</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>p1</td>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>p1</td>
      <td>1</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>p1</td>
      <td>2</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>p1</td>
      <td>3</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>p1</td>
      <td>4</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>5</th>
      <td>p1</td>
      <td>5</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>6</th>
      <td>p1</td>
      <td>6</td>
      <td>9.20</td>
    </tr>
    <tr>
      <th>7</th>
      <td>p1</td>
      <td>7</td>
      <td>9.80</td>
    </tr>
    <tr>
      <th>8</th>
      <td>p1</td>
      <td>8</td>
      <td>9.81</td>
    </tr>
    <tr>
      <th>9</th>
      <td>p1</td>
      <td>9</td>
      <td>9.78</td>
    </tr>
    <tr>
      <th>10</th>
      <td>p1</td>
      <td>10</td>
      <td>9.77</td>
    </tr>
    <tr>
      <th>11</th>
      <td>p1</td>
      <td>11</td>
      <td>9.75</td>
    </tr>
    <tr>
      <th>12</th>
      <td>p1</td>
      <td>12</td>
      <td>9.71</td>
    </tr>
    <tr>
      <th>13</th>
      <td>p1</td>
      <td>13</td>
      <td>9.68</td>
    </tr>
    <tr>
      <th>14</th>
      <td>p1</td>
      <td>14</td>
      <td>9.76</td>
    </tr>
    <tr>
      <th>15</th>
      <td>p1</td>
      <td>15</td>
      <td>9.79</td>
    </tr>
    <tr>
      <th>16</th>
      <td>p1</td>
      <td>16</td>
      <td>9.81</td>
    </tr>
    <tr>
      <th>17</th>
      <td>p1</td>
      <td>17</td>
      <td>9.76</td>
    </tr>
    <tr>
      <th>18</th>
      <td>p1</td>
      <td>18</td>
      <td>6.53</td>
    </tr>
    <tr>
      <th>19</th>
      <td>p1</td>
      <td>19</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>20</th>
      <td>p1</td>
      <td>20</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>21</th>
      <td>p1</td>
      <td>21</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>22</th>
      <td>p1</td>
      <td>22</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>23</th>
      <td>p1</td>
      <td>23</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>24</th>
      <td>p2</td>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>25</th>
      <td>p2</td>
      <td>1</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>26</th>
      <td>p2</td>
      <td>2</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>27</th>
      <td>p2</td>
      <td>3</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>28</th>
      <td>p2</td>
      <td>4</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>29</th>
      <td>p2</td>
      <td>5</td>
      <td>0.58</td>
    </tr>
    <tr>
      <th>30</th>
      <td>p2</td>
      <td>6</td>
      <td>92.93</td>
    </tr>
    <tr>
      <th>31</th>
      <td>p2</td>
      <td>7</td>
      <td>97.39</td>
    </tr>
    <tr>
      <th>32</th>
      <td>p2</td>
      <td>8</td>
      <td>97.42</td>
    </tr>
    <tr>
      <th>33</th>
      <td>p2</td>
      <td>9</td>
      <td>91.70</td>
    </tr>
    <tr>
      <th>34</th>
      <td>p2</td>
      <td>10</td>
      <td>76.20</td>
    </tr>
    <tr>
      <th>35</th>
      <td>p2</td>
      <td>11</td>
      <td>68.35</td>
    </tr>
    <tr>
      <th>36</th>
      <td>p2</td>
      <td>12</td>
      <td>68.16</td>
    </tr>
    <tr>
      <th>37</th>
      <td>p2</td>
      <td>13</td>
      <td>73.04</td>
    </tr>
    <tr>
      <th>38</th>
      <td>p2</td>
      <td>14</td>
      <td>83.43</td>
    </tr>
    <tr>
      <th>39</th>
      <td>p2</td>
      <td>15</td>
      <td>95.69</td>
    </tr>
    <tr>
      <th>40</th>
      <td>p2</td>
      <td>16</td>
      <td>95.85</td>
    </tr>
    <tr>
      <th>41</th>
      <td>p2</td>
      <td>17</td>
      <td>95.56</td>
    </tr>
    <tr>
      <th>42</th>
      <td>p2</td>
      <td>18</td>
      <td>73.52</td>
    </tr>
    <tr>
      <th>43</th>
      <td>p2</td>
      <td>19</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>44</th>
      <td>p2</td>
      <td>20</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>45</th>
      <td>p2</td>
      <td>21</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>46</th>
      <td>p2</td>
      <td>22</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>47</th>
      <td>p2</td>
      <td>23</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.lineplot(data = temp, x = 'hora', y = 'eficiencia', hue = 'planta');
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_56_0.png)
    


**INSIGHT #3**

Plant 1 has a very low capacity to transform DC to AC, which suggests problems with the inverters

Other conclusions:

* Go into the details of the inverters on floor 1, to see if they are all or there are some that bias the average
* Review why plant 2 loses efficiency during the hours of most irradiation

We are going to start with the second, comparing the production of DC with that of AC in plant 2.


```python
temp = df[['planta','hora','kw_dc','kw_ac']].melt(id_vars= ['planta','hora'])
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
      <th>planta</th>
      <th>hora</th>
      <th>variable</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>p1</td>
      <td>0</td>
      <td>kw_dc</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>p1</td>
      <td>0</td>
      <td>kw_dc</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>p1</td>
      <td>0</td>
      <td>kw_dc</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>p1</td>
      <td>0</td>
      <td>kw_dc</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>p1</td>
      <td>0</td>
      <td>kw_dc</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>272939</th>
      <td>p2</td>
      <td>23</td>
      <td>kw_ac</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>272940</th>
      <td>p2</td>
      <td>23</td>
      <td>kw_ac</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>272941</th>
      <td>p2</td>
      <td>23</td>
      <td>kw_ac</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>272942</th>
      <td>p2</td>
      <td>23</td>
      <td>kw_ac</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>272943</th>
      <td>p2</td>
      <td>23</td>
      <td>kw_ac</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>272944 rows × 4 columns</p>
</div>




```python
plt.figure(figsize = (12,8))
sns.lineplot(data = temp[temp.planta == 'p2'], x = 'hora', y = 'value', hue = 'variable', ci = False);
```

    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_59_1.png)
    


We see that indeed in the central hours there is a loss of efficiency. But nowhere near the level of loss that we had seen in the previous analysis.

We are going to analyze the distribution of efficiency in those hours.


```python
temp = df.between_time('08:00:00','15:00:00')
temp = temp[temp.planta == 'p2']
```


```python
temp.eficiencia.plot.density();
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_62_0.png)
    


There is a data set with zero efficiency, and that is what causes the problem. But what is the cause of that zero efficiency?

We are going to select those cases and review them.


```python
temp[temp.kw_dc == 0]
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
      <th>date</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-05-15 09:45:00</th>
      <td>p2</td>
      <td>5</td>
      <td>15</td>
      <td>9</td>
      <td>45</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.80</td>
      <td>31.38</td>
      <td>45.72</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1645.00</td>
      <td>1215280381.00</td>
      <td>2020-05-15</td>
    </tr>
    <tr>
      <th>2020-05-15 09:45:00</th>
      <td>p2</td>
      <td>5</td>
      <td>15</td>
      <td>9</td>
      <td>45</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.80</td>
      <td>31.38</td>
      <td>45.72</td>
      <td>Et9kgGMDl729KT4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1541.00</td>
      <td>1705791.00</td>
      <td>2020-05-15</td>
    </tr>
    <tr>
      <th>2020-05-15 09:45:00</th>
      <td>p2</td>
      <td>5</td>
      <td>15</td>
      <td>9</td>
      <td>45</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.80</td>
      <td>31.38</td>
      <td>45.72</td>
      <td>Quc1TzYxW2pYoWX</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1324.00</td>
      <td>329510409.00</td>
      <td>2020-05-15</td>
    </tr>
    <tr>
      <th>2020-05-15 09:45:00</th>
      <td>p2</td>
      <td>5</td>
      <td>15</td>
      <td>9</td>
      <td>45</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.80</td>
      <td>31.38</td>
      <td>45.72</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1735.00</td>
      <td>209145328.00</td>
      <td>2020-05-15</td>
    </tr>
    <tr>
      <th>2020-05-15 10:00:00</th>
      <td>p2</td>
      <td>5</td>
      <td>15</td>
      <td>10</td>
      <td>0</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.83</td>
      <td>31.89</td>
      <td>46.13</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1645.00</td>
      <td>1215280381.00</td>
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
      <th>2020-06-16 14:30:00</th>
      <td>p2</td>
      <td>6</td>
      <td>16</td>
      <td>14</td>
      <td>30</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.56</td>
      <td>30.83</td>
      <td>44.38</td>
      <td>q49J1IKaHRwDQnt</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>34379.33</td>
      <td>2020-06-16</td>
    </tr>
    <tr>
      <th>2020-06-16 14:30:00</th>
      <td>p2</td>
      <td>6</td>
      <td>16</td>
      <td>14</td>
      <td>30</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.56</td>
      <td>30.83</td>
      <td>44.38</td>
      <td>rrq4fwE8jgrTyWY</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>8075096.33</td>
      <td>2020-06-16</td>
    </tr>
    <tr>
      <th>2020-06-16 14:30:00</th>
      <td>p2</td>
      <td>6</td>
      <td>16</td>
      <td>14</td>
      <td>30</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.56</td>
      <td>30.83</td>
      <td>44.38</td>
      <td>vOuJvMaM2sgwLmb</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>173022.79</td>
      <td>2020-06-16</td>
    </tr>
    <tr>
      <th>2020-06-16 14:30:00</th>
      <td>p2</td>
      <td>6</td>
      <td>16</td>
      <td>14</td>
      <td>30</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.56</td>
      <td>30.83</td>
      <td>44.38</td>
      <td>xMbIugepa2P7lBB</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7126074.93</td>
      <td>2020-06-16</td>
    </tr>
    <tr>
      <th>2020-06-16 14:30:00</th>
      <td>p2</td>
      <td>6</td>
      <td>16</td>
      <td>14</td>
      <td>30</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.56</td>
      <td>30.83</td>
      <td>44.38</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>13955359.33</td>
      <td>2020-06-16</td>
    </tr>
  </tbody>
</table>
<p>3667 rows × 16 columns</p>
</div>



Parece que no es problema del inverter, si no de que en esos momentos no se ha generado DC.

Vamos a poner la condición de que DC > 0 y ver ahí cual es la eficiencia.


```python
temp[temp.kw_dc > 0].eficiencia.plot.density();
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_66_0.png)
    


Indeed when there is DC the efficiency is higher than 96%.

The question then is why is there no DC? Is there a pattern?

Let's create a DC = 0 flag so we can analyze it.


```python
temp['kw_dc_cero'] = np.where(temp['kw_dc'] == 0, 1, 0)
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
      <th>date</th>
      <th>kw_dc_cero</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-05-15 08:00:00</th>
      <td>p2</td>
      <td>5</td>
      <td>15</td>
      <td>8</td>
      <td>0</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.46</td>
      <td>27.68</td>
      <td>35.71</td>
      <td>4UPUqMRk7TRMgml</td>
      <td>581.05</td>
      <td>569.41</td>
      <td>98.00</td>
      <td>554.00</td>
      <td>2429565.00</td>
      <td>2020-05-15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-05-15 08:00:00</th>
      <td>p2</td>
      <td>5</td>
      <td>15</td>
      <td>8</td>
      <td>0</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.46</td>
      <td>27.68</td>
      <td>35.71</td>
      <td>81aHJ1q11NBPMrL</td>
      <td>534.67</td>
      <td>524.09</td>
      <td>98.02</td>
      <td>516.60</td>
      <td>1215279252.60</td>
      <td>2020-05-15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-05-15 08:00:00</th>
      <td>p2</td>
      <td>5</td>
      <td>15</td>
      <td>8</td>
      <td>0</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.46</td>
      <td>27.68</td>
      <td>35.71</td>
      <td>9kRcWv60rDACzjR</td>
      <td>568.53</td>
      <td>557.16</td>
      <td>98.00</td>
      <td>551.80</td>
      <td>2247720128.80</td>
      <td>2020-05-15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-05-15 08:00:00</th>
      <td>p2</td>
      <td>5</td>
      <td>15</td>
      <td>8</td>
      <td>0</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.46</td>
      <td>27.68</td>
      <td>35.71</td>
      <td>Et9kgGMDl729KT4</td>
      <td>526.24</td>
      <td>515.83</td>
      <td>98.02</td>
      <td>503.00</td>
      <td>1704753.00</td>
      <td>2020-05-15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-05-15 08:00:00</th>
      <td>p2</td>
      <td>5</td>
      <td>15</td>
      <td>8</td>
      <td>0</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.46</td>
      <td>27.68</td>
      <td>35.71</td>
      <td>IQ2d7wF4YD8zU1Q</td>
      <td>578.17</td>
      <td>566.58</td>
      <td>97.99</td>
      <td>552.79</td>
      <td>19942078.79</td>
      <td>2020-05-15</td>
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
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2020-06-17 15:00:00</th>
      <td>p2</td>
      <td>6</td>
      <td>17</td>
      <td>15</td>
      <td>0</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.36</td>
      <td>27.23</td>
      <td>29.35</td>
      <td>q49J1IKaHRwDQnt</td>
      <td>562.34</td>
      <td>551.13</td>
      <td>98.01</td>
      <td>3380.87</td>
      <td>519981.87</td>
      <td>2020-06-17</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-06-17 15:00:00</th>
      <td>p2</td>
      <td>6</td>
      <td>17</td>
      <td>15</td>
      <td>0</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.36</td>
      <td>27.23</td>
      <td>29.35</td>
      <td>rrq4fwE8jgrTyWY</td>
      <td>534.27</td>
      <td>523.71</td>
      <td>98.02</td>
      <td>3190.40</td>
      <td>121130615.40</td>
      <td>2020-06-17</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-06-17 15:00:00</th>
      <td>p2</td>
      <td>6</td>
      <td>17</td>
      <td>15</td>
      <td>0</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.36</td>
      <td>27.23</td>
      <td>29.35</td>
      <td>vOuJvMaM2sgwLmb</td>
      <td>578.85</td>
      <td>567.15</td>
      <td>97.98</td>
      <td>3534.07</td>
      <td>2426903.07</td>
      <td>2020-06-17</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-06-17 15:00:00</th>
      <td>p2</td>
      <td>6</td>
      <td>17</td>
      <td>15</td>
      <td>0</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.36</td>
      <td>27.23</td>
      <td>29.35</td>
      <td>xMbIugepa2P7lBB</td>
      <td>568.86</td>
      <td>557.49</td>
      <td>98.00</td>
      <td>3433.50</td>
      <td>106895609.50</td>
      <td>2020-06-17</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-06-17 15:00:00</th>
      <td>p2</td>
      <td>6</td>
      <td>17</td>
      <td>15</td>
      <td>0</td>
      <td>iq8k7ZNt4Mwm3w0</td>
      <td>0.36</td>
      <td>27.23</td>
      <td>29.35</td>
      <td>xoJJ8DcxJEcupym</td>
      <td>578.49</td>
      <td>566.90</td>
      <td>98.00</td>
      <td>3534.67</td>
      <td>209334959.67</td>
      <td>2020-06-17</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>20376 rows × 17 columns</p>
</div>



We will start with the numerical variables.


```python
temp.groupby('kw_dc_cero')[['irradiacion','t_ambiente','t_modulo']].mean()
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
      <th>irradiacion</th>
      <th>t_ambiente</th>
      <th>t_modulo</th>
    </tr>
    <tr>
      <th>kw_dc_cero</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.59</td>
      <td>30.48</td>
      <td>44.32</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.80</td>
      <td>32.48</td>
      <td>52.03</td>
    </tr>
  </tbody>
</table>
</div>



At room temperature there is not much difference, but at module temperature and irradiation yes.

Could it be that if it gets too hot the module stops generating DC?

Let's see it by comparing the module temperature with the DC generation.


```python
sns.scatterplot(data = temp, x = 't_modulo', y = 'kw_dc',hue = 'kw_dc_cero');
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_72_0.png)
    


The previous hypothesis is not confirmed, since there are many cases of high temperatures where DC is generated, and also of kw_dc equal to zero in almost all temperature ranges.

We are now going to analyze the categorical ones, starting with the inverter.


```python
temp.groupby('inverter_id').kw_dc_cero.mean().sort_values(ascending = False).plot.bar();
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_74_0.png)
    


There is a big difference in the percentage of zero DC production per inverter.

From some that have less than 5% to some that exceed 30%.

**INSIGHT #4:**: On plant 2 there are several inverters that are not getting enough DC production, and therefore whose modules need revision.

We are going to analyze the inverters from the point of view of the average efficiency to see if there are "good and bad".


```python
temp[temp.kw_dc > 0].groupby(['inverter_id','date'],as_index = False).eficiencia.mean().boxplot(column = 'eficiencia', by = 'inverter_id', figsize = (14,10))
plt.xticks(rotation = 90);
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_77_0.png)
    


**INSIGHT #5:**: Once discounting the problem of not generating DC, the inverters of plant 2 do work well and do the job of transformation to AC well.

To finish analyzing the efficiency of the inverters, we can see their performance on each of the days to see if there may have been specific problems.

```python
temp[temp.kw_dc > 0].groupby(['inverter_id','date']).eficiencia.mean().unstack(level = 0).plot(subplots = True, sharex=True, figsize=(20,40))
plt.xticks(rotation = 90);
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_80_0.png)
    

To have a term of comparison we are going to repeat the analyzes with plant 1.


```python
temp = df.between_time('08:00:00','15:00:00')
temp = temp[temp.planta == 'p1']
temp['kw_dc_cero'] = np.where(temp['kw_dc'] == 0, 1, 0)
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
      <th>date</th>
      <th>kw_dc_cero</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-05-15 08:00:00</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>8</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.20</td>
      <td>25.42</td>
      <td>31.41</td>
      <td>1BY6WEcLGh8j5v7</td>
      <td>3246.00</td>
      <td>318.67</td>
      <td>9.82</td>
      <td>263.57</td>
      <td>6259822.57</td>
      <td>2020-05-15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-05-15 08:00:00</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>8</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.20</td>
      <td>25.42</td>
      <td>31.41</td>
      <td>1IF53ai7Xc0U56Y</td>
      <td>2805.62</td>
      <td>275.46</td>
      <td>9.82</td>
      <td>292.50</td>
      <td>6183937.50</td>
      <td>2020-05-15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-05-15 08:00:00</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>8</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.20</td>
      <td>25.42</td>
      <td>31.41</td>
      <td>3PZuoBAID5Wc2HD</td>
      <td>2736.12</td>
      <td>268.62</td>
      <td>9.82</td>
      <td>287.75</td>
      <td>6988046.75</td>
      <td>2020-05-15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-05-15 08:00:00</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>8</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.20</td>
      <td>25.42</td>
      <td>31.41</td>
      <td>7JYdWkrLSPkdwr4</td>
      <td>2741.50</td>
      <td>269.15</td>
      <td>9.82</td>
      <td>281.00</td>
      <td>7603241.00</td>
      <td>2020-05-15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-05-15 08:00:00</th>
      <td>p1</td>
      <td>5</td>
      <td>15</td>
      <td>8</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.20</td>
      <td>25.42</td>
      <td>31.41</td>
      <td>McdE0feGgRqW7Ca</td>
      <td>3208.88</td>
      <td>315.05</td>
      <td>9.82</td>
      <td>291.00</td>
      <td>7159255.00</td>
      <td>2020-05-15</td>
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
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2020-06-17 15:00:00</th>
      <td>p1</td>
      <td>6</td>
      <td>17</td>
      <td>15</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.32</td>
      <td>28.62</td>
      <td>39.95</td>
      <td>uHbuxQJl8lW7ozc</td>
      <td>4719.62</td>
      <td>462.89</td>
      <td>9.81</td>
      <td>5423.50</td>
      <td>7286458.50</td>
      <td>2020-06-17</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-06-17 15:00:00</th>
      <td>p1</td>
      <td>6</td>
      <td>17</td>
      <td>15</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.32</td>
      <td>28.62</td>
      <td>39.95</td>
      <td>wCURE6d3bPkepu2</td>
      <td>5077.75</td>
      <td>497.80</td>
      <td>9.80</td>
      <td>5343.75</td>
      <td>7028061.75</td>
      <td>2020-06-17</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-06-17 15:00:00</th>
      <td>p1</td>
      <td>6</td>
      <td>17</td>
      <td>15</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.32</td>
      <td>28.62</td>
      <td>39.95</td>
      <td>z9Y9gH1T5YWrNuG</td>
      <td>5113.00</td>
      <td>501.29</td>
      <td>9.80</td>
      <td>5282.88</td>
      <td>7250667.88</td>
      <td>2020-06-17</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-06-17 15:00:00</th>
      <td>p1</td>
      <td>6</td>
      <td>17</td>
      <td>15</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.32</td>
      <td>28.62</td>
      <td>39.95</td>
      <td>zBIq5rxdHJRwDNY</td>
      <td>4675.38</td>
      <td>458.61</td>
      <td>9.81</td>
      <td>5284.75</td>
      <td>6582836.75</td>
      <td>2020-06-17</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-06-17 15:00:00</th>
      <td>p1</td>
      <td>6</td>
      <td>17</td>
      <td>15</td>
      <td>0</td>
      <td>HmiyD2TTLFNqkNe</td>
      <td>0.32</td>
      <td>28.62</td>
      <td>39.95</td>
      <td>zVJPv84UY57bAof</td>
      <td>4853.75</td>
      <td>475.96</td>
      <td>9.81</td>
      <td>5368.75</td>
      <td>7362730.75</td>
      <td>2020-06-17</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>21450 rows × 17 columns</p>
</div>




```python
temp.eficiencia.plot.density();
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_83_0.png)
    


We see that no, here all the inverters have a constant efficiency (although very low)


```python
temp.groupby(['inverter_id','date'],as_index = False).eficiencia.mean().boxplot(column = 'eficiencia', by = 'inverter_id', figsize = (14,10))
plt.xticks(rotation = 90);
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_85_0.png)
    


We see that except for specific days in some inverters, in the rest the efficiency is constant.

We are going to review the average daily efficiency for each inverter.


```python
temp.groupby(['inverter_id','date']).eficiencia.mean().unstack(level = 0).plot(subplots = True, sharex=True, figsize=(20,40))
plt.xticks(rotation = 90);
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_88_0.png)
    


In the inverter analysis we see again that all the data are constant.

We are going to verify that then there are no failures in the generation of DC.


```python
temp.groupby('inverter_id').kw_dc_cero.mean().sort_values(ascending = False).plot.bar();
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_90_0.png)
    


We see that although there are some inverters that have had failures, their magnitude is less than 2% of the measurements.

Therefore the generation of DC in plant 1 is correct, and the failure is in the transformation from DC to AC.

## CONCLUSIONS

After an analysis of the data we can conclude that:
    
* There are serious data quality problems. It should be reviewed in which part of the chain these problems are generated, including the meters of the plants.
* The fact that the DC generation is about 10 times higher in plant 1 than in plant 2, added to the fact that the efficiency in plant 1 is over 10% leads us to think that the DC generation data on floor 1 it may be artificially scaled for some reason.
* But for now, in the absence of verification, we will assume that the data is correct.
* The two plants have received high amounts of irradiation, we have not located any problem at this stage
* Although the ambient temperature is higher on floor 2 and its modules get hotter than those on floor 1, this does not seem to have a significant impact
* Plant 1 DC generation works fine, the modules seem to bring DC to the inverters.
* The DC generation of plant 2 does NOT work well, some modules carry very little DC to the inverters even in the hours of greatest irradiation.
* The transformation from DC to AC of floor 1 does NOT work well, it only transforms around 10%, yes, constantly. And this low efficiency is not due to moments of non-reception of DC nor is it concentrated in specific inverters, but rather it seems more structural (again keep in mind that it could be due to a data quality problem in kw_dc of plant 1
* The transformation from DC to AC of plant 2 works well, since once the periods of zero DC generation are eliminated, the rest have an efficiency greater than 97%

Recommendations:

* Review the data collection and its reliability
* Maintenance check on the inverter modules of plant 2 in which there are many moments of zero DC generation
* Maintenance review of the inverters of Plant 1
