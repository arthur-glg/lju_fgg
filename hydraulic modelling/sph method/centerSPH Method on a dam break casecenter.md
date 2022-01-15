# <center>SPH Method on a dam break case</center>

[TOC]

## Task 1 :  For the initial geometry, compare the required computational time of a CPU and a GPU run

I run the computation on my computer:

- For GPU computational time : 4 minutes, 30 seconds minutes (NVIDIA GTX 1050) 
- For CPU computational time : around 5 hours (Intel i7-8565U)

## Task 2 : Modify the geometry of the model, generate it and export its figure from Paraview.

### The basic geometry 

```xml
<geometry>
            <definition dp="0.0085" units_comment="metres (m)"> 
                <pointmin x="-0.05" y="-0.05" z="-0.05" />
                <pointmax x="2" y="1" z="1" />
            </definition>
            <commands>
                <mainlist>
                    <setshapemode>dp | bound</setshapemode>
                    <setdrawmode mode="full" />
                    <setmkfluid mk="0" />
                    <drawbox>
                        <boxfill>solid</boxfill>
                        <point x="0" y="0" z="0" />
                        <size x="0.4" y="0.67" z="0.3" />
                    </drawbox>
                    <setmkbound mk="0" />
                    <drawbox>
                        <boxfill>bottom | left | right | front | back</boxfill>
                        <point x="0" y="0" z="0" />
                        <size x="1.6" y="0.67" z="0.4" />
                    </drawbox>
                    <shapeout file="Box"/>
                    <setmkvoid />
                    <drawbox>
                        <boxfill>solid</boxfill>
                        <point x="0.9" y="0.24" z="0" />
                        <size x="0.12" y="0.12" z="0.45" />
                    </drawbox>
                    <setmkbound mk="1" />
                    <drawbox>
                        <boxfill>top | left | right | front | back</boxfill>
                        <point x="0.9" y="0.24" z="0" />
                        <size x="0.12" y="0.12" z="0.45" />
                    </drawbox>
                    <setmkbound mk="10" />
                    <drawbox>
                        <boxfill>left</boxfill>
                        <point x="0.9" y="0.24" z="0" />
                        <size x="0.12" y="0.12" z="0.45" />
                    </drawbox>					
                    <shapeout file="Building"/>
                </mainlist>
            </commands>
        </geometry>
```

![image-20220107153054053](C:\Users\guill\AppData\Roaming\Typora\typora-user-images\image-20220107153054053.png)

### Modified geometry

```xml
<geometry>
            <definition dp="0.0085" units_comment="metres (m)"> 
                <pointmin x="-0.05" y="-0.05" z="-0.05" />
                <pointmax x="2" y="1" z="1" />
            </definition>
            <commands>
                <mainlist>
                    <setshapemode>dp | bound</setshapemode>
                    <setdrawmode mode="full" />
                    <setmkfluid mk="0" />
                    <drawbox>
                        <boxfill>solid</boxfill>
                        <point x="0" y="0" z="0" />
                        <size x="0.4" y="0.67" z="0.3" />
                    </drawbox>
                    <setmkbound mk="0" />
                    <drawbox>
                        <boxfill>bottom | left | right | front | back</boxfill>
                        <point x="0" y="0" z="0" />
                        <size x="1.2" y="0.67" z="0.4" />
                    </drawbox>
                    <shapeout file="Box"/>
                    <setmkvoid />
                    <drawbox>
                        <boxfill>solid</boxfill>
                        <point x="0.6" y="0.24" z="0" />
                        <size x="0.20" y="0.20" z="0.20" />
                    </drawbox>
                    <setmkbound mk="1" />
                    <drawbox>
                        <boxfill>top | left | right | front | back</boxfill>
                        <point x="0.6" y="0.24" z="0" />
                        <size x="0.20" y="0.20" z="0.20" />
                    </drawbox>
                    <setmkbound mk="10" />
                    <drawbox>
                        <boxfill>left</boxfill>
                        <point x="0.6" y="0.24" z="0" />
                        <size x="0.20" y="0.20" z="0.20" />
                    </drawbox>					
                    <shapeout file="Building"/>
                </mainlist>
            </commands>
        </geometry>
```

![image-20220107155751300](C:\Users\guill\AppData\Roaming\Typora\typora-user-images\image-20220107155751300.png)

## Task 3 : For the initial geometry, make a screenshot of an animation showing the water flushing against the  object or the downstream wall

![](C:\Users\guill\Desktop\screen.png)

## Task 4 : For the initial geometry, show time-series graphs of water surface elevations in the selected points

![](C:\Users\guill\Desktop\DualSPHysics_v5.0\figure\points.png)

![](C:\Users\guill\Desktop\DualSPHysics_v5.0\figure\elevation.png)

## Task 5 : For the initial geometry, show time-series graphs of forces acting upon the object

![](C:\Users\guill\Desktop\DualSPHysics_v5.0\figure\force.png)
