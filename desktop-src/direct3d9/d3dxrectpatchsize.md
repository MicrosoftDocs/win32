---
Description: Gets the size of the rectangle patch.
ms.assetid: d25373ef-789d-4515-83da-7049f040c9a4
title: D3DXRectPatchSize function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXRectPatchSize function

Gets the size of the rectangle patch.

## Syntax


```C++
HRESULT D3DXRectPatchSize(
  _In_  const FLOAT *pfNumSegs,
  _Out_       DWORD *pdwTriangles,
  _Out_       DWORD *pwdVertices
);
```



## Parameters

<dl> <dt>

*pfNumSegs* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](winprog.windows_data_types)\***

Number of segments per edge to tessellate.

</dd> <dt>

*pdwTriangles* \[out\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)\***

Pointer to a DWORD that contains the number of triangles in the patch.

</dd> <dt>

*pwdVertices* \[out\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)\***

Pointer to a DWORD that contains the number of vertices in the patch.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> <dt>

[**D3DXTessellateRectPatch**](d3dxtessellaterectpatch.md)
</dt> </dl>

 

 




