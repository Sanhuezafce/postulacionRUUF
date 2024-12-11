# postulacionRUUF

## Sol techo rectangular
Con respecto a los paneles en el rectangulo, se puede notar en el codigo que se utilizan los tests provistos por RUUF junto con casos bases extra.
El uso de las 4 formas es necesario a pesar de que un principio pense de que no, ya que permite al paso recursivo probar en todas las posibles formas si el panel cabe en el techo.

## Sol techo triangular
A pesar de que no logre implementarlo por temas de tiempo, siento que la solucion propuesta al final del video explicativo funciona. Bastaria llamar recursivamente dando de parametro un triangulo cada mas chico (h-altura rectangulo) para asi lograr ver por sectores que tanto se puede rellenar el triangulo. Se puede volver a reutilizar la solucion del techo rectangular para cada sector y no estoy seguro al 100% si es necesario una funcion auxiliar para verificar que el rectangulo entre en el triangulo provisto. Creo que esto se puede confirmar sin dicha funcion al momento de calcular la altura del triangulo vs la altura del rectangulo.

## Sol techo sobrelapado
Con respecto a esta solucion, no tuve tiempo para pensar algo realmente viable. Lo unico que se me ocurre dentro del periodo de tiempo sugerido son los casos bases cuando el espacio del sobrelapamiento, no permite incluir rectangulos nuevos. En dicho caso, basta reutilizar la funcion del techo rectangular para mbos rectangulos y bastaria. En caso de que el espacio del sobrelapamiento si permita incluir rectangulos, se complica mas debido a que no basta con dividir en 3 sectores la figura (rect1, sobrelapamiento y rec2) ya que, esto impide que rectangulos alargados entren en 2 zonas a la vez. 

Debido a esto, no me atrevo a decir como lo solucionaria al 100% en esta ocasion.
