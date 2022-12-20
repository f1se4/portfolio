# CREACION DEL DATAMART ANALITICO

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
pd.options.display.max_columns = 8
```

## CARGA DE DATOS 


```python
import sqlalchemy as sa
con = sa.create_engine('sqlite:///ecommerce.db')
```


```python
from sqlalchemy import inspect
insp = inspect(con)
tablas = insp.get_table_names()
tablas
```




    ['2019-Dec', '2019-Nov', '2019-Oct', '2020-Feb', '2020-Jan']




```python
oct = pd.read_sql('2019-Oct', con)
nov = pd.read_sql('2019-Nov', con)
dic = pd.read_sql('2019-Dec', con)
ene = pd.read_sql('2020-Jan', con)
feb = pd.read_sql('2020-Feb', con)
```

## INTEGRACION DE DATOS 


```python
df = pd.concat([oct,nov,dic,ene,feb], axis = 0)
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
      <th>index</th>
      <th>event_time</th>
      <th>event_type</th>
      <th>product_id</th>
      <th>...</th>
      <th>brand</th>
      <th>price</th>
      <th>user_id</th>
      <th>user_session</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>68</td>
      <td>2019-10-01 00:01:46 UTC</td>
      <td>view</td>
      <td>5843665</td>
      <td>...</td>
      <td>f.o.x</td>
      <td>9.44</td>
      <td>462033176</td>
      <td>a18e0999-61a1-4218-8f8f-61ec1d375361</td>
    </tr>
    <tr>
      <th>1</th>
      <td>72</td>
      <td>2019-10-01 00:01:55 UTC</td>
      <td>cart</td>
      <td>5868461</td>
      <td>...</td>
      <td>italwax</td>
      <td>3.57</td>
      <td>514753614</td>
      <td>e2fecb2d-22d0-df2c-c661-15da44b3ccf1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>95</td>
      <td>2019-10-01 00:02:50 UTC</td>
      <td>view</td>
      <td>5877456</td>
      <td>...</td>
      <td>jessnail</td>
      <td>122.22</td>
      <td>527418424</td>
      <td>86e77869-afbc-4dff-9aa2-6b7dd8c90770</td>
    </tr>
    <tr>
      <th>3</th>
      <td>122</td>
      <td>2019-10-01 00:03:41 UTC</td>
      <td>view</td>
      <td>5649270</td>
      <td>...</td>
      <td>concept</td>
      <td>6.19</td>
      <td>555448072</td>
      <td>b5f72ceb-0730-44de-a932-d16db62390df</td>
    </tr>
    <tr>
      <th>4</th>
      <td>124</td>
      <td>2019-10-01 00:03:44 UTC</td>
      <td>view</td>
      <td>18082</td>
      <td>...</td>
      <td>cnd</td>
      <td>16.03</td>
      <td>552006247</td>
      <td>2d8f304b-de45-4e59-8f40-50c603843fe5</td>
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
      <th>429785</th>
      <td>4156660</td>
      <td>2020-02-29 23:58:49 UTC</td>
      <td>cart</td>
      <td>5815662</td>
      <td>...</td>
      <td>None</td>
      <td>0.92</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>429786</th>
      <td>4156663</td>
      <td>2020-02-29 23:58:57 UTC</td>
      <td>view</td>
      <td>5815665</td>
      <td>...</td>
      <td>None</td>
      <td>0.59</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>429787</th>
      <td>4156668</td>
      <td>2020-02-29 23:59:05 UTC</td>
      <td>cart</td>
      <td>5815665</td>
      <td>...</td>
      <td>None</td>
      <td>0.59</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>429788</th>
      <td>4156675</td>
      <td>2020-02-29 23:59:28 UTC</td>
      <td>view</td>
      <td>5817692</td>
      <td>...</td>
      <td>None</td>
      <td>0.79</td>
      <td>619841242</td>
      <td>18af673b-7fb9-4202-a66d-5c855bc0fd2d</td>
    </tr>
    <tr>
      <th>429789</th>
      <td>4156680</td>
      <td>2020-02-29 23:59:54 UTC</td>
      <td>view</td>
      <td>5716351</td>
      <td>...</td>
      <td>irisk</td>
      <td>0.79</td>
      <td>619841242</td>
      <td>18af673b-7fb9-4202-a66d-5c855bc0fd2d</td>
    </tr>
  </tbody>
</table>
<p>2095076 rows × 10 columns</p>
</div>



## CALIDAD DE DATOS 

### Tipos de variables


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 2095076 entries, 0 to 429789
    Data columns (total 10 columns):
     #   Column         Dtype  
    ---  ------         -----  
     0   index          int64  
     1   event_time     object 
     2   event_type     object 
     3   product_id     int64  
     4   category_id    int64  
     5   category_code  object 
     6   brand          object 
     7   price          float64
     8   user_id        int64  
     9   user_session   object 
    dtypes: float64(1), int64(4), object(5)
    memory usage: 175.8+ MB
    

Eliminamos la columna index.


```python
df.drop(columns = 'index', inplace = True)
```

Análisis y corrección de tipos.

* pasar event_time a datetime

Pasamos event_time a datetime.

TRUCO PRO: pd.to_datetime() puede tardar mucho en ejecutarse en datasets grandes.

Pero por algún motivo si dividimos la cadena de la fecha en sus partes y la volvemos a juntar y después transformamos a datetime especificándole el formato exacto funciona MUCHO más rápido.

Te voy a enseñar las dos formas:

* la fácil y tradicional con pd.to_datetime: puedes usar esta si no quieres complicarte con la función
* la avanzada creando una función para hacer lo que he comentado

Te recuerdo el link para los códigos de los formatos: 

https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

En mi equipo con 32GB de RAM la forma tradicional tardó más de 5 minutos, mientras que la avanzanda menos de 10 segundos.


```python
#forma tradicional, la dejo comentada porque voy a utilizar la otra
#df.event_time = pd.to_datetime(df.event_time)
```


```python
#forma avanzada crando una función
#a esta función hay que pasarle la variable fecha y el formato en el que está

def datetime_rapido(dt,formato):

    def divide_fecha(fecha):
        division = fecha.split()
        date = division[0]
        time = division[1]
        cadena = date + ' ' + time
        return cadena

    resultado = pd.to_datetime(dt.apply(lambda x: divide_fecha(x)), format = formato)

    return resultado
```

Ejecutamos la función.


```python
formato = '%Y-%m-%d %H:%M:%S'

df.event_time = datetime_rapido(df.event_time,formato)
```


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 2095076 entries, 0 to 429789
    Data columns (total 9 columns):
     #   Column         Dtype         
    ---  ------         -----         
     0   event_time     datetime64[ns]
     1   event_type     object        
     2   product_id     int64         
     3   category_id    int64         
     4   category_code  object        
     5   brand          object        
     6   price          float64       
     7   user_id        int64         
     8   user_session   object        
    dtypes: datetime64[ns](1), float64(1), int64(3), object(4)
    memory usage: 159.8+ MB
    

### Nombres de variables

Renombramos las variables a español.


```python
df.columns = ['fecha',
              'evento',
              'producto',
              'categoria',
              'categoria_cod',
              'marca',
              'precio',
              'usuario',
              'sesion']
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
      <th>evento</th>
      <th>producto</th>
      <th>categoria</th>
      <th>...</th>
      <th>marca</th>
      <th>precio</th>
      <th>usuario</th>
      <th>sesion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2019-10-01 00:01:46</td>
      <td>view</td>
      <td>5843665</td>
      <td>1487580005092295511</td>
      <td>...</td>
      <td>f.o.x</td>
      <td>9.44</td>
      <td>462033176</td>
      <td>a18e0999-61a1-4218-8f8f-61ec1d375361</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019-10-01 00:01:55</td>
      <td>cart</td>
      <td>5868461</td>
      <td>1487580013069861041</td>
      <td>...</td>
      <td>italwax</td>
      <td>3.57</td>
      <td>514753614</td>
      <td>e2fecb2d-22d0-df2c-c661-15da44b3ccf1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2019-10-01 00:02:50</td>
      <td>view</td>
      <td>5877456</td>
      <td>1487580006300255120</td>
      <td>...</td>
      <td>jessnail</td>
      <td>122.22</td>
      <td>527418424</td>
      <td>86e77869-afbc-4dff-9aa2-6b7dd8c90770</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019-10-01 00:03:41</td>
      <td>view</td>
      <td>5649270</td>
      <td>1487580013749338323</td>
      <td>...</td>
      <td>concept</td>
      <td>6.19</td>
      <td>555448072</td>
      <td>b5f72ceb-0730-44de-a932-d16db62390df</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2019-10-01 00:03:44</td>
      <td>view</td>
      <td>18082</td>
      <td>1487580005411062629</td>
      <td>...</td>
      <td>cnd</td>
      <td>16.03</td>
      <td>552006247</td>
      <td>2d8f304b-de45-4e59-8f40-50c603843fe5</td>
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
      <th>429785</th>
      <td>2020-02-29 23:58:49</td>
      <td>cart</td>
      <td>5815662</td>
      <td>1487580006317032337</td>
      <td>...</td>
      <td>None</td>
      <td>0.92</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>429786</th>
      <td>2020-02-29 23:58:57</td>
      <td>view</td>
      <td>5815665</td>
      <td>1487580006317032337</td>
      <td>...</td>
      <td>None</td>
      <td>0.59</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>429787</th>
      <td>2020-02-29 23:59:05</td>
      <td>cart</td>
      <td>5815665</td>
      <td>1487580006317032337</td>
      <td>...</td>
      <td>None</td>
      <td>0.59</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>429788</th>
      <td>2020-02-29 23:59:28</td>
      <td>view</td>
      <td>5817692</td>
      <td>1487580010872045658</td>
      <td>...</td>
      <td>None</td>
      <td>0.79</td>
      <td>619841242</td>
      <td>18af673b-7fb9-4202-a66d-5c855bc0fd2d</td>
    </tr>
    <tr>
      <th>429789</th>
      <td>2020-02-29 23:59:54</td>
      <td>view</td>
      <td>5716351</td>
      <td>1487580010872045658</td>
      <td>...</td>
      <td>irisk</td>
      <td>0.79</td>
      <td>619841242</td>
      <td>18af673b-7fb9-4202-a66d-5c855bc0fd2d</td>
    </tr>
  </tbody>
</table>
<p>2095076 rows × 9 columns</p>
</div>



### Análisis de nulos


```python
df.isna().sum().sort_values(ascending = False)
```




    categoria_cod    2060411
    marca             891646
    sesion               506
    fecha                  0
    evento                 0
    producto               0
    categoria              0
    precio                 0
    usuario                0
    dtype: int64



Conclusiones:

* categoria_cod tiene casi todos los registros a nulo
* marca tiene casi la mitad de los registros a nulo
* hay 500 nulos en sesión

Acciones:

* eliminar las variables categoria_cod y marca
* eliminar los nulos de sesión ya que es una variable relevante


```python
df = df.drop(columns = ['categoria_cod','marca']).dropna()
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
      <th>evento</th>
      <th>producto</th>
      <th>categoria</th>
      <th>precio</th>
      <th>usuario</th>
      <th>sesion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2019-10-01 00:01:46</td>
      <td>view</td>
      <td>5843665</td>
      <td>1487580005092295511</td>
      <td>9.44</td>
      <td>462033176</td>
      <td>a18e0999-61a1-4218-8f8f-61ec1d375361</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019-10-01 00:01:55</td>
      <td>cart</td>
      <td>5868461</td>
      <td>1487580013069861041</td>
      <td>3.57</td>
      <td>514753614</td>
      <td>e2fecb2d-22d0-df2c-c661-15da44b3ccf1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2019-10-01 00:02:50</td>
      <td>view</td>
      <td>5877456</td>
      <td>1487580006300255120</td>
      <td>122.22</td>
      <td>527418424</td>
      <td>86e77869-afbc-4dff-9aa2-6b7dd8c90770</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019-10-01 00:03:41</td>
      <td>view</td>
      <td>5649270</td>
      <td>1487580013749338323</td>
      <td>6.19</td>
      <td>555448072</td>
      <td>b5f72ceb-0730-44de-a932-d16db62390df</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2019-10-01 00:03:44</td>
      <td>view</td>
      <td>18082</td>
      <td>1487580005411062629</td>
      <td>16.03</td>
      <td>552006247</td>
      <td>2d8f304b-de45-4e59-8f40-50c603843fe5</td>
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
      <th>429785</th>
      <td>2020-02-29 23:58:49</td>
      <td>cart</td>
      <td>5815662</td>
      <td>1487580006317032337</td>
      <td>0.92</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>429786</th>
      <td>2020-02-29 23:58:57</td>
      <td>view</td>
      <td>5815665</td>
      <td>1487580006317032337</td>
      <td>0.59</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>429787</th>
      <td>2020-02-29 23:59:05</td>
      <td>cart</td>
      <td>5815665</td>
      <td>1487580006317032337</td>
      <td>0.59</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>429788</th>
      <td>2020-02-29 23:59:28</td>
      <td>view</td>
      <td>5817692</td>
      <td>1487580010872045658</td>
      <td>0.79</td>
      <td>619841242</td>
      <td>18af673b-7fb9-4202-a66d-5c855bc0fd2d</td>
    </tr>
    <tr>
      <th>429789</th>
      <td>2020-02-29 23:59:54</td>
      <td>view</td>
      <td>5716351</td>
      <td>1487580010872045658</td>
      <td>0.79</td>
      <td>619841242</td>
      <td>18af673b-7fb9-4202-a66d-5c855bc0fd2d</td>
    </tr>
  </tbody>
</table>
<p>2094570 rows × 7 columns</p>
</div>



### Análisis de las variables numéricas


```python
df.describe()
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
      <th>usuario</th>
      <th>categoria</th>
      <th>producto</th>
      <th>precio</th>
      <th>...</th>
      <th>segundo</th>
      <th>festivo</th>
      <th>black_friday</th>
      <th>san_valentin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2074026.00</td>
      <td>2074026.00</td>
      <td>2074026.00</td>
      <td>2074026.00</td>
      <td>...</td>
      <td>2074026.00</td>
      <td>2074026.00</td>
      <td>2074026.00</td>
      <td>2074026.00</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>521758909.23</td>
      <td>1553192964541272064.00</td>
      <td>5485203.09</td>
      <td>8.50</td>
      <td>...</td>
      <td>29.50</td>
      <td>0.06</td>
      <td>0.01</td>
      <td>0.01</td>
    </tr>
    <tr>
      <th>std</th>
      <td>87354480.68</td>
      <td>168128659843838048.00</td>
      <td>1304219.20</td>
      <td>19.21</td>
      <td>...</td>
      <td>17.29</td>
      <td>0.24</td>
      <td>0.10</td>
      <td>0.08</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4661182.00</td>
      <td>1487580004807082752.00</td>
      <td>3752.00</td>
      <td>0.05</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>482863572.00</td>
      <td>1487580005754995456.00</td>
      <td>5724633.00</td>
      <td>2.06</td>
      <td>...</td>
      <td>15.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>553690395.00</td>
      <td>1487580008246412288.00</td>
      <td>5811652.00</td>
      <td>4.06</td>
      <td>...</td>
      <td>29.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>578763499.00</td>
      <td>1487580013489291520.00</td>
      <td>5858221.00</td>
      <td>6.98</td>
      <td>...</td>
      <td>44.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>max</th>
      <td>622087993.00</td>
      <td>2242903426784559104.00</td>
      <td>5932585.00</td>
      <td>327.78</td>
      <td>...</td>
      <td>59.00</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
<p>8 rows × 13 columns</p>
</div>



Vemos negativos en el precio. Vamos a profundizar.


```python
df[df.precio <= 0]
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
      <th>evento</th>
      <th>producto</th>
      <th>categoria</th>
      <th>precio</th>
      <th>usuario</th>
      <th>sesion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>343</th>
      <td>2019-10-01 02:15:41</td>
      <td>view</td>
      <td>5892052</td>
      <td>1487580010377117763</td>
      <td>0.00</td>
      <td>555455025</td>
      <td>320f6021-30ac-4a58-ae17-bac1cc32aac3</td>
    </tr>
    <tr>
      <th>924</th>
      <td>2019-10-01 05:16:30</td>
      <td>view</td>
      <td>5889621</td>
      <td>1487580010561667147</td>
      <td>0.00</td>
      <td>523988665</td>
      <td>00849bd2-fcd2-4cb4-af31-4e264f151848</td>
    </tr>
    <tr>
      <th>933</th>
      <td>2019-10-01 05:18:03</td>
      <td>view</td>
      <td>5889622</td>
      <td>1487580010561667147</td>
      <td>0.00</td>
      <td>523988665</td>
      <td>80cfe614-f0a5-4101-a2b6-a21227590470</td>
    </tr>
    <tr>
      <th>937</th>
      <td>2019-10-01 05:18:46</td>
      <td>view</td>
      <td>5889623</td>
      <td>1487580010561667147</td>
      <td>0.00</td>
      <td>523988665</td>
      <td>c2cd0464-3d2b-48e2-9667-bac248fe297a</td>
    </tr>
    <tr>
      <th>1077</th>
      <td>2019-10-01 05:38:01</td>
      <td>view</td>
      <td>5889627</td>
      <td>1487580010561667147</td>
      <td>0.00</td>
      <td>523988665</td>
      <td>8b2bf9d8-43f0-43b2-bed3-13b2c956cada</td>
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
      <th>428011</th>
      <td>2020-02-29 20:04:49</td>
      <td>cart</td>
      <td>5824841</td>
      <td>1897124478404526487</td>
      <td>0.00</td>
      <td>469761446</td>
      <td>8bf369b4-92c0-4fb8-88a5-8a2dd0947e46</td>
    </tr>
    <tr>
      <th>428012</th>
      <td>2020-02-29 20:04:49</td>
      <td>cart</td>
      <td>5826413</td>
      <td>1487580005511725929</td>
      <td>0.00</td>
      <td>469761446</td>
      <td>8bf369b4-92c0-4fb8-88a5-8a2dd0947e46</td>
    </tr>
    <tr>
      <th>428013</th>
      <td>2020-02-29 20:04:49</td>
      <td>cart</td>
      <td>5832437</td>
      <td>1487580007675986893</td>
      <td>0.00</td>
      <td>469761446</td>
      <td>8bf369b4-92c0-4fb8-88a5-8a2dd0947e46</td>
    </tr>
    <tr>
      <th>428014</th>
      <td>2020-02-29 20:04:49</td>
      <td>cart</td>
      <td>5851606</td>
      <td>2055161088059638328</td>
      <td>0.00</td>
      <td>469761446</td>
      <td>8bf369b4-92c0-4fb8-88a5-8a2dd0947e46</td>
    </tr>
    <tr>
      <th>428370</th>
      <td>2020-02-29 20:26:16</td>
      <td>view</td>
      <td>5923106</td>
      <td>1487580008246412266</td>
      <td>0.00</td>
      <td>622047714</td>
      <td>74f04dc6-2b3c-4565-beda-f575d73ed81c</td>
    </tr>
  </tbody>
</table>
<p>20544 rows × 7 columns</p>
</div>



Son unos 20000 registros, podríamos eliminarlos.

Pero antes ¿se concentran quizá en algún producto determinado?


```python
df[df.precio <= 0].producto.value_counts().head(10)
```




    5896186    79
    5903915    50
    5873428    37
    5851294    29
    5851304    29
    5837624    28
    5712583    27
    5851272    27
    5907812    26
    5899512    26
    Name: producto, dtype: int64



No parece que sea problema de un producto concreto, así que vamos a eliminar todos los registros.


```python
df = df[df.precio > 0]
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
      <th>evento</th>
      <th>producto</th>
      <th>categoria</th>
      <th>precio</th>
      <th>usuario</th>
      <th>sesion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2019-10-01 00:01:46</td>
      <td>view</td>
      <td>5843665</td>
      <td>1487580005092295511</td>
      <td>9.44</td>
      <td>462033176</td>
      <td>a18e0999-61a1-4218-8f8f-61ec1d375361</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019-10-01 00:01:55</td>
      <td>cart</td>
      <td>5868461</td>
      <td>1487580013069861041</td>
      <td>3.57</td>
      <td>514753614</td>
      <td>e2fecb2d-22d0-df2c-c661-15da44b3ccf1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2019-10-01 00:02:50</td>
      <td>view</td>
      <td>5877456</td>
      <td>1487580006300255120</td>
      <td>122.22</td>
      <td>527418424</td>
      <td>86e77869-afbc-4dff-9aa2-6b7dd8c90770</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019-10-01 00:03:41</td>
      <td>view</td>
      <td>5649270</td>
      <td>1487580013749338323</td>
      <td>6.19</td>
      <td>555448072</td>
      <td>b5f72ceb-0730-44de-a932-d16db62390df</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2019-10-01 00:03:44</td>
      <td>view</td>
      <td>18082</td>
      <td>1487580005411062629</td>
      <td>16.03</td>
      <td>552006247</td>
      <td>2d8f304b-de45-4e59-8f40-50c603843fe5</td>
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
      <th>429785</th>
      <td>2020-02-29 23:58:49</td>
      <td>cart</td>
      <td>5815662</td>
      <td>1487580006317032337</td>
      <td>0.92</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>429786</th>
      <td>2020-02-29 23:58:57</td>
      <td>view</td>
      <td>5815665</td>
      <td>1487580006317032337</td>
      <td>0.59</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>429787</th>
      <td>2020-02-29 23:59:05</td>
      <td>cart</td>
      <td>5815665</td>
      <td>1487580006317032337</td>
      <td>0.59</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>429788</th>
      <td>2020-02-29 23:59:28</td>
      <td>view</td>
      <td>5817692</td>
      <td>1487580010872045658</td>
      <td>0.79</td>
      <td>619841242</td>
      <td>18af673b-7fb9-4202-a66d-5c855bc0fd2d</td>
    </tr>
    <tr>
      <th>429789</th>
      <td>2020-02-29 23:59:54</td>
      <td>view</td>
      <td>5716351</td>
      <td>1487580010872045658</td>
      <td>0.79</td>
      <td>619841242</td>
      <td>18af673b-7fb9-4202-a66d-5c855bc0fd2d</td>
    </tr>
  </tbody>
</table>
<p>2074026 rows × 7 columns</p>
</div>



### Análisis de las variables categóricas


```python
df.evento.nunique()
```




    4




```python
df.evento.value_counts()
```




    view                961558
    cart                574547
    remove_from_cart    410357
    purchase            127564
    Name: evento, dtype: int64




```python
df.producto.nunique()
```




    45327




```python
df.categoria.nunique()
```




    508



### Índice

Vamos a poner la fecha como el index.


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
      <th>evento</th>
      <th>producto</th>
      <th>categoria</th>
      <th>precio</th>
      <th>usuario</th>
      <th>sesion</th>
    </tr>
    <tr>
      <th>fecha</th>
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
      <th>2019-10-01 00:01:46</th>
      <td>view</td>
      <td>5843665</td>
      <td>1487580005092295511</td>
      <td>9.44</td>
      <td>462033176</td>
      <td>a18e0999-61a1-4218-8f8f-61ec1d375361</td>
    </tr>
    <tr>
      <th>2019-10-01 00:01:55</th>
      <td>cart</td>
      <td>5868461</td>
      <td>1487580013069861041</td>
      <td>3.57</td>
      <td>514753614</td>
      <td>e2fecb2d-22d0-df2c-c661-15da44b3ccf1</td>
    </tr>
    <tr>
      <th>2019-10-01 00:02:50</th>
      <td>view</td>
      <td>5877456</td>
      <td>1487580006300255120</td>
      <td>122.22</td>
      <td>527418424</td>
      <td>86e77869-afbc-4dff-9aa2-6b7dd8c90770</td>
    </tr>
    <tr>
      <th>2019-10-01 00:03:41</th>
      <td>view</td>
      <td>5649270</td>
      <td>1487580013749338323</td>
      <td>6.19</td>
      <td>555448072</td>
      <td>b5f72ceb-0730-44de-a932-d16db62390df</td>
    </tr>
    <tr>
      <th>2019-10-01 00:03:44</th>
      <td>view</td>
      <td>18082</td>
      <td>1487580005411062629</td>
      <td>16.03</td>
      <td>552006247</td>
      <td>2d8f304b-de45-4e59-8f40-50c603843fe5</td>
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
      <th>2020-02-29 23:58:49</th>
      <td>cart</td>
      <td>5815662</td>
      <td>1487580006317032337</td>
      <td>0.92</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>2020-02-29 23:58:57</th>
      <td>view</td>
      <td>5815665</td>
      <td>1487580006317032337</td>
      <td>0.59</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>2020-02-29 23:59:05</th>
      <td>cart</td>
      <td>5815665</td>
      <td>1487580006317032337</td>
      <td>0.59</td>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
    </tr>
    <tr>
      <th>2020-02-29 23:59:28</th>
      <td>view</td>
      <td>5817692</td>
      <td>1487580010872045658</td>
      <td>0.79</td>
      <td>619841242</td>
      <td>18af673b-7fb9-4202-a66d-5c855bc0fd2d</td>
    </tr>
    <tr>
      <th>2020-02-29 23:59:54</th>
      <td>view</td>
      <td>5716351</td>
      <td>1487580010872045658</td>
      <td>0.79</td>
      <td>619841242</td>
      <td>18af673b-7fb9-4202-a66d-5c855bc0fd2d</td>
    </tr>
  </tbody>
</table>
<p>2074026 rows × 6 columns</p>
</div>



## TRANSFORMACION DE DATOS

Vamos a crear 3 tipos de nuevas variables

* Extraer componentes
* Variables de calendario: Festivos locales (Rusia)
* Indicadores exógenos: Días no necesariamente festivos pero con interés comercial: Black Friday, Cyber Monday, Reyes, San Valentin

### Componentes de la fecha


```python
def componentes_fecha(dataframe):
    date = dataframe.index.date
    año = dataframe.index.year
    mes = dataframe.index.month
    dia = dataframe.index.day
    hora = dataframe.index.hour
    minuto = dataframe.index.minute
    segundo = dataframe.index.second
    
    
    return(pd.DataFrame({'date':date, 'año':año,'mes':mes, 'dia':dia, 'hora':hora, 'minuto':minuto, 'segundo':segundo}))
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
      <th>evento</th>
      <th>producto</th>
      <th>categoria</th>
      <th>precio</th>
      <th>...</th>
      <th>dia</th>
      <th>hora</th>
      <th>minuto</th>
      <th>segundo</th>
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
      <th>2019-10-01 00:01:46</th>
      <td>view</td>
      <td>5843665</td>
      <td>1487580005092295511</td>
      <td>9.44</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>46</td>
    </tr>
    <tr>
      <th>2019-10-01 00:01:55</th>
      <td>cart</td>
      <td>5868461</td>
      <td>1487580013069861041</td>
      <td>3.57</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>55</td>
    </tr>
    <tr>
      <th>2019-10-01 00:02:50</th>
      <td>view</td>
      <td>5877456</td>
      <td>1487580006300255120</td>
      <td>122.22</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2019-10-01 00:03:41</th>
      <td>view</td>
      <td>5649270</td>
      <td>1487580013749338323</td>
      <td>6.19</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>41</td>
    </tr>
    <tr>
      <th>2019-10-01 00:03:44</th>
      <td>view</td>
      <td>18082</td>
      <td>1487580005411062629</td>
      <td>16.03</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>44</td>
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
      <th>2020-02-29 23:58:49</th>
      <td>cart</td>
      <td>5815662</td>
      <td>1487580006317032337</td>
      <td>0.92</td>
      <td>...</td>
      <td>29</td>
      <td>23</td>
      <td>58</td>
      <td>49</td>
    </tr>
    <tr>
      <th>2020-02-29 23:58:57</th>
      <td>view</td>
      <td>5815665</td>
      <td>1487580006317032337</td>
      <td>0.59</td>
      <td>...</td>
      <td>29</td>
      <td>23</td>
      <td>58</td>
      <td>57</td>
    </tr>
    <tr>
      <th>2020-02-29 23:59:05</th>
      <td>cart</td>
      <td>5815665</td>
      <td>1487580006317032337</td>
      <td>0.59</td>
      <td>...</td>
      <td>29</td>
      <td>23</td>
      <td>59</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2020-02-29 23:59:28</th>
      <td>view</td>
      <td>5817692</td>
      <td>1487580010872045658</td>
      <td>0.79</td>
      <td>...</td>
      <td>29</td>
      <td>23</td>
      <td>59</td>
      <td>28</td>
    </tr>
    <tr>
      <th>2020-02-29 23:59:54</th>
      <td>view</td>
      <td>5716351</td>
      <td>1487580010872045658</td>
      <td>0.79</td>
      <td>...</td>
      <td>29</td>
      <td>23</td>
      <td>59</td>
      <td>54</td>
    </tr>
  </tbody>
</table>
<p>2074026 rows × 13 columns</p>
</div>



### Variables de calendario: festivos

Para incorporar festivos podemos usar el paquete holidays.

No es perfecto, pero nos da mucha flexibilidad porque tiene fiestas de varios países e incluso a nivel comunidades.

Lo instalamos con: conda install -c conda-forge holidays

Lo importamos con: import holidays

Y podemos ver el listado de países y el uso básico en:

https://github.com/dr-prodigy/python-holidays

Por ejemplo vamos a hacer la prueba con España.


```python
import holidays

festivo_es = holidays.ES(years=2021)

for fecha, fiesta in festivo_es.items():
    print(fecha,fiesta)
```

    2021-01-01 Año nuevo
    2021-01-06 Epifanía del Señor
    2021-04-01 Jueves Santo
    2021-04-02 Viernes Santo
    2021-05-01 Día del Trabajador
    2021-08-16 Asunción de la Virgen (Trasladado)
    2021-10-12 Día de la Hispanidad
    2021-11-01 Todos los Santos
    2021-12-06 Día de la Constitución Española
    2021-12-08 La Inmaculada Concepción
    2021-12-25 Navidad
    

Definimos el objeto festivo_ru ya que este ecommerce es Ruso.


```python
festivo_ru = holidays.RU(years=2020)
festivo_ru
```




    {datetime.date(2020, 1, 1): 'Новый год', datetime.date(2020, 1, 2): 'Новый год', datetime.date(2020, 1, 3): 'Новый год', datetime.date(2020, 1, 4): 'Новый год', datetime.date(2020, 1, 5): 'Новый год', datetime.date(2020, 1, 6): 'Новый год', datetime.date(2020, 1, 7): 'Православное Рождество', datetime.date(2020, 1, 8): 'Новый год', datetime.date(2020, 2, 23): 'День защитника отечества', datetime.date(2020, 3, 8): 'День женщин', datetime.date(2020, 5, 1): 'Праздник Весны и Труда', datetime.date(2020, 5, 9): 'День Победы', datetime.date(2020, 6, 12): 'День России', datetime.date(2020, 11, 4): 'День народного единства', datetime.date(2020, 12, 31): 'Новый год'}



Vamos a incorporar una variable que diga en cada registro si era un día festivo o no.


```python
df['festivo'] = df.date.apply(lambda x: 1 if (x in festivo_ru) else 0)
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
      <th>evento</th>
      <th>producto</th>
      <th>categoria</th>
      <th>precio</th>
      <th>...</th>
      <th>hora</th>
      <th>minuto</th>
      <th>segundo</th>
      <th>festivo</th>
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
      <th>2019-10-01 00:01:46</th>
      <td>view</td>
      <td>5843665</td>
      <td>1487580005092295511</td>
      <td>9.44</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>46</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:01:55</th>
      <td>cart</td>
      <td>5868461</td>
      <td>1487580013069861041</td>
      <td>3.57</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>55</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:02:50</th>
      <td>view</td>
      <td>5877456</td>
      <td>1487580006300255120</td>
      <td>122.22</td>
      <td>...</td>
      <td>0</td>
      <td>2</td>
      <td>50</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:03:41</th>
      <td>view</td>
      <td>5649270</td>
      <td>1487580013749338323</td>
      <td>6.19</td>
      <td>...</td>
      <td>0</td>
      <td>3</td>
      <td>41</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:03:44</th>
      <td>view</td>
      <td>18082</td>
      <td>1487580005411062629</td>
      <td>16.03</td>
      <td>...</td>
      <td>0</td>
      <td>3</td>
      <td>44</td>
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
    </tr>
    <tr>
      <th>2020-02-29 23:58:49</th>
      <td>cart</td>
      <td>5815662</td>
      <td>1487580006317032337</td>
      <td>0.92</td>
      <td>...</td>
      <td>23</td>
      <td>58</td>
      <td>49</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-02-29 23:58:57</th>
      <td>view</td>
      <td>5815665</td>
      <td>1487580006317032337</td>
      <td>0.59</td>
      <td>...</td>
      <td>23</td>
      <td>58</td>
      <td>57</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-02-29 23:59:05</th>
      <td>cart</td>
      <td>5815665</td>
      <td>1487580006317032337</td>
      <td>0.59</td>
      <td>...</td>
      <td>23</td>
      <td>59</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-02-29 23:59:28</th>
      <td>view</td>
      <td>5817692</td>
      <td>1487580010872045658</td>
      <td>0.79</td>
      <td>...</td>
      <td>23</td>
      <td>59</td>
      <td>28</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-02-29 23:59:54</th>
      <td>view</td>
      <td>5716351</td>
      <td>1487580010872045658</td>
      <td>0.79</td>
      <td>...</td>
      <td>23</td>
      <td>59</td>
      <td>54</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>2074026 rows × 14 columns</p>
</div>



Comprobamos los festivos.


```python
df[df.festivo == 1].date.value_counts().sort_index()
```




    2019-11-04    16430
    2019-12-31     2848
    2020-01-01     7644
    2020-01-02    10776
    2020-01-03    10617
    2020-01-04    13084
    2020-01-05    14554
    2020-01-06    10621
    2020-01-07    12922
    2020-01-08    14004
    2020-02-23     9817
    Name: date, dtype: int64



### Indicadores exógenos

Vamos a añadir indicadores para Black Friday y San Valentín.


```python
df['black_friday'] = 0
df.loc['2019-11-29','black_friday'] = 1

df['san_valentin'] = 0
df.loc['2020-02-14','san_valentin'] = 1
```

Comprobamos


```python
df['black_friday'].value_counts()
```




    0    2051695
    1      22331
    Name: black_friday, dtype: int64




```python
df['san_valentin'].value_counts()
```




    0    2061781
    1      12245
    Name: san_valentin, dtype: int64



## TABLON ANALITICO FINAL

Revisamos lo que tenemos.


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
      <th>evento</th>
      <th>producto</th>
      <th>categoria</th>
      <th>precio</th>
      <th>...</th>
      <th>segundo</th>
      <th>festivo</th>
      <th>black_friday</th>
      <th>san_valentin</th>
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
      <th>2019-10-01 00:01:46</th>
      <td>view</td>
      <td>5843665</td>
      <td>1487580005092295511</td>
      <td>9.44</td>
      <td>...</td>
      <td>46</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:01:55</th>
      <td>cart</td>
      <td>5868461</td>
      <td>1487580013069861041</td>
      <td>3.57</td>
      <td>...</td>
      <td>55</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:02:50</th>
      <td>view</td>
      <td>5877456</td>
      <td>1487580006300255120</td>
      <td>122.22</td>
      <td>...</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:03:41</th>
      <td>view</td>
      <td>5649270</td>
      <td>1487580013749338323</td>
      <td>6.19</td>
      <td>...</td>
      <td>41</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:03:44</th>
      <td>view</td>
      <td>18082</td>
      <td>1487580005411062629</td>
      <td>16.03</td>
      <td>...</td>
      <td>44</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 16 columns</p>
</div>



Vamos a poner las columnas en un orden más natural.


```python
variables = df.columns.to_list()
variables
```




    ['evento',
     'producto',
     'categoria',
     'precio',
     'usuario',
     'sesion',
     'date',
     'año',
     'mes',
     'dia',
     'hora',
     'minuto',
     'segundo',
     'festivo',
     'black_friday',
     'san_valentin']




```python
orden = ['usuario',
         'sesion',
         'categoria',
         'evento',
         'producto',
         'precio']

orden
```




    ['usuario', 'sesion', 'categoria', 'evento', 'producto', 'precio']




```python
resto = [nombre for nombre in variables if nombre not in orden]

resto
```




    ['date',
     'año',
     'mes',
     'dia',
     'hora',
     'minuto',
     'segundo',
     'festivo',
     'black_friday',
     'san_valentin']




```python
df = df[orden + resto]
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
      <th>usuario</th>
      <th>sesion</th>
      <th>categoria</th>
      <th>evento</th>
      <th>...</th>
      <th>segundo</th>
      <th>festivo</th>
      <th>black_friday</th>
      <th>san_valentin</th>
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
      <th>2019-10-01 00:01:46</th>
      <td>462033176</td>
      <td>a18e0999-61a1-4218-8f8f-61ec1d375361</td>
      <td>1487580005092295511</td>
      <td>view</td>
      <td>...</td>
      <td>46</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:01:55</th>
      <td>514753614</td>
      <td>e2fecb2d-22d0-df2c-c661-15da44b3ccf1</td>
      <td>1487580013069861041</td>
      <td>cart</td>
      <td>...</td>
      <td>55</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:02:50</th>
      <td>527418424</td>
      <td>86e77869-afbc-4dff-9aa2-6b7dd8c90770</td>
      <td>1487580006300255120</td>
      <td>view</td>
      <td>...</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:03:41</th>
      <td>555448072</td>
      <td>b5f72ceb-0730-44de-a932-d16db62390df</td>
      <td>1487580013749338323</td>
      <td>view</td>
      <td>...</td>
      <td>41</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:03:44</th>
      <td>552006247</td>
      <td>2d8f304b-de45-4e59-8f40-50c603843fe5</td>
      <td>1487580005411062629</td>
      <td>view</td>
      <td>...</td>
      <td>44</td>
      <td>0</td>
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
    </tr>
    <tr>
      <th>2020-02-29 23:58:49</th>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
      <td>1487580006317032337</td>
      <td>cart</td>
      <td>...</td>
      <td>49</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-02-29 23:58:57</th>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
      <td>1487580006317032337</td>
      <td>view</td>
      <td>...</td>
      <td>57</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-02-29 23:59:05</th>
      <td>147995998</td>
      <td>5ff96629-3627-493e-a25b-5a871ec78c90</td>
      <td>1487580006317032337</td>
      <td>cart</td>
      <td>...</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-02-29 23:59:28</th>
      <td>619841242</td>
      <td>18af673b-7fb9-4202-a66d-5c855bc0fd2d</td>
      <td>1487580010872045658</td>
      <td>view</td>
      <td>...</td>
      <td>28</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-02-29 23:59:54</th>
      <td>619841242</td>
      <td>18af673b-7fb9-4202-a66d-5c855bc0fd2d</td>
      <td>1487580010872045658</td>
      <td>view</td>
      <td>...</td>
      <td>54</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>2074026 rows × 16 columns</p>
</div>



Guardamos como pickle para no perder los metadatos.


```python
df.to_pickle('tablon_analitico.pickle')
```
