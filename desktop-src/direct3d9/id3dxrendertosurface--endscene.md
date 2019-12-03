---
Description: Ends a scene.
ms.assetid: f721593e-6cba-4569-8276-6a4ffc0fc37a
title: ID3DXRenderToSurface::EndScene method (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXRenderToSurface.EndScene
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXRenderToSurface::EndScene method

Ends a scene.

## Syntax


```C++
HRESULT EndScene(
  [in] DWORD MipFilter
);
```



## Parameters

<dl> <dt>

*MipFilter* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Filter options, enumerated in [D3DX\_FILTER](d3dx-filter.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXRenderToSurface](id3dxrendertosurface.md)
</dt> <dt>

[**ID3DXRenderToSurface::BeginScene**](id3dxrendertosurface--beginscene.md)
</dt> </dl>

 

 




