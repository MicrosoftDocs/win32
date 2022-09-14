---
description: Returns a flexible vertex format (FVF) code from a declarator.
ms.assetid: 4f30087e-0042-44bc-a7a5-5386b18fcad7
title: D3DXFVFFromDeclarator function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXFVFFromDeclarator
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXFVFFromDeclarator function

Returns a flexible vertex format (FVF) code from a declarator.

## Syntax


```C++
HRESULT D3DXFVFFromDeclarator(
  _In_  const LPD3DVERTEXELEMENT9 *pDeclaration,
  _Out_       DWORD               *pFVF
);
```



## Parameters

<dl> <dt>

*pDeclaration* \[in\]
</dt> <dd>

Type: **const [**LPD3DVERTEXELEMENT9**](d3dvertexelement9.md)\***

Array of [**D3DVERTEXELEMENT9**](d3dvertexelement9.md) elements, describing the FVF code.

</dd> <dt>

*pFVF* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Pointer to a DWORD value, representing the returned combination of [D3DFVF](d3dfvf.md) that describes the vertex format returned from the declarator.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be: D3DERR\_INVALIDCALL.

## Remarks

This function will fail for any declarator that does not map directly to an FVF.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> <dt>

[**D3DXDeclaratorFromFVF**](d3dxdeclaratorfromfvf.md)
</dt> </dl>

 

 
