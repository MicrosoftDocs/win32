---
description: This table maps members of a D3DVERTEXELEMENT9 declaration to a FVF code.
ms.assetid: be4357b5-5b92-44ca-9100-ec9473930446
title: Mapping between a Direct3D Declaration and FVF Codes (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Mapping between a Direct3D Declaration and FVF Codes (Direct3D 9)

This table maps members of a [**D3DVERTEXELEMENT9**](d3dvertexelement9.md) declaration to a FVF code.



| Data type             | Usage                      | Usage index | FVF                       |
|-----------------------|----------------------------|-------------|---------------------------|
| D3DDECLTYPE\_FLOAT3   | D3DDECLUSAGE\_POSITION     | 0           | D3DFVF\_XYZ               |
| D3DDECLTYPE\_FLOAT4   | D3DDECLUSAGE\_POSITIONT    | 0           | D3DFVF\_XYZRHW            |
| D3DDECLTYPE\_FLOATn   | D3DDECLUSAGE\_BLENDWEIGHT  | 0           | D3DFVF\_XYZBn             |
| D3DDECLTYPE\_UBYTE4   | D3DDECLUSAGE\_BLENDINDICES | 0           | D3DFVF\_XYZB (nWeights+1) |
| D3DDECLTYPE\_FLOAT3   | D3DDECLUSAGE\_NORMAL       | 0           | D3DFVF\_NORMAL            |
| D3DDECLTYPE\_FLOAT1   | D3DDECLUSAGE\_PSIZE        | 0           | D3DFVF\_PSIZE             |
| D3DDECLTYPE\_D3DCOLOR | D3DDECLUSAGE\_COLOR        | 0           | D3DFVF\_DIFFUSE           |
| D3DDECLTYPE\_D3DCOLOR | D3DDECLUSAGE\_COLOR        | 1           | D3DFVF\_SPECULAR          |
| D3DDECLTYPE\_FLOATm   | D3DDECLUSAGE\_TEXCOORD     | n           | D3DFVF\_TEXCOORDSIZEm(n)  |
| D3DDECLTYPE\_FLOAT3   | D3DDECLUSAGE\_POSITION     | 1           | N/A                       |
| D3DDECLTYPE\_FLOAT3   | D3DDECLUSAGE\_NORMAL       | 1           | N/A                       |



 

## Related topics

<dl> <dt>

[Vertex Declaration](vertex-declaration.md)
</dt> </dl>

 

 



