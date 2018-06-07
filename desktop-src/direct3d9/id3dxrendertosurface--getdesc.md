---
Description: Retrieves the parameters of the render surface.
ms.assetid: 4f46a4c6-7c50-479c-b2f5-24edff590c57
title: ID3DXRenderToSurface::GetDesc method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXRenderToSurface](id3dxrendertosurface.md)
</dt> </dl>

 

 




