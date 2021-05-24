---
description: 'The following flags are used to specify sprite rendering options to the flags parameter in the Begin method:'
ms.assetid: 195ee969-30e8-4828-a0be-f0d2a82e247c
title: D3DXSPRITE
ms.topic: article
ms.date: 05/31/2018
---

# D3DXSPRITE

The following flags are used to specify sprite rendering options to the flags parameter in the [**Begin**](id3dxsprite--begin.md) method:



| \#define                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DXSPRITE\_DONOTSAVESTATE           | The device state is not to be saved or restored when [**Begin**](id3dxsprite--begin.md) or [**End**](id3dxsprite--end.md) is called.                                                                                                                                                                                                                                                                                            |
| D3DXSPRITE\_DONOTMODIFY\_RENDERSTATE | The device render state is not to be changed when [**Begin**](id3dxsprite--begin.md) is called. The device is assumed to be in a valid state to draw vertices containing UsageIndex = 0 in the D3DDECLUSAGE\_POSITION, D3DDECLUSAGE\_TEXCOORD, and D3DDECLUSAGE\_COLOR data.                                                                                                                                                     |
| D3DXSPRITE\_OBJECTSPACE              | The world, view, and projection transforms are not modified. The transforms currently set to the device are used to transform the sprites when the batched sprites are drawn (when [**Flush**](id3dxsprite--flush.md) or [**End**](id3dxsprite--end.md) is called). If this flag is not specified, then world, view, and projection transforms are modified so that sprites are drawn in screen-space coordinates.              |
| D3DXSPRITE\_BILLBOARD                | Each sprite will be rotated about its center so that it is facing the viewer. [**SetWorldViewLH**](id3dxsprite--setworldviewlh.md) or [**SetWorldViewRH**](id3dxsprite--setworldviewrh.md) must be called first.                                                                                                                                                                                                                |
| D3DXSPRITE\_ALPHABLEND               | Enables alpha blending with D3DRS\_ALPHATESTENABLE set to **TRUE** (for nonzero alpha). D3DBLEND\_SRCALPHA will be the source blend state, and D3DBLEND\_INVSRCALPHA will be the destination blend state in calls to [**SetRenderState**](/windows/desktop/api). See [Alpha Blending State (Direct3D 9)](alpha-blending-state.md). [**ID3DXFont**](id3dxfont.md) expects this flag to be set when drawing text. |
| D3DXSPRITE\_SORT\_TEXTURE            | Sort sprites by texture prior to drawing. This can improve performance when drawing non-overlapping sprites of uniform depth. You may also combine D3DXSPRITE\_SORT\_TEXTURE with either D3DXSPRITE\_SORT\_DEPTH\_FRONTTOBACK or D3DXSPRITE\_SORT\_DEPTH\_BACKTOFRONT. This will sort the list of sprites by depth first and texture second.<br/>                                                                           |
| D3DXSPRITE\_SORT\_DEPTH\_FRONTTOBACK | Sprites are sorted by depth in front-to-back order prior to drawing. This procedure is recommended when drawing opaque sprites of varying depths. You may combine D3DXSPRITE\_SORT\_DEPTH\_FRONTTOBACK with D3DXSPRITE\_SORT\_TEXTURE to sort first by depth, and second by texture.<br/>                                                                                                                                   |
| D3DXSPRITE\_SORT\_DEPTH\_BACKTOFRONT | Sprites are sorted by depth in back-to-front order prior to drawing. This procedure is recommended when drawing transparent sprites of varying depths. You may combine D3DXSPRITE\_SORT\_DEPTH\_BACKTOFRONT with D3DXSPRITE\_SORT\_TEXTURE to sort first by depth, and second by texture.<br/>                                                                                                                              |
| D3DXSPRITE\_DO\_NOT\_ADDREF\_TEXTURE | Disables calling AddRef() on every draw, and Release() on Flush() for better performance.                                                                                                                                                                                                                                                                                                                                         |



 

## Constant Information



| Requirement                         | Value            |
|--------------------------|-------------|
| Header                   | d3dx9core.h |
| Minimum operating system | Windows 98  |



 

## Related topics

<dl> <dt>

[D3DX Constants](dx9-graphics-reference-d3dx-constants.md)
</dt> </dl>

 

 




