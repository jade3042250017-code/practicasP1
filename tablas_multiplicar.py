'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''


print("\033c")

def tabla(num_tab,n):
    mul=num_tab*n
    print(f"{num_tab} x {n}  = {mul} ")
    n+=1
    return n
  
num_tabla=int(input("Dame un numero para obtener la tabla de multiplicar:  "))

for num in range(1,11):
  num=tabla(num_tabla,num)








