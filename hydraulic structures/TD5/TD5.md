# <center>Design of a low-level outlet</center>

<center><b>Arthur Guillot - Le Goff</b> </center> 

<center><b>Autumn semester 2021-2022 | Hydroelectric power</b> </center> 

------

[TOC]

------



<div style="page-break-after: always; break-after: page;"></div>

![](D:\lju_fgg\lju_fgg\hydraulic structures\TD5\grand_schema.png)

## Dimension 

The intake is a quadratic cross section with a side $D$, such as $F=D^2$.

<u>With the Thales theorem :</u> $\frac{B-b_0}{H-h_0}=\frac{x}{P}$

$x=\frac{P.(B-B_0)}{H-h_0}=\frac{9(56-8)}{70-10}=7,2$ m

<u>And :</u> $B'=B-x=56,8-7,2=49,6$ m

<u>For the intake height :</u>

- $y=0,02*B'=0,02*49,6=1$ m
- $z_{in}=z_{out}+y=8+1=9$ m
- $L_p=\sqrt{B'^2+y^2}=49,61$ m

## Hydraulic losses 

![](D:\lju_fgg\lju_fgg\hydraulic structures\TD5\loss.png)

### Local losses 

**Hydraulic losses at the intake :**
$\xi_{in}=0,5$
$\Delta h_{intake}=\xi_{in}\frac{Q^2}{F^2.2g}$

**Hydraulic losses due to the trash racks at the intake :**
$\xi_{trash}=\chi.\beta(\frac{s}{l})^{4/3}.sin(\alpha)=1*2,42(\frac{10}{50})^{4/3}*sin(70)=0,26$
$\Delta h_{trash}=\xi_{trash}\frac{Q^2}{F^2.2g}$

**Hydraulic losses at the hydraulic gates :**
$\xi_{in}=0,1$
$\Delta h_{gates}=\xi_{gates}\frac{Q^2}{F^2.2g}$

**Hydraulic losses at the outtake :**
$\xi_{out}=2$
$\Delta h_{out}=\xi_{out}\frac{Q^2}{F^2.2g}$

### Friction losses 

$\lambda = 0,02$, the friction coefficient 
$L_p=49,61$ m
$\Delta h_{friction}=\frac{Q^2}{2g}.\frac{\lambda.L_p}{D}.\frac{1}{F^2}$

### Equilibrium equation 

$$
H_0-P=\sum \Delta h_{local}+\Delta h_{friction}+\frac{v_{out}^2}{2g}\\
H_0-P=\frac{Q^2}{2g.F^2}(\xi_{in}+\xi_{trash}+\xi_{gates}+\xi_{out}+\frac{\lambda L_p}{D}+1)\\
F=\sqrt{\frac{Q^2}{2g.()H_0-P}(\xi_{in}+\xi_{trash}+\xi_{gates}+\xi_{out}+\frac{\lambda L_p}{D}+1)}
$$

## Final calculus 

In order to find the right $D$, we used a calculus by iteration. We start our loop with $D=4$ m

```python
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
```

For a 10 loop iteration we have the following results :

```python
2.0707355989956264
2.0992635758413654
2.0984755778874224
2.0984970679599178
2.098496481683014
2.0984964976772513
2.0984964972409115
2.0984964972528153
2.0984964972524907
2.0984964972524995
```

We can therefore conclude that : ==$D=2,1$ m==

