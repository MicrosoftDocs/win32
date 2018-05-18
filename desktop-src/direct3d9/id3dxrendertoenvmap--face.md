---
Description: 'Initiate the drawing of each face of an environment map.'
ms.assetid: 'c100e138-c5a8-49bb-9a91-e7f70410470f'
title: 'ID3DXRenderToEnvMap::Face method'
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

Type: **[**D3DCUBEMAP\_FACES**](direct3d9.d3dcubemap_faces)**

The first face of the environmental cube map. See [**D3DCUBEMAP\_FACES**](direct3d9.d3dcubemap_faces).

</dd> <dt>

*MipFilter* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

A valid combination of one or more [D3DX\_FILTER](d3dx-filter.md) flags.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

This method must be called once for each type of environment map. The only exception is a cubic environment map which requires this method to be called six times, once for each face in D3DCUBEMAP\_FACES. For more information, see [Environment Mapping (Direct3D 9)](environment-mapping.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXRenderToEnvMap](id3dxrendertoenvmap.md)
</dt> </dl>

 

 




