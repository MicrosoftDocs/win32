---
Description: Restore all render targets and, if needed, compose all the rendered faces into the environment map surface.
ms.assetid: 57c73787-36e7-4088-b5ff-78894e3a5d90
title: ID3DXRenderToEnvMapEnd method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXRenderToEnvMap::End method

Restore all render targets and, if needed, compose all the rendered faces into the environment map surface.

## Syntax


```C++
HRESULT End(
  [in] DWORD MipFilter
);
```



## Parameters

<dl> <dt>

*MipFilter* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

A valid combination of one or more [D3DX\_FILTER](d3dx-filter.md) flags.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXRenderToEnvMap](id3dxrendertoenvmap.md)
</dt> <dt>

[**ID3DXRenderToEnvMap::Face**](id3dxrendertoenvmap--face.md)
</dt> </dl>

 

 




