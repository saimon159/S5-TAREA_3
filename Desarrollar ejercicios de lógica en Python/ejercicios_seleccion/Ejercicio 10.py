#Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se dicta el nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los jueves son para práctica hablada y los viernes se dicta inglés para viajeros.
#Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato "día, DD/MM", donde [día] es un día de la semana, DD es el número de día y MM es el número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo día supere el número 31 o el mes supere el número 12, finalizar el programa indicando que se produjo un error. Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
#Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, pero eso sólo si se trata de los niveles inicial, intermedio o avanzado, ya que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el programa le mostrará el porcentaje de aprobados.
#Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a clase y el programa le indicará "asistió la mayoría" en caso de que la asistencia sea mayor al 50% o "no asistió la mayoría" si no es así.
#Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir "Comienzo de nuevo ciclo" y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego imprimir el ingreso total en $.


fecha=input("Fecha (formato 'día, DD/MM'): ")
fecha=fecha.lower()
diasemana=fecha[0:fecha.find(',')]
dianro=int(fecha[fecha.find(',')+2:fecha.find('/')])
mesnro=int(fecha[fecha.find('/')+1:])
if dianro>31 or mesnro>12:
    print("Fecha incorrecta")
else:
    if diasemana in "lunes,martes,miércoles":
        respuesta=input("¿Se tomaron exámenes? S/N: ")
        if respuesta.lower()=="s":
            aprobados=int(input("Cantidad de aprobados: "))
            reprobados=int(input("Cantidad de reprobados: "))
            print("Porcentaje de aprobados:", (aprobados*100)/(aprobados+reprobados), "%")
    elif diasemana=="jueves":
        asistencia=int(input("Porcentaje de asistencia: "))
        if asistencia>50:
            print("Asistió la mayoría")
        else:
            print("No asistió la mayoría")
    elif diasemana=="viernes":
        if dianro==1 and (mesnro==1 or mesnro==7):
            print("Nuevo ciclo")
            alumnos=int(input("Cantidad de alumnos: "))
            arancel=float(input("Arancel: $"))
            print("Ingreso total: $", alumnos*arancel)
    else:
        print("Fecha incorrecta")
print("Fin del programa")