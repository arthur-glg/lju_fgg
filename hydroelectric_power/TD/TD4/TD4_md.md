# <center>Production of electricity</center>

<center><b>Arthur Guillot - Le Goff</b> </center> 

<center><b>Autumn semester 2021-2022 | Hydroelectric power</b> </center> 

------

[TOC]

------

<div style="page-break-after: always; break-after: page;"></div>

In this exercise we will calculate our yearly electricity production in kW.h and the total price of sold electricity. 

## Our input data for this exercise

- $Q=71$, the discharge [m^3^.s^-1^];
- $H=71$, the height of the dam [m];
- $\Delta H=10$, the hydraulic head losses in the system [m];
- $c=0,07$ €/Kw.h, the cost of energy;
- $Qb = 40$, the base flow downstream of tailwater [m^3^.s^-1^];
- $R_{hmax}=525,75$, the reservoir maximum level [m.asl];
- $R_{Vmax} = 7785$, the reservoir maximum level [m^3^];
- $T_{hmin}=452,25$, the tailwater minimum level [m.asl];
- $T_{Vmin}=1556$, the tailwater minimum volume [m^3^].

## Calculation

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD4\figure\tab.png)

- $R_{DailyVolume}=(Q-Flow)*\frac{Flow.24.3,6}{Q}$, [m^3^];
- $R_{V}=R_{Vmax}-R_{DailyVolume} $, the reservoir volume [m^3^];
- $R_{hlow}=501,8595+0,007054*R_V-9,04456*10^-7*R_V^2+4,84154*10^-11*R_V^3$, the lowest level of the reservoir [m.asl];
- $R_{hmean}=\frac{R_{hlow}+R_{hmax}}{2}$ , the mean level of the reservoir [m.asl];
- $T_{DailyVolume}=(Qb-Flow)*\frac{Flow.24.3,6}{Qb}$, [m^3^];
- $T_V=T_{Vmin}+T_{DailyVolume}$, the tail volume [m^3^];
- $T_{h,high}=0,00293595798661*T_V+516,681207587491-H$, the highest level of the tailwater [m.asl];
- $T_{hmean}=\frac{T_{h,high}+T_{hmin}}{2}$, the mean level of the tail [m.asl];
- $GrossHead = R_{hmean}-T_{hmean}$, [m];
- $NetHead=GrossHead -\Delta H$, [m];
- $Power = 9,81*NetHead*Q*\mu$, [kW];
- $DailyProduction=\frac{Power*Flow*24}{Q}$, [kW.h];
- $TotalProduction(t)=\frac{[DailyProduction(t-1)+DailyProduction(t)]*DaysOfOpertation}{2}$, [kW.h];
- $TotalPrice = TotalProduction*0,07$, [€]

<div style="page-break-after: always; break-after: page;"></div>

## Graph comparison 

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD4\figure\kWh.png)

<center><em>Comparison of energy production for the 3 scenarios </em></center>

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD4\figure\Sans titre - 1.png)

<center><em>Total price of sold electricity </em></center>

