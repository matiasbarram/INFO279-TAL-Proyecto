**Proyecto en grupo (2 miembros) - opción A:** El proyecto en grupo consiste en entrenar y evaluar varios modelos de clasificación supervisada capaz de clasificar una noticia según la taxonomía siguiente: 

- 1- Mundo, 2- Economía, 3- Política y Conflictos, 4- Ciencias y Tecnología, 5- Catástrofes y Accidentes, 6- Cultura y Artes, 7- Deporte, 8- Ecología y Planeta, 9- Crimen, delitos y Justicia, 10- Salud

# Información importante

Este proyecto está dividido en 3 cuadernillos:

1. **Paso_1_extracion_por_url_y_lda**: Clasificación de noticias por su URL y LDA
    * Clasificación inicial mediante la url y categoria que proveen los propios medios de prensa y luego aplicación de LDA para categorizar noticias que no fue posibles categorizarlas con el metodo anterior.

2. **paso_2_re_extraccion_lda**: Re-clasificación de topicos.
    * Para poder mejorar la eleccion de categoria, se realizó un segundo LDA con la intención poder clasificar de mejor manera algunos topicos que no eran clasificables en primera instancia.

3. **paso_3_unir_dataframes**: Se unen las nuevas clasificaciones al dataset final


# Conclusiones: 
* Estamos satisfechos con el resultado, pero es posible mejorar nuestro dataset inicial, podriamos realizar más LDA para clasificar de mejor manera las noticias.
* Las noticias de 1. Mundo es posible reclasificarlas si asumimos que dentro de mundo pueden haber noticias de Salud, Politica, Conflictos, etc. quiźas utiliando esas noticas podríamos disminuir el posible sesgo que tenga nuestro dataset debido a la diversidad de noticias que podria abarcar mundo.


# Link dataset:

* https://drive.google.com/file/d/1DdCCxYTvKl249F6SL6XR1bFc09Z_ll7q/view?usp=sharing
