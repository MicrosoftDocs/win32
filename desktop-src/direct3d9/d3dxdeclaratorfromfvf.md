---
Description: 'Returns a declarator from a flexible vertex format (FVF) code.'
ms.assetid: '0272239c-0873-4a5c-b046-541f4ba603f4'
title: D3DXDeclaratorFromFVF function
---

# D3DXDeclaratorFromFVF function

Returns a declarator from a flexible vertex format (FVF) code.

## Syntax


```C++
HRESULT D3DXDeclaratorFromFVF(
  _In_    DWORD             FVF,
  _Inout_ D3DVERTEXELEMENT9 Declaration
);
```



## Parameters

<dl> <dt>

*FVF* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Combination of [D3DFVF](d3dfvf.md) that describes the FVF from which to generate the returned declarator array.

</dd> <dt>

*Declaration* \[in, out\]
</dt> <dd>

Type: **[**D3DVERTEXELEMENT9**](d3dvertexelement9.md)**

An array of [**D3DVERTEXELEMENT9**](d3dvertexelement9.md) elements describing the vertex format of the mesh vertices. The upper limit of this declarator array is [**MAX\_FVF\_DECL\_SIZE**](direct3d9.max_fvf_decl_size).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DXERR\_INVALIDMESH.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> <dt>

[**D3DXFVFFromDeclarator**](d3dxfvffromdeclarator.md)
</dt> </dl>

 

 




