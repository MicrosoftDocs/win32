---
description: The frame buffer blender can now blend alpha channels independent from color-channel blending on render targets. This control is enabled with a new render state, D3DRS\_SEPARATEALPHABLENDENABLE.
ms.assetid: 6d30b13e-f4c6-4bc4-8735-15c398c099f1
title: Render Target Alpha (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Render Target Alpha (Direct3D 9)

The frame buffer blender can now blend alpha channels independent from color-channel blending on render targets. This control is enabled with a new render state, D3DRS\_SEPARATEALPHABLENDENABLE.

When D3DRS\_SEPARATEALPHABLENDENABLE is set to **FALSE** (which is the default condition), the render-target blending factors and operations applied to alpha are the same as those defined for blending color channels. A driver needs to set the D3DPMISCCAPS\_SEPARATEALPHABLEND cap to indicate that it can support render-target alpha blending. Be sure to enable D3DRS\_ALPHABLEND to tell the pipeline that alpha blending is needed.

To control the factors in the alpha channel of the render-target blenders, two new render states are defined as follows:


```
D3DRS_SRCBLENDALPHA 
D3DRS_DESTBLENDALPHA 
```



Like the D3DRS\_SRCBLEND and D3DRS\_DESTBLEND, these can be set to one of the values in the [**D3DBLEND**](./d3dblend.md) enumeration. The source and destination blend settings can be combined in several ways, depending on the settings in the SrcBlendCaps and DestBlendCaps members of [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9).

The alpha blending is done as follows:

renderTargetAlpha = (alpha<sub>in</sub> \* srcBlendOp) BlendOp (alpha<sub>rt</sub> \* destBlendOp)

Where:

-   alpha<sub>in</sub> is the input alpha value.
-   srcBlendOp is one of the blend factors in [**D3DBLEND**](./d3dblend.md).
-   BlendOp is one of the blend factors in [**D3DBLENDOP**](./d3dblendop.md).
-   alpha<sub>rt</sub> is the render-target alpha value.
-   destBlendOp is one of the blend factors in [**D3DBLEND**](./d3dblend.md).
-   renderTargetAlpha is the final blended alpha value.

## Related topics

<dl> <dt>

[Alpha Blending](alpha-blending.md)
</dt> </dl>

 

 
