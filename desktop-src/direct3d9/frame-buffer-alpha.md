---
description: Frame buffer alpha-blending is a bit different than vertex alpha, material alpha, and texture alpha.
ms.assetid: 3664215d-ad03-400e-beab-b0421cf6b693
title: Frame Buffer Alpha (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Frame Buffer Alpha (Direct3D 9)

Frame buffer alpha-blending is a bit different than vertex alpha, material alpha, and texture alpha. Vertex, material, and texture alpha set transparency values that are used only for the current primitive, and by themselves have no effect on other primitives. Frame buffer alpha-blending controls how the current primitive is combined with existing pixels in the frame buffer to yield a final pixel color.

When performing alpha blending, two colors are being combined: a source color and a destination color. The source color is from the transparent object, the destination color is the color already at the pixel location. The destination color is the result of rendering some other object that is behind the transparent object, that is, the object that will be visible through the transparent object. Alpha blending uses a formula to control the ratio between the source and destination objects.


```
Final Color = ObjectColor * SourceBlendFactor + PixelColor * DestinationBlendFactor 
```



ObjectColor is the contribution from the primitive being rendered at the current pixel location. PixelColor is the contribution from the frame buffer at the current pixel location.

The set of alpha blend factors that can be used are listed below.



| Blend mode factor         | Description                                                                                                                                                                              |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DBLEND\_ZERO            | (0, 0, 0, 0)                                                                                                                                                                             |
| D3DBLEND\_ONE             | (1, 1, 1, 1)                                                                                                                                                                             |
| D3DBLEND\_SRCCOLOR        | (Rs, Gs, Bs, As)                                                                                                                                                                         |
| D3DBLEND\_INVSRCCOLOR     | (1-Rs, 1-Gs, 1-Bs, 1-As)                                                                                                                                                                 |
| D3DBLEND\_SRCALPHA        | (As, As, As, As)                                                                                                                                                                         |
| D3DBLEND\_INVSRCALPHA     | (1-As, 1-As, 1-As, 1-As)                                                                                                                                                                 |
| D3DBLEND\_DESTALPHA       | (Ad, Ad, Ad, Ad)                                                                                                                                                                         |
| D3DBLEND\_INVDESTALPHA    | (1-Ad, 1-Ad, 1-Ad, 1-Ad)                                                                                                                                                                 |
| D3DBLEND\_DESTCOLOR       | (Rd, Gd, Bd, Ad)                                                                                                                                                                         |
| D3DBLEND\_INVDESTCOLOR    | (1-Rd, 1-Gd, 1-Bd, 1-Ad)                                                                                                                                                                 |
| D3DBLEND\_SRCALPHASAT     | (f, f, f, 1); f = min(As, 1-Ad)                                                                                                                                                          |
| D3DBLEND\_BOTHSRCALPHA    | Obsolete for DirectX 6 and later. You can achieve the same effect by setting the source and destination blend factors to D3DBLEND\_SRCALPHA and D3DBLEND\_INVSRCALPHA in separate calls. |
| D3DBLEND\_BOTHINVSRCALPHA | Obsolete for DirectX 6. You can achieve the same effect by setting the source and destination blend factors to D3DBLEND\_INVSRCALPHA and D3DBLEND\_SRCALPHA in separate calls.           |
| D3DBLEND\_BLENDFACTOR     | Use color.r, color.g, color.b, and color.a obtained from the D3DRS\_BLENDFACTOR setting.                                                                                                 |
| D3DBLEND\_INVBLENDFACTOR  | Use 1-color.r, 1-color.g, 1-color.b, and 1-color.a obtained from the D3DRS\_BLENDFACTOR setting.                                                                                         |



 

Direct3D uses the D3DRS\_ALPHABLENDENABLE render state to enable alpha transparency blending. The type of alpha blending that is done depends on the D3DRS\_SRCBLEND and D3DRS\_DESTBLEND render states. Source and destination blend states are used in pairs. The following code fragment sets the source blend state to D3DBLEND\_SRCCOLOR and the destination blend state to D3DBLEND\_INVSRCCOLOR.


```
// This code fragment assumes that lpD3DDevice is a 
//   valid pointer to a device.

// Enable alpha blending.
lpD3DDevice->SetRenderState(D3DRS_ALPHABLENDENABLE, 
                            TRUE);

// Set the source blend state.
lpD3DDevice->SetRenderState(D3DRS_SRCBLEND, 
                            D3DBLEND_SRCCOLOR);

// Set the destination blend state.
lpD3DDevice->SetRenderState(D3DRS_DESTBLEND, 
                            D3DBLEND_INVSRCCOLOR);
```



This code performs a linear blend between the source color (the color of the primitive being rendered at the current location) and the destination color (the color at the current location in the frame buffer). The resulting appearance is similar to tinted glass in that some of the color of the destination object seems to be transmitted through the source object; the rest of it appears to be absorbed.

Many of these blend factors require alpha values in the texture to operate correctly. Thus, when using vertex or material alpha, the application is restricted as to which modes will produce interesting results.

## Related topics

<dl> <dt>

[Alpha Blending](alpha-blending.md)
</dt> </dl>

 

 



