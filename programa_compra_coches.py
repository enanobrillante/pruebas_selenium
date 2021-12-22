''' Ejercicio clase abierta 4: 
Dado el problema anterior:
1-Ya no se sabe la cantidad de clientes que ingresaran al sistema.
2-Si el pedido no es uno de los autos en venta, debe volver a preguntar.
3-Lo mismo para la cantidad de puertas y colores.
4-Si la cantidad de clientes fue:
    0 a 5 personas: no hay descuento
    6 a 10 personas: hay un descuento del 10%
    11 a 50 pesronas: descuento del 15%
    mas de 50 personas: descuento del 18 %

5-Solo se va a mostrar que fue vendido al final del programa, con  el precio y el nombre del comprador
&- al final se pregunta si otro cliente desea seguir comprando, sino finaliza el programa.

'''
fin_programa = False




def calcular_precio(marca,cant_puertas,color,cant_ventas):
    marcas = {'ford':10000,'chev':12000,'fiat':8000}
    colores = {'blanco':1000,'azul':2000,'negro':3000}
    puertas = {'2':500,'3':650,'5':870}  

    precio = marcas[marca] + colores[color] + puertas[cant_puertas]
    if cant_ventas <= 1:
        print("No corresponde descuento.")
    elif cant_ventas >= 2 and cant_ventas <= 3:
        #print("Se le aplica un descuento del 10%")
        precio = precio - (precio * 0.10)
    elif  cant_ventas >= 4 and cant_ventas <= 10:
        #print("Se le aplica un descuento del 15%")
        precio = precio - (precio * 0.15)
    elif cant_ventas >= 11 and cant_ventas <= 20:
        #print("Se le aplica un descuento del 18%")
        precio = precio - (precio * 0.18)
    
    return precio    

lista_ventas = []    
lista_puerta = ["2","3","5"]
lista_marca = ["ford","chev","fiat"]
lista_color = ["blanco","azul","negro"]

while fin_programa == False:
      
    
    nombre = input("Ingrese nombre: ").lower()
    apellido = input("Ingrese Apellido: ").lower()
    marca = input("Ingrese marca ford, chev o fiat ").lower()

    

    
    while marca not in lista_marca :
        print("Marca incorrecta, vuelva a seleccionar una marca: ")
        marca = input("Ingrese marca ford, chev o fiat ").lower()
           
    
         
    puertas = input("Ingrese cantidad de puertas, 2, 3 o 5: ")
    
    
    while puertas not in lista_puerta:
        print("Cantidad de puertas incorrecta.")
        puertas = input("Ingrese cantidad de puertas, 2, 3 o 5: ")
           
        
    

    color = input("Ingrese color: blanco, azul o negro ").lower()

    
    while color not in lista_color:
        print("El color es incorrecto.")
        color = input("Ingrese color: blanco, azul o negro: ").lower()
        
                
      

    

    


    #creamos un diccionario para guardar cada venta

    venta = {'nombre': nombre, 'apellido':apellido, 'marca':marca, 'puertas':puertas, 'color':color }

    #agrego el diccionario a la lista de vantas

    lista_ventas.append(venta)
    cant_ventas = len(lista_ventas)   

    precio_final = calcular_precio(marca,puertas,color,cant_ventas)

    fin= input("Quiere agregar un nuevo cliente?\n Escriba 'si', para agregar nuevo cliente o 'no' para finalizar el programa: ")
    if fin == "si":
        fin_programa = False 
    else:
        fin_programa = True
        




for ventas in lista_ventas:
    
     

    print(f"El cliente {ventas['nombre']} {ventas['apellido']} compró un auto marca {ventas['marca']} con {ventas['puertas']} puertas , de color {ventas['color']} a un precio final de {precio_final}.")