---
Description: Sets the minimum bone influence. Influence values smaller than this are ignored.
ms.assetid: 9af19c9e-bb6e-4f93-973f-5c38f88eea3d
title: ID3DXSkinInfoSetMinBoneInfluence method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXSkinInfo::SetMinBoneInfluence method

Sets the minimum bone influence. Influence values smaller than this are ignored.

## Syntax


```C++
HRESULT SetMinBoneInfluence(
  [in] FLOAT MinInfl
);
```



## Parameters

<dl> <dt>

*MinInfl* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Minimum influence value. Influence values smaller than this are ignored.

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

[**ID3DXSkinInfo::GetMinBoneInfluence**](id3dxskininfo--getminboneinfluence.md)
</dt> </dl>

 

 




