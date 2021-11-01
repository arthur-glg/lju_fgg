# <center>Design of a reservoir hydropower scheme</center>

<center><b>Arthur Guillot - Le Goff</b> </center> 

<center><b>Autumn semester 2021-2022 | Hydroelectric power</b> </center> 

------

[TOC]

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

