'''Finding measurement'''
H=71
m=0.8
B=m*H
b0=H/10
if b0<=8:
    b0=8
h0=b0/m
'''Load combination'''
#dead load
gconc=24
H0=H-6
G1=b0*H*gconc
G2=0.5*(B-b0)*(H-h0)*gconc
rG1=B-(b0/2)
rG2=(2/3)*(B-b0)
#hydrostatic pressure
gw=10
Pw=gw*0.5*H0*H0
rw=(1/3)*H0
#uplift pressure
gamma=0.85
Pu=gamma*H0*gw*B/2
ru=(2/3)*B
#silt pressure
gs=18
Hs=H0/3
Ps=gs*0.5*Hs*Hs
rs=Hs/3
#earthquake forces
a=9.81*0.1
Sv1=a*G1
Sv2=a*G2
Sh1=(2/3)*a*G1
Sh2=(2/3)*a*G2

'''security factors check'''
nsl=(G1+G2-Pu-Sv1-Sv2)/(Pw-Ps-Sh1-Sh2)
print("nsl=",nsl)
nov=((G1+Sv1)*rG1+(G2+Sv2)*rG2)/(Pw*rw+Ps*rs+Pu*ru+Sh1*rG1+Sh2*rG2)
print("nov=",nov)
