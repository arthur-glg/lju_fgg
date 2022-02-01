# <center>Design of the stillin basin</center>

<center><b>Arthur Guillot - Le Goff</b> </center> 

<center><b>Autumn semester 2021-2022 | Hydroelectric power</b> </center> 

------

[TOC]

------



<div style="page-break-after: always; break-after: page;"></div>

## Find the hydraulic jump equation 

![](D:\lju_fgg\lju_fgg\hydraulic structures\TD2\scheme1.png)

<u>We define :</u>

- $y_i^c$, the centre of gravity 
- $v_i$, the velocity of the profile 
- $P_i$, the external forces
- $\rho$, the density 
- $Q$, the discharge 
- $b$, the width of the basin 

<u>We can write the momentum equation :</u>  $\rho .Q(v_2-v_1)=P_1-P_2-P_{friction}$ , and we set $P_{friction}=0$

- $v_1=\frac{Q}{A_1}$ and $v_2=\frac{Q}{A_2}$
- $P_1=\rho gA_1y_1^c$ and $P_2=\rho gA_2y_2^c$

<u>Then :</u> 
$$
\cancel{\rho}Q^2(\frac{1}{A_2}-\frac{1}{A_1})=\cancel{\rho}g(A_1y_1^c-A_2y_2^c)\\
A_i= y_i.b \text{  and  } y_i^c=\frac{y_i}{2}\\
\frac{Q^2}{b.y_2}+gb\frac{y_2^2}{2}=\frac{Q^2}{b.y_1}+gb\frac{y_1^2}{2}\\
\text{we note : } \frac{Q}{b}=Q_s \text{ ,the specific discharge}\\
(y_2^2-y_1^2)=\frac{2 Q_s^2}{g}(\frac{1}{y_1}-\frac{1}{y_2})\\
(y_2+y_1)\cancel{(y_2-y_1)}=\frac{2 Q_s^2}{g}\frac{\cancel{(y_2-y_1)}}{y_1.y_2}\\
y_1.y_2^2+y_1^2.y_2-\frac{2 Q_s^2}{g}=0 \text{ ,a quadratic equation}\\
y_2=\frac{-y_1^2+\sqrt{y_1^4-\frac{8 Q_s^2y_1}{g}}}{2 y_1}=\frac{y_1}{2}(\sqrt{1-\frac{8Q_s^2}{gy_1}}-1)
$$
<u>We note :</u> $\frac{Q_s}{y_1}=v$, so $\frac{Q_s}{gy_1^3}=\frac{v^2}{gh}=F_r^2$, the Froude number 

<u>Conclusion :</u> we have the following hydraulic jump equation==$y_2=\frac{y_1}{2}(\sqrt{1+8F_r^2}-1)$==   

## Specific energy loss 

- $\Delta E=E_2-E_1=(y_2-\frac{Q_s^2}{2gy_2^2})-(y_1-\frac{Q_s^2}{2gy_1^2})=\frac{y_2-y_1}{4y_2y_1}$
- $\frac{E_2}{E_1}=\frac{(\sqrt{1+8F_r^2})^3-4F_r^2+1}{8F_r^2(2+F_r^2)}$

## Calculation for the design 

![](D:\lju_fgg\lju_fgg\hydraulic structures\TD2\design.png)

<u>We have :</u> $T_0=H_{PR}+H_P+\frac{\cancel{v_0^2}}{2g}=65+2=67$ m

<u>We use the Bernoulli equations between the T and t :</u>
$$
T_0=y_1+\frac{v_s^2}{2g}+\sum{\xi}. \frac{v_s^2}{2g}\\
v_s=\frac{1}{\sqrt{1+\sum{\xi}}}.\sqrt{2g(T_0-y_1)}
$$
We need to find $v_s$ and $y_1$.

![](D:\lju_fgg\lju_fgg\hydraulic structures\TD2\quick scheme.png)

<u>The specific discharge :</u> $Q_s=\frac{Q}{b_{SB}}=y_1.v_s=\frac{400}{30}=13,33$ m

<u>We also note :</u> $\varphi =\frac{1}{\sqrt{1+\sum{\xi}}}=0,9$ the hydraulic loss coefficient.

<u>So :</u> $y_1=\frac{Q_s}{v_s}=\frac{Q_s}{\sqrt{2g(T_0-y_1)}}$

<u>By iteration :</u>

- $y_{1,0}=0$
- $y_{1,1}= \frac{Q_s}{\varphi \sqrt{2g(T_0-y_1)}}=\frac{13,33}{0,9 \sqrt{2.9,81(67-0)}}=0,4085$
- $y_{1,2}=\frac{13,33}{0,9 \sqrt{2.9,81(67-0,4085)}}=0,4097$
- $y_{1,3}=0,4097$

<u>So :</u> $v_s=\varphi \sqrt{2g(T_0-y_1)}=0,9 \sqrt{2.9,81(67-0,4097)}$

==$v_s=32,53$ m.s^_1^==

<u>With the Froude number :</u> $F_r= \frac{v_s}{\sqrt{g.y_1}}=\frac{32,53}{\sqrt{9,81.0,097}}=16,22$
$y_2=\frac{y_1}{2}(\sqrt{1+8F_r^2}-1)=\frac{0,4097}{2}(\sqrt{1+8.16,22^2}-1)$
==$y_2=9,19$ m==





