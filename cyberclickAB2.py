
import pandas as pd

#PREPARACION DE LOS DATOS

#Abro el archivo "input" usando su "path" en mi PC
arxiu=pd.read_csv(r"C:\Users\Usuari\Desktop\PYTHON\CyberClick\input.txt", sep="\s+", header=None, engine="python")

#Defino los encabezamientos para cada columna
arxiu.columns=["min-max","lletra","password"]

#Separo la columna min-max en una columna min y otra max
arxiu[["min","max"]] = arxiu["min-max"].str.split("-",expand=True)

#Defino los nuevos encabezamientos
arxiu.columns=["min-max","lletra","password","min","max"]

#Elimino los ":" de la columna "lletra"
arxiu["lletra"] = arxiu["lletra"].str.replace(":","")

#Transformo las columnas en listas
llistapassword=arxiu["password"].tolist()
llistalletra=arxiu["lletra"].tolist()
llistamin=arxiu["min"].tolist()
llistamax=arxiu["max"].tolist()

#Transformo las listas de minimos y maximos (strings) a listas de valores enteros
llistamin = [int(n) for n in llistamin]
llistamax = [int(n) for n in llistamax]

#Creo la lista que contendra las validaciones para cada password True=correcta y False=incorrecta
#segun cada politica, por defecto False
llistavalidacio1=[False]*len(llistapassword)
llistavalidacio2=[False]*len(llistapassword)





#EVALUACION DE PASSWORDS SEGUN POLITICA 1

#Defino la función que valida (True/False) segun las condiciones de la politica 1
def validacion1(password,lletra,min1,max1):

    if password.count(lletra)>=min1 and password.count(lletra)<=max1:
        
        validacion1=True
        
    else:
        
        validacion1=False        

    return validacion1

#Recorro la lista de password validando con la funcion "validacion1" cada posicion
for i in range(len(llistapassword)):

        llistavalidacio1[i]=validacion1(llistapassword[i],llistalletra[i],llistamin[i],llistamax[i])
    
#Recuento de passwords correctos e incorrectos segun la politica 1
passwordscorrectes1=llistavalidacio1.count(True)
passwordsincorrectes1=llistavalidacio1.count(False)

#Muestro por pantalla los passwords correctos e incorrectos según la politica 1
print("Passwords correctos según politica 1:", passwordscorrectes1, "Passwords incorrectos según politica 1:", passwordsincorrectes1)





#EVALUACION DE PASSWORDS SEGUN POLITICA 2

#Defino la funcion que valida (True/False) según las condiciones de la política 2
def validacion2(password,lletra,pos1,pos2):

    password=list(password)



    if password[pos1-1]==lletra and password[pos2-1]==lletra:

        validacion2=False
            
    elif password[pos1-1]==lletra and password[pos2-1]!=lletra:
            
        validacion2=True
            
    elif password[pos1-1]!=lletra and password[pos2-1]==lletra:

        validacion2=True
            
    else:

        validacion2=False
            
    return validacion2

#Recorro la lista de passwords validando con la funcion "validacion2" cada posicion
for i in range(len(llistapassword)):

    llistavalidacio2[i]=validacion2(llistapassword[i],llistalletra[i],llistamin[i],llistamax[i])

#Recuento de passwords correctos e incorrectos segun la politica 2
passwordscorrectes2=llistavalidacio2.count(True)
passwordsincorrectes2=llistavalidacio2.count(False)

#Muestro por pantalla los passwords correctos e incorrectos según la politica 2
print("Passwords correctos según politica 2:", passwordscorrectes2, "Passwords incorrectos según politica 2:", passwordsincorrectes2)

#Muestro en pantalla las filas y columnas del archivo original para comprovar que no me he dejado ningún valor
print(arxiu.shape)

    

        
    




    
