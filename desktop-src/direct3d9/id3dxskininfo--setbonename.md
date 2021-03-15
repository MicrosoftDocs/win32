---
description: Sets the bone name.
ms.assetid: 2eecddb8-4efa-41a3-be83-7404047a9857
title: ID3DXSkinInfo::SetBoneName method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXSkinInfo.SetBoneName
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSkinInfo::SetBoneName method

Sets the bone name.

## Syntax


```C++
HRESULT SetBoneName(
  [in] DWORD  Bone,
  [in] LPCSTR pName
);
```



## Parameters

<dl> <dt>

*Bone* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Bone number

</dd> <dt>

*pName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Bone name

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

Bone names are returned by [**D3DXLoadMeshFromXof**](d3dxloadmeshfromxof.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> <dt>

[**ID3DXSkinInfo::GetBoneName**](id3dxskininfo--getbonename.md)
</dt> </dl>

 

 
