---
Description: Gets the bone name, from the bone index.
ms.assetid: f56faf41-c119-4cdd-bb8a-86fc99ff5893
title: ID3DXSkinInfo::GetBoneName method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXSkinInfo::GetBoneName method

Gets the bone name, from the bone index.

## Syntax


```C++
LPCSTR GetBoneName(
  [in] DWORD Bone
);
```



## Parameters

<dl> <dt>

*Bone* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Bone number.

</dd> </dl>

## Return value

Type: **[**LPCSTR**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Returns the bone name. Do not free this string.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> <dt>

[**ID3DXSkinInfo::SetBoneName**](id3dxskininfo--setbonename.md)
</dt> <dt>

[**ID3DXSkinInfo::GetNumBones**](id3dxskininfo--getnumbones.md)
</dt> </dl>

 

 




