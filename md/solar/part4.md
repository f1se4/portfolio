# ANALISIS E INSIGHTS

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



## ANALISIS E INSIGHTS

La primera palanca es la recepción de la energía solar.

Tenemos 3 kpis con los que medir esta palanca: irradiación que llega, temperatura ambiente y temperatura del módulo.

Estos kpis se miden con un único sensor por planta, así que el dato es el mismo para todos los inverters.

Tenemos que entender cómo funcionan estas variables entre sí antes de pasar a ver cómo interactúan con el siguiente nivel.

Dado que da igual el inverter y solo necesitamos esas 3 variables vamos a crear un dataset más pequeño con solo un inverter de cada planta para trabajar sobre el.


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



### ¿Las dos plantas reciben la misma cantidad de energía solar?


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
    


Conclusiones:

* En general la planta 2 recibe más energía solar que la 1
* Pero esta diferencia no puede implicar el problema de rendimiento que supuestamente existe

### ¿Cómo se relacionan esas tres variables?


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


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_16_0.png)
    



```python
sns.pairplot(temp.reset_index(), hue = 'planta', height=3, plot_kws={'alpha': 0.1});
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_17_0.png)
    


Conclusiones:

* La irradiación correlaciona mucho con la temperatura del módulo
* Pero no tanto con la temperatura ambiente
* Por tanto una primera forma de identificar módulos defectuosos o sucios es localizar los que produzcan poco cuando la irradiación es alta

### ¿Cómo se distribuye la irradiación y la temperatura a lo largo del día?


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


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_21_0.png)
    



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
    


Conclusiones:

* Ambas plantas tienen patrones similares. Podríamos pensar que están en zonas geográficas no muy alejadas
* Existe irradiación (y por tanto a priori las plantas deberían producir) entre las 7 y las 17
* La irradiación máxima se produce entre las 11 y las 12
* La temperatura ambiente máxima se produce entre las 14 y las 16

### ¿Ambas plantas son igual de capaces de generar DC a partir de la irradiación?


```python
plt.figure(figsize = (12,8))
sns.scatterplot(data = df, x = df.irradiacion, y = df.kw_dc);
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_26_0.png)
    


Existen 2 patrones claramente diferentes. ¿Serán las plantas?


```python
plt.figure(figsize = (12,8))
sns.scatterplot(data = df, x = df.irradiacion, y = df.kw_dc, hue = 'planta');
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_28_0.png)
    


La planta número 2 produce muchos menos kw ante los mismos niveles de irradiación.

Pero antes habíamos visto que la relación entre dc y ac en la planta 1 era rara.

Y también que los datos de dc y ac no cuadraban con los de kw_dia.

Hay algo raro en los datos.

Vamos a ver la relación entre la irradiación y kw_dia a ver si nos da luz.


```python
plt.figure(figsize = (12,10))
sns.scatterplot(data = df, x = df.irradiacion, y = df.kw_dia, hue = 'planta');
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_30_0.png)
    


Es muy extraño. Parece que la relación es que a más irradiación menos kw generados. Lo cual no tiene sentido.

Incluso parece que los máximos de kw se producen en horas de irradiación cero.

¿Te imaginas qué puede estar pasando?

CUIDADO: la variable kw_dia es un ACUMULADO. Eso significa que debería alcanzar su máximo cuando llega la última hora del día, por ej las 23:45, donde obviamente la irradiación es cero.

Y no tener datos hsta pasadas las 7 que es cuando vemos que hay irradiación.

Vamos a comprobarlo.


```python
df.groupby('hora')[['kw_dia']].mean().plot.bar();
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_33_0.png)
    


De nuevo algo no cuadra. Hay generación entre las 00 y las 06.

Y además a partir de las 18 comienza a decaer, lo cual no debería pasar si es un acumulado.

Conclusión:

No nos fiamos de estas variables acumuladas como kw_dia y kw_total.

Pero la verdad es que tampoco nos fiamos mucho de las otras.

En una situación real yo pararía el proyecto hasta ser capaz de ver qué pasa con los datos.

Pero para poder continuar vamos a asumir que los datos de dc y ac son correctos.

Y bajo esa asunción obtendremos nuestras conclusiones.

**INSIGHT #1**

La planta 2 genera niveles mucho más bajos de DC incluso a niveles similares de irradiación

### ¿La generación es constante a lo largo de los días?

Podemos usar el df_dia para graficar la visión global de generación de DC durante el período de análisis.


```python
plt.figure(figsize = (10,8))
sns.lineplot(data = df_dia.reset_index(), x = df_dia.reset_index().fecha, y = 'kw_dc_sum', hue = 'planta');
```


    
![png](static/notebooks/solar/04_AnalisisInsights_files/04_AnalisisInsights_38_0.png)
    


Vemos que la planta 1 tiene mucha más variabilidad mientras que la planta 2 es mucho más constante.

Pero sobre todo nos extraña los bajos niveles de generacion de DC en de la planta 2 en comparación con la 1.

Vamos a examinar la generación de cada día a ver si vemos algo raro.

Generamos una variable date para poder agregar por ella.


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



Creamos un dataframe temporal para analizar la generación de DC horaria en cada día en la planta 1.


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



Vamos a pasar date a columnas, para poder respresentar cada columna (que son los dates) como una variable y por tanto como un gráfico independiente.


```python
dc_constante_p1.unstack(level = 1).plot(subplots = True, layout = (17,2), sharex=True, figsize=(20,30));
```


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_45_0.png)
    


Conclusiones:

* En la planta 1 sí se mantienen unos patrones similares durante todos los días
* A excepción de un parón el día 20 de Mayo y una caída extraña el 05 de Junio
* Pero ninguna parece ser estructural
* Por tanto aunque cada día pudiera tener diferentes totales de producción los patrones intradía son similares y parecen correctos

Repetimos el análisis en la planta 2


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



Vamos a pasar date a columnas, para poder respresentar cada columna (que son los dates) como una variable y por tanto como un gráfico independiente.


```python
dc_constante_p2.unstack(level = 1).plot(subplots = True, layout = (17,2), sharex=True, figsize=(20,30));
```


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_50_0.png)
    


Conclusiones:

* De nuevo el día 20 de Mayo aparece con un comportamiento raro
* Los niveles de producción son constantes durante los días, pero siempre unas 10 veces por debajo de los nivels de la planta 1

**INSIGHT #2:** Los niveles bajos de la planta 2 son constantes y presentan unas curvas diarias que parecen normales.

### ¿La conversión de DC a AC se genera correctamente?


```python
sns.scatterplot(data = df, x = df.kw_dc, y = df.kw_ac, hue = df.planta);
```


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_53_0.png)
    


De nuevo los patrones son clarísimos: la planta 2 transforma la corriente de forma mucho más eficiente.

Vamos a ampliar analizando la variable eficiencia que habíamos creado.


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


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_56_0.png)
    


**INSIGHT #3**

La planta 1 tiene una capacidad de transformar DC a AC bajísima, lo cual sugiere problemas con los inverters

Otras conclusiones:

* Entrar en el detalle de los inverters de la planta 1, a ver si son todos o hay algunos que sesgan la media
* Revisar por qué la planta 2 pierde eficiencia durante las horas de más irradiación

Vamos a empezar por la segunda, comparando la producción de DC con la de AC en la planta 2.


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

    C:\Users\f1se4\AppData\Local\Temp\ipykernel_26308\981826885.py:2: FutureWarning: 
    
    The `ci` parameter is deprecated. Use `errorbar=('ci', False)` for the same effect.
    
      sns.lineplot(data = temp[temp.planta == 'p2'], x = 'hora', y = 'value', hue = 'variable', ci = False);
    


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_59_1.png)
    


Vemos que efectivamente en las horas centrales hay pérdida de eficiencia. Pero ni de lejos el nivel de pérdida que habíamos visto en el análisis anterior.

Vamos a analizar la distribución de la eficiencia en esas horas.


```python
temp = df.between_time('08:00:00','15:00:00')
temp = temp[temp.planta == 'p2']
```


```python
temp.eficiencia.plot.density();
```


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_62_0.png)
    


Hay un conjunto de datos con eficiencia cero, y es lo que genera el problema. ¿Pero cual es la causa de esa eficiencia cero?

Vamos a seleccionar esos casos y revisarlos.


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


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_66_0.png)
    


Efectivamente cuando hay DC la eficiencia es superior al 96%.

La pregunta entonces es ¿por qué no hay DC? ¿Hay algún patrón?

Vamos a crear un indicador de DC = 0 para poder analizarlo.


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



Empezamos por las variables numéricas.


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



En la temperatura ambiente no hay mucha diferencia, pero en la del módulo y en la irradiación sí.

¿Podría ser que si se calienta demasiado el módulo deje de generar DC?

Vamos a verlo comparando la temperatura del módulo con la generación de DC.


```python
sns.scatterplot(data = temp, x = 't_modulo', y = 'kw_dc',hue = 'kw_dc_cero');
```


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_72_0.png)
    


La hipótesis anterior no se confirma, ya que hay muchos casos de temperaturas altas donde se genera DC, y también de kw_dc igual a cero en casi todos los rangos de temperaturas.

Vamos a analizar ahora las categóricas, empezando por el inverter.


```python
temp.groupby('inverter_id').kw_dc_cero.mean().sort_values(ascending = False).plot.bar();
```


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_74_0.png)
    


Existe gran diferencia en el porcentaje de producción cero de DC por inverter.

Desde algunos que tienen menos del 5% hasta algunos que superan el 30%.

**INSIGHT #4:**: En la planta 2 existen varios inverters a los que no está llegando suficiente producción de DC, y por tanto cuyos módulos necesitan revisión.

Vamos a analizar los inverters desde el punto de vista de la eficiencia media para ver si hay "buenos y malos".


```python
temp[temp.kw_dc > 0].groupby(['inverter_id','date'],as_index = False).eficiencia.mean().boxplot(column = 'eficiencia', by = 'inverter_id', figsize = (14,10))
plt.xticks(rotation = 90);
```


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_77_0.png)
    


**INSIGHT #5:**: Una vez descontando el problema de la no generación de DC, los inverters de la planta 2 sí funcionan bien y hacen bien el trabajo de transformación a AC.

Para terminar de analizar la eficiencia de los inverters podemos ver su rendimiento en cada  uno de los días para ver si han posido existir problemas puntuales


```python
temp[temp.kw_dc > 0].groupby(['inverter_id','date']).eficiencia.mean().unstack(level = 0).plot(subplots = True, sharex=True, figsize=(20,40))
plt.xticks(rotation = 90);
```


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_80_0.png)
    


Para tener un término de comparación vamos a repetir los análisis con la planta 1.


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


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_83_0.png)
    


Vemos que no, aquí todos los inverters tienen una eficiencia constante (aunque muy baja)


```python
temp.groupby(['inverter_id','date'],as_index = False).eficiencia.mean().boxplot(column = 'eficiencia', by = 'inverter_id', figsize = (14,10))
plt.xticks(rotation = 90);
```


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_85_0.png)
    


Vemos que salvo días puntuales en algunos inverters en el resto la eficiencia es constante.

Vamos a revisar la eficiencia media diaria por cada inverter.


```python
temp.groupby(['inverter_id','date']).eficiencia.mean().unstack(level = 0).plot(subplots = True, sharex=True, figsize=(20,40))
plt.xticks(rotation = 90);
```


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_88_0.png)
    


En el análisis por inverter vemos de nuevo que todos los datos son constantes.

Vamos a comprobar que entonces no hay fallos en la generación de DC.


```python
temp.groupby('inverter_id').kw_dc_cero.mean().sort_values(ascending = False).plot.bar();
```


    
![png](04_AnalisisInsights_files/04_AnalisisInsights_90_0.png)
    


Vemos que aunque hay algunos inverters que han tenido fallos su magnitud es inferior al 2% de las mediciones.

Por tanto la generación de DC en la planta 1 sí es correcta, y el fallo está en la transformación de DC a AC.

## CONCLUSIONES

Tras un ananálisis de los datos podemos concluir que:
    
* Existen graves problemas de calidad de datos. Se debería revisar en qué parte de la cadena se generan estos problemas, incluyendo los medidores de las plantas.
* El hecho de que la generación en DC sea unas 10 veces superior en la planta 1 que en la 2, sumado al hecho de que la eficiencia en la planta 1 esté sobre el 10% nos lleva a pensar que el dato de generación de DC en la planta 1 puede estar artificialmente escalado por algún motivo.
* Pero de momento a falta de comprobación vamos a asumir que los datos son correctos.
* La dos plantas han recibido altas cantidades de irradiación, no hemos localizado ningún problema en esta fase
* Aunque la temperatura ambiente es superior en la planta 2 y sus módulos se calientan más que los de la planta 1 esto no parece tener un impacto significativo
* La generación de DC de la planta 1 funciona bien, los módulos parecen llevar DC a los inverters.
* La generación de DC de la planta 2 NO funciona bien, algunos módulos llevan muy poco DC a los inverters incluso en las horas de mayor irradiación.
* La transformación de DC a AC de la planta 1 NO funciona bien, solo se transforma en torno al 10%, eso sí, de forma constante. Y esta baja eficiencia no es debida a momentos de no recepción de DC ni se concentra en inverters concretos, si no que parece más estructural (de nuevo tener en cuenta que podría deberse a un problema de calidad de datos en kw_dc de la planta 1
* La transformación de DC a AC de la planta 2 funciona bien, ya que una vez eliminados los períodos de generación cero de DC el resto tienen una eficiencia superior al 97%

Recomendaciones:

* Revisar la captación de datos y su fiabilidad
* Revisión de mantenimiento en los módulos de los inverters  de la planta 2 en los que hay muchos momentos de generación cero de DC
* Revisión de mantenimiento de los inverters de la Planta 1
