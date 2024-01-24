---
description: Find the index that indicates where a given vertex is in a given bone's list of influenced vertices.
ms.assetid: 'vs|directx_sdk|~\id3dx10skininfo_findboneinfluenceindex.htm'
title: ID3DX10SkinInfo::FindBoneInfluenceIndex method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10SkinInfo.FindBoneInfluenceIndex
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10SkinInfo::FindBoneInfluenceIndex method

Find the index that indicates where a given vertex is in a given bone's list of influenced vertices.

## Syntax


```C++
HRESULT FindBoneInfluenceIndex(
  [in] UINT BoneIndex,
  [in] UINT VertexIndex,
  [in] UINT *pInfluenceIndex
);
```



## Parameters

<dl> <dt>

*BoneIndex* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

An index that specifies an existing bone. Must be between 0 and the value returned by [**ID3DX10SkinInfo::GetNumBones**](id3dx10skininfo-getnumbones.md).

</dd> <dt>

*VertexIndex* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The index of the vertex in the vertex buffer.

</dd> <dt>

*pInfluenceIndex* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

The index of the vertex in the bone's list of influenced vertices.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

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

 

 
