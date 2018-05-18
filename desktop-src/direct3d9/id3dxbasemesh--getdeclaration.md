---
Description: 'Retrieves a declaration describing the vertices in the mesh.'
ms.assetid: 'e9028282-acf1-4ca4-8af0-7fb655dcb5d1'
title: 'ID3DXBaseMesh::GetDeclaration method'
---

# ID3DXBaseMesh::GetDeclaration method

Retrieves a declaration describing the vertices in the mesh.

## Syntax


```C++
HRESULT GetDeclaration(
  [in, out] D3DVERTEXELEMENT9 Declaration
);
```



## Parameters

<dl> <dt>

*Declaration* \[in, out\]
</dt> <dd>

Type: **[**D3DVERTEXELEMENT9**](d3dvertexelement9.md)**

Array of [**D3DVERTEXELEMENT9**](d3dvertexelement9.md) elements describing the vertex format of the mesh vertices. The upper limit of this declarator array is [**MAX\_FVF\_DECL\_SIZE**](direct3d9.max_fvf_decl_size). The vertex element array ends with the [**D3DDECL\_END**](d3ddecl-end.md) macro.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

The array of elements includes the [**D3DDECL\_END**](d3ddecl-end.md) macro, which ends the declaration.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXBaseMesh](id3dxbasemesh.md)
</dt> </dl>

 

 




