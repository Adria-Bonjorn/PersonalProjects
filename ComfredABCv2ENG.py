#CODE FOR HVAC MACHINE SELECTION****By: Adrià Bonjorn Cervera - July 2021

#Import function "ceil" from library "math"

from math import ceil

print("\n----------------------------------------")
print("AIR CONDITIONING MACHINE SELECTION - Adrià Bonjorn")
print("----------------------------------------\n")

#--------------------------------------------------------------------------------
#This program is meant to be a practice project applied to a necessity in my current job.
#The main idea is to develop a simple set of algorithms that allows AC machine selection
#(based on some of my own empirical coeficients) for non technical staff in order to improve
#client atention and productivity in my current company, an AC distributor (Comfred Suministros)
#--------------------------------------------------------------------------------

#Initialize variables
ti=0 #Type of machine
ns=0 #Number of rooms to air-condition
tf=0 #Mode of use
cf=0 #Coeficient due to the mode of use
ta=0 #Type of insulation
ca=0 #Coeficient due to the type of insulation
st=0  #Total area to air-condition
ss=[]  #Area of each room to air-condition. It's a list
ssa=0 #Auxiliar variable to check validity of entered areas.


#EVALUATION SETTING SECTION--------------------------------------------------------------------------------

#Evaluation functions and variables to check user inputs

#Main error message
nv="This value is not valid!"

#Defining the function "eval" that checks the validity of the integer values entered in the selection inputs
def eval(va,txt,nv):
    ve=int(input(txt))
    while ve not in va:        
        print(nv)        
        ve=int(input(txt))        
    return ve

#Setting the arguments that function "eval" is going to use to evaluate and ask for inputs
vati=(1,2)
txtti="Select type of machine Split(1) o Ceiling Duct(2):"
vatf=(1,2,3)
txttf="Select mode of use cooling(1), heating(2) o cooling+heating(3):"
vata=(1,2,3)
txtta="Select type of insulation Good(1), Standard(2) o Poor(3):"

#Defining the function "eval2" that checks if the integer entered is positive
def eval2(txt,nv):
    ve=int(input(txt))
    while ve <=0:
        print(nv)        
        ve=int(input(txt))        
    return ve

#Defining the function "eval3" that checks if the float entered is positive
def eval3(txt,nv):
    ve=float(input(txt))
    while ve <=0:
        print(nv)        
        ve=float(input(txt))        
    return ve

#Setting the arguments that functions "eval2" and "eval3" is going to use to evaluate and ask for inputs
txtns="Introduce the number of rooms to air-condition:"
txtq="Introduce air flow of the selected model of machine(m3/h):\n"
txth="Introduce maximum heigh of the grills (mm):\n"
txtv="Introduce exit air velocity at grills (m/s): \n"
txtst="Introduce area to air-condition:"

#Defining the function "eval4" that checks the validity of areas for each room
def eval4(txt,i,nv):
    print(txt, i,":")
    ve=int(input())
    while ve <=0:
        print(nv)        
        ve=int(input(txt, i, ":"))        
    return ve

#Setting the arguments that function "eval4" is going to use to evaluate and ask for inputs
txtssa="Introduce area to air-condition:"

#USER INTERACTION SECTION--------------------------------------------------------------------------------

#User interaction loop starts

while True:
    #Selecting type of machine Split(1) o Ceiling Duct(2)
    ti=eval(vati,txtti,nv)

    #Selecting mode of use cooling(1), heating(2) o cooling+heating(3)
    tf=eval(vatf,txttf,nv)
           
    #Selecting type of insulation Good(1), Standard(2) o Poor(3)
    ta=eval(vata,txtta,nv)


    #Introducing area to air-condition. For Ceiling Duct(2) user should introduce various values
    if ti==2:
        ns=eval2(txtns,nv)           
        ss=[0]*ns
        for i in range(ns):
            ssa=eval4(txtssa,i+1,nv)
            ss[i]=ssa        
        st=sum(ss)    
    else:
        st=eval2(txtst,nv)


    #CALCULUS AND OUTPUT SECTION--------------------------------------------------------------------------------
        
        
    #Assigning coeficient due to the mode of use
    if tf==1:
        cf=1.1
    else:
        cf=1.2

    #Assigning coeficient due to the type of insulation
    if ta==1:
        ca=1
    elif ta==2:
        ca=1.1    
    else:
        ca=1.2

    #Recommended machine power calculus
    pr=st*cf*ca/10
    print("The recommended cooling/heating power is:", pr, "kW\n")

    #Grill sizeing
    if ti==2:
        
        #Introducing variables for grill sizeing calculus
        q=eval2(txtq,nv)    
        v=eval3(txtv,nv)    
        h=eval2(txth,nv)

        #Preparing grill sizeing variables for calculus
        q=q/3600
        rh=[h]*ns
        rw=[0]*ns
        qr=[0]*ns

        #Grill sizeing calculus
        for i in range(1,ns+1):
            rh[i-1]=h        
            rw[i-1]=1000*q*(ss[i-1]/st)/v/(h/1000)        
            rw[i-1]=ceil(rw[i-1]/50)*50
            qr[i-1]=q*(ss[i-1]/st)*3600
            print("Grill for room", i, ":", rw[i-1], "x", rh[i-1],"--->", qr[i-1], "m3/h")

            
    if input('Select another AC machine(1) /// Exit(2)') == '2':
        break
            
    

