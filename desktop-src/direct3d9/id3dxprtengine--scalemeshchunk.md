---
Description: 'Scales all the samples associated with a given submesh. The method is useful for computing subsurface scattering.'
ms.assetid: 'abb9ca6a-5fc2-4986-8a38-29998fe5e537'
title: 'ID3DXPRTEngine::ScaleMeshChunk method'
---

# ID3DXPRTEngine::ScaleMeshChunk method

Scales all the samples associated with a given submesh. The method is useful for computing subsurface scattering.

## Syntax


```C++
HRESULT ScaleMeshChunk(
  [in]      UINT            uMeshChunk,
  [in]      FLOAT           fScale,
  [in, out] LPD3DXPRTBUFFER pDataOut
);
```



## Parameters

<dl> <dt>

*uMeshChunk* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Location in the mesh at which to start scaling samples.

</dd> <dt>

*fScale* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Value by which to multiply each vector in the submesh.

</dd> <dt>

*pDataOut* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to a [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object to receive rescaled samples in the submesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> </dl>

 

 




