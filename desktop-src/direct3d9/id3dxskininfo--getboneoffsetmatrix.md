---
Description: 'Gets the bone offset matrix.'
ms.assetid: '99d47635-ffae-4668-a37c-b15442148fa1'
title: 'ID3DXSkinInfo::GetBoneOffsetMatrix method'
---

# ID3DXSkinInfo::GetBoneOffsetMatrix method

Gets the bone offset matrix.

## Syntax


```C++
LPD3DXMATRIX GetBoneOffsetMatrix(
  [in] DWORD Bone
);
```



## Parameters

<dl> <dt>

*Bone* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Bone number.

</dd> </dl>

## Return value

Type: **[**LPD3DXMATRIX**](d3dxmatrix.md)**

Returns a pointer to the bone offset matrix. Do not free this pointer.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> <dt>

[**SetBoneOffsetMatrix**](id3dxskininfo--setboneoffsetmatrix.md)
</dt> <dt>

[**GetNumBones**](id3dxskininfo--getnumbones.md)
</dt> </dl>

 

 




