# ANALISIS E INSIGHTS (TOTAL)

***NOTA: Este notebook incluye también todas las lecciones, incluyendo las de la parte I, para que puedas ejecutar todos los cálculos y objetos anteriores y de esa forma continuar fácilmente con la parte II que comienza en la lección 1.2.5 ¿Cual es la supervivencia de los clientes?***


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
pd.options.display.max_columns = 8
```


```python
df = pd.read_pickle('tablon_analitico.pickle')
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



## Entendiendo los eventos

### ¿Cómo está funcionando el Customer Journey?


```python
eventos = df.evento.value_counts()
eventos
```




    view                961558
    cart                574547
    remove_from_cart    410357
    purchase            127564
    Name: evento, dtype: int64




```python
kpi_visualizaciones_p = 100
kpi_carrito_p = eventos.loc['cart'] / eventos.loc['view'] * 100
kpi_abandono_p = eventos.loc['remove_from_cart'] / eventos.loc['cart'] * 100
kpi_compra_p = eventos.loc['purchase'] / eventos.loc['cart'] * 100

kpis = pd.DataFrame({'kpi':['visitas','carrito','compra'],
                     'valor':[kpi_visualizaciones_p,kpi_carrito_p,kpi_compra_p]})

kpis
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
      <th>kpi</th>
      <th>valor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>visitas</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>carrito</td>
      <td>59.75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>compra</td>
      <td>22.20</td>
    </tr>
  </tbody>
</table>
</div>



conda install -c conda-forge plotly


```python
from plotly import graph_objects as go

fig = go.Figure(go.Funnel(
    y = kpis.kpi,
    x = kpis.valor.round(2),
    marker = {'color': ['red','blue','green']},
    opacity = 0.3
    ))

fig.update_layout(
    title = 'Funnel Conversión Inicial')
    
fig.show()
```



Conclusiones:

* Las tasas de partida son un 60% de carrito sobre visualiazaciones y un 22% de compra sobre carrito
* Por tanto existe un 40% de visitas sobre las que hay que trabajar para conseguir más carritos, y un 78% de carritos sobre los que trabajar para conseguir más compras

TRUCO PRO:

Este tipo de análisis conviene encapsularlo en funciones.

De tal forma que ante un nuevo cliente que tenga la misma estructura de datos podremos preparar informes automáticos para los análisis más frecuentes.

Por ejemplo vamos a crear una función para hacer funnel analytics.


```python
#Esta función recibe la variable de los eventos como entrada
def funnel_analytics(evento):
    
    #hacemos el conteo
    eventos = df.evento.value_counts()

    #preparamos las variables
    kpi_visitas_p = 100
    kpi_carrito_p = eventos.loc['cart'] / eventos.loc['view'] * 100
    kpi_abandono_p = eventos.loc['remove_from_cart'] / eventos.loc['cart'] * 100
    kpi_compra_p = eventos.loc['purchase'] / eventos.loc['cart'] * 100
    kpis = pd.DataFrame({'kpi':['visitas','carrito','compra'],
                         'valor':[kpi_visitas_p,kpi_carrito_p,kpi_compra_p]})
    
    #creamos el gráfico
    from plotly import graph_objects as go
    fig = go.Figure(go.Funnel(
        y = kpis.kpi,
        x = kpis.valor.round(2),
        marker = {'color': ['red','blue','green']},
        opacity = 0.3
        ))

    fig.update_layout(
        title = 'Funnel Conversión Inicial')

    fig.show()
    
    #imprimimos un informe de conclusiones
    print(f'Las tasas de partida son un {kpi_carrito_p.round(2)}% de carrito sobre visualiazaciones y un {kpi_compra_p.round(2)}% de compra sobre carrito. \n')
    print(f'Por tanto existe un {100 - kpi_carrito_p.round(2)}% de visitas sobre las que hay que trabajar para conseguir más carritos, y un {100 - kpi_compra_p.round(2)}% de carritos sobre los que trabajar para conseguir más compras.')
```

La ejecutamos.


```python
funnel_analytics(df.evento)
```



    Las tasas de partida son un 59.75% de carrito sobre visualiazaciones y un 22.2% de compra sobre carrito. 
    
    Por tanto existe un 40.25% de visitas sobre las que hay que trabajar para conseguir más carritos, y un 77.8% de carritos sobre los que trabajar para conseguir más compras.
    

### ¿Cuántos productos se ven, se añaden al carro, se abandonan y se compran de media en cada sesión?

A diferencia del análisis macro del funnel este análisis es por sesión, lo cual lo hace más operativo.

Conocer los principales kpis por sesión nos permite establecer la línea base para ir midiendo los resultados de las acciones de CRO.

Primero creamos un dataframe con la granularidad a nivel de sesión y evento que necesitamos.


```python
sesion_prod = df.groupby(['sesion','evento']).producto.count()
sesion_prod
```




    sesion                                evento
    0000597b-de39-4a77-9fe5-02c8792ca14e  view      3
    0000645a-8160-4a3d-91bf-154bff0a22e3  view      2
    000090e1-da13-42b1-a31b-91a9ee5e6a88  view      1
    0000b3cb-5422-4bf2-b8fe-5c1831d0dc1b  view      1
    0000de26-bd58-42c9-9173-4763c76b398e  view      1
                                                   ..
    ffff6695-b64d-4a67-aa14-34b3b7f63c3f  view      2
    ffff7d69-b706-4c64-9d6d-da57a04bc32b  view      1
    ffff8044-2a22-4846-8a72-999e870abbe9  view      1
    ffff91d4-7879-4a4b-8b26-c67915a27dc8  view      1
    ffffbe0a-d2c2-47c7-afab-680bfdfda50d  view      1
    Name: producto, Length: 581763, dtype: int64



Pasamos los eventos a columnas.


```python
sesion_prod = sesion_prod.unstack().fillna(0)
sesion_prod
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
      <th>evento</th>
      <th>cart</th>
      <th>purchase</th>
      <th>remove_from_cart</th>
      <th>view</th>
    </tr>
    <tr>
      <th>sesion</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0000597b-de39-4a77-9fe5-02c8792ca14e</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>0000645a-8160-4a3d-91bf-154bff0a22e3</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2.00</td>
    </tr>
    <tr>
      <th>000090e1-da13-42b1-a31b-91a9ee5e6a88</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>0000b3cb-5422-4bf2-b8fe-5c1831d0dc1b</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>0000de26-bd58-42c9-9173-4763c76b398e</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>ffff6695-b64d-4a67-aa14-34b3b7f63c3f</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2.00</td>
    </tr>
    <tr>
      <th>ffff7d69-b706-4c64-9d6d-da57a04bc32b</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>ffff8044-2a22-4846-8a72-999e870abbe9</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>ffff91d4-7879-4a4b-8b26-c67915a27dc8</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>ffffbe0a-d2c2-47c7-afab-680bfdfda50d</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
<p>446054 rows × 4 columns</p>
</div>



Para comprobar calculamos los totales y debería darnos los mismos que a nivel global.


```python
sesion_prod.sum()
```




    evento
    cart                     574547.00
    purchase                 127564.00
    remove_from_cart         410357.00
    view                     961558.00
    dtype: float64



Reordenamos las columnas.


```python
sesion_prod = sesion_prod[['view','cart','remove_from_cart','purchase']]
sesion_prod
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
      <th>evento</th>
      <th>view</th>
      <th>cart</th>
      <th>remove_from_cart</th>
      <th>purchase</th>
    </tr>
    <tr>
      <th>sesion</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0000597b-de39-4a77-9fe5-02c8792ca14e</th>
      <td>3.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>0000645a-8160-4a3d-91bf-154bff0a22e3</th>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>000090e1-da13-42b1-a31b-91a9ee5e6a88</th>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>0000b3cb-5422-4bf2-b8fe-5c1831d0dc1b</th>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>0000de26-bd58-42c9-9173-4763c76b398e</th>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
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
      <th>ffff6695-b64d-4a67-aa14-34b3b7f63c3f</th>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>ffff7d69-b706-4c64-9d6d-da57a04bc32b</th>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>ffff8044-2a22-4846-8a72-999e870abbe9</th>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>ffff91d4-7879-4a4b-8b26-c67915a27dc8</th>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>ffffbe0a-d2c2-47c7-afab-680bfdfda50d</th>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>446054 rows × 4 columns</p>
</div>



Calculamos la media de cada evento por sesión.


```python
media_eventos_sesion = sesion_prod.mean()
media_eventos_sesion
```




    evento
    view                          2.16
    cart                          1.29
    remove_from_cart              0.92
    purchase                      0.29
    dtype: float64



Conclusión:

En cada sesión, de media:

* Se ven 2.2 productos
* Se añaden 1.3 productos al carrito
* Se eliminan 0.9 productos del carrito
* Se compran 0.3 productos

Como decíamos, éstos son los números que deberemos incrementar con las acciones de CRO.

### ¿Existen diferencias entre los eventos por horas?

Creamos el dataframe a granularidad evento y hora.


```python
eventos_hora = df.groupby(['evento','hora']).producto.count()
eventos_hora
```




    evento  hora
    cart    0        6475
            1        5555
            2        6433
            3        8544
            4       11242
                    ...  
    view    19      63730
            20      57311
            21      38905
            22      23043
            23      13307
    Name: producto, Length: 96, dtype: int64



Pasamos los eventos a columnas.


```python
eventos_hora = eventos_hora.unstack(level = 0)
eventos_hora
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
      <th>evento</th>
      <th>cart</th>
      <th>purchase</th>
      <th>remove_from_cart</th>
      <th>view</th>
    </tr>
    <tr>
      <th>hora</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6475</td>
      <td>962</td>
      <td>3238</td>
      <td>8731</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5555</td>
      <td>1128</td>
      <td>3930</td>
      <td>7280</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6433</td>
      <td>1220</td>
      <td>3509</td>
      <td>8378</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8544</td>
      <td>1535</td>
      <td>5331</td>
      <td>11807</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11242</td>
      <td>2389</td>
      <td>8095</td>
      <td>18365</td>
    </tr>
    <tr>
      <th>5</th>
      <td>16890</td>
      <td>3491</td>
      <td>11913</td>
      <td>27438</td>
    </tr>
    <tr>
      <th>6</th>
      <td>21993</td>
      <td>5125</td>
      <td>16223</td>
      <td>38055</td>
    </tr>
    <tr>
      <th>7</th>
      <td>27069</td>
      <td>5951</td>
      <td>17883</td>
      <td>46072</td>
    </tr>
    <tr>
      <th>8</th>
      <td>29526</td>
      <td>7158</td>
      <td>21156</td>
      <td>49587</td>
    </tr>
    <tr>
      <th>9</th>
      <td>32095</td>
      <td>7593</td>
      <td>21680</td>
      <td>54185</td>
    </tr>
    <tr>
      <th>10</th>
      <td>32901</td>
      <td>7816</td>
      <td>23982</td>
      <td>56458</td>
    </tr>
    <tr>
      <th>11</th>
      <td>33284</td>
      <td>8495</td>
      <td>25496</td>
      <td>57594</td>
    </tr>
    <tr>
      <th>12</th>
      <td>34258</td>
      <td>8250</td>
      <td>23714</td>
      <td>57530</td>
    </tr>
    <tr>
      <th>13</th>
      <td>31996</td>
      <td>8133</td>
      <td>22852</td>
      <td>55534</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30451</td>
      <td>7122</td>
      <td>21835</td>
      <td>52184</td>
    </tr>
    <tr>
      <th>15</th>
      <td>28789</td>
      <td>6485</td>
      <td>20162</td>
      <td>49809</td>
    </tr>
    <tr>
      <th>16</th>
      <td>28775</td>
      <td>6531</td>
      <td>19791</td>
      <td>51055</td>
    </tr>
    <tr>
      <th>17</th>
      <td>32525</td>
      <td>6242</td>
      <td>24330</td>
      <td>55667</td>
    </tr>
    <tr>
      <th>18</th>
      <td>36435</td>
      <td>8211</td>
      <td>30551</td>
      <td>59533</td>
    </tr>
    <tr>
      <th>19</th>
      <td>39609</td>
      <td>7435</td>
      <td>27666</td>
      <td>63730</td>
    </tr>
    <tr>
      <th>20</th>
      <td>34828</td>
      <td>7256</td>
      <td>24985</td>
      <td>57311</td>
    </tr>
    <tr>
      <th>21</th>
      <td>23228</td>
      <td>4606</td>
      <td>17396</td>
      <td>38905</td>
    </tr>
    <tr>
      <th>22</th>
      <td>13589</td>
      <td>2883</td>
      <td>8680</td>
      <td>23043</td>
    </tr>
    <tr>
      <th>23</th>
      <td>8057</td>
      <td>1547</td>
      <td>5959</td>
      <td>13307</td>
    </tr>
  </tbody>
</table>
</div>



Vamos a visualizar cómo se distribuyen los eventos por hora.


```python
eventos_hora.plot()
plt.xticks(ticks = eventos_hora.index);
```


    
![png](static/notebooks/ecommerce/part3_files/part3_34_0.png)
    


Existe una pauta global como era de esperar.

Pero para ver mejor las diferencias podemos crear una nueva variable que sea el ratio de compras por visita en cada hora.


```python
eventos_hora['compras_visitas'] = eventos_hora.purchase / eventos_hora.view * 100
eventos_hora
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
      <th>evento</th>
      <th>cart</th>
      <th>purchase</th>
      <th>remove_from_cart</th>
      <th>view</th>
      <th>compras_visitas</th>
    </tr>
    <tr>
      <th>hora</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6475</td>
      <td>962</td>
      <td>3238</td>
      <td>8731</td>
      <td>11.02</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5555</td>
      <td>1128</td>
      <td>3930</td>
      <td>7280</td>
      <td>15.49</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6433</td>
      <td>1220</td>
      <td>3509</td>
      <td>8378</td>
      <td>14.56</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8544</td>
      <td>1535</td>
      <td>5331</td>
      <td>11807</td>
      <td>13.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11242</td>
      <td>2389</td>
      <td>8095</td>
      <td>18365</td>
      <td>13.01</td>
    </tr>
    <tr>
      <th>5</th>
      <td>16890</td>
      <td>3491</td>
      <td>11913</td>
      <td>27438</td>
      <td>12.72</td>
    </tr>
    <tr>
      <th>6</th>
      <td>21993</td>
      <td>5125</td>
      <td>16223</td>
      <td>38055</td>
      <td>13.47</td>
    </tr>
    <tr>
      <th>7</th>
      <td>27069</td>
      <td>5951</td>
      <td>17883</td>
      <td>46072</td>
      <td>12.92</td>
    </tr>
    <tr>
      <th>8</th>
      <td>29526</td>
      <td>7158</td>
      <td>21156</td>
      <td>49587</td>
      <td>14.44</td>
    </tr>
    <tr>
      <th>9</th>
      <td>32095</td>
      <td>7593</td>
      <td>21680</td>
      <td>54185</td>
      <td>14.01</td>
    </tr>
    <tr>
      <th>10</th>
      <td>32901</td>
      <td>7816</td>
      <td>23982</td>
      <td>56458</td>
      <td>13.84</td>
    </tr>
    <tr>
      <th>11</th>
      <td>33284</td>
      <td>8495</td>
      <td>25496</td>
      <td>57594</td>
      <td>14.75</td>
    </tr>
    <tr>
      <th>12</th>
      <td>34258</td>
      <td>8250</td>
      <td>23714</td>
      <td>57530</td>
      <td>14.34</td>
    </tr>
    <tr>
      <th>13</th>
      <td>31996</td>
      <td>8133</td>
      <td>22852</td>
      <td>55534</td>
      <td>14.65</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30451</td>
      <td>7122</td>
      <td>21835</td>
      <td>52184</td>
      <td>13.65</td>
    </tr>
    <tr>
      <th>15</th>
      <td>28789</td>
      <td>6485</td>
      <td>20162</td>
      <td>49809</td>
      <td>13.02</td>
    </tr>
    <tr>
      <th>16</th>
      <td>28775</td>
      <td>6531</td>
      <td>19791</td>
      <td>51055</td>
      <td>12.79</td>
    </tr>
    <tr>
      <th>17</th>
      <td>32525</td>
      <td>6242</td>
      <td>24330</td>
      <td>55667</td>
      <td>11.21</td>
    </tr>
    <tr>
      <th>18</th>
      <td>36435</td>
      <td>8211</td>
      <td>30551</td>
      <td>59533</td>
      <td>13.79</td>
    </tr>
    <tr>
      <th>19</th>
      <td>39609</td>
      <td>7435</td>
      <td>27666</td>
      <td>63730</td>
      <td>11.67</td>
    </tr>
    <tr>
      <th>20</th>
      <td>34828</td>
      <td>7256</td>
      <td>24985</td>
      <td>57311</td>
      <td>12.66</td>
    </tr>
    <tr>
      <th>21</th>
      <td>23228</td>
      <td>4606</td>
      <td>17396</td>
      <td>38905</td>
      <td>11.84</td>
    </tr>
    <tr>
      <th>22</th>
      <td>13589</td>
      <td>2883</td>
      <td>8680</td>
      <td>23043</td>
      <td>12.51</td>
    </tr>
    <tr>
      <th>23</th>
      <td>8057</td>
      <td>1547</td>
      <td>5959</td>
      <td>13307</td>
      <td>11.63</td>
    </tr>
  </tbody>
</table>
</div>



Reordenamos las variables


```python
eventos_hora = eventos_hora[['view','cart','remove_from_cart','purchase','compras_visitas']]
eventos_hora
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
      <th>evento</th>
      <th>view</th>
      <th>cart</th>
      <th>remove_from_cart</th>
      <th>purchase</th>
      <th>compras_visitas</th>
    </tr>
    <tr>
      <th>hora</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8731</td>
      <td>6475</td>
      <td>3238</td>
      <td>962</td>
      <td>11.02</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7280</td>
      <td>5555</td>
      <td>3930</td>
      <td>1128</td>
      <td>15.49</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8378</td>
      <td>6433</td>
      <td>3509</td>
      <td>1220</td>
      <td>14.56</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11807</td>
      <td>8544</td>
      <td>5331</td>
      <td>1535</td>
      <td>13.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>18365</td>
      <td>11242</td>
      <td>8095</td>
      <td>2389</td>
      <td>13.01</td>
    </tr>
    <tr>
      <th>5</th>
      <td>27438</td>
      <td>16890</td>
      <td>11913</td>
      <td>3491</td>
      <td>12.72</td>
    </tr>
    <tr>
      <th>6</th>
      <td>38055</td>
      <td>21993</td>
      <td>16223</td>
      <td>5125</td>
      <td>13.47</td>
    </tr>
    <tr>
      <th>7</th>
      <td>46072</td>
      <td>27069</td>
      <td>17883</td>
      <td>5951</td>
      <td>12.92</td>
    </tr>
    <tr>
      <th>8</th>
      <td>49587</td>
      <td>29526</td>
      <td>21156</td>
      <td>7158</td>
      <td>14.44</td>
    </tr>
    <tr>
      <th>9</th>
      <td>54185</td>
      <td>32095</td>
      <td>21680</td>
      <td>7593</td>
      <td>14.01</td>
    </tr>
    <tr>
      <th>10</th>
      <td>56458</td>
      <td>32901</td>
      <td>23982</td>
      <td>7816</td>
      <td>13.84</td>
    </tr>
    <tr>
      <th>11</th>
      <td>57594</td>
      <td>33284</td>
      <td>25496</td>
      <td>8495</td>
      <td>14.75</td>
    </tr>
    <tr>
      <th>12</th>
      <td>57530</td>
      <td>34258</td>
      <td>23714</td>
      <td>8250</td>
      <td>14.34</td>
    </tr>
    <tr>
      <th>13</th>
      <td>55534</td>
      <td>31996</td>
      <td>22852</td>
      <td>8133</td>
      <td>14.65</td>
    </tr>
    <tr>
      <th>14</th>
      <td>52184</td>
      <td>30451</td>
      <td>21835</td>
      <td>7122</td>
      <td>13.65</td>
    </tr>
    <tr>
      <th>15</th>
      <td>49809</td>
      <td>28789</td>
      <td>20162</td>
      <td>6485</td>
      <td>13.02</td>
    </tr>
    <tr>
      <th>16</th>
      <td>51055</td>
      <td>28775</td>
      <td>19791</td>
      <td>6531</td>
      <td>12.79</td>
    </tr>
    <tr>
      <th>17</th>
      <td>55667</td>
      <td>32525</td>
      <td>24330</td>
      <td>6242</td>
      <td>11.21</td>
    </tr>
    <tr>
      <th>18</th>
      <td>59533</td>
      <td>36435</td>
      <td>30551</td>
      <td>8211</td>
      <td>13.79</td>
    </tr>
    <tr>
      <th>19</th>
      <td>63730</td>
      <td>39609</td>
      <td>27666</td>
      <td>7435</td>
      <td>11.67</td>
    </tr>
    <tr>
      <th>20</th>
      <td>57311</td>
      <td>34828</td>
      <td>24985</td>
      <td>7256</td>
      <td>12.66</td>
    </tr>
    <tr>
      <th>21</th>
      <td>38905</td>
      <td>23228</td>
      <td>17396</td>
      <td>4606</td>
      <td>11.84</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23043</td>
      <td>13589</td>
      <td>8680</td>
      <td>2883</td>
      <td>12.51</td>
    </tr>
    <tr>
      <th>23</th>
      <td>13307</td>
      <td>8057</td>
      <td>5959</td>
      <td>1547</td>
      <td>11.63</td>
    </tr>
  </tbody>
</table>
</div>



Visualizamos para ver si hay horas en las que se compra proporcionalmente más.


```python
plt.figure(figsize = (12,6))
sns.lineplot(data = eventos_hora, x = eventos_hora.index, y = 'compras_visitas')
plt.xticks(eventos_hora.index);
```


    
![png](static/notebooks/ecommerce/part3_files/part3_40_0.png)
    


Conclusiones:
    
* Las horas en las que la gente compra más son la 1, las 8, de 11 a 13 y las 18
* Las horas en las que la gente no compra son las 24, de 3 a 7, de 14 a 17 y de 19 a 23

Vamos a analizar ahora no de forma proporcional, si no en absoluto si existen o no horas más frecuentes para cada tipo de evento.


```python
plt.figure(figsize = (12,12))
sns.heatmap(data = eventos_hora);
```


    
![png](static/notebooks/ecommerce/part3_files/part3_42_0.png)
    


El problema es que como cada evento tiene diferente escala este gráfico no nos permite diferenciar bien los patrones.

Para solucionarlo podemos usar la tipificación de variables que aprendimos en el módulo de estadística.


```python
def tipificar(variable):
    media = variable.mean()
    dt = variable.std()
    return(variable.apply(lambda x: (x - media) / dt))
```


```python
eventos_hora_tip = eventos_hora.apply(tipificar)
eventos_hora_tip
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
      <th>evento</th>
      <th>view</th>
      <th>cart</th>
      <th>remove_from_cart</th>
      <th>purchase</th>
      <th>compras_visitas</th>
    </tr>
    <tr>
      <th>hora</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-1.60</td>
      <td>-1.56</td>
      <td>-1.63</td>
      <td>-1.62</td>
      <td>-1.83</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-1.68</td>
      <td>-1.64</td>
      <td>-1.54</td>
      <td>-1.56</td>
      <td>1.91</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.62</td>
      <td>-1.56</td>
      <td>-1.59</td>
      <td>-1.53</td>
      <td>1.13</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.45</td>
      <td>-1.37</td>
      <td>-1.38</td>
      <td>-1.41</td>
      <td>-0.17</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-1.11</td>
      <td>-1.13</td>
      <td>-1.06</td>
      <td>-1.09</td>
      <td>-0.17</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-0.65</td>
      <td>-0.63</td>
      <td>-0.61</td>
      <td>-0.68</td>
      <td>-0.41</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.10</td>
      <td>-0.17</td>
      <td>-0.10</td>
      <td>-0.07</td>
      <td>0.22</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.31</td>
      <td>0.28</td>
      <td>0.09</td>
      <td>0.24</td>
      <td>-0.24</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.49</td>
      <td>0.50</td>
      <td>0.48</td>
      <td>0.69</td>
      <td>1.03</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.72</td>
      <td>0.73</td>
      <td>0.54</td>
      <td>0.85</td>
      <td>0.67</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.84</td>
      <td>0.80</td>
      <td>0.81</td>
      <td>0.93</td>
      <td>0.53</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.90</td>
      <td>0.83</td>
      <td>0.99</td>
      <td>1.19</td>
      <td>1.29</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.89</td>
      <td>0.92</td>
      <td>0.78</td>
      <td>1.09</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.79</td>
      <td>0.72</td>
      <td>0.67</td>
      <td>1.05</td>
      <td>1.20</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.62</td>
      <td>0.58</td>
      <td>0.56</td>
      <td>0.67</td>
      <td>0.37</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.50</td>
      <td>0.43</td>
      <td>0.36</td>
      <td>0.44</td>
      <td>-0.16</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.56</td>
      <td>0.43</td>
      <td>0.32</td>
      <td>0.45</td>
      <td>-0.35</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0.80</td>
      <td>0.77</td>
      <td>0.85</td>
      <td>0.35</td>
      <td>-1.67</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1.00</td>
      <td>1.11</td>
      <td>1.58</td>
      <td>1.08</td>
      <td>0.49</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1.21</td>
      <td>1.40</td>
      <td>1.24</td>
      <td>0.79</td>
      <td>-1.29</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.88</td>
      <td>0.97</td>
      <td>0.93</td>
      <td>0.72</td>
      <td>-0.46</td>
    </tr>
    <tr>
      <th>21</th>
      <td>-0.06</td>
      <td>-0.06</td>
      <td>0.03</td>
      <td>-0.26</td>
      <td>-1.14</td>
    </tr>
    <tr>
      <th>22</th>
      <td>-0.87</td>
      <td>-0.92</td>
      <td>-0.99</td>
      <td>-0.91</td>
      <td>-0.58</td>
    </tr>
    <tr>
      <th>23</th>
      <td>-1.37</td>
      <td>-1.42</td>
      <td>-1.31</td>
      <td>-1.40</td>
      <td>-1.32</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize = (12,12))
sns.heatmap(data = eventos_hora_tip);
```


    
![png](static/notebooks/ecommerce/part3_files/part3_46_0.png)
    


Vamos a sacar también los gráficos de líneas para verlo más claramente.


```python
eventos_hora_tip.plot(subplots = True, sharex = False, figsize = (12,12),xticks = eventos_hora_tip.index);
```


    
![png](static/notebooks/ecommerce/part3_files/part3_48_0.png)
    


Conclusiones:

* **INSIGHT #1**: Todas las métricas se maximzan en las franjas entre las 9 y las 13 y entre las 18 y las 20
* Esta info es muy relevante por ejemplo de cara a paid ads, tanto de generación de tráfico como de retargeting
* Además, parece haber algún subtipo de usuario que compra a la 1 de la mañana, que aunque no sea muy frecuente sí compra mucho

### ¿Cúal es la media de facturación mensual?


```python
df.loc[df.evento == 'purchase'].groupby('mes').precio.sum().mean()
```




    124309.92



### ¿Cúal es la tendencia en los últimos meses?


```python
tendencia = df.groupby('evento').resample('W').evento.count().unstack(level = 0)
tendencia
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
      <th>evento</th>
      <th>cart</th>
      <th>purchase</th>
      <th>remove_from_cart</th>
      <th>view</th>
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
      <th>2019-10-06</th>
      <td>31483</td>
      <td>4440</td>
      <td>14647</td>
      <td>36353</td>
    </tr>
    <tr>
      <th>2019-10-13</th>
      <td>28151</td>
      <td>5422</td>
      <td>17989</td>
      <td>44410</td>
    </tr>
    <tr>
      <th>2019-10-20</th>
      <td>23920</td>
      <td>5033</td>
      <td>15303</td>
      <td>39486</td>
    </tr>
    <tr>
      <th>2019-10-27</th>
      <td>25651</td>
      <td>5665</td>
      <td>18411</td>
      <td>40383</td>
    </tr>
    <tr>
      <th>2019-11-03</th>
      <td>24087</td>
      <td>5746</td>
      <td>16491</td>
      <td>39365</td>
    </tr>
    <tr>
      <th>2019-11-10</th>
      <td>29142</td>
      <td>6663</td>
      <td>24008</td>
      <td>46177</td>
    </tr>
    <tr>
      <th>2019-11-17</th>
      <td>25335</td>
      <td>5141</td>
      <td>17215</td>
      <td>41170</td>
    </tr>
    <tr>
      <th>2019-11-24</th>
      <td>38069</td>
      <td>9754</td>
      <td>27973</td>
      <td>56477</td>
    </tr>
    <tr>
      <th>2019-12-01</th>
      <td>31994</td>
      <td>7493</td>
      <td>23106</td>
      <td>48883</td>
    </tr>
    <tr>
      <th>2019-12-08</th>
      <td>23265</td>
      <td>5105</td>
      <td>19443</td>
      <td>42055</td>
    </tr>
    <tr>
      <th>2019-12-15</th>
      <td>24636</td>
      <td>5953</td>
      <td>18246</td>
      <td>45874</td>
    </tr>
    <tr>
      <th>2019-12-22</th>
      <td>19927</td>
      <td>4701</td>
      <td>15452</td>
      <td>39237</td>
    </tr>
    <tr>
      <th>2019-12-29</th>
      <td>17051</td>
      <td>3705</td>
      <td>11102</td>
      <td>32803</td>
    </tr>
    <tr>
      <th>2020-01-05</th>
      <td>16735</td>
      <td>3294</td>
      <td>13464</td>
      <td>31909</td>
    </tr>
    <tr>
      <th>2020-01-12</th>
      <td>26264</td>
      <td>5589</td>
      <td>17956</td>
      <td>46873</td>
    </tr>
    <tr>
      <th>2020-01-19</th>
      <td>28402</td>
      <td>6913</td>
      <td>22945</td>
      <td>50210</td>
    </tr>
    <tr>
      <th>2020-01-26</th>
      <td>26353</td>
      <td>6359</td>
      <td>18544</td>
      <td>48478</td>
    </tr>
    <tr>
      <th>2020-02-02</th>
      <td>29193</td>
      <td>7120</td>
      <td>21102</td>
      <td>52432</td>
    </tr>
    <tr>
      <th>2020-02-09</th>
      <td>28796</td>
      <td>5853</td>
      <td>20050</td>
      <td>48422</td>
    </tr>
    <tr>
      <th>2020-02-16</th>
      <td>27836</td>
      <td>6332</td>
      <td>22601</td>
      <td>47213</td>
    </tr>
    <tr>
      <th>2020-02-23</th>
      <td>25619</td>
      <td>6000</td>
      <td>18146</td>
      <td>43627</td>
    </tr>
    <tr>
      <th>2020-03-01</th>
      <td>22638</td>
      <td>5283</td>
      <td>16163</td>
      <td>39721</td>
    </tr>
  </tbody>
</table>
</div>




```python
tendencia = tendencia[['view','cart','remove_from_cart','purchase']]
tendencia
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
      <th>evento</th>
      <th>view</th>
      <th>cart</th>
      <th>remove_from_cart</th>
      <th>purchase</th>
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
      <th>2019-10-06</th>
      <td>36353</td>
      <td>31483</td>
      <td>14647</td>
      <td>4440</td>
    </tr>
    <tr>
      <th>2019-10-13</th>
      <td>44410</td>
      <td>28151</td>
      <td>17989</td>
      <td>5422</td>
    </tr>
    <tr>
      <th>2019-10-20</th>
      <td>39486</td>
      <td>23920</td>
      <td>15303</td>
      <td>5033</td>
    </tr>
    <tr>
      <th>2019-10-27</th>
      <td>40383</td>
      <td>25651</td>
      <td>18411</td>
      <td>5665</td>
    </tr>
    <tr>
      <th>2019-11-03</th>
      <td>39365</td>
      <td>24087</td>
      <td>16491</td>
      <td>5746</td>
    </tr>
    <tr>
      <th>2019-11-10</th>
      <td>46177</td>
      <td>29142</td>
      <td>24008</td>
      <td>6663</td>
    </tr>
    <tr>
      <th>2019-11-17</th>
      <td>41170</td>
      <td>25335</td>
      <td>17215</td>
      <td>5141</td>
    </tr>
    <tr>
      <th>2019-11-24</th>
      <td>56477</td>
      <td>38069</td>
      <td>27973</td>
      <td>9754</td>
    </tr>
    <tr>
      <th>2019-12-01</th>
      <td>48883</td>
      <td>31994</td>
      <td>23106</td>
      <td>7493</td>
    </tr>
    <tr>
      <th>2019-12-08</th>
      <td>42055</td>
      <td>23265</td>
      <td>19443</td>
      <td>5105</td>
    </tr>
    <tr>
      <th>2019-12-15</th>
      <td>45874</td>
      <td>24636</td>
      <td>18246</td>
      <td>5953</td>
    </tr>
    <tr>
      <th>2019-12-22</th>
      <td>39237</td>
      <td>19927</td>
      <td>15452</td>
      <td>4701</td>
    </tr>
    <tr>
      <th>2019-12-29</th>
      <td>32803</td>
      <td>17051</td>
      <td>11102</td>
      <td>3705</td>
    </tr>
    <tr>
      <th>2020-01-05</th>
      <td>31909</td>
      <td>16735</td>
      <td>13464</td>
      <td>3294</td>
    </tr>
    <tr>
      <th>2020-01-12</th>
      <td>46873</td>
      <td>26264</td>
      <td>17956</td>
      <td>5589</td>
    </tr>
    <tr>
      <th>2020-01-19</th>
      <td>50210</td>
      <td>28402</td>
      <td>22945</td>
      <td>6913</td>
    </tr>
    <tr>
      <th>2020-01-26</th>
      <td>48478</td>
      <td>26353</td>
      <td>18544</td>
      <td>6359</td>
    </tr>
    <tr>
      <th>2020-02-02</th>
      <td>52432</td>
      <td>29193</td>
      <td>21102</td>
      <td>7120</td>
    </tr>
    <tr>
      <th>2020-02-09</th>
      <td>48422</td>
      <td>28796</td>
      <td>20050</td>
      <td>5853</td>
    </tr>
    <tr>
      <th>2020-02-16</th>
      <td>47213</td>
      <td>27836</td>
      <td>22601</td>
      <td>6332</td>
    </tr>
    <tr>
      <th>2020-02-23</th>
      <td>43627</td>
      <td>25619</td>
      <td>18146</td>
      <td>6000</td>
    </tr>
    <tr>
      <th>2020-03-01</th>
      <td>39721</td>
      <td>22638</td>
      <td>16163</td>
      <td>5283</td>
    </tr>
  </tbody>
</table>
</div>




```python
tendencia.plot(subplots = True, figsize = (12,6), sharex = True, xticks = tendencia.index, x_compat=True, rot = 90);
```


    
![png](static/notebooks/ecommerce/part3_files/part3_55_0.png)
    


La tendencia es plana en todas las métricas, lo que confirma la necesidad de las acciones de CRO.

Existe un pico significativo en la semana del 24, obviamente por black friday, vamos a hacer el mismo análisis pero diario y solo para noviembre y dicienbre para ver el efecto.


```python
tendencia_diaria = df.loc['2019-11':'2019-12'].groupby('evento').resample('D').evento.count().unstack(level = 0)
tendencia_diaria
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
      <th>evento</th>
      <th>cart</th>
      <th>purchase</th>
      <th>remove_from_cart</th>
      <th>view</th>
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
      <th>2019-11-01</th>
      <td>3565</td>
      <td>709</td>
      <td>2810</td>
      <td>5352</td>
    </tr>
    <tr>
      <th>2019-11-02</th>
      <td>3015</td>
      <td>912</td>
      <td>2124</td>
      <td>4857</td>
    </tr>
    <tr>
      <th>2019-11-03</th>
      <td>3540</td>
      <td>755</td>
      <td>2622</td>
      <td>5583</td>
    </tr>
    <tr>
      <th>2019-11-04</th>
      <td>4652</td>
      <td>676</td>
      <td>4854</td>
      <td>6248</td>
    </tr>
    <tr>
      <th>2019-11-05</th>
      <td>4118</td>
      <td>753</td>
      <td>2711</td>
      <td>7213</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2019-12-27</th>
      <td>2023</td>
      <td>507</td>
      <td>1335</td>
      <td>4058</td>
    </tr>
    <tr>
      <th>2019-12-28</th>
      <td>1744</td>
      <td>329</td>
      <td>1193</td>
      <td>3704</td>
    </tr>
    <tr>
      <th>2019-12-29</th>
      <td>2134</td>
      <td>263</td>
      <td>1149</td>
      <td>3939</td>
    </tr>
    <tr>
      <th>2019-12-30</th>
      <td>1364</td>
      <td>258</td>
      <td>823</td>
      <td>3434</td>
    </tr>
    <tr>
      <th>2019-12-31</th>
      <td>563</td>
      <td>114</td>
      <td>447</td>
      <td>1724</td>
    </tr>
  </tbody>
</table>
<p>61 rows × 4 columns</p>
</div>




```python
tendencia_diaria = tendencia_diaria[['view','cart','remove_from_cart','purchase']]
tendencia_diaria
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
      <th>evento</th>
      <th>view</th>
      <th>cart</th>
      <th>remove_from_cart</th>
      <th>purchase</th>
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
      <th>2019-11-01</th>
      <td>5352</td>
      <td>3565</td>
      <td>2810</td>
      <td>709</td>
    </tr>
    <tr>
      <th>2019-11-02</th>
      <td>4857</td>
      <td>3015</td>
      <td>2124</td>
      <td>912</td>
    </tr>
    <tr>
      <th>2019-11-03</th>
      <td>5583</td>
      <td>3540</td>
      <td>2622</td>
      <td>755</td>
    </tr>
    <tr>
      <th>2019-11-04</th>
      <td>6248</td>
      <td>4652</td>
      <td>4854</td>
      <td>676</td>
    </tr>
    <tr>
      <th>2019-11-05</th>
      <td>7213</td>
      <td>4118</td>
      <td>2711</td>
      <td>753</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2019-12-27</th>
      <td>4058</td>
      <td>2023</td>
      <td>1335</td>
      <td>507</td>
    </tr>
    <tr>
      <th>2019-12-28</th>
      <td>3704</td>
      <td>1744</td>
      <td>1193</td>
      <td>329</td>
    </tr>
    <tr>
      <th>2019-12-29</th>
      <td>3939</td>
      <td>2134</td>
      <td>1149</td>
      <td>263</td>
    </tr>
    <tr>
      <th>2019-12-30</th>
      <td>3434</td>
      <td>1364</td>
      <td>823</td>
      <td>258</td>
    </tr>
    <tr>
      <th>2019-12-31</th>
      <td>1724</td>
      <td>563</td>
      <td>447</td>
      <td>114</td>
    </tr>
  </tbody>
</table>
<p>61 rows × 4 columns</p>
</div>




```python
tendencia_diaria.plot(subplots = True, figsize = (16,10), sharex = True, xticks = tendencia_diaria.index, x_compat=True, rot = 90);
```


    
![png](static/notebooks/ecommerce/part3_files/part3_59_0.png)
    


Conclusiones:

* Efectivamente el pico coincide con el black friday (día 29)
* Pero aún hay un pico mayor unos días antes, el día 22, posiblemente por el inicio de la semana black friday
* Sorprendemente los propios días de Navidad tienen una tendencia decreciente, lo que significa que los consumidores claramente han adelantado sus compras

Vamos a hacer el mismo análisis para Enero y Febrero.


```python
tendencia_diaria = df.loc['2020-01':'2020-02'].groupby('evento').resample('D').evento.count().unstack(level = 0)
tendencia_diaria = tendencia_diaria[['view','cart','remove_from_cart','purchase']]
tendencia_diaria.plot(subplots = True, figsize = (16,10), sharex = True, xticks = tendencia_diaria.index, x_compat=True, rot = 90);
```


    
![png](static/notebooks/ecommerce/part3_files/part3_61_0.png)
    


Conclusiones:

* Durante la semana de Reyes tampoco hay pico de ventas
* Ni los días previos a San Valentín
* Pero sí hay un pico muy pronunciado el 27 de Enero, seguramente algún evento local

**INSIGHT #2** La gran conclusión es que todo el pastel de las compras navideñas se reparte en la semana del black friday

### ¿Momentos de la verdad?

¿Podríamos llegar a identificar momentos a nivel de día-hora en los que se producen el mayor número de compras?

Sería muy útil para concentrar gran parte de la inversión de campañas justo en esos momentos.


```python
compras_dia_hora = df.loc[df.evento == 'purchase'].groupby(['date','hora']).evento.count().unstack(level = 0).fillna(0)
compras_dia_hora
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
      <th>date</th>
      <th>2019-10-01</th>
      <th>2019-10-02</th>
      <th>2019-10-03</th>
      <th>2019-10-04</th>
      <th>...</th>
      <th>2020-02-26</th>
      <th>2020-02-27</th>
      <th>2020-02-28</th>
      <th>2020-02-29</th>
    </tr>
    <tr>
      <th>hora</th>
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
      <th>0</th>
      <td>13.00</td>
      <td>18.00</td>
      <td>1.00</td>
      <td>2.00</td>
      <td>...</td>
      <td>5.00</td>
      <td>40.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>5.00</td>
      <td>0.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>5.00</td>
      <td>26.00</td>
      <td>33.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>24.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>8.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.00</td>
      <td>24.00</td>
      <td>10.00</td>
      <td>0.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>10.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15.00</td>
      <td>0.00</td>
      <td>45.00</td>
      <td>27.00</td>
      <td>...</td>
      <td>10.00</td>
      <td>148.00</td>
      <td>16.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>5</th>
      <td>49.00</td>
      <td>9.00</td>
      <td>6.00</td>
      <td>17.00</td>
      <td>...</td>
      <td>6.00</td>
      <td>48.00</td>
      <td>11.00</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>6</th>
      <td>23.00</td>
      <td>34.00</td>
      <td>18.00</td>
      <td>10.00</td>
      <td>...</td>
      <td>94.00</td>
      <td>26.00</td>
      <td>58.00</td>
      <td>35.00</td>
    </tr>
    <tr>
      <th>7</th>
      <td>26.00</td>
      <td>60.00</td>
      <td>26.00</td>
      <td>54.00</td>
      <td>...</td>
      <td>30.00</td>
      <td>53.00</td>
      <td>38.00</td>
      <td>65.00</td>
    </tr>
    <tr>
      <th>8</th>
      <td>28.00</td>
      <td>71.00</td>
      <td>129.00</td>
      <td>49.00</td>
      <td>...</td>
      <td>120.00</td>
      <td>80.00</td>
      <td>67.00</td>
      <td>25.00</td>
    </tr>
    <tr>
      <th>9</th>
      <td>24.00</td>
      <td>34.00</td>
      <td>90.00</td>
      <td>61.00</td>
      <td>...</td>
      <td>38.00</td>
      <td>92.00</td>
      <td>20.00</td>
      <td>22.00</td>
    </tr>
    <tr>
      <th>10</th>
      <td>15.00</td>
      <td>62.00</td>
      <td>43.00</td>
      <td>22.00</td>
      <td>...</td>
      <td>66.00</td>
      <td>29.00</td>
      <td>64.00</td>
      <td>19.00</td>
    </tr>
    <tr>
      <th>11</th>
      <td>95.00</td>
      <td>80.00</td>
      <td>83.00</td>
      <td>36.00</td>
      <td>...</td>
      <td>80.00</td>
      <td>69.00</td>
      <td>86.00</td>
      <td>63.00</td>
    </tr>
    <tr>
      <th>12</th>
      <td>9.00</td>
      <td>43.00</td>
      <td>100.00</td>
      <td>67.00</td>
      <td>...</td>
      <td>52.00</td>
      <td>57.00</td>
      <td>40.00</td>
      <td>58.00</td>
    </tr>
    <tr>
      <th>13</th>
      <td>16.00</td>
      <td>76.00</td>
      <td>69.00</td>
      <td>18.00</td>
      <td>...</td>
      <td>50.00</td>
      <td>59.00</td>
      <td>6.00</td>
      <td>23.00</td>
    </tr>
    <tr>
      <th>14</th>
      <td>74.00</td>
      <td>31.00</td>
      <td>38.00</td>
      <td>36.00</td>
      <td>...</td>
      <td>70.00</td>
      <td>51.00</td>
      <td>26.00</td>
      <td>44.00</td>
    </tr>
    <tr>
      <th>15</th>
      <td>25.00</td>
      <td>10.00</td>
      <td>45.00</td>
      <td>28.00</td>
      <td>...</td>
      <td>51.00</td>
      <td>28.00</td>
      <td>44.00</td>
      <td>46.00</td>
    </tr>
    <tr>
      <th>16</th>
      <td>99.00</td>
      <td>21.00</td>
      <td>33.00</td>
      <td>42.00</td>
      <td>...</td>
      <td>55.00</td>
      <td>10.00</td>
      <td>14.00</td>
      <td>59.00</td>
    </tr>
    <tr>
      <th>17</th>
      <td>88.00</td>
      <td>80.00</td>
      <td>55.00</td>
      <td>31.00</td>
      <td>...</td>
      <td>6.00</td>
      <td>32.00</td>
      <td>27.00</td>
      <td>34.00</td>
    </tr>
    <tr>
      <th>18</th>
      <td>53.00</td>
      <td>24.00</td>
      <td>35.00</td>
      <td>54.00</td>
      <td>...</td>
      <td>98.00</td>
      <td>220.00</td>
      <td>46.00</td>
      <td>55.00</td>
    </tr>
    <tr>
      <th>19</th>
      <td>29.00</td>
      <td>25.00</td>
      <td>19.00</td>
      <td>14.00</td>
      <td>...</td>
      <td>28.00</td>
      <td>85.00</td>
      <td>56.00</td>
      <td>21.00</td>
    </tr>
    <tr>
      <th>20</th>
      <td>53.00</td>
      <td>22.00</td>
      <td>63.00</td>
      <td>17.00</td>
      <td>...</td>
      <td>85.00</td>
      <td>7.00</td>
      <td>12.00</td>
      <td>15.00</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1.00</td>
      <td>55.00</td>
      <td>25.00</td>
      <td>42.00</td>
      <td>...</td>
      <td>44.00</td>
      <td>22.00</td>
      <td>16.00</td>
      <td>17.00</td>
    </tr>
    <tr>
      <th>22</th>
      <td>33.00</td>
      <td>10.00</td>
      <td>0.00</td>
      <td>42.00</td>
      <td>...</td>
      <td>5.00</td>
      <td>49.00</td>
      <td>2.00</td>
      <td>21.00</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>7.00</td>
      <td>0.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>6.00</td>
      <td>5.00</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
<p>24 rows × 152 columns</p>
</div>




```python
plt.figure(figsize = (20,14))
sns.heatmap(compras_dia_hora);
```


    
![png](static/notebooks/ecommerce/part3_files/part3_66_0.png)
    


## Entendiendo los clientes

Para analizar a nivel de cliente lo mejor es crear un dataframe de solo compradores con granularidad cliente y las variables que nos interesan.

Hay que tener cuidado con la función de agregación que usamos en cada una.


```python
clientes = df.loc[df.evento == 'purchase'].groupby(['usuario']).agg({'producto':'count',
                                                          'sesion':'nunique', 
                                                          'precio': 'mean',
                                                          'date': 'max'})

clientes
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
      <th>producto</th>
      <th>sesion</th>
      <th>precio</th>
      <th>date</th>
    </tr>
    <tr>
      <th>usuario</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>25392526</th>
      <td>3</td>
      <td>1</td>
      <td>7.38</td>
      <td>2019-12-18</td>
    </tr>
    <tr>
      <th>27756757</th>
      <td>1</td>
      <td>1</td>
      <td>20.63</td>
      <td>2020-01-27</td>
    </tr>
    <tr>
      <th>50748978</th>
      <td>9</td>
      <td>1</td>
      <td>1.11</td>
      <td>2019-12-14</td>
    </tr>
    <tr>
      <th>52747911</th>
      <td>3</td>
      <td>1</td>
      <td>7.67</td>
      <td>2019-10-10</td>
    </tr>
    <tr>
      <th>65241811</th>
      <td>5</td>
      <td>1</td>
      <td>8.36</td>
      <td>2019-11-11</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>621995551</th>
      <td>5</td>
      <td>1</td>
      <td>2.09</td>
      <td>2020-02-29</td>
    </tr>
    <tr>
      <th>622021687</th>
      <td>1</td>
      <td>1</td>
      <td>13.33</td>
      <td>2020-02-29</td>
    </tr>
    <tr>
      <th>622041514</th>
      <td>3</td>
      <td>1</td>
      <td>0.63</td>
      <td>2020-02-29</td>
    </tr>
    <tr>
      <th>622042698</th>
      <td>3</td>
      <td>1</td>
      <td>28.04</td>
      <td>2020-02-29</td>
    </tr>
    <tr>
      <th>622065819</th>
      <td>4</td>
      <td>1</td>
      <td>5.12</td>
      <td>2020-02-29</td>
    </tr>
  </tbody>
</table>
<p>11040 rows × 4 columns</p>
</div>



Renombramos


```python
clientes.columns = ['productos_tot_num','compras_tot_num','precio_medio_prod','ult_compra']
clientes
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
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>precio_medio_prod</th>
      <th>ult_compra</th>
    </tr>
    <tr>
      <th>usuario</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>25392526</th>
      <td>3</td>
      <td>1</td>
      <td>7.38</td>
      <td>2019-12-18</td>
    </tr>
    <tr>
      <th>27756757</th>
      <td>1</td>
      <td>1</td>
      <td>20.63</td>
      <td>2020-01-27</td>
    </tr>
    <tr>
      <th>50748978</th>
      <td>9</td>
      <td>1</td>
      <td>1.11</td>
      <td>2019-12-14</td>
    </tr>
    <tr>
      <th>52747911</th>
      <td>3</td>
      <td>1</td>
      <td>7.67</td>
      <td>2019-10-10</td>
    </tr>
    <tr>
      <th>65241811</th>
      <td>5</td>
      <td>1</td>
      <td>8.36</td>
      <td>2019-11-11</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>621995551</th>
      <td>5</td>
      <td>1</td>
      <td>2.09</td>
      <td>2020-02-29</td>
    </tr>
    <tr>
      <th>622021687</th>
      <td>1</td>
      <td>1</td>
      <td>13.33</td>
      <td>2020-02-29</td>
    </tr>
    <tr>
      <th>622041514</th>
      <td>3</td>
      <td>1</td>
      <td>0.63</td>
      <td>2020-02-29</td>
    </tr>
    <tr>
      <th>622042698</th>
      <td>3</td>
      <td>1</td>
      <td>28.04</td>
      <td>2020-02-29</td>
    </tr>
    <tr>
      <th>622065819</th>
      <td>4</td>
      <td>1</td>
      <td>5.12</td>
      <td>2020-02-29</td>
    </tr>
  </tbody>
</table>
<p>11040 rows × 4 columns</p>
</div>



Vamos a calcular variables adicionales.


```python
clientes['gasto_tot'] = clientes.productos_tot_num * clientes.precio_medio_prod
clientes['productos_por_compra'] = clientes.productos_tot_num / clientes.compras_tot_num
clientes
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
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>precio_medio_prod</th>
      <th>ult_compra</th>
      <th>gasto_tot</th>
      <th>productos_por_compra</th>
    </tr>
    <tr>
      <th>usuario</th>
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
      <th>25392526</th>
      <td>3</td>
      <td>1</td>
      <td>7.38</td>
      <td>2019-12-18</td>
      <td>22.14</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>27756757</th>
      <td>1</td>
      <td>1</td>
      <td>20.63</td>
      <td>2020-01-27</td>
      <td>20.63</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>50748978</th>
      <td>9</td>
      <td>1</td>
      <td>1.11</td>
      <td>2019-12-14</td>
      <td>10.01</td>
      <td>9.00</td>
    </tr>
    <tr>
      <th>52747911</th>
      <td>3</td>
      <td>1</td>
      <td>7.67</td>
      <td>2019-10-10</td>
      <td>23.02</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>65241811</th>
      <td>5</td>
      <td>1</td>
      <td>8.36</td>
      <td>2019-11-11</td>
      <td>41.79</td>
      <td>5.00</td>
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
      <th>621995551</th>
      <td>5</td>
      <td>1</td>
      <td>2.09</td>
      <td>2020-02-29</td>
      <td>10.46</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>622021687</th>
      <td>1</td>
      <td>1</td>
      <td>13.33</td>
      <td>2020-02-29</td>
      <td>13.33</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>622041514</th>
      <td>3</td>
      <td>1</td>
      <td>0.63</td>
      <td>2020-02-29</td>
      <td>1.90</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>622042698</th>
      <td>3</td>
      <td>1</td>
      <td>28.04</td>
      <td>2020-02-29</td>
      <td>84.13</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>622065819</th>
      <td>4</td>
      <td>1</td>
      <td>5.12</td>
      <td>2020-02-29</td>
      <td>20.48</td>
      <td>4.00</td>
    </tr>
  </tbody>
</table>
<p>11040 rows × 6 columns</p>
</div>



### ¿Cómo se distribuyen los clientes en cuanto a gasto?


```python
sns.histplot(data = clientes, x = 'gasto_tot', bins = 50)
plt.xlim([0,300]);
```


    
![png](static/notebooks/ecommerce/part3_files/part3_75_0.png)
    


La gran mayoría de los clientes han gastado menos de 50€ en el período.

### ¿Cómo se distribuyen los clientes en cuanto al número de compras?


```python
sns.countplot(data = clientes, x = 'compras_tot_num');
```


    
![png](static/notebooks/ecommerce/part3_files/part3_78_0.png)
    


**INSIGHT #3** La gran mayoría de los clientes sólo hace una compra.

Existe gran recorrido para mejorar este ratio mediante:

* email marketing con newletters y ofertas personalizadas

### ¿Cuántos productos compra un cliente de media en cada compra?


```python
clientes.productos_por_compra.describe()
```




    count          11040.00
    mean               7.79
    std                9.49
    min                1.00
    25%                3.00
    50%                5.00
    75%               10.00
    max              219.00
    Name: productos_por_compra, dtype: float64



**INSIGHT #4** La compra mediana incluye 5 productos.

Pero un 25% de los clientes compran más de 10 productos en la misma compra.

Existe gran recorrido para mejorar este ratio mediante:

* sistemas de recomendación en el momento de la compra

### ¿Qué clientes nos han generado más ingresos?


```python
clientes.nlargest(n = 10, columns = 'gasto_tot')
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
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>precio_medio_prod</th>
      <th>ult_compra</th>
      <th>gasto_tot</th>
      <th>productos_por_compra</th>
    </tr>
    <tr>
      <th>usuario</th>
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
      <th>573823111</th>
      <td>268</td>
      <td>2</td>
      <td>5.82</td>
      <td>2020-02-21</td>
      <td>1559.21</td>
      <td>134.00</td>
    </tr>
    <tr>
      <th>539751397</th>
      <td>236</td>
      <td>13</td>
      <td>6.16</td>
      <td>2020-02-19</td>
      <td>1453.37</td>
      <td>18.15</td>
    </tr>
    <tr>
      <th>556579890</th>
      <td>506</td>
      <td>4</td>
      <td>2.75</td>
      <td>2020-02-27</td>
      <td>1392.45</td>
      <td>126.50</td>
    </tr>
    <tr>
      <th>442763940</th>
      <td>195</td>
      <td>8</td>
      <td>6.37</td>
      <td>2019-12-23</td>
      <td>1241.53</td>
      <td>24.38</td>
    </tr>
    <tr>
      <th>561592095</th>
      <td>94</td>
      <td>3</td>
      <td>11.81</td>
      <td>2019-10-31</td>
      <td>1109.70</td>
      <td>31.33</td>
    </tr>
    <tr>
      <th>527739278</th>
      <td>244</td>
      <td>13</td>
      <td>4.39</td>
      <td>2020-02-16</td>
      <td>1071.00</td>
      <td>18.77</td>
    </tr>
    <tr>
      <th>527806771</th>
      <td>195</td>
      <td>13</td>
      <td>4.86</td>
      <td>2020-02-20</td>
      <td>948.01</td>
      <td>15.00</td>
    </tr>
    <tr>
      <th>430220205</th>
      <td>190</td>
      <td>6</td>
      <td>4.99</td>
      <td>2020-02-29</td>
      <td>947.30</td>
      <td>31.67</td>
    </tr>
    <tr>
      <th>491009486</th>
      <td>219</td>
      <td>1</td>
      <td>4.32</td>
      <td>2020-02-12</td>
      <td>946.20</td>
      <td>219.00</td>
    </tr>
    <tr>
      <th>520501669</th>
      <td>64</td>
      <td>11</td>
      <td>14.27</td>
      <td>2020-01-17</td>
      <td>913.01</td>
      <td>5.82</td>
    </tr>
  </tbody>
</table>
</div>



Para calcular calculamos el gasto total medio por cliente.


```python
clientes.gasto_tot.describe()
```




    count          11040.00
    mean              56.30
    std               81.73
    min                0.13
    25%               16.22
    50%               32.74
    75%               60.30
    max             1559.21
    Name: gasto_tot, dtype: float64



**INSIGHT #5** Existen clientes con gasto medio decenas de veces superior a la media.

Hay que fidelizar estos clientes mediante programas de fidelización.

### ¿Cual es la supervivencia de los clientes?

Dado que solo tenemos 5 meses de histórico vamos a crear análisis de cohortes a 3 meses vista, lo cual nos da para hacer 3 cohortes.

Preparamos un dataframe solo con compradores y con las variables usuario y mes.


```python
c = df.loc[df.evento == 'purchase', ['usuario','mes']]
c
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
      <th>mes</th>
    </tr>
    <tr>
      <th>fecha</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2019-10-01 00:26:49</th>
      <td>536128518</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2019-10-01 00:26:49</th>
      <td>536128518</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2019-10-01 00:26:49</th>
      <td>536128518</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2019-10-01 00:26:49</th>
      <td>536128518</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2019-10-01 00:26:49</th>
      <td>536128518</td>
      <td>10</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2020-02-29 22:29:19</th>
      <td>622065819</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2020-02-29 22:29:19</th>
      <td>622065819</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2020-02-29 22:29:19</th>
      <td>622065819</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2020-02-29 22:29:19</th>
      <td>622065819</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2020-02-29 23:26:42</th>
      <td>610361057</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>127564 rows × 2 columns</p>
</div>



Pasamos los meses a columnas.


```python
c = pd.crosstab(c.usuario,c.mes).reset_index()
c
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
      <th>mes</th>
      <th>usuario</th>
      <th>1</th>
      <th>2</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25392526</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>27756757</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>50748978</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>52747911</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>65241811</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
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
    </tr>
    <tr>
      <th>11035</th>
      <td>621995551</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11036</th>
      <td>622021687</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11037</th>
      <td>622041514</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11038</th>
      <td>622042698</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11039</th>
      <td>622065819</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>11040 rows × 6 columns</p>
</div>



Renombramos y eliminamos el usuario que ya no lo necesitamos.


```python
c.columns = ['usuario','c4','c5','c1','c2','c3']
c.drop(columns = 'usuario', inplace = True)
c
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
      <th>c4</th>
      <th>c5</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>11035</th>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11036</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11037</th>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11038</th>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11039</th>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>11040 rows × 5 columns</p>
</div>



La primera cohorte será la del mes 2, ya que queremos seleccionar "nuevos" clientes (al menos que no estuvieran el mes anterior)


```python
c2 = c.loc[(c.c1 == 0) & (c.c2 > 0)]
c2
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
      <th>c4</th>
      <th>c5</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>27</td>
      <td>17</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7702</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7703</th>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7705</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7708</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7709</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>2640 rows × 5 columns</p>
</div>



Pasamos a un dataframe binario ya que solo nos importa si ese cliente ha comprado o no en cada mes.


```python
def binarizar(variable):
    variable = variable.transform(lambda x: 1 if (x > 0) else 0)
    return(variable)
```


```python
c2_b = c2.apply(binarizar)
c2_b
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
      <th>c4</th>
      <th>c5</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7702</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7703</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7705</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7708</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7709</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>2640 rows × 5 columns</p>
</div>



Calcumamos el porcentaje de clientes de esta cohorte que han seguido comprando en los siguientes meses.


```python
c2_f = c2_b.sum() / c2_b.shape[0]
c2_f = c2_f.sort_index()
c2_f
```




    c1              0.00
    c2              1.00
    c3              0.10
    c4              0.10
    c5              0.08
    dtype: float64



Replicamos todo el proceso para la cohorte 3


```python
c3 = c.loc[(c.c2 == 0) & (c.c3 > 0)]
c3_b = c3.apply(binarizar)
c3_f = c3_b.sum() / c3_b.shape[0]
c3_f = c3_f.sort_index()
c3_f['c1'] = 0
c3_f
```




    c1              0.00
    c2              0.00
    c3              1.00
    c4              0.10
    c5              0.08
    dtype: float64



Replicamos todo el proceso para la cohorte 4


```python
c4 = c.loc[(c.c3 == 0) & (c.c4 > 0)]
c4_b = c4.apply(binarizar)
c4_f = c4_b.sum() / c4_b.shape[0]
c4_f = c4_f.sort_index()
c4_f['c1'] = 0
c4_f['c2'] = 0
c4_f
```




    c1              0.00
    c2              0.00
    c3              0.00
    c4              1.00
    c5              0.12
    dtype: float64



Creamos el dataframe de cohortes.


```python
cohortes = pd.DataFrame({'c2':c2_f,'c3':c3_f,'c4':c4_f})
cohortes
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
      <th>c2</th>
      <th>c3</th>
      <th>c4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>c1</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>c2</th>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>c3</th>
      <td>0.10</td>
      <td>1.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>c4</th>
      <td>0.10</td>
      <td>0.10</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>c5</th>
      <td>0.08</td>
      <td>0.08</td>
      <td>0.12</td>
    </tr>
  </tbody>
</table>
</div>




```python
cohortes = cohortes.drop(index = 'c1').T
cohortes
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
      <th>c2</th>
      <th>c3</th>
      <th>c4</th>
      <th>c5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>c2</th>
      <td>1.00</td>
      <td>0.10</td>
      <td>0.10</td>
      <td>0.08</td>
    </tr>
    <tr>
      <th>c3</th>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.10</td>
      <td>0.08</td>
    </tr>
    <tr>
      <th>c4</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.12</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize = (12,6))
sns.heatmap(cohortes,annot = True, fmt = '.0%', cmap='Greys');
```


    
![png](static/notebooks/ecommerce/part3_files/part3_110_0.png)
    


**INSIGHT #6**: El 90% de que los nuevos clientes no vuelve a comprar en los meses posteriores

### ¿Cual es el LTV de los clientes?

Teniendo en cuenta el 90% de que los nuevos clientes no vuelve a comprar en los meses posteriores podemos calcular el LTV con el histórico que tenemos sin miedo a equivocarnos mucho.

Para ello vamos a coger a los clientes de la cohorte 2 y calcular el total de sus compras.


```python
maestro_ltv = df.loc[(df.evento == 'purchase') & (df.mes != 10) & (df.mes == 11),'usuario'].to_list()
maestro_ltv
```




    [549319657,
     549319657,
     549319657,
     549319657,
     ...
     ...
     510126861,
     510126861,
     510126861,
     440684807,
     ...]




```python
clientes_ltv = clientes.loc[clientes.index.isin(maestro_ltv)]
clientes_ltv
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
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>precio_medio_prod</th>
      <th>ult_compra</th>
      <th>gasto_tot</th>
      <th>productos_por_compra</th>
    </tr>
    <tr>
      <th>usuario</th>
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
      <th>65241811</th>
      <td>5</td>
      <td>1</td>
      <td>8.36</td>
      <td>2019-11-11</td>
      <td>41.79</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>80577370</th>
      <td>10</td>
      <td>2</td>
      <td>10.62</td>
      <td>2019-11-29</td>
      <td>106.24</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>88211255</th>
      <td>22</td>
      <td>4</td>
      <td>4.86</td>
      <td>2020-02-25</td>
      <td>106.87</td>
      <td>5.50</td>
    </tr>
    <tr>
      <th>93279832</th>
      <td>44</td>
      <td>2</td>
      <td>3.19</td>
      <td>2019-12-19</td>
      <td>140.51</td>
      <td>22.00</td>
    </tr>
    <tr>
      <th>94390236</th>
      <td>3</td>
      <td>1</td>
      <td>9.73</td>
      <td>2019-11-07</td>
      <td>29.20</td>
      <td>3.00</td>
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
      <th>579798049</th>
      <td>5</td>
      <td>1</td>
      <td>2.10</td>
      <td>2019-11-30</td>
      <td>10.52</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>579813390</th>
      <td>7</td>
      <td>2</td>
      <td>2.98</td>
      <td>2020-02-04</td>
      <td>20.83</td>
      <td>3.50</td>
    </tr>
    <tr>
      <th>579834429</th>
      <td>1</td>
      <td>1</td>
      <td>27.14</td>
      <td>2019-11-30</td>
      <td>27.14</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>579900887</th>
      <td>11</td>
      <td>2</td>
      <td>5.67</td>
      <td>2019-12-02</td>
      <td>62.34</td>
      <td>5.50</td>
    </tr>
    <tr>
      <th>579903865</th>
      <td>1</td>
      <td>1</td>
      <td>8.43</td>
      <td>2019-11-30</td>
      <td>8.43</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
<p>3105 rows × 6 columns</p>
</div>




```python
clientes_ltv.gasto_tot.describe()
```




    count           3105.00
    mean              79.62
    std              113.62
    min                0.13
    25%               20.29
    50%               41.49
    75%               90.00
    max             1453.37
    Name: gasto_tot, dtype: float64



Dada la variabilidad de la media sería más seguro coger la mediana.

**INSIGHT #7**: El LTV medio es de 42€.

Aplicando nuestro margen sobre esa cifra y el % que queremos dedicar a captación nos sale el importe máximo a invertir en CPA.

Aplicar las acciones de CRO permitirá incrementar el LTV y por tanto también el CPA, siendo una ventaja estratégica muy importante.

### ¿Sobre qué clientes ejecutar las próximas campañas (RFM)?

Vamos a aprender una técnica llamada RFM (Recency - Frequency - Monetary).

Esta técnica es muy potente para contextos de retail y por tanto también en ecommerce.

Permite dar respuesta a necesidades como:

* Cuál es la proporción de clientes que realizan un solo pedido y clientes frecuentes
* Cuales son los clientes VIP (que potencialmente necesitan programas de fidelización y atención personalizada)
* Cuál es la cantidad de clientes nuevos (a incentivar para que vuelvan a realizar un pedido)
* Cuántos y cuáles son los clientes que no realizan compras hace tiempo
* Cuántos y cuáles son los clientes en los cuales no vale la pena invertir más tiempo y recursos
* Etc

Pese a su potencia es muy sencilla de construir, por tanto es casi obligatoria en este tipo de análisis.

Lo primero es identificar las variables con las que crear cada una de las dimensiones:

* Recency: ult_compra
* Frequency: compras_tot_num
* Monetary: gasto_tot

Y discretizar cada una de ellas.

Vamos a dejar la recencia para el final porque requerirá una transformación previa.

Comenzamos por Frequency


```python
clientes['F'] = clientes.compras_tot_num.transform(lambda x: pd.cut(x,5, labels = False)) + 1
clientes
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
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>precio_medio_prod</th>
      <th>ult_compra</th>
      <th>gasto_tot</th>
      <th>productos_por_compra</th>
      <th>F</th>
    </tr>
    <tr>
      <th>usuario</th>
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
      <th>25392526</th>
      <td>3</td>
      <td>1</td>
      <td>7.38</td>
      <td>2019-12-18</td>
      <td>22.14</td>
      <td>3.00</td>
      <td>1</td>
    </tr>
    <tr>
      <th>27756757</th>
      <td>1</td>
      <td>1</td>
      <td>20.63</td>
      <td>2020-01-27</td>
      <td>20.63</td>
      <td>1.00</td>
      <td>1</td>
    </tr>
    <tr>
      <th>50748978</th>
      <td>9</td>
      <td>1</td>
      <td>1.11</td>
      <td>2019-12-14</td>
      <td>10.01</td>
      <td>9.00</td>
      <td>1</td>
    </tr>
    <tr>
      <th>52747911</th>
      <td>3</td>
      <td>1</td>
      <td>7.67</td>
      <td>2019-10-10</td>
      <td>23.02</td>
      <td>3.00</td>
      <td>1</td>
    </tr>
    <tr>
      <th>65241811</th>
      <td>5</td>
      <td>1</td>
      <td>8.36</td>
      <td>2019-11-11</td>
      <td>41.79</td>
      <td>5.00</td>
      <td>1</td>
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
      <th>621995551</th>
      <td>5</td>
      <td>1</td>
      <td>2.09</td>
      <td>2020-02-29</td>
      <td>10.46</td>
      <td>5.00</td>
      <td>1</td>
    </tr>
    <tr>
      <th>622021687</th>
      <td>1</td>
      <td>1</td>
      <td>13.33</td>
      <td>2020-02-29</td>
      <td>13.33</td>
      <td>1.00</td>
      <td>1</td>
    </tr>
    <tr>
      <th>622041514</th>
      <td>3</td>
      <td>1</td>
      <td>0.63</td>
      <td>2020-02-29</td>
      <td>1.90</td>
      <td>3.00</td>
      <td>1</td>
    </tr>
    <tr>
      <th>622042698</th>
      <td>3</td>
      <td>1</td>
      <td>28.04</td>
      <td>2020-02-29</td>
      <td>84.13</td>
      <td>3.00</td>
      <td>1</td>
    </tr>
    <tr>
      <th>622065819</th>
      <td>4</td>
      <td>1</td>
      <td>5.12</td>
      <td>2020-02-29</td>
      <td>20.48</td>
      <td>4.00</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>11040 rows × 7 columns</p>
</div>



Comprobamos


```python
clientes.groupby('F').compras_tot_num.mean()
```




    F
    1              1.31
    2              7.06
    3             12.00
    4             16.50
    5             23.50
    Name: compras_tot_num, dtype: float64



Ahora Monetary


```python
clientes['M'] = clientes.gasto_tot.transform(lambda x: pd.cut(x,5, labels = False)) + 1
clientes.groupby('M').gasto_tot.mean()
```




    M
    1             48.36
    2            410.98
    3            765.18
    4           1043.96
    5           1468.34
    Name: gasto_tot, dtype: float64



Para la recencia tenemos que transformar la fecha a un número, por ejemplo la distancia en días de cada fecha a la fecha más reciente disponible.


```python
mas_reciente = clientes.ult_compra.max()

clientes['ult_compra_dias'] = clientes.ult_compra.transform(lambda x: mas_reciente - x)

clientes
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
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>precio_medio_prod</th>
      <th>ult_compra</th>
      <th>...</th>
      <th>productos_por_compra</th>
      <th>F</th>
      <th>M</th>
      <th>ult_compra_dias</th>
    </tr>
    <tr>
      <th>usuario</th>
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
      <th>25392526</th>
      <td>3</td>
      <td>1</td>
      <td>7.38</td>
      <td>2019-12-18</td>
      <td>...</td>
      <td>3.00</td>
      <td>1</td>
      <td>1</td>
      <td>73 days</td>
    </tr>
    <tr>
      <th>27756757</th>
      <td>1</td>
      <td>1</td>
      <td>20.63</td>
      <td>2020-01-27</td>
      <td>...</td>
      <td>1.00</td>
      <td>1</td>
      <td>1</td>
      <td>33 days</td>
    </tr>
    <tr>
      <th>50748978</th>
      <td>9</td>
      <td>1</td>
      <td>1.11</td>
      <td>2019-12-14</td>
      <td>...</td>
      <td>9.00</td>
      <td>1</td>
      <td>1</td>
      <td>77 days</td>
    </tr>
    <tr>
      <th>52747911</th>
      <td>3</td>
      <td>1</td>
      <td>7.67</td>
      <td>2019-10-10</td>
      <td>...</td>
      <td>3.00</td>
      <td>1</td>
      <td>1</td>
      <td>142 days</td>
    </tr>
    <tr>
      <th>65241811</th>
      <td>5</td>
      <td>1</td>
      <td>8.36</td>
      <td>2019-11-11</td>
      <td>...</td>
      <td>5.00</td>
      <td>1</td>
      <td>1</td>
      <td>110 days</td>
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
      <th>621995551</th>
      <td>5</td>
      <td>1</td>
      <td>2.09</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>5.00</td>
      <td>1</td>
      <td>1</td>
      <td>0 days</td>
    </tr>
    <tr>
      <th>622021687</th>
      <td>1</td>
      <td>1</td>
      <td>13.33</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>1.00</td>
      <td>1</td>
      <td>1</td>
      <td>0 days</td>
    </tr>
    <tr>
      <th>622041514</th>
      <td>3</td>
      <td>1</td>
      <td>0.63</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>3.00</td>
      <td>1</td>
      <td>1</td>
      <td>0 days</td>
    </tr>
    <tr>
      <th>622042698</th>
      <td>3</td>
      <td>1</td>
      <td>28.04</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>3.00</td>
      <td>1</td>
      <td>1</td>
      <td>0 days</td>
    </tr>
    <tr>
      <th>622065819</th>
      <td>4</td>
      <td>1</td>
      <td>5.12</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>4.00</td>
      <td>1</td>
      <td>1</td>
      <td>0 days</td>
    </tr>
  </tbody>
</table>
<p>11040 rows × 9 columns</p>
</div>



Nos ha creado un timedelta, tenemos que pasarlo a número de días.


```python
clientes['ult_compra_dias'] = clientes.ult_compra_dias.dt.days
clientes
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
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>precio_medio_prod</th>
      <th>ult_compra</th>
      <th>...</th>
      <th>productos_por_compra</th>
      <th>F</th>
      <th>M</th>
      <th>ult_compra_dias</th>
    </tr>
    <tr>
      <th>usuario</th>
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
      <th>25392526</th>
      <td>3</td>
      <td>1</td>
      <td>7.38</td>
      <td>2019-12-18</td>
      <td>...</td>
      <td>3.00</td>
      <td>1</td>
      <td>1</td>
      <td>73</td>
    </tr>
    <tr>
      <th>27756757</th>
      <td>1</td>
      <td>1</td>
      <td>20.63</td>
      <td>2020-01-27</td>
      <td>...</td>
      <td>1.00</td>
      <td>1</td>
      <td>1</td>
      <td>33</td>
    </tr>
    <tr>
      <th>50748978</th>
      <td>9</td>
      <td>1</td>
      <td>1.11</td>
      <td>2019-12-14</td>
      <td>...</td>
      <td>9.00</td>
      <td>1</td>
      <td>1</td>
      <td>77</td>
    </tr>
    <tr>
      <th>52747911</th>
      <td>3</td>
      <td>1</td>
      <td>7.67</td>
      <td>2019-10-10</td>
      <td>...</td>
      <td>3.00</td>
      <td>1</td>
      <td>1</td>
      <td>142</td>
    </tr>
    <tr>
      <th>65241811</th>
      <td>5</td>
      <td>1</td>
      <td>8.36</td>
      <td>2019-11-11</td>
      <td>...</td>
      <td>5.00</td>
      <td>1</td>
      <td>1</td>
      <td>110</td>
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
      <th>621995551</th>
      <td>5</td>
      <td>1</td>
      <td>2.09</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>5.00</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>622021687</th>
      <td>1</td>
      <td>1</td>
      <td>13.33</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>1.00</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>622041514</th>
      <td>3</td>
      <td>1</td>
      <td>0.63</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>3.00</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>622042698</th>
      <td>3</td>
      <td>1</td>
      <td>28.04</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>3.00</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>622065819</th>
      <td>4</td>
      <td>1</td>
      <td>5.12</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>4.00</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>11040 rows × 9 columns</p>
</div>



Ya podemos crear la R, pero hay que tener en cuenta que en este caso lo mejor son los valores más bajos.


```python
clientes['R'] = clientes.ult_compra_dias.transform(lambda x: pd.cut(x,5, labels = False)) + 1
clientes.groupby('R').ult_compra_dias.mean()
```




    R
    1             14.62
    2             43.04
    3             75.94
    4            103.85
    5            135.91
    Name: ult_compra_dias, dtype: float64



Para estandarizar su intrepretación con el resto de las dimensiones vamos a darle la vuelta.


```python
clientes['R'] = 6 - clientes.R
clientes.groupby('R').ult_compra_dias.mean()
```




    R
    1            135.91
    2            103.85
    3             75.94
    4             43.04
    5             14.62
    Name: ult_compra_dias, dtype: float64



Integramos en un dataframe rfm.


```python
clientes
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
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>precio_medio_prod</th>
      <th>ult_compra</th>
      <th>...</th>
      <th>F</th>
      <th>M</th>
      <th>ult_compra_dias</th>
      <th>R</th>
    </tr>
    <tr>
      <th>usuario</th>
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
      <th>25392526</th>
      <td>3</td>
      <td>1</td>
      <td>7.38</td>
      <td>2019-12-18</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>73</td>
      <td>3</td>
    </tr>
    <tr>
      <th>27756757</th>
      <td>1</td>
      <td>1</td>
      <td>20.63</td>
      <td>2020-01-27</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>33</td>
      <td>4</td>
    </tr>
    <tr>
      <th>50748978</th>
      <td>9</td>
      <td>1</td>
      <td>1.11</td>
      <td>2019-12-14</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>77</td>
      <td>3</td>
    </tr>
    <tr>
      <th>52747911</th>
      <td>3</td>
      <td>1</td>
      <td>7.67</td>
      <td>2019-10-10</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>142</td>
      <td>1</td>
    </tr>
    <tr>
      <th>65241811</th>
      <td>5</td>
      <td>1</td>
      <td>8.36</td>
      <td>2019-11-11</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>110</td>
      <td>2</td>
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
      <th>621995551</th>
      <td>5</td>
      <td>1</td>
      <td>2.09</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>622021687</th>
      <td>1</td>
      <td>1</td>
      <td>13.33</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>622041514</th>
      <td>3</td>
      <td>1</td>
      <td>0.63</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>622042698</th>
      <td>3</td>
      <td>1</td>
      <td>28.04</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>622065819</th>
      <td>4</td>
      <td>1</td>
      <td>5.12</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
<p>11040 rows × 10 columns</p>
</div>



Creamos variables adicionales.


```python
clientes['valor'] = clientes.R + clientes.F + clientes.M
clientes['RFM'] = clientes.apply(lambda x: str(x.R) + str(x.F) + str(x.M), axis = 1)
clientes
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
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>precio_medio_prod</th>
      <th>ult_compra</th>
      <th>...</th>
      <th>ult_compra_dias</th>
      <th>R</th>
      <th>valor</th>
      <th>RFM</th>
    </tr>
    <tr>
      <th>usuario</th>
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
      <th>25392526</th>
      <td>3</td>
      <td>1</td>
      <td>7.38</td>
      <td>2019-12-18</td>
      <td>...</td>
      <td>73</td>
      <td>3</td>
      <td>5</td>
      <td>311</td>
    </tr>
    <tr>
      <th>27756757</th>
      <td>1</td>
      <td>1</td>
      <td>20.63</td>
      <td>2020-01-27</td>
      <td>...</td>
      <td>33</td>
      <td>4</td>
      <td>6</td>
      <td>411</td>
    </tr>
    <tr>
      <th>50748978</th>
      <td>9</td>
      <td>1</td>
      <td>1.11</td>
      <td>2019-12-14</td>
      <td>...</td>
      <td>77</td>
      <td>3</td>
      <td>5</td>
      <td>311</td>
    </tr>
    <tr>
      <th>52747911</th>
      <td>3</td>
      <td>1</td>
      <td>7.67</td>
      <td>2019-10-10</td>
      <td>...</td>
      <td>142</td>
      <td>1</td>
      <td>3</td>
      <td>111</td>
    </tr>
    <tr>
      <th>65241811</th>
      <td>5</td>
      <td>1</td>
      <td>8.36</td>
      <td>2019-11-11</td>
      <td>...</td>
      <td>110</td>
      <td>2</td>
      <td>4</td>
      <td>211</td>
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
      <th>621995551</th>
      <td>5</td>
      <td>1</td>
      <td>2.09</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>0</td>
      <td>5</td>
      <td>7</td>
      <td>511</td>
    </tr>
    <tr>
      <th>622021687</th>
      <td>1</td>
      <td>1</td>
      <td>13.33</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>0</td>
      <td>5</td>
      <td>7</td>
      <td>511</td>
    </tr>
    <tr>
      <th>622041514</th>
      <td>3</td>
      <td>1</td>
      <td>0.63</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>0</td>
      <td>5</td>
      <td>7</td>
      <td>511</td>
    </tr>
    <tr>
      <th>622042698</th>
      <td>3</td>
      <td>1</td>
      <td>28.04</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>0</td>
      <td>5</td>
      <td>7</td>
      <td>511</td>
    </tr>
    <tr>
      <th>622065819</th>
      <td>4</td>
      <td>1</td>
      <td>5.12</td>
      <td>2020-02-29</td>
      <td>...</td>
      <td>0</td>
      <td>5</td>
      <td>7</td>
      <td>511</td>
    </tr>
  </tbody>
</table>
<p>11040 rows × 12 columns</p>
</div>



Sobre este dataframe ya podemos hacer infinidad de análisis.

Por ejemplo combinándolo con la técnica del minicubo podemos obtener todo tipo de insights.


```python
#Paso 1: Seleccionar qué variables serán la métricas y cuales las dimensiones
metricas = ['productos_tot_num','compras_tot_num','gasto_tot']
dimensiones = ['R','F','M','RFM','valor']

minicubo = clientes[dimensiones + metricas]
minicubo
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
      <th>R</th>
      <th>F</th>
      <th>M</th>
      <th>RFM</th>
      <th>valor</th>
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>gasto_tot</th>
    </tr>
    <tr>
      <th>usuario</th>
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
      <th>25392526</th>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>311</td>
      <td>5</td>
      <td>3</td>
      <td>1</td>
      <td>22.14</td>
    </tr>
    <tr>
      <th>27756757</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>411</td>
      <td>6</td>
      <td>1</td>
      <td>1</td>
      <td>20.63</td>
    </tr>
    <tr>
      <th>50748978</th>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>311</td>
      <td>5</td>
      <td>9</td>
      <td>1</td>
      <td>10.01</td>
    </tr>
    <tr>
      <th>52747911</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>111</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>23.02</td>
    </tr>
    <tr>
      <th>65241811</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>211</td>
      <td>4</td>
      <td>5</td>
      <td>1</td>
      <td>41.79</td>
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
      <th>621995551</th>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>511</td>
      <td>7</td>
      <td>5</td>
      <td>1</td>
      <td>10.46</td>
    </tr>
    <tr>
      <th>622021687</th>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>511</td>
      <td>7</td>
      <td>1</td>
      <td>1</td>
      <td>13.33</td>
    </tr>
    <tr>
      <th>622041514</th>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>511</td>
      <td>7</td>
      <td>3</td>
      <td>1</td>
      <td>1.90</td>
    </tr>
    <tr>
      <th>622042698</th>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>511</td>
      <td>7</td>
      <td>3</td>
      <td>1</td>
      <td>84.13</td>
    </tr>
    <tr>
      <th>622065819</th>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>511</td>
      <td>7</td>
      <td>4</td>
      <td>1</td>
      <td>20.48</td>
    </tr>
  </tbody>
</table>
<p>11040 rows × 8 columns</p>
</div>




```python
#Paso 2: pasar a transaccional las dimensiones
minicubo = minicubo.melt(id_vars = metricas)
minicubo
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
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>gasto_tot</th>
      <th>variable</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>1</td>
      <td>22.14</td>
      <td>R</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>20.63</td>
      <td>R</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>1</td>
      <td>10.01</td>
      <td>R</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1</td>
      <td>23.02</td>
      <td>R</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1</td>
      <td>41.79</td>
      <td>R</td>
      <td>2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>55195</th>
      <td>5</td>
      <td>1</td>
      <td>10.46</td>
      <td>valor</td>
      <td>7</td>
    </tr>
    <tr>
      <th>55196</th>
      <td>1</td>
      <td>1</td>
      <td>13.33</td>
      <td>valor</td>
      <td>7</td>
    </tr>
    <tr>
      <th>55197</th>
      <td>3</td>
      <td>1</td>
      <td>1.90</td>
      <td>valor</td>
      <td>7</td>
    </tr>
    <tr>
      <th>55198</th>
      <td>3</td>
      <td>1</td>
      <td>84.13</td>
      <td>valor</td>
      <td>7</td>
    </tr>
    <tr>
      <th>55199</th>
      <td>4</td>
      <td>1</td>
      <td>20.48</td>
      <td>valor</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
<p>55200 rows × 5 columns</p>
</div>




```python
#Paso 3: Agregar las métricas por "variable" y "valor" con las funciones deseadas
minicubo = minicubo.groupby(['variable','value'], as_index = False)[metricas].mean()
minicubo
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
      <th>variable</th>
      <th>value</th>
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>gasto_tot</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>1</td>
      <td>10.61</td>
      <td>1.31</td>
      <td>52.09</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>2</td>
      <td>71.42</td>
      <td>7.06</td>
      <td>320.47</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>3</td>
      <td>123.64</td>
      <td>12.00</td>
      <td>643.20</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>4</td>
      <td>156.75</td>
      <td>16.50</td>
      <td>560.15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>F</td>
      <td>5</td>
      <td>124.00</td>
      <td>23.50</td>
      <td>652.42</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>58</th>
      <td>valor</td>
      <td>9</td>
      <td>98.02</td>
      <td>7.25</td>
      <td>491.71</td>
    </tr>
    <tr>
      <th>59</th>
      <td>valor</td>
      <td>10</td>
      <td>140.89</td>
      <td>10.22</td>
      <td>625.93</td>
    </tr>
    <tr>
      <th>60</th>
      <td>valor</td>
      <td>11</td>
      <td>291.00</td>
      <td>5.75</td>
      <td>1189.31</td>
    </tr>
    <tr>
      <th>61</th>
      <td>valor</td>
      <td>12</td>
      <td>189.80</td>
      <td>16.60</td>
      <td>833.43</td>
    </tr>
    <tr>
      <th>62</th>
      <td>valor</td>
      <td>13</td>
      <td>179.00</td>
      <td>18.00</td>
      <td>1136.70</td>
    </tr>
  </tbody>
</table>
<p>63 rows × 5 columns</p>
</div>



Para analizar cada dimensión la seleccionamos.


```python
minicubo[minicubo.variable == 'F']
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
      <th>variable</th>
      <th>value</th>
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>gasto_tot</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>1</td>
      <td>10.61</td>
      <td>1.31</td>
      <td>52.09</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>2</td>
      <td>71.42</td>
      <td>7.06</td>
      <td>320.47</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>3</td>
      <td>123.64</td>
      <td>12.00</td>
      <td>643.20</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>4</td>
      <td>156.75</td>
      <td>16.50</td>
      <td>560.15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>F</td>
      <td>5</td>
      <td>124.00</td>
      <td>23.50</td>
      <td>652.42</td>
    </tr>
  </tbody>
</table>
</div>



Y la analizamos de forma gráfica.


```python
minicubo[minicubo.variable == 'F'].set_index('value').plot.bar(subplots = True, sharex = False, figsize = (12,12))
plt.tight_layout();
```

    c:\Users\sgarciam\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\indexes\base.py:6982: FutureWarning:
    
    In a future version, the Index constructor will not infer numeric dtypes when passed object-dtype sequences (matching Series behavior)
    
    


    
![png](static/notebooks/ecommerce/part3_files/part3_144_1.png)
    



```python
minicubo[minicubo.variable == 'R']
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
      <th>variable</th>
      <th>value</th>
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>gasto_tot</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>R</td>
      <td>1</td>
      <td>8.15</td>
      <td>1.08</td>
      <td>41.56</td>
    </tr>
    <tr>
      <th>11</th>
      <td>R</td>
      <td>2</td>
      <td>9.25</td>
      <td>1.18</td>
      <td>45.58</td>
    </tr>
    <tr>
      <th>12</th>
      <td>R</td>
      <td>3</td>
      <td>9.54</td>
      <td>1.29</td>
      <td>47.25</td>
    </tr>
    <tr>
      <th>13</th>
      <td>R</td>
      <td>4</td>
      <td>11.72</td>
      <td>1.44</td>
      <td>58.19</td>
    </tr>
    <tr>
      <th>14</th>
      <td>R</td>
      <td>5</td>
      <td>16.83</td>
      <td>1.82</td>
      <td>79.04</td>
    </tr>
  </tbody>
</table>
</div>




```python
minicubo[minicubo.variable == 'R'].set_index('value').plot.bar(subplots = True, sharex = False, figsize = (12,12))
plt.tight_layout();
```

    c:\Users\sgarciam\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\indexes\base.py:6982: FutureWarning:
    
    In a future version, the Index constructor will not infer numeric dtypes when passed object-dtype sequences (matching Series behavior)
    
    


    
![png](static/notebooks/ecommerce/part3_files/part3_146_1.png)
    



```python
minicubo[minicubo.variable == 'M']
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
      <th>variable</th>
      <th>value</th>
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>gasto_tot</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>M</td>
      <td>1</td>
      <td>10.12</td>
      <td>1.34</td>
      <td>48.36</td>
    </tr>
    <tr>
      <th>6</th>
      <td>M</td>
      <td>2</td>
      <td>74.28</td>
      <td>4.31</td>
      <td>410.98</td>
    </tr>
    <tr>
      <th>7</th>
      <td>M</td>
      <td>3</td>
      <td>138.50</td>
      <td>6.86</td>
      <td>765.18</td>
    </tr>
    <tr>
      <th>8</th>
      <td>M</td>
      <td>4</td>
      <td>189.50</td>
      <td>7.33</td>
      <td>1043.96</td>
    </tr>
    <tr>
      <th>9</th>
      <td>M</td>
      <td>5</td>
      <td>336.67</td>
      <td>6.33</td>
      <td>1468.34</td>
    </tr>
  </tbody>
</table>
</div>




```python
minicubo[minicubo.variable == 'M'].set_index('value').plot.bar(subplots = True, sharex = False, figsize = (12,12))
plt.tight_layout();
```

    c:\Users\sgarciam\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\indexes\base.py:6982: FutureWarning:
    
    In a future version, the Index constructor will not infer numeric dtypes when passed object-dtype sequences (matching Series behavior)
    
    


    
![png](static/notebooks/ecommerce/part3_files/part3_148_1.png)
    



```python
minicubo[minicubo.variable == 'RFM']
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
      <th>variable</th>
      <th>value</th>
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>gasto_tot</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15</th>
      <td>RFM</td>
      <td>111</td>
      <td>7.97</td>
      <td>1.08</td>
      <td>39.28</td>
    </tr>
    <tr>
      <th>16</th>
      <td>RFM</td>
      <td>112</td>
      <td>37.38</td>
      <td>1.50</td>
      <td>397.98</td>
    </tr>
    <tr>
      <th>17</th>
      <td>RFM</td>
      <td>114</td>
      <td>94.00</td>
      <td>3.00</td>
      <td>1109.70</td>
    </tr>
    <tr>
      <th>18</th>
      <td>RFM</td>
      <td>211</td>
      <td>8.94</td>
      <td>1.17</td>
      <td>43.16</td>
    </tr>
    <tr>
      <th>19</th>
      <td>RFM</td>
      <td>212</td>
      <td>47.00</td>
      <td>1.73</td>
      <td>391.14</td>
    </tr>
    <tr>
      <th>20</th>
      <td>RFM</td>
      <td>213</td>
      <td>35.50</td>
      <td>1.00</td>
      <td>662.84</td>
    </tr>
    <tr>
      <th>21</th>
      <td>RFM</td>
      <td>221</td>
      <td>85.67</td>
      <td>6.33</td>
      <td>194.48</td>
    </tr>
    <tr>
      <th>22</th>
      <td>RFM</td>
      <td>311</td>
      <td>8.98</td>
      <td>1.26</td>
      <td>43.91</td>
    </tr>
    <tr>
      <th>23</th>
      <td>RFM</td>
      <td>312</td>
      <td>53.46</td>
      <td>2.46</td>
      <td>376.38</td>
    </tr>
    <tr>
      <th>24</th>
      <td>RFM</td>
      <td>321</td>
      <td>39.00</td>
      <td>6.50</td>
      <td>141.28</td>
    </tr>
    <tr>
      <th>25</th>
      <td>RFM</td>
      <td>322</td>
      <td>121.00</td>
      <td>6.50</td>
      <td>389.19</td>
    </tr>
    <tr>
      <th>26</th>
      <td>RFM</td>
      <td>324</td>
      <td>195.00</td>
      <td>8.00</td>
      <td>1241.53</td>
    </tr>
    <tr>
      <th>27</th>
      <td>RFM</td>
      <td>411</td>
      <td>10.37</td>
      <td>1.36</td>
      <td>49.99</td>
    </tr>
    <tr>
      <th>28</th>
      <td>RFM</td>
      <td>412</td>
      <td>60.69</td>
      <td>2.54</td>
      <td>404.22</td>
    </tr>
    <tr>
      <th>29</th>
      <td>RFM</td>
      <td>413</td>
      <td>130.50</td>
      <td>2.50</td>
      <td>868.30</td>
    </tr>
    <tr>
      <th>30</th>
      <td>RFM</td>
      <td>421</td>
      <td>41.00</td>
      <td>6.92</td>
      <td>205.31</td>
    </tr>
    <tr>
      <th>31</th>
      <td>RFM</td>
      <td>422</td>
      <td>92.88</td>
      <td>7.12</td>
      <td>440.47</td>
    </tr>
    <tr>
      <th>32</th>
      <td>RFM</td>
      <td>423</td>
      <td>153.33</td>
      <td>7.33</td>
      <td>672.97</td>
    </tr>
    <tr>
      <th>33</th>
      <td>RFM</td>
      <td>433</td>
      <td>64.00</td>
      <td>11.00</td>
      <td>913.01</td>
    </tr>
    <tr>
      <th>34</th>
      <td>RFM</td>
      <td>511</td>
      <td>11.94</td>
      <td>1.50</td>
      <td>56.07</td>
    </tr>
    <tr>
      <th>35</th>
      <td>RFM</td>
      <td>512</td>
      <td>78.79</td>
      <td>3.05</td>
      <td>399.18</td>
    </tr>
    <tr>
      <th>36</th>
      <td>RFM</td>
      <td>513</td>
      <td>133.00</td>
      <td>3.14</td>
      <td>742.48</td>
    </tr>
    <tr>
      <th>37</th>
      <td>RFM</td>
      <td>514</td>
      <td>219.00</td>
      <td>1.00</td>
      <td>946.20</td>
    </tr>
    <tr>
      <th>38</th>
      <td>RFM</td>
      <td>515</td>
      <td>387.00</td>
      <td>3.00</td>
      <td>1475.83</td>
    </tr>
    <tr>
      <th>39</th>
      <td>RFM</td>
      <td>521</td>
      <td>47.88</td>
      <td>6.83</td>
      <td>192.19</td>
    </tr>
    <tr>
      <th>40</th>
      <td>RFM</td>
      <td>522</td>
      <td>89.51</td>
      <td>7.51</td>
      <td>442.50</td>
    </tr>
    <tr>
      <th>41</th>
      <td>RFM</td>
      <td>523</td>
      <td>184.67</td>
      <td>7.33</td>
      <td>766.90</td>
    </tr>
    <tr>
      <th>42</th>
      <td>RFM</td>
      <td>524</td>
      <td>190.00</td>
      <td>6.00</td>
      <td>947.30</td>
    </tr>
    <tr>
      <th>43</th>
      <td>RFM</td>
      <td>531</td>
      <td>58.25</td>
      <td>11.50</td>
      <td>233.84</td>
    </tr>
    <tr>
      <th>44</th>
      <td>RFM</td>
      <td>532</td>
      <td>94.00</td>
      <td>12.50</td>
      <td>448.09</td>
    </tr>
    <tr>
      <th>45</th>
      <td>RFM</td>
      <td>533</td>
      <td>200.00</td>
      <td>11.00</td>
      <td>858.26</td>
    </tr>
    <tr>
      <th>46</th>
      <td>RFM</td>
      <td>534</td>
      <td>219.50</td>
      <td>13.00</td>
      <td>1009.51</td>
    </tr>
    <tr>
      <th>47</th>
      <td>RFM</td>
      <td>535</td>
      <td>236.00</td>
      <td>13.00</td>
      <td>1453.37</td>
    </tr>
    <tr>
      <th>48</th>
      <td>RFM</td>
      <td>541</td>
      <td>121.50</td>
      <td>16.50</td>
      <td>288.65</td>
    </tr>
    <tr>
      <th>49</th>
      <td>RFM</td>
      <td>543</td>
      <td>192.00</td>
      <td>16.50</td>
      <td>831.65</td>
    </tr>
    <tr>
      <th>50</th>
      <td>RFM</td>
      <td>552</td>
      <td>126.00</td>
      <td>24.00</td>
      <td>484.81</td>
    </tr>
    <tr>
      <th>51</th>
      <td>RFM</td>
      <td>553</td>
      <td>122.00</td>
      <td>23.00</td>
      <td>820.04</td>
    </tr>
  </tbody>
</table>
</div>




```python
minicubo[minicubo.variable == 'RFM'].set_index('value').plot.bar(subplots = True, sharex = False, figsize = (12,12))
plt.tight_layout();
```


    
![png](static/notebooks/ecommerce/part3_files/part3_150_0.png)
    



```python
minicubo[minicubo.variable == 'valor']
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
      <th>variable</th>
      <th>value</th>
      <th>productos_tot_num</th>
      <th>compras_tot_num</th>
      <th>gasto_tot</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>52</th>
      <td>valor</td>
      <td>3</td>
      <td>7.97</td>
      <td>1.08</td>
      <td>39.28</td>
    </tr>
    <tr>
      <th>53</th>
      <td>valor</td>
      <td>4</td>
      <td>9.04</td>
      <td>1.17</td>
      <td>44.41</td>
    </tr>
    <tr>
      <th>54</th>
      <td>valor</td>
      <td>5</td>
      <td>9.31</td>
      <td>1.27</td>
      <td>46.08</td>
    </tr>
    <tr>
      <th>55</th>
      <td>valor</td>
      <td>6</td>
      <td>10.73</td>
      <td>1.38</td>
      <td>53.07</td>
    </tr>
    <tr>
      <th>56</th>
      <td>valor</td>
      <td>7</td>
      <td>12.64</td>
      <td>1.54</td>
      <td>60.42</td>
    </tr>
    <tr>
      <th>57</th>
      <td>valor</td>
      <td>8</td>
      <td>66.13</td>
      <td>5.06</td>
      <td>313.01</td>
    </tr>
    <tr>
      <th>58</th>
      <td>valor</td>
      <td>9</td>
      <td>98.02</td>
      <td>7.25</td>
      <td>491.71</td>
    </tr>
    <tr>
      <th>59</th>
      <td>valor</td>
      <td>10</td>
      <td>140.89</td>
      <td>10.22</td>
      <td>625.93</td>
    </tr>
    <tr>
      <th>60</th>
      <td>valor</td>
      <td>11</td>
      <td>291.00</td>
      <td>5.75</td>
      <td>1189.31</td>
    </tr>
    <tr>
      <th>61</th>
      <td>valor</td>
      <td>12</td>
      <td>189.80</td>
      <td>16.60</td>
      <td>833.43</td>
    </tr>
    <tr>
      <th>62</th>
      <td>valor</td>
      <td>13</td>
      <td>179.00</td>
      <td>18.00</td>
      <td>1136.70</td>
    </tr>
  </tbody>
</table>
</div>




```python
minicubo[minicubo.variable == 'valor'].set_index('value').plot.bar(subplots = True, sharex = False, figsize = (12,12))
plt.tight_layout();
```

    c:\Users\sgarciam\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\indexes\base.py:6982: FutureWarning:
    
    In a future version, the Index constructor will not infer numeric dtypes when passed object-dtype sequences (matching Series behavior)
    
    


    
![png](static/notebooks/ecommerce/part3_files/part3_152_1.png)
    


Se podría mejorar el análisis porque en F y M los atípicos hacen que se concentren la mayoría de los datos en la categoría 1.

Lo que habría que hacer es eliminar esos atípicos y volver a realizar el ejercicio.

Te lo dejo como tarea de práctica.

Pero con este análisis somos capaces de identificar los clientes que con mayor probabilidad responderán mejor a nuevas campañas, además de obtener un montón de insights valiosos para el negocio.

## Entendiendo los productos

Vamos a crear un dataframe a nivel de producto para poder analizar esta dimensión.

Primero calculamos los conteos de cada evento en cada producto.


```python
prod = df.groupby(['producto','evento']).size()
prod
```




    producto  evento          
    3752      view                 10
    3762      cart                127
              purchase             28
              remove_from_cart     59
              view                258
                                 ... 
    5932538   view                  1
    5932540   cart                  1
              view                  2
    5932578   view                  1
    5932585   view                  2
    Length: 137068, dtype: int64




```python
prod  = prod.unstack(level = 1).fillna(0)
prod
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
      <th>evento</th>
      <th>cart</th>
      <th>purchase</th>
      <th>remove_from_cart</th>
      <th>view</th>
    </tr>
    <tr>
      <th>producto</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3752</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>10.00</td>
    </tr>
    <tr>
      <th>3762</th>
      <td>127.00</td>
      <td>28.00</td>
      <td>59.00</td>
      <td>258.00</td>
    </tr>
    <tr>
      <th>3763</th>
      <td>10.00</td>
      <td>2.00</td>
      <td>2.00</td>
      <td>51.00</td>
    </tr>
    <tr>
      <th>3771</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>9.00</td>
    </tr>
    <tr>
      <th>3774</th>
      <td>26.00</td>
      <td>7.00</td>
      <td>13.00</td>
      <td>76.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5932537</th>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>5932538</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>5932540</th>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2.00</td>
    </tr>
    <tr>
      <th>5932578</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>5932585</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2.00</td>
    </tr>
  </tbody>
</table>
<p>45327 rows × 4 columns</p>
</div>



Vamos a incorporar el precio, para ello primero creamos un maestro de precios por producto.


```python
maestro_precios = df.groupby('producto', as_index = False).precio.mean()
maestro_precios
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
      <th>producto</th>
      <th>precio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3752</td>
      <td>15.71</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3762</td>
      <td>19.29</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3763</td>
      <td>16.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3771</td>
      <td>15.08</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3774</td>
      <td>15.92</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>45322</th>
      <td>5932537</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45323</th>
      <td>5932538</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45324</th>
      <td>5932540</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45325</th>
      <td>5932578</td>
      <td>6.02</td>
    </tr>
    <tr>
      <th>45326</th>
      <td>5932585</td>
      <td>6.33</td>
    </tr>
  </tbody>
</table>
<p>45327 rows × 2 columns</p>
</div>




```python
prod = pd.merge(left = prod, right = maestro_precios, how = 'left', on = 'producto')
prod
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
      <th>producto</th>
      <th>cart</th>
      <th>purchase</th>
      <th>remove_from_cart</th>
      <th>view</th>
      <th>precio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3752</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>10.00</td>
      <td>15.71</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3762</td>
      <td>127.00</td>
      <td>28.00</td>
      <td>59.00</td>
      <td>258.00</td>
      <td>19.29</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3763</td>
      <td>10.00</td>
      <td>2.00</td>
      <td>2.00</td>
      <td>51.00</td>
      <td>16.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3771</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>9.00</td>
      <td>15.08</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3774</td>
      <td>26.00</td>
      <td>7.00</td>
      <td>13.00</td>
      <td>76.00</td>
      <td>15.92</td>
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
      <th>45322</th>
      <td>5932537</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45323</th>
      <td>5932538</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45324</th>
      <td>5932540</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45325</th>
      <td>5932578</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>6.02</td>
    </tr>
    <tr>
      <th>45326</th>
      <td>5932585</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2.00</td>
      <td>6.33</td>
    </tr>
  </tbody>
</table>
<p>45327 rows × 6 columns</p>
</div>



Reordenamos los nombres.


```python
prod
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
      <th>producto</th>
      <th>cart</th>
      <th>purchase</th>
      <th>remove_from_cart</th>
      <th>view</th>
      <th>precio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3752</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>10.00</td>
      <td>15.71</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3762</td>
      <td>127.00</td>
      <td>28.00</td>
      <td>59.00</td>
      <td>258.00</td>
      <td>19.29</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3763</td>
      <td>10.00</td>
      <td>2.00</td>
      <td>2.00</td>
      <td>51.00</td>
      <td>16.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3771</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>9.00</td>
      <td>15.08</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3774</td>
      <td>26.00</td>
      <td>7.00</td>
      <td>13.00</td>
      <td>76.00</td>
      <td>15.92</td>
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
      <th>45322</th>
      <td>5932537</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45323</th>
      <td>5932538</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45324</th>
      <td>5932540</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45325</th>
      <td>5932578</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>6.02</td>
    </tr>
    <tr>
      <th>45326</th>
      <td>5932585</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2.00</td>
      <td>6.33</td>
    </tr>
  </tbody>
</table>
<p>45327 rows × 6 columns</p>
</div>




```python
prod = prod[['producto','view','cart','remove_from_cart','purchase','precio']]
prod
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
      <th>producto</th>
      <th>view</th>
      <th>cart</th>
      <th>remove_from_cart</th>
      <th>purchase</th>
      <th>precio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3752</td>
      <td>10.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>15.71</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3762</td>
      <td>258.00</td>
      <td>127.00</td>
      <td>59.00</td>
      <td>28.00</td>
      <td>19.29</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3763</td>
      <td>51.00</td>
      <td>10.00</td>
      <td>2.00</td>
      <td>2.00</td>
      <td>16.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3771</td>
      <td>9.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>15.08</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3774</td>
      <td>76.00</td>
      <td>26.00</td>
      <td>13.00</td>
      <td>7.00</td>
      <td>15.92</td>
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
      <th>45322</th>
      <td>5932537</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45323</th>
      <td>5932538</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45324</th>
      <td>5932540</td>
      <td>2.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45325</th>
      <td>5932578</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6.02</td>
    </tr>
    <tr>
      <th>45326</th>
      <td>5932585</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6.33</td>
    </tr>
  </tbody>
</table>
<p>45327 rows × 6 columns</p>
</div>



### ¿Cuales son los productos más vendidos?


```python
prod.sort_values('purchase',ascending = False)[0:20]
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
      <th>producto</th>
      <th>view</th>
      <th>cart</th>
      <th>remove_from_cart</th>
      <th>purchase</th>
      <th>precio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>16807</th>
      <td>5809910</td>
      <td>9195.00</td>
      <td>2796.00</td>
      <td>1249.00</td>
      <td>764.00</td>
      <td>5.21</td>
    </tr>
    <tr>
      <th>28178</th>
      <td>5854897</td>
      <td>624.00</td>
      <td>2486.00</td>
      <td>793.00</td>
      <td>483.00</td>
      <td>0.32</td>
    </tr>
    <tr>
      <th>6644</th>
      <td>5700037</td>
      <td>1150.00</td>
      <td>2603.00</td>
      <td>716.00</td>
      <td>361.00</td>
      <td>0.40</td>
    </tr>
    <tr>
      <th>314</th>
      <td>5304</td>
      <td>516.00</td>
      <td>1184.00</td>
      <td>426.00</td>
      <td>341.00</td>
      <td>0.32</td>
    </tr>
    <tr>
      <th>9900</th>
      <td>5751422</td>
      <td>2204.00</td>
      <td>1119.00</td>
      <td>625.00</td>
      <td>331.00</td>
      <td>10.87</td>
    </tr>
    <tr>
      <th>15394</th>
      <td>5802432</td>
      <td>701.00</td>
      <td>2495.00</td>
      <td>745.00</td>
      <td>322.00</td>
      <td>0.32</td>
    </tr>
    <tr>
      <th>16809</th>
      <td>5809912</td>
      <td>3059.00</td>
      <td>1352.00</td>
      <td>863.00</td>
      <td>321.00</td>
      <td>5.19</td>
    </tr>
    <tr>
      <th>18415</th>
      <td>5815662</td>
      <td>1219.00</td>
      <td>1697.00</td>
      <td>653.00</td>
      <td>310.00</td>
      <td>0.91</td>
    </tr>
    <tr>
      <th>9862</th>
      <td>5751383</td>
      <td>2341.00</td>
      <td>1035.00</td>
      <td>550.00</td>
      <td>298.00</td>
      <td>10.24</td>
    </tr>
    <tr>
      <th>14043</th>
      <td>5792800</td>
      <td>1527.00</td>
      <td>911.00</td>
      <td>512.00</td>
      <td>285.00</td>
      <td>10.25</td>
    </tr>
    <tr>
      <th>26312</th>
      <td>5849033</td>
      <td>2099.00</td>
      <td>1035.00</td>
      <td>583.00</td>
      <td>278.00</td>
      <td>10.25</td>
    </tr>
    <tr>
      <th>5386</th>
      <td>5686925</td>
      <td>344.00</td>
      <td>1677.00</td>
      <td>499.00</td>
      <td>231.00</td>
      <td>0.35</td>
    </tr>
    <tr>
      <th>6653</th>
      <td>5700046</td>
      <td>432.00</td>
      <td>1376.00</td>
      <td>381.00</td>
      <td>215.00</td>
      <td>0.40</td>
    </tr>
    <tr>
      <th>1761</th>
      <td>5528035</td>
      <td>1146.00</td>
      <td>719.00</td>
      <td>401.00</td>
      <td>200.00</td>
      <td>9.44</td>
    </tr>
    <tr>
      <th>22111</th>
      <td>5833330</td>
      <td>680.00</td>
      <td>576.00</td>
      <td>359.00</td>
      <td>194.00</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>16808</th>
      <td>5809911</td>
      <td>1923.00</td>
      <td>828.00</td>
      <td>599.00</td>
      <td>189.00</td>
      <td>5.21</td>
    </tr>
    <tr>
      <th>18525</th>
      <td>5816170</td>
      <td>1642.00</td>
      <td>751.00</td>
      <td>532.00</td>
      <td>182.00</td>
      <td>5.22</td>
    </tr>
    <tr>
      <th>5420</th>
      <td>5687151</td>
      <td>508.00</td>
      <td>540.00</td>
      <td>288.00</td>
      <td>179.00</td>
      <td>1.90</td>
    </tr>
    <tr>
      <th>8232</th>
      <td>5729864</td>
      <td>160.00</td>
      <td>505.00</td>
      <td>211.00</td>
      <td>176.00</td>
      <td>0.41</td>
    </tr>
    <tr>
      <th>24787</th>
      <td>5843836</td>
      <td>165.00</td>
      <td>1007.00</td>
      <td>265.00</td>
      <td>172.00</td>
      <td>0.38</td>
    </tr>
  </tbody>
</table>
</div>



Posiblemente lograríamos incrementar las ventas y el ticket medio simplemente destacando estos productos en la tienda.

### ¿Hay productos que no se venden y podríamos eliminar del catálogo?


```python
prod[prod.purchase == 0]
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
      <th>producto</th>
      <th>view</th>
      <th>cart</th>
      <th>remove_from_cart</th>
      <th>purchase</th>
      <th>precio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3752</td>
      <td>10.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>15.71</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3771</td>
      <td>9.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>15.08</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3790</td>
      <td>10.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>7.92</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3809</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>12.54</td>
    </tr>
    <tr>
      <th>9</th>
      <td>3812</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>12.54</td>
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
      <th>45322</th>
      <td>5932537</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45323</th>
      <td>5932538</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45324</th>
      <td>5932540</td>
      <td>2.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45325</th>
      <td>5932578</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6.02</td>
    </tr>
    <tr>
      <th>45326</th>
      <td>5932585</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>6.33</td>
    </tr>
  </tbody>
</table>
<p>21850 rows × 6 columns</p>
</div>



Guauu, hemos encontrado una buena!

INSIGHT #8: Casi la mitad de los productos no han tenido ninguna venta en los 5 meses del histórico.

Se podría comenzar todo un nuevo análisis sobre estos productos:

* ¿No se ven?
* ¿Se ven pero no se compran?
* ¿Es porque se sustituyen por otros productos propios?
* ¿Es porque están mucho más baratos en la competencia?
* Etc

Se podrían eliminar del catálogo, o como mínimo de la tienda, newsletter, etc, para que no ocupen espacio de los productos que sí se venden.

### ¿Cual es la relación entre el precio y el volumen de ventas?

Ya que este análisis incluye las ventas vamos a eliminar los productos que no han tenido ninguna.


```python
sns.scatterplot(data = prod[prod.purchase > 0], x = 'precio', y = 'purchase', hue = 'precio');
```


    
![png](static/notebooks/ecommerce/part3_files/part3_172_0.png)
    


Sí que existe una clara relación decreciente.

Vamos a hacer zoom por ejemplo por debajo de 50€ para entenderlo mejor.


```python
sns.scatterplot(data = prod[(prod.purchase > 0) & (prod.precio < 50)], x = 'precio', y = 'purchase', hue = 'precio');
```


    
![png](static/notebooks/ecommerce/part3_files/part3_174_0.png)
    


### ¿Hay productos de los que los clientes se arrepienten y eliminan más del carrito?


```python
prod.insert(loc = 4,
            column = 'remove_from_cart_porc',
            value = prod.remove_from_cart / prod.cart *100 )
prod
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
      <th>producto</th>
      <th>view</th>
      <th>cart</th>
      <th>remove_from_cart</th>
      <th>remove_from_cart_porc</th>
      <th>purchase</th>
      <th>precio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3752</td>
      <td>10.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>15.71</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3762</td>
      <td>258.00</td>
      <td>127.00</td>
      <td>59.00</td>
      <td>46.46</td>
      <td>28.00</td>
      <td>19.29</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3763</td>
      <td>51.00</td>
      <td>10.00</td>
      <td>2.00</td>
      <td>20.00</td>
      <td>2.00</td>
      <td>16.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3771</td>
      <td>9.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>15.08</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3774</td>
      <td>76.00</td>
      <td>26.00</td>
      <td>13.00</td>
      <td>50.00</td>
      <td>7.00</td>
      <td>15.92</td>
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
      <th>45322</th>
      <td>5932537</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45323</th>
      <td>5932538</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45324</th>
      <td>5932540</td>
      <td>2.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>45325</th>
      <td>5932578</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>6.02</td>
    </tr>
    <tr>
      <th>45326</th>
      <td>5932585</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>6.33</td>
    </tr>
  </tbody>
</table>
<p>45327 rows × 7 columns</p>
</div>




```python
prod.loc[prod.cart > 30].sort_values('remove_from_cart_porc', ascending = False)[0:30]
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
      <th>producto</th>
      <th>view</th>
      <th>cart</th>
      <th>remove_from_cart</th>
      <th>remove_from_cart_porc</th>
      <th>purchase</th>
      <th>precio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>14330</th>
      <td>5797131</td>
      <td>26.00</td>
      <td>38.00</td>
      <td>136.00</td>
      <td>357.89</td>
      <td>7.00</td>
      <td>4.43</td>
    </tr>
    <tr>
      <th>37937</th>
      <td>5893670</td>
      <td>36.00</td>
      <td>35.00</td>
      <td>109.00</td>
      <td>311.43</td>
      <td>3.00</td>
      <td>4.90</td>
    </tr>
    <tr>
      <th>29128</th>
      <td>5858481</td>
      <td>41.00</td>
      <td>31.00</td>
      <td>64.00</td>
      <td>206.45</td>
      <td>7.00</td>
      <td>4.55</td>
    </tr>
    <tr>
      <th>16658</th>
      <td>5809346</td>
      <td>8.00</td>
      <td>34.00</td>
      <td>62.00</td>
      <td>182.35</td>
      <td>7.00</td>
      <td>0.78</td>
    </tr>
    <tr>
      <th>26120</th>
      <td>5848412</td>
      <td>34.00</td>
      <td>37.00</td>
      <td>66.00</td>
      <td>178.38</td>
      <td>12.00</td>
      <td>0.79</td>
    </tr>
    <tr>
      <th>37944</th>
      <td>5893677</td>
      <td>64.00</td>
      <td>41.00</td>
      <td>70.00</td>
      <td>170.73</td>
      <td>10.00</td>
      <td>4.69</td>
    </tr>
    <tr>
      <th>8416</th>
      <td>5731470</td>
      <td>39.00</td>
      <td>34.00</td>
      <td>58.00</td>
      <td>170.59</td>
      <td>10.00</td>
      <td>6.32</td>
    </tr>
    <tr>
      <th>3217</th>
      <td>5635096</td>
      <td>32.00</td>
      <td>32.00</td>
      <td>52.00</td>
      <td>162.50</td>
      <td>11.00</td>
      <td>4.42</td>
    </tr>
    <tr>
      <th>3244</th>
      <td>5635127</td>
      <td>41.00</td>
      <td>32.00</td>
      <td>52.00</td>
      <td>162.50</td>
      <td>10.00</td>
      <td>4.43</td>
    </tr>
    <tr>
      <th>21617</th>
      <td>5830537</td>
      <td>35.00</td>
      <td>37.00</td>
      <td>60.00</td>
      <td>162.16</td>
      <td>8.00</td>
      <td>1.73</td>
    </tr>
    <tr>
      <th>39359</th>
      <td>5900645</td>
      <td>47.00</td>
      <td>33.00</td>
      <td>52.00</td>
      <td>157.58</td>
      <td>8.00</td>
      <td>4.39</td>
    </tr>
    <tr>
      <th>6222</th>
      <td>5696152</td>
      <td>81.00</td>
      <td>41.00</td>
      <td>64.00</td>
      <td>156.10</td>
      <td>12.00</td>
      <td>2.37</td>
    </tr>
    <tr>
      <th>29629</th>
      <td>5859474</td>
      <td>44.00</td>
      <td>43.00</td>
      <td>67.00</td>
      <td>155.81</td>
      <td>12.00</td>
      <td>1.72</td>
    </tr>
    <tr>
      <th>31887</th>
      <td>5867624</td>
      <td>26.00</td>
      <td>46.00</td>
      <td>70.00</td>
      <td>152.17</td>
      <td>10.00</td>
      <td>3.89</td>
    </tr>
    <tr>
      <th>9227</th>
      <td>5741027</td>
      <td>89.00</td>
      <td>35.00</td>
      <td>53.00</td>
      <td>151.43</td>
      <td>7.00</td>
      <td>5.19</td>
    </tr>
    <tr>
      <th>2123</th>
      <td>5560972</td>
      <td>73.00</td>
      <td>51.00</td>
      <td>76.00</td>
      <td>149.02</td>
      <td>11.00</td>
      <td>2.98</td>
    </tr>
    <tr>
      <th>6235</th>
      <td>5696184</td>
      <td>38.00</td>
      <td>41.00</td>
      <td>61.00</td>
      <td>148.78</td>
      <td>7.00</td>
      <td>2.37</td>
    </tr>
    <tr>
      <th>17716</th>
      <td>5813067</td>
      <td>48.00</td>
      <td>43.00</td>
      <td>63.00</td>
      <td>146.51</td>
      <td>5.00</td>
      <td>1.72</td>
    </tr>
    <tr>
      <th>221</th>
      <td>4874</td>
      <td>26.00</td>
      <td>39.00</td>
      <td>57.00</td>
      <td>146.15</td>
      <td>10.00</td>
      <td>0.37</td>
    </tr>
    <tr>
      <th>27643</th>
      <td>5853242</td>
      <td>47.00</td>
      <td>43.00</td>
      <td>62.00</td>
      <td>144.19</td>
      <td>6.00</td>
      <td>3.15</td>
    </tr>
    <tr>
      <th>33396</th>
      <td>5875280</td>
      <td>53.00</td>
      <td>32.00</td>
      <td>46.00</td>
      <td>143.75</td>
      <td>5.00</td>
      <td>5.53</td>
    </tr>
    <tr>
      <th>34325</th>
      <td>5877765</td>
      <td>62.00</td>
      <td>35.00</td>
      <td>50.00</td>
      <td>142.86</td>
      <td>9.00</td>
      <td>9.02</td>
    </tr>
    <tr>
      <th>23183</th>
      <td>5837619</td>
      <td>128.00</td>
      <td>81.00</td>
      <td>115.00</td>
      <td>141.98</td>
      <td>18.00</td>
      <td>1.73</td>
    </tr>
    <tr>
      <th>23833</th>
      <td>5839637</td>
      <td>55.00</td>
      <td>43.00</td>
      <td>61.00</td>
      <td>141.86</td>
      <td>12.00</td>
      <td>2.37</td>
    </tr>
    <tr>
      <th>28667</th>
      <td>5857018</td>
      <td>33.00</td>
      <td>32.00</td>
      <td>45.00</td>
      <td>140.62</td>
      <td>7.00</td>
      <td>3.15</td>
    </tr>
    <tr>
      <th>13942</th>
      <td>5789608</td>
      <td>57.00</td>
      <td>32.00</td>
      <td>45.00</td>
      <td>140.62</td>
      <td>7.00</td>
      <td>4.69</td>
    </tr>
    <tr>
      <th>3005</th>
      <td>5619864</td>
      <td>80.00</td>
      <td>47.00</td>
      <td>66.00</td>
      <td>140.43</td>
      <td>8.00</td>
      <td>2.84</td>
    </tr>
    <tr>
      <th>3205</th>
      <td>5635081</td>
      <td>26.00</td>
      <td>35.00</td>
      <td>49.00</td>
      <td>140.00</td>
      <td>4.00</td>
      <td>4.40</td>
    </tr>
    <tr>
      <th>30741</th>
      <td>5863821</td>
      <td>42.00</td>
      <td>51.00</td>
      <td>71.00</td>
      <td>139.22</td>
      <td>1.00</td>
      <td>4.49</td>
    </tr>
    <tr>
      <th>10701</th>
      <td>5760769</td>
      <td>38.00</td>
      <td>31.00</td>
      <td>43.00</td>
      <td>138.71</td>
      <td>6.00</td>
      <td>2.62</td>
    </tr>
  </tbody>
</table>
</div>



Habría que ver por qué estos productos se eliminan más veces de las que se añaden:

* Si el motivo tiene sentido: revisar qué pasa con estos productos (otros productos alternativos, etc.)
* Si no lo tiene eliminar estos registros y analizar únicamente los que tienen remove_from_cart_porc menor o igual a 100	

### ¿Cuales son los productos más vistos?


```python
prod.view.sort_values(ascending = False)[0:20].plot.bar();
```


    
![png](static/notebooks/ecommerce/part3_files/part3_180_0.png)
    


Posiblemente lograríamos incrementar las ventas y el ticket medio simplemente destacando estos productos en la tienda.

Siempre que además de ser vistos también se vendan.

### ¿Hay productos deseados pero no comprados?

Por ejemplo productos que miran muchos clientes pero que luego no los compran.

Si los encontráramos habría que revisar qué pasa con ellos.


```python
sns.scatterplot(data = prod, x = 'view', y = 'purchase');
```


    
![png](static/notebooks/ecommerce/part3_files/part3_184_0.png)
    


Vamos a quitar el atípico y hacer zoom en la ventana de muchas vistas pocas compras.


```python
sns.scatterplot(data = prod.loc[prod.view < 4000], x = 'view', y = 'purchase', hue = 'precio')
plt.xlim(1000,3000)
plt.ylim(0,150)
```




    (0.0, 150.0)




    
![png](static/notebooks/ecommerce/part3_files/part3_186_1.png)
    


Hay una oportunidad con estos productos, porque por algún motivo generan el interés de los clientes, pero finalmente no los compran.

Habría que hacer un análisis sobre ellos.

### Construyendo un sistema de recomendación

Uno de los activos que más pueden incrementar las ventas de un ecommerce es un sistema de recomendación.

Ya podríamos aplicar uno básico con los análisis de más visto y más vendido realizados anteriormente.

Pero la verdadera potencia viene cuando creamos un recomendador que personaliza para cada compra.

Tipos de sistemas de recomendación:

* Filtrado colaborativo:
    * Basados en items
    * Basados en usuario
* De contenido

En nuestro caso vamos a desarrollar uno con filtrado colaborativo basado en items.

Los pasos a seguir son:

1. Crear el dataframe con el kpi de interés
2. Reducir la dimensión (opcional)
3. Seleccionar una métrica de distancia
4. Calcular la matriz item-item
5. Crear la lógica de priorización

#### Crear el dataframe con el kpi de interés

En este caso usaremos lo que se llama un kpi implícito, que será el número de veces que los productos han sido comprados por el mismo usuario.

Kpis explícitos sería por ejemplo estrellas o puntuaciones del 1 al 10.

Dado que este es una algoritmo que tarda en calcularse vamos a reducir el problema y calcularlo solo para los 100 productos más vendidos.

Además, por motivos didácticos vamos a hacer el paso a paso manualmente. En un uso real se recomienda usar un paquete ya preconstruído que posiblemente estará más optimizado en cuanto a rendimiento.

Primero calculamos un maestro con los 100 productos más vendidos.


```python
mas_vendidos = prod.sort_values('purchase', ascending = False).producto[0:100]
mas_vendidos
```




    16807    5809910
    28178    5854897
    6644     5700037
    314         5304
    9900     5751422
              ...   
    30395    5862564
    9778     5749720
    9732     5749149
    22751    5835859
    22116    5833335
    Name: producto, Length: 100, dtype: int64



Creamos un dataframe temporal filtrando por estos productos.


```python
temp = df.loc[df.producto.isin(mas_vendidos)]
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
      <th>2019-10-01 00:26:49</th>
      <td>536128518</td>
      <td>a31f0991-645e-4472-a012-95eb2f814568</td>
      <td>1487580006317032337</td>
      <td>purchase</td>
      <td>...</td>
      <td>49</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:46:20</th>
      <td>555415545</td>
      <td>b9cc1771-9062-4e08-a3ad-363314cd17d8</td>
      <td>1602943681873052386</td>
      <td>view</td>
      <td>...</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:48:13</th>
      <td>555415545</td>
      <td>b9cc1771-9062-4e08-a3ad-363314cd17d8</td>
      <td>1602943681873052386</td>
      <td>view</td>
      <td>...</td>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 00:52:39</th>
      <td>555415545</td>
      <td>b9cc1771-9062-4e08-a3ad-363314cd17d8</td>
      <td>1487580005092295511</td>
      <td>view</td>
      <td>...</td>
      <td>39</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2019-10-01 01:33:26</th>
      <td>555456891</td>
      <td>b3239dc3-f107-4034-a507-4c41f646e38a</td>
      <td>1487580005092295511</td>
      <td>view</td>
      <td>...</td>
      <td>26</td>
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
      <th>2020-02-29 23:11:44</th>
      <td>615102046</td>
      <td>17b94398-0397-4c59-bc84-fe91dde0a8ec</td>
      <td>1487580006509970331</td>
      <td>cart</td>
      <td>...</td>
      <td>44</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-02-29 23:12:40</th>
      <td>615102046</td>
      <td>17b94398-0397-4c59-bc84-fe91dde0a8ec</td>
      <td>2195085255034011676</td>
      <td>cart</td>
      <td>...</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-02-29 23:12:50</th>
      <td>599909613</td>
      <td>1c6c708d-135d-487b-afa9-4bbcfd28db4d</td>
      <td>1602943681873052386</td>
      <td>cart</td>
      <td>...</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-02-29 23:20:21</th>
      <td>231719601</td>
      <td>a7467d5c-e848-406f-97f4-fcb6a4113e68</td>
      <td>1602943681873052386</td>
      <td>view</td>
      <td>...</td>
      <td>21</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
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
  </tbody>
</table>
<p>168170 rows × 16 columns</p>
</div>



Creamos la matriz  usuario-item.


```python
usuario_item = temp.loc[temp.evento == 'purchase'].groupby(['usuario','producto']).size().unstack(level = 1).fillna(0)
usuario_item
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
      <th>producto</th>
      <th>4497</th>
      <th>4600</th>
      <th>4768</th>
      <th>4938</th>
      <th>...</th>
      <th>5857360</th>
      <th>5862564</th>
      <th>5862943</th>
      <th>5889300</th>
    </tr>
    <tr>
      <th>usuario</th>
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
      <th>25392526</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>50748978</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>74332980</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>80577370</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>88211255</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
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
    </tr>
    <tr>
      <th>621646584</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>621788730</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>621925941</th>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>621974977</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>622021687</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>5064 rows × 100 columns</p>
</div>



#### Reducir la dimensión (opcional)

Vemos que nos ha salido una matriz sparse.

Posiblemente sería conveniente reducir la dimensión con técnicas como SVD, pero eso requería un minicurso en sí mismo.

Aquí vamos a continuar sin hacer la reducción.

#### Seleccionar una métrica de distancia

Métricas más comunes:

* Distancia euclídea
* Correlación
* Coseno

En este caso vamos a coger por ejemplo la distancia euclídea.

La operativizamos mediante la función spatial.distance.euclidean de Scipy.


```python
from scipy import spatial
```

#### Calcular la matriz item-item

Creamos el recomendador que toma como input una matriz usuario-item y devuelve una matriz item-item con la distancia euclídea como dato.


```python
def recomendador(dataframe):

    def distancia(producto):
        return(dataframe.apply(lambda x: spatial.distance.euclidean(x,producto)))

    return(dataframe.apply(lambda x: distancia(x)))
```


```python
item_item = recomendador(usuario_item)
item_item
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
      <th>producto</th>
      <th>4497</th>
      <th>4600</th>
      <th>4768</th>
      <th>4938</th>
      <th>...</th>
      <th>5857360</th>
      <th>5862564</th>
      <th>5862943</th>
      <th>5889300</th>
    </tr>
    <tr>
      <th>producto</th>
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
      <th>4497</th>
      <td>0.00</td>
      <td>14.42</td>
      <td>14.49</td>
      <td>15.62</td>
      <td>...</td>
      <td>15.78</td>
      <td>15.17</td>
      <td>16.40</td>
      <td>15.33</td>
    </tr>
    <tr>
      <th>4600</th>
      <td>14.42</td>
      <td>0.00</td>
      <td>10.68</td>
      <td>14.49</td>
      <td>...</td>
      <td>14.46</td>
      <td>13.86</td>
      <td>14.73</td>
      <td>13.89</td>
    </tr>
    <tr>
      <th>4768</th>
      <td>14.49</td>
      <td>10.68</td>
      <td>0.00</td>
      <td>14.56</td>
      <td>...</td>
      <td>14.39</td>
      <td>13.86</td>
      <td>14.80</td>
      <td>14.11</td>
    </tr>
    <tr>
      <th>4938</th>
      <td>15.62</td>
      <td>14.49</td>
      <td>14.56</td>
      <td>0.00</td>
      <td>...</td>
      <td>15.46</td>
      <td>14.97</td>
      <td>15.72</td>
      <td>15.13</td>
    </tr>
    <tr>
      <th>4958</th>
      <td>15.91</td>
      <td>14.59</td>
      <td>14.73</td>
      <td>15.52</td>
      <td>...</td>
      <td>15.94</td>
      <td>15.26</td>
      <td>16.12</td>
      <td>15.03</td>
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
      <th>5857007</th>
      <td>15.07</td>
      <td>13.60</td>
      <td>13.75</td>
      <td>14.59</td>
      <td>...</td>
      <td>14.83</td>
      <td>14.46</td>
      <td>15.17</td>
      <td>14.42</td>
    </tr>
    <tr>
      <th>5857360</th>
      <td>15.78</td>
      <td>14.46</td>
      <td>14.39</td>
      <td>15.46</td>
      <td>...</td>
      <td>0.00</td>
      <td>13.75</td>
      <td>16.19</td>
      <td>15.43</td>
    </tr>
    <tr>
      <th>5862564</th>
      <td>15.17</td>
      <td>13.86</td>
      <td>13.86</td>
      <td>14.97</td>
      <td>...</td>
      <td>13.75</td>
      <td>0.00</td>
      <td>15.39</td>
      <td>14.66</td>
    </tr>
    <tr>
      <th>5862943</th>
      <td>16.40</td>
      <td>14.73</td>
      <td>14.80</td>
      <td>15.72</td>
      <td>...</td>
      <td>16.19</td>
      <td>15.39</td>
      <td>0.00</td>
      <td>15.23</td>
    </tr>
    <tr>
      <th>5889300</th>
      <td>15.33</td>
      <td>13.89</td>
      <td>14.11</td>
      <td>15.13</td>
      <td>...</td>
      <td>15.43</td>
      <td>14.66</td>
      <td>15.23</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 100 columns</p>
</div>



#### Crear la lógica de priorización

Ya tenemos listo el recomendador.

Lo que tendríamos que hacer es una llamada a esta tabla cada vez que un usuario mire un producto o lo meta en el carrito.

Pero para que sea más efectivo podríamos usar toda la info acumulada de la sesión o incluso de todo el usuario si está logado.

Eso significa que necesitamos un sistema para recomendar productos tanto si el input es de un solo producto como de varios.

Y que a la vez devuelva varias recomendaciones, para cubrir todos los "huecos" de recomendación que nuestra web pudiera tener.

Aplicaremos un algoritmo muy sencillo que hará:

1. Crear un array con los productos de entrada para extraer sus vectores de la matriz item-item
2. Calcular la suma de distancias de todos los productos
3. Quitarse a ellos mismos para no autorecomendarse.
4. Devolver los 10 con menor distancia


```python
#En el caso de varios productos vendrá del servidor web como una cadena separada con punto y coma
def priorizador(productos,devuelve = 10):
    #crear array con productos de entrada
    array = np.int64(productos.split(';'))
    
    #extraer sus vectores de la matriz total
    matriz = item_item[array]
    
    #calcular la suma de distancias
    suma_distancias = matriz.agg(sum,axis = 1)
    
    #eliminar los productos input
    suma_distancias = suma_distancias.loc[~suma_distancias.index.isin(list(array))]
    
    #Devolver los 10 con menor distancia
    return(suma_distancias.sort_values()[0:devuelve])
```

Comprobamos cómo funciona si le pasamos un producto


```python
priorizador('4497')
```




    producto
    5724230             14.39
    4600                14.42
    5550302             14.49
    4768                14.49
    5749149             14.56
    5833318             14.63
    5824810             14.70
    5835859             14.70
    5809303             14.73
    5833335             14.73
    dtype: float64



Comprobamos cómo funciona si le pasamos varios productos


```python
priorizador('4497;4600;4768')
```




    producto
    5749149             40.25
    5833318             40.47
    5833335             40.81
    5809303             40.81
    5724230             41.00
    5824810             41.08
    5835859             41.23
    5550302             41.47
    5816169             41.51
    5844894             41.55
    dtype: float64



# CONCLUSIONES

La tendencia actual es plana en todas las métricas, lo que confirma la necesidad de las acciones de CRO.

Tras el análisis realizado sobre los datos transaccionales se ha desarrollado un plan CRO de 12 iniciativas concretas organizadas en 5 grandes palancas de negocio que con alta probabilidad van a incrementar los baselines consiguiendo un incremento global de los ingresos del ecommerce.

## Baseline

En cada sesión, de media:

* KPIs por sesión: Se ven 2.2 productos
* KPIs por sesión: Se añaden 1.3 productos al carrito
* KPIs por sesión: Se eliminan 0.9 productos del carrito
* KPIs por sesión: Se compran 0.3 productos
* Venta cruzada: mediana de 5 productos por compra
* Recurrencia: el 10% de los clientes vuelve a comprar tras el primer mes
* Conversión: 60% de añadir al carrito sobre visualizaciones
* Conversión: 22% de compra sobre añadidos a carrito
* Conversión: 13% de compra sobre visualizaciones
* Facturación media mensual: 125.000€

## Acciones de incremento de visualizaciones

1. Revisar las campañas de paid (generación y retargeting) para concentrar la inversión en franjas entre las 9 y las 13 y entre las 18 y las 20
2. Concentrar la inversión del período navideño y post-navideño en la semana del black friday
3. Incrementar la inversión hasta llegar al CPA máximo en base al LTV que hemos identificado

## Acciones de incremento de conversión

4. Preconfigurar la home con los productos identificados en los análisis most viewed y most sold.
5. Trabajar sobre los productos con alta tasa de abandono de carrito
6. Trabajar sobre los productos muy vistos pero poco comprados

## Acciones de incremento de venta cruzada

7. La compra mediana incluye 5 productos
8. Incrementar este ratio mediante la recomendación en tiempo real con el nuevo recomendador

## Acciones de incremento de frecuencia de compra

9. El 90% de los clientes sólo hace una compra
10. Crear una newsletter periódica con el nuevo recomendador para incrementar la frecuencia de visita
11. Campañas promocionales sobre los segmentos top de la segmentación RFM

## Acciones de fidelización de clientes

12. Crear un programa de fidelización segmentado por la nueva segmentación RFM
