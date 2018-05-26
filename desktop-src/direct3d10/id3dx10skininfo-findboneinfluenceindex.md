---
Description: Find the index that indicates where a given vertex is in a given bones list of influenced vertices.
ms.assetid: 81522848-ae66-446f-990b-832123a2e175
title: ID3DX10SkinInfoFindBoneInfluenceIndex method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **[**UINT**](winprog.windows_data_types)**

An index that specifies an existing bone. Must be between 0 and the value returned by [**ID3DX10SkinInfo::GetNumBones**](id3dx10skininfo-getnumbones.md).

</dd> <dt>

*VertexIndex* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The index of the vertex in the vertex buffer.

</dd> <dt>

*pInfluenceIndex* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)\***

The index of the vertex in the bone's list of influenced vertices.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be: E\_INVALIDARG.

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

 

 




