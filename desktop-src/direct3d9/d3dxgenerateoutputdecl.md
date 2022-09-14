---
description: Generates an output vertex declaration from the input declaration. The output declaration is intended for use by the mesh tessellation functions.
ms.assetid: 528b0da3-fc31-4872-98f2-31e03c1cae5e
title: D3DXGenerateOutputDecl function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXGenerateOutputDecl
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXGenerateOutputDecl function

Generates an output vertex declaration from the input declaration. The output declaration is intended for use by the mesh tessellation functions.

## Syntax


```C++
HRESULT D3DXGenerateOutputDecl(
  _Out_       D3DVERTEXELEMENT9 *pOutput,
  _In_  const D3DVERTEXELEMENT9 *pInput
);
```



## Parameters

<dl> <dt>

*pOutput* \[out\]
</dt> <dd>

Type: **[**D3DVERTEXELEMENT9**](d3dvertexelement9.md)\***

Pointer to the output vertex declaration. See [**D3DVERTEXELEMENT9**](d3dvertexelement9.md).

</dd> <dt>

*pInput* \[in\]
</dt> <dd>

Type: **const [**D3DVERTEXELEMENT9**](d3dvertexelement9.md)\***

Pointer to the input vertex declaration. See [**D3DVERTEXELEMENT9**](d3dvertexelement9.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following values: D3DERR\_INVALIDCALL.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 




