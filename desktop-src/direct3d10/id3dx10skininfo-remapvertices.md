---
Description: Change which vertices are influenced by which bones.
ms.assetid: b0d71f3e-9a2d-469d-808b-2fa768cf14b0
title: ID3DX10SkinInfoRemapVertices method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DX10SkinInfo::RemapVertices method

Change which vertices are influenced by which bones.

## Syntax


```C++
HRESULT RemapVertices(
  [in] UINT NewVertexCount,
  [in] UINT *pVertexRemap
);
```



## Parameters

<dl> <dt>

*NewVertexCount* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The new number of vertices.

</dd> <dt>

*pVertexRemap* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)\***

A pointer to an array of vertex indices, which describe the remapping. For example, say SkinInfo contains some vertices such that bone0 is mapped to v0, bone1 to v1, and bone2 to v2, and array with 2,1,0 is specified for pBoneRemap. This will cause bone0 to be mapped to v2, bone1 to v1, and bone2 to v0.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be: E\_OUTOFMEMORY or E\_INVALIDARG.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10SkinInfo](id3dx10skininfo.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




