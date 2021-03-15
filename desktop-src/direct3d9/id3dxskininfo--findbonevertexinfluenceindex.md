---
description: Retrieves the index of the bone influence affecting a single vertex.
ms.assetid: 'vs|directx_sdk|~\id3dxskininfo__findbonevertexinfluenceindex.htm'
title: ID3DXSkinInfo::FindBoneVertexInfluenceIndex method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXSkinInfo.FindBoneVertexInfluenceIndex
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSkinInfo::FindBoneVertexInfluenceIndex method

Retrieves the index of the bone influence affecting a single vertex.

## Syntax


```C++
HRESULT FindBoneVertexInfluenceIndex(
  [in]      DWORD boneNum,
  [in]      DWORD vertexNum,
  [in, out] DWORD *pInfluenceIndex
);
```



## Parameters

<dl> <dt>

*boneNum* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Index of the bone. Must be between 0 and the number of bones.

</dd> <dt>

*vertexNum* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Index of the vertex for which the bone influence is to be found. Must be between 0 and the number of vertices in the mesh.

</dd> <dt>

*pInfluenceIndex* \[in, out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Pointer to the index of the bone influence that affects vertexNum.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the specified bone does not influence the given vertex, S\_FALSE is returned. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> <dt>

[**ID3DXSkinInfo::GetBoneVertexInfluence**](id3dxskininfo--getbonevertexinfluence.md)
</dt> <dt>

[**ID3DXSkinInfo::SetBoneVertexInfluence**](id3dxskininfo--setbonevertexinfluence.md)
</dt> <dt>

[**ID3DXSkinInfo::GetBoneInfluence**](id3dxskininfo--getboneinfluence.md)
</dt> </dl>

 

 
