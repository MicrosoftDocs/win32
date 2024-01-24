---
description: Extracts coefficient data from a single-channel buffer and adds the data to an ID3DXMesh object.
ms.assetid: 4fada987-ddd7-4c02-a177-dd81f3790588
title: ID3DXPRTBuffer::ExtractToMesh method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTBuffer.ExtractToMesh
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTBuffer::ExtractToMesh method

Extracts coefficient data from a single-channel buffer and adds the data to an [**ID3DXMesh**](id3dxmesh.md) object.

## Syntax


```C++
HRESULT ExtractToMesh(
  [in] UINT         NumCoefficients,
  [in] D3DDECLUSAGE Usage,
  [in] UINT         UsageIndexStart,
  [in] LPD3DXMESH   pScene
);
```



## Parameters

<dl> <dt>

*NumCoefficients* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of coefficients to extract from the buffer. When using spherical harmonic (SH) precomputed radiance transfer (PRT), the number of coefficients should be Order ². Order must be in the range of [D3DXSH\_MINORDER](other-d3dx-constants.md) to D3DXSH\_MAXORDER, inclusive.

</dd> <dt>

*Usage* \[in\]
</dt> <dd>

Type: **[**D3DDECLUSAGE**](./d3ddeclusage.md)**

Vertex usage descriptions of the mesh. See [**D3DDECLUSAGE**](./d3ddeclusage.md).

</dd> <dt>

*UsageIndexStart* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Starting index for coefficients to be stored in the mesh.

</dd> <dt>

*pScene* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to an [**ID3DXMesh**](id3dxmesh.md) mesh object that will store coefficients.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTBuffer](id3dxprtbuffer.md)
</dt> </dl>

 

 
