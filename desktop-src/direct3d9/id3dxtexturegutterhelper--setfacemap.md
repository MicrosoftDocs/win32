---
description: Sets the index of the mesh face to which each texel belongs.
ms.assetid: 45d931bc-fb8b-48da-b30d-99d5dc183494
title: ID3DXTextureGutterHelper::SetFaceMap method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXTextureGutterHelper.SetFaceMap
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXTextureGutterHelper::SetFaceMap method

Sets the index of the mesh face to which each texel belongs.

## Syntax


```C++
HRESULT SetFaceMap(
  [in] UINT *pFaceData
);
```



## Parameters

<dl> <dt>

*pFaceData* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Pointer to the index of the mesh face to which each texel belongs.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Remarks

The mesh face data input to this method is valid only for valid (non-class 0) texels. [**ID3DXTextureGutterHelper::GetGutterMap**](id3dxtexturegutterhelper--getguttermap.md) will return non-zero values for valid texels.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXTextureGutterHelper](id3dxtexturegutterhelper.md)
</dt> </dl>

 

 
