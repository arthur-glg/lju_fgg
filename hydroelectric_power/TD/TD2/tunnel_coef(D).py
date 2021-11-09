from math import *
D=[4,4.5,5,5.5,6]

def coef(D):
    Q=71
    g=9.81

    #INTAKE
    Evt=0.5
    Fvt=71
    Kvt=Evt/(2*g*Fvt**2)

    #TRASHRACKS
    Chi=1
    Beta=2.42
    s=10*10**(-3)
    l=50*10**(-3)
    alpha=70
    Eres=Chi*Beta*((s/l)**(4/3))*sin(alpha)
    Fres=Fvt
    Kres=Eres/(2*g*Fres**2)

    #NARROWING OF THE TUNNEL
    Fzap=D**2
    Ezoz=0.34
    Kzoz=(Ezoz/(2*g*Fres**2))*((Fres**2/Fzap**2)-1)

    #MAIN HYDRAULIC GATES
    Ezap=0.1
    Kzap=Ezap/(2*g*Fzap**2)

    #CHANGE OF GEOMETRY
    Fk=(pi*D**2)/4
    r=D/2
    Etran=0.11
    Ktran=(Etran/(2*g*Fzap**2))*(Fzap**2/Fk**2-1)

    #CURVATURE OF THE TUNNEL AXIS
    def Elom(a,R):
        return((0.13+1.85*(r/R)**3.5)*(a/90))
    Elom1=Elom(90,70)
    Elom2=Elom(47,110)
    Elom3=Elom(16,150)
    Elom4=Elom(25,150)
    Klom=(Elom1+Elom2+Elom3+Elom4)/(2*g*Fk**2)

    #SURGE TANK
    Est=0.1
    Kst=Est/(2*g*Fk**2)

    #FRICTION LOSS
    ng=0.0013
    Lambda=0.012
    Lk=2600
    Klin=(Lambda*Lk)/((Fk**2)*D*2*g)

    return(Kvt+Kres+Kzoz+Kzap+Klom+Klom+Kst+Klin)

for k in range(5):
    print(D[k])
    a=coef(D[k])
    print(a)
    print("------------------")
