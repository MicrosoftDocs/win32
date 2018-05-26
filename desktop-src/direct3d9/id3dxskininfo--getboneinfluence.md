---
Description: Gets the vertices and weights that a bone influences.
ms.assetid: 84cb064b-b6b2-402d-81cc-8c02de6f8b52
title: ID3DXSkinInfoGetBoneInfluence method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXSkinInfo::GetBoneInfluence method

Gets the vertices and weights that a bone influences.

## Syntax


```C++
HRESULT GetBoneInfluence(
  [in]      DWORD Bone,
  [in, out] DWORD *vertices,
  [in, out] FLOAT *weights
);
```



## Parameters

<dl> <dt>

*Bone* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Bone number.

</dd> <dt>

*vertices* \[in, out\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)\***

Get the array of vertices influenced by a bone.

</dd> <dt>

*weights* \[in, out\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)\***

Get the array of weights influenced by a bone.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

Use [**ID3DXSkinInfo::GetNumBoneInfluences**](id3dxskininfo--getnumboneinfluences.md) to find out how many vertices the bone influences.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> <dt>

[**ID3DXSkinInfo::SetBoneInfluence**](id3dxskininfo--setboneinfluence.md)
</dt> </dl>

 

 




