# <center>Design of a reservoir hydropower scheme</center>

<center><b>Arthur Guillot - Le Goff</b> </center> 

<center><b>Autumn semester 2021-2022 | Hydroelectric power</b> </center> 

------

[TOC]

------

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD1\images\fond.png)

<div style="page-break-after: always; break-after: page;"></div>

## Task 1: Determine the design of a gravity dam, height H to satisfy safety factors against sliding and overturning.

### Finding measurement

![Introduction to notations for the gravity dam measurements](D:/lju_fgg/lju_fgg/hydroelectric_power/TD/TD1/images/schema_dimension.png)

<center><em>Figure 1 : Introduction to notations for the gravity dam measurements</em></center>

According to the Bureau of Reclemamation of the USA departement of the intrior "Design of gravity dams" paper we can calculate the missing dimensions according to the current standards.
$$
m=\frac{B}{H}=\frac{b_{0}}{h_{0}}\simeq0,8
\newline
b_{0}=\frac{H}{10}\geq8m
$$
<u>We can therefore calculate :</u>

-   $B=m.H=0,8\times71=56,8$m
-   $b_{0}=\frac{H}{10}=\frac{71}{10}=7,1m\leq8$, so we choose $b_{0}=8m$
-   $h_{0}=\frac{b_{0}}{m}=\frac{8}{8,0}=10m$

### Stability analysis

Now we have to figure out the weakpoints ans the critical failure modes. We can identify three of them:

-   **Sliding** : too much pressure causes the dam to move in the horizontal plane. The following safety factor is then considered: $n_{SL}=\frac{\sum V}{\sum H}$. Where $\sum V$ represent the sum of the vertical efforts and $\sum H$ for the horizontal ones. To meet the safety requirements $n_{SL}>3$ for the usual load case.

-   **Overturning** : the dam rotates around a fixed point. In our case and as shown in the diagram the lower end on the right. The safety factor is described as, $n_{OV}=\frac{M_{stab}}{M_{dest}}>2$.

-   **Crushing :** in this case we are looking at compression and tension failure.

### Load Combination

For this example we have chosen to consider the usual load case. It is then a question of determining the set of forces wich have a reasonable probability of simultaneous occurence. The calculations could have been made in an even less favourable scenario (unusual or extreme flood case, dynamic cases by considering waves, wind, earthquakes). The problem will be solved with the following assumptions :

-   The reservoir is at his operational level ($H_{0}$),

-   we are considering the dead load of the dam,

-   the uplift pressure is at his full drainage capacity,

-   there is a presence of silt that affect the dam.

<u><span class="underline">We can report on the following efforts :</span></u>

![Efforts on the dam](D:/lju_fgg/lju_fgg/hydroelectric_power/TD/TD1/images/schema_forces.png)

<center><em>Figure 2 : Efforts on the dam</em></center>

<u>Where :</u>

-   $G_{1}$ and $G_{2}$represent the **dead load** of the dam. The following formulas describing the effort are then considered :

    -   $\gamma_{conc}=24$ kN/m³

    -   $G_{1}=b_{0}.H.\gamma_{conc}.e=13632$ kN
        where $e$ is the thickness of the study section ($e=1$ m), so we won't consider it in the next equations 

    -   $G_{2}=\frac{1}{2}(B-b_{0})(H-H_{0})\gamma_{conc}=35721$ kN

    -   $r_{G1}=B-\frac{b_{0}}{2}=52,8$ m

    -   $r_{G2}=\frac{2}{3}(B-b_{0})=32,5$ m

-   $P_{w}$ the **hydrostatic pressure** on the dam :

    -   $\gamma_{w}=10$ kN/m³

    -   $P_{w}=\gamma_{w}.\frac{H_{0}^{2}}{2}=21125$ kN

    -   $r_{w}=\frac{1}{3}.H_{0}=21,7$ m

-   $P_{u}$ the **uplift pressure** on the dam :

    -   To reduce the effect of uplift, draingaes to the ground are installed in the dam. This reduction is associated with the coefficient $\lambda=0,85$

    -   $P_{u}=\lambda.H_{0}.\gamma_{w}.\frac{B}{2}=15691$ kN

    -   $r_{u}=\frac{2}{3}.B=37,8$ m

-   $P_{s}$the **silt pressure** on the dam :

    -   $\gamma_{S}=18$ kN/m³

    -   $H_{S}=\frac{H_{0}}{3}=21,6$ m

    -   $P_{S}=\gamma_{S}.\frac{H_{s}^{2}}{2}=4225$ kN

    -   $r_{S}=\frac{H_{s}}{3}=7,2$ m

### Checking safety factors

We can therefore calculate our safety factors.
$$
n_{SL}=\frac {G_1+G_2-P_u}{P_w-P_S}= 1,99
\newline
n_{OV}=\frac{G_1.r_{G1}+G_2.r_{G2}}{P_w.r_w+P_S.r_S+P_u.r_u}=1,74
$$
We can now conclude that the current design of the dam ==does not satisfy the safety criteria== because $n_{SL}<3$ and $n_{OV}<2$.

### Annex: calculation code 

```python
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
lamb=0.85
Pu=lamb*H0*gw*B/2
ru=(2/3)*B
#silt pressure
gs=18
Hs=H0/3
Ps=gs*0.5*Hs*Hs
rs=Hs/3
'''security factors check'''
nsl=(G1+G2-Pu)/(Pw-Ps)
nov=(G1*rG1+G2*rG2)/(Pw*rw+Ps*rs+Pu*ru)
```

## Task 2: Determine the design of spillway section to safely evacuate flood with a 100-year  return period downstream

Our spillway design must be design to propagate $Q_{100}=400$ m³/s while one of the four overspilling sections is blocked. The spillway is constructed with a Creager shape and the overspilling section are $6$ m wide. 

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD1\images\schema_overspilling.png)

<center><em>Figure 3 : Sideview of Creager spillway</em></center>

<u>Where :</u>

- $H_d$ is overspilling height of the water,
- $H_e$ is the energy height.

### Spilway equations

$$
Q =m.b.\sqrt{2g}.H_e^{\frac{3}{2}}
$$

<u>Where :</u>

- $m=m_0(\frac{H_e}{H_d})^{0,16}$ , the spillway coeficient for a Creager spillway ($m_0=0,4956$), 
- $b=6$m the width of the spillway, 
- $H_e =H_d+\frac{v_0^2}{2}$, with tow cases :$\begin{cases}{\frac{H_0}{H_d}>1,33\Rightarrow v_0=0}\\{\frac{H_0}{H_d}\le1,33\Rightarrow v_0  \ne 0}\end{cases}$

<u>For our design :</u> $H_0\gg H_d$ so $v_0=0$, then $H_e=H_d$ and $m=m_0$.

Whe can rewrite the spillway equation as $Qp=m_0.b.\sqrt{2g}.H_d^\frac{3}{2}$
$$
H_d = \left(\frac{Q_p}{m_0.b.\sqrt{2g}}\right)^\frac{2}{3}=\left(\frac{400/3}{0,4956.6.\sqrt{2.9,81}}\right)^\frac{2}{3}=4,68 \text{ m}
$$
As we want $H_d \le 4$ m, we can calculate $b_{min}=\frac{Q_p}{m_0.\sqrt{2g}.H_d^{\frac{3}{2}}}=7,6$ m, and we roud it up at $b_{min}=8$ m.

Using the same formula, we obtain : $H_d(b_{min})=3,9$ m.

<div style="page-break-after: always; break-after: page;"></div>

### Technical drawing at scale

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD1\pdf autocad\montage autocad.png)

<div style="page-break-after: always; break-after: page;"></div>

## Task 3:  Design the intake structure for the powerhouse, route water to the powerhouse and  further to the stilling basin downstream of the dam

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD1\images\schema_perte.png)

<center><em>Figure 4 : Design of the waterway to the powerhouse</em></center>

We are now going to calculate all of the losses from the pressure tunnel entrance to the regulation basin. As shown in the previous figure we separate the calculations into three parts:

- $\Delta h_1$ : head loss in the pressure tunnel, 
- $\Delta h_2$ : penstock losses, 
- $\Delta h_3$ : draft tube ones. 

These losses are defined as lengths corresponding to the dissipation of the mechanical energy of a moving fluid. 
$$
\Delta h_i = \xi_i\frac{v_i^2}{2g}=\xi_i \frac{Q_i^2}{F_i^2. 2g} = K_i.Q_i^2
$$
We are then interested in two types of losses: local losses and frictional losses. 

### Hydraulic losses in the pressure tunnel

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD1\images\scheme_intake.png)

<center><em>Figure 5 :Scheme of the intake structure of the pressure tunnel</em></center>

<u>With :</u>

- $(1)$ : the intake,
- $(2)$ : the trash-racks,
- $(3)$ : a transition from the quadratic intake profile to gate profile, 
- $(4)$ : main hydraulic gates,
- $(5)$ : transition from gate profile to tunnel profile, 
- $(6)$ : the pressure tunnel. 

**$(1)$ The intake** 

$\xi_{Vt}=0,5$
$K_{Vt}=\frac{\xi_{Vt}}{F_{Vt}^2.2g}=\frac{0,5}{71^2.2.9,81}=5,05e-06$ , avec $F_{Vt}=A_p$

**$(2)$ The trash-racks** 

<u>Some notations :</u>

- $\alpha=70°$, the inclination of the trash-racks
- $\chi=1$, the flow coefficient ($=1$ because of the horizontal flow)
- $s=10$ mm, width of individual trash-rack bar
- $l=50$ mm, distance between each bars 
- $\beta=2,42$, the trash-rack bar geometry coefficient

$\xi_{res}=\chi.\beta\left(\frac{s}{l}\right)^{\frac{4}{3}}.sin(\alpha)=0,219$

 $K_{res}=\frac{\xi_{res}}{F_{res}^2.2g}=2,21e-06$

**$(3)$ Narrowing of the tunnel** 

<u>To estimate $\underline{\xi_{zoz}}$</u> : 

|  $F_2/F_1$  | $0,01$ | $0,1$  | $0,2$ | $0,4$ | $0,6$ | $0,8$ |
| :---------: | :----: | :----: | :---: | :---: | :---: | :---: |
| $\xi_{zoz}$ | $0,5$  | $0,45$ | $0,4$ | $0,3$ | $0,2$ | $0,1$ |

With a linear interpolation we get : $\xi_{zoz}=0,34$ 
$K_{zoz}=\frac{\xi_{zoz}}{F_{res}^2.2g}\left(\frac{F_{res}^2}{F_{zap}^2}-1\right)=2,92e-05$

**$(4)$ Main hydraulic gates**

$\xi_{zap}=0,1$
$K_{zap}=\frac{\xi_{zap}}{F_{zap}^2.2g}=9,62e-06$ 

**$(5)$ Changing of geomtry**

With a linear interpolation we get : $\xi_{tran}=0,11$ 

$K_{tran}=\frac{\xi_{tran}}{F_{zap}^2.2g}\left(\frac{F_{zap}^2}{F_{k}^2}-1\right)=6,57e-06$

**Curvature of the tunnel axis**

We have four turn in the tunnel, described as :

| Angle of the turn | Radius of the tunnel axis |
| :---------------: | :-----------------------: |
|  $\alpha_1=90°$   |    $R_1=70 \text{ m}$     |
|  $\alpha_2=47°$   |    $R_2=110 \text{ m}$    |
|  $\alpha_3=16°$   |    $R_3=150 \text{ m}$    |
|  $\alpha_4=24°$   |    $R_4=150 \text{ m}$    |

and : $\xi_{lom,i}=(0,13+1,85\left(\frac{r}{R_i}\right)^{3,5})\frac{\alpha_i}{90}$

$K_{lom}= \sum\limits_{i=1}^{n=4}\frac{\xi_{lom,i}}{F_k^2.2g}=4,01e-05$

**Surge tank**

$\xi_{st}=0,1$
$K_{st}=\frac{\xi_{st}}{F_k^2.2g}=1,56e-05$

**Friction losses**

<u>Some notations :</u>

- $\lambda=0,012$, Dracy-Weisnbach coefficient
- $L_K=2600\text{ m}$

$K_{lin}=\frac{\lambda.L_k}{D}\frac{1}{F_k^2}\frac{1}{2g}=0,0010$

<u>**Summation of the hydraulic losses in the pressure tunnel :**</u>
$$
\Delta h_1 =Q^2(K_{Vt}+K_{res}+K_{zoz}+K_{zap}+K_{lom}+K_{st}+K_{lin}) \\
$$
==We have for hydraulic losses in the tunnel $\Delta h_1 = 5,83 \text{ m}$==

*Calculation were made using python, following this script*

```python
from math import *

'''Declaration of variables'''
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
D=0.62*(Q**0.48)
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

'''___Final calculus___'''
Dh1=(Q**2)*(Kvt+Kres+Kzoz+Kzap+Klom+Klom+Kst+Klin)
print("Δh1=",Dh1)
```

### Hydraulic losses in the penstock 

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD1\images\scheme_losses_penstock.png)

<center><em>Figure 6 : Scheme of the penstock pipes</em></center>

**Change of geometry at the dowstream of the surgetank**

$\xi_{zoz,1}=0,1$

$K_{zoz,1}=\frac{\xi_{zoz,1}}{F_{k}^2.2g}\left(\frac{F_{k}^2}{F_{c}^2}-1\right)=9,67e-06$

**Change of geometry before th hydraulic gates in the penstock**

$\xi_{zoz,2}=0,1$
$F_{zap}=a^2$  and  $K_{zoz,2}=\frac{\xi_{zoz,2}}{F_{c}^2.2g}\left(\frac{F_{c}^2}{F_{zap}^2}-1\right)=2,33e-05$

**Hydraulic gates**

$\xi_{zap}=0,2$
$K_{zap}=\frac{\xi_{zap}}{F_{zap^2.2g}}=9,72e-05$

**Change of geometry after the hydraulic gates**

$\delta=8°$ implies that $c=0,13$ in the formula $\xi_{raz}=c\left(1- \frac{F_{zap}}{F_c} \right)=0,036$
$K_{raz}=\frac{\xi_{raz}}{F_{zap}^2.2g}=1,76e-05$

**Change of the penstock axis**

| Angle of the turn | Radius of the tunnel axis |
| :---------------: | :-----------------------: |
|   $\alpha_1=9°$   |    $R_1=50 \text{ m}$     |
|  $\alpha_2=17°$   |    $R_2=50 \text{ m}$     |

As  in the previous section we calculate $\xi_{lom,1}$ and $\xi_{lom,2}$. 

$K_{lom}=\frac{\xi_{lom,1}+\xi_{lom,2}}{F_c^2.2g}=9,49e-06$

**Division of the penstock**

<u>First :</u>
$\xi_{raz,2}=0,2$ and $K_{raz,2}=\frac{\xi_{raz,2}}{F_c^2.2g}=5,05e-05$

<u>Second :</u>

$F_j$ the circular surface defined by the diameter $D_j$ can be determinated based on the water velocity before entering the turbine : $v_j=7m.s^{-1}$ at $Q_j=\frac{Q}{2}$.

We have $F_j=\frac{Q_j}{v_j}$ in the equation, $K_{zozj}=\frac{\xi_{zoz}}{F_{c}^2.2g}\left(\frac{F_{c}^2}{F_{j}^2}-1\right)=1,72e-04$ 
For the other branch : $K'_{zozj}=\frac{K_{zozj}}{4}=4,32e-05$

**Turbine inlet valve**

$\xi_{lop}=0,12$
$K_{lop}=\frac{\xi_{lop}}{F_j^2.2g}=2,37e-04$

And for second branch : $K'_{lop}=\frac{K_{lop}}{4}=5,94e-05$

**Friction losses**

- The lenght of the penstock is $L_c=160 \text{ m}$
- $\lambda = 0,0118$

$K_{lin}=\frac{\lambda.L_c}{D}\frac{1}{F_c^2}\frac{1}{2g}=1,12e-04$

<u>**Summation of the hydraulic losses in the penstock :**</u>
$$
\Delta h_1 =Q^2(K_{zoz,1}+K_{zoz,2}+K_{zap}+K_{raz,1}+K_{lom}+K_{zozj}+K_{zozj}'+K_{lop}+K_{lop}'+K_{lin}) \\
$$
==We have for hydraulic losses in the penstock $\Delta h_1 = 3,95 \text{ m}$==

*Calculation were made using python, following this script*

```python
from math import *

'''Declaration of variables'''
Q=71
H=Q
g=9.81

##CHANGE OF GEOMETRY DOWNTREAM OF THE SURGETANK##
v=5
Ac=Q/v
Dmin=2*sqrt(Ac/pi)
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

'''___Final calculus___'''
Dh2=(Q**2)*(Kzoz1+Kzoz2+Kzap+Kraz1+Klom+Kzozj+Kzozjp+Klop+Klopp+Klin)
```

### Hydraulic losses in the draft tube 

In th draft tube we know the velocity of the water $v_{out}=1,5 \space m.s^{-1}$, we can determine the surface of the tube $F_{out}=\frac{Q}{v_{out}}$ .

<u>Then :</u>

$\xi_{out}=2$
$K_{out}=\frac{\xi_{out}}{F_{out}^2.2g}=4,54e-05$

==We can calculate the loss in the draft tube : $\Delta h_3=Q^2.K_{out}=0,23$ m==

*Calculation were made using python, following this script*

```python
##DRAFT TUBE##
vout=1.5
Fout=Q/vout
Eout=2
Kout=Eout/(2*g*Fout**2)

Dh3=Kout*Q**2
```

### Conclusion 

The total loss in the entire system is ==$\Delta h=\Delta h_1+\Delta h_2+\Delta h_3 =10$ m==

The net utilizable design fall is therefore : ==$H_{net}=H-\Delta h=71-10=61$ m==



