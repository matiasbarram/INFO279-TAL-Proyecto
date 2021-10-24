# Trabajo realizado por José Vasquez y Matías Barra

**Proyecto en grupo (2 miembros) - opción A:** El proyecto en grupo consiste en entrenar y evaluar varios modelos de clasificación supervisada capaz de clasificar una noticia según la taxonomía siguiente: 

- 1- Mundo, 2- Economía, 3- Política y Conflictos, 4- Ciencias y Tecnología, 5- Catástrofes y Accidentes, 6- Cultura y Artes, 7- Deporte, 8- Ecología y Planeta, 9- Crimen, delitos y Justicia, 10- Salud

# Información importante

Este proyecto está dividido en 3 cuadernillos:

1. **Paso_1_extracion_por_url_y_lda**: Clasificación de noticias por su URL y LDA
    * Clasificación inicial mediante la url y categoría que proveen los propios medios de prensa y luego aplicación de LDA para categorizar noticias que no fue posibles categorizarlas con el metodo anterior.

2. **paso_2_re_extraccion_lda**: Re-clasificación de tópicos.
    * Para poder mejorar la elección de categoría, se realizó un segundo LDA con la intención poder clasificar de mejor manera algunos tópicos que no eran clasificables en primera instancia.

3. **paso_3_unir_dataframes**: Se unen las nuevas clasificaciones al dataset final

El trabajo realizado con LDA se basa en el material que se encuentra en el repositorio https://github.com/matthieuvernier/INFO279_2021


# Conclusiones: 
*  La estrategia adoptada entrega etiquetas correctas para una buena parte de las noticias, pero, al no tratarse de una revisión exhaustiva hecha por personas, algunas noticias no se encuentran correctamente etiquetadas, cosa que queda en evidencia al mostrar el contenido y la categoría de ciertos dataframes en los cuadernillos. En general, estamos satisfechos con el dataset inicial resultante, pero sin lugar a dudas es algo mejorable como por ejemplo a través de un uso más fino de LDA para disminuir el número de noticias mal etiquetadas, y para suplir de más material a las categorías menos numerosas.
* Las noticias de 1. Mundo es posible reclasificarlas si asumimos que dentro de mundo pueden haber noticias de Salud, Politica, Conflictos, etc. quiźas utiliando esas noticas podríamos disminuir el posible sesgo que tenga nuestro dataset debido a la diversidad de noticias que podria abarcar mundo.


# Link dataset:

* https://drive.google.com/file/d/1DdCCxYTvKl249F6SL6XR1bFc09Z_ll7q/view?usp=sharing
