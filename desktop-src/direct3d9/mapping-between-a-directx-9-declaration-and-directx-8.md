---
title: Map between D3D9 and D3D8 declarations
description: This table maps members of a D3DVERTEXELEMENT9 declaration to a Direct3D 8 declaration.
ms.assetid: da02b2cd-5221-4d37-97d5-840df91e39a6
ms.topic: article
ms.date: 05/31/2018
---

# Map between D3D9 and D3D8 declarations

This table maps members of a [**D3DVERTEXELEMENT9**](d3dvertexelement9.md) declaration to a Direct3D 8 declaration.



| Direct3D 9 Usage           | Direct3D 9 Usage index | Direct3D 8            |
|----------------------------|------------------------|-----------------------|
| D3DDECLUSAGE\_POSITION     | 0                      | D3DVSDE\_POSITION     |
| D3DDECLUSAGE\_POSITION     | 1                      | D3DVSDE\_POSITION2    |
| D3DDECLUSAGE\_NORMAL       | 0                      | D3DVSDE\_NORMAL       |
| D3DDECLUSAGE\_NORMAL       | 1                      | D3DVSDE\_NORMAL2      |
| D3DDECLUSAGE\_BLENDWEIGHT  | 0                      | D3DVSDE\_BLENDWEIGHT  |
| D3DDECLUSAGE\_BLENDINDICES | 0                      | D3DVSDE\_BLENDINDICES |
| D3DDECLUSAGE\_PSIZE        | 0                      | D3DVSDE\_PSIZE        |
| D3DDECLUSAGE\_COLOR        | 0                      | D3DVSDE\_DIFFUSE      |
| D3DDECLUSAGE\_COLOR        | 1                      | D3DVSDE\_SPECULAR     |
| D3DDECLUSAGE\_TEXCOORD     | n                      | D3DVSDE\_TEXCOORDn    |



 

When a declaration is used with hardware vertex processing on a Direct3D 7 driver, the Direct3D runtime converts it to a FVF with the following rules:

-   Only stream 0 should be used (evident from the MaxStreams cap).
-   The order of vertex elements should be the same as order of FVF bits.
-   Gaps in texture coordinates are not allowed.
-   Any vertex element not described the table cannot be converted into a valid FVF for all pre-DirectX 8 drivers and, hence, cannot be used on those drivers.
-   Only D3DDECLTYPE\_FLOAT2 is allowed for vertex elements with D3DDECLUSAGE\_TEXCOORD if device does not set either of the D3DPTEXTURECAPS\_PROJECTED or D3DPTEXTURECAPS\_CUBEMAP caps.

## Related topics

<dl> <dt>

[Vertex Declaration](vertex-declaration.md)
</dt> </dl>

 

 



