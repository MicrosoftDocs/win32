---
Description: Sets the influence value for a bone.
ms.assetid: c6dc8a33-8f5c-47d0-8637-a2492b1e3089
title: ID3DXSkinInfoSetBoneInfluence method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXSkinInfo::SetBoneInfluence method

Sets the influence value for a bone.

## Syntax


```C++
HRESULT SetBoneInfluence(
  [in]       DWORD Bone,
  [in]       DWORD numInfluences,
  [in] const DWORD *vertices,
  [in] const FLOAT *weights
);
```



## Parameters

<dl> <dt>

*Bone* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Bone number.

</dd> <dt>

*numInfluences* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Number of influences.

</dd> <dt>

*vertices* \[in\]
</dt> <dd>

Type: **const [**DWORD**](winprog.windows_data_types)\***

The array of vertices influenced by a bone.

</dd> <dt>

*weights* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](winprog.windows_data_types)\***

The array of weights influenced by a bone.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> <dt>

[**ID3DXSkinInfo::GetBoneInfluence**](id3dxskininfo--getboneinfluence.md)
</dt> <dt>

[**ID3DXSkinInfo::GetNumBoneInfluences**](id3dxskininfo--getnumboneinfluences.md)
</dt> </dl>

 

 




