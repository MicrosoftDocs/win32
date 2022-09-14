---
description: Primitives that have no textures are rendered with the color specified by their material, or with the colors specified for the vertices, if any.
ms.assetid: 8a7ed4b1-25a1-4984-baea-6e176f0545ea
title: Outline and Fill State (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Outline and Fill State (Direct3D 9)

Primitives that have no textures are rendered with the color specified by their material, or with the colors specified for the vertices, if any. You can select the method to fill them by specifying a value defined by the [**D3DFILLMODE**](./d3dfillmode.md) enumerated type for the D3DRS\_FILLMODE render state.

To enable dithering, your application must pass the D3DRS\_DITHERENABLE enumerated value as the first parameter to [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate). It must set the second parameter to **TRUE** to enable dithering, and **FALSE** to disable it.

At times, drawing the last pixel in a line can cause unsightly overlap with surrounding primitives. You can control this using the D3DRS\_LASTPIXEL enumerated value. However, do not alter this setting without some forethought. Under some conditions, suppressing the rendering of the last pixel can cause unsightly gaps between primitives.

Object outlines can be drawn by setting the appropriate line drawing pattern. The default line drawing state is to draw solid lines. For more information, see [Line Drawing Support in D3DX (Direct3D 9)](line-drawing-support-in-d3dx.md) render state.

## Related topics

<dl> <dt>

[Render States](render-states.md)
</dt> </dl>

 

 
