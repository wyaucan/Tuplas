"""
Ejercicio 3
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura,
y después las muestre por pantalla con el mensaje
En <asignatura> has sacado <nota> donde <asignatura> 
es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
notas introducidas por el usuario.
"""

tupla = ('Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lengua')

tupla2=[]
for a in tupla:
    nota = int(input('Tu nota obetenida en '+a+' es: '))
    tupla2 = tupla2 + [nota]
for b in range(len(tupla)):
    print('En',tupla[b], 'has sacado',tupla2[b])


    