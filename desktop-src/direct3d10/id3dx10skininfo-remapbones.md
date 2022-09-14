---
description: Change which bones influence which vertices.
ms.assetid: 0955e0ba-ffc5-408b-ab38-2abd39e1c429
title: ID3DX10SkinInfo::RemapBones method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10SkinInfo.RemapBones
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10SkinInfo::RemapBones method

Change which bones influence which vertices.

## Syntax


```C++
HRESULT RemapBones(
  [in] UINT NewBoneCount,
  [in] UINT *pBoneRemap
);
```



## Parameters

<dl> <dt>

*NewBoneCount* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The new number of bones.

</dd> <dt>

*pBoneRemap* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

A pointer to an array of bone indices, which describe the remapping. For example, say SkinInfo contains some bones such that bone0 is mapped to v0, bone1 to v1, and bone2 to v2, and array with 2,1,0 is specified for pBoneRemap. This will cause bone0 to be mapped to v2, bone1 to v1, and bone2 to v0.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be: E\_OUTOFMEMORY or E\_INVALIDARG.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10SkinInfo](id3dx10skininfo.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
