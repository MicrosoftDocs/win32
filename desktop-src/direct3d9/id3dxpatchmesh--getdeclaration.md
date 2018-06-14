---
Description: Gets the vertex declaration.
ms.assetid: 53ff2fb5-68b6-4edd-b48f-e06df306ee3f
title: ID3DXPatchMesh::GetDeclaration method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXPatchMesh::GetDeclaration method

Gets the vertex declaration.

## Syntax


```C++
HRESULT GetDeclaration(
  [out] LPD3DVERTEXELEMENT9 pDeclaration
);
```



## Parameters

<dl> <dt>

*pDeclaration* \[out\]
</dt> <dd>

Type: **[**LPD3DVERTEXELEMENT9**](d3dvertexelement9.md)**

Array of [**D3DVERTEXELEMENT9**](d3dvertexelement9.md) elements describing the vertex format of the mesh vertices. The dimension of this declarator array is [**MAX\_FVF\_DECL\_SIZE**](https://msdn.microsoft.com/en-us/library/Bb147183(v=VS.85).aspx). The vertex element array ends with the [**D3DDECL\_END**](d3ddecl-end.md) macro.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

The array of elements includes the [**D3DDECL\_END**](d3ddecl-end.md) macro, which ends the declaration.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPatchMesh](id3dxpatchmesh.md)
</dt> </dl>

 

 




