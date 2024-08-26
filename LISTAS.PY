m=int(input())
while(m!=0 or p!=5):
    if (m==1):
        print("Diga que opcion del menu quiere realizar: \n1-Crear persona.\n2-Eliminar persona.\n3-Lista de personas. \n4-Buscar persona.")
        p =int(input())
        if(p==1):
            lista1=list()
            print("colocale un valor al listado: ")
            lista1.append(input())
            print (lista1)
            
        elif(p==2):
            lista2=list()
            lista2.append ("yan")
            lista2.append ("suarez")
            lista2.append ("james")
            lista2.append ("paolo")
            print("Elimina el valor del menu(recuerde que debe escribir de la misma manera que esta en el menu):",lista2,"teniendo en cuenta que estan enumerados del 0 al 3")
            lista2.remove(int(input()))
            print (lista2)
            
        elif(p==3):
            lista3=list()
            lista3.append ("yan")
            lista3.append ("suarez")
            lista3.append ("james")
            lista3.append ("paolo") 
            print(lista3)
            
        elif(p==4):
            lista4=list()
            lista4.append ("yan")
            lista4.append ("suarez")
            lista4.append ("james")
            lista4.append ("paolo")
            print(lista4)
            if input() in lista4:
                print("El elemento que ingresaste se encuentra dentro del menu")
            else:    
                print("El elemento que ingresaste no se encuentra en el menu")  
    elif(m==2):
            break

