# PREPARACION DE DATOS

En esta fase vamos a crear nuevas variables o transformar las existentes para poder dar mejor respuesta a nuestro objetivo.

Vamos a poner ejemplos tanto de como usar las variables internas como de cómo enriquecer con variables externas.

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

## CARGA DE DATOS


```python
con = sa.create_engine('sqlite:///../DatosCaso1/airbnb.db')

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
    </tr>
  </tbody>
</table>
</div>



## PREPARACION DE VARIABLES

### Creacion de kpis de palancas

Primero vamos a crear las variables de análisis, es decir las que habíamos identificado como los Kpis que usaremos en las palancas que influyen sobre el negocio.

Habíamos dicho que eran 3:

* precio por noche: esta ya la tenemos directamente en la variable price, pero vamos a revisarla para ver que la entendemos bien
* ocupación: tenemos availability_365 pero hay que transformarla
* precio del inmueble: esta tendremos que crearla con variables externas así que la dejamos para después

**Empezamos con el precio.**

La documentación no aclara si el precio es por todo el inmueble, o si en el caso de que se alquile una habitación es por habitación.

Es un dato clave para poder hacer la valoración de los potenciales ingresos de un inmueble.

Vamos a intentar entenderlo analizando el precio medio por tipo de alquiler.

Es importante filtrar por solo un distrito para no incluir el efecto "zona".

Así que primero elegimos un distrito que tenga muchos datos.


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



Conclusión:
    
* alquilar el apartamento tiene un precio medio de 148€
* alquilar una habitación tiene un precio medio de 60€ o 67€ según sea compartida o privada
* por tanto para calcular los "ingresos" de un inmueble sí deberemos multiplicar el precio el precio por el número de habitaciones cuando sea de los tipos Private room o Shared room

Ahora bien, multiplicar el precio por el total de habitaciones puede sesgar artificialmente al alza la capacidad de generar ingresos de un inmueble.

Ya que si se alquila por habitaciones no es probable que siempre esté al 100%

Por tanto deberíamos ponderarlo por el porcentaje medio de habitaciones alquiladas.

No tenemos ese dato, pero supongamos que hemos hablado con el responsable de negocio y nos ha dicho que es del 70%.

Podemos crear la variable precio total aplicando apply sobre una función personalizada.


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



**Ahora vamos con la ocupación**

La variable que tenemos que nos permite medir esto es availability_365.

Esta variable nos dice el número de días a un año vista que el inmueble NO está ocupado.

Por tanto nos interesaría transformarla a una medida más directa de ocupación, por ejemplo el % del año que SI está ocupada.

Podemos hacerlo con una tranformación directa.


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
    </tr>
  </tbody>
</table>
</div>



### Transformación de varaibles de análisis

Algunas de las preguntas semilla están dirigidas a comprobar cómo se comporta el precio o la ocupación según otras variables como el número de habitaciones, la media de valoraciones, etc.

Normalmente podremos hacer mejor estos análisis si discretizamos la variable de análisis.

En nuestro caso las candidatas para este análisis son: accommodates, bedrooms, beds y number_of_reviews.

En bedrooms tiene sentido una discretización más personalizada. En las otras podemos hacerla automática.

**Discretizar bedrooms**

Comenzamos por evaluar la distribución de los datos.


```python
df.bedrooms.value_counts().plot.bar();
```


    
![png](04_Preparacion%20de%20datos_files/04_Preparacion%20de%20datos_23_0.png)
    


Vamos a discretizar para 1,2,3 y más de 3.

Podemos usar np.select


```python
condiciones = [df.bedrooms == 1,
               df.bedrooms == 2,
               df.bedrooms == 3,
               df.bedrooms > 3]

resultados = ['01_Una','02_Dos','03_Tres','04_Cuatro o mas']

df['bedrooms_disc'] = np.select(condiciones, resultados, default = -999)
```

Comprobamos


```python
df.bedrooms_disc.value_counts().plot.bar();
```


    
![png](04_Preparacion%20de%20datos_files/04_Preparacion%20de%20datos_27_0.png)
    


**Discretizar accommodates, beds y number_of_reviews**

Vamos a usar qcut para discritizar con percentiles 0.5, 0.8, 1


```python
df['accommodates_disc'] = pd.qcut(df.accommodates,[0, 0.5, 0.8, 1],
                                 labels = ['0-2','3','4-16'])

df['accommodates_disc'].value_counts().sort_index(ascending = False).plot.barh();
```


    
![png](04_Preparacion%20de%20datos_files/04_Preparacion%20de%20datos_29_0.png)
    



```python
df['beds_disc'] = pd.qcut(df.beds,[0, 0.5, 0.8, 1],
                         labels = ['1','2','3-24'])

df['beds_disc'].value_counts().sort_index(ascending = False).plot.barh();
```


    
![png](04_Preparacion%20de%20datos_files/04_Preparacion%20de%20datos_30_0.png)
    



```python
df['number_of_reviews_disc'] = pd.qcut(df.number_of_reviews,[0, 0.5, 0.8, 1],
                                      labels = ['1-4','5-48','48-744'])

df['number_of_reviews_disc'].value_counts().sort_index(ascending = False).plot.barh();
```


    
![png](04_Preparacion%20de%20datos_files/04_Preparacion%20de%20datos_31_0.png)
    


### Creación de variables con datos externos

En este caso en concreto se podrían hacer muchas cosas con datos externos.

Lo primero, que ya hemos incorporado parcialmente, es la palanca del precio del inmueble.

Decíamos que la podíamos estimar multiplicando los metros cuadrados del inmueble por el precio por m2.

El precio_m2 ya lo hemos conseguido, pero el tamaño del inmueble no lo tenemos en los datos.

Lo que podemos hacer es establecer unos criterios en base al número de habitaciones.

No es perfecto, pero nos servirá de aproximación.

**Estimación de los metros cuadrados del inmueble**

Vamos usar el siguiente algoritmo:

* una habitación: m2 = 50
* dos habitaciones: m2 = 70
* tres habitaciones: m2 = 90
* cuatro habitaciones: m2 = 120
* cinco o más habitaciones: m2 = 150


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



Ahora ya podemos estimar el precio de compra del inmueble.

Recordamos que al precio que nos sale le quitábamos un 30% por capacidad de negociación.


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
      <td>164</td>
      <td>5740.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>50</td>
      <td>Latina</td>
      <td>125</td>
      <td>4375.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>90</td>
      <td>Arganzuela</td>
      <td>155</td>
      <td>9765.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>186</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.0</td>
      <td>50</td>
      <td>Arganzuela</td>
      <td>155</td>
      <td>5425.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3.0</td>
      <td>90</td>
      <td>Arganzuela</td>
      <td>155</td>
      <td>9765.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>186</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>186</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2.0</td>
      <td>70</td>
      <td>Centro</td>
      <td>186</td>
      <td>9114.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>186</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>186</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2.0</td>
      <td>70</td>
      <td>Salamanca</td>
      <td>191</td>
      <td>9359.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>186</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>186</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>186</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>186</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1.0</td>
      <td>50</td>
      <td>Centro</td>
      <td>186</td>
      <td>6510.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2.0</td>
      <td>70</td>
      <td>Centro</td>
      <td>186</td>
      <td>9114.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2.0</td>
      <td>70</td>
      <td>Centro</td>
      <td>186</td>
      <td>9114.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>3.0</td>
      <td>90</td>
      <td>Centro</td>
      <td>186</td>
      <td>11718.0</td>
    </tr>
  </tbody>
</table>
</div>



Ahora vamos a poner un ejemplo de qué otro tipo de variables podemos construir.

En este caso podríamos hacer mucho con las coordenadas x,y.

Ya que en turismo la localización es muy importante.

Por ejemplo podríamos calcular las distancias a diferentes puntos de interés como monumentos, lugares de ocio, recintos deportivos, etc.

Simplemente como ejemplo vamos a calcular la distancia de cada inmueble a la Puerta del Sol.

Para ello buscamos en Google su longitud y latitud: https://www.123coordenadas.com/coordinates/81497-puerta-del-sol-madrid

Latitud: 40.4167278
Longitud: -3.7033387

**Cálculo de la distancia de cada inmueble a la Puerta del Sol**

Dada la curvatura de la tierra la distancia entre dos puntos a partir de su latitud y longitud se calcula con una fórmula que se llama distancia de Haversine.

Una búsqueda en Google nos da una función ya construída para calcularla que podemos adaptar: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points


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

Creamos la variable


```python
#Las coordenadas de la Puerta del Sol serán lat1 y lon1
lat1 = 40.4167278
lon1 = -3.7033387

df['pdi_sol'] = df.apply(lambda registro: haversine(lat1,lon1,registro.latitude,registro.longitude),axis = 1)
```

Comprobamos revisando la distancia media por distritos.


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



## GUARDAMOS EN EL DATAMART

Vamos a guardar esta version como df_preparado


```python
df.to_sql('df_preparado', con = con, if_exists = 'replace')
```




    17710


