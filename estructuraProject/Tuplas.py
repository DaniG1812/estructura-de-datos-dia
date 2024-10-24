tupla1 = ()
print(tupla1)

tupla2 = ("Una cadena", 123, 4.9, True) #Una tupla heterogenea
print(tupla2)
print(tupla2[1]) #Acceder al elemento de la tupla
print(tupla2[2])

tupla3 = (0,1,2,3)
tupla4 = ("A","B","C","D")
tupla5 = (tupla3,tupla4)
print(tupla5)
print(tupla5[1][1]) #Muestra de la tupla2 el elemento en el indice1
print(tupla5[1][0])
print(tupla5[0][3])

tupla6 = ("A","B","C","D","E")
tupla7 = (1, 2, 3, 4, 5)
tupla8 = tupla6 + tupla7 #Concatenar
print(tupla8)

#Repetir una tupla
tupla9 = (1, 2, 3, 4, 5)
tupla10 = tupla9 * 3
print(tupla10)

tupla11 = ("Rojas",)
tupla12 = (123,)
tupla13 = ("Rosas",)
tupla14 = ("rosas",)
print((tupla11,tupla12) < (tupla13,tupla14))
