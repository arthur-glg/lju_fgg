from math import *
##Initialisation
Q=70
g=9.81
H0=65
P=9.2
C=(Q**2)/(2*g*(H0-P))
Ein=0.5
Etrash=0.26
Egates=0.1
Eout=2
Lambda=0.02
Lp=49.61
D=4
print(D)
##Loop to iterate
for k in range(10):
    F=sqrt(C*(Ein+Etrash+Egates+Eout+1+((Lambda*Lp)/(D))))
    D=sqrt(F)
    print(D)
    
