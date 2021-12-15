# Trabajo realizado por José Vasquez y Matías Barra

**Proyecto en grupo (2 miembros) - opción A:** El proyecto en grupo consiste en entrenar y evaluar varios modelos de clasificación supervisada capaz de clasificar una noticia según la taxonomía siguiente: 

- 1- Mundo, 2- Economía, 3- Política y Conflictos, 4- Ciencias y Tecnología, 5- Catástrofes y Accidentes, 6- Cultura y Artes, 7- Deporte, 8- Ecología y Planeta, 9- Crimen, delitos y Justicia, 10- Salud


# Actualización entrega 2

Para poder entrenar el modelo, se realizaron 6 pasos, donde los primeros 2 se mantuvieron exactamente igual, el paso 3 se modificó y apartir del paso 4 es el proceos de clasificación de noticias.

**Pasos:**


3. **Scrapping**
Para poder aumentar el volumen de noticias, se decidió utilizar la tecnica vista en clases de *scrapping*. Se scrappearon noticias del medio de prensa CNN para las categorias de cultura, ecologia y planeta, catastrofe y accidentes, creando un dataset de noticias distinto para cada categoria. 

4. **Unir dataframe**
Se juntaron los dataset generados en el paso **3** con nuestro dataset final, aumentando nuestra cantidad de noticias para entrenar.


5. **Primeros modelos de clasificación**

Se realiza un preprocesamiento al dataset para luego realizar el entrenamiento de los primeros modelos de clasificación de noticias. 
Los modelos utilizados en este paso fueron, Regresión Logistica, RandomForest y CNN.

Se compraró el rendimiento de los modelos utilizando NLTK o Spacy.

Estos modelos fueron entrenados sin ajuste de parametros, con la intención de comprar sus rendimientos a grandes rasgos, en concreto, en los pasos siguentes trabajaremos con CNN para intentar mejorar su rendimiento. 

6. **Optimización con CNN**

Este es el pasó con más trabajo, donde se fueron probando distintos parametros para poder mejorar el acc y disminuir la loss del modelo. en la parte final hay una tabla resumen con los distintos modelos generados y sus distintos valores.

Algunos de los parametros que se fueron ajustando son, epocas, loss, batch size, etc.




## Información importante entrega 1

Este proyecto está dividido en 3 cuadernillos:

1. **Paso_1_extracion_por_url_y_lda**: Clasificación de noticias por su URL y LDA
    * Clasificación inicial mediante la url y categoría que proveen los propios medios de prensa y luego aplicación de LDA para categorizar noticias que no fue posibles categorizarlas con el metodo anterior.

2. **paso_2_re_extraccion_lda**: Re-clasificación de tópicos.
    * Para poder mejorar la elección de categoría, se realizó un segundo LDA con la intención poder clasificar de mejor manera algunos tópicos que no eran clasificables en primera instancia.

3. **paso_3_unir_dataframes**: Se unen las nuevas clasificaciones al dataset final

El trabajo realizado con LDA se basa en el material que se encuentra en el repositorio https://github.com/matthieuvernier/INFO279_2021


# Conclusiones: 
*  La estrategia adoptada entrega etiquetas correctas para una buena parte de las noticias, pero, al no tratarse de una revisión exhaustiva hecha por personas, algunas noticias no se encuentran correctamente etiquetadas, cosa que queda en evidencia al mostrar el contenido y la categoría de ciertos dataframes en los cuadernillos.
*  En general, estamos satisfechos con el dataset inicial resultante, pero sin lugar a dudas es algo mejorable como por ejemplo a través de un uso más fino de LDA para disminuir el número de noticias mal etiquetadas, y para suplir de más material a las categorías menos numerosas.
* Las noticias de 1. Mundo es posible reclasificarlas si asumimos que dentro de mundo pueden haber noticias de Salud, Politica, Conflictos, etc. quiźas utiliando esas noticas podríamos disminuir el posible sesgo que tenga nuestro dataset debido a la diversidad de noticias que podria abarcar mundo.


# Link dataset:

* https://drive.google.com/file/d/1DdCCxYTvKl249F6SL6XR1bFc09Z_ll7q/view?usp=sharing
