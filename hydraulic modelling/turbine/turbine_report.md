# <center>Measurement of water turbine characteristics</center>

<center><b>Arthur Guillot - Le Goff</b> </center> 

<center><b>Autumn semester 2021-2022 | Hydroelectric power</b> </center> 

------

[TOC]

------

<div style="page-break-after: always; break-after: page;"></div>

## Laboratory setup 

![](D:\lju_fgg\lju_fgg\hydraulic modelling\turbine\figure\schematic.png)

<center>Schematic of the measurement setup</center>

To carry out these measurements, water is pumped from a tank and fed under the control of a valve directly to the turbine. The water then falls into the lower reservoir and is returned via an adjustable valve to the basement reservoir. If the lower reservoir water level hits $H_{max}$ there is a safety escape route to make the water flow back into the basement reservoir. 

## Methodology

What we called the characteristic of the turbine is in fact it's operational points, the points of $Q$, $\Delta P$ where its efficiency $\eta$ is maximum. The method to calculate this operational point is to compare the hydraulic power created by the turbine to the mechanical power captured by the linked engine. 
$$
P_{hydro}=Q. \Delta P \\
P_{meca}= C.\omega = r.F.\omega \\
\eta = \frac{P_{meca}}{P_{hydro}}
$$
<u>Where :</u>

- $Q$ is the flow rate measured by an electromagnetic flow meter 
- $\Delta P$ is the pressure difference measured by a differential pressure transducer
- $C=r.F$ the torque applied to the motor shaft by the turbine 
- $r=7,5 $ cm the action turbine radius
- $F$ is the acting force, 
- $\omega $ is the speed of rotation of the turbine 

## Measurement 

### First calculation, rotation speed fixed and variable pump power

![](D:\lju_fgg\lju_fgg\hydraulic modelling\turbine\figure\tab1.png)

![](D:\lju_fgg\lju_fgg\hydraulic modelling\turbine\figure\graph1.png)

We have : $\eta= 896959Q^3 - 47215Q^2 + 811.64Q - 4.017$

We can therefore calculate the maximum of this function and deduce from it the operational points.

==$ Q_{ope}= 0,015 $ m^3^/s==

==$ \Delta P_{ope}=5,4 $ kPa==

==$ \eta_{ope}=0,56 $==

<div style="page-break-after: always; break-after: page;"></div>

### Second calculation, variable rotation speed

![](D:\lju_fgg\lju_fgg\hydraulic modelling\turbine\figure\tab2.png)

![](D:\lju_fgg\lju_fgg\hydraulic modelling\turbine\figure\graph2.png)

![](D:\lju_fgg\lju_fgg\hydraulic modelling\turbine\figure\graph2_2.png)

We have : $\eta= -1.10^8Q^3 + 6.10^6Q^2 - 92813Q + 485.92$

We can therefore calculate the maximum of this function and deduce from it the operational points.

==$\omega_{ope}=60$ rad/s==

==$Q_{ope}= 0,0169$ m^3^/s==

==$\Delta P_{ope}=6,15$ kPa==

==$\eta_{ope}=0,63$==





