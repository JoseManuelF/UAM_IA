write_log(S) :- open('error_logs.txt', append, Out), write(Out, S), write(Out, '\n'), close(Out).

/***************
* EJERCICIO 1. sum_pot_prod/4
*
*	ENTRADA:
*		X: Vector de entrada de numeros de valor real.
*		Y: Vector de entrada de numeros de valor real.
*		Potencia: Numero de valor entero, potencia.
*	SALIDA:
*		Resultado: Numero de valor real resultado de la operacion sum_pot_prod. 
*
****************/
sum_pot_prod(X, Y, Potencia, Resultado) :- error_control1(X, Y, Potencia), prod(X, Y, Potencia, Resultado).

/* Error control */
error_control1(X, Y, Potencia) :- not(error_pot1(Potencia)), not(error_length1(X, Y)).

error_pot1(Potencia) :- (Potencia < 0 -> write_log('ERROR 1.1 Potencia.')).
error_length1(X, Y) :- length(X, Lx), length(Y, Ly), (Lx =\= Ly -> write_log('ERROR 1.2 Longitud.')).

/* Sum of the products powered to a number */
prod([], [], _, Sum) :- Sum is 0.
prod([H1|T1], [H2|T2], Potencia, Resultado) :- prod(T1, T2, Potencia, Sum), Resultado is (H1*H2)**Potencia + Sum.

/***************
* EJERCICIO 2. segundo_penultimo/3
*
*       ENTRADA:
*               L: Lista de entrada de numeros de valor real.
*       SALIDA:
*               X : Numero de valor real. Segundo elemento.
*		Y : Numero de valor real. Penultimo elemento.
*
****************/
segundo_penultimo(L, X, Y) :- not(error_length2(L)), calculate_second(L, X), calculate_penultimate(L, Y).

/* Error control */
error_length2(L) :- length(L, Len), (Len < 2 -> write_log('ERROR 2.1 Longitud.')).

/* We get the values of the second and penultimate position in the list */
calculate_second([_, E|_], X) :- X is E.

calculate_penultimate([E, _], Y) :- Y is E.
calculate_penultimate([_|TL], Y) :- calculate_penultimate(TL, Y).

/***************
* EJERCICIO 3. sublista/5
*
*       ENTRADA:
*		L: Lista de entrada de cadenas de texto.
*		Menor: Numero de valor entero, indice inferior.
*		Mayor: Numero de valor entero, indice superior.
*		E: Elemento, cadena de texto.
*       SALIDA:
*		Sublista: Sublista de salida de cadenas de texto.
*
****************/
/* After getting the sublist we check whether it contains the element given or not */
sublista(L, Menor, Mayor, E, Sublista) :- error_control3(L, Menor, Mayor, E), get_sublist(L, Menor, Mayor, Sublista),
                                          not(error_element3(Sublista, E)).

/* Error control */
error_control3(L, Menor, Mayor, E) :- not(error_element3(L, E)), not(error_indexes3(L, Menor, Mayor)).

error_element3(L, E) :- (not(find_element(L, E)) -> write_log('ERROR 3.1 Elemento.')).
/* Returns true if the element is found in the list */
find_element([E|_], E).
find_element([_|TL], E) :- find_element(TL, E).

error_indexes3(L, Menor, Mayor) :- length(L, Len), (((Menor > Mayor) ; (Mayor > Len)) -> write_log('ERROR 3.2 Indices.')).

/* We get the sublist with the indexes given */
get_sublist([HL|_], 1, 1, [HL]).
get_sublist([HL|TL], 1, Mayor, [HL|Sublista]) :- Mayor > 1, Index2 is Mayor - 1, get_sublist(TL, 1, Index2, Sublista).
get_sublist([_|TL], Menor, Mayor, Sublista) :- Menor > 1, Index1 is Menor - 1, Index2 is Mayor - 1,
                                               get_sublist(TL, Index1, Index2, Sublista).

/***************
* EJERCICIO 4. espacio_lineal/4
*
*       ENTRADA:
*               Menor: Numero de valor entero, valor inferior del intervalo.
*               Mayor: Numero de valor entero, valor superior del intervalo.
*               Numero_elementos: Numero de valor entero, numero de valores de la rejilla.
*       SALIDA:
*               Rejilla: Vector de numeros de valor real resultante con la rejilla.
*
****************/
/* As we get a nested list from linear_grid, we use the flatten predicate in lists for removing the extra brackets */
espacio_lineal(Menor, Mayor, Numero_elementos, Rejilla) :- error_control4(Menor, Mayor, Numero_elementos),
                                                           distance_elements(Menor, Mayor, Numero_elementos, Distance),
                                                           linear_grid(Menor, Mayor, Numero_elementos, NestedList, Distance, _),
                                                           flatten(NestedList, Rejilla).

/* Error control */
error_control4(Menor, Mayor, Numero_elementos) :- not(error_indexes4(Menor, Mayor)), not(error_npoints4(Numero_elementos)).

error_indexes4(Menor, Mayor) :- (Menor >= Mayor -> write_log('ERROR 4.1 Indices.')).
error_npoints4(Numero_elementos) :- (Numero_elementos < 2 -> write_log('ERROR 4.2 Numero Elementos.')).

/* We get the distance between the elements in the linear grid list */
distance_elements(Menor, Mayor, Numero_elementos, Distance) :- Distance is (Mayor - Menor)/(Numero_elementos - 1).

/* We calculate the linear grid with the number of points and the interval given */
linear_grid(Menor, _, 1, Menor, _, Menor).
linear_grid(Menor, Mayor, Numero_elementos, [Rejilla|[Sum]], Distance, Sum) :- Count is Numero_elementos - 1,
                                                                               linear_grid(Menor, Mayor, Count, Rejilla, Distance, CurrentValue),
                                                                               Sum is CurrentValue + Distance.

/***************
* EJERCICIO 5. normalizar/2
*
*       ENTRADA:
*		Distribucion_sin_normalizar: Vector de numeros reales de entrada. Distribucion sin normalizar.
*       SALIDA:
*		Distribucion: Vector de numeros reales de salida. Distribucion normalizada.
*
****************/
normalizar(Distribucion_sin_normalizar, Distribucion) :- print('Error. Este ejercicio no esta implementado todavia.'), !, fail.

/***************
* EJERCICIO 6. divergencia_kl/3
*
*       ENTRADA:
*		D1: Vector de numeros de valor real. Distribucion.
*		D2: Vector de numeros de valor real. Distribucion.
*       SALIDA:
*		KL: Numero de valor real. Divergencia KL.
*
****************/
divergencia_kl(D1, D2, KL) :- print('Error. Este ejercicio no esta implementado todavia.'), !, fail.

/***************
* EJERCICIO 7. producto_kronecker/3
*
*       ENTRADA:
*		Matriz_A: Matriz de numeros de valor real.
*		Matriz_B: Matriz de numeros de valor real.
*       SALIDA:
*		Matriz_bloques: Matriz de bloques (matriz de matrices) de numeros reales.
*
****************/
producto_kronecker(Matriz_A, Matriz_B, Matriz_bloques) :- print('Error. Este ejercicio no esta implementado todavia.'), !, fail.

/***************
* EJERCICIO 8a. distancia_euclidea/3
*
*       ENTRADA:
*               X1: Vector de numeros de valor real. 
*               X2: Vector de numeros de valor real.
*       SALIDA:
*               D: Numero de valor real. Distancia euclidea.
*
****************/
distancia_euclidea(X1, X2, D) :- print('Error. Este ejercicio no esta implementado todavia.'), !, fail.

/***************
* EJERCICIO 8b. calcular_distancias/3
*
*       ENTRADA:
*               X_entrenamiento: Matriz de numeros de valor real donde cada fila es una instancia representada por un vector.
*               X_test: Matriz de numeros de valor real donde cada fila es una instancia representada por un vector. Instancias sin etiquetar.
*       SALIDA:
*               Matriz_resultados: Matriz de numeros de valor real donde cada fila es un vector con la distancia de un punto de test al conjunto de entrenamiento X_entrenamiento.
*
****************/
calcular_distancias(X_entrenamiento, X_test, Matriz_resultados) :- print('Error. Este ejercicio no esta implementado todavia.'), !, fail.

/***************
* EJERCICIO 8c. predecir_etiquetas/4
*
*       ENTRADA:
*               Y_entrenamiento: Vector de valores alfanumericos de una distribucion categorica. Cada etiqueta corresponde a una instancia de X_entrenamiento.
*               K: Numero de valor entero.
*               Matriz_resultados: Matriz de numeros de valor real donde cada fila es un vector con la distancia de un punto de test al conjunto de entrenamiento X_entrenamiento.
*       SALIDA:
*               Y_test: Vector de valores alfanumericos de una distribucion categorica. Cada etiqueta corresponde a una instancia de X_test.
*
****************/
predecir_etiquetas(Y_entrenamiento, K, Matriz_resultados, Y_test) :- print('Error. Este ejercicio no esta implementado todavia.'), !, fail.

/***************
* EJERCICIO 8d. predecir_etiqueta/4
*
*       ENTRADA:
*               Y_entrenamiento: Vector de valores alfanumericos de una distribucion categorica. Cada etiqueta corresponde a una instancia de X_entrenamiento.
*               K: Numero de valor entero.
*               Vec_distancias: Vector de valores reales correspondiente a una fila de Matriz_resultados.
*       SALIDA:
*               Etiqueta: Elemento de valor alfanumerico.
*
****************/
predecir_etiqueta(Y_entrenamiento, K, Vec_distancias, Etiqueta) :- print('Error. Este ejercicio no esta implementado todavia.'), !, fail.

/***************
* EJERCICIO 8e. calcular_K_etiquetas_mas_relevantes/4
*
*       ENTRADA:
*               Y_entrenamiento: Vector de valores alfanumericos de una distribucion categorica. Cada etiqueta corresponde a una instancia de X_entrenamiento.
*               K: Numero de valor entero.
*               Vec_distancias: Vector de valores reales correspondiente a una fila de Matriz_resultados.
*       SALIDA:
*		K_etiquetas: Vector de valores alfanumericos de una distribucion categorica.
*
****************/
calcular_K_etiquetas_mas_relevantes(Y_entrenamiento, K, Vec_distancias, K_etiquetas) :- print('Error. Este ejercicio no esta implementado todavia.'), !, fail.

/***************
* EJERCICIO 8f. calcular_etiqueta_mas_relevante/2
*
*       ENTRADA:
*               K_etiquetas: Vector de valores alfanumericos de una distribucion categorica.
*       SALIDA:
*               Etiqueta: Elemento de valor alfanumerico.
*
****************/
calcular_etiqueta_mas_relevante(K_etiquetas, Etiqueta) :- print('Error. Este ejercicio no esta implementado todavia.'), !, fail.

/***************
* EJERCICIO 8g. k_vecinos_proximos/5
*
*       ENTRADA:
*		X_entrenamiento: Matriz de numeros de valor real donde cada fila es una instancia representada por un vector.
*		Y_entrenamiento: Vector de valores alfanumericos de una distribucion categorica. Cada etiqueta corresponde a una instancia de X_entrenamiento.
*		K: Numero de valor entero.
*		X_test: Matriz de numeros de valor real donde cada fila es una instancia representada por un vector. Instancias sin etiquetar.
*       SALIDA:
*		Y_test: Vector de valores alfanumericos de una distribucion categorica. Cada etiqueta corresponde a una instancia de X_test.
*
****************/
k_vecinos_proximos(X_entrenamiento, Y_entrenamiento, K, X_test, Y_test) :- print('Error. Este ejercicio no esta implementado todavia.'), !, fail.
