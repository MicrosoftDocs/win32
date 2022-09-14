---
description: Retrieves the parameters of the render surface.
ms.assetid: 4f46a4c6-7c50-479c-b2f5-24edff590c57
title: ID3DXRenderToSurface::GetDesc method (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXRenderToSurface.GetDesc
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXRenderToSurface::GetDesc method

Retrieves the parameters of the render surface.

## Syntax


```C++
HRESULT GetDesc(
  [out] D3DXRTS_DESC *pParameters
);
```



## Parameters

<dl> <dt>

*pParameters* \[out\]
</dt> <dd>

Type: **[**D3DXRTS\_DESC**](d3dxrts-desc.md)\***

Pointer to a [**D3DXRTS\_DESC**](d3dxrts-desc.md) structure, describing the parameters of the render surface.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXRenderToSurface](id3dxrendertosurface.md)
</dt> </dl>

 

 




