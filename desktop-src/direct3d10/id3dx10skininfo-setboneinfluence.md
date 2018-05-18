---
Description: 'Set the amount of influence a given bone has over a given vertex.'
ms.assetid: 'adbdc784-c6b4-4e10-85c8-5e0b794d946f'
title: 'ID3DX10SkinInfo::SetBoneInfluence method'
---

# ID3DX10SkinInfo::SetBoneInfluence method

Set the amount of influence a given bone has over a given vertex.

## Syntax


```C++
HRESULT SetBoneInfluence(
  [in] UINT  BoneIndex,
  [in] UINT  InfluenceIndex,
  [in] float Weight
);
```



## Parameters

<dl> <dt>

*BoneIndex* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

An index that specifies an existing bone. Must be between 0 and the value returned by [**ID3DX10SkinInfo::GetNumBones**](id3dx10skininfo-getnumbones.md).

</dd> <dt>

*InfluenceIndex* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

An index into the bone's list of vertices that it influences.

</dd> <dt>

*Weight* \[in\]
</dt> <dd>

Type: **float**

The amount of influence, between 0 and 1, that the bone has over the vertex.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be E\_INVALIDARG.

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

 

 




