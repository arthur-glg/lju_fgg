# <center>Design of the overspilling section</center>

<center><b>Arthur Guillot - Le Goff</b> </center> 

<center><b>Autumn semester 2021-2022 | Hydroelectric power</b> </center> 

------

[TOC]

------



<div style="page-break-after: always; break-after: page;"></div>

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



