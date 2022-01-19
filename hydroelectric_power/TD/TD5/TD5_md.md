# <center>Complete financial analysis</center>

<center><b>Arthur Guillot - Le Goff</b> </center> 

<center><b>Autumn semester 2021-2022 | Hydroelectric power</b> </center> 

------

[TOC]

------

<div style="page-break-after: always; break-after: page;"></div>

In this last exercise we are going to do a complete financial evaluation for your investment in a new HPP following two methodologies, one with a **fixed cost price** and another with a **variable cost price**.  

## Fixed cost 

### Setup

The investment is analysed with the respect to the investment plan for each financial item. We are going to analyse only for seven years. That correspond to the design and construction duration (5 years of construction). 

<u>Quotas for the financial items :</u>

- Total : 67 m€
  - construction works 52,24% : 35 m€;
  - equipment 35,83% : 24 m€;
    - mechanical 8,96% : 6 m€;
    - electrical 19,4% : 13 m€;
    - hydro-mechanical 7,46% : 5 m€;
  - start-up investment 11,94% : 8 m€.

We translate those input data as the following table,

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD5\figure\input data.png)

### Calculation sheet 

To calculate our investment cost we divide the estimated proportion cost following the time dynamics over the seven years such as:
$$
Investment(y)=\frac{Dynamic(y).Proportion}{100}
$$
![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD5\figure\fixed_tab.png)

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD5\figure\fixed_graph.png)

## Variable cost 

### Integration of the inflation

In this method we consider some intermediate price increase following an inflation rate of $r=1,8$ %/year.

To add the inflation to our calculus we use the parameter $p$ as that we multiply by the intermediate $Total$. 
$$
p=(1+\frac{r}{100})^{n-1}
$$

### Calculation sheet

 ![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD5\figure\varia_tab.png)

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD5\figure\varia_graph.png)

## Financial construction of the project based on variable cost 

We consider that the concession for hydropower production is granted for 50 years. As before preparation works and construction will last for 7 years. 

### Static indicators 

We can estimate :

- the average yearly production, 
- the rated power of the powerhouse: 45 MW,
- the investment cost, 
- the production consist of :
  - anormalization cost :
    - construction works : 2% over 30 years, 
    - equipment : 5% over 20 years, 
    - start-up : 15% over 7 years,
  - annual operation cost (the operation is only for half of the year):
    - maintenance : 0,5%
    - insurance : 0,2 %
    - workload : 1%

<img src="D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD5\figure\dyna_tab.png" style="zoom:50%;" />

![](D:\lju_fgg\lju_fgg\hydroelectric_power\TD\TD5\figure\dyna_courbe.png)

### Dynamic indicators 

- we consider the price of energy sold on the market 
- the discount rate 
- we estimated financial construction plan, then the NPV (Net present value)
- we estimated the internal rate of return

For a good economic plan: 

- $NPV > 0$
- $IRR> DiscountRate $ or at least $IRR>0$
