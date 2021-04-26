---
description: Normal maps generation constants.
ms.assetid: edf4c3e4-1af4-43b4-80c7-6fab02575f7b
title: D3DX_NORMALMAP
ms.topic: article
ms.date: 05/31/2018
---

# D3DX\_NORMALMAP

Normal maps generation constants.



| \#define                            | Description                                                                                                                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DX\_NORMALMAP\_MIRROR\_U          | Indicates that pixels off the edge of the texture on the u-axis should be mirrored, not wrapped.                                                                                                   |
| D3DX\_NORMALMAP\_MIRROR\_V          | Indicates that pixels off the edge of the texture on the v-axis should be mirrored, not wrapped.                                                                                                   |
| D3DX\_NORMALMAP\_MIRROR             | Same as specifying D3DX\_NORMALMAP\_MIRROR\_U \| D3DX\_NORMALMAP\_MIRROR\_V.                                                                                                                       |
| D3DX\_NORMALMAP\_INVERTSIGN         | Inverts the direction of each normal.                                                                                                                                                              |
| D3DX\_NORMALMAP\_COMPUTE\_OCCLUSION | Computes the per-pixel occlusion term and encodes it into the alpha. An alpha of 1 means that the pixel is not obscured in any way, and an alpha of 0 means that the pixel is completely obscured. |



 

## Constant Information



|                          |            |
|--------------------------|------------|
| Header                   | d3dx9tex.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[D3DX Constants](dx9-graphics-reference-d3dx-constants.md)
</dt> <dt>

[**D3DXComputeNormalMap**](d3dxcomputenormalmap.md)
</dt> </dl>

 

 



