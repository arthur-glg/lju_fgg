# <center>Operation with a reservoir</center>

<center><b>Arthur Guillot - Le Goff</b> </center> 

<center><b>Autumn semester 2021-2022 | Hydroelectric power</b> </center> 

------

[TOC]

------

<div style="page-break-after: always; break-after: page;"></div>

## Part. 1

### Objective and input data

The objective of this exercise is to calculate the hydraulic and operational regimes for 4 different scenarios : 

- A wet hydrological year ($Q_m=16,6$ m^3^.s^-1^)
- A mean hydrological year ($Q_m=13,3$ m^3^.s^-1^)
- A dry hydrological year ($Q_m=10,04$ m^3^.s^-1^)
- A maximum operation in a wet hydrological year ($Q_m=16,6$ m^3^.s^-1^)

Where $Q_m$ is the mean river flow.

For the calculations, we work with the following data:

- $Q=71$ m^3^.s^-1^, our personal rated discharge;
- $\Delta t=3600$ s, one hour computational time step;
- $E_{op}=524,75$ m.asl, the operational reservoir elevation.

### Calculation sheet 

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD3\figures\f1_tableau calculs.png)

<u>Here is the explanation of our calculations :</u>

- $V_d=Q_m.\Delta t$, the intake of the reservoir [m^3^];
- $V_i=f.\Delta t$, the outtake from the reservoir [m^3^], $f$ being the operational flow [m^3^.s^-1^];
- $Balance =V_d-V_i$ [m^3^];
- $E_{res}=501,8595+0,007054*V_{res}-9,04456*10^-7*V_{res}^2+4,84154*10^-11*V_{res}^3$, the reservoir level [m.n.m];
- $V_{res}=5414521,34504851-21286,7185857706*E_{res}+20,8148557973526*E_{res}^2+0,00022032983939908*E_{res}^3$, the reservoir volume [m^3^];
- $Denivelation(h)=E_{res}(h)-E_{op}$, the denivelation from the operation level of the reservoir. 

### Results

#### Mean year

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD3\figures\mean year graph.png)

#### Dry year 

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD3\figures\dry year graph.png)

#### Wet year 

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD3\figures\wet year graph.png)

#### Maximum operation in a wet year 

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD3\figures\maw wet year graph.png)

We can conclude that we have similar behaviour in form for the first three scenarios. However, we observe very different variations, the dry year being much more volatile, then the wet year and finally the mean year. Except for the maximum operation in a wet year scenario where we observe an equal variation concentrated on a single peak in the middle of the day. 

## Part. 2, tailwater reservoir operation 

On this part we are now looking to create the daily operation diagram for the wet, dry and mean scenario. As we are taking water from the river we need to compensate this loss to not affect that much the ecosystem. 

<u>Our input data are :</u>

- $H_{dam}=71$ m, the height of the dam;
- $Q=71$ m^3^.s^-1^, the discharge;
- $\Delta t =3600$ s, the calculation time step;
- $ht_{min}=524,75-H_{dam}-3,5=450,25$ m, the minimum level of the tail water.

### Calculation sheet

<img src="D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD3\figures\tabpart2.png" style="zoom: 50%;" />

<u>Our calculus are :</u>

- $V_{odt}=-\Delta t.f_{out}$, the outtake from the tail race, $f_{out}$ being the outflow from the tailrace;
- $V_{dot}=-V_i$, the intake of the reservoir;
- When the cumulative of the balance is at its minimum we set :
  - the water level to $ht_{min}$;
  - the total volume equal to $340,604329.(ht_{min}-H_{dam}-73)-151119,74$;
  - the denivelation to $0$.
- For before and after the minimum point we use the following formulas :
  - $level(h)=0,00293595798661*V_{total}+516,681207587491-H_{dam}$;
  - $V_{total}(h)=V_{total}(h+1)-\frac{Balance(h+1)}{1000}$, before the minimum;
  - $V_{total}(h)=V_{total}(h-1)-\frac{Balance(h-1)}{1000}$, after the minimum.

### Results 

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD3\figures\reservoir operation.png)
