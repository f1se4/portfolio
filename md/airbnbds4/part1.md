# DISEÑO DEL PROYECTO

Este caso simula que somos una empresa inmobiliaria que hace inversiones en grandes ciudades comprando inmuebles para posteriormente alquilarlos como apartamentos turísticos.

La dirección ha tomado la decisión de invertir en Madrid, y nos ha encargado analizar los datos que el líder del sector AirBnb hace públicos para intentar encontrar los tipos de inmuebles que tienen mayor potencial comercial para alquier turístico.

Como entregable principal esperan la tipología (o tipologías) de inmuebles que el equipo de valoraciones debe buscar entre las oportunidades existentes en la ciudad y los principales barrios o zonas geográficas en las que focalizarse.

Para cumplir con el objetivo aplicaremos la metodología de Discovery y las técnicas de BA aprendidas.

Aunque este caso concreto esté centrado en el alquiler turístico el mismo tipo de aproximación se puede usar en casos que tengan un alto componente de "ubicación":

* apertura y cierre de tiendas
* reducción de capacidad instalada
* expansión de franquicias
* etc.

## OBJETIVO

Localizar el perfil (o perfiles) de inmuebles que maximizan el potencial comercial en el mercado del alquiler turístico y las principales zonas donde buscarlos.

## PALANCAS

Tras hablar con el equipo de valoraciones nos dicen que las palancas que tienen más impacto en la rentabilidad de este tipo de inversiones son:

* **Precio alquiler**: cuanto más se pueda cobrar por noche mayor es la rentabilidad
* **Ocupación**: en general cuantos más días al año se pueda alquilar un inmueble mayor es su rentabilidad
* **Precio inmueble**: cuanto más barato se pueda adquirir la propiedad mayor es la rentabilidad

## KPIs

En este ejemplo los Kpis son bastante directos:

* Mediremos la ocupación como el número de días anuales que el inmueble se pueda alquilar
* Mediremos el precio del alquiler como el precio por noche en euros según Airbnb
* Mediremos el precio de un inmueble como la multiplicación entre el número de metros cuadrados y el precio medio del m2 en su zona, y aplicaremos un 25% de descuento sobre el precio oficial por la fuerza de negociciación de nuestro equipo de compras.

## ENTIDADES Y DATOS

Las entidades relevantes para nuestro objetivo y de las que podemos disponer de datos son:

* Inmuebles
* Propietarios
* Distritos

Los datos concretos en cada uno de ellos los revisaremos en el siguiente módulo.

## PREGUNTAS SEMILLA

Sobre el precio del alquiler:

* ¿Cual es el precio medio? ¿y el rango de precios?¿Y por distritos?¿Y por barrios?
* ¿Cual es el ranking de distritos y barrios por precio medio de alquiler?
* ¿Qué factores (a parte de la localización determinan el precio del alquiler?
* ¿Cual es la relación entre el tamaño del inmueble y el precio por el que se puede alquilar?
* ¿Cómo influye la competencia (num inmuebles disponibles por barrio) sobre el precio del alquiler?
* ¿Cómo varían los precios por tipo de alquiler (todo el piso, habitación privada, habitación compartida)?


Sobre la ocupación:

* ¿Cual es la ocupación media? ¿Y por distritos?¿Y por barrios?
* ¿Cómo de probable es cada nivel de ocupación en cada distrito?
* ¿Cual es el ranking de distritos y barrios por ocupación?
* ¿Qué factores (a parte de la localización determinan la ocupación?
* ¿Cual es la relación entre el tamaño del inmueble y su grado de ocupación?
* ¿Cómo influye la competencia (num inmuebles disponibles por barrio) sobre la ocupación?

Sobre el precio de compra:

* ¿Cual es el ranking de precio por m2 por distrito?
* ¿Cual es el ranking de precio del inmueble (m2 * tamaño medio) por distrito?
* ¿Cual es la relación entre el precio del inmueble y el precio del alquiler por distrito?
* ¿Cual es la relación entre el precio del inmueble y la ocupación por distrito?
