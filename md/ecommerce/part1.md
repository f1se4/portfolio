# DISEÑO DEL PROYECTO

En este caso trabajaremos como consultores para un ecommerce del sector cosméticos.

Esta empresa ha teniendo una evolución plana durante los últimos meses y nos ha contratado para analizar sus datos transaccionales e implementar acciones CRO personalizadas a su situación en base a dicho análisis.

En este caso entre otras cosas vamos a aprender:

* cómo son los datos de un ecommerce
* técnicas de análisis orientadas a incrementar facturación y margen en un ecommerce, tanto básicas o genéricas como algunas técnicas avanzadas específicas de este sector
* las principales métricas sobre las que tenemos que trabajar y algunas acciones CRO que podemos poner en práctica para mejorarlas
* a construir dos recursos analíticos muy potentes para este sector: una segmentación RFM y un sistema de recomendación. 

Por tanto, mucho de lo que aprendamos aquí es de aplicación general en prácticamente cualquier ecommerce.

## OBJETIVO

Analizar los datos transaccionales para intentar potenciales acciones CRO que incrementen visitas, conversiones y ticket medio, y por tanto incrementar la facturación global del ecommerce.

Crear activos analíticos avanzados como una segmentación RFM y un sistema de recomendación que impulsen la consecución del objetivo.

## PALANCAS

Como siempre vamos a entender primero el negocio, y sus principales procesos, métricas y conceptos.





    
![png](static/notebooks/ecommerce/part1_files/part1_6_0.png)
    



El primer paso es cuando un usuario llega a la web del ecommerce. Normalmente vendrá desde:

* Campañas de pago: paid ads como Facebook Ads o Google Ads
* Contenido orgánico: blog, rrss, ...
* Tráfico directo: conoce la url y la introduce en el navegador

Ese tráfico se llama visitas, y las páginas que van viendo se llaman páginas vistas, aunque en nuestro caso lo llamaremos views.

El usuario navega por la web y cuando le gusta un producto lo mete en el carrito.

Finalmente puede sacar productos del carrito, salir sin comprar nada, o finalmente hacer el pedido.

Un proceso común es la venta cruzada, en la cual se recomiendan al usuario otros productos que también podrían interesarle.

Incluso cuando se ha ido podemos volver a contartar al usuario mediante retargeting o email marketing.

Todo este proceso se llama funnel o también customer journey.

En el entorno online prácticamente todo se puede registrar. 

El registro del usuario puede ser logado o no.

La secuencia de acciones que hace un usuario en la misma sesión de navegación se llama sesión.

El ratio de compras sobre las visitas se llama ratio de conversión.

Además existen otras métricas clave que tenemos que dominar para gestionar correctamente un ecommerce:

* CPA
* AOV
* Frecuencia de compra
* LTV
* Churn

CONCEPTO CLAVE: Solo existen 3 formas de incrementar un negocio:

1. Más clientes: esto implica conseguir más visitas y mayor conversión
2. Más frecuencia: esto implica conseguir que los mismos clientes compren más veces
3. Mayor ticket medio: esto implica conseguir que se compre más o más caro en la misma sesión de compra

Para conseguir esos 3 efectos trabajamos sobre las siguientes palancas operativas:

* Customer journey: cómo podemos optimizar cada uno de los pasos del proceso
* Clientes: cómo podemos usar la info disponible de los clientes para optimizar las campañas que realicemos
* Productos: cómo podemos optimizar el catálogo de productos e identificar de manera personalizada qué productos tenemos que poner delante de cada cliente

Entenderemos en nuestro caso CRO de manera amplia, es decir como la disciplina que pone en práctica acciones para trabajar sobre las palancas y conceptos anteriores.

## KPIs

* Visitas
* Conversión
* Frecuencia de compra
* Ticket medio
* Tasa abandono carrito
* LTV

## ENTIDADES Y DATOS

En nuestro caso las entidades que tenemos en la granularidad de los datos son:
    
* Usuarios
* Clientes
* Sesiones
* Eventos
* Productos

## PREGUNTAS SEMILLA

Habiendo entendido las palancas, kpis y entidades ya podemos plantear las preguntas semilla:

Sobre el customer journey:

* ¿Cómo es un proceso típico de compra?
* ¿Cuántos productos se ven, se añaden al carro, se abandonan y se compran de media en cada sesión?
* ¿Cómo ha sido la tendencia de estos indicadores en los últimos meses?

Sobre los clientes:

* ¿Cuántos productos compra cada cliente?
* ¿Cuánto se gasta cada cliente?
* ¿Hay "mejores clientes" que haya que identificar y tratar de forma diferente?
* ¿Los clientes repiten compras en los siguientes meses?
* ¿Cual es el LTV medio de un cliente?
* ¿Podemos diseñar campañas personalizas al valor del cliente?

Sobre los productos:

* ¿Cuales son los productos más vendidos?
* ¿Hay productos que no se venden?
* ¿Existe relación entre el precio del producto y su volumen de ventas?
* ¿Hay productos que se visiten pero no se compren?
* ¿Hay productos que se saquen recurrentemente del carrito?
* ¿Se podrían hacer recomendaciones personalizadas de productos para cada cliente?
