#1._Escibir una funcion que reciba un mensaje y un nombre y escriba en pantalla "<mensaje> <nombre>
def saludar(mensaje:str, nombre:str)->str: #Asignar como valores de entrada mensaje y nombre con tipo de dato string(str) y arroje una salida de tipo string
   print(f"{mensaje} {nombre}")

#2._ Escribir una funcion que reciba el nombre y la edad de una persona. El mensaje de salida tiene
# que ser: "Hola <nombre> tienes <edad> años
def mensaje(nombre:str, edad:int)->str: #Asignar como valores de entrada nombre de tipo string y edad de tipo int y arroje una salida de tipo string
   print("Hola", (nombre), "tienes", (edad), "años")

#3._ Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior
# enviando esta como argumento obtenga el mensaje: "Hola <nombre> tienes <edad> años
def calcular_edad(año_actual:int, año_nacimiento:int, nombre:str)->str: #Asignar como valores de entrada año_actual y año_nacimiento que son tipo integer(int) y un tercer parametro nombre de tipo string el cual se usa para llamar la funcion como parametro y arroje una salida de tipo string
   edad = año_actual - año_nacimiento
   return mensaje(nombre,edad) #Llamado de la funcion calcular_edad como parametro de la funcion calcular_edad


if __name__ == "__main__":
   print("\nEscribir una funcion que reciba un mensaje y un nombre y escriba en pantalla\n<mensaje> <nombre>")
   saludar("Hola","Antonio Fernández alias 'El Niño'")
   
   print("\nEscribir una funcion que reciba el nombre y la edad de una persona. El mensaje de salida tiene que ser:\nHola <nombre> tienes <edad> años")
   mensaje("Toño", "41")
   
   print("\nEscribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior enviando\nesta como argumento obtenga el mensaje:\nHola <nombre> tienes <edad> años")
   calcular_edad(2022,1981,"Antonio")
   print('\n\n')