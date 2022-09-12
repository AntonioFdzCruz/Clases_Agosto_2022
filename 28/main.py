#n1=10
#msg="Hola"

# print(n1,msg)
# print(str(n1)+msg)
# #fstrings
# print(f"{n1} {msg}")
# hacer una funcion que reciba el nombre de una persona
# el año de nacimiento y año actual retornando el mensaje
# "hola <nombre>,tienes <edad> años"

# def mensaje1(name:str,a_nacimiento:int,a_actual:int)->str: 
#  edad=a_actual - a_nacimiento
#  return f"Hola {name},tienes {edad} años"

# def mensaje2(name:str,a_nacimiento:int,a_actual:int)->str: 
#     return f"Hola {name},tienes {a_actual-a_nacimiento} años"

# def caclcular_edad(a_nacimiento:int, a_actual:int)->int:
#     return a_actual - a_nacimiento

# def mensaje3(name:str, a_nacimiento:int, a_actual:int)->str:
#     #return f"Hola {name}, tienes {calcular_edad(a_nacimiento, a_actual)} años"  
 
# if _name=="main_":
#     print(mensaje1("Alex",1980,2022))
#     res= mensaje1("Walter",1990,2022)
#     print(res)
#     print(mensaje3("Regina",2010,2022))
# alumnos = ["Hugo","Paco","Luis","Lupita"]

# print(f"Alumnos: {alumnos}")

# for i in range(4):
#     print(f"Alumos: {alumnos[i]}")
#tuplas
# alumnos = ["Hugo","Paco","Luis","Lupita"] 
# print(f"Alumnos: {alumnos}")

# for i in range(len(alumnos)):
#     print(f"Alumos {i+1}: {alumnos[i]}")
#sets
# alumnos = ["Hugo","Paco","Luis","Lupita"] 
# print(f"Alumnos: {alumnos}")

#diccionarios
# alumnos = {"nombre":"Hugo", "Materia1": 10, "Materia2": 5}
# print(f"Alumnos: {alumnos}")
# print(f"Alumno: {alumnos["nombre"]}")

# numeros_list=[1,2,1,2,3,4,3,4,3,4,3,4,3,4,3,4]
# numeros_set={1,2,1,2,3,4,3,4,3,4,3,4,3,4,3,4}
# print(numeros_list)
# print(numeros_set)

e =["nombre", "Est Dat", "Prog Func", "inglés"]
alumnos = ["Hugo", "Paco", "Luis", "Lupita"]
m_e_d=[9,7,9,8]
m_p_f=[10,8,7,9]
m_i=[6,9,7,8]

print(f"{e[0]:^10}{e[1]:^10}{e[2]:^10}{e[3]:^10}")
for i in range(len(alumnos)):
    print(f"{alumnos[i]:^10}{m_e_d[i]:^10}{m_p_f[i]:^10}{m_i[i]:^10}")

