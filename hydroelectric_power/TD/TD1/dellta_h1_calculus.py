from math import *

'''Declaration of variables'''
Q=71
g=9.81
Evt=0.5
Fvt=71
Chi=1
Beta=1
s=10*10**(-3)
l=50*10**(-3)
alpha=1.22
Eres=Chi*Beta*((s/l)**(4/3))*sin(alpha)
Fres=Fvt
D=0.62*Q**(0.46)
Fzap=D**2
Ezoz=0.365
Ezap=0.1
Fk=(pi*D**2)/4
r=D/2
def Elom(a,R):
    return((0.13+1.85*(r/R)**3.5)*(a/90))
Elom1=Elom(90,70)
Elom2=Elom(47,110)
Elom3=Elom(16,150)
Elom4=Elom(25,150)


'''Calculus
#Doing it step by step to avoid mistakes
Dh1 = (Evt/Fvt**2)+(Eres/Fres**2)+((Ezoz/Fres**2)*((Fres**2/Fzap**2)-1))    #1
Dh1 = Dh1 + ((Ezap/Fzap**2)*((Fzap**2/Fk**2)-1))    #2
Dh1 = Dh1 + (Elom1+Elom2+Elom3+Elom4)/(Fk**2)   #3
Dh1 = Dh1 + (Lambda*Lk/D)*(1/Fk**2) #4
Dh1 = Dh1 + (Evt/Fk**2)
Dh1 = ((Q**2)/(2*g))*Dh1
print(Dh1)
'''
