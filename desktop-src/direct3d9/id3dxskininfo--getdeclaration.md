---
Description: 'Gets the vertex declaration.'
ms.assetid: '49738e9b-09cb-489f-b9af-32d220fbede8'
title: 'ID3DXSkinInfo::GetDeclaration method'
---

# ID3DXSkinInfo::GetDeclaration method

Gets the vertex declaration.

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

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> <dt>

[**ID3DXSkinInfo::SetDeclaration**](id3dxskininfo--setdeclaration.md)
</dt> </dl>

 

 




