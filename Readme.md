# Instrucciones de uso de la app

1. **Ingresar y ejecutar el archivo `ejecutable.py`**.

2. **Ingreso de bases nitrogenadas**:
   
   Al ejecutar el código, se abrirá una consola en Python que nos pedirá que ingresemos en forma de filas **6 valores A, C, G y T**, que son las bases nitrogenadas del ADN. Esto generará una matriz de **6x6**.

3. **Menú principal**:
   
   Al continuar con la ejecución, se abrirá un **nuevo menú** con las siguientes opciones:

### Opciones del Menú:

#### Opción 2: **Detectar mutaciones**
   
   - En este apartado, el programa detectará si hay bases nitrogenadas que se repiten al menos **4 veces** en **vertical**, **horizontal** o **diagonal**.
   
   - Si se detectan mutaciones, el programa mostrará:
     - **True**
     - Las posiciones de las bases mutadas
     - La base nitrogenada que se repite.
   
   - Si no se detectan mutaciones, aparecerá el siguiente mensaje:
   
     > "Resultados de la detección: No se detectaron mutaciones en la matriz."

#### Opción 3: **Mutar ADN**
   
   En este apartado, se nos harán varias preguntas para ingresar parámetros de la mutación:

   1. **Ingrese la base nitrogenada para la mutación (A, C, G, T)**:
      - Ingrese **1 solo valor** entre **A**, **C**, **G**, o **T**. El programa acepta tanto mayúsculas como minúsculas.
   
   2. **Ingrese la intensidad de la mutación (4, 5, 6)**:
      - Elija la intensidad de la mutación, que se aplicará a **4**, **5** o **6** bases nitrogenadas.
   
   3. **¿Qué tipo de mutación deseas aplicar? (Radiación o Virus)**:
      - Tendremos **2 opciones**:
        - **Radiación**: Aparecerá una pregunta adicional donde elegiremos en qué dirección se realizará la mutación.
          - **¿En qué dirección deseas realizar la mutación? (horizontal o vertical)**.
        - **Virus**: Si elegimos **virus**, la mutación será **diagonal (Principal o Secundaria, según el Usuario decida)**.
   
   - En ambos casos, el programa aplicará la mutación y mostrará el resultado en pantalla. Luego, volverá a mostrar el menú principal.

#### Opción 4: **Sanar ADN**
   
   En este apartado, el programa realiza las siguientes acciones:

   - El programa evalúa si el ADN está mutado o no y lo guarda en una variable booleana.
   - El ADN actual se muestra en pantalla.
   - Luego, el programa evalúa, mediante un condicional `if`, si el ADN debe ser sanado.

     - Si el ADN **está mutado** (condicional `True`):
       1. Se llamará al método `sanar_mutaciones`, que vuelve a verificar si la mutación es **verdadera** o **falsa**.
       2. Si la mutación es **verdadera**, el programa ejecutará un bloque de código para modificar el ADN aleatoriamente.
       3. Después, se verificará nuevamente si el ADN está sano, repitiendo el proceso las veces necesarias hasta que esté **completamente sano**.
       4. Finalmente, se mostrará el ADN **sano** por pantalla.
   
     - Si el ADN **ya está sano** (condicional `False`):
       - El programa mostrará un mensaje indicando que el ADN ya está sano y no es necesario sanarlo.

#### Opción 5: **Salir**
   
   - La opción número **5** terminará la ejecución del programa.

---

> Integrantes del Grupo:

- Cercola Enzo Fernando
- Gonzalez Victor Ezequiel
- Monassa Joaquin Emiliano
- Saez Sebastian Francisco
- Trione Martin Luca
