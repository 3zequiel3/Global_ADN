█ Instrucciones de uso de la app:

► Ingresar y ejecutar el archivo ejecutable.py

► Al ejecutar el codigo se abrira una consola en python que nos pedira que ingresemos en forma de filas 6 valores A, C, G y T que son las bases nitrogenadas del ADN, para lograr una matriz de 6x6

► Continuando con la ejecucion se abrira un nuevo MENU

► En el encontraremos 4 opciones a ingresar con los siguientes numeros:

2: Detectar mutaciones

 En este apartado el programa detectara si hay bases nitrogenadas que se repitan al menos 4 veces en vertical, horizontal o diagonalmente.

 Luego nos dara True, las posiciones y la base nitrogenada que se repite en caso de tener una mutacion presente en la matriz

 En el caso de que no se detecten mutaciones aparecera el siguiente mensaje:

 "Resultados de la detección: No se detectaron mutaciones en la matriz."

3: Mutar ADN

En este apartado nos apareceran varios mensajes y preguntas, en los cuales debemos ingresar parametros de la mutacion:

 - Ingrese la base nitrogenada para la mutación (A, C, G, T):

Debemos ingresar 1 solo valor entre a, c, g o t (es indistintohacerlo con mayuscula o minuscula)


 - Ingrese la intensidad de la mutación (4, 5, 6):

 En este punto elegiremos la intensidad de la mutacion si es de 4,5 o 6 bases nitrogenadas en que se aplicara la mutacion


 -¿Qué tipo de mutación deseas aplicar? (Radiacion o Virus):

 En este apartado tendremos 2 opciones si elegimos radiacion (mutacion horizontal o vertical) o virus (mutacion diagonal):

 ► Radiacion: 
    Aparecera otra pregunta mas y elegiremos en que direccion queremos realizar la mutacion
 -¿En qué dirección deseas realizar la mutación? (horizontal o vertical): 

 ► Virus:

 En ambos casos en este punto nos dara el resultado de la mutacion en pantalla y volvera a aparecer el Menu



4: Sanar ADN:  (completar)
   En este apartado el programa evalúa si el adn está mutado o no y lo guarda en una variabre booleana, y se muestra por pantalla el adn actual.
   
   Luego determina mediante un condicional if si se debe sanar o no.

   Si el condicional resulta en verdadero:
      
      Se llamara al metodo sanar_mutaciones, el cual vuelve a evaluar si la mutación es verdadera o falsa.

         Si la mutación es verdadera ejecutará un bloque de código para modificar el adn aleatoriamente, para luego volver a verificar si no está mutado, este proceso lo repetirá las veces que sea necesario. Y devolverá el adn sano.

         Cuando se verificó que el adn está sano, muestra por pantalla el nuevo adn.


   Si el condicional resulta en falso:
      mostrará por pantalla que el adn ya está sano y que no hay necesidad de sanarlo.

5: Salir

La opcion numero 5 dara por finalizada la ejecucion del programa




