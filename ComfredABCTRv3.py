
#***************************************
#THERMAL FLOOR-ADRIÀ BONJORN CERVERA****
#***************************************

#This code pretends to give an orientative guide to sizing a thermal floor
#from the data introduced by the user.
#Feneral questions are asked to the user and lets him choose different
#variables for the calculus.



#Import "ceil" from the library "math"

from math import ceil


print("\n----------------------------------------")
print("THERMAL FLOOR CALCULUS - Adrià Bonjorn")
print("----------------------------------------\n")


#FUNCTION SECTION----------------------------------------------------------------------------


#Erro message
nv="***This value is not valid!***"

#Defining "eval1" function that validates the values entered by user in multi-type selection
def eval1(va,txt,nv):
    ve=int(input(txt))
    while ve not in va:        
        print(nv)        
        ve=int(input(txt))        
    return ve

#Arguments for "eval1" function"
vaCanviVarCal1=(1,2)
txtCanviVarCal1="Do you want to change any variable? Yes(1) / No(2)"
vaCanviVarCal2=(1,2,3,4,5,6,7)
txtCanviVarCal2="Which variable do you want to change? Select a number from (1) to (7)"
vaCanviVarCal3=(1,2)
txtCanviVarCal3="Do you want to change another variable? Yes(1) / No(2)\n"
txtPlantaSales="In wich floor is this room?"
vaPreguntaPerimetre=(1,2)
txtPreguntaPerimetre="Do you want to introduce the perimeter for each room? Yes(1) / No(2)\n"
vaResultatSales=(1,2)
txtResultatSales="Do you want to see the results for each room? Yes(1) / No(2)\n"

#Defining "eval2" function that validates that the integer values entered by user are positive and different from zero
def eval2(txt,nv):
    ve=int(input(txt))
    while ve <=0:
        print(nv)        
        ve=int(input(txt))        
    return ve


#Defining "eval3" function that validates that the float values entered by user are positive and different from zero
def eval3(txt,nv):
    ve=float(input(txt))
    while ve <= 0:        
        print(nv)        
        ve=float(input(txt))        
    return ve

#Arguments for "eval2" and "eval3" functions
txtvarcalval="Introduce new value:"
txtNumSales="Introduce the total number of rooms:"



#Defining "eval3" function that validates that the float values for room areas entered by user are positive and different from zero
def eval4(txt,i,nv):
    print(txt, i,":")
    ve=float(input())
    while ve <=0:
        print(nv)
        print(txt, i, ":")
        ve=int(input())        
    return ve

#Arguments for "eval4" function"
txtSupSales="Introduece area of the room"
txtPerimetre="Introduece perimeter of the room"



#CONFIGURATION SECTION----------------------------------------------------------------------------


#Introducing list of variables for the calculus. varcalnom=names and varcalval=values (default values)

varcalnom=["(1)Approximate thermal power [W/m2]","(2)Area of a plate [m2]",
           "(3)oversizing[%]","(4)Lenght of pipe per circuit [m]",
           "(5)Thermal differential [ºC]","(6)Area covered by a circuit [m2]",
           "(7)Nº of floors [-]"]

varcalval=[100,1.17,20,100,5,9,1]

print("The calculus variables and its default values are:")

for i in range(len(varcalval)):
    
    print(varcalnom[i], ":", varcalval[i])

print("\n")

#Modification of calculus variables by the user (if user decides to)
CanviVarCal=eval1(vaCanviVarCal1,txtCanviVarCal1,nv)

while CanviVarCal==1:

    CanviVarCalpos=eval1(vaCanviVarCal2,txtCanviVarCal2,nv)

    if CanviVarCalpos==7:
        print("Remember that the number of floors must be an integer, not a float point number!")
        varcalval[CanviVarCalpos-1]=eval2(txtvarcalval,nv)

    else:    
        varcalval[CanviVarCalpos-1]=eval3(txtvarcalval,nv)

    CanviVarCal=eval1(vaCanviVarCal3,txtCanviVarCal3,nv)

#USER INTERACTION SECTION----------------------------------------------------------------------------


#vaNumPlanta are the values acceptable as floor number: 1,2,3... until default number of floors or the one decided by user
vaNumPlanta=range(1,varcalval[6]+1)

print("\n----------------------------------------")


#Creating the lists that will contain de data and results for the calculus
NumSales=eval2(txtNumSales,nv)
SupSales=[0]*NumSales
PlantaSales=[0]*NumSales



#Introducing the area of each room and the floor where they are (only if number of floors different from 1)

PreguntaPerimetre=eval1(vaPreguntaPerimetre,txtPreguntaPerimetre,nv)


for i in range(NumSales):

    SupSales[i]=eval4(txtSupSales,i+1,nv)

    if PreguntaPerimetre==1:
        Perimetre[i]=eval4(txtPerimetre,i+1,nv)

    if varcalval[6]!=1:
        PlantaSales[i]=eval1(vaNumPlanta,txtPlantaSales,nv)
    else:
        PlantaSales[i]=1

print("\n----------------------------------------")

#CALCULUS SECTION----------------------------------------------------------------------------



#Lists that will contain the results for each room
CircuitsSales=[0]*NumSales
TubSales=[0]*NumSales
PlaquesSales=[0]*NumSales
Perimetre=[0]*NumSales
BandaPerimetral=[0]*NumSales
PotenciaSales=[0]*NumSales
CabalSales=[0]*NumSales
Vies=[0]*varcalval[6]

#Calculus for each room
for i in range(NumSales):

    CircuitsSales[i]=ceil(SupSales[i]/varcalval[5])
    TubSales[i]=(CircuitsSales[i]*varcalval[3])/(1-varcalval[2]/100)
    PlaquesSales[i]=(SupSales[i]/varcalval[1])/(1-varcalval[2]/100)
    BandaPerimetral[i]=Perimetre[i]/(1-varcalval[2]/100)
    PotenciaSales[i]=SupSales[i]*varcalval[0]
    CabalSales[i]=((PotenciaSales[i]*60)/(varcalval[4]*4.18*1000))*0.06

    for ii in range(varcalval[6]):
        
        if PlantaSales[i]==ii+1:
            
            Vies[ii]+=CircuitsSales[i]



print("\n----------------------------------------")

print("General results:")
print("Total pipe length [m]", sum(TubSales))
print("Total number of plates[-]", sum(PlaquesSales))

if PreguntaPerimetre==1:
    print("Total perimetral band [m]", sum(BandaPerimetral))
print("Total number of circuits [-]", sum(CircuitsSales))

for i in range(varcalval[6]):
    print("    Connections needed in the collectors of floor", i+1, ":", Vies[i])

print("Total power [kW]", sum(PotenciaSales)/1000)
print("Total water flow [m3/h]", sum(CabalSales))
print("\n")


    

ResultatSales=eval1(vaResultatSales,txtResultatSales,nv)

if ResultatSales==1:

    print("\n----------------------------------------")

    print("Results for each room:\n")

    for i in range(NumSales):

        print("Room", i+1, ":")
        print("     Pipe [m]", TubSales[i])
        print("     Plates [-]", PlaquesSales[i])
        
        if PreguntaPerimetre==1:
            print("     Perimetral band [m]", BandaPerimetral[i])
        
        print("     Nº of circuits [-]", CircuitsSales[i])
        
        print("     Power [kW]", PotenciaSales[i]/1000)
        print("     Water flow [m3/h]", CabalSales[i])
        print("\n")




    




