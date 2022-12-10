# CREACIÓN DEL DATAMART ANALÍTICO

Realmente nuestro caso empezaría aquí.

Los data engineer o informáticos nos han dado acceso a la base de datos que contiene toda la información.

Y a partir de aquí tenemos que cargarla a Python y empezar a trabajar.

Podríamos unir ya los datos en esta fase y crear el "tablón analítico" para hacer después la calidad de datos, ya que en este caso los datos no son masivos.

Pero como buena práctica yo recomiendo hacer primero la calidad de datos individual de cada tabla, sobre todo porque si  el volumen fuera muy alto al unirlos todavía se multiplica más.

Por tanto inicialmente las dejaramos como tablas individuales, después aplicaremos calidad de datos y finalmente las uniremos para forma el tablón o más oficialmente el datamart analítico.

En este módulo vamos a:

1. Acceder a la base de datos
2. Importar los datos como dataframes de Pandas
3. Realizar la calidad de datos
4. Crear el datamart analítico
5. Guardarlo como una tabla en la base de datos para no tener que repetir el proceso

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
```

## IMPORTACION DE DATOS

### Datos internos

Crear la conexión a la base de datos


```python
con = sa.create_engine('sqlite:///../Datos/airbnb.db')
```

Si desconociéramos los nombres de las tablas que están en la base de datos, la doc de SqlAlchemy nos dice que podemos usar la función inspect.

https://docs.sqlalchemy.org/en/14/core/reflection.html#fine-grained-reflection-with-inspector


```python
from sqlalchemy import inspect
insp = inspect(con)
tablas = insp.get_table_names()
tablas
```




    ['df', 'df_preparado', 'listings', 'listings_det']



Cargar las tablas


```python
listings = pd.read_sql('listings', con)
listings_det = pd.read_sql('listings_det', con)
```

Truco PRO 1:

Cargar las tablas una a una suele ser lo más conveniente, pero si tuvieras por ejemplo 100 tablas podría ser pesado.

Un truco es crear los dataframes de forma dinámica, usando los nombres que ya teníamos en la lista tablas.

Para ello podemos usar la función exec dentro de un bucle que recorra la lista con los nombres de las tablas.

Esto es para usuarios avanzados, así que te dejo que lo investigues por tu cuenta, y si no lo entiendes no te preocupes, la opción manual te servirá en el 99% de los casos.


```python
# lo dejo comentado para que no lo ejecutes por error. Si lo quieres ejecutar quita las parrillas
# for tabla in tablas:
#     exec(f'{tabla} = pd.read_sql(tabla, con)')
```

Truco PRO 2:

*NOTA: Este truco solo sirve para cuando has cargado las tablas con la opción PRO. Si las has cargado con la opción manual no tiene sentido, por eso te lo dejo también comentado*

También podemos revisar las dimensiones de cada tabla de forma automática para ver que han cargado bien.

Para ello podemos usar eval() que hace que entienda el nombre de la tabla como un objeto y no como una cadena, y por tanto nos deje aplicar el método shape


```python
# lo dejo comentado para que no lo ejecutes por error. Si lo quieres ejecutar quita las parrillas
# for cada in tablas:
#     print(cada + ': ' + str(eval(cada).shape))
```

    df: (17710, 24)
    df_preparado: (17710, 34)
    listings: (18909, 19)
    listings_det: (18909, 75)


### Datos Externos

En nuestros datos no tenemos el precio de compra de un inmueble, pero habíamos visto que es una de las palancas principales.

Por tanto vasos a buscar esos datos de forma externa.

En esta página tenemos justo la info que necesitamos: https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/venta/madrid-comunidad/madrid-provincia/madrid/

Podemos extraerla de forma sencilla con el plugin instant data scraper de Chrome, y guardarla en nuestra carpeta Datos con el nombre 'precios_idealista.csv'

Cargamos los datos, quitamos el primer registro y seleccionamos solo las columnas de precio y distrito


```python
precio_m2 = pd.read_csv('../Datos/precios_idealista.csv') \
    .loc[1:,['table__cell','icon-elbow']] \
    .rename(columns = {'table__cell':'precio_m2','icon-elbow':'distrito'})
precio_m2
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
      <th>precio_m2</th>
      <th>distrito</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>4.085 €/m2</td>
      <td>Arganzuela</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.409 €/m2</td>
      <td>Barajas</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.123 €/m2</td>
      <td>Carabanchel</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.827 €/m2</td>
      <td>Centro</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.098 €/m2</td>
      <td>Chamartín</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5.381 €/m2</td>
      <td>Chamberí</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2.940 €/m2</td>
      <td>Ciudad Lineal</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3.568 €/m2</td>
      <td>Fuencarral</td>
    </tr>
    <tr>
      <th>9</th>
      <td>3.871 €/m2</td>
      <td>Hortaleza</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2.267 €/m2</td>
      <td>Latina</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4.033 €/m2</td>
      <td>Moncloa</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2.500 €/m2</td>
      <td>Moratalaz</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.918 €/m2</td>
      <td>Puente de Vallecas</td>
    </tr>
    <tr>
      <th>14</th>
      <td>4.788 €/m2</td>
      <td>Retiro</td>
    </tr>
    <tr>
      <th>15</th>
      <td>6.114 €/m2</td>
      <td>Salamanca</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2.591 €/m2</td>
      <td>San Blas</td>
    </tr>
    <tr>
      <th>17</th>
      <td>3.678 €/m2</td>
      <td>Tetuán</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1.995 €/m2</td>
      <td>Usera</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2.403 €/m2</td>
      <td>Vicálvaro</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2.354 €/m2</td>
      <td>Villa de Vallecas</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1.693 €/m2</td>
      <td>Villaverde</td>
    </tr>
  </tbody>
</table>
</div>



Limpiamos el precio:
    
1. quitando la unidad
2. quitando los puntos de separador de miles
3. cambiando el tipo a entero


```python
precio_m2['precio_m2'] = precio_m2.precio_m2.str.split(expand = True)[0].str.replace('.','',regex=False).astype('int')
precio_m2
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
      <th>precio_m2</th>
      <th>distrito</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>4085</td>
      <td>Arganzuela</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3409</td>
      <td>Barajas</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2123</td>
      <td>Carabanchel</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4827</td>
      <td>Centro</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5098</td>
      <td>Chamartín</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5381</td>
      <td>Chamberí</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2940</td>
      <td>Ciudad Lineal</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3568</td>
      <td>Fuencarral</td>
    </tr>
    <tr>
      <th>9</th>
      <td>3871</td>
      <td>Hortaleza</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2267</td>
      <td>Latina</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4033</td>
      <td>Moncloa</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2500</td>
      <td>Moratalaz</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1918</td>
      <td>Puente de Vallecas</td>
    </tr>
    <tr>
      <th>14</th>
      <td>4788</td>
      <td>Retiro</td>
    </tr>
    <tr>
      <th>15</th>
      <td>6114</td>
      <td>Salamanca</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2591</td>
      <td>San Blas</td>
    </tr>
    <tr>
      <th>17</th>
      <td>3678</td>
      <td>Tetuán</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1995</td>
      <td>Usera</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2403</td>
      <td>Vicálvaro</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2354</td>
      <td>Villa de Vallecas</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1693</td>
      <td>Villaverde</td>
    </tr>
  </tbody>
</table>
</div>



## CALIDAD DE DATOS

### Tabla listings

#### Visión general


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
      <th>index</th>
      <th>id</th>
      <th>name</th>
      <th>host_id</th>
      <th>host_name</th>
      <th>neighbourhood_group</th>
      <th>neighbourhood</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>room_type</th>
      <th>price</th>
      <th>minimum_nights</th>
      <th>number_of_reviews</th>
      <th>last_review</th>
      <th>reviews_per_month</th>
      <th>calculated_host_listings_count</th>
      <th>availability_365</th>
      <th>number_of_reviews_ltm</th>
      <th>license</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>6369</td>
      <td>Rooftop terrace room ,  ensuite bathroom</td>
      <td>13660</td>
      <td>Simon</td>
      <td>Chamartín</td>
      <td>Hispanoamérica</td>
      <td>40.45724</td>
      <td>-3.67688</td>
      <td>Private room</td>
      <td>60</td>
      <td>1</td>
      <td>80</td>
      <td>2019-05-14</td>
      <td>1.21</td>
      <td>2</td>
      <td>180</td>
      <td>4</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>21853</td>
      <td>Bright and airy room</td>
      <td>83531</td>
      <td>Abdel</td>
      <td>Latina</td>
      <td>Cármenes</td>
      <td>40.40381</td>
      <td>-3.74130</td>
      <td>Private room</td>
      <td>31</td>
      <td>4</td>
      <td>33</td>
      <td>2018-05-29</td>
      <td>0.39</td>
      <td>2</td>
      <td>364</td>
      <td>0</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>23001</td>
      <td>Apartmento Arganzuela- Madrid Rio</td>
      <td>82175</td>
      <td>Jesus</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.38840</td>
      <td>-3.69511</td>
      <td>Entire home/apt</td>
      <td>50</td>
      <td>15</td>
      <td>0</td>
      <td>None</td>
      <td>NaN</td>
      <td>5</td>
      <td>222</td>
      <td>0</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>24805</td>
      <td>Gran Via Studio Madrid</td>
      <td>346366726</td>
      <td>A</td>
      <td>Centro</td>
      <td>Universidad</td>
      <td>40.42183</td>
      <td>-3.70529</td>
      <td>Entire home/apt</td>
      <td>92</td>
      <td>5</td>
      <td>12</td>
      <td>2020-03-01</td>
      <td>0.51</td>
      <td>1</td>
      <td>115</td>
      <td>2</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>26825</td>
      <td>Single Room whith private Bathroom</td>
      <td>114340</td>
      <td>Agustina</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.38975</td>
      <td>-3.69018</td>
      <td>Private room</td>
      <td>26</td>
      <td>2</td>
      <td>149</td>
      <td>2018-05-15</td>
      <td>1.65</td>
      <td>1</td>
      <td>349</td>
      <td>0</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
listings.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 18909 entries, 0 to 18908
    Data columns (total 19 columns):
     #   Column                          Non-Null Count  Dtype  
    ---  ------                          --------------  -----  
     0   index                           18909 non-null  int64  
     1   id                              18909 non-null  int64  
     2   name                            18906 non-null  object 
     3   host_id                         18909 non-null  int64  
     4   host_name                       18883 non-null  object 
     5   neighbourhood_group             18909 non-null  object 
     6   neighbourhood                   18909 non-null  object 
     7   latitude                        18909 non-null  float64
     8   longitude                       18909 non-null  float64
     9   room_type                       18909 non-null  object 
     10  price                           18909 non-null  int64  
     11  minimum_nights                  18909 non-null  int64  
     12  number_of_reviews               18909 non-null  int64  
     13  last_review                     13877 non-null  object 
     14  reviews_per_month               13877 non-null  float64
     15  calculated_host_listings_count  18909 non-null  int64  
     16  availability_365                18909 non-null  int64  
     17  number_of_reviews_ltm           18909 non-null  int64  
     18  license                         2828 non-null   object 
    dtypes: float64(3), int64(9), object(7)
    memory usage: 2.7+ MB


#### Variables y tipos

Vamos a eliminar aquellas variables que no necesitaremos directamente para nuestros objetivos.


```python
a_eliminar = ['index',
              'host_name',
              'number_of_reviews',
              'last_review',
              'reviews_per_month',
              'number_of_reviews_ltm',
              'license'
             ]

listings.drop(columns = a_eliminar, inplace=True)

listings
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
      <th>neighbourhood_group</th>
      <th>neighbourhood</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>room_type</th>
      <th>price</th>
      <th>minimum_nights</th>
      <th>calculated_host_listings_count</th>
      <th>availability_365</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6369</td>
      <td>Rooftop terrace room ,  ensuite bathroom</td>
      <td>13660</td>
      <td>Chamartín</td>
      <td>Hispanoamérica</td>
      <td>40.457240</td>
      <td>-3.676880</td>
      <td>Private room</td>
      <td>60</td>
      <td>1</td>
      <td>2</td>
      <td>180</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21853</td>
      <td>Bright and airy room</td>
      <td>83531</td>
      <td>Latina</td>
      <td>Cármenes</td>
      <td>40.403810</td>
      <td>-3.741300</td>
      <td>Private room</td>
      <td>31</td>
      <td>4</td>
      <td>2</td>
      <td>364</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23001</td>
      <td>Apartmento Arganzuela- Madrid Rio</td>
      <td>82175</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.388400</td>
      <td>-3.695110</td>
      <td>Entire home/apt</td>
      <td>50</td>
      <td>15</td>
      <td>5</td>
      <td>222</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24805</td>
      <td>Gran Via Studio Madrid</td>
      <td>346366726</td>
      <td>Centro</td>
      <td>Universidad</td>
      <td>40.421830</td>
      <td>-3.705290</td>
      <td>Entire home/apt</td>
      <td>92</td>
      <td>5</td>
      <td>1</td>
      <td>115</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26825</td>
      <td>Single Room whith private Bathroom</td>
      <td>114340</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.389750</td>
      <td>-3.690180</td>
      <td>Private room</td>
      <td>26</td>
      <td>2</td>
      <td>1</td>
      <td>349</td>
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
    </tr>
    <tr>
      <th>18904</th>
      <td>52182264</td>
      <td>Enormous Private Room in 12-Bedroom Unit - los...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.424384</td>
      <td>-3.691216</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>87</td>
      <td>358</td>
    </tr>
    <tr>
      <th>18905</th>
      <td>52182273</td>
      <td>Stunning Private Room in 11-Bedroom Unit - los...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.424447</td>
      <td>-3.691309</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>87</td>
      <td>358</td>
    </tr>
    <tr>
      <th>18906</th>
      <td>52182303</td>
      <td>Classic Private Room in 7-Bedroom Unit - los 3...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.424989</td>
      <td>-3.691783</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>87</td>
      <td>358</td>
    </tr>
    <tr>
      <th>18907</th>
      <td>52182321</td>
      <td>Elegant Private Room in 12-Bedroom Unit - los ...</td>
      <td>378060726</td>
      <td>Salamanca</td>
      <td>Recoletos</td>
      <td>40.424352</td>
      <td>-3.690211</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>87</td>
      <td>358</td>
    </tr>
    <tr>
      <th>18908</th>
      <td>52182334</td>
      <td>Fashioned Private Room in 12-Bedroom Unit - lo...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.425670</td>
      <td>-3.691727</td>
      <td>Private room</td>
      <td>33</td>
      <td>1</td>
      <td>87</td>
      <td>358</td>
    </tr>
  </tbody>
</table>
<p>18909 rows × 12 columns</p>
</div>



Revisamos los tipos de variable


```python
listings.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 18909 entries, 0 to 18908
    Data columns (total 12 columns):
     #   Column                          Non-Null Count  Dtype  
    ---  ------                          --------------  -----  
     0   id                              18909 non-null  int64  
     1   name                            18906 non-null  object 
     2   host_id                         18909 non-null  int64  
     3   neighbourhood_group             18909 non-null  object 
     4   neighbourhood                   18909 non-null  object 
     5   latitude                        18909 non-null  float64
     6   longitude                       18909 non-null  float64
     7   room_type                       18909 non-null  object 
     8   price                           18909 non-null  int64  
     9   minimum_nights                  18909 non-null  int64  
     10  calculated_host_listings_count  18909 non-null  int64  
     11  availability_365                18909 non-null  int64  
    dtypes: float64(2), int64(6), object(4)
    memory usage: 1.7+ MB


Conclusión: pasar algunas objeto (neighbourhood_group, neighbourhood, room_type) a categóricas.


```python
for variable in ['neighbourhood_group','neighbourhood','room_type']:
    listings[variable] = listings[variable].astype('category')
```

Comprobamos


```python
listings.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 18909 entries, 0 to 18908
    Data columns (total 12 columns):
     #   Column                          Non-Null Count  Dtype   
    ---  ------                          --------------  -----   
     0   id                              18909 non-null  int64   
     1   name                            18906 non-null  object  
     2   host_id                         18909 non-null  int64   
     3   neighbourhood_group             18909 non-null  category
     4   neighbourhood                   18909 non-null  category
     5   latitude                        18909 non-null  float64 
     6   longitude                       18909 non-null  float64 
     7   room_type                       18909 non-null  category
     8   price                           18909 non-null  int64   
     9   minimum_nights                  18909 non-null  int64   
     10  calculated_host_listings_count  18909 non-null  int64   
     11  availability_365                18909 non-null  int64   
    dtypes: category(3), float64(2), int64(6), object(1)
    memory usage: 1.4+ MB


#### Análisis de nulos

Por la columna Non-null del info() vemos que solo name tiene 3 nulos.

Los revisamos pero vemos que no supone un problema, así que los dejamos.


```python
listings[listings.name.isna()]
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
      <th>neighbourhood_group</th>
      <th>neighbourhood</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>room_type</th>
      <th>price</th>
      <th>minimum_nights</th>
      <th>calculated_host_listings_count</th>
      <th>availability_365</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1538</th>
      <td>7164589</td>
      <td>None</td>
      <td>37525983</td>
      <td>Centro</td>
      <td>Palacio</td>
      <td>40.41458</td>
      <td>-3.71422</td>
      <td>Private room</td>
      <td>30</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2394</th>
      <td>11687495</td>
      <td>None</td>
      <td>48387429</td>
      <td>San Blas - Canillejas</td>
      <td>Simancas</td>
      <td>40.43765</td>
      <td>-3.62672</td>
      <td>Entire home/apt</td>
      <td>50</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2842</th>
      <td>13585476</td>
      <td>None</td>
      <td>20922102</td>
      <td>Centro</td>
      <td>Universidad</td>
      <td>40.42718</td>
      <td>-3.71144</td>
      <td>Entire home/apt</td>
      <td>65</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



#### Análisis de duplicados

Comprobamos si hay algún registro duplicado


```python
listings.duplicated().sum()
```




    0



#### Análisis de variables categóricas

Vamos a analizar los valores y las frecuencias de las variables categóricas


```python
listings.neighbourhood_group.value_counts()
```




    Centro                   8433
    Salamanca                1267
    Chamberí                 1148
    Arganzuela               1070
    Tetuán                    811
    Carabanchel               669
    Retiro                    656
    Ciudad Lineal             601
    Chamartín                 562
    Latina                    547
    Puente de Vallecas        542
    Moncloa - Aravaca         535
    San Blas - Canillejas     485
    Hortaleza                 374
    Fuencarral - El Pardo     294
    Usera                     275
    Villaverde                186
    Barajas                   147
    Moratalaz                 131
    Villa de Vallecas         105
    Vicálvaro                  71
    Name: neighbourhood_group, dtype: int64




```python
listings.neighbourhood.value_counts()
```




    Embajadores    2255
    Universidad    1772
    Palacio        1533
    Sol            1126
    Justicia        910
                   ... 
    El Plantío        5
    Valdemarín        4
    El Pardo          3
    Horcajo           2
    Atalaya           1
    Name: neighbourhood, Length: 128, dtype: int64




```python
listings.room_type.value_counts()
```




    Entire home/apt    11098
    Private room        7390
    Shared room          258
    Hotel room           163
    Name: room_type, dtype: int64



Vemos que hay hoteles. Nuestra empresa no se plantea comprar hoteles, así que tenemos que eliminar estos registros.


```python
listings = listings.loc[listings.room_type != 'Hotel room']
```


```python
listings.room_type.value_counts()
```




    Entire home/apt    11098
    Private room        7390
    Shared room          258
    Hotel room             0
    Name: room_type, dtype: int64



#### Análisis de variables numéricas

De las variables numéricas tiene sentido analizar desde price hasta availability_365, osea desde las posiciones de columnas de la 8 a la 11


```python
listings.iloc[:,8:12].describe().T
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
      <th>price</th>
      <td>18746.0</td>
      <td>129.271365</td>
      <td>432.384680</td>
      <td>8.0</td>
      <td>36.0</td>
      <td>64.0</td>
      <td>105.0</td>
      <td>9999.0</td>
    </tr>
    <tr>
      <th>minimum_nights</th>
      <td>18746.0</td>
      <td>7.295850</td>
      <td>35.430022</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>1125.0</td>
    </tr>
    <tr>
      <th>calculated_host_listings_count</th>
      <td>18746.0</td>
      <td>10.731676</td>
      <td>26.429455</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>6.0</td>
      <td>194.0</td>
    </tr>
    <tr>
      <th>availability_365</th>
      <td>18746.0</td>
      <td>153.761656</td>
      <td>140.363063</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>113.0</td>
      <td>310.0</td>
      <td>365.0</td>
    </tr>
  </tbody>
</table>
</div>



Conclusiones:

* En el precio hay que revisar mínimos y máximos
* En minimum_nights hay que revisar los máximos
* En calculated_host_listings_count hay que revisar los máximos

Revisamos mínimos y máximos en el precio


```python
listings.price.plot.kde()
```




    <AxesSubplot:ylabel='Density'>




    
![png](static/notebooks/airbnbds4/03_Creacion%20del%20datamart%20analitico_files/03_Creacion%20del%20datamart%20analitico_55_1.png)
    


Revisamos los máximos


```python
plt.figure(figsize=(16,8))
listings.price.loc[listings.price > 1000].value_counts().sort_index().plot.bar()
plt.xticks(size = 10);
```


    
![png](static/notebooks/airbnbds4/03_Creacion%20del%20datamart%20analitico_files/03_Creacion%20del%20datamart%20analitico_57_0.png)
    


Conclusión: 
    
* el valor 9999 normalmente suele ser una forma de imputar nulos, pero en este caso su frecuencia no está muy lejos de otros valores que pueden ser válidos, como el 8000, así que no lo vamos a tocar

Revisamos los valores cercanos a cero


```python
plt.figure(figsize=(16,8))
listings.price.loc[listings.price < 30].value_counts().sort_index().plot.bar()
plt.xticks(size = 10);
```


    
![png](static/notebooks/airbnbds4/03_Creacion%20del%20datamart%20analitico_files/03_Creacion%20del%20datamart%20analitico_60_0.png)
    


Conclusión: 
    
* Hay un pico en 20 euros, y parece que por debajo de esa cantidad sería difícil obtener rentabilidad, así que vamos a descartar los inmuebles que se alquilan por debajo de 20 euros


```python
listings = listings.loc[listings.price > 19]
listings
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
      <th>neighbourhood_group</th>
      <th>neighbourhood</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>room_type</th>
      <th>price</th>
      <th>minimum_nights</th>
      <th>calculated_host_listings_count</th>
      <th>availability_365</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6369</td>
      <td>Rooftop terrace room ,  ensuite bathroom</td>
      <td>13660</td>
      <td>Chamartín</td>
      <td>Hispanoamérica</td>
      <td>40.457240</td>
      <td>-3.676880</td>
      <td>Private room</td>
      <td>60</td>
      <td>1</td>
      <td>2</td>
      <td>180</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21853</td>
      <td>Bright and airy room</td>
      <td>83531</td>
      <td>Latina</td>
      <td>Cármenes</td>
      <td>40.403810</td>
      <td>-3.741300</td>
      <td>Private room</td>
      <td>31</td>
      <td>4</td>
      <td>2</td>
      <td>364</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23001</td>
      <td>Apartmento Arganzuela- Madrid Rio</td>
      <td>82175</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.388400</td>
      <td>-3.695110</td>
      <td>Entire home/apt</td>
      <td>50</td>
      <td>15</td>
      <td>5</td>
      <td>222</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24805</td>
      <td>Gran Via Studio Madrid</td>
      <td>346366726</td>
      <td>Centro</td>
      <td>Universidad</td>
      <td>40.421830</td>
      <td>-3.705290</td>
      <td>Entire home/apt</td>
      <td>92</td>
      <td>5</td>
      <td>1</td>
      <td>115</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26825</td>
      <td>Single Room whith private Bathroom</td>
      <td>114340</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.389750</td>
      <td>-3.690180</td>
      <td>Private room</td>
      <td>26</td>
      <td>2</td>
      <td>1</td>
      <td>349</td>
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
    </tr>
    <tr>
      <th>18904</th>
      <td>52182264</td>
      <td>Enormous Private Room in 12-Bedroom Unit - los...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.424384</td>
      <td>-3.691216</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>87</td>
      <td>358</td>
    </tr>
    <tr>
      <th>18905</th>
      <td>52182273</td>
      <td>Stunning Private Room in 11-Bedroom Unit - los...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.424447</td>
      <td>-3.691309</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>87</td>
      <td>358</td>
    </tr>
    <tr>
      <th>18906</th>
      <td>52182303</td>
      <td>Classic Private Room in 7-Bedroom Unit - los 3...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.424989</td>
      <td>-3.691783</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>87</td>
      <td>358</td>
    </tr>
    <tr>
      <th>18907</th>
      <td>52182321</td>
      <td>Elegant Private Room in 12-Bedroom Unit - los ...</td>
      <td>378060726</td>
      <td>Salamanca</td>
      <td>Recoletos</td>
      <td>40.424352</td>
      <td>-3.690211</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>87</td>
      <td>358</td>
    </tr>
    <tr>
      <th>18908</th>
      <td>52182334</td>
      <td>Fashioned Private Room in 12-Bedroom Unit - lo...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.425670</td>
      <td>-3.691727</td>
      <td>Private room</td>
      <td>33</td>
      <td>1</td>
      <td>87</td>
      <td>358</td>
    </tr>
  </tbody>
</table>
<p>17710 rows × 12 columns</p>
</div>



Para minimum_nights y alculated_host_listings_count habría que hacer un ejercicio similar.

No obstante no es algo que sea core en nuestro análisis y por tanto te lo dejo como deberes para que practiques.

### Tabla listings_det

#### Visión general


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
      <th>index</th>
      <th>id</th>
      <th>listing_url</th>
      <th>scrape_id</th>
      <th>last_scraped</th>
      <th>name</th>
      <th>description</th>
      <th>neighborhood_overview</th>
      <th>picture_url</th>
      <th>host_id</th>
      <th>...</th>
      <th>review_scores_communication</th>
      <th>review_scores_location</th>
      <th>review_scores_value</th>
      <th>license</th>
      <th>instant_bookable</th>
      <th>calculated_host_listings_count</th>
      <th>calculated_host_listings_count_entire_homes</th>
      <th>calculated_host_listings_count_private_rooms</th>
      <th>calculated_host_listings_count_shared_rooms</th>
      <th>reviews_per_month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>6369</td>
      <td>https://www.airbnb.com/rooms/6369</td>
      <td>20210910193531</td>
      <td>2021-09-11</td>
      <td>Rooftop terrace room ,  ensuite bathroom</td>
      <td>Excellent connection with the AIRPORT and EXHI...</td>
      <td>None</td>
      <td>https://a0.muscache.com/pictures/683224/4cc318...</td>
      <td>13660</td>
      <td>...</td>
      <td>4.89</td>
      <td>4.77</td>
      <td>4.85</td>
      <td>None</td>
      <td>f</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1.21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>21853</td>
      <td>https://www.airbnb.com/rooms/21853</td>
      <td>20210910193531</td>
      <td>2021-09-11</td>
      <td>Bright and airy room</td>
      <td>We have a quiet and sunny room with a good vie...</td>
      <td>We live in a leafy neighbourhood with plenty o...</td>
      <td>https://a0.muscache.com/pictures/68483181/87bc...</td>
      <td>83531</td>
      <td>...</td>
      <td>4.82</td>
      <td>4.21</td>
      <td>4.67</td>
      <td>None</td>
      <td>f</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0.39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>23001</td>
      <td>https://www.airbnb.com/rooms/23001</td>
      <td>20210910193531</td>
      <td>2021-09-11</td>
      <td>Apartmento Arganzuela- Madrid Rio</td>
      <td>Apartamento de tres dormitorios dobles, gran s...</td>
      <td>Barrio Arganzuela, junto a Madrid Rio, zonas c...</td>
      <td>https://a0.muscache.com/pictures/58e6a770-509c...</td>
      <td>82175</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>f</td>
      <td>5</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>24805</td>
      <td>https://www.airbnb.com/rooms/24805</td>
      <td>20210910193531</td>
      <td>2021-09-11</td>
      <td>Gran Via Studio Madrid</td>
      <td>Studio located 50 meters from Gran Via, next t...</td>
      <td>The area is next to the Gran Via, so people li...</td>
      <td>https://a0.muscache.com/pictures/miso/Hosting-...</td>
      <td>346366726</td>
      <td>...</td>
      <td>5.00</td>
      <td>5.00</td>
      <td>4.83</td>
      <td>None</td>
      <td>f</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>26825</td>
      <td>https://www.airbnb.com/rooms/26825</td>
      <td>20210910193531</td>
      <td>2021-09-11</td>
      <td>Single Room whith private Bathroom</td>
      <td>Nice and cozy roon for one person with a priva...</td>
      <td>Es un barrio muy tranquilo, en una zona de Mad...</td>
      <td>https://a0.muscache.com/pictures/149358/218d5b...</td>
      <td>114340</td>
      <td>...</td>
      <td>4.71</td>
      <td>4.70</td>
      <td>4.72</td>
      <td>None</td>
      <td>f</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1.65</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 75 columns</p>
</div>




```python
listings_det.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 18909 entries, 0 to 18908
    Data columns (total 75 columns):
     #   Column                                        Non-Null Count  Dtype  
    ---  ------                                        --------------  -----  
     0   index                                         18909 non-null  int64  
     1   id                                            18909 non-null  int64  
     2   listing_url                                   18909 non-null  object 
     3   scrape_id                                     18909 non-null  int64  
     4   last_scraped                                  18909 non-null  object 
     5   name                                          18906 non-null  object 
     6   description                                   17854 non-null  object 
     7   neighborhood_overview                         10997 non-null  object 
     8   picture_url                                   18908 non-null  object 
     9   host_id                                       18909 non-null  int64  
     10  host_url                                      18909 non-null  object 
     11  host_name                                     18883 non-null  object 
     12  host_since                                    18883 non-null  object 
     13  host_location                                 18841 non-null  object 
     14  host_about                                    9427 non-null   object 
     15  host_response_time                            11972 non-null  object 
     16  host_response_rate                            11972 non-null  object 
     17  host_acceptance_rate                          11531 non-null  object 
     18  host_is_superhost                             18883 non-null  object 
     19  host_thumbnail_url                            18883 non-null  object 
     20  host_picture_url                              18883 non-null  object 
     21  host_neighbourhood                            12034 non-null  object 
     22  host_listings_count                           18883 non-null  float64
     23  host_total_listings_count                     18883 non-null  float64
     24  host_verifications                            18909 non-null  object 
     25  host_has_profile_pic                          18883 non-null  object 
     26  host_identity_verified                        18883 non-null  object 
     27  neighbourhood                                 10997 non-null  object 
     28  neighbourhood_cleansed                        18909 non-null  object 
     29  neighbourhood_group_cleansed                  18909 non-null  object 
     30  latitude                                      18909 non-null  float64
     31  longitude                                     18909 non-null  float64
     32  property_type                                 18909 non-null  object 
     33  room_type                                     18909 non-null  object 
     34  accommodates                                  18909 non-null  int64  
     35  bathrooms                                     0 non-null      float64
     36  bathrooms_text                                18884 non-null  object 
     37  bedrooms                                      17475 non-null  float64
     38  beds                                          18568 non-null  float64
     39  amenities                                     18909 non-null  object 
     40  price                                         18909 non-null  object 
     41  minimum_nights                                18909 non-null  int64  
     42  maximum_nights                                18909 non-null  int64  
     43  minimum_minimum_nights                        18908 non-null  float64
     44  maximum_minimum_nights                        18908 non-null  float64
     45  minimum_maximum_nights                        18908 non-null  float64
     46  maximum_maximum_nights                        18908 non-null  float64
     47  minimum_nights_avg_ntm                        18908 non-null  float64
     48  maximum_nights_avg_ntm                        18908 non-null  float64
     49  calendar_updated                              0 non-null      float64
     50  has_availability                              18909 non-null  object 
     51  availability_30                               18909 non-null  int64  
     52  availability_60                               18909 non-null  int64  
     53  availability_90                               18909 non-null  int64  
     54  availability_365                              18909 non-null  int64  
     55  calendar_last_scraped                         18909 non-null  object 
     56  number_of_reviews                             18909 non-null  int64  
     57  number_of_reviews_ltm                         18909 non-null  int64  
     58  number_of_reviews_l30d                        18909 non-null  int64  
     59  first_review                                  13877 non-null  object 
     60  last_review                                   13877 non-null  object 
     61  review_scores_rating                          13877 non-null  float64
     62  review_scores_accuracy                        13638 non-null  float64
     63  review_scores_cleanliness                     13640 non-null  float64
     64  review_scores_checkin                         13640 non-null  float64
     65  review_scores_communication                   13640 non-null  float64
     66  review_scores_location                        13637 non-null  float64
     67  review_scores_value                           13636 non-null  float64
     68  license                                       2828 non-null   object 
     69  instant_bookable                              18909 non-null  object 
     70  calculated_host_listings_count                18909 non-null  int64  
     71  calculated_host_listings_count_entire_homes   18909 non-null  int64  
     72  calculated_host_listings_count_private_rooms  18909 non-null  int64  
     73  calculated_host_listings_count_shared_rooms   18909 non-null  int64  
     74  reviews_per_month                             13877 non-null  float64
    dtypes: float64(22), int64(18), object(35)
    memory usage: 10.8+ MB


#### Variables y tipos

Vamos a seleccionar solo aquellas variables que nos aporten información relevante para nuestros objetivos.


```python
a_incluir = ['id',
              'description',
              'host_is_superhost',
              'accommodates',
              'bathrooms',
              'bedrooms',
              'beds',
              'number_of_reviews',
              'review_scores_rating',
              'review_scores_communication',
              'review_scores_location'
             ]

listings_det = listings_det.loc[:,a_incluir]

listings_det
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
      <th>description</th>
      <th>host_is_superhost</th>
      <th>accommodates</th>
      <th>bathrooms</th>
      <th>bedrooms</th>
      <th>beds</th>
      <th>number_of_reviews</th>
      <th>review_scores_rating</th>
      <th>review_scores_communication</th>
      <th>review_scores_location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6369</td>
      <td>Excellent connection with the AIRPORT and EXHI...</td>
      <td>t</td>
      <td>2</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>80</td>
      <td>4.87</td>
      <td>4.89</td>
      <td>4.77</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21853</td>
      <td>We have a quiet and sunny room with a good vie...</td>
      <td>f</td>
      <td>1</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>33</td>
      <td>4.58</td>
      <td>4.82</td>
      <td>4.21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23001</td>
      <td>Apartamento de tres dormitorios dobles, gran s...</td>
      <td>f</td>
      <td>6</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24805</td>
      <td>Studio located 50 meters from Gran Via, next t...</td>
      <td>f</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>12</td>
      <td>4.92</td>
      <td>5.00</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26825</td>
      <td>Nice and cozy roon for one person with a priva...</td>
      <td>f</td>
      <td>1</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>149</td>
      <td>4.68</td>
      <td>4.71</td>
      <td>4.70</td>
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
      <th>18904</th>
      <td>52182264</td>
      <td>ROOM - 8 sqm. • 1st Floor &lt;br /&gt; &lt;br /&gt;cozy ro...</td>
      <td>f</td>
      <td>1</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18905</th>
      <td>52182273</td>
      <td>ROOM - 10 sqm. • 4th Floor &lt;br /&gt; &lt;br /&gt;cozy r...</td>
      <td>f</td>
      <td>1</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18906</th>
      <td>52182303</td>
      <td>ROOM &lt;br /&gt; &lt;br /&gt;cozy room in madrid centro i...</td>
      <td>f</td>
      <td>1</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18907</th>
      <td>52182321</td>
      <td>ROOM -9 sqm. • 1st Floor &lt;br /&gt; &lt;br /&gt;cozy roo...</td>
      <td>f</td>
      <td>1</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18908</th>
      <td>52182334</td>
      <td>ROOM - 10 sqm. • 1st Floor &lt;br /&gt; &lt;br /&gt;cozy r...</td>
      <td>f</td>
      <td>1</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>18909 rows × 11 columns</p>
</div>



Analizamos los tipos


```python
listings_det.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 18909 entries, 0 to 18908
    Data columns (total 11 columns):
     #   Column                       Non-Null Count  Dtype  
    ---  ------                       --------------  -----  
     0   id                           18909 non-null  int64  
     1   description                  17854 non-null  object 
     2   host_is_superhost            18883 non-null  object 
     3   accommodates                 18909 non-null  int64  
     4   bathrooms                    0 non-null      float64
     5   bedrooms                     17475 non-null  float64
     6   beds                         18568 non-null  float64
     7   number_of_reviews            18909 non-null  int64  
     8   review_scores_rating         13877 non-null  float64
     9   review_scores_communication  13640 non-null  float64
     10  review_scores_location       13637 non-null  float64
    dtypes: float64(6), int64(3), object(2)
    memory usage: 1.6+ MB


Conclusión: pasar host_is_superhost a categórica.


```python
listings_det['host_is_superhost'] = listings_det['host_is_superhost'].astype('category')
    
listings_det.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 18909 entries, 0 to 18908
    Data columns (total 11 columns):
     #   Column                       Non-Null Count  Dtype   
    ---  ------                       --------------  -----   
     0   id                           18909 non-null  int64   
     1   description                  17854 non-null  object  
     2   host_is_superhost            18883 non-null  category
     3   accommodates                 18909 non-null  int64   
     4   bathrooms                    0 non-null      float64 
     5   bedrooms                     17475 non-null  float64 
     6   beds                         18568 non-null  float64 
     7   number_of_reviews            18909 non-null  int64   
     8   review_scores_rating         13877 non-null  float64 
     9   review_scores_communication  13640 non-null  float64 
     10  review_scores_location       13637 non-null  float64 
    dtypes: category(1), float64(6), int64(3), object(1)
    memory usage: 1.5+ MB


#### Análisis de nulos


```python
listings_det.isna().sum()
```




    id                                 0
    description                     1055
    host_is_superhost                 26
    accommodates                       0
    bathrooms                      18909
    bedrooms                        1434
    beds                             341
    number_of_reviews                  0
    review_scores_rating            5032
    review_scores_communication     5269
    review_scores_location          5272
    dtype: int64



Conclusiones:

* bathrooms está totalmente a nulos, por tanto la eliminamos
* description no pasa nada porque tenga nulos, así que la dejamos
* host_is_superhost tiene muy pocos nulos y no es una variables super relevante, así que la dejamos
* beds: podemos intentar imputarla a partir de accomodates
* bedrooms sí es una variable importante para nosotros, podemos intentar imputar los nulos a través de proxies como accomodates o beds

Vamos a ver si podemos hacer una imputación de beds a partir del número de personas que se pueden acomodar.


```python
pd.crosstab(listings_det.beds, listings_det.accommodates)
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
      <th>accommodates</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
      <th>16</th>
    </tr>
    <tr>
      <th>beds</th>
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
      <th>0.0</th>
      <td>222</td>
      <td>259</td>
      <td>41</td>
      <td>68</td>
      <td>15</td>
      <td>12</td>
      <td>5</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1.0</th>
      <td>2765</td>
      <td>4911</td>
      <td>399</td>
      <td>639</td>
      <td>14</td>
      <td>9</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2.0</th>
      <td>120</td>
      <td>1110</td>
      <td>1016</td>
      <td>2277</td>
      <td>125</td>
      <td>148</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3.0</th>
      <td>18</td>
      <td>75</td>
      <td>231</td>
      <td>925</td>
      <td>395</td>
      <td>582</td>
      <td>18</td>
      <td>26</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4.0</th>
      <td>20</td>
      <td>28</td>
      <td>32</td>
      <td>216</td>
      <td>214</td>
      <td>498</td>
      <td>73</td>
      <td>92</td>
      <td>3</td>
      <td>9</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5.0</th>
      <td>2</td>
      <td>5</td>
      <td>6</td>
      <td>20</td>
      <td>42</td>
      <td>178</td>
      <td>75</td>
      <td>94</td>
      <td>9</td>
      <td>30</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6.0</th>
      <td>14</td>
      <td>9</td>
      <td>2</td>
      <td>5</td>
      <td>7</td>
      <td>62</td>
      <td>21</td>
      <td>61</td>
      <td>9</td>
      <td>18</td>
      <td>4</td>
      <td>8</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7.0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>6</td>
      <td>10</td>
      <td>19</td>
      <td>8</td>
      <td>17</td>
      <td>2</td>
      <td>6</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8.0</th>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>21</td>
      <td>3</td>
      <td>18</td>
      <td>2</td>
      <td>9</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2</td>
      <td>8</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10.0</th>
      <td>10</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>4</td>
      <td>9</td>
    </tr>
    <tr>
      <th>11.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>12.0</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>13.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>14.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>15.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>16.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>17.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>18.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>23.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>24.0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



Parece que sí podríamos hacer una asignación mas o menos directa. Leyendo la matriz en vertical vemos que:

* una o dos personas se suelen corresponder con una cama
* tres o cuatro personas se suelen corresponder con dos camas
* cinco o seis personas se suelen corresponder con tres camas
* a más de 6 personas le vamos a poner cuatro camas

Repasamos el número de nulos y la frecuencia de cada valor


```python
listings_det['beds'].value_counts(dropna = False)
```




    1.0     8751
    2.0     4805
    3.0     2272
    4.0     1186
    0.0      628
    5.0      466
    NaN      341
    6.0      222
    7.0       78
    8.0       68
    10.0      39
    9.0       20
    14.0       6
    11.0       6
    12.0       5
    16.0       5
    13.0       4
    18.0       2
    17.0       2
    24.0       1
    15.0       1
    23.0       1
    Name: beds, dtype: int64



Creamos una función para imputar los nulos de beds en base a accommodates


```python
def imputar_nulos(registro):
    #Lista de condiciones
    condiciones = [(registro.accommodates <= 2),
               (registro.accommodates > 2) & (registro.accommodates <= 4),
               (registro.accommodates > 4) & (registro.accommodates <= 6),
               (registro.accommodates > 6)]

    #Lista de resultados
    resultados = [1,2,3,4]
    
    #Salida
    return(np.select(condiciones,resultados, default = -999))

#Imputación
listings_det.loc[listings_det.beds.isna(),'beds'] = listings_det.loc[listings_det.beds.isna()].apply(imputar_nulos, axis = 1).astype('float64')

```

Comprobamos


```python
listings_det.beds.value_counts(dropna = False)
```




    1.0     9061
    2.0     4828
    3.0     2276
    4.0     1190
    0.0      628
    5.0      466
    6.0      222
    7.0       78
    8.0       68
    10.0      39
    9.0       20
    14.0       6
    11.0       6
    12.0       5
    16.0       5
    13.0       4
    18.0       2
    17.0       2
    24.0       1
    15.0       1
    23.0       1
    Name: beds, dtype: int64



Ahora vamos a ver si podemos hacer una imputación de bedrooms.

Empezamos por cruzar el número de habitaciones con el número de personas que se pueden acomodar.


```python
pd.crosstab(listings_det.bedrooms, listings_det.accommodates)
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
      <th>accommodates</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
      <th>16</th>
    </tr>
    <tr>
      <th>bedrooms</th>
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
      <th>1.0</th>
      <td>3009</td>
      <td>5569</td>
      <td>1141</td>
      <td>2265</td>
      <td>111</td>
      <td>81</td>
      <td>4</td>
      <td>14</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2.0</th>
      <td>74</td>
      <td>173</td>
      <td>348</td>
      <td>1560</td>
      <td>444</td>
      <td>852</td>
      <td>51</td>
      <td>48</td>
      <td>4</td>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3.0</th>
      <td>21</td>
      <td>22</td>
      <td>45</td>
      <td>104</td>
      <td>220</td>
      <td>509</td>
      <td>106</td>
      <td>158</td>
      <td>7</td>
      <td>20</td>
      <td>4</td>
      <td>13</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4.0</th>
      <td>16</td>
      <td>21</td>
      <td>1</td>
      <td>12</td>
      <td>18</td>
      <td>38</td>
      <td>34</td>
      <td>96</td>
      <td>10</td>
      <td>39</td>
      <td>2</td>
      <td>15</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5.0</th>
      <td>9</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
      <td>6</td>
      <td>9</td>
      <td>34</td>
      <td>3</td>
      <td>8</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>12</td>
    </tr>
    <tr>
      <th>6.0</th>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7.0</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <th>8.0</th>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>9.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>10.0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>14.0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>18.0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



No parece muy fiable.

Vamos a contrastarlo con el número de camas.


```python
pd.crosstab(listings_det.bedrooms, listings_det.beds, dropna=False)
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
      <th>beds</th>
      <th>0.0</th>
      <th>1.0</th>
      <th>2.0</th>
      <th>3.0</th>
      <th>4.0</th>
      <th>5.0</th>
      <th>6.0</th>
      <th>7.0</th>
      <th>8.0</th>
      <th>9.0</th>
      <th>...</th>
      <th>11.0</th>
      <th>12.0</th>
      <th>13.0</th>
      <th>14.0</th>
      <th>15.0</th>
      <th>16.0</th>
      <th>17.0</th>
      <th>18.0</th>
      <th>23.0</th>
      <th>24.0</th>
    </tr>
    <tr>
      <th>bedrooms</th>
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
      <th>1.0</th>
      <td>451</td>
      <td>8038</td>
      <td>3039</td>
      <td>459</td>
      <td>139</td>
      <td>15</td>
      <td>36</td>
      <td>1</td>
      <td>13</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2.0</th>
      <td>65</td>
      <td>108</td>
      <td>1372</td>
      <td>1329</td>
      <td>532</td>
      <td>110</td>
      <td>33</td>
      <td>7</td>
      <td>5</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3.0</th>
      <td>7</td>
      <td>28</td>
      <td>22</td>
      <td>414</td>
      <td>393</td>
      <td>242</td>
      <td>80</td>
      <td>25</td>
      <td>11</td>
      <td>7</td>
      <td>...</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4.0</th>
      <td>6</td>
      <td>23</td>
      <td>3</td>
      <td>7</td>
      <td>95</td>
      <td>63</td>
      <td>56</td>
      <td>27</td>
      <td>19</td>
      <td>6</td>
      <td>...</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5.0</th>
      <td>1</td>
      <td>14</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>26</td>
      <td>10</td>
      <td>16</td>
      <td>17</td>
      <td>2</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6.0</th>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7.0</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8.0</th>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14.0</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15.0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18.0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>13 rows × 21 columns</p>
</div>



Aquí sí podríamos hacer una asignación más directa. Leyendo la matriz en vertical vemos que:

* cero, una o dos camas se suele corresponder con una habitación
* tres o cuatro camas se suele corresponder con dos habitaciones
* cinco o seis camas se suele corresponder con tres habitaciones
* a más camas le vamos a poner cuatro habitaciones

Vamos a modificar la función que habíamos creado para imputar los nulos de bedrooms a partir de beds.

Primero hacemos el conteo de bedrooms


```python
listings_det.bedrooms.value_counts(dropna = False)
```




    1.0     12212
    2.0      3562
    NaN      1434
    3.0      1233
    4.0       311
    5.0       105
    6.0        24
    7.0        11
    8.0         7
    9.0         3
    10.0        3
    14.0        2
    15.0        1
    18.0        1
    Name: bedrooms, dtype: int64



Ejecutamos la función actualizada


```python
def imputar_nulos(registro):
    #Lista de condiciones
    condiciones = [(registro.beds <= 2),
               (registro.beds > 2) & (registro.beds <= 4),
               (registro.beds > 4) & (registro.beds <= 6),
               (registro.beds > 6)]

    #Lista de resultados
    resultados = [1,2,3,4]
    
    #Salida
    return(np.select(condiciones,resultados, default = -999))

#Imputación
listings_det.loc[listings_det.bedrooms.isna(),'bedrooms'] = listings_det.loc[listings_det.bedrooms.isna()].apply(imputar_nulos, axis = 1).astype('float64')
```

Comprobamos


```python
listings_det.bedrooms.value_counts(dropna = False)
```




    1.0     13540
    2.0      3657
    3.0      1244
    4.0       311
    5.0       105
    6.0        24
    7.0        11
    8.0         7
    9.0         3
    10.0        3
    14.0        2
    15.0        1
    18.0        1
    Name: bedrooms, dtype: int64



Por último vamos a eliminar bathrooms


```python
listings_det.drop(columns = 'bathrooms', inplace = True)
listings_det
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
      <th>description</th>
      <th>host_is_superhost</th>
      <th>accommodates</th>
      <th>bedrooms</th>
      <th>beds</th>
      <th>number_of_reviews</th>
      <th>review_scores_rating</th>
      <th>review_scores_communication</th>
      <th>review_scores_location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6369</td>
      <td>Excellent connection with the AIRPORT and EXHI...</td>
      <td>t</td>
      <td>2</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>80</td>
      <td>4.87</td>
      <td>4.89</td>
      <td>4.77</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21853</td>
      <td>We have a quiet and sunny room with a good vie...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>33</td>
      <td>4.58</td>
      <td>4.82</td>
      <td>4.21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23001</td>
      <td>Apartamento de tres dormitorios dobles, gran s...</td>
      <td>f</td>
      <td>6</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24805</td>
      <td>Studio located 50 meters from Gran Via, next t...</td>
      <td>f</td>
      <td>3</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>12</td>
      <td>4.92</td>
      <td>5.00</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26825</td>
      <td>Nice and cozy roon for one person with a priva...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>149</td>
      <td>4.68</td>
      <td>4.71</td>
      <td>4.70</td>
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
      <th>18904</th>
      <td>52182264</td>
      <td>ROOM - 8 sqm. • 1st Floor &lt;br /&gt; &lt;br /&gt;cozy ro...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18905</th>
      <td>52182273</td>
      <td>ROOM - 10 sqm. • 4th Floor &lt;br /&gt; &lt;br /&gt;cozy r...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18906</th>
      <td>52182303</td>
      <td>ROOM &lt;br /&gt; &lt;br /&gt;cozy room in madrid centro i...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18907</th>
      <td>52182321</td>
      <td>ROOM -9 sqm. • 1st Floor &lt;br /&gt; &lt;br /&gt;cozy roo...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18908</th>
      <td>52182334</td>
      <td>ROOM - 10 sqm. • 1st Floor &lt;br /&gt; &lt;br /&gt;cozy r...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>18909 rows × 10 columns</p>
</div>



#### Análisis de duplicados

Comprobamos si hay algún registro duplicado


```python
listings_det.duplicated().sum()
```




    0




```python
listings_det.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 18909 entries, 0 to 18908
    Data columns (total 10 columns):
     #   Column                       Non-Null Count  Dtype   
    ---  ------                       --------------  -----   
     0   id                           18909 non-null  int64   
     1   description                  17854 non-null  object  
     2   host_is_superhost            18883 non-null  category
     3   accommodates                 18909 non-null  int64   
     4   bedrooms                     18909 non-null  float64 
     5   beds                         18909 non-null  float64 
     6   number_of_reviews            18909 non-null  int64   
     7   review_scores_rating         13877 non-null  float64 
     8   review_scores_communication  13640 non-null  float64 
     9   review_scores_location       13637 non-null  float64 
    dtypes: category(1), float64(5), int64(3), object(1)
    memory usage: 1.3+ MB


#### Análisis de variables categóricas

Vamos a analizar los valores y las frecuencias de las variables categóricas


```python
listings_det.host_is_superhost.value_counts()
```




    f    15423
    t     3460
    Name: host_is_superhost, dtype: int64



#### Análisis de variables numéricas


```python
listings_det.describe(include = 'number').T
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
      <th>id</th>
      <td>18909.0</td>
      <td>3.055841e+07</td>
      <td>1.448889e+07</td>
      <td>6369.0</td>
      <td>19305558.00</td>
      <td>33537761.00</td>
      <td>42555334.00</td>
      <td>52182334.0</td>
    </tr>
    <tr>
      <th>accommodates</th>
      <td>18909.0</td>
      <td>3.094928e+00</td>
      <td>1.963715e+00</td>
      <td>0.0</td>
      <td>2.00</td>
      <td>2.00</td>
      <td>4.00</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>bedrooms</th>
      <td>18909.0</td>
      <td>1.414670e+00</td>
      <td>8.116969e-01</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>2.00</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>beds</th>
      <td>18909.0</td>
      <td>1.909197e+00</td>
      <td>1.444317e+00</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>2.00</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>number_of_reviews</th>
      <td>18909.0</td>
      <td>3.270612e+01</td>
      <td>6.524996e+01</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>5.00</td>
      <td>32.00</td>
      <td>744.0</td>
    </tr>
    <tr>
      <th>review_scores_rating</th>
      <td>13877.0</td>
      <td>4.549404e+00</td>
      <td>7.834379e-01</td>
      <td>0.0</td>
      <td>4.50</td>
      <td>4.75</td>
      <td>4.94</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>review_scores_communication</th>
      <td>13640.0</td>
      <td>4.776612e+00</td>
      <td>4.632929e-01</td>
      <td>1.0</td>
      <td>4.75</td>
      <td>4.92</td>
      <td>5.00</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>review_scores_location</th>
      <td>13637.0</td>
      <td>4.788151e+00</td>
      <td>3.774844e-01</td>
      <td>1.0</td>
      <td>4.73</td>
      <td>4.92</td>
      <td>5.00</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



No vemos nada extraño.

En este punto ya hemos detectado y corregido los principales problemas de calidad de datos así que pasamos a crear el datamart analítico integrando nuestras tablas.

## DATAMART ANALITICO

Tenemos 2 tablas principales:

* listings
* listings_det

Y sabemos que ambas comparten el campo id, por tanto podemos cruzarlas por él.

La tabla principal es listings, ya que la de detalle lo que hace es darnos datos adicionales.

Por tanto la tabla que ha de mandar en la integración es listings.

Además tambien tenemos la tabla del precio, que en este caso cruza conceptualmente con listings a través del distrito (neighbourhood_group).

Aunque no hemos comprobado todavía que los literales sean iguales, por tanto quizá será necesario hacer alguna corrección manual.

Vamos a empezar por las 2 principales.

Dado que va a mandar la tabla listings el resultado final tendrá que tener tantas filas como listings y tantas columnas como las de ambas tablas (menos 1 por el id que se quedará como una única variable)


```python
listings.shape
```




    (17710, 12)




```python
listings_det.shape
```




    (18909, 10)



Es decir, si sale bien la tabla final tendrá 17710 filas y 21 columnas.


```python
df = pd.merge(left = listings, right = listings_det, how = 'left', on = 'id')
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
      <th>...</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6369</td>
      <td>Rooftop terrace room ,  ensuite bathroom</td>
      <td>13660</td>
      <td>Chamartín</td>
      <td>Hispanoamérica</td>
      <td>40.457240</td>
      <td>-3.676880</td>
      <td>Private room</td>
      <td>60</td>
      <td>1</td>
      <td>...</td>
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
    </tr>
    <tr>
      <th>1</th>
      <td>21853</td>
      <td>Bright and airy room</td>
      <td>83531</td>
      <td>Latina</td>
      <td>Cármenes</td>
      <td>40.403810</td>
      <td>-3.741300</td>
      <td>Private room</td>
      <td>31</td>
      <td>4</td>
      <td>...</td>
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
    </tr>
    <tr>
      <th>2</th>
      <td>23001</td>
      <td>Apartmento Arganzuela- Madrid Rio</td>
      <td>82175</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.388400</td>
      <td>-3.695110</td>
      <td>Entire home/apt</td>
      <td>50</td>
      <td>15</td>
      <td>...</td>
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
    </tr>
    <tr>
      <th>3</th>
      <td>24805</td>
      <td>Gran Via Studio Madrid</td>
      <td>346366726</td>
      <td>Centro</td>
      <td>Universidad</td>
      <td>40.421830</td>
      <td>-3.705290</td>
      <td>Entire home/apt</td>
      <td>92</td>
      <td>5</td>
      <td>...</td>
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
    </tr>
    <tr>
      <th>4</th>
      <td>26825</td>
      <td>Single Room whith private Bathroom</td>
      <td>114340</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.389750</td>
      <td>-3.690180</td>
      <td>Private room</td>
      <td>26</td>
      <td>2</td>
      <td>...</td>
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
    </tr>
    <tr>
      <th>17705</th>
      <td>52182264</td>
      <td>Enormous Private Room in 12-Bedroom Unit - los...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.424384</td>
      <td>-3.691216</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>...</td>
      <td>358</td>
      <td>ROOM - 8 sqm. • 1st Floor &lt;br /&gt; &lt;br /&gt;cozy ro...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17706</th>
      <td>52182273</td>
      <td>Stunning Private Room in 11-Bedroom Unit - los...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.424447</td>
      <td>-3.691309</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>...</td>
      <td>358</td>
      <td>ROOM - 10 sqm. • 4th Floor &lt;br /&gt; &lt;br /&gt;cozy r...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17707</th>
      <td>52182303</td>
      <td>Classic Private Room in 7-Bedroom Unit - los 3...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.424989</td>
      <td>-3.691783</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>...</td>
      <td>358</td>
      <td>ROOM &lt;br /&gt; &lt;br /&gt;cozy room in madrid centro i...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17708</th>
      <td>52182321</td>
      <td>Elegant Private Room in 12-Bedroom Unit - los ...</td>
      <td>378060726</td>
      <td>Salamanca</td>
      <td>Recoletos</td>
      <td>40.424352</td>
      <td>-3.690211</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>...</td>
      <td>358</td>
      <td>ROOM -9 sqm. • 1st Floor &lt;br /&gt; &lt;br /&gt;cozy roo...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17709</th>
      <td>52182334</td>
      <td>Fashioned Private Room in 12-Bedroom Unit - lo...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.425670</td>
      <td>-3.691727</td>
      <td>Private room</td>
      <td>33</td>
      <td>1</td>
      <td>...</td>
      <td>358</td>
      <td>ROOM - 10 sqm. • 1st Floor &lt;br /&gt; &lt;br /&gt;cozy r...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>17710 rows × 21 columns</p>
</div>



Ahora vamos a ver cómo podemos incorporar la información externa del precio por metro cuadrado.

Para ello lo primero es analizar los valores de la variable distrito en ambas tablas, ya que necesitan coincidir para que podamos cruzarlos.

En df la variable es categórica, así que para sacar los niveles tenemos que usar .categories


```python
distritos1 = pd.Series(df.neighbourhood_group.unique().categories).sort_values()
distritos1
```




    2                Arganzuela
    16                  Barajas
    10              Carabanchel
    3                    Centro
    0                 Chamartín
    7                  Chamberí
    14            Ciudad Lineal
    6     Fuencarral - El Pardo
    9                 Hortaleza
    1                    Latina
    18        Moncloa - Aravaca
    19                Moratalaz
    5        Puente de Vallecas
    11                   Retiro
    4                 Salamanca
    13    San Blas - Canillejas
    12                   Tetuán
    17                    Usera
    20                Vicálvaro
    15        Villa de Vallecas
    8                Villaverde
    dtype: object




```python
distritos2 = precio_m2.distrito
distritos2
```




    1             Arganzuela
    2                Barajas
    3            Carabanchel
    4                 Centro
    5              Chamartín
    6               Chamberí
    7          Ciudad Lineal
    8             Fuencarral
    9              Hortaleza
    10                Latina
    11               Moncloa
    12             Moratalaz
    13    Puente de Vallecas
    14                Retiro
    15             Salamanca
    16              San Blas
    17                Tetuán
    18                 Usera
    19             Vicálvaro
    20     Villa de Vallecas
    21            Villaverde
    Name: distrito, dtype: object



Comparando parece todo igual excepto:

* Fuencarral - El Pardo
* Moncloa - Aravaca
* San Blas - Canillejas

Por tanto vamos a reemplazar estos valores en precio_m2 para que sean iguales a los de df y podamos cruzarlos


```python
precio_m2.distrito = precio_m2.distrito.map({'Fuencarral':'Fuencarral - El Pardo',
                        'Moncloa':'Moncloa - Aravaca',
                        'San Blas':'San Blas - Canillejas'}) \
                    .fillna(precio_m2.distrito)

precio_m2
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
      <th>precio_m2</th>
      <th>distrito</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>4085</td>
      <td>Arganzuela</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3409</td>
      <td>Barajas</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2123</td>
      <td>Carabanchel</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4827</td>
      <td>Centro</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5098</td>
      <td>Chamartín</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5381</td>
      <td>Chamberí</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2940</td>
      <td>Ciudad Lineal</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3568</td>
      <td>Fuencarral - El Pardo</td>
    </tr>
    <tr>
      <th>9</th>
      <td>3871</td>
      <td>Hortaleza</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2267</td>
      <td>Latina</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4033</td>
      <td>Moncloa - Aravaca</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2500</td>
      <td>Moratalaz</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1918</td>
      <td>Puente de Vallecas</td>
    </tr>
    <tr>
      <th>14</th>
      <td>4788</td>
      <td>Retiro</td>
    </tr>
    <tr>
      <th>15</th>
      <td>6114</td>
      <td>Salamanca</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2591</td>
      <td>San Blas - Canillejas</td>
    </tr>
    <tr>
      <th>17</th>
      <td>3678</td>
      <td>Tetuán</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1995</td>
      <td>Usera</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2403</td>
      <td>Vicálvaro</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2354</td>
      <td>Villa de Vallecas</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1693</td>
      <td>Villaverde</td>
    </tr>
  </tbody>
</table>
</div>



Ahora sí que ya podemos cruzarlos.

Manda df.


```python
df = pd.merge(left = df, right = precio_m2, how = 'left', left_on='neighbourhood_group', right_on='distrito')
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
      <th>...</th>
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
      <td>6369</td>
      <td>Rooftop terrace room ,  ensuite bathroom</td>
      <td>13660</td>
      <td>Chamartín</td>
      <td>Hispanoamérica</td>
      <td>40.457240</td>
      <td>-3.676880</td>
      <td>Private room</td>
      <td>60</td>
      <td>1</td>
      <td>...</td>
      <td>t</td>
      <td>2</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>80</td>
      <td>4.87</td>
      <td>4.89</td>
      <td>4.77</td>
      <td>5098</td>
      <td>Chamartín</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21853</td>
      <td>Bright and airy room</td>
      <td>83531</td>
      <td>Latina</td>
      <td>Cármenes</td>
      <td>40.403810</td>
      <td>-3.741300</td>
      <td>Private room</td>
      <td>31</td>
      <td>4</td>
      <td>...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>33</td>
      <td>4.58</td>
      <td>4.82</td>
      <td>4.21</td>
      <td>2267</td>
      <td>Latina</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23001</td>
      <td>Apartmento Arganzuela- Madrid Rio</td>
      <td>82175</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.388400</td>
      <td>-3.695110</td>
      <td>Entire home/apt</td>
      <td>50</td>
      <td>15</td>
      <td>...</td>
      <td>f</td>
      <td>6</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4085</td>
      <td>Arganzuela</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24805</td>
      <td>Gran Via Studio Madrid</td>
      <td>346366726</td>
      <td>Centro</td>
      <td>Universidad</td>
      <td>40.421830</td>
      <td>-3.705290</td>
      <td>Entire home/apt</td>
      <td>92</td>
      <td>5</td>
      <td>...</td>
      <td>f</td>
      <td>3</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>12</td>
      <td>4.92</td>
      <td>5.00</td>
      <td>5.00</td>
      <td>4827</td>
      <td>Centro</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26825</td>
      <td>Single Room whith private Bathroom</td>
      <td>114340</td>
      <td>Arganzuela</td>
      <td>Legazpi</td>
      <td>40.389750</td>
      <td>-3.690180</td>
      <td>Private room</td>
      <td>26</td>
      <td>2</td>
      <td>...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>149</td>
      <td>4.68</td>
      <td>4.71</td>
      <td>4.70</td>
      <td>4085</td>
      <td>Arganzuela</td>
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
    </tr>
    <tr>
      <th>17705</th>
      <td>52182264</td>
      <td>Enormous Private Room in 12-Bedroom Unit - los...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.424384</td>
      <td>-3.691216</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4827</td>
      <td>Centro</td>
    </tr>
    <tr>
      <th>17706</th>
      <td>52182273</td>
      <td>Stunning Private Room in 11-Bedroom Unit - los...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.424447</td>
      <td>-3.691309</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4827</td>
      <td>Centro</td>
    </tr>
    <tr>
      <th>17707</th>
      <td>52182303</td>
      <td>Classic Private Room in 7-Bedroom Unit - los 3...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.424989</td>
      <td>-3.691783</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4827</td>
      <td>Centro</td>
    </tr>
    <tr>
      <th>17708</th>
      <td>52182321</td>
      <td>Elegant Private Room in 12-Bedroom Unit - los ...</td>
      <td>378060726</td>
      <td>Salamanca</td>
      <td>Recoletos</td>
      <td>40.424352</td>
      <td>-3.690211</td>
      <td>Private room</td>
      <td>29</td>
      <td>1</td>
      <td>...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6114</td>
      <td>Salamanca</td>
    </tr>
    <tr>
      <th>17709</th>
      <td>52182334</td>
      <td>Fashioned Private Room in 12-Bedroom Unit - lo...</td>
      <td>378060726</td>
      <td>Centro</td>
      <td>Justicia</td>
      <td>40.425670</td>
      <td>-3.691727</td>
      <td>Private room</td>
      <td>33</td>
      <td>1</td>
      <td>...</td>
      <td>f</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4827</td>
      <td>Centro</td>
    </tr>
  </tbody>
</table>
<p>17710 rows × 23 columns</p>
</div>



Comprobamos que no se hayan generado nulos en la unión.


```python
df.precio_m2.isna().sum()
```




    0



## GUARDAR EN LA BASE DE DATOS

Ahora que ya tenemos el tablón de análisis vamos a guardarlo en la base de datos para que cada vez que queramos hacer análisis no tengamos que repetir todo el procesamiento de este notebook


```python
df.to_sql('df', con = con, if_exists = 'replace')
```
