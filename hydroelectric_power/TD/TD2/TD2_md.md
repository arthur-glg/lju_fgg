# <center>Ecolnomic feasibility of cross-section of the pressure tunnel and penstock</center>

<center><b>Arthur Guillot - Le Goff</b> </center> 

<center><b>Autumn semester 2021-2022 | Hydroelectric power</b> </center> 

------

[TOC]

------

<div style="page-break-after: always; break-after: page;"></div>

## Methodology

The objective of this exercise is to optimise the geometry of the headrace (pressure) tunnel and the penstock. In this step of the design process we need to consider construction criteria and financial feasability. Our analysis is based on the following table :

| Diameter | Hydraulic loss coefficient | Construction costs | Energy loss | Loss of energy | Cost of the lost energy |
| :------: | :------------------------: | :----------------: | :---------: | :------------: | :---------------------: |
|   [m]    |             /              |        [€]         |     [m]     |     [kW.h]     |           [€]           |

**Diameter**
This is our variable, we will calculate very other parameters based on its variation. 
For the tunnel, the diameter varies as : [ 4 | 4,5 | 5 | 5,5 | 6 ]. And for the penstock : [ 4 | 4,5 | 5 | 5,5 ].

**Hydraulic loss coefficient**

To calculate those coefficient we will be using the same methods than the first exercise. I'm once again using python for calculations. The code is available at the end of this document. 

**Construction costs**

- Pressure tunnel construction cost breakdown :
  - 2% for the preparation of works, 
  - 16,5% for the earthworks, 
  - 22% for jet grounding, 
  - 22% for support, 
  - 36% for the concrete works.
- Penstock construction breakdown :
  - 2% for earthworks and preparation,
  - 2% for concrete works,
  - 20% for hydraulic equipement, 
  - 76% for steel pipeline. 

To calculate the global cost of all of this construction operation we use the following formula (where $D$ is the diamater.) :
$$
Costs=1435,36.D-615,646
$$


**Energy loss**
As we calculate the hydraulic loss cofficient, we have $\Delta h=K.Q^2 $ where $K$ is the hydraulic coefficient and $Q$ the flow rate.

**Loss of energy in kW.h**

Or calculation of the lost energy is estimated based on :

- the design ccaracteristic of the trubine, 
- the flow duration curve, 
- all the hydraulic losses. 

<u>For energy production in one year :</u>
$$
E=\eta_{ag}.9,81.H_{net}.Q_{med}.\eta_i.T
$$
*Where :*

- $\eta_{ag}$ is the utilisation coefficient for the entire power unit (turbine, transformer, generator and switch)
  $\eta_{ag}=\eta_{tur}.\eta_{trans}.\eta_{gen}.\eta_{sw}=0,865$
- $H_{net}=H-\Delta h$
- $Q_{med}=16,6 \text{ }m^3.s^{-1}$, the discharge estimated with a hydrological study
- $\eta_{i}=0,9$, the utilisation rate of the yearly inflow from the flow duration curve
- $T=2600$, the numbers of hours in a year

**Cost of the loss energy**

We can calculate : $\Delta C=\Delta E.c $, where $c=0,07$ €/kW.h

 ### Input data

For each case fo diameter we got this table for input data :

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD2\image\input_data.png)

### Financial items

We can now make this next table that give us a report about the cost and income for the 4 years of construction and the next 20 years of operation :

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD2\image\financial_items.png)

<div style="page-break-after: always; break-after: page;"></div>

### Net present value 

Net present value is calculated as the difference of present value of benefits and present value of expenditure. This calculus is done over the lifetim of a project. This value is used to understand the risk an investor is taking. It is a good indicator for comparing the economic viability of different projects. 

Generally speaking :

- If $NPV>0$, the project can be accepted 
- if $NPV<0$, the project is rejected 

We can, therefore, calculate an $NPV$ with the following formula :
$$
NPV(i,n)= \sum\limits_{i=0}^{n}\frac{CF_{i}}{(1+r)^i}
$$
Where $r$ is the discount value and $CF_i$ the balanc of cash flow. 

We have the following table :

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD2\image\npv_tab.png)

## Compilation of calculations and diameter optimisation

The method described in the previous sections is repeated for the different diameters for both the tunnel and the penstock. We compile the results in the following tables.

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD2\image\compile.png)

Our interest is then to find an optimal diameter. This is the diameter for which the sum of the NPVs is minimal. We are then interested in the following graphics. 

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD2\image\graph.png)

With a simple identification of an extremum with a derivate we find :

- ==$D_{min,tunnel}=5,47$ m==
- ==$D_{min,penstock}=4,84$ m==

