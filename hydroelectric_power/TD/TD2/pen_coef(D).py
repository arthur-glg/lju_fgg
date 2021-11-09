from math import *
D=[4,4.5,5,5.5]

def coef(Dmin):
    Q=71
    H=Q
    g=9.81

    ##CHANGE OF GEOMETRY DOWNTREAM OF THE SURGETANK##
    v=5
    Ac=Q/v
    Ezoz1=0.1
    Fk=18.075123574829497
    Fc=(pi*Dmin**2)/4
    Kzoz1=(Ezoz1)/(2*g*Fk**2)*(((Fk**2)/(Fc**2))-1)

    ##HYDRAULIC GATES IN THE PENSTOCK##
    Ezoz2=0.1
    a=3.2
    Fzap=a**2
    Kzoz2=(Ezoz2)/(2*g*Fc**2)*(((Fc**2)/(Fzap**2))-1)

    ##HYDRAULIC GATES##
    Ezap=0.2
    Kzap=Ezap/(2*g*Fzap**2)

    ##CHANGE OF GEOMETRY##
    c=0.13
    Eraz1=c*(1-(Fzap/Fc))
    Kraz1=Eraz1/(2*g*Fzap**2)

    ##CHANGE OF PENSTOCK AXIS##
    def Elom(a,R):
        r=Dmin/2
        return((0.13+1.85*(r/R)**3.5)*(a/90))
    Elom1=Elom(9,50)
    Elom2=Elom(17,50)
    Klom=(Elom1+Elom2)/(2*g*Fc**2)

    ##DIVISION OG THE PENSTOCK##
    Eraz2=0.2
    Kraz2=Eraz2/(2*g*Fc**2)
    vj=7
    Qj=Q/2
    Fj=Qj/vj
    Ezoz=0.1
    Kzozj=(Ezoz/(2*g*Fc**2))*(((Fc**2)/(Fj**2))-1)
    Kzozjp=Kzozj/4

    ##TURBINE INLET VALVE##
    Elop=0.12
    Klop=Elop/(2*g*Fj**2)
    Klopp=Klop/4

    ##FRICTION LOSSES##
    Lc=160
    Lambda=0.0118
    Klin=(Lambda*Lc)/(Dmin*Fc**2*2*g)

    ##DRAFT TUBE##
    vout=1.5
    Fout=Q/vout
    Eout=2
    Kout=Eout/(2*g*Fout**2)

    return(Kzoz1+Kzoz2+Kzap+Kraz1+Klom+Kzozj+Kzozjp+Klop+Klopp+Klin+Kout)

for k in range(4):
    print(D[k])
    a=coef(D[k])
    print(a)
    print("------------------")
    
