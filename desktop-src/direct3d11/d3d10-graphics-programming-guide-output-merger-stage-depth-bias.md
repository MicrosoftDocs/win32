---
title: Depth Bias
description: Polygons that are coplanar in 3D space can be made to appear as if they are not coplanar by adding a z-bias (or depth bias) to each one.
ms.assetid: ee904316-dc6d-48a4-bdb7-0f7dcdb9d9d6
ms.topic: article
ms.date: 05/31/2018
---

# Depth Bias

Polygons that are coplanar in 3D space can be made to appear as if they are not coplanar by adding a z-bias (or depth bias) to each one.

This is a technique commonly used to ensure that shadows in a scene are displayed properly. For instance, a shadow on a wall will likely have the same depth value as the wall. If an application renders a wall first and then a shadow, the shadow might not be visible, or depth artifacts might be visible.


An application can help ensure that coplanar polygons are rendered properly by adding the bias (from the **DepthBias** member of [**D3D11\_RASTERIZER\_DESC1**](/windows/desktop/api/D3D11_1/ns-d3d11_1-cd3d11_rasterizer_desc1)) to the z-values that the system uses when rendering the sets of coplanar polygons. Polygons with a larger z value will be drawn in front of polygons with a smaller z value.

There are two options for calculating depth bias.

1.  If the depth buffer currently bound to the output-merger stage has a **UNORM** format or no depth buffer is bound, the bias value is calculated like this:
    ```
    Bias = (float)DepthBias * r + SlopeScaledDepthBias * MaxDepthSlope;
    ```

    

    where *r* is the minimum representable value > 0 in the depth-buffer format converted to **float32**. The **DepthBias** and **SlopeScaledDepthBias** values are [**D3D11\_RASTERIZER\_DESC1**](/windows/desktop/api/D3D11_1/ns-d3d11_1-cd3d11_rasterizer_desc1) structure members. The **MaxDepthSlope** value is the maximum of the horizontal and vertical slopes of the depth value at the pixel.
2.  If a floating-point depth buffer is bound to the output-merger stage the bias value is calculated like this:
    ```
    Bias = (float)DepthBias * 2**(exponent(max z in primitive) - r) +
                SlopeScaledDepthBias * MaxDepthSlope;
    ```

    

    where *r* is the number of mantissa bits in the floating point representation (excluding the hidden bit); for example, 23 for **float32**.

The bias value is then clamped like this:


```
if(DepthBiasClamp > 0)
    Bias = min(DepthBiasClamp, Bias)
else if(DepthBiasClamp < 0)
    Bias = max(DepthBiasClamp, Bias)
```



The bias value is then used to calculate the pixel depth.


```
if ( (DepthBias != 0) || (SlopeScaledDepthBias != 0) )
    z = z + Bias
```



Depth-bias operations occur on vertices after clipping, therefore, depth-bias has no effect on geometric clipping. The bias value is constant for a given primitive and is added to the z value for each vertex before interpolator setup. When you use [feature levels](overviews-direct3d-11-devices-downlevel-intro.md) 10.0 and higher, all bias calculations are performed using 32-bit floating-point arithmetic. Bias is not applied to any point or line primitives, except for lines drawn in wireframe mode.

One of the artifacts with shadow buffer based shadows is shadow acne, or a surface shadowing itself due to minor differences between the depth computation in a shader, and the depth of the same surface in the shadow buffer. One way to alleviate this is to use **DepthBias** and **SlopeScaledDepthBias** when rendering a shadow buffer. The idea is to push surfaces out enough while rendering a shadow buffer so that the comparison result (between the shadow buffer z and the shader z) is consistent across the surface, and avoid local self-shadowing.

However, using **DepthBias** and **SlopeScaledDepthBias** can introduce new rendering problems when a polygon viewed at an extremely sharp angle causes the bias equation to generate a very large z value. This in effect pushes the polygon extremely far away from the original surface in the shadow map. One way to help alleviate this particular problem is to use **DepthBiasClamp**, which provides an upper bound (positive or negative) on the magnitude of the z bias calculated.

> [!Note]  
> For [feature levels](overviews-direct3d-11-devices-downlevel-intro.md) 9.1, 9.2, 9.3, **DepthBiasClamp** is not supported.

 

## Related topics

<dl> <dt>

[Output-Merger Stage](d3d10-graphics-programming-guide-output-merger-stage.md)
</dt> </dl>

 

 




