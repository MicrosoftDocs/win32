---
Description: Get a list of vertices that a given bone influences and a list of the amount of influence that bone has on each vertex.
ms.assetid: d1dea694-874d-4f21-87a8-f6b013617544
title: ID3DX10SkinInfoGetBoneInfluences method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DX10SkinInfo::GetBoneInfluences method

Get a list of vertices that a given bone influences and a list of the amount of influence that bone has on each vertex.

## Syntax


```C++
HRESULT GetBoneInfluences(
  [in]      UINT  BoneIndex,
  [in]      UINT  Offset,
  [in]      UINT  Count,
  [in, out] UINT  *pDestIndices,
  [in, out] float *pDestWeights
);
```



## Parameters

<dl> <dt>

*BoneIndex* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

An index that specifies an existing bone. Must be between 0 and the value returned by [**ID3DX10SkinInfo::GetNumBones**](id3dx10skininfo-getnumbones.md).

</dd> <dt>

*Offset* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

An offset from the top of the bone's list of influenced vertices. This must be between 0 and the value returned by [**ID3DX10SkinInfo::GetBoneInfluenceCount**](id3dx10skininfo-getboneinfluencecount.md).

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The number of indices and weights to retrieve. Must be between 0 and the value returned by ID3DX10SkinInfo::GetBoneInfluenceCount.

</dd> <dt>

*pDestIndices* \[in, out\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)\***

A list of indices into the vertex buffer, each one representing a vertex influenced by the bone. These values correspond to the values in pDestWeights, such that pDestIndices\[i\] corresponds to pDestWeights\[i\].

</dd> <dt>

*pDestWeights* \[in, out\]
</dt> <dd>

Type: **float\***

A list of the amount of influence the bone has on each vertex. These values correspond to the values in pDestIndices, such that pDestWeights\[i\] corresponds to pDestIndices\[i\].f

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be: E\_INVALIDARG or E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10SkinInfo](id3dx10skininfo.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




