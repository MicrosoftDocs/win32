---
Description: 'Retrieves the blend factor and vertex affected by a specified bone influence.'
ms.assetid: 'bbed4766-e571-4a9e-b7e3-047052470cbe'
title: 'ID3DXSkinInfo::GetBoneVertexInfluence method'
---

# ID3DXSkinInfo::GetBoneVertexInfluence method

Retrieves the blend factor and vertex affected by a specified bone influence.

## Syntax


```C++
HRESULT GetBoneVertexInfluence(
  [in]      DWORD boneNum,
  [in]      DWORD influenceNum,
  [in, out] FLOAT *pWeight,
  [in, out] DWORD *pVertexNum
);
```



## Parameters

<dl> <dt>

*boneNum* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Index of the bone. Must be between 0 and the number of bones.

</dd> <dt>

*influenceNum* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Index of the influence array of the specified bone.

</dd> <dt>

*pWeight* \[in, out\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)\***

Pointer to the blend factor influenced by influenceNum.

</dd> <dt>

*pVertexNum* \[in, out\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)\***

Pointer to the vertex influenced by influenceNum.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> <dt>

[**ID3DXSkinInfo::SetBoneVertexInfluence**](id3dxskininfo--setbonevertexinfluence.md)
</dt> <dt>

[**ID3DXSkinInfo::FindBoneVertexInfluenceIndex**](id3dxskininfo--findbonevertexinfluenceindex.md)
</dt> <dt>

[**ID3DXSkinInfo::GetBoneInfluence**](id3dxskininfo--getboneinfluence.md)
</dt> </dl>

 

 




