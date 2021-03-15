---
description: Gets the fixed function vertex value.
ms.assetid: 9b80c4b9-2e5b-4965-99b9-ad6c459ef413
title: ID3DXSkinInfo::GetFVF method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXSkinInfo.GetFVF
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSkinInfo::GetFVF method

Gets the fixed function vertex value.

## Syntax


```C++
DWORD GetFVF();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Returns the flexible vertex format (FVF) codes.

## Remarks

This method can return 0 if the vertex format cannot be mapped directly to an FVF code. This will occur for a mesh created from a vertex declaration that doesn't have the same order and elements supported by the FVF codes.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> <dt>

[**ID3DXSkinInfo::SetFVF**](id3dxskininfo--setfvf.md)
</dt> </dl>

 

 
