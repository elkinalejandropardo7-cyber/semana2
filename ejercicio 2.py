#Validación de Clave Fija: Solicitar al usuario una contraseña numérica (ej. 1234). Mientras la clave ingresada sea incorrecta, el sistema debe mostrar un mensaje de error y volver a pedirla. Al acertar, debe mostrar un mensaje de bienvenida.

while True :
  print ("--/ Validación de contraseña ")
  contraseñagu = "Eduar1"
  contraseña = input (" Digite la contraseña ")
  if contraseña != contraseñagu:
    print ( "contraseña incorrecta vuelva a intentarlo ")
  
  else : 
    print ("contraseña correcta puede ingresar al sistema ")
    break