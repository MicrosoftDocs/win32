---
Description: 'Clear a bone''s list of vertices that it influences.'
ms.assetid: '1ba6f43a-1f85-4057-b0ed-247cc38d4932'
title: 'ID3DX10SkinInfo::ClearBoneInfluences method'
---

# ID3DX10SkinInfo::ClearBoneInfluences method

Clear a bone's list of vertices that it influences.

## Syntax


```C++
HRESULT ClearBoneInfluences(
  [in] UINT BoneIndex
);
```



## Parameters

<dl> <dt>

*BoneIndex* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

An index that specifies an existing bone. Must be between 0 and the value returned by [**ID3DX10SkinInfo::GetNumBones**](id3dx10skininfo-getnumbones.md).

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

 

 




