---
description: Get the number of vertices that a given bone influences.
ms.assetid: e92361ea-4269-4d63-a8d1-560a486b6563
title: ID3DX10SkinInfo::GetBoneInfluenceCount method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10SkinInfo.GetBoneInfluenceCount
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10SkinInfo::GetBoneInfluenceCount method

Get the number of vertices that a given bone influences.

## Syntax


```C++
UINT GetBoneInfluenceCount(
  [in] UINT BoneIndex
);
```



## Parameters

<dl> <dt>

*BoneIndex* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

An index that specifies an existing bone. Must be between 0 and the value returned by [**ID3DX10SkinInfo::GetNumBones**](id3dx10skininfo-getnumbones.md).

</dd> </dl>

## Return value

Type: **[**UINT**](../winprog/windows-data-types.md)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be: E\_INVALIDARG.

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

 

 
