from unittest import result


def cuadrado(a:int)->int: #Se crea una funcion que pide como parametro un dato ya sea de tipo integer(int) o flotante(float) y su salida sera un valor ya sea tipo int o float
    operacion=(a*a)
    return cuadrado(a,operacion) #La funcion devuelve el resultado de multiplicar el dato por si mismo, es decir elevar al cuadrado

def cuadrado2(a:int)->int:
    return {a*a}

#Example:
a:int=input('Ingresa un número entero ->')
b:int=a**2
c:int=pow(a,2)

if __name__ == "__main__":
#    print (f'{cuadrado(a)}')
    print (c)
    print (b)
    print (f'{cuadrado2(a)}')
    