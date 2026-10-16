# Validación de Nota Positiva: Solicitar una calificación numérica entre 0.0 y 5.0. El algoritmo no debe permitir avanzar hasta que la nota ingresada se encuentre dentro de ese rango válido.

while True :
 print (" sistema de notas ")
 nota = float(input("ingrese su nota de 0 a 5")) 
 if nota>=0 and nota<=5 :
  print (" Nota aceptada puede avanzar ")
  break

 else : 
  print(" nota no valida")