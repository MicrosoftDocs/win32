---
description: Enable an existing bone to influence a group of vertices and define how much influence the bone has on each vertex.
ms.assetid: 37ba97a8-ba40-4700-b8b8-fa7cc9118307
title: ID3DX10SkinInfo::AddBoneInfluences method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10SkinInfo.AddBoneInfluences
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10SkinInfo::AddBoneInfluences method

Enable an existing bone to influence a group of vertices and define how much influence the bone has on each vertex.

## Syntax


```C++
HRESULT AddBoneInfluences(
  [in] UINT  BoneIndex,
  [in] UINT  InfluenceCount,
  [in] UINT  *pIndices,
  [in] float *pWeights
);
```



## Parameters

<dl> <dt>

*BoneIndex* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

An index that specifies an existing bone. Must be between 0 and the value returned by [**ID3DX10SkinInfo::GetNumBones**](id3dx10skininfo-getnumbones.md).

</dd> <dt>

*InfluenceCount* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of vertices to add to the bone's influence.

</dd> <dt>

*pIndices* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Pointer to an array of vertex indices. Each member of this array has a corresponding member in pWeights, such that pIndices\[i\] corresponds to pWeights\[i\]. The corresponding value in pWeights\[i\] determines how much influence BoneIndex will have on the vertex indexed by pIndices\[i\]. The size of the pIndices array must be equal to or greater than InfluenceCount.

</dd> <dt>

*pWeights* \[in\]
</dt> <dd>

Type: **float\***

Pointer to an array of bone weights. Each member of this array has a corresponding member in pIndices, such that pWeights\[i\] corresponds to pIndices\[i\]. Each value in pWeights is between 0 and 1 and defines the amount of influence the bone has over each vertex. The size of pWeights must be equal to or greater than InfluenceCount.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be: E\_INVALIDARG or E\_OUTOFMEMORY.

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

 

 
