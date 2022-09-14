---
description: Gets the handle of an annotation by looking up its name.
ms.assetid: da4e2805-5f06-4a9b-836f-85a8c154c502
title: ID3DXBaseEffect::GetAnnotationByName method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseEffect.GetAnnotationByName
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXBaseEffect::GetAnnotationByName method

Gets the handle of an annotation by looking up its name.

## Syntax


```C++
D3DXHANDLE GetAnnotationByName(
  [in] D3DXHANDLE hObject,
  [in] LPCSTR     pName
);
```



## Parameters

<dl> <dt>

*hObject* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Handle of a technique, pass, or top-level parameter. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

String containing the annotation name.

</dd> </dl>

## Return value

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Returns the handle of the specified annotation, or **NULL** if the name was not found. See [Handles (Direct3D 9)](handles.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> </dl>

 

 
