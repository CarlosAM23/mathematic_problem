print("Si tu edad actual es el doble de lo que tu hermana tenía hace 5 años, y la edad de tu hermana "
    + "\ndentro de 5 años será el triple de la de tu hermano que acaba de cumplir 5 años. ¿Cuántos tendré dentro de 6 años?")

question_answer = int(input("¿Quieres obtener la respuesta de la pregunta? escribe \"1\" si sí, o escribe \"0\" si no: "))
hermano = 5
hermana = hermano*3 - 5
yo = 2*(hermana - 5)
answer = yo + 6

hermana = str(hermana)
hermano = str(hermano)
yo = str(yo)
answer = str(answer)

solution = str("Partimos por el dato concreto que nos dan, que es la edad del hermano, éste tiene " + hermano + " años "
        + "\na éste le otorgaremos la variable \"a\", a su hermana la variable \"b\" el cual "
        + "\nsegún el enunciado se traduciría en la siguiente ecuación: \nb + 5 = a * 3 \nDespejando "
        + "obtendríamos:\nb=(a * 3) - 5\nEntonces reemplazando valores y resolviendo la ecuación "
        + "tendríamos que:\nb=(" + hermano + " * 3) - 5 \nb = " + hermana + "\nLuego se enuncia que mi edad es el doble de lo que mi hermana tenía hace 5 años, "
        + "aquí se me otorgará la variable \"c\" por lo que tendremos la siguiente escuación:"
        + "\nc = 2 * (b - 5)" + "\nPero como conocemos el valor de b = " + hermana + " entonces solo nos quedaría reemplazar "
        + "\ny efectuar la ecuación:" + "\nc = 2 * (" + hermana + " - 5)" + "\nc = " + yo + "\nNos piden cuántos años tendría dentro de 6 años por lo que reemplazando y resolviendo:"
        + "\nc + 6 = " + answer + " años")

if  question_answer == 1:
    print(answer)
elif question_answer == 0:
    print("Está bien, resuévelo tú mismo")
else:
    print("Escoge una de las dos opciones")

question_solution = int(input("¿Quieres la solución? escribe \"1\" si sí, o escribe \"0\" si no: "))

if  question_solution == 1:
    print(solution)
elif question_solution == 0:
    print("Está bien, halla la solución por ti mismo")
else:
    print("Escoge una de las dos opciones")
