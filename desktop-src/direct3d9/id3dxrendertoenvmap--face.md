---
description: Initiate the drawing of each face of an environment map.
ms.assetid: c100e138-c5a8-49bb-9a91-e7f70410470f
title: ID3DXRenderToEnvMap::Face method (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXRenderToEnvMap.Face
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXRenderToEnvMap::Face method

Initiate the drawing of each face of an environment map.

## Syntax


```C++
HRESULT Face(
  [in] D3DCUBEMAP_FACES Face,
  [in] DWORD            MipFilter
);
```



## Parameters

<dl> <dt>

*Face* \[in\]
</dt> <dd>

Type: **[**D3DCUBEMAP\_FACES**](./d3dcubemap-faces.md)**

The first face of the environmental cube map. See [**D3DCUBEMAP\_FACES**](./d3dcubemap-faces.md).

</dd> <dt>

*MipFilter* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

A valid combination of one or more [D3DX\_FILTER](d3dx-filter.md) flags.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

This method must be called once for each type of environment map. The only exception is a cubic environment map which requires this method to be called six times, once for each face in D3DCUBEMAP\_FACES. For more information, see [Environment Mapping (Direct3D 9)](environment-mapping.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXRenderToEnvMap](id3dxrendertoenvmap.md)
</dt> </dl>

 

 
